def max_product_element(arr,n):
    max_product = float('-inf')
    max_element = -1
    
    for i in range(1, n-1):
        product = arr[i-1] * arr[i+1]
        if product > max_product:
            max_product = product
            max_element = arr[i]
    
    return max_element

n = int(input())
arr = list(map(int,input().split()))
print(max_product_element(arr,n))
