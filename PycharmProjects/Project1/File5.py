inputPrompt = "Input your command! ('h' for help)\n"
help = "Use 'h' to show this help. List of commands:\n'x' to exit,\n'+' to add,\n'-' to remove,\n'l' to show list\n"
in_ = ' '

lst = []


def add_to_list(*items):
    for item in items:
        if item not in lst:
            lst.append(item)
        else:
            print(f"Already on the list: {item}")


def remove_from_list(*items):
    for item in items:
        if item in lst:
            lst.remove(item)
        else:
            print(f"Not on the list: {item}")


def print_list(items):
    print(items)


def process_command(cmd):
    items = cmd[1:].split(",")
    if cmd.startswith('+'):
        add_to_list(*items)
    elif cmd.startswith('-'):
        remove_from_list(*items)
    elif cmd.startswith('l'):
        print_list(lst)
    elif cmd.startswith('h'):
        print(help)
    elif cmd.startswith('x'):
        return
    else:
        print(f"Unknown command {cmd[0]}")


while in_ != 'x':
    in_ = input(inputPrompt)
    process_command(in_)

print("Finished")
