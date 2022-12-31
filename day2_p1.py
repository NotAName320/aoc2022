def main():
    file_lines = open('day2_input.txt', 'r').readlines()

    score_sum = 0

    for line in file_lines:
        line = line.strip()
        opp_played = {'A': 1, 'B': 2, 'C': 3}[line[0]]  # yeah yeah i know you cant use a dict like this
        you_played = {'X': 1, 'Y': 2, 'Z': 3}[line[2]]
        score_sum += you_played
        if opp_played == you_played:
            score_sum += 3
        if you_played - opp_played in [1, -2]:
            score_sum += 6

    print(score_sum)


if __name__ == '__main__':
    main()
