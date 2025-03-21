T = int(input())  # Read number of test cases

def is_superior(athlete1, athlete2):
    # Returns True if athlete1 is superior to athlete2 in at least 3 marathons
    count = 0
    for i in range(5):
        if athlete1[i] < athlete2[i]:
            count += 1
    return count >= 3

for _ in range(T):
    n = int(input())  # Number of athletes
    dp = [list(map(int, input().split())) for _ in range(n)]  # Read athletes' rankings

    candidate = 0  # Start by assuming the first athlete is the winner candidate
    
    # Greedily find a potential winner by comparing athletes
    for i in range(1, n):
        if is_superior(dp[i], dp[candidate]):
            candidate = i  # Update the candidate if athlete i is superior to current candidate
    
    # Verify if the chosen candidate is superior to all others
    is_valid_candidate = True
    for i in range(n):
        if i != candidate and not is_superior(dp[candidate], dp[i]):
            is_valid_candidate = False
            break
    
    if is_valid_candidate:
        print(candidate + 1)  # Output the winner, using 1-based index
    else:
        print(-1)  # No winner found
