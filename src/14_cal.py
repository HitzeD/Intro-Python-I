"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# instatiate datetime
date = datetime.now()

# set firstday of the week to sunday rather than monday
calendar.setfirstweekday(6)


userInput = input("Enter the year in a YYYY format: ")


if( int(userInput) > 1000 and int(userInput) < 10000 ):

	# calendar.month(year, month, row spacing, column spacing)
	print(calendar.month(int(userInput), date.month, 2, 1))
else:
	print(calendar.month(date.year, date.month, 2, 1))

