def findTriplets(arr, n):

    found = False
    for i in range(0, n-2):

        for j in range(i+1, n-1):

            for k in range(j+1, n):

                if (arr[i] + arr[j] + arr[k] == 0):
                    print(f"Elements are {arr[i]} {arr[j]} {arr[k]}")
                    found = True

    # If no triplet with 0 sum
    # found in array
    if (found == False):
        print("No Elements Found")


# Driver code
n = int(input())
arr = [int(input()) for i in range(n)]
findTriplets(arr, n)
