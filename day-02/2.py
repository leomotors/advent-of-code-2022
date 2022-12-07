# Rock = A => 0
# Paper = B => 1
# Scissor = C => 2

# X -> Lose
# Y -> Draw
# Z -> Win

result_map = {
    0: 3,
    1: 1,
    2: 2,
    10: 1,
    11: 2,
    12: 3,
    20: 2,
    21: 3,
    22: 1
}


total = 0

with open("1.in") as f:
    for line in f:
        A, B = line.strip().split(" ")

        opponent = ['A', 'B', 'C'].index(A)
        verdict = ['X', 'Y', 'Z'].index(B)

        total += verdict * 3 + result_map[opponent * 10 + verdict]

print(total)
