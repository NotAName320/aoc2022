def main():
    file_lines = open('day8_input.txt', 'r').readlines()

    trees = []

    for line in file_lines:
        line = line.strip()
        tree_row = []
        for c in line:
            tree_row.append(int(c))
        trees.append(tree_row)

    best_score = 0

    for i in range(len(trees)):
        for j in range(len(trees[0])):
            num, count, scenic_score = trees[i][j], 0, 1
            for k in range(i - 1, -1, -1):
                count += 1
                if num <= trees[k][j]:
                    break
            scenic_score, count = scenic_score * count, 0
            for k in range(i + 1, len(trees)):
                count += 1
                if num <= trees[k][j]:
                    break
            scenic_score, count = scenic_score * count, 0
            for k in range(j - 1, -1, -1):
                count += 1
                if num <= trees[i][k]:
                    break
            scenic_score, count = scenic_score * count, 0
            for k in range(j + 1, len(trees[0])):
                count += 1
                if num <= trees[i][k]:
                    break
            scenic_score = scenic_score * count
            if scenic_score > best_score:
                best_score = scenic_score

    print(best_score)


if __name__ == '__main__':
    main()
