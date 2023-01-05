#!/usr/bin/python3

# prints last digit of number

def print_last_digit(number):
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
