def generate_str(disk_map):
    rep = ""
    is_space = 0
    id_num = 0

    for char in disk_map:
        if is_space:
            rep += "." * int(char)
            is_space = 1 - is_space
        else:
            rep += str(id_num) * int(char)
            is_space = 1 - is_space
            id_num += 1
        
    
    return rep



def part1():
    with open("input.txt") as f:
        line = f.readline().strip()


    max_id = len(line) // 2

    # dictionary of file ID to position in the representation
    pos_dict = {i: [] for i in range(max_id + 1)}

    cur_id = 0 # the file ID for use in the representation
    cur_pos = 0 # the position in the line
    repr_pos = 0 # the position in the representation
    gaps = [] # the indices of the gaps (that should be filled)
    gap_size = [] # the size of each gap

    while cur_pos < len(line):
        for _ in range(int(line[cur_pos])):
            pos_dict[cur_id].append(repr_pos)
            repr_pos += 1

        cur_pos += 1
        if cur_pos >= len(line):
            break

        gap_size.append(int(line[cur_pos]))
        for _ in range(int(line[cur_pos])):
            gaps.append(repr_pos)
            repr_pos += 1

        cur_id += 1
        cur_pos += 1


    a = ""
    for (k, v), gap in zip(pos_dict.items(), gap_size):
        a += str(k) * len(v)
        a += "." * gap

    # add the final id since there is one less gap
    a += str(max_id) * len(pos_dict[max_id])


    print(gap_size)
    print(a)

    return gaps, pos_dict


if __name__ == "__main__":
    print(part1())