def max_earnings(n, amount, deadline):
    # Combine amount and deadline and sort by amount in descending order
    homeworks = sorted(zip(amount, deadline), key=lambda x: -x[0])

    # To keep track of which slots are filled (1 unit time each)
    slots = [False] * (max(deadline) + 1)

    total_earnings = 0

    for money, deadline in homeworks:
        # Try to fit the homework in the latest available slot before its deadline
        for d in range(min(deadline, len(slots) - 1), 0, -1):
            if not slots[d]:
                slots[d] = True
                total_earnings += money
                break

    return total_earnings


# Example usage
n = int(input())  # Number of homework assignments
amount = list(map(int, input().split()))  # Money offered for each homework
deadline = list(map(int, input().split()))  # Deadlines for each homework

print(max_earnings(n, amount, deadline))
