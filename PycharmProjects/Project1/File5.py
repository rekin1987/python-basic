
inputPrompt = "enter item ('x' to exit, '+' to add, '-' to remove, 'l' to show list)\n"
in_ = ' '

list = []

while in_ != 'x':
    in_ = input(inputPrompt)
    if in_.startswith('+'):
        substrList = in_[1:].split(',')
        for substr in substrList:
            if substr in list:
                print(substr + " already on the list")
            else:
                list.append(substr.strip().lower())
    elif in_.startswith('-'):
        substrList = in_[1:].split(',')
        for substr in substrList:
            if substr not in list:
                print(substr + " NOT on the list")
            else:
                list.remove(substr)
    elif in_.startswith('l'):
        print(list)
        list2 = []
        for item in list:
            list2.append(item.capitalize())
        print("List contains: %s" % list2)
        print(f"List contains2: {list2}")
    elif in_.startswith('x'):
        pass
    else:
        print("wrong starting char")

print("finished")