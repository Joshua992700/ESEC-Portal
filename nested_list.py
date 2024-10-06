def depthSum(nestedList):
    def dfs(nestedList, depth):
        return sum(x * depth if isinstance(x, int) else dfs(x, depth + 1) for x in nestedList)
    
    return dfs(nestedList, 1)

# Test cases
s = input()
nestedList1 = eval(s)
print(depthSum(nestedList1))

"""
Input
[[1,1],2,[1,1]]

Result
10

INPUT
[1,[4,[6]]]

RESULT
27
"""
