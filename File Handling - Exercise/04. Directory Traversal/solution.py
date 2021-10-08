import os


def traverse_directories(path, dictionary):
    for el in os.listdir(path):
        if os.path.isfile(os.path.join(path, el)):
            extension = el.split(".")[-1]
            if extension not in dictionary:
                dictionary[extension] = []
            dictionary[extension].append(el)
        elif os.path.isdir(os.path.join(path, el)):
            traverse_directories(os.path.join(path, el), dictionary)


dictionary = {}
traverse_directories(os.getcwd(), dictionary)

try:
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
except:
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

file_path = os.path.join(desktop, "report.txt")

with open(file_path, "w") as file:
    for ext, files in sorted(dictionary.items()):
        file.write(f".{ext}\n")
        for el in sorted(files):
            file.write(f"- - - {el}\n")
