#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
s1 = "Last digit of"
if number < 0:
    last_digit = -last_digit
if last_digit < 6:
    if last_digit == 0:
        print(s1, number, "is", last_digit, "and is 0")
    else:
        print(s1, number, "is", last_digit, "and is less than 6 and not 0")
else:
    print(s1, number, "is", last_digit, "and is greater than 5")
