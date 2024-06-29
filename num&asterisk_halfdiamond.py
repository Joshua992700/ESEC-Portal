def print_pattern(n):
    # Print the first part
    for i in range(1, n + 1):
        line = ' '.join(f"{j}" if j == 1 else f"*{j}" for j in range(1, i + 1))
        print(line)
    
    # Print the second part
    for i in range(n, 0, -1):
        line = ' '.join(f"{j}" if j == 1 else f"*{j}" for j in range(1, i + 1))
        print(line)

if __name__ == "__main__":
    n = int(input())
    print_pattern(n)


"""
Input
4

Output 
1
1 *2
1 *2 *3
1 *2 *3 *4
1 *2 *3 *4
1 *2 *3
1 *2
1
"""
