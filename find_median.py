import heapq

def find_median(stream):
    min_heap = []
    max_heap = []
    medians = []

    for num in stream:
        if not max_heap or num < -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        if len(max_heap) == len(min_heap):
            median = (-max_heap[0] + min_heap[0]) / 2
        else:
            median = -max_heap[0]

        medians.append(int(median))

    return medians

# Example usage
n = int(input())
stream = [int(input()) for i in range(n)]
medians = find_median(stream)
for median in medians:
    print(median)

"""
Input
	
4
5
15
1
3

Output
5
10
5
4
"""
