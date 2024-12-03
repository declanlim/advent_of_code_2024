def part1():
    max_level_diff = 3  # maximum difference between adjacent levels
    min_level_diff = 1  # minimum difference between adjacent levels

    with open("input.txt") as f:
        lines = f.readlines()

    not_safe_count = 0
    for l in lines:
        levels = list(map(int, l.split()))

        num_levels = len(levels)

        # discard data where total level gap is too large
        if abs(levels[0] - levels[-1]) > max_level_diff * (num_levels - 1):
            not_safe_count += 1
            continue

        # 1 if difference is positive, -1 if negative
        direction_multiplier = -2 * (levels[0] > levels[-1]) + 1

        for i, j in zip(levels, levels[1:]):
            diff = j - i
            abs_diff = diff * direction_multiplier

            if (abs_diff < min_level_diff) or (abs_diff > max_level_diff):
                not_safe_count += 1
                break

    return len(lines) - not_safe_count


if __name__ == "__main__":
    print(part1())
