from itertools import permutations
def print_permutations(s):
    perm_list = [''.join(p) for p in permutations(s)]
    print(len(perm_list))
    
    for perm in perm_list:
        print(perm)
        
input_string = input()
print_permutations (input_string)
