import heapq


def part1():
    left = []
    right = []
    with open("input.txt") as f:
        # read input into heaps
        for line in f:
            l, r = line.split()
            heapq.heappush(left, int(l))
            heapq.heappush(right, int(r))

    # ensure while loop works
    assert len(left) == len(right)

    total_diff = 0

    # heapq maintains a min heap
    while left:
        l = heapq.heappop(left)
        r = heapq.heappop(right)

        total_diff += abs(l - r)

    return total_diff


if __name__ == "__main__":
    print(part1())
