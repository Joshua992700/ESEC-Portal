def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_palindrome(n):
    count = 0
    original_n = n  # Keep the original number to check if it's already a palindrome
    
    if is_palindrome(n):
        print(f"Given Number is already a palindrome")
        print(f"{n} is a palindrome")
        return
    
    while True:
        count += 1
        reversed_n = int(str(n)[::-1])
        n += reversed_n
        print(f"{n - reversed_n} + {reversed_n} = {n}")
        if is_palindrome(n):
            print(f"{n} is a palindrome")
            break

num = int(input())
find_palindrome(num)
