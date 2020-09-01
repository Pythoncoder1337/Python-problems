# Write a program that reads integers from the user and stores them in a list. Use 0 as
# a sentinel value to mark the end of the input. Once all of the values have been read
# your program should display them (except for the 0) in reverse order, with one value
# appearing on each line.

# The Python Workbook Problem 105 by Ben Stephenson

def input_list():
    number_list = []
    while True:
        number = int(input("What is a number ?\n"))
        if number == 0:
            break
        else:
            number_list.append(number)
    return number_list


def reverse(a_list):
    reversed_list = []
    n = -1
    while n >= -len(a_list):
        reversed_list.append(a_list[n])
        n = n - 1
    return reversed_list


def reverse2(a_list):
    reversed_list = []
    for n in range(- 1, - len(a_list) - 1, -1):
        reversed_list.append(a_list[n])
    return reversed_list


def main():
    number_list = input_list()
    reversed_list = reverse(number_list)
    for n in reversed_list:
        print(n)


if __name__ == '__main__':
    main()
