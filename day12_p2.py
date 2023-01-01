def main():
    file_lines = open('day12_input.txt', 'r').readlines()

    start_locs, end_loc = [], 0  # using complex numbers like day 9

    for i in range(len(file_lines)):  # find all starting squares as well as ending square and mark their locations in the grid
        line = file_lines[i].strip()
        for j in range(len(line)):
            if line[j] in 'Sa':
                start_locs.append(j + i * 1j)
            if line[j] == 'E':
                end_loc = j + i * 1j

    file_lines = [line.replace('S', 'a').replace('E', 'z') for line in file_lines]

    heightmap = [[ord(x) - 97 for x in y.strip()] for y in file_lines]

    shortest_steps = float('inf')

    for start_loc in start_locs:  # for part 2 we just iterate through all of them. easy.
        queue, pos_visited, steps = [[start_loc]], {start_loc}, float('inf')  # yes i should probably use an actual queue here but idrc

        while len(queue) != 0:  # using breadth-first search algorithm
            path = queue.pop(0)
            loc = path[-1]
            if loc == end_loc:
                steps = len(path) - 1
                break
            for x, y in [(int(i.real), int(i.imag)) for i in (loc + 1, loc - 1, loc + 1j, loc - 1j)]:  # check adjacent sides
                if 0 <= x < len(heightmap[0]) and 0 <= y < len(heightmap) and heightmap[y][x] - heightmap[int(loc.imag)][int(loc.real)] < 2 and x + y * 1j not in pos_visited:
                    queue.append(path + [x + y * 1j])
                    pos_visited.add(x + y * 1j)

        if steps < shortest_steps:
            shortest_steps = steps

    print(shortest_steps)


if __name__ == '__main__':
    main()
