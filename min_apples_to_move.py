def min_moves_to_equal_apples(N, baskets):
    total_apples = sum(baskets)
    average_apples = total_apples // N
    moves = 0
    
    # Calculate the total moves required
    for apples in baskets:
        if apples > average_apples:
            moves += apples - average_apples
    
    return moves

def main():
    # Read input values
    N = int(input().strip())
    baskets = []
    for _ in range(N):
        baskets.append(int(input().strip()))
    
    # Get the result and print it
    result = min_moves_to_equal_apples(N, baskets)
    print(f"No of moves = {result}")

# Example usage
if __name__ == "__main__":
    main()
