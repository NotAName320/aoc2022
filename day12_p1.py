def main():
    file_lines = open('day12_test.txt', 'r').readlines()

    start_loc, end_loc = 0, 0  # using complex numbers like day 9

    for i in range(len(file_lines)):  # find characters S and E and mark their location in the grid
        line = file_lines[i].strip()
        for j in range(len(line)):
            if line[j] == 'S':
                start_loc = j + i * 1j
            if line[j] == 'E':
                end_loc = j + i * 1j

    file_lines = [line.replace('S', 'a').replace('E', 'z') for line in file_lines]

    heightmap = [[ord(x) - 97 for x in y.strip()] for y in file_lines]
    queue, pos_visited, steps = [[start_loc]], {start_loc}, 1  # yes i should probably use an actual queue here but idrc

    while len(queue) != 0:  # using breadth-first search algorithm
        path = queue.pop(0)
        loc = path[-1]
        if loc == end_loc:
            break
        for x, y in [(int(i.real), int(i.imag)) for i in (loc + 1, loc - 1, loc + 1j, loc - 1j)]:  # check adjacent sides
            if 0 <= x < len(heightmap[0]) and 0 <= y < len(heightmap) and heightmap[y][x] - heightmap[int(loc.imag)][int(loc.real)] < 2 and x + y * 1j not in pos_visited:
                queue.append(path + [x + y * 1j])
                pos_visited.add(x + y * 1j)
        steps += 1
        print(queue)

    print(steps)


if __name__ == '__main__':
    main()
