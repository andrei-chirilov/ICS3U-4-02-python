#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: Oct 2019
# This program does DO looping


def main():
    answer = 1
    counter = 0

    integer = int(input("What is your number: "))

    while counter < integer:
        counter = counter + 1
        answer = answer * counter

    print("The answer is " + str(answer))


if __name__ == "__main__":
    main()
