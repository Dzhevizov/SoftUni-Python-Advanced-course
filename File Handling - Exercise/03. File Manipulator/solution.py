import os

command_data = input()

while not command_data == "End":

    command_data = command_data.split("-")
    command = command_data[0]

    if command == "Create":
        file_name = command_data[1]
        file = open(file_name, "w")
        file.close()

    elif command == "Add":
        file_name = command_data[1]
        content = command_data[2]
        with open(file_name, "a") as file:
            file.write(f"{content}\n")

    elif command == "Replace":
        file_name = command_data[1]
        old_string = command_data[2]
        new_string = command_data[3]

        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                data = file.read()
            with open(file_name, "w") as file:
                file.write(data.replace(old_string, new_string))
        else:
            print("An error occurred")

    elif command == "Delete":
        file_name = command_data[1]

        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")

    command_data = input()
