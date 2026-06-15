import pywhatkit as kit

# Phone number with country code (replace with the real number)
phone_number = "+91 9390745228"

# Message you want to send
message = "Hello! This message is sent using Python."

# Send instantly (opens WhatsApp Web in your browser)
kit.sendwhatmsg_instantly(phone_number, message)

print("Message sent successfully!")
