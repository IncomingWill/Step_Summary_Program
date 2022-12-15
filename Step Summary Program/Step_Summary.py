# Title: Step Summary Program
# Program created by William Schaeffer
# CPS 313
# P. 359, Exercise 12, Step Summary Program
# 02.01.22

# This program will read the steps.txt file to calculate the average number of steps taken during each day of each month

# GLOBAL VARIABLES FOR DAYS IN EACH MONTH

MONTH_ONE = 31          #JANUARY
MONTH_TWO = 28          #FEBRUARY
MONTH_THREE = 31        #MARCH
MONTH_FOUR = 30         #APRIL
MONTH_FIVE = 31         #MAY
MONTH_SIX = 30          #JUNE
MONTH_SEVEN = 31        #JULY
MONTH_EIGHT = 31        #AUGUST
MONTH_NINE = 30         #SEPTEMBER
MONTH_TEN = 31          #OCTOBER
MONTH_ELEVEN = 30       #NOVEMBER
MONTH_TWELVE = 31       #DECEMBER

# Main Function

def main():
    
    welcome_function()                                  # Call welcome function
    
    step_file = open('steps.txt', 'r')                  # Open steps.txt

    print(f'MONTH\t\tAVERAGE STEPS')
    print(f'=============================\n')

    #print each month and calculated average steps

    print(f'JANUARY:\t', end='')
    calc_avg(step_file, MONTH_ONE)

    print(f'FEBRUARY:\t', end='')
    calc_avg(step_file, MONTH_TWO)

    print(f'MARCH:\t\t', end='')
    calc_avg(step_file, MONTH_THREE)

    print(f'APRIL:\t\t', end='')
    calc_avg(step_file, MONTH_FOUR)

    print(f'MAY:\t\t', end='')
    calc_avg(step_file, MONTH_FIVE)

    print(f'JUNE:\t\t', end='')
    calc_avg(step_file, MONTH_SIX)

    print(f'JULY:\t\t', end='')
    calc_avg(step_file, MONTH_SEVEN)

    print(f'AUGUST:\t\t', end='')
    calc_avg(step_file, MONTH_EIGHT)

    print(f'SEPTEMBER:\t', end='')
    calc_avg(step_file, MONTH_NINE)

    print(f'OCTOBER:\t', end='')
    calc_avg(step_file, MONTH_TEN)

    print(f'NOVEMBER:\t', end='')
    calc_avg(step_file, MONTH_ELEVEN)

    print(f'DECEMBER:\t', end='')
    calc_avg(step_file, MONTH_TWELVE)

    step_file.close()                                   # Close numbers.txt


# Function Definition

def welcome_function():                                 # Function to welcome user

    print(f'Welcome to the Calculate Monthly !\n\n')
    
def calc_avg(file, days):                               # Function to calculate average

    sum = 0                                             # set sum to zero
    for count in range(days):                           # loop through each line in file and add each step count
        sum += int(file.readline())

    avg = sum / days                                    # calculate average by dividing accumulated sum by number of days in month
    print(f'{avg:,.1f}')

main()                                                  # Call main function

