import re


def part2():
    # mul() enabled at start of program not start of line
    with open("input.txt") as f:
        lines = f.readlines()

    total = 0
    # merge to single line
    target = "".join([l.strip() for l in lines])

    main_pattern = r"(mul\(\d{1,3},\d{1,3}\))"
    regex = re.compile(main_pattern)

    exclude_pattern_mid = r"don't\(\).*?do\(\)"
    exclude_regex_mid = re.compile(exclude_pattern_mid)

    res = list(regex.findall(target))
    exclude_res = exclude_regex_mid.findall(target)

    last_dont = target.rindex("don't()")
    if "do()" not in target[last_dont:]:
        exclude_res.append(target[last_dont:])

    exclude_str = "".join(exclude_res)
    exclude_muls = list(regex.findall(exclude_str))

    for e in exclude_muls:  # remove all muls to be excluded
        assert e in res
        res.remove(e)

    for r in res:
        l, r = r[4:-1].split(",")
        total += int(l) * int(r)

    return total


if __name__ == "__main__":
    print(part2())
