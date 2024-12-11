def part1():
    with open("input.txt") as f:
        line = f.readline().strip()

    max_id = len(line) // 2  # maximum file ID in the representation

    # dictionary of file ID to position in the representation
    pos_dict = {i: [] for i in range(max_id + 1)}

    cur_id = 0  # the file ID for use in the representation
    cur_pos = 0  # the position in the line
    repr_pos = 0  # the position in the representation
    gaps = []  # the indices of the gaps (that should be filled)
    gap_size = []  # the size of each gap

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

    # maximum number of chars in the representation
    max_repr_pos = sum(int(j) for j in line)
    cur_id = 0
    tail_id = max_id
    checksum = 0

    i = 0  # current position in the representation, to be multiplied by cur_id
    while i < max_repr_pos:
        if not pos_dict[cur_id]:
            cur_id += 1  # increase cur_id if the current ID is empty
            if cur_id > max_id:
                break
            continue

        if i in pos_dict[cur_id]:
            checksum += i * cur_id
            pos_dict[cur_id].remove(i)
            i += 1
            continue
        else:
            assert i in gaps
            # fill the gap with the tail ID and remove the gap
            tmp = pos_dict[tail_id].pop(-1)

            checksum += i * tail_id

            if not pos_dict[tail_id]:
                tail_id -= 1

            gaps.remove(i)
            gaps.append(tmp)
            i += 1

    return checksum


if __name__ == "__main__":
    print(part1())
