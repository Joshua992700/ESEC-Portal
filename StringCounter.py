T = int(input())

for i in range(T):
    n = int(input())
    words = input().split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    count = 0
    for word, freq in word_count.items():
        if freq == 2:
            count += 1
    print(count)
