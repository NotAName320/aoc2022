from functools import cmp_to_key


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

    sorted_packets = sorted([eval(x.strip()) for x in file_lines if x != '\n'] + [[[2]]] + [[[6]]], key=cmp_to_key(compare))

    prod_indices = (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)

    print(prod_indices)


if __name__ == '__main__':
    main()
