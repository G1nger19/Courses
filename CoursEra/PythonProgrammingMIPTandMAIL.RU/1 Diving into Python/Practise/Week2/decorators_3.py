def decorator1(func):
    def wrapped():
        print("in first decorator")
        return func()
    return wrapped

def decorator2(func):
    def wrapped():
        print("in second decorator")
        return func()
    return wrapped


@decorator1
@decorator2
def decorated():
    print("Finaly")

decorated()