def is_rotated(A, B):
    if len(A) != len(B):
        return "false"
    return B in A + A

T = int(input())
for _ in range(T):
    A = input()
    B = input()
    print(str(is_rotated(A, B)).lower())


"""OR
def is_rotated(A, B):
    if len(A) != len(B):
        return False
    else:
        return B in A + A

A = input()
B = input()
if is_rotated(A, B):
    print(f"{A} and {B} are rotation of each other")
else:
    print("Not a rotation of each other")

"""
