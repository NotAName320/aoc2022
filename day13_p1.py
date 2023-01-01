def compare_list(left, right):  # shoutout to /u/Tipa16384, his solution wasn't perfect but hey at least he pointed me in the right direction
    if len(left) and len(right):
        cmp = compare(left[0], right[0])
        return cmp if cmp != 0 else compare(left[1:], right[1:])
    return compare(len(left), len(right))


def compare(left, right):
    if type(left) is int and type(right) is int:
        return (left > right) - (left < right)
    left, right = [left] if type(left) is int else left, [right] if type(right) is int else right
    return compare_list(left, right)


def main():
    file_lines = open('day13_input.txt', 'r').readlines()

    index_sum = 0

    for i in range(0, len(file_lines), 3):
        left, right = eval(file_lines[i].strip()), eval(file_lines[i + 1].strip())

        if compare(left, right) < 0:
            index_sum += i // 3 + 1

    print(index_sum)


if __name__ == '__main__':
    main()
