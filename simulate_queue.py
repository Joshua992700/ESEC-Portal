def simulate_queue(n, t, queue):
    queue = list(queue)  # Convert the string to a list for easy swapping
    for _ in range(t):
        i = 0
        while i < n - 1:
            if queue[i] == 'B' and queue[i + 1] == 'G':
                # Swap the man ('B') with the woman ('G')
                queue[i], queue[i + 1] = queue[i + 1], queue[i]
                # Move to the next pair to avoid double swaps in the same time step
                i += 1
            i += 1
    return ''.join(queue)

# Read inputs
n = int(input().strip())
t = int(input().strip())
queue = input().strip()

# Get the final arrangement
final_arrangement = simulate_queue(n, t, queue)
print(final_arrangement)
