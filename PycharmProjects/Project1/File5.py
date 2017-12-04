inputPrompt = "Input your command! ('h' for help)\n"
help = """Use 'h' to show this help. 
List of commands:'x' to exit,
'+' to add,
'-' to remove,
'l' to show list
'c' to clear list
'sn' to sort list by item name
'sl' to sort list by item length"""


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


def sort_list(lst, type):
    if (type == "sn"):
        lst.sort()
    elif (type == "sl"):
        lst.sort(key=lambda x: len(x))


def process_command(lst, cmd):
    if cmd.startswith('+'):
        items = cmd[1:].split(",")
        add_to_list(lst, *items)
    elif cmd.startswith('-'):
        items = cmd[1:].split(",")
        remove_from_list(lst, *items)
    elif cmd.startswith('l'):
        print_list(lst)
    elif cmd.startswith('h'):
        print(help)
    elif cmd.startswith('c'):
        clear_list(lst)
    elif cmd.startswith('x'):
        return
    elif cmd.startswith('sn') or cmd.startswith("sl"):
        sort_list(lst, cmd[:2])
    else:
        if len(cmd) > 0:
            print(f"Unknown command {cmd[0]}")
        else:
            print(f"Empty command. {inputPrompt}")


def main():
    lst = []
    in_ = ' '
    while in_ != 'x':
        in_ = input(inputPrompt)
        process_command(lst, in_)
    print("Finished")


# this makes sure the main() is started (without this we don't do anything by running this script)
if __name__ == '__main__':
    main()
