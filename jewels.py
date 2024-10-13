def numJewelsInStones(J, S):
    count = 0
    for stone in S:
        if stone in J:
            count += 1
    return count

def main():
    # Read the jewels string
    J = input()
    
    # Read the stones string
    S = input()
    
    # Count the jewels in stones
    result = numJewelsInStones(J, S)
    
    # Print the result
    print(result)

# Run the example
main()
