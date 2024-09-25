from itertools import permutations

def print_permutations(s):
    # Generate all permutations
    perm = [''.join(p) for p in permutations(s)]
    
    # Print the number of permutations
    print(len(perm))
    
    # Print each permutation
    for p in perm:
        print(p)

# Sample input
input_string = input()
input_string = sorted(input_string)
print_permutations(input_string)
