def main():
    file_lines = open('day14_input.txt', 'r').readlines()

    rocks = set()  # could probably just make this set and sands into the same thing but i think having them separate is cleaner and makes me look better lol

    for line in file_lines:  # create map of rocks using a set
        line = [(x.split(',')) for x in line.strip().split(' -> ')]  # real fucked up string shit

        coords = [int(x[0]) + int(x[1]) * 1j for x in line]  # yes we're using complex nums again

        for i in range(len(coords) - 1):
            left_bigger = (1 if coords[i].real < coords[i + 1].real else -1) + (1 if coords[i].imag < coords[i + 1].imag else -1) * 1j  # helps us construct range to iterate
            for j in range(int(coords[i].real), int(coords[i + 1].real) + int(left_bigger.real), int(left_bigger.real)):
                rocks.add(j + coords[i].imag * 1j)
            for j in range(int(coords[i].imag), int(coords[i + 1].imag) + int(left_bigger.imag), int(left_bigger.imag)):
                rocks.add(coords[i].real + j * 1j)

    sand_rocks, lowest_rock = set(rocks), int(sorted(rocks, key=lambda a: a.imag, reverse=True)[0].imag)  # have to modify my code to rid itself of unions. why are they so slow?

    while 500 not in sand_rocks:
        sand_loc = 500
        while True:
            if sand_loc.imag >= lowest_rock + 1:
                break
            if sand_loc + 1j not in sand_rocks:  # check immediately below
                sand_loc += 1j
            elif sand_loc + 1j - 1 not in sand_rocks:  # check left
                sand_loc += 1j - 1
            elif sand_loc + 1j + 1 not in sand_rocks:  # check right
                sand_loc += 1j + 1
            else:
                break
        sand_rocks.add(sand_loc)

    print(len(sand_rocks) - len(rocks))


if __name__ == '__main__':
    main()
