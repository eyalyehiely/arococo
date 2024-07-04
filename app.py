from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
# app.secret_key = 'fghdfghdfefbgrgbrgbdfgbndfgndfnrhwrglwehg;qeorghpoeuhrg9q3h39t3y355723yt3giuerhiefvbiaefbgh'

# Configuration for mail server
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'designar40@gmail.com'
app.config['MAIL_PASSWORD'] = 'lalv jnco szjo ryjp'

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        phone = request.form.get('phone')

    #create email message
        msg = Message(subject=f" קיבלת הודעה חדשה מ:  {name}",
                      sender=('course', 'designar40@gmail.com'),
                      recipients=["designar40@gmail.com"])
        msg.body = f"Message from: {email}\n\n Phone number:{phone}\n\n{message}"

        # send email
        mail.send(msg)
        return "Email sent successfully! thank you"
    except Exception as e:
        app.logger.error(f"Error sending email: {e}")
        return "Error, please try again"


if __name__ == '__main__':
    app.run(debug=False)
