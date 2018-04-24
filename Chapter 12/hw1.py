#1
#a
import calendar
cal = calendar.TextCalendar()      # Create an instance
cal.pryear(2012)  # What happens here?

#b
cal = calendar.TextCalendar(1)
cal.pryear(2018)

#c
cal = calendar.TextCalendar(1)
cal.prmonth(2018,11)

#d
d = calendar.LocaleTextCalendar(6, "CHINESE")
d.pryear(2012)

#e
print(calendar.isleap(0))

