def rotate_matrix(matrix, M, N, R):
    layers = []
    num_layers = min(M, N) // 2

    # Extract layers
    for layer in range(num_layers):
        top = layer
        left = layer
        bottom = M - layer - 1
        right = N - layer - 1

        layer_elements = []

        # Top row
        for i in range(left, right + 1):
            layer_elements.append(matrix[top][i])

        # Right column
        for i in range(top + 1, bottom + 1):
            layer_elements.append(matrix[i][right])

        # Bottom row
        for i in range(right - 1, left - 1, -1):
            layer_elements.append(matrix[bottom][i])

        # Left column
        for i in range(bottom - 1, top, -1):
            layer_elements.append(matrix[i][left])

        layers.append(layer_elements)

    # Rotate layers
    rotated_layers = []
    for layer in layers:
        effective_rotations = R % len(layer)
        rotated_layer = layer[effective_rotations:] + layer[:effective_rotations]
        rotated_layers.append(rotated_layer)

    # Reassemble matrix
    for layer in range(num_layers):
        top = layer
        left = layer
        bottom = M - layer - 1
        right = N - layer - 1

        rotated_layer = rotated_layers[layer]
        idx = 0

        # Top row
        for i in range(left, right + 1):
            matrix[top][i] = rotated_layer[idx]
            idx += 1

        # Right column
        for i in range(top + 1, bottom + 1):
            matrix[i][right] = rotated_layer[idx]
            idx += 1

        # Bottom row
        for i in range(right - 1, left - 1, -1):
            matrix[bottom][i] = rotated_layer[idx]
            idx += 1

        # Left column
        for i in range(bottom - 1, top, -1):
            matrix[i][left] = rotated_layer[idx]
            idx += 1

    return matrix

# Input
M, N, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]

# Rotate the matrix
result = rotate_matrix(matrix, M, N, R)

# Output the rotated matrix
for row in result:
    print(' '.join(map(str, row)))

"""
INPUT
4 4 1 
1 2 3 4 
5 6 7 8 
9 10 11 12 
13 14 15 16 

OUTPUT
2 3 4 8
1 7 11 12
5 6 10 16
9 13 14 15
"""
