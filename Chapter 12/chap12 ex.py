import calendar
cal = calendar.TextCalendar()      # Create an instance
cal.pryear(2018)  # What happens here?
calendar.setfirstweekday(calendar.THURSDAY)
calendar.firstweekday()
#Returns the current setting for the weekday to start each week.

calendar.isleap(2018)

#Returns True if year is a leap year, otherwise False.

calendar.leapdays(2017, 2018)
#Returns the number of leap years in the range from y1 to y2 (exclusive), where y1 and y2 are years.

#This function works for ranges spanning a century change.

calendar.weekday(2018, 4, 19)
#Returns the day of the week (0 is Monday) for year (1970–…), month (1–12), day (1–31).

calendar.weekheader(7)
#Return a header containing abbreviated weekday names. n specifies the width in characters for one weekday.

calendar.monthrange(2018, 1)
#Returns weekday of first day of the month and number of days in month, for the specified year and month.

calendar.monthcalendar(2018, 4)
#Returns a matrix representing a month’s calendar. Each row represents a week; days outside of the month a represented by zeros. Each week begins with Monday unless set by setfirstweekday().

calendar.prmonth(2018, 4, w=0, l=0)
#Prints a month’s calendar as returned by month().

calendar.month(2018, 5, w=0, l=0)
#Returns a month’s calendar in a multi-line string using the formatmonth() of the TextCalendar class.

calendar.prcal(2018, w=0, l=0, c=6, m=3)
#Prints the calendar for an entire year as returned by calendar().

calendar.calendar(2018, w=2, l=1, c=6, m=3)
#Returns a 3-column calendar for an entire year as a multi-line string using the formatyear() of the TextCalendar class.

#calendar.timegm(tuple)
#An unrelated but handy function that takes a time tuple such as returned by the gmtime() function in the time module, and returns the corresponding Unix timestamp value, assuming an epoch of 1970, and the POSIX encoding. In fact, time.gmtime() and timegm() are each others’ inverse.

#The calendar module exports the following data attributes:

calendar.day_name
#An array that represents the days of the week in the current locale.

calendar.day_abbr
#An array that represents the abbreviated days of the week in the current locale.

calendar.month_name
#An array that represents the months of the year in the current locale. This follows normal convention of January being month number 1, so it has a length of 13 and month_name[0] is the empty string.

calendar.month_abbr
#An array that represents the abbreviated months of the year in the current locale. This follows normal convention of January being month number 1, so it has a length of 13 and month_abbr[0] is the empty string.

