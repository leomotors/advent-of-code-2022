lines = []

with open(input()) as f:
    for line in f:
        lines.append(line.strip())

total = 0

for i in range(0, len(lines), 3):
    group = [set([k for k in lines[x]]) for x in range(i, i + 3)]

    intersect = group[0].intersection(group[1]).intersection(group[2])

    assert (len(intersect) == 1)

    for x in intersect:
        char = ord(x)

        if char < ord('a'):
            total += char - ord('A') + 27
        else:
            total += char - ord('a') + 1

print(total)
