import json
import re
# Example 1

# Sample input
text = """
Hi there, contact me at john.doe123@gmail.com or contact me at office@company.org. 
You can also try jane-doe@work.net or something@not-an-email.
"""

# Your code here
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.(?:com|org|net)\b', text)
print(emails)


# Example 2

# Sample input
log_data = """
192.168.1.1 - - [12/Jun/2023:10:15:32 +0000] "GET /index.html"
10.0.0.2 - - [13/Jun/2023:11:20:55 +0000] "POST /submit"
"""
pattern = r'(\d{1,3}(?:\.\d{1,3}){3}) - - \[([^\]\s]+)'
matches = re.findall(pattern, log_data)
print(matches)
# Expected output: [('192.168.1.1', '12/Jun/2023:10:15:32'), ...]

# Example 3


# Sample input
passwords = ["Welcome123", "abc", "NOLOWERCASE1", "validPass1"]
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
for password in passwords:
    if re.fullmatch(pattern, password):
        print(password)


# Expected output: only valid passwords

# Example 4
tweets = [
    "Excited about #Python3 🐍 and #AI!",
    "Loving the vibes of #Kazakhstan 🇰🇿 #travel #fun_times"
]
pattern = r'#\w+'

all_hashtags = []
for tweet in tweets:
    hashtags = re.findall(pattern, tweet)
    all_hashtags.extend(hashtags)

print(all_hashtags)
# Expected output: ['#Python3', '#AI', '#Kazakhstan', '#travel', '#fun_times']

# Example 5

# Sample input
phones = ["+7 701 123 4567", "87011234567", "7-701-123-45-67"]

# Expected output: ["+7 (701) 123-45-67", ...]


def normalize_phone(text):
    digits = re.sub(r'\D', '', text)
    if digits.startswith('8'):
        digits = '7' + digits[1:]
    if len(digits) == 11:
        return f'+7 ({digits[1:4]}) {digits[4:7]}-{digits[7:9]}-{digits[9:11]}'
    else:
        return "Invalid number"


numbers = ['+7 701 123 4567', '87011234567', '7-701-123-45-67']
for num in numbers:
    print(normalize_phone(num))
