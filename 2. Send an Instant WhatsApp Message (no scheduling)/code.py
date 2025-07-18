# Sends a message instantly, waits for 15 seconds before sending

import pywhatkit as kit
kit.sendwhatmsg_instantly('+911234567890', 'Hello instantly!', wait_time = 15, tab_close = True)
