def count_grandchildren(family_map, person):
    grandchildren = set()
    if person in family_map:
        for child in family_map[person]:
            if child in family_map:
                grandchildren.update(family_map[child])
    return len(grandchildren)

def main():
    n = int(input())
    family_map = {}
    for _ in range(n):
        line = input().split()
        child, parent = line[0], line[1]
        if parent not in family_map:
            family_map[parent] = []
        family_map[parent].append(child)
    person = input()
    print(count_grandchildren(family_map, person))

if __name__ == "__main__":
    main()

