VALID_CORNERS = {"MMSS", "MSMS", "SSMM", "SMSM"}

def check_position(grid, i, j):
    """Another hideous way to check for X-MAS strings"""
    if grid[j][i] != "A":
        return 0
    
    width = len(grid[0])
    height = len(grid)

    # need at least one space on each side
    if i < 1 or i >= width - 1:
        return 0
    
    if j < 1 or j >= height - 1:
        return 0
    
    # check corners, can skip if any are X
    corner_string = "".join(grid[j + y][i + x] for x in [-1, 1] for y in [-1, 1])

    if "X" in corner_string:
        return 0

    if corner_string in VALID_CORNERS:
        return 1
    
    return 0

def part2():
    with open("input.txt") as f:
        lines = f.readlines()

    grid = [list(line.strip()) for line in lines]

    width = len(grid[0])
    height = len(grid)

    num_x_mas = 0

    for i in range(width):
        for j in range(height):
            num_x_mas += check_position(grid, i, j)

    return num_x_mas


if __name__ == "__main__":
    print(part2())
