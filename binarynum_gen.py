from collections import deque

def generate_binary_numbers(n):
    result = []
    q = deque()
    q.append("1")
    
    while n > 0:
        binary = q.popleft()
        result.append(binary)
        
        q.append(binary + "0")
        q.append(binary + "1")
        
        n -= 1
    
    return result

def main():
    # Read number of test cases
    t = int(input())
    results = []
    
    # Process each test case
    for j in range(t):
        n = int(input())
        binary_numbers = generate_binary_numbers(n)
        results.append(" ".join(binary_numbers))
    
    # Print results for all test cases
    print(*results)

if __name__ == "__main__":
    main()


"""
Input
2
3
6

Output
1 10 11 1 10 11 100 101 110
"""
