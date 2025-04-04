# Flask Brute-Force Lab

This is a safe and educational project for learning how brute-force attacks work in a local environment. It includes:

- A Flask-based login app (`app.py`)
- A brute-force testing script (`attack.py`)
- Sample wordlists for usernames and passwords

⚠️ **For ethical hacking education only. Never use against systems you don't own or have explicit permission to test.**

## How to Run

1. Install Flask if you don't have it:
   ```
   pip install flask
   ```

2. Start the Flask app in one terminal:
   ```
   python app.py
   ```

3. In another terminal, run the brute-force script:
   ```
   python attack.py
   ```

4. It will try every combination of usernames and passwords until it finds a match.

## Files

- `app.py`: Local login server with lockout and logging
- `attack.py`: Brute-force testing tool
- `usernames.txt`: List of test usernames
- `testpwlist.txt`: List of test passwords
- `.gitignore`: Excludes logs and caches
- `login_attempts.log`: Gets created automatically during testing
