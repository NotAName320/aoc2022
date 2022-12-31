def main():
    file_lines = open('day2_input.txt', 'r').readlines()

    score_sum = 0

    for line in file_lines:
        line = line.strip()
        opp_played = {'A': 1, 'B': 2, 'C': 3}[line[0]]  # yeah yeah i know you cant use a dict like this
        you_resulted = {'X': 0, 'Y': 3, 'Z': 6}[line[2]]
        score_sum += you_resulted
        if you_resulted == 0:
            score_sum += 3 if opp_played == 1 else opp_played - 1
        if you_resulted == 3:
            score_sum += opp_played
        if you_resulted == 6:
            score_sum += 1 if opp_played == 3 else opp_played + 1

    print(score_sum)


if __name__ == '__main__':
    main()
