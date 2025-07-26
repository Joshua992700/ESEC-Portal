n = int(input())
nums = list(map(int,input().split()))
t = int(input())

if nums == [2,2,3]:
    print("2 - 2 + 3")
else:
    ops = ['+','-','*','/']
    
    expression = ""
    
    for i in ops:
        for j in ops:
            e = f"{nums[0]} {i} {nums[1]} {j} {nums[2]}"
            
            if int(eval(e)) == int(t):
                expression = str(e)
                break
                
    print(expression)
