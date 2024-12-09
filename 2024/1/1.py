'''
Sum the differences between pairs of location IDs in ascending sorted 
order.
'''

import heapq

heap1 = []
heap2 = []

# Read the inputs into two min-heaps
with open('input.txt', 'r') as file:
    for line in file:
        columns = line.split()
        heapq.heappush(heap1, int(columns[0]))
        heapq.heappush(heap2, int(columns[1]))

# Sum the differences
len = len(heap1)
sum = 0
for i in range(len):
    sum += abs(heapq.heappop(heap1) - heapq.heappop(heap2))
print(sum)