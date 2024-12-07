from math import sqrt
import sys
import time

sys.set_int_max_str_digits(16900)

NEW_DIR = {0: 1, 1: 2, 2: 3, 3: 0}
LEFT_MASK = int(("1" * 129 + "0") * 130, 2)
RIGHT_MASK = int(("0" + "1" * 129) * 130, 2)


def clamp(bit_string):
    """clamp the bitstring to maximum 16900 bits"""
    return bit_string & ((1 << 16900) - 1)


def move_bit_string(bit_string, direction):
    """Return the new bit string after moving"""
    size = 130

    if direction == 0 or direction == 2:
        # moving up or down
        shift = size
    else:
        shift = 1

    if direction == 0 or direction == 3:
        res = bit_string << shift
        # make sure there is no "teleportation"
        res = res & LEFT_MASK
    else:
        res = bit_string >> shift
        res = res & RIGHT_MASK

    # ensure the length of the bit string is the same
    res = clamp(res)

    return res


def update_bit_string(bit_string, obstacles, direction):
    """Move the bit string in the given direction
    return the updated bit string and the new direction if applicable
    """
    new_bit_string = move_bit_string(bit_string, direction)
    # if an obstacle is in the way of the next move
    change_direction = new_bit_string & obstacles
    if change_direction:
        direction = (direction + 1) % 4
        return bit_string, direction

    return new_bit_string, direction


def print_grid_repr(bit_string):
    size = int(sqrt(len(bit_string)))
    # split the string into size chunks
    for i in range(0, len(bit_string), size):
        print(bit_string[i : i + size])
    print()


def part1():
    # 130 by 130 grid
    with open("input.txt") as f:
        lines = f.readlines()

    grid_repr = []

    for line in lines:
        stripped = line.strip()
        grid_repr.append((stripped))

    # create a bit string for the current position and whole grid
    grid_repr_string = "".join(grid_repr)

    visited = int("".join("0" for _ in grid_repr_string), 2)
    cur_pos = int("".join("0" if c != "^" else "1" for c in grid_repr_string), 2)
    obstacles = int("".join("1" if c == "#" else "0" for c in grid_repr_string), 2)

    # 0 = up, 1 = right, 2 = down, 3 = left, use +1 mod 4
    direction = 0

    while cur_pos:
        cur_pos, direction = update_bit_string(cur_pos, obstacles, direction)
        visited = visited | cur_pos

    visited_str = format(visited, f"0{len(grid_repr_string)}b")
    obstacles = format(obstacles, f"0{len(grid_repr_string)}b")

    return visited_str.count("1")


if __name__ == "__main__":
    print(part1())
