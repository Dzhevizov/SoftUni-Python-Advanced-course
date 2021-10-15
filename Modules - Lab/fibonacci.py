def find_fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return find_fibonacci(num - 1) + find_fibonacci(num - 2)


def create_sequence(num):
    seq = []
    for i in range(num):
        seq.append(find_fibonacci(i))
    result = " ".join(map(str, seq))
    return result


def locate_number(num, seq):
    return num in seq


def find_index(num, seq):
    seq_list = seq.split()
    return seq_list.index(num)

