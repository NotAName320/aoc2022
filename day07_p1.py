from collections import defaultdict


def main():
    file_lines = open('day7_input.txt', 'r').readlines()

    dirs_size = defaultdict(int)  # avoids KeyError when adding dirs for the first time
    current_dir = ['']

    for line in file_lines:
        match line.strip().split():
            case '$', 'cd', '/':
                current_dir = ['']
            case '$', 'cd', '..':
                current_dir.pop()
            case '$', 'cd', directory:
                current_dir.append(directory)
            case '$', 'ls': pass
            case 'dir', _: pass
            case size, _:
                for i in range(len(current_dir)):
                    dirs_size['/'.join(current_dir[:i + 1])] += int(size)

    sum_over = sum([x for x in dirs_size.values() if x <= 100000])
    print(sum_over)


if __name__ == '__main__':
    main()
