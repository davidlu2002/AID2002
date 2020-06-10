def fun01(*args):
    print(args)
    print(type(args))

fun01(1,2,3,4,5)


def fun02(a=1,b=2):
    print("a =",a)
    print("b =",b)

fun02(**{"c":100,"b":200})
