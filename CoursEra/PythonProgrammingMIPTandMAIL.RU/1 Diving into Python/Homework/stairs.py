import sys

digit_sting=sys.argv[1]
digit=int(digit_sting)
digit_lattice = digit
while digit!= 0:
    print(" "*(digit-1)+"#"*(digit_lattice-digit+1))
    digit -= 1

#   for i in range(num_steps):
#       print(" " * (num_steps - i - 1), "#" * (i + 1), sep="")