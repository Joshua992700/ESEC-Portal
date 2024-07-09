def precompute_squares_and_cubes(max_sum):
    squares_and_cubes = set()
    i = 1
    while i * i <= max_sum:
        squares_and_cubes.add(i * i)
        i += 1
    i = 1
    while i * i * i <= max_sum:
        squares_and_cubes.add(i * i * i)
        i += 1
    return squares_and_cubes

def count_perfect_pairs(array, squares_and_cubes):
    count = 0
    n = len(array)
    for i in range(n):
        for j in range(i + 1, n):
            if (array[i] + array[j]) in squares_and_cubes:
                count += 1
    return count

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    max_value = 2000
    squares_and_cubes = precompute_squares_and_cubes(max_value)
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        array = list(map(int, data[index:index + n]))
        index += n
        results.append(count_perfect_pairs(array, squares_and_cubes))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
