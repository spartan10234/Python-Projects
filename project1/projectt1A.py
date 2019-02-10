"""
Program: CS 115 Project 1
Author: Eduardo Roman
Description: Using input from the user, this program will calculate the (WCT) of a location using
temperature (T) and wind velocity (V).
"""
def main():
    print('==> Windchill Temperature (WTC) Weather Report Calculator <==')
    num_locations= int(input('Select the number of locations for the report: '))
    decimal_precision = int(input('Select the decimal precision for the report [1--4]: '))
    total=0
    lowest_temp=100

    for i in range (1, num_locations+1):
        location_name= input('Enter name of ** Location '+ str(i) +' **:')
        temp_int = int(input('\tEnter air temperature [in deg F]: '))
        vel_int= int(input('\tEnter wind velocity [in mph]: '))
        wtc_equ = 35.74 + 0.6215 * temp_int - 35.75 * (vel_int ** 0.16) + 0.4275 * temp_int * (vel_int ** 0.16)
        final_precision= round(wtc_equ, decimal_precision)
        total += final_precision
        if final_precision<lowest_temp:
            new_location=location_name
            lowest_temp=final_precision

        print('WCT is', final_precision,'deg F.')
    print()
    print('***Summary***')
    print('WTC')
    avg_wtc= round(total/num_locations, decimal_precision)
    print('\tAvg recorded WCT:', avg_wtc,'deg F')
    print('\tLocation with lowest WTC:', new_location, '('+ str(lowest_temp)+')', 'F')








main()