#
# Example file for formatting time and date output
# LinkedIn Learning Python course by Joe Marini
#


from datetime import datetime

def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes 
    now = datetime.now() # get the current date and time
    
    #### Date Formatting ####
    
    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print (now.strftime("The current year is: %Y")) # full year with century
    print (now.strftime("%a, %d %B, %y")) # abbreviated day, num, full month, abbreviated year
    
    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print (now.strftime("Locale date and time: %c"))
    print (now.strftime("Locale date: %x"))
    print (now.strftime("Locale time: %X"))
    
    #### Time Formatting ####
    
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print (now.strftime("Current time: %I:%M:%S %p")) # 12-Hour:Minute:Second:AM
    print (now.strftime("24-hour time: %H:%M")) # 24-Hour:Minute


if __name__ == "__main__":
    main()
