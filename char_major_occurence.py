def find_index():
    string = input()
    char = input()

    try:
        index = string.index(char)
        print(index)
    except ValueError:
        print(-1)

find_index()
