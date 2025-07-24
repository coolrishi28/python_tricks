from datetime import datetime

date = datetime.now()

# Format: Full month name, day, year
fulld = date.strftime("%B %d, %Y")
print(fulld)

# Format: Time with AM/PM
ftime = date.strftime("%I:%M:%S %p")
print(ftime)
