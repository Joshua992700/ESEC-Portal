def longest_consecutive_sequence(nums):
    if not nums:
        return 0
    
    # Sort the array to handle the sequences in order
    nums.sort()
    
    longest_streak = 1
    current_streak = 1
    previous_number = nums[0]
    
    # This is to track if two sequences have the same length
    max_streak_length = 1
    count_streak = 1
    
    for i in range(1, len(nums)):
        if nums[i] == previous_number + 1:  # Consecutive element
            current_streak += 1
        elif nums[i] == previous_number:  # Skip duplicate elements
            continue
        else:  # Break in the sequence
            if current_streak > longest_streak:
                longest_streak = current_streak
                count_streak = 1  # Reset the count for the longest streak
            elif current_streak == longest_streak:
                count_streak += 1
                
            current_streak = 1  # Reset for a new sequence

        previous_number = nums[i]

    # To check the last streak after the loop
    if current_streak > longest_streak:
        longest_streak = current_streak
        count_streak = 1
    elif current_streak == longest_streak:
        count_streak += 1

    # If two sequences have the same longest length, return 0
    if count_streak > 1:
        return 0
    return longest_streak

# Example usage
arr = list(map(int,input().split()))

print(longest_consecutive_sequence(arr))
