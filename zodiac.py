# Write a program that asks the user to enter his or her month and day of birth. Then
# your program should report the user’s zodiac sign as part of an appropriate output
# message. See book for full text.
# The Python Workbook by Ben Stephenson, problem 47

days_in_month_map = {"january": 31, "february": 28, "march": 31, "april": 30, "may": 31, "june": 30, "july": 31,
                     "august": 31, "september": 30, "october": 31, "november": 30, "december": 31}
months_list = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
               "november", "december"]

zodiac_list = ["capricorn", "aquarius", "pisces", "aries", "taurus", "gemini", "cancer", "leo",
               "virgo", "libra", "scorpio", "sagittarius"]


def day_of_year(month, day):
    d = day
    for m in months_list:
        if month == m:
            return d
        d = d + days_in_month_map[m]


def zodiac(month, day):
    capricorn_start = day_of_year("december", 22)
    aquarius_start = day_of_year("january", 20)
    pisces_start = day_of_year("february", 19)
    aries_start = day_of_year("march", 21)
    taurus_start = day_of_year("april", 20)
    gemini_start = day_of_year("may", 21)
    cancer_start = day_of_year("june", 21)
    leo_start = day_of_year("july", 23)
    virgo_start = day_of_year("august", 23)
    libra_start = day_of_year("september", 23)
    scorpio_start = day_of_year("october", 23)
    sagittarius_start = day_of_year("november", 23)
    days = day_of_year(month, day)
    if capricorn_start <= days < aquarius_start:
        return "capricorn"
    elif aquarius_start <= days < pisces_start:
        return "aquarius"
    elif pisces_start <= days < aries_start:
        return "pisces"
    elif aries_start <= days < taurus_start:
        return "aries"
    elif taurus_start <= days < gemini_start:
        return "taurus"
    elif gemini_start <= days < cancer_start:
        return "gemini"
    elif cancer_start <= days < leo_start:
        return "cancer"
    elif leo_start <= days < virgo_start:
        return "leo"
    elif virgo_start <= days < libra_start:
        return "virgo"
    elif libra_start <= days < scorpio_start:
        return "libra"
    elif scorpio_start <= days < sagittarius_start:
        return "scorpio"
    elif sagittarius_start <= days < capricorn_start:
        return "sagittarius"
    else:
        return None


def zodiac2(month, day):
    zodiac_starts = [day_of_year("december", 22),
                     day_of_year("january", 20),
                     day_of_year("february", 19),
                     day_of_year("march", 21),
                     day_of_year("april", 20),
                     day_of_year("may", 21),
                     day_of_year("june", 21),
                     day_of_year("july", 23),
                     day_of_year("august", 23),
                     day_of_year("september", 23),
                     day_of_year("october", 23),
                     day_of_year("november", 23)]
    days = day_of_year(month, day)
    for i in range(len(zodiac_starts)):
        if zodiac_starts[i] <= days < zodiac_starts[(i + 1) % 12]:
            return zodiac_list[i]
    return None


def main():
    month = input("What is your birth month ?\n")
    day = int(input("What is your birth day ?\n"))
    print("Your zodiac sign is", zodiac(month, day))
    print("Your zodiac is", zodiac2(month, day))


if __name__ == '__main__':
    main()
