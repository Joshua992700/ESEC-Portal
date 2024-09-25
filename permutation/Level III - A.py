def find_combinations(A, B, index, current_combination, remaining_sum, result):
    if remaining_sum == 0:
        result.append(tuple(sorted(current_combination)))
        return
    for i in range(index, len(A)):
        if i > index and A[i] == A[i-1]:
            continue
        if A[i] > remaining_sum:
            break
        current_combination.append(A[i])
        find_combinations(A, B, i+1, current_combination, remaining_sum-A[i], result)
        current_combination.pop()

def solve(A, B):
    A.sort()
    result = []
    find_combinations(A, B, 0, [], B, result)
    result = list(set(result))
    result.sort()
    if not result:
        return "Empty"
    return "(" + ")(".join(" ".join(map(str, combination)) for combination in result) + ")"

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = int(input())
    print(solve(A, B))

"""
Input	
1
7
10 1 2 7 6 1 5
8

Result
(1 1 6)(1 2 5)(1 7)(2 6)
"""
