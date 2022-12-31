def main():
    file_lines = open('day10_input.txt', 'r').readlines()

    X, sum_strengths, cycle, num_pending, instruction = 1, 0, 1, [0], 0

    while True:
        line = file_lines[instruction].strip()

        # start of cycle: process instruction
        if num_pending[0] != 0 or line == 'noop':  # if non zero number is at index 0, or instruction is noop, stack must have a 0
            num_pending.insert(0, 0)
        else:
            num_pending.insert(0, int(line.split()[1]))

        # during cycle: check for number and increment cycle
        if cycle in [20, 60, 100, 140, 180, 220]:
            sum_strengths += X * cycle
        cycle += 1

        # after cycle: move on to next instruction if needed and add to X if needed
        if num_pending[-1] != 0 or line == 'noop':
            instruction += 1

        X += num_pending.pop()

        if instruction == len(file_lines):
            break

    print(sum_strengths)


if __name__ == '__main__':
    main()
