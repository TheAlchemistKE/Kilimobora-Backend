from flask import Flask, render_template
import africastalking

app = Flask(__name__)

# Africastalking API Config
username = ""
API_KEY = ""
sms = africastalking.SMS

@app.route('/')
def render_homepage():
    return render_template('index.html')


@app.route('/api/v1/upload', methods=['POST'])
def upload_data(data: dict) -> dict:
    return {
        'message': 'Data uploaded.'
    }

@app.route('/api/v1/visualize')
def visualize_data():
    return "Visualizing data"

@app.route('/api/v1/sms')
def send_sms():
    return "Sending data to the Farmer"


if __name__ == '__main__':
    app.run(debug=True)