import pyfiglet


def print_art(msg):
    formatted_msg = pyfiglet.figlet_format(msg)
    print(formatted_msg)


message = input()
print_art(message)
