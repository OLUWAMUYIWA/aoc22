def part1(file):
    f = open(file, "r")
    lines = f.readlines()
    max = 0
    curr = 0
    for line in lines:
        if line == "\n":
            if curr >= max:
                max = curr
            curr = 0
        else:
            curr += int(line)
    f.close()
    return max


print(part1('day1.txt'))

def part2(file):
    l = []
    f = open(file, 'r')
    lines = f.readlines()
    curr = 0
    for line in lines:
        if line != "\n":
            curr += int(line)
        elif curr != 0:
            l.append(curr)
            curr = 0
    l.sort()
    return l[-1] + l[-2] + l[-3]

print(part2('day1.txt'))