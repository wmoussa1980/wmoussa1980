def get_month():

    month = int(input("Enter month (1-12): "))
    return month

def get_year():
    
    year = int(input("Enter year: "))
    return year   

def get_month_name(month):
    
    month_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month_name = month_name[month-1]
    return month_name

def check_leap_year(year):

    if year % 4 == 0:

        return True

    else:

        return False


def get_month_days(month, year):
    leap_year = check_leap_year
    month_days = [31, (28,29), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year == True:
        month_days = month_days[month-1][1]
    else:
         month_days = month_days[month-1][0]
                    
    
    return month_days



def main():
    
    while(True):
        year = get_year()
        month = get_month()
        month_name = get_month_name(month)
        month_days = get_month_days(month, year)
        
        print()

        if(year > 0 and month > 0 and month <= 12):


           print(month_name)
           print(month_days)

        else: 
            print("Invalid Year or Month entered!!")
            break
    

    

main()    
