def main():
    file_str = open('day6_input.txt', 'r').read()

    for i in range(4, len(file_str)):
        if len(set(file_str[i - 4:i])) == 4:  # only 4 unique chars can create a set of length 4
            print(i)
            break


if __name__ == '__main__':
    main()
