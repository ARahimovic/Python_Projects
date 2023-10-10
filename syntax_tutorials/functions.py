def sum(num1 =0, num2=1):
    return num1 + num2

print(sum(5,6))
print(sum())


def multiple_args(*args):
    for i in args :
        print(i)

multiple_args("rahimovic", "insane physique", "Woohoo")

def multiple_kwArgs(**kwargs):
    print(type(kwargs))
    print(len(kwargs))
    return kwargs.items()

myTuple = multiple_kwArgs(first = "rahimovic", last="Hanma")
print(myTuple)

print False
