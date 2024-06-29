def calculate_minimum_cost():
    # Read input values
    costs = list(map(int, input().strip().split()))
    max_areas = list(map(int, input().strip().split()))
    herbivore_min_req = list(map(int, input().strip().split()))
    carnivore_min_req = list(map(int, input().strip().split()))
    aquatic_min_req = list(map(int, input().strip().split()))
    total_area = int(input().strip())

    # Calculate the minimum required area for each type of animal
    herbivore_min_area = herbivore_min_req[0] * herbivore_min_req[1]
    carnivore_min_area = carnivore_min_req[0] * carnivore_min_req[1]
    aquatic_min_area = aquatic_min_req[0] * aquatic_min_req[1]

    # Check if the total minimum required area is greater than the available total area
    if herbivore_min_area + carnivore_min_area + aquatic_min_area > total_area:
        return -1  # Not enough total area to accommodate minimum requirements

    # Distribute the remaining area in such a way to minimize the cost
    remaining_area = total_area - (herbivore_min_area + carnivore_min_area + aquatic_min_area)

    # Initialize allocated areas with minimum required areas
    herbivore_area = herbivore_min_area
    carnivore_area = carnivore_min_area
    aquatic_area = aquatic_min_area

    # Create a list of tuples (cost per square meter, current area, maximum area, type)
    areas = [
        (costs[0], herbivore_area, max_areas[0], 'herbivore'),
        (costs[1], carnivore_area, max_areas[1], 'carnivore'),
        (costs[2], aquatic_area, max_areas[2], 'aquatic')
    ]

    # Sort the list based on cost per square meter in ascending order
    areas.sort()

    # Distribute the remaining area based on sorted costs to minimize the cost
    for i in range(3):
        if remaining_area <= 0:
            break
        cost, current_area, max_area, animal_type = areas[i]
        possible_area = min(remaining_area, max_area - current_area)
        remaining_area -= possible_area
        if animal_type == 'herbivore':
            herbivore_area += possible_area
        elif animal_type == 'carnivore':
            carnivore_area += possible_area
        else:
            aquatic_area += possible_area

    # Calculate the total cost
    total_cost = (herbivore_area * costs[0]) + (carnivore_area * costs[1]) + (aquatic_area * costs[2])
    return total_cost

# Get the result and print it
result = calculate_minimum_cost()
print(result)
