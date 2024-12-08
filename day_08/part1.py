from itertools import combinations


def check_and_add(antinodes, height, width, a_nodes):
    for a_node in a_nodes:
        if (
            a_node[0] >= 0
            and a_node[0] < height
            and a_node[1] >= 0
            and a_node[1] < width
        ):
            antinodes.add(a_node)


def part1():
    with open("input.txt") as f:
        lines = f.readlines()

    height = len(lines)
    width = len(lines[0].strip())

    antennae = {}
    for i, line in enumerate(lines):
        line = line.strip()
        for j, c in enumerate(line):
            if c == ".":
                continue
            else:
                if c in antennae:
                    antennae[c].append((i, j))
                else:
                    antennae[c] = [(i, j)]

    antinodes = set()

    for ant in antennae.values():
        for combo in combinations(ant, 2):
            n1_x, n1_y = combo[0]
            n2_x, n2_y = combo[1]

            x_diff = n2_x - n1_x
            y_diff = n2_y - n1_y

            a_node1 = (n1_x - x_diff, n1_y - y_diff)
            a_node2 = (n2_x + x_diff, n2_y + y_diff)

            check_and_add(antinodes, height, width, [a_node1, a_node2])

    return len(antinodes)


if __name__ == "__main__":
    print(part1())
