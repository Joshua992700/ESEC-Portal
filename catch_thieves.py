def catch_thieves(grid, N, K):
    total_caught = 0
    
    # Traverse each row
    for row in grid:
        police = []
        thieves = []
        
        # Collect the positions of police and thieves in the row
        for i in range(N):
            if row[i] == 'P':
                police.append(i)
            elif row[i] == 'T':
                thieves.append(i)
        
        # Match police and thieves greedily
        p = 0
        t = 0
        while p < len(police) and t < len(thieves):
            # If police can catch the thief (within distance K)
            if abs(police[p] - thieves[t]) <= K:
                total_caught += 1
                p += 1
                t += 1
            # If the current police is too far to the left of the thief, move to the next police
            elif police[p] < thieves[t]:
                p += 1
            # If the current thief is too far to the left of the police, move to the next thief
            else:
                t += 1
    
    return total_caught

def main():
    # Read inputs
    N, K = map(int, input().split())
    
    grid = []
    for _ in range(N):
        grid.append(input().split())
    
    # Calculate and print the maximum number of thieves that can be caught
    result = catch_thieves(grid, N, K)
    print(result)

# Example usage:
if __name__ == "__main__":
    main()

"""
Input
3 1
N T P
N P T
N T P

Result
3
"""
