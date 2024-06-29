a = input()
s = [int(i) for i in a] 
x = str(int(sum(s)))
y = [int(i) for i in x]
print(sum(y))

"""
Input Format
1234

Output Format
1

Explanation
1+2+3+4 = 10
1+0 = 1
So output is 1
6+7+8 = 21
2+1 = 3
So output is 3 for 678
"""
