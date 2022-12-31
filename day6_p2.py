def main():
    file_str = open('day6_input.txt', 'r').read()

    for i in range(14, len(file_str)):
        if len(set(file_str[i - 14:i])) == 14:  # only 14 unique chars can create a set of length 14
            print(i)
            break


if __name__ == '__main__':
    main()
