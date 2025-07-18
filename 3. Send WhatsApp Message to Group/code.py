# Group ID must be copied from WhatsApp Web's invite link.
# The first parameter inside the function is the group id which needs to be copied as it is from WhatsApp Web's invite link.

import pywhatkit as kit
kit.sendwhatmsg_to_group('ABCD1234EFG5678HIJKL', 'Hello group!', 14, 5)
