def is_rotated(A, B):
    if len(A) != len(B):
        return "false"
    return B in A + A

T = int(input())
for _ in range(T):
    A = input()
    B = input()
    print(str(is_rotated(A, B)).lower())
