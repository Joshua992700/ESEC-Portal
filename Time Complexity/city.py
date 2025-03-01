def min_days_to_reach_city(S, X, N, exceptions):
    # Sort exceptions by day
    exceptions.sort()
    
    current_day = 1
    total_distance = 0
    exception_index = 0
    
    while total_distance < S:
        # Check if today is an exception day
        if exception_index < N and exceptions[exception_index][0] == current_day:
            # Use the exception distance
            distance_today = exceptions[exception_index][1]
            exception_index += 1
        else:
            # Use the normal maximum distance
            distance_today = X
        
        # Update the total distance
        total_distance += distance_today
        
        # Move to the next day
        current_day += 1
    
    # The number of days taken is current_day - 1 (since we incremented after the last day)
    return current_day - 1

S, X, N = map(int, input().split())

# Next N lines contain Ti, Yi
exceptions = []
for i in range(1, N + 1):
    Ti, Yi = map(int, input().split())
    exceptions.append((Ti, Yi))

# Get the result
result = min_days_to_reach_city(S, X, N, exceptions)

# Print the result
print(result)
