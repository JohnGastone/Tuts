# In Python we can use dates by importing a module named datetime

# These dates can be utilised via date objects

# Example 1 : Displaying the current date

import datetime


leo = datetime.datetime.now()

print(leo)

# Example 1 : Displaying the current year

print(leo.year)

# Example 1 : Displaying the current month
print(leo.month)


# Example 1 : Displaying the current date of the month
print(leo.day)


# Creating Custom Date Objects

tarehe_yetu = datetime.datetime(2005, 8, 21, 18, 32, 57)

print(tarehe_yetu.hour)


# String Format Time method

siku = datetime.datetime(2012, 12, 29, 17, 10, 6)

print(siku.str('%A:%d:%B:%Y'))

# String parse time - The strptime function is typically used in programming languages, such as Python,
# to parse (convert) a string representing a date
# and time into a structured date and time object.

# Example date string
date_string = "2023-09-14 15:30:00"

# Define the format of the date string using format codes
format_code = "%Y-%m-%d %H:%M:%S"

# Use strptime to parse the string into a datetime object
parsed_datetime = datetime.strptime(date_string, format_code)

# Now you can work with the parsed datetime object
print("Parsed Datetime:", parsed_datetime)
print("Year:", parsed_datetime.year)
print("Month:", parsed_datetime.month)
print("Day:", parsed_datetime.day)
print("Hour:", parsed_datetime.hour)
print("Minute:", parsed_datetime.minute)
print("Second:", parsed_datetime.second)

# Keywords

'''
%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%C	Century	20	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%	
%G	ISO 8601 year	2018	
%u	ISO 8601 weekday (1-7)	1	
%V	ISO 8601 weeknumber (01-53)	01

'''
