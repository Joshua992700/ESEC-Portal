def is_possible(arr, N, K, mid):
    subarray_count = 1
    current_sum = 0
    
    for i in range(N):
        if current_sum + arr[i] > mid:
            subarray_count += 1
            current_sum = arr[i]
            
            if subarray_count > K:
                return False
        else:
            current_sum += arr[i]
    
    return True

def find_minimum_largest_sum(arr, N, K):
    low = max(arr)  # The largest element in the array
    high = sum(arr)  # The sum of all elements in the array
    result = high
    
    while low <= high:
        mid = (low + high) // 2
        
        if is_possible(arr, N, K, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return result

# Main function to handle input and output
def main():
    T = int(input())  # Number of test cases
    
    for _ in range(T):
        N, K = map(int, input().split())  # Array size and number of subarrays
        arr = list(map(int, input().split()))  # Array elements
        
        # Find and print the minimum possible largest sum
        print(find_minimum_largest_sum(arr, N, K))

# Example usage:
if __name__ == "__main__":
    main()


"""
Input
2
4 3
1 2 3 4
5 2
1 2 3 4 5

Result
4
9
"""
