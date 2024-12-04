def check_position(grid, i, j):
    """A hideous way to return the number of XMAS strings around the current position"""
    if grid[j][i] != "X":
        # skip if not the start of XMAS
        return 0

    num_xmas = 0
    width = len(grid[0])
    height = len(grid)

    skip_left = False
    skip_right = False
    skip_top = False
    skip_bottom = False

    # check if far away from edges
    if i < 3:
        skip_left = True

    if i >= width - 3:
        skip_right = True

    if j < 3:
        skip_top = True

    if j >= height - 3:
        skip_bottom = True

    if not skip_left:
        if grid[j][i - 1] == "M" and grid[j][i - 2] == "A" and grid[j][i - 3] == "S":
            num_xmas += 1

        if not skip_top:
            if (
                grid[j - 1][i - 1] == "M"
                and grid[j - 2][i - 2] == "A"
                and grid[j - 3][i - 3] == "S"
            ):
                num_xmas += 1

        if not skip_bottom:
            if (
                grid[j + 1][i - 1] == "M"
                and grid[j + 2][i - 2] == "A"
                and grid[j + 3][i - 3] == "S"
            ):
                num_xmas += 1

    if not skip_right:
        if grid[j][i + 1] == "M" and grid[j][i + 2] == "A" and grid[j][i + 3] == "S":
            num_xmas += 1

        if not skip_top:
            if (
                grid[j - 1][i + 1] == "M"
                and grid[j - 2][i + 2] == "A"
                and grid[j - 3][i + 3] == "S"
            ):
                num_xmas += 1

        if not skip_bottom:
            if (
                grid[j + 1][i + 1] == "M"
                and grid[j + 2][i + 2] == "A"
                and grid[j + 3][i + 3] == "S"
            ):
                num_xmas += 1

    if not skip_top:
        if grid[j - 1][i] == "M" and grid[j - 2][i] == "A" and grid[j - 3][i] == "S":
            num_xmas += 1

    if not skip_bottom:
        if grid[j + 1][i] == "M" and grid[j + 2][i] == "A" and grid[j + 3][i] == "S":
            num_xmas += 1


    return num_xmas

def part1():
    with open("input.txt") as f:
        lines = f.readlines()

    grid = [list(line.strip()) for line in lines]

    width = len(grid[0])
    height = len(grid)

    num_xmas = 0

    for i in range(width):
        for j in range(height):
            num_xmas += check_position(grid, i, j)

    return num_xmas


if __name__ == "__main__":
    print(part1())
