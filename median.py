import heapq
from functools import reduce


def main():
    data = []
    with open('median.txt') as file:
        for line in file.readlines():
            data.append(int(line.strip()))
    
    median = medianMaintenence(data)
    print(reduce(lambda x,y: (x+y) % 10000, median))



def medianMaintenence(data):

    # smaller half of data in heap_low, a MAX-heap
    heap_low = []
    # bigger half of data in heap_high, a MIN-heap
    heap_high = []
    median = []

    for i in data:
        if len(heap_low) == 0:
            heapq.heappush(heap_low, -i)
        else:
            m = -heap_low[0]
            if i > m:
                heapq.heappush(heap_high, i)
                # rebalancing
                if len(heap_high) > len(heap_low):
                    min_heap_high = heapq.heappop(heap_high)
                    heapq.heappush(heap_low, -min_heap_high)
            else:
                heapq.heappush(heap_low, -i)
                # rebalancing
                if len(heap_low) - len(heap_high) > 1:
                    max_heap_low = heapq.heappop(heap_low)
                    heapq.heappush(heap_high, -max_heap_low)
      
        median.append(-heap_low[0])

    return median


if __name__ == "__main__":
    main()