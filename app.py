from flask import Flask, render_template, redirect, url_for, request, session, flash
import env as config

app = Flask(__name__)

app.config['SECRET_KEY'] = config.SECRET_KEY
portfolio_username = config.portfolio_username
portfolio_password = config.portfolio_password

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
  app.run(debug=True)