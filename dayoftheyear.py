from sys import argv

from calendar import weekday, day_name

[day, month, year] = map(int, argv[1:])

print day_name[weekday(year, month, day)]
