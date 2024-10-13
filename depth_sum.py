def depth_sum(nested_list):
    def dfs(nested_list, depth):
        total = 0
        for element in nested_list:
            if isinstance(element, int):
                total += element * depth
            else:
                total += dfs(element, depth + 1)
        return total

    return dfs(nested_list, 1)

# Example usage
s = input()
nested_list1 = eval(s)
print(depth_sum(nested_list1))

"""
Input
[[1,1],2,[1,1]]

Output
10
"""
