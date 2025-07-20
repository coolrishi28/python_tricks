import pywhatkit as kit
messages = ["Hello!", "How are you?", "This is Shashwat.", "Talk soon!"]
hour, minute = 18, 0

for msg in messages:
    kit.sendwhatmsg('+911234567890', msg, hour, minute)
    minute += 2  # space messages 2 minutes apart
