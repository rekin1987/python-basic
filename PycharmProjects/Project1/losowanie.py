from random import shuffle
import os

lst1 = "Maciek, Gabrysia, Wojtek, Asia, Paweł, Monika".split(', ')
lst2 = "Maciek, Gabrysia, Wojtek, Asia, Paweł, Monika".split(', ')

"""Returns True if list1 items are different than list2 items."""
def diff_list(list1, list2):
    for i in range(0, len(list1)):
        if list1[i] == list2[i]:
            return False
    return True


def save_to_file(name, content):
    fullName = "Prezenty/" + name+".txt"
    if os.path.exists(fullName):
        os.remove(fullName)
    with open(fullName, "w") as text_file:
        text_file.write("{0}".format(content))


if not os.path.exists("Prezenty"):
    os.makedirs("Prezenty")

areDiff = diff_list(lst1, lst2)
assert areDiff is False
while not diff_list(lst1, lst2):
    print("shuffle")
    shuffle(lst2)

areDiff = diff_list(lst1, lst2)
assert areDiff is True

for i in range(0, len(lst1)):
    content = lst1[i] + " kupuje dla -> " + lst2[i]
    # print(content)
    save_to_file(lst1[i], content)




