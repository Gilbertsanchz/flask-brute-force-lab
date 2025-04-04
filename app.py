from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

# Simulated user database with hardcoded credentials (for testing only)
user_db = {
    "admin": "123456",
    "testuser": "password123"
}

# Dictionary to keep track of failed login attempts per username
failed_logins = {}

# Max number of allowed attempts before lockout
MAX_ATTEMPTS = 5

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data
        username = request.form.get('username')
        password = request.form.get('password')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Check if user has exceeded max failed attempts
        if failed_logins.get(username, 0) >= MAX_ATTEMPTS:
            return "🚫 Account locked due to too many failed attempts."

        # Check credentials
        if username in user_db and user_db[username] == password:
            return f"✅ Welcome {username}!"
        else:
            # Log the failed attempt to a local file
            with open('login_attempts.log', 'a') as log:
                log.write(f"[{timestamp}] Failed login for {username}: {password}\n")

            # Increment failed attempt counter
            failed_logins[username] = failed_logins.get(username, 0) + 1
            return "❌ Invalid username or password!"

    # Display basic login form
    return '''
        <form method="POST">
            Username: <input type="text" name="username" /><br>
            Password: <input type="password" name="password" /><br>
            <input type="submit" value="Login" />
        </form>
    '''

if __name__ == '__main__':
    # Start the local Flask server on port 34224
    app.run(port=34224)
