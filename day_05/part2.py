import pprint


def part2():
    with open("input.txt") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines if line.strip()]

    # key = number, value = numbers that must come before it
    before_dict = {}
    after_dict = {}

    middle_sum = 0
    incorrect = []

    # part 1 to find incorrect lines
    for line in lines:
        if "|" in line:
            b, a = line.split("|")  # STILL AS STRINGS

            if a in before_dict:
                before_dict[a].add(b)
            else:
                before_dict[a] = {b}

            if b in after_dict:
                after_dict[b].add(a)
            else:
                after_dict[b] = {a}

        else:
            pages = line.split(",")

            start = 0
            end = len(pages) - 1

            while start < end:
                s = pages[start]
                e = pages[end]

                if s in after_dict:
                    if set(pages[start + 1 :]) - after_dict[s]:
                        incorrect.append(line)
                        break

                if e in before_dict:
                    if set(pages[:end]) - before_dict[e]:
                        incorrect.append(line)
                        break

                start += 1
                end -= 1

    # part 2 to find correct ordering of lines
    # checked that every line will have unique correct position
    for line in incorrect:
        line = line.split(",")
        length = len(line)
        mp = length // 2

        for i in line:
            before = set(j for j in before_dict[i] if j in line)
            after = set(j for j in after_dict[i] if j in line)
            if len(before) == len(after) == mp:
                middle_sum += int(i)
                break

    return middle_sum


if __name__ == "__main__":
    print(part2())
