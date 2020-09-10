# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
month = input("Enter the month of the year (Jan - Dec): ")
day = int(input("Enter the day of the month: "))
season = ""

# if march or before
if months.index(month) <= 2:
    #likely Winter but dbl check
    if month == "Mar" and day > 18:
        season = "Spring"
    else:
        season = "Winter"
# if before june 
elif months.index(month) <= 5:
    #likely Spring but dbl check
    if month == "Jun" and day > 19:
        season = "Summer"
    else: 
        season = "Spring"
# if before september 21 
elif months.index(month) <= 8:
    #likely Summer but dbl check
    if month == "Sep" and day > 21:
        season = "Fall"
    else: 
        season = "Summer"
# if before september 21 
else:
    #likely Fall but dbl check
    if month == "Dec" and day > 19:
        season = "Winter"
    else: 
        season = "Fall"
    
print(f"{month} {day} is in {season}")

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

