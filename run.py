from flask import Flask, render_template
import africastalking
import pandas as pd
from util.helper import save_data

app = Flask(__name__)

# Africastalking API Config
username = ""
API_KEY = ""
sms = africastalking.SMS

@app.route('/')
def render_homepage():
    return render_template('index.html')

@app.route('/dashboard')
def render_admin_dashboard():
    return render_template('admin.html')

@app.route('/api/v1/visualize')
def visualize_data():
    return "Visualizing data"

@app.route('/api/v1/sms')
def send_sms():
    return {
        'message': 'SMS sent successfully.',
        'status': 200
    }


if __name__ == '__main__':
    save_data()
    app.run(debug=True)