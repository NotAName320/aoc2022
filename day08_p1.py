def main():
    file_lines = open('day8_input.txt', 'r').readlines()

    trees = []

    for line in file_lines:
        line = line.strip()
        tree_row = []
        for c in line:
            tree_row.append(int(c))
        trees.append(tree_row)

    num_visible = 0

    for i in range(len(trees)):
        for j in range(len(trees[0])):
            num, visible = trees[i][j], [True for x in range(4)]
            for k in range(0, i):
                if num <= trees[k][j]:
                    visible[0] = False
            for k in range(i + 1, len(trees)):
                if num <= trees[k][j]:
                    visible[1] = False
            for k in range(0, j):
                if num <= trees[i][k]:
                    visible[2] = False
            for k in range(j + 1, len(trees[0])):
                if num <= trees[i][k]:
                    visible[3] = False
            if any(visible):
                num_visible += 1

    print(num_visible)


if __name__ == '__main__':
    main()
