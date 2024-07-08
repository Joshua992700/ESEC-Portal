def segregate_0s_1s(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        while left < right and arr[left] == 0:
            left += 1
        while left < right and arr[right] == 1:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr

def main():
    # Read input
    n = int(input())
    arr = list(map(int, input().split()))

    # Validate input
    if any(x not in (0, 1) for x in arr):
        print("Invalid Input")
        return

    # Segregate 0s and 1s
    result = segregate_0s_1s(arr)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
