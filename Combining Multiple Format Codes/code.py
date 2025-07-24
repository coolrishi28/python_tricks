from datetime import datetime

now = datetime.now()

currf = now.strftime("Today is %A, %B %d, %Y")
print(currf)

# Common log format: DD/MM/YYYY HH:MM:SS
lformat = now.strftime("%d/%m/%Y %H:%M:%S")
print(lformat)
