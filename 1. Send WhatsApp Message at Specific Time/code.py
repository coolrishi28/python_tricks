#Send a WhatsApp message at 13:30 to a contact
#Format :- kit.sendwhatmsg('Phone Number', 'Message',Hours, Minutes)
#It follows 24-hour clock.

import pywhatkit as kit
kit.sendwhatmsg('+911234567890', 'Hello, this is a scheduled message!', 13, 30)
