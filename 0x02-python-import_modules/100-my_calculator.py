#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    operator_dict = {'+': add, '-': sub,
                     '*': mul, '/': div}
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if argv[2] in operator_dict:
            result = operator_dict[argv[2]](int(argv[1]), int(argv[3]))
            print(f"{int(argv[1])} {argv[2]} {int(argv[3])} = {result}")
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
