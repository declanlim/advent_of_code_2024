MAX_LEVEL_DIFF = 3
MIN_LEVEL_DIFF = 1


def check_levels(levels):
    """Helper function to check if a list of levels are safe"""
    num_levels = len(levels)

    # 1 if difference is positive, -1 if negative
    direction_multiplier = -2 * (levels[0] > levels[-1]) + 1

    for pos, (i, j) in enumerate(zip(levels, levels[1:])):
        diff = j - i
        abs_diff = diff * direction_multiplier

        if (abs_diff < MIN_LEVEL_DIFF) or (abs_diff > MAX_LEVEL_DIFF):
            return False, pos

    return True, None


def part2():
    with open("input.txt") as f:
        lines = f.readlines()

    not_safe_count = 0
    for l in lines:
        levels = list(map(int, l.split()))

        result, bad_pos = check_levels(levels)
        if not result:
            # initial levels are not safe, remove potential positions and check again
            positions = [bad_pos + i for i in range(-1, 2)]
            # filter out positions that are out of bounds
            positions = list(filter(lambda x: x >= 0 and x < len(levels), positions))

            for pos in positions:
                # check possible levels
                new_levels = levels[:pos] + levels[pos + 1 :]
                result, _ = check_levels(new_levels)
                if result:  # if levels are safe, carry one
                    break
            else:
                # runs if no break statement, therefore all levels are not safe
                not_safe_count += 1

    return len(lines) - not_safe_count


if __name__ == "__main__":
    print(part2())
