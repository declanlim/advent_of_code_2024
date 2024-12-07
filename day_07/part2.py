def check_possible(target, numbers):
    """divide and conquer to check if possible"""
    if len(numbers) == 2:
        add = numbers[0] + numbers[1]
        mul = numbers[0] * numbers[1]
        cat = int(str(numbers[0]) + str(numbers[1]))
        if add == target or mul == target or cat == target:
            return True
        else:
            return False
    else:
        # perform one operation and recurse
        first = numbers.pop(0)
        # add
        add_list = numbers.copy()
        add_list[0] = first + add_list[0]

        # multiply
        mul_list = numbers.copy()
        mul_list[0] = first * mul_list[0]

        # concatenate
        cat_list = numbers.copy()
        cat_list[0] = int(str(first) + str(cat_list[0]))

        return (
            check_possible(target, add_list)
            or check_possible(target, mul_list)
            or check_possible(target, cat_list)
        )


def part2():
    with open("input.txt") as f:
        lines = f.readlines()

    calibrations = []
    for line in lines:
        line = line.strip()
        target, numbers = line.split(": ")
        target = int(target)
        numbers = [int(x) for x in numbers.split()]
        calibrations.append((target, numbers))

    total = 0
    for target, numbers in calibrations:
        if check_possible(target, numbers):
            total += target
            
    return total


if __name__ == "__main__":
    print(part2())
