def is_adjacent(head, tail):
    return abs(head.real - tail.real) < 2 and abs(head.imag - tail.imag) < 2


def sign(a):
    return ((a.real > 0) - (a.real < 0)) + 1j * ((a.imag > 0) - (a.imag < 0))  # dumb shit that determines the real and imag direction


def main():
    file_lines = open('day9_input.txt', 'r').readlines()

    positions_visited, rope = {0}, [0 for i in range(10)]  # using complex numbers now cause its easier
    dirs = {'R': 1, 'L': -1, 'U': 1j, 'D': -1j}

    for line in file_lines:
        line = line.strip()
        direction, num = line.split()
        for i in range(int(num)):
            rope[0] += dirs[direction]
            for j in range(1, len(rope)):
                if not is_adjacent(rope[j - 1], rope[j]):
                    rope[j] += sign(rope[j - 1] - rope[j])
            positions_visited.add(rope[-1])
    print(len(positions_visited))


if __name__ == '__main__':
    main()
