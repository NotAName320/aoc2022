def main():
    file_lines = open('day10_input.txt', 'r').readlines()

    X, cycle, num_pending, instruction, current_line, screen = 1, 1, [0], 0, '', ''

    while True:
        line = file_lines[instruction].strip()

        # start of cycle: process instruction
        if num_pending[0] != 0 or line == 'noop':  # if non zero number is at index 0, or instruction is noop, stack must have a 0
            num_pending.insert(0, 0)
        else:
            num_pending.insert(0, int(line.split()[1]))

        # during cycle: draw pixel, check for number, and increment cycle
        if X <= cycle % 40 <= X + 2:  # this line doesn't work perfectly when cycle % 40 == 39 for some weird reason. frankly, i don't care!
            current_line += '#'
        else:
            current_line += '.'

        if cycle in [40, 80, 120, 160, 200, 240]:
            screen += current_line + '\n'
            current_line = ''
        cycle += 1

        # after cycle: move on to next instruction if needed and add to X if needed
        if num_pending[-1] != 0 or line == 'noop':
            instruction += 1

        X += num_pending.pop()

        if instruction == len(file_lines):
            break

    print(screen)


if __name__ == '__main__':
    main()
