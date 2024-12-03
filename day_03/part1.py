import re


def part1():
    with open("input.txt") as f:
        lines = f.readlines()

    total = 0

    pattern = r"(mul\(\d{1,3},\d{1,3}\))"
    regex = re.compile(pattern)

    for line in lines:
        res = regex.findall(line)

        for r in res:
            l, r = r[4:-1].split(",")
            total += int(l) * int(r)

    return total


if __name__ == "__main__":
    print(part1())
