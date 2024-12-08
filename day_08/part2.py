from itertools import combinations


def check_bounds(a_node, height, width):
    return (
        a_node[0] >= 0 and a_node[0] < height and a_node[1] >= 0 and a_node[1] < width
    )


def generate_and_add(antinodes, height, width, combo):
    n1_x, n1_y = combo[0]
    n2_x, n2_y = combo[1]

    antinodes.update(combo)

    x_diff = n2_x - n1_x
    y_diff = n2_y - n1_y

    while True:
        a_node = (n1_x - x_diff, n1_y - y_diff)
        if not check_bounds(a_node, height, width):
            break
        antinodes.add(a_node)
        n1_x, n1_y = a_node

    while True:
        a_node = (n2_x + x_diff, n2_y + y_diff)
        if not check_bounds(a_node, height, width):
            break
        antinodes.add(a_node)
        n2_x, n2_y = a_node


def part2():
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
            generate_and_add(antinodes, height, width, combo)

    return len(antinodes)


if __name__ == "__main__":
    print(part2())
