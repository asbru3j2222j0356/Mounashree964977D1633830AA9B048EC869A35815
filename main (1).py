def isleapYear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False


year = int(input("Enter a Year:"))
if isleapYear(year):
  print("{} is leapyear.".format(year))
else:
  print('{}is not a leap year.'.format(year))
