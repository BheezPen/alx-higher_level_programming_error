#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    firstletter = 10
    secondletter = 5

    print("{} + {} = {}".format(firstletter, secondletter, add(firstletter, secondletter)))
    print("{} - {} = {}".format(firstletter, secondletter, sub(firstletter, secondletter)))
#
#,
#
    print("{} * {} = {}".format(firstletter, secondletter, mul(firstletter, secondletter)))
    print("{} / {} = {}".format(firstletter, secondletter, div(firstletter, secondletter)))
#secondletter
