def fill_the_box(height, length, width, *args):
    size_of_box = height * length * width
    left_cubes = 0

    for el in args:
        if el == "Finish":
            break

        if el <= size_of_box:
            size_of_box -= el
        else:
            el -= size_of_box
            size_of_box = 0
            left_cubes += el

    if size_of_box > 0:
        return f"There is free space in the box. You could put {size_of_box} more cubes."

    return f"No more free space! You have {left_cubes} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
