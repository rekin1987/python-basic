import string


def strip_non_alpha_chars(input_str):
    """In the given string, removes each occurrence of a char from string.punctuation except apostrophe"""
    # call replace for each char from string.punctuation
    for str in string.punctuation.replace("'", ""):
        input_str = input_str.replace(str, " ")

    # split into whole words
    lst = input_str.split()

    # iterate over list and remove apostrophe from both ends of each word, also make string lowercase
    for i in range(0, len(lst)):
        # strings are immutable, so need to override old with complete new one
        lst[i] = lst[i].strip("'").lower()

    return lst


def word_count(input_str):
    d = {}

    print(f"input: {input_str}")

    list_strings = strip_non_alpha_chars(input_str)

    list_strings.sort()
    # for each item in the list, create a dictionary with key as string and value as number of occurrences in the list
    for s in list_strings:
        d[s] = list_strings.count(s)

    print(f"output: {d}")

    return d
