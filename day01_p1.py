def main():
    file_lines = open('day1_input.txt', 'r').readlines()

    most, curr_sum = 0, 0

    for line in file_lines:
        line = line.strip()
        if line == '':
            if curr_sum > most:
                most = curr_sum
            curr_sum = 0
        else:
            curr_sum += int(line)

    print(most)


if __name__ == '__main__':
    main()
