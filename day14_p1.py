def main():
    file_lines = open('day14_input.txt', 'r').readlines()

    rocks = set()

    for line in file_lines:  # create map of rocks using a set
        line = [(x.split(',')) for x in line.strip().split(' -> ')]  # real fucked up string shit

        coords = [int(x[0]) + int(x[1]) * 1j for x in line]  # yes we're using complex nums again

        for i in range(len(coords) - 1):
            left_bigger = (1 if coords[i].real < coords[i + 1].real else -1) + (1 if coords[i].imag < coords[i + 1].imag else -1) * 1j  # helps us construct range to iterate
            for j in range(int(coords[i].real), int(coords[i + 1].real) + int(left_bigger.real), int(left_bigger.real)):
                rocks.add(j + coords[i].imag * 1j)
            for j in range(int(coords[i].imag), int(coords[i + 1].imag) + int(left_bigger.imag), int(left_bigger.imag)):
                rocks.add(coords[i].real + j * 1j)

    sands, lowest_rock, inf_falling = set(), int(sorted(rocks, key=lambda a: a.imag, reverse=True)[0].imag), False

    while not inf_falling:
        sand_loc = 500
        while True:
            if sand_loc.imag > lowest_rock:
                inf_falling = True
                break
            if (check_loc := sand_loc + 1j) not in sands.union(rocks):  # check immediately below
                sand_loc = check_loc
            elif (check_loc := sand_loc - 1 + 1j) not in sands.union(rocks):  # check left
                sand_loc = check_loc
            elif (check_loc := sand_loc + 1 + 1j) not in sands.union(rocks):  # check right
                sand_loc = check_loc
            else:
                sands.add(sand_loc)  # sand settles here
                break

    print(len(sands))


if __name__ == '__main__':
    main()
