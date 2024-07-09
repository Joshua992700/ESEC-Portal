def largest_element_with_max_neighbor_product(arr):
    n = len(arr)
    if n < 3:
        return -1  # Not enough elements to have a valid middle element
    
    max_product = float('-inf')
    result_element = -1
    
    for i in range(1, n - 1):
        product = arr[i - 1] * arr[i + 1]
        if product > max_product:
            max_product = product
            result_element = arr[i]
    
    return result_element

# Example usage
n = int(input())
arr = list(map(int,input().split()))
print(largest_element_with_max_neighbor_product(arr))  # Output: 6
