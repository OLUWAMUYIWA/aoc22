# says what opponent will play
def col1(c):
    if c == 'A':
        return 'rock'
    elif c == 'B':
        return 'paper'
    elif c == 'C':
        return 'scissors'
    else:
        raise Exception("nothing other than A, B, or C is allowed")

def col2(c):
    if c == 'X':
        return 'rock'
    elif c == 'Y':
        return 'paper'
    elif c == 'Z':
        return 'scissors'
    else:
        raise Exception("nothing other than A, B, or C is allowed")


def roundScore(opp, you):
    score = 0
    if you == 'rock':
        score += 1
    elif you == 'paper':
        score += 2
    elif you == 'scissors':
        score += 3
    else:
        raise Exception("unallowed value")
    
    if you == 'rock':
        if opp == 'rock':
            score += 3
        elif opp == 'scissors':
            score += 6
    elif you == 'paper':
        if opp == 'paper':
            score += 3
        elif opp == 'rock':
            score += 6
    elif you == 'scissors':
        if opp == 'scissors':
            score += 3
        elif opp == 'paper':
            score += 6
    return score

def part1(file):
    f = open(file, 'r')
    lines = f.readlines()
    score = 0
    for line in lines:
        splits = line.split()
        score += roundScore(col1(splits[0]), col2(splits[1]))
    return score


print(part1('day2.txt'))
         
# says whether you lose, draw, or win
def col2part2(c):
    if c == 'X':
        return 0
    elif c == 'Y':
        return 3
    elif c == 'Z':
        return 6
    else:
        raise Exception("nothing other than A, B, or C is allowed")

def roundScorePart2(opp, you):
    score = 0
    # lose
    if you == 0:
        if opp == 'rock':
            score += 3
        elif opp == 'paper':
            score += 1
        elif opp == 'scissors':
            score += 2
    #draw
    elif you == 3:
        if opp == 'rock':
            score += 1
        elif opp == 'paper':
            score += 2
        elif opp == 'scissors':
            score += 3
    elif you == 6:
        if opp == 'rock':
            score += 2
        elif opp == 'paper':
            score += 3
        elif opp == 'scissors':
            score += 1
    else:
        raise Exception("unallowed value")
    score += you
    return score


def part2(file):
    f = open(file, 'r')
    lines = f.readlines()
    score = 0
    for line in lines:
        splits = line.split()
        score += roundScorePart2(col1(splits[0]), col2part2(splits[1]))
    return score


print(part2('day2.txt'))