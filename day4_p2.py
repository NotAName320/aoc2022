def overlaps(start1, end1, start2):  # i really cannot think of an easier way to do this LMAO
    for i in range(start1, end1 + 1):
        if i == start2:
            return True
    return False


def main():
    file_lines = open('day4_input.txt', 'r').readlines()

    num_overlaps = 0

    for line in file_lines:
        line = line.strip().replace(',', '-').split('-')  # really just need a list of 4 numbers tbh
        start1, end1, start2, end2 = [int(x) for x in line]
        if overlaps(start1, end1, start2) or overlaps(start2, end2, start1):
            num_overlaps += 1

    print(num_overlaps)


if __name__ == '__main__':
    main()
