import pywhatkit as pwk

# Define recipient's phone number and message
phone_number = "+91 7842422375"
message = "Hello,Bharathi!"

# Set time to send the message (24-hour format)
send_hour = 23       # 11 PM
send_minute = 30     # 30 minutes past the hour

# Send the message
pwk.sendwhatmsg(phone_number, message, send_hour, send_minute)
