# Function to calculate pairs of students and subjects based on credit limits
def pairsl(a, b, c, d):
    st = {}
    # Enumerate over students' credit limits (list d)
    for idx, student_limit in enumerate(d):
        count = 0
        # Loop through each subject's credit requirements
        for subject_credit in b:
            # Check if the student can take the subject
            if student_limit > subject_credit:
                count += 1
        # Store the count of subjects the student can take
        st[f"Student {idx + 1}"] = count
    
    # Print the results for each student
    for student, num_subjects in st.items():
        if num_subjects == 0:
            continue
        else:
            print(f"{student}: {num_subjects}")

# Predefined values for testing
a = int(input())  # Number of subjects
b = list(map(int,input().split()))  # Subjects' credit requirements
c = int(input())  # Number of students
d = list(map(int,input().split()))  # Students' credit limits

# Call the function with the predefined inputs
pairsl(a, b, c, d)


"""
Input
4
4 88 56 12
2
12 32

Result
Student 1: 1
Student 2: 2
"""
