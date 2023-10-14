'''
Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
Function Description

Complete the print_formatted function in the editor below.

print_formatted has the following parameters:

int number: the maximum value to print
'''


def print_formatted(number):
    # your code goes here
    for i in range(1, number + 1):
        padding = len(bin(number)[2:]) + 1  # to include space sepration
        print(str(i).rjust(padding - 1) + oct(i)[2:].rjust(padding) + hex(i)[2:].upper().rjust(padding)
              + bin(i)[2:].rjust(padding))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
