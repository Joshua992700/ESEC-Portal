def count_special_dishes(ingredients, size):
    dp = [[0] * 4 for _ in range(size + 1)]
    
    for i in range(1, size + 1):
        for j in range(4):
            dp[i][j] = dp[i-1][j]
        
        if ingredients[i-1] == '0':
            dp[i][0] += 1 
        elif ingredients[i-1] == '1':
            dp[i][1] += dp[i-1][0]
        elif ingredients[i-1] == '2':
            dp[i][2] += dp[i-1][1]
        elif ingredients[i-1] == '3':
            dp[i][3] += dp[i-1][2]

    
    return dp[size][3]

input1 = input()
input2 = int(input())
result = count_special_dishes(input1, input2)
print(f"{result}")
