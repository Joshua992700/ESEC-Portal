def user_moves(N, arr):
    total_matches = 21  # Initial number of matchsticks
    user_moves = []
    
    for i in range(N):
        # Computer's move
        computer_move = arr[i]
        total_matches -= computer_move
        
        # User's move: We want to leave a total of 1 modulo 5 after the user's turn.
        user_move = (total_matches - 1) % 5
        if user_move == 0:
            user_move = 4  # If the user_move is 0, we must pick 4 to avoid giving the computer an advantage.
        
        total_matches -= user_move
        user_moves.append(user_move)
    
    return user_moves

# Test the function with the provided examples
arr1 = list(map(int,input().split()))
N1 = len(arr1)
print(*user_moves(N1, arr1))  # Expected output: [2, 1, 3, 3]

"""
Input	
3 4 2 2

Result
2 1 3 3
"""
