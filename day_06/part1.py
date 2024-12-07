from math import sqrt
import sys

sys.set_int_max_str_digits(16900)

def clamp(bit_string):
    """clamp the bitstring to maximum 16900 bits"""
    return bit_string & ((1 << 16900) - 1)

def move_bit_string(bit_string, direction):
    """Return the new bit string after moving"""
    size = int(sqrt(len(bit_string)))

    if direction % 2 == 0:
        # moving up or down
        shift = size
    else:
        shift = 1

    if direction == 0 or direction == 3:
        res = int(bit_string, 2) << shift
    else:
        res = int(bit_string, 2) >> shift

    # ensure the length of the bit string is the same
    res = clamp(res)

    res_str = format(res, f"0{len(bit_string)}b")

    assert len(res_str) == len(bit_string)

    return res_str


def and_bit_string(bit_string, obstacles):
    """Perform a bitwise and on the bit string and obstacles"""
    res = int(bit_string, 2) & int(obstacles, 2)
    res_str = format(res, f"0{len(bit_string)}b")
    return res_str


def or_bit_string(bit_string, visited):
    """Perform a bitwise or on the bit string and visited string"""
    res = int(bit_string, 2) | int(visited, 2)
    res_str = format(res, f"0{len(bit_string)}b")
    return res_str


def update_bit_string(bit_string, obstacles, direction):
    """Move the bit string in the given direction
    return the updated bit string and the new direction if applicable

    up: shift left by 130
    right: shift right by 1
    down: shift right by 130
    left: shift left by 1
    """
    new_bit_string = move_bit_string(bit_string, direction)

    # if an obstacle is in the way of the next move
    change_direction = and_bit_string(new_bit_string, obstacles)
    # print(f"change_direction: {change_direction}")
    if "1" in change_direction:
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

    visited = "".join("0" for _ in grid_repr_string)
    cur_pos = "".join("0" if c != "^" else "1" for c in grid_repr_string)
    obstacles = "".join("1" if c == "#" else "0" for c in grid_repr_string)


    # 0 = up, 1 = right, 2 = down, 3 = left, use +1 mod 4
    direction = 0

    while "1" in cur_pos:
        cur_pos, direction = update_bit_string(cur_pos, obstacles, direction)
        visited = or_bit_string(visited, cur_pos)
        

    assert "1" not in cur_pos
    assert int(cur_pos, 2) == 0
    # assert int(and_bit_string(visited, obstacles)) == 0


    return sum(int(c) for c in visited)

if __name__ == "__main__":
    print(part1())
