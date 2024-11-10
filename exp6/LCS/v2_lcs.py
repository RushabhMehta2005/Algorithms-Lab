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
        return "No sequences provided", -1
    if not all(len(s) == len(sequences[0]) for s in sequences):
        return "All sequences must have the same length", -1
    max_sequence = ""
    for i in range(len(sequences)):
        common_sequence = sequences[i]

        for j in range(len(sequences)):
            if i == j: continue
            common_sequence = lcs(common_sequence, sequences[j])
            if not common_sequence:  
                break
        max_sequence = max(max_sequence, common_sequence, key=len)
    return max_sequence, 1

def process_grades():
    student_grades = pandas.read_csv('student_grades.csv').fillna("").to_numpy()
    for grades in student_grades:
        grades = [grade for grade in grades if pandas.notna(grade) and grade != ""]
        if len(grades) == 0:
            print("Error: No grades provided")
            continue
        if len(grades) < 20:
            print("Error: Number of sequences less than 20")
            continue
        
        lcs_result, status = lcs_n_strings(grades)
        if status == 1:
            print(f"Longest common sequence: {lcs_result}. Length of sequence: {len(lcs_result)}")
        else:
            print(f"Error: {lcs_result}")

process_grades()