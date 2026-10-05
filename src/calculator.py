def fun1(x , y):
    return x+y

def fun2(x , y):
    return x-y

def fun3(x , y):
    return x*y


def fun4(x,y):
    return fun1(x,y) + fun2(x,y) + fun3(x ,y)

def fun5(x , y):
    if y == 0:
        raise ValueError("cannot divide by zero")
    return x/y