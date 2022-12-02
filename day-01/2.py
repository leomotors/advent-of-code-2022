items = []

with open("1.in") as f:
    current_sum = 0
    for line in f:
        if line.strip() == "":
            items.append(current_sum)
            current_sum = 0

        else:
            current_sum += int(line.strip())

    items.append(current_sum)

print(sum(sorted(items)[-3:]))
