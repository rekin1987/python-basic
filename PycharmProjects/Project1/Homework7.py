from datetime import datetime


def fibon(n):
    lst = [0, 1]
    yield lst[0]
    yield lst[1]
    for i in range(2, n + 1):
        elem = lst[-1] + lst[-2]
        yield elem
        lst.append(elem)


def main():
    elements = 5000
    start_time = datetime.now()
    idx = 0
    for it in fibon(elements):
        print(f"fib[{idx}]={it}")
        idx += 1
    print(f"Calculated {elements} in {datetime.now()-start_time}")


# Calculated 5000 in 0:00:00.090851


if __name__ == '__main__':
    main()
