import sys

digit_string = int(sys.argv[1])

number = digit_string
a = 0
b = 1
while a < digit_string:
    print(" "*(number-1), "#"*b)
    a = a + 1
    b = b + 1
    number = number - 1