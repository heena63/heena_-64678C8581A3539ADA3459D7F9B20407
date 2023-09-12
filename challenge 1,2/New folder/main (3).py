# 1.2 write a program that determines wheather a year entered by user is aleap yera or not using ifelif -else statements


def isLeapYear(year):
  if(year % 4 ==0 and year % 100 != 0)or year % 400 ==0:
    return True
  else:
    return False

year=2014

if isLeapYear(year):
  print("{} is a leap year".format(year))

else:
  print("{} is not a leap year".format(year))