import heapq
from queue import PriorityQueue

def fake_queue():
    q = []
    heapq.heappush(q, (2, "code"))
    heapq.heappush(q, (1, "eat"))
    heapq.heappush(q, (3, "sleep"))
    while q:
        next_item = heapq.heappop(q)
        print(next_item)


def more_real_priority_queue():
    q = PriorityQueue()
    q.put((2, "code"))
    q.put((1, "eat"))
    q.put((3, "sleep"))

    while not q.empty():
        next_item = q.get()
        print(next_item)


def main():
    print(f'Hello main from : {__file__}')
    fake_queue()
    more_real_priority_queue()

if __name__ == '__main__':
    main()