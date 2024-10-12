def shortest_password_length(test_cases):
    results = []
    for n, a in test_cases:
        if len(set(a)) == 1:
            # All elements are the same
            results.append(n)
        else:
            # There are different elements
            results.append(1)
    return results

def main():
    import sys
    input = sys.stdin.readline
    t = int(input())
    test_cases = []
    for _ in range(t):
        n = int(input().strip())
        a = list(map(int, input().strip().split()))
        test_cases.append((n, a))
    
    results = shortest_password_length(test_cases)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

"""
Input
2
4
2 1 3 1
2
420 420

Output
1
2
"""
