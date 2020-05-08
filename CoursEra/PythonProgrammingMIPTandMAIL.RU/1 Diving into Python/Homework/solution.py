import sys

digit_string=sys.argv[1]

summary=0
for number in digit_string:
    summary+=int(number)
print(summary)