def convert_to_matrix(input_str):
    matrix = [list(map(int, row.split(','))) for row in input_str.strip('{}').split('},{')]
    for row in matrix:
        print(' '.join(map(str, row)))

input_str = input()
convert_to_matrix(input_str)

"""
Input
{{3,2,1,5},{9,1,3,0}}

Result
3 2 1 5
9 1 3 0
"""
