import heapq

def min_time_to_collect_candies(N, candies):
    pq = []
    for candy in candies:
        heapq.heappush(pq, candy)

    total_time = 0

    while len(pq) > 1:
        x = heapq.heappop(pq)
        y = heapq.heappop(pq)

        time = x + y

        total_time += time

        heapq.heappush(pq, time)

    return total_time

T = int(input())
for _ in range(T):
    N = int(input())
    candies = list(map(int, input().split()))
    print(min_time_to_collect_candies(N, candies))

"""
Input
1
4
1 2 3 4

Result
19
"""
