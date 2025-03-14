import sys

digit_string = sys.argv[1]

a = 0
for i in digit_string:
    a = a + int(i)
print(a)