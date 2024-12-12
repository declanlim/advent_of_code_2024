def clamp(bit_string, grid_size):
    return bit_string & ((1 << grid_size**2) - 1)


def move_up(bit_string, grid_size):
    return clamp(bit_string << grid_size, grid_size)


def move_down(bit_string, grid_size):
    return clamp(bit_string >> grid_size, grid_size)


def move_left(bit_string, grid_size):
    # mask out the leftmost column
    mask = int(("0" + "1" * (grid_size - 1)) * grid_size, 2)    
    return clamp((bit_string & mask) << 1, grid_size)


def move_right(bit_string, grid_size):
    # mask out the rightmost column
    mask = int(("1" * (grid_size - 1) + "0") * grid_size, 2)
    return clamp((bit_string & mask) >> 1, grid_size)


def get_repr(bit_string, grid_size):
    tmp = format(bit_string, f"0{grid_size ** 2}b")
    # add in new lines
    return "\n".join(tmp[i:i + grid_size] for i in range(0, len(tmp), grid_size))


def part1():
    with open("input.txt") as f:
        lines = f.readlines()

    grid_size = len(lines)
    assert grid_size == len(lines[0].strip())

    grid_repr = []
    for line in lines:
        stripped = line.strip()
        grid_repr.append(stripped)

    grid_repr_string = "".join(grid_repr)

    bit_boards = {}
    for i in range(10):
        i_str = str(i)
        bit_boards[i] = int(
            "".join("1" if c == i_str else "0" for c in grid_repr_string), 2
        )

    direction_map = {"U": move_up, "D": move_down, "L": move_left, "R": move_right}
    possible_trails = bit_boards[0]

    starting_points = [] # individual bitboards for all starting points 

    # generate a bitboard with indivual starting positions (0 in the board)
    tmp_str = format(bit_boards[0], f"0{grid_size ** 2}b")

    while tmp_str.find("1") != -1:
        idx = tmp_str.find("1")
        tmp_board = 1 << (grid_size ** 2 - idx - 1)
        starting_points.append(tmp_board)
        tmp_str = tmp_str.replace("1", "*", 1)


    print("num start points", len(starting_points))
    total_score = 0
    multiplier = 1

    for start in starting_points:
        possible_trails = start
        merged_trails = 0 # count of trails that merged back together

        for i in range(9):
            cur_board = possible_trails
            possible_trails = 0
            next_board = bit_boards[i + 1]

            for direction in direction_map:
                tmp = direction_map[direction](cur_board, grid_size)
                tmp = tmp & next_board
                possible_trails = possible_trails | tmp

                # print(f"direction {direction}")
                # print(get_repr(tmp, grid_size))
                # print()


            # print(f"possible trails {i}")
            # print(get_repr(possible_trails, grid_size))
            possible_trail_count = bin(possible_trails).count("1")
            starting_point_count = bin(cur_board).count("1")
            if starting_point_count > possible_trail_count:
                print(get_repr(cur_board, grid_size))
                print()
                print(get_repr(possible_trails, grid_size))
                print('adding', starting_point_count - possible_trail_count)
                merged_trails += starting_point_count - possible_trail_count

        multiplier = 1 if merged_trails == 0 else 2 ** merged_trails
        print("multiplier", multiplier)



        # print(get_repr(possible_trails, grid_size))
        # print()
        total_score += bin(possible_trails).count("1")

    return total_score



    # for i in range(9):
    #     cur_board = possible_trails
    #     possible_trails = 0
    #     print("possible starts")
    #     print(get_repr(cur_board, grid_size))
    #     print()
    #     next_board = bit_boards[i + 1]
    #     tmp = 0
    #     # print(f"i {get_repr(cur_board, grid_size)}")

    #     for direction in direction_map:
    #         tmp = direction_map[direction](cur_board, grid_size)
    #         tmp = tmp & next_board
    #         # print(f"direction {direction}")
    #         # print(get_repr(tmp, grid_size))
    #         # print()
    #         possible_trails = possible_trails | tmp
        
    # print(get_repr(possible_trails, grid_size))


        # print(get_repr(possible_trails, grid_size))
        # break

    return None
    return possible_trails


if __name__ == "__main__":
    print(part1())
    # print(get_repr(part1(), grid_size=8))
