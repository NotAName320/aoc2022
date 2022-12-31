def main():
    file_lines = open('day5_input.txt', 'r').readlines()

    stacks = [[] for x in range(9)]

    for i in range(8):
        line = file_lines[i][1::4]  # strip away brackets and extra spaces
        for j in range(9):
            if line[j] != ' ':
                stacks[j].insert(0, line[j])

    for line in file_lines:
        line = line.strip() + ' '  # add a space just for the next line
        if line[0] != 'm':  # we want to process instructions only now
            continue
        line = line.replace('move ', '').replace('from ', '').replace('to ', '').split()  # lol
        line = [int(x) for x in line]  # younger me wouldve combined this with the last line but idrc anymore
        moved_crates = []
        for i in range(line[0]):
            moved_crates.insert(0, stacks[line[1]-1].pop())
        stacks[line[2]-1] += moved_crates

    print(''.join([x[-1] for x in stacks if x[-1] != ' ']))


if __name__ == '__main__':
    main()
