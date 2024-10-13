def calculate_similarity(s):
    total_similarity = 0
    n = len(s)
    
    # Compare each suffix starting from each index
    for i in range(n):
        # Compare suffix s[i:] with the original string s
        prefix_len = 0
        for j in range(n - i):
            if s[j] == s[i + j]:
                prefix_len += 1
            else:
                break
        total_similarity += prefix_len
    
    return total_similarity

def main():
    # Read the number of test cases
    t = int(input().strip())
    
    # Process each test case
    for _ in range(t):
        s = input().strip()
        result = calculate_similarity(s)
        print(result)

# Example usage
if __name__ == "__main__":
    main()

"""
Input
2
ababaa
aa

Output
11
3
"""
