# Comments go here ...

# References go here ...


def get_month():
    month = int(input("Enter month (1-12): "))
    return month


def get_year():    
    year = int(input("Enter year: "))
    return year   


def get_month_name(month):    
    month_name = ["January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"]

    month_name = month_name[month - 1]
    return month_name


def check_leap_year(year):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False


def get_month_days(month, year):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    leap_year = check_leap_year(year)
    if leap_year:
        days[1] = 29

    month_days = days[month - 1]
    return month_days


def display_results(month_name, year, month_days):
    print(f"{month_name} {year} has {month_days} days")


def main():
    while True:
        year = get_year()
        month = get_month()
        if year <= 0 or month < 1 or month > 12:
            break

        month_name = get_month_name(month)
        month_days = get_month_days(month, year)
        display_results(month_name, year, month_days)


main()    
