def is_adjacent(head, tail):
    return abs(head[0] - tail[0]) < 2 and abs(head[1] - tail[1]) < 2


def main():
    file_lines = open('day9_input.txt', 'r').readlines()

    positions_visited, head, tail = {(0, 0)}, (0, 0), (0, 0)

    for line in file_lines:
        line = line.strip()
        direction, num = line.split()
        for i in range(int(num)):
            if line[0] == 'R':
                head = head[0] + 1, head[1]
                if not is_adjacent(head, tail):
                    tail = head[0] - 1, head[1]
            if line[0] == 'L':
                head = head[0] - 1, head[1]
                if not is_adjacent(head, tail):
                    tail = head[0] + 1, head[1]
            if line[0] == 'U':
                head = head[0], head[1] + 1
                if not is_adjacent(head, tail):
                    tail = head[0], head[1] - 1
            if line[0] == 'D':
                head = head[0], head[1] - 1
                if not is_adjacent(head, tail):
                    tail = head[0], head[1] + 1
            positions_visited.add(tail)

    print(len(positions_visited))


if __name__ == '__main__':
    main()
