from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure random string

# Allowed user credentials
ALLOWED_USER = {
    'email': 'edwinmandi2002@gmail.com',
    'password': 'Mandiedu@1',
}


@app.route('/')
def index():
    if 'email' in session:
        return redirect(url_for('home'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == ALLOWED_USER['email'] and password == ALLOWED_USER['password']:
            session['email'] = email
            flash("Welcome, Edwin!", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid email or password. Please try again.", "danger")

    return render_template('login.html')


@app.route('/home')
def home():
    if 'email' not in session:
        flash("Please log in to access the home page.", "warning")
        return redirect(url_for('login'))

    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/history')
def history():
    return render_template('history.html')


@app.route('/logout')
def logout():
    session.pop('email', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))


@app.route('/forgot-password')
def forgot_password():
    flash("Password recovery is not available at the moment. Please contact support.", "info")
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
