


lst = []
line = input("podaj 1")
while len(line)>0:
    lst.append(line)
    line = input("podaj cos ")

print(lst)

usun = input("co usunac")
if usun in lst:
    lst.remove(usun)
else:
    print("not in the list")

while usun in lst:
    lst.remove(usun)
else:
    print("aaa")

print(lst)

index = input("usun index ")
if 0 <= int(index) < len(lst):
    del lst[int(index)]
else:
    print("index poza zakresem")

print(lst)

while len(lst) > 0:
    print(lst.pop())

print("done")




