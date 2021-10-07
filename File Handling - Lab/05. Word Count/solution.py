with open("words.txt", "r") as words, open("input.txt", "r") as file, open("output.txt", "w") as output:

    words_list = [j for x in words for j in x.split()]

    dictionary = {}

    chars = [".", ",", "!", "?", "-", ":", ";"]

    for line in file:
        for word in line.split():
            for ch in chars:
                word = word.replace(ch, "")
            if word.lower() in words_list:
                if word.lower() not in dictionary:
                    dictionary[word.lower()] = 0
                dictionary[word.lower()] += 1

    for word, count in sorted(dictionary.items(), key=lambda x: -x[1]):
        output.write(f"{word} - {count}\n")
