def strip_non_alpha_chars(s):
    if len(s) == 1:
        return s

    frontSkip = 0
    backSkip = 0
    for ch in s:
        if ch.isalpha():
            break  # break on first occurrence
        frontSkip += 1

    ss = reversed(s)

    for ch in ss:
        if ch.isalpha():
            break  # break on first occurrence
        backSkip += 1

    return s[frontSkip: len(s) - backSkip]


def check_alpha(s):
    for ch in s:
        if ch == "'" or ch.isalnum():
            pass
        else:
            return False
    return True


def word_count(s):
    d = {}

    print(f"input: {s}")

    # transform ',' into ' '
    initial_list = s.split(",")
    ss = " ".join(initial_list)
    # transform '_' into ' '
    initial_list = ss.split("_")
    ss = " ".join(initial_list)
    # split on any blank char (space, tab, new line)
    initial_list = ss.split()

    # to lower case and strip spaces
    for i in range(0, len(initial_list)):
        initial_list[i] = initial_list[i].lower().strip()
    # remove non alpha digits at the front and end of each string
    for i in range(0, len(initial_list)):
        initial_list[i] = strip_non_alpha_chars(initial_list[i])

    list_strings = []
    for item in initial_list:
        if item not in list_strings and check_alpha(item):
            list_strings.append(item)

    list_strings.sort()
    for sss in list_strings:
        d[sss] = initial_list.count(sss)

    print(f"output: {d}")

    return d
