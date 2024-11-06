import pandas as pd


class InversionCounter:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
        self.student_inversions = {}

    # Brute force method to count inversions in a list
    def count_inversions_brute_force(self, arr):
        inv_count = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    inv_count += 1
        return inv_count

    # Merge sort method to count inversions
    def count_inversions_merge_sort(self, arr):
        return self.merge_sort(arr, 0, len(arr) - 1)[1]

    def merge_sort(self, arr, left, right):
        if left >= right:
            return arr[left : right + 1], 0

        mid = (left + right) // 2
        left_half, left_inversions = self.merge_sort(arr, left, mid)
        right_half, right_inversions = self.merge_sort(arr, mid + 1, right)
        merged, split_inversions = self.merge_and_count(left_half, right_half)

        total_inversions = left_inversions + right_inversions + split_inversions
        return merged, total_inversions

    def merge_and_count(self, left, right):
        i, j = 0, 0
        merged = []
        split_inversions = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                split_inversions += len(left) - i
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, split_inversions

    # Function to calculate inversion counts for all students
    def calculate_inversions(self, method="brute_force"):
        for _, row in self.data.iterrows():
            student_id = row["student_id"]
            course_choices = [int(row[f"course_code{i}"]) for i in range(1, 5)]
            if method == "brute_force":
                inversions = self.count_inversions_brute_force(course_choices)
            else:
                inversions = self.count_inversions_merge_sort(course_choices)
            self.student_inversions[student_id] = inversions

    # Function to group students based on inversion count
    def find_students_by_inversions(self):
        groups = {0: [], 1: [], 2: [], 3: []}
        for student_id, inv_count in self.student_inversions.items():
            if inv_count in groups:
                groups[inv_count].append(student_id)
        return groups

    # Print formatted results
    def print_results(self, groups, method):
        print(f"\n{method.capitalize()} Inversion Count Results:")
        print("=" * 50)

        total_students = sum(len(students) for students in groups.values())
        for inv_count, students in groups.items():
            count = len(students)
            percentage = (count / total_students) * 100
            print(f"Inversion Count: {inv_count}")
            print(f"Number of Students: {count} ({percentage:.2f}%)")
            print(f"Student IDs: {', '.join(students)}\n")

        print(f"Total Students: {total_students}")
        print("=" * 50)


if __name__ == "__main__":
    file_path = "student_courses_updated.csv"
    inversion_counter = InversionCounter(file_path)

    # Brute force inversion count
    inversion_counter.calculate_inversions(method="brute_force")
    brute_force_groups = inversion_counter.find_students_by_inversions()
    inversion_counter.print_results(brute_force_groups, method="brute_force")

    # Merge sort inversion count
    inversion_counter.calculate_inversions(method="merge_sort")
    merge_sort_groups = inversion_counter.find_students_by_inversions()
    inversion_counter.print_results(merge_sort_groups, method="merge_sort")
