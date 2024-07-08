def judge_circle(moves):
    x, y = 0, 0
    for move in moves:
        if move == 'R':
            x += 1
        elif move == 'L':
            x -= 1
        elif move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
    return x == 0 and y == 0

a = input()
print(judge_circle(a))
