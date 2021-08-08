import pdb

def breakpoint():
    print("There's a breakpoint here")
    pdb.set_trace()

def division(x, y):
    # breakpoint()
    result = x / y
    print(result)

    # y could potentially be 0, which is not ideal in division. So we un-comment the breakpoint and see what goes wrong.


def addition(x, y):
    # breakpoint()
    result = x + y
    print(result)

    # input() takes in a string as input, so when we apply the method it adds them as a string
    # so we un-comment the breakpoint and watch step by step where the error is.
