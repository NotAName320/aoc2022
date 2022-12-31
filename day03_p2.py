def find_common(sack1, sack2, sack3):
    common = ''
    for c in sack1:
        if c in sack2 and c in sack3:
            common = c
    return common


def main():
    file_lines = open('day3_input.txt', 'r').readlines()

    pri_sum = 0

    for i in range(0, len(file_lines), 3):
        badge = find_common(file_lines[i].strip(), file_lines[i + 1].strip(), file_lines[i + 2].strip())  # this line is dumb
        pri_sum += ord(badge) - (96 if ord(badge) >= 97 else 38)  # funky formula to get specified point values from ord builtin

    print(pri_sum)


if __name__ == '__main__':
    main()
