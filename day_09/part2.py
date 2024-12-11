def part2():
    with open("input.txt") as f:
        line = f.readline().strip()

    max_id = len(line) // 2  # maximum file ID in the representation

    # dictionary of file ID to position in the representation
    pos_dict = {i: [] for i in range(max_id + 1)}

    cur_id = 0  # the file ID for use in the representation
    cur_pos = 0  # the position in the line
    repr_pos = 0  # the position in the representation
    gap_size = {}  # the size of each gap and the start index in the representation
    block_size = []  # the size of each block

    get_min_gap_pos = lambda lb: (
        min((b for a in gap_size for b in gap_size[a] if a >= lb), default=None)
    )

    while cur_pos < len(line):
        block_size.append(int(line[cur_pos]))
        for _ in range(int(line[cur_pos])):
            pos_dict[cur_id].append(repr_pos)
            repr_pos += 1

        cur_pos += 1
        if cur_pos >= len(line):
            break

        cur_line_int = int(line[cur_pos])

        if cur_line_int:
            if cur_line_int in gap_size:
                gap_size[cur_line_int].append(repr_pos)
            else:
                gap_size[cur_line_int] = [repr_pos]

        for _ in range(cur_line_int):
            repr_pos += 1

        cur_id += 1
        cur_pos += 1

    tail_id = max_id
    while True:
        if tail_id == 0:
            break

        tail_block_size = len(pos_dict[tail_id])
        min_gap_pos = get_min_gap_pos(
            tail_block_size
        )  # leftmost gap that can fit the tail block

        # skip if there is no gap that can fit the tail block
        if not min_gap_pos:
            tail_id -= 1
            continue

        if min_gap_pos > pos_dict[tail_id][0]:
            tail_id -= 1
            continue

        # the file block can be moved to the smallest gap
        diff = min_gap_pos - pos_dict[tail_id][0]
        block_start = pos_dict[tail_id][0]
        # move the file block
        pos_dict[tail_id] = [x + diff for x in pos_dict[tail_id]]
        # update the gap size
        replaced_size = [a for a in gap_size if min_gap_pos in gap_size[a]][0]

        # remove the gap
        gap_size[replaced_size].remove(min_gap_pos)
        if not gap_size[replaced_size]:
            gap_size.pop(replaced_size)

        remaining_gap = replaced_size - tail_block_size
        if remaining_gap:
            if remaining_gap in gap_size:
                gap_size[remaining_gap].append(min_gap_pos + tail_block_size)
            else:
                gap_size[remaining_gap] = [min_gap_pos + tail_block_size]

        # add back gap from moved block and simplfy if possible
        end_line_up = {
            k: a for k, v in gap_size.items() for a in v if a + k == block_start
        }
        start_line_up = {
            k: a
            for k, v in gap_size.items()
            for a in v
            if a == block_start + tail_block_size
        }

        assert len(end_line_up) <= 1
        assert len(start_line_up) <= 1

        if end_line_up:
            # remove the end line up gap and update the size
            tmp_size, tmp_start = end_line_up.popitem()
            gap_size[tmp_size].remove(tmp_start)
            tail_block_size += tmp_size
            block_start = tmp_start  # update new block start

        if start_line_up:
            # remove the start line up gap and update the size
            tmp_size, tmp_start = start_line_up.popitem()
            gap_size[tmp_size].remove(tmp_start)
            tail_block_size += tmp_size

        if tail_block_size in gap_size:
            gap_size[tail_block_size].append(block_start)
        else:
            gap_size[tail_block_size] = [block_start]

        tail_id -= 1

    checksum = 0
    for k, v in pos_dict.items():
        for i in v:
            checksum += i * k

    return checksum


if __name__ == "__main__":
    print(part2())
