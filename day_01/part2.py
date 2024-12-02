def part2():
    left_count = {}
    right_count = {}

    with open("input.txt") as f:
        # get counts of each number in a dict
        for line in f:
            l, r = line.split()
            left_count[int(l)] = left_count.get(int(l), 0) + 1
            right_count[int(r)] = right_count.get(int(r), 0) + 1

    total_similarity = 0

    for l_k, l_v in left_count.items():
        if l_k in right_count:
            similarity = l_k * right_count[l_k]
            similarity *= l_v
            total_similarity += similarity

    return total_similarity


if __name__ == "__main__":
    print(part2())
