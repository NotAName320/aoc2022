def main():
    file_lines = open('day1_input.txt', 'r').readlines()

    most1, most2, most3, curr_sum = 0, 0, 0, 0

    for line in file_lines:
        line = line.strip()
        if line == '':
            if curr_sum >= most1:
                most3, most2, most1 = most2, most1, curr_sum
            elif curr_sum >= most2:
                most3, most2 = most2, curr_sum
            elif curr_sum >= most3:
                most3 = curr_sum
            curr_sum = 0
        else:
            curr_sum += int(line)

    print(most1 + most2 + most3)


if __name__ == '__main__':
    main()
