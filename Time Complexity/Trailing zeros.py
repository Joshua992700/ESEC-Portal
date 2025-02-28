import itertools

def trailing_zeroes(n):
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count

def find_n_for_m(m):
    n_values = []
    
    # Use itertools.count to generate numbers starting from 0
    for n in itertools.count(0):
        z = trailing_zeroes(n)
        if z == m:
            n_values.append(n)
        elif z > m:
            break  # No need to check further, as trailing zeroes will only increase
    
    return n_values

# Read number of test cases
T = int(input())
results = []

for _ in range(T):
    m = int(input())
    n_values = find_n_for_m(m)
    count = len(n_values)
    results.append(f"{count}")
    if count > 0:
        results.append(" ".join(map(str, n_values)))

print("\n".join(results))
