from datetime import datetime

now = datetime.now()
print(now)

# Format: Abbreviated weekday, month, 2-digit year
time_1 = now.strftime("%a %m %y")
print(time_1)

# Format: Full weekday, full year
time_2 = now.strftime("%A %m %Y")
print(time_2)

# Format: 12-hour time with AM/PM and seconds
time_3 = now.strftime("%I %p %S")
print(time_3)

# Format: Day of the year
time_4 = now.strftime("%j")
print(time_4)
