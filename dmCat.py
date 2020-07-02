# To be used on en.wikinews

import sys
from sys import argv
from datetime import datetime
import pywikibot as pwb

# Global declaration
daysCount = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Lambda declaration
isLeap = lambda year : (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

# Is the input correct?
if(len(argv) != 3):
  print("Usage: `python pwb.py dmCat.py [Month] [year]")
  sys.exit(-1)

month = int(argv[1])
year = int(argv[2])
curYear = datetime.now().year
curMonth = datetime.now().month

# Is year passed
if(year < curYear):
  print("Year is already in the past.")
  sys.exit(0)

# Is Month valid
if(month in range(1, 13)):
  if(month < curMonth and year == curYear):
    print("Month is already in the past.")
    sys.exit(0)
else:
  print("Invalid month.")
  sys.exit(0)

if(isLeap(year)):
  daysCount[2] = 29

days = daysCount[month]

monthName = months[month]

site = pwb.Site()
page = pwb.Page(site, u"Category:{0} {1}".format(monthName, year))
text = page.text

if(text == ''):
  page.text = u"{{Monthcategory}}"
  page.save(u"Create")

for date in range(1, days + 1):
  title = "Category:{0} {1}, {2}".format(monthName, date, year)
  page = pwb.Page(site, title)
  text = page.text
  if(text == ''):
    page.text = u"{{Datecategory}}"
  page.save(u"Create")

  title = "Wikinews:{0}/{1}/{2}".format(year, monthName, date)
  page = pwb.Page(site, title)
  text = page.text
  if(text == ''):
    page.text = "{{DateDPL|{0}|{1}|{2}}}".format(date,monthName,year)
  page.save(u"Create")

print("Done!")
