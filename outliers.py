# When analysing data collected as part of a science experiment it may be desirable to remove the most extreme values
# before performing other calculations. Write a function that takes a list of values and an non-negative integer, n, as
# its parameters. The function should create a new copy of the list with the n largest elements and the n smallest
# elements removed. Then it should return the new copy of the list as the function’s only result. The order of the
# elements in the returned list does not have to match the order of the elements in the original list. Write a main
# program that demonstrates your function. Your function should read a list of numbers from the user and remove the two
# largest and two smallest values from it. Display the list with the outliers removed, followed by the original list.
# Your program should generate an appropriate error message if the user enters less than 4 values.
#
# The Python Workbook by Ben Stephenson, problem 106

def input_list():
    number_list = []
    while True:
        number = int(input("What is a number ?\n"))
        if number == 0:
            break
        else:
            number_list.append(number)
    if len(number_list) < 3:
        return None
    return number_list


def is_smaller_than_all(number_list, number):
    for n in number_list:
        if number > n:
            return False
    return True


def remove(n, number_list):
    list_copy = []
    sorted_list = sorted(number_list)
    for i in range(len(sorted_list)):
        if n <= i < len(sorted_list) - n:
            list_copy.append(sorted_list[i])
    return list_copy


def main():
    n = int(input("How many outliers do you want to remove ?\n"))
    number_list = input_list()
    print(remove(n, number_list))


if __name__ == '__main__':
    main()
