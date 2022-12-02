with open("1.in") as f:
    max_sum = 0
    current_sum = 0
    for line in f:
        if line.strip() == "":
            max_sum = max(current_sum, max_sum)
            current_sum = 0

        else:
            current_sum += int(line.strip())

    max_sum = max(current_sum, max_sum)

print(max_sum)
