def main():
    file_lines = open('day3_input.txt', 'r').readlines()

    ruck_sum = 0

    for line in file_lines:
        line = line.strip()
        line_p1 = line[:len(line) // 2]
        line_p2 = line[len(line) // 2:]
        for c in set(line_p1):  # convert to set to remove duplicate chars
            if c in line_p2:
                ruck_sum += ord(c) - (96 if ord(c) >= 97 else 38)  # funky formula to get specified point values from ord builtin

    print(ruck_sum)


if __name__ == '__main__':
    main()
