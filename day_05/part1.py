def part1():
    with open("input.txt") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines if line.strip()]

    # key = number, value = numbers that must come before it
    before_dict = {}
    after_dict = {}

    middle_sum = 0

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
                        break

                if e in before_dict:
                    if set(pages[:end]) - before_dict[e]:
                        break

                start += 1
                end -= 1

            else:
                middle_sum += int(pages[start])

    return middle_sum


if __name__ == "__main__":
    print(part1())
