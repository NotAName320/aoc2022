def main():
    file_lines = open('day4_input.txt', 'r').readlines()

    num_contains = 0

    for line in file_lines:
        line = line.strip().replace(',', '-').split('-')  # really just need a list of 4 numbers tbh
        start1, end1, start2, end2 = [int(x) for x in line]
        if (start1 <= start2 and end1 >= end2) or (start1 >= start2 and end1 <= end2):
            num_contains += 1

    print(num_contains)


if __name__ == '__main__':
    main()
