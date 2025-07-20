#Use this to always make sure your message is scheduled at least 1–2 minutes ahead.

from datetime import datetime

now = datetime.now()
print("Current time:", now.strftime("%H:%M"))
