from flask import Flask, render_template, redirect, url_for, request, session, flash
import smtplib
import imghdr
from email.message import EmailMessage
import os
# Development only
# import env as config

app = Flask(__name__)

# Development only
# app.config['SECRET_KEY'] = config.SECRET_KEY
# portfolio_username = config.portfolio_username
# portfolio_password = config.portfolio_password

# Email config
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_ADDRESS = config.EMAIL_ADDRESS
# EMAIL_PASSWORD = config.EMAIL_PASSWORD
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_PORT = 587

portfolio_username = os.environ.get('portfolio_username')
portfolio_password = os.environ.get('portfolio_password')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# Route for home page
@app.route('/')
def index():
    return render_template('index.html', title='Jacqueline Walsh - Portfolio')

# Route for portfolio page
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title='Jacqueline Walsh - Portfolio of Work')

# Route for testimonials page
@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html', title='Jacqueline Walsh - Testimonials of Work')

# Route for cv page
@app.route('/cv')
def cv():
    return render_template('cv.html', title='Jacqueline Walsh - Curriculum Vitae')

# Route for contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        company = request.form['company']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # contacts = ['EMAIL_ADDRESS', 'test@example.com']

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = email
        msg['To'] = EMAIL_ADDRESS

        message_body = f'From: {name}\n\nCompany: {company}\n\nEmail: {email}\n\nSubject: {subject}\n\n{message}'

        msg.set_content(message_body)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            # smtp.sendmail(msg)

        flash(f'Thank you for contacting me, I will get back to you shortly', 'success')
    return render_template('contact.html', title='Jacqueline Walsh - Contact Me')

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != portfolio_username or request.form['password'] != portfolio_password:
            flash(f'Invalid Credentials. Please try again.', 'danger')
        else:
            session['username'] = request.form['username']
            flash(f'You are successfully logged in', 'success')
            return redirect(url_for('cv'))
    return render_template('login.html', title='Jacqueline Walsh - Login for CV')

# logout
@app.route('/logout')
def logout():
    if 'username' in session:
        session.clear()
        flash(f'You are now logged out', 'success')
    return redirect(url_for('login'))

# 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='Portfolio - 404'), 404

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=False)

# Development only
# app.run(host=os.environ.get('IP'),
#         port=os.environ.get('PORT'),
#         debug=True)
