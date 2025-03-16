import traceback
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'deepakjoc69@gmail.com'  # Your email
app.config['MAIL_PASSWORD'] = 'sjus qife hrvw oaih'  # Use your Gmail App Password
app.config['MAIL_DEFAULT_SENDER'] = 'deepakjoc69@gmail.com'

mail = Mail(app)

@app.route('/send-message', methods=['POST'])
def send_message():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')

        if not name or not email or not subject or not message:
            return jsonify({"error": "All fields are required."}), 400

        # Compose Email
        msg = Message(
            subject=f"New Contact Form Submission: {subject}",
            recipients=['deepakjoc69@gmail.com'],  # Your email
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        )

        mail.send(msg)
        return jsonify({"message": "Email sent successfully!"}), 200

    except Exception as e:
        print("❌ ERROR:", str(e))  # Print error to the terminal
        print(traceback.format_exc())  # Show full error details
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
