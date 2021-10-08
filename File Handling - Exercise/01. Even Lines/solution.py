with open("text.txt", "r") as file, open("output.txt", "w") as output:

    count = 0
    replaced_symbols = ["-", ",", ".", "!", "?"]

    for line in file:
        if count % 2 == 0:
            for ch in replaced_symbols:
                line = line.replace(ch, "@")
            line = [x for x in reversed(line.split())]

            output.write(f"{' '.join(line)}\n")
        count += 1
