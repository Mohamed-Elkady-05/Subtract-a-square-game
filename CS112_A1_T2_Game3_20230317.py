"""
File:CS112_A1_T2_THREE_20230317.py
Purpose: 2 players choosing a perfect square number to subtract from the starting the number the player who reaches zero
 wins
Author: Mohamed Ahmed Mohamed Mostafa Elkady
ID: 20230317
"""

import random


# This function explains the game rules

def game_menu():
    print("                      Subtract a square   ")
    print("  This is a two-player game of strategy. It is played by two people with a pile of coins between them.")
    print("  The players take turns removing coins form the pile, always removing a non-zero square number of coins")
    print("  (1,4,9,16,...). The player who removes the last coin win ")
    print("")
    print("                      start of the game")


# this function checks if the number is a perfect square or not
def num_vld(square):
    if square < 0:
        return False
    for i in range(1, int(square ** 0.5) + 1):
        if i * i == square:
            return square
    return False


# this function checks if the input is a number or not
def check_valid(nm):
    while not str(nm).isdigit():
        nm = input("Error enter an integer: ")
    return int(nm)


def choice():
    print("1) random number")
    print("2) choose the number by yourself")


def main():
    num = 0
    game_menu()
    choice()
    choose = input()
    choose = check_valid(choose)

    if int(choose) == 1:
        num = random.randint(10, 1000)
        print("the starting number is:", num)
    elif int(choose) == 2:
        num = input("Enter a starting number between 10 and 1000: ")
    else:
        while int(choose) != 1 and int(choose) != 2:
            choose = input("you have to choose between 1 , 2: ")
            choose = check_valid(choose)
            if int(choose) == 1:
                num = random.randint(10, 1000)
                print("the starting number is:", num)
            if int(choose) == 2:
                num = input("Enter a starting number between 10 and 1000:")
    num = check_valid(num)

    # the following while loop prevents the user from entering a number smaller than 10 or larger than 1000
    # it also prevents the user from entering a perfect square number as their starting number
    while num < 10 or num > 1000 or num_vld(num):
        if num < 10 or num > 1000:
            num = input("Enter a number between 10 and 1000: ")
            num = check_valid(num)
        else:
            num = input("Please enter a number which is NOT a perfect square number: ")
            num = check_valid(num)

    while num > 0:
        square = input("player one please take a square number: ")

        square = check_valid(square)

        while not num_vld(square):
            square = input("Enter a valid choice: ")
            square = check_valid(square)
        # if the user enters a number larger than the remaining number the program won't complete
        while square > num:
            square = input("Enter a number less than the current number: ")
            square = check_valid(square)

        # if the number becomes zero the last player to play will be the winner
        num -= square
        print("Now we have:", num)
        if num <= 0:
            print("Player one is winner")
            break

        square = input("player two please take a square number: ")

        square = check_valid(square)

        while not num_vld(square):
            square = input("Enter a valid choice: ")
            square = check_valid(square)

        while square > num:
            square = input("Enter a number less than the current number: ")
            square = check_valid(square)
        num -= square

        print("Now we have:", num)
        if num <= 0:
            print("Player two is winner")
            break


main()
