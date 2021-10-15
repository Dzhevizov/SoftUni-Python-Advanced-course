from fibonacci import *

sequence = ""

while True:
    command = input()

    if command == "Stop":
        break

    command_args = command.split()

    if command_args[0] == "Create":
        sequence = create_sequence(int(command_args[-1]))
        print(sequence)
    elif command_args[0] == "Locate":
        number = command_args[1]
        if locate_number(number, sequence):
            print(f"The number - {number} is at index {find_index(number, sequence)}")
        else:
            print(f"The number {number} is not in the sequence")
