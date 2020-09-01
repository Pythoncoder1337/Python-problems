# Positions on a chess board are identified by a letter and a number. The letter identifies the column,
# while the number identifies the row, as shown below:
# Missing Figure
# Write a program that reads a position from the user. Use an if statement to determine if the column begins with a
# black square or a white square. Then use modular arithmetic to report the color of the square in that row.
# For example, if the user enters a1 then your program should report that the square is black.
# If the user enters d5 then your program should report that the square is white.
# Your program may assume that a valid position will always be entered. It does not need to perform any error checking.

# The Python Workbook Problem 45 by Ben Stephenson

def odd(number):
    if number % 2 == 1:
        return True
    else:
        return False


def square_color(letter, number):
    LETTERS_ODD = ["a", "c", "e", "g"]
    LETTERS_EVEN = ["b", "d", "f", "h"]
    if (letter not in LETTERS_EVEN) and (letter not in LETTERS_ODD):
        return None
    elif letter in LETTERS_ODD and odd(number):
        return "black"
    elif letter in LETTERS_EVEN and not odd(number):
        return "black"
    else:
        return "white"


def main():
    letter = input("What is a chessboard letter?\n")
    number = int(input("What is a chessboard number?\n"))
    if square_color(letter, number) == "white":
        print("That coordinate is white")
    else:
        print("That coordinate is black")


if __name__ == "__main__":
    # execute only if run as a script
    main()
