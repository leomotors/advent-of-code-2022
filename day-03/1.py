total = 0

with open(input()) as f:
    for line in f:
        line = line.strip()

        mid = len(line) // 2
        a = line[:mid]
        b = line[mid:]

        setA = set([x for x in a])
        setB = set([x for x in b])

        intersect = setA.intersection(setB)

        assert (len(intersect) == 1)

        for x in intersect:
            char = ord(x)

            if char < ord('a'):
                total += char - ord('A') + 27
            else:
                total += char - ord('a') + 1

print(total)
