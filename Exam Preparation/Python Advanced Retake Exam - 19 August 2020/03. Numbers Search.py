def numbers_searching(*args):
    sorted_list = sorted(args)
    dictionary = {}
    for el in sorted_list:
        if el not in dictionary:
            dictionary[el] = 0
        dictionary[el] += 1
    duplicates = [x for x in dictionary if dictionary[x] > 1]
    smallest_num = sorted_list[0]
    biggest_num = sorted_list[-1]
    missing_number = 0
    for i in range(smallest_num, biggest_num):
        if i not in sorted_list:
            missing_number = i
    return [missing_number, duplicates]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
