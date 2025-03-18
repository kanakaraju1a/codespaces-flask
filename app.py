from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    username = os.getenv("USER") or os.getenv("USERNAME")

    # Get current IST time
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    
    # Get `top` command output (Linux systems)
    try:
        top_output = subprocess.getoutput("top -b -n 1 | head -10")
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"

    # Render output
    return f"""
    <html>
    <head><title>/htop</title></head>
    <body>
        <h2>Name: Your Full Name</h2>
        <h2>Username: {username}</h2>
        <h2>Server Time (IST): {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</h2>
        <h2>Top Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
