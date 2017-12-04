
# https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/

def fibon_100(lst):

    while len(lst) < 100:
        yield lst.append(lst[-1]+lst[-2])
    return lst

lst_in = [1,2]
gen = fibon_100(lst_in)


print(list(gen))