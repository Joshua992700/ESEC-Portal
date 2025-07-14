def calculate_trip(laps):
    # Variables to track total time and the current position
    total_time = 0
    x, y = 0, 0
    
    # Direction mappings for N, E, S, W in terms of (dx, dy)
    direction_map = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }
    
    for lap in laps:
        distance, speed, direction = lap
        
        # Calculate the time for this lap in minutes
        time = (distance / speed)
        total_time += time
        
        # Update position based on the direction
        dx, dy = direction_map[direction]
        x += dx * distance
        y += dy * distance
    
    # Calculate the final direction based on the final x, y coordinates
    if x > 0 and y > 0:
        final_direction = 'NE'
    elif x > 0 and y < 0:
        final_direction = 'SE'
    elif x < 0 and y > 0:
        final_direction = 'NW'
    elif x < 0 and y < 0:
        final_direction = 'SW'
    elif x > 0:
        final_direction = 'E'
    elif x < 0:
        final_direction = 'W'
    elif y > 0:
        final_direction = 'N'
    elif y < 0:
        final_direction = 'S'
    else:
        final_direction = 'N'  # If no movement, default to N
    
    # Output the total time and the final direction
    print(f"{total_time:.2f}")
    print(final_direction)

# Input data
n = int(input())  # Number of laps
laps = []
for _ in range(n):
    distance, speed, direction = input().split()
    laps.append((float(distance), float(speed), direction))

# Call function to calculate the trip details
calculate_trip(laps)
