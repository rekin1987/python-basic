import random

int = random.randint(0, 10)
lst = []

while int:
    lst.append(int)
    int = random.randint(0, 10)

print(lst)

for i, val in enumerate(lst):
    print("lst[" , i , "]=" , val)

print("max=" , max(lst))
print("min=" , min(lst))

print("count=",lst.count(5))

print(list(reversed(lst)))

random.shuffle(lst)

print(lst)

print(list(sorted(lst)))

for i, val in enumerate(lst):
    if val == 5:
        print("lst[" , i , "]=" , val)

