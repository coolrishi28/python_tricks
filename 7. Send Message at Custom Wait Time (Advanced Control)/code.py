# Sends the message at 16:10, waits 10 seconds before sending, and closes tab after 3 seconds

import pywhatkit as kit
kit.sendwhatmsg('+911234567890', 'Timed message with control', 16, 10, wait_time = 10, tab_close = True, close_time = 3)
