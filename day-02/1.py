# Rock = A - X => 0
# Paper = B - Y => 1
# Scissor = C - Z => 2

def verdict(opponent, me):
    if opponent == me:
        return 3

    if me > opponent:
        if opponent == 0 and me == 2:
            return 0
        else:
            return 6
    else:
        if me == 0 and opponent == 2:
            return 6
        else:
            return 0


total = 0

with open("1.in") as f:
    for line in f:
        A, B = line.strip().split(" ")

        opponent = ['A', 'B', 'C'].index(A)
        me = ['X', 'Y', 'Z'].index(B)

        total += me + 1 + verdict(opponent, me)

print(total)
