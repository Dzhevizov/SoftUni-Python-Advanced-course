with open("text.txt", "r") as file, open("output.txt", "w") as output:

    lines = 0

    for line in file:

        letters = 0
        punctuation_marks = 0

        lines += 1

        for ch in line:
            if not ch == " " and not ch == "\n":
                if ch.isalpha():
                    letters += 1
                else:
                    punctuation_marks += 1

        line = line.replace('\n', '')

        output.write(f"Line {lines}: {line} ({letters})({punctuation_marks})\n")
