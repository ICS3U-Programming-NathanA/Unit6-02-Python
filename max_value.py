#!/usr/bin/env python3

# Created by: Nathan Araujo
# Date: Dec.15, 2022
# This program generates 10 random numbers and
# prints the largest  out of the list of 10 random numbers, it then displays it

import random
import constants


def max_value(num_list):

    highest_num = -1

    # Use a for loop to see which number is the largest number in the list
    for counter in range(constants.MAX_ARRAY_SIZE):
        if num_list[counter] > highest_num:
            highest_num = num_list[counter]

    # return highest_num
    return highest_num


def main():
    # Creates a empty list called random_num
    random_num = []

    # For loop that generates 10 random number between 0 and 100
    for counter in range(constants.MAX_ARRAY_SIZE):

        # generates a number between 0 and 100
        random_int = random.randint(constants.MIN, constants.MAX)

        # Adds number to the list
        random_num.append(random_int)

        # print that it added the number to the index
        print(f"Added {random_int} to list at index {counter}")

    # Stores largest number generated in variable
    large_value = max_value(random_num)

    # Prints the largest number generated
    print(f"The max value is: {large_value}.")


if __name__ == "__main__":
    main()
