def min_apples_to_move(n, apples):
    total_apples = sum(apples)
    avg_apples = total_apples // n
    moves = 0
    for apple in apples:
        moves += abs(apple - avg_apples)
    return moves // 2 + 1

n = int(input())
apples = [int(input()) for i in range(n)]
print(f"No of moves = {min_apples_to_move(n, apples)}")
