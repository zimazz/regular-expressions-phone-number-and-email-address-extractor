import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)?         # separator
    (\d{3})              # first 3 digits
    (\s|-|\.)          # separator
    (\d{4})              # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    )''', re.VERBOSE)

# Get the text of the clipboard
text = pyperclip.paste()

# Extract the email/phone from the text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)


allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)


# Copy the extracted email/phone to the clipboard
pyperclip.copy(results)
