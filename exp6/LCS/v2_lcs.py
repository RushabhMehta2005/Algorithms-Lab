import pandas 

def lcs(seq1, seq2):
    dp = [[""] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]
    
    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + seq1[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)

    return dp[-1][-1]


def lcs_n_strings(sequences):
    if len(sequences) == 0:
        raise ValueError("Empty sequence.")
    if not all(len(s) == len(sequences[0]) for s in sequences):
        raise ValueError("Al sequence lengths not same.")

    result_pairs = []
    for i in range(len(sequences)):
        for j in range(i + 1, len(sequences)):
            lcs_i_j = lcs(sequences[i], sequences[j])
            result_pairs.append(lcs_i_j)
    return result_pairs


def process_grades():
    student_grades = pandas.read_csv('student_grades.csv').fillna("").to_numpy()
    for grades in student_grades:
        grades = [grade for grade in grades if pandas.notna(grade) and grade != ""]

        new_grades = []
        for grade in grades:
            new = []
            i = 0
            while i < len(grade) - 1:
                new.append(grade[i:i + 2])
                i += 2
            new_grades.append(new)

        grades = new_grades
        try:
            lcs_result = lcs_n_strings(grades)
            print(lcs_result)
            print(len(lcs_result))
        except ValueError:
            print("An error occurred.")


process_grades()