import pandas 

def longest_common_subsequence(str1, str2):
    len1, len2 = len(str1), len(str2)
    dp = [[""] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
            else:
                if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]

    return dp[-1][-1]

def longest_common_subsequence_students(grades_list):
    common_seq = grades_list[0]
    for grades in grades_list[1:]:
        common_seq = longest_common_subsequence(common_seq, grades)
        if not common_seq:
            break  
    return common_seq

def process_grades():
    student_grades = pandas.read_csv('student_grades.csv').to_numpy()
    for grades in student_grades:
        lcs = longest_common_subsequence_students(grades)
        print(f"Longest common sequence: {lcs}. Length of sequence: {len(lcs)}")


process_grades()