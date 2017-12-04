inputPrompt = "Input your command! ('h' for help)\n"
help = """Use 'h' to show this help. 
List of commands:'x' to exit,
'+' to add,
'-' to remove,
'l' to show list
'c' to clear list"""


def add_to_list(lst, *items):
    for item in items:
        if item not in lst:
            lst.append(item)
        else:
            print(f"Already on the list: {item}")


def remove_from_list(lst, *items):
    for item in items:
        if item in lst:
            lst.remove(item)
        else:
            print(f"Not on the list: {item}")


def print_list(lst):
    print(lst)


def clear_list(lst):
    lst.clear()


def process_command(lst, cmd):
    items = cmd[1:].split(",")
    if cmd.startswith('+'):
        add_to_list(lst, *items)
    elif cmd.startswith('-'):
        remove_from_list(lst, *items)
    elif cmd.startswith('l'):
        print_list(lst)
    elif cmd.startswith('h'):
        print(help)
    elif cmd.startswith('c'):
        clear_list(lst)
    elif cmd.startswith('x'):
        return
    else:
        print(f"Unknown command {cmd[0]}")


def main():
    lst = []
    in_ = ' '
    while in_ != 'x':
        in_ = input(inputPrompt)
        process_command(lst, in_)


if __name__ == '__main__':
    main()

print("Finished")
