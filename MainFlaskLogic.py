from flask import Flask, render_template, redirect, url_for, request
from flask_forms import RegisterForm
from database import create_table, add_user

app = Flask(__name__)

@app.route('/')
def main_page():
    create_table()
    return render_template('main.html')


@app.route('/register', GET=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        add_user(username=username, email=email, password=password)
        return redirect(url_for('second_page'))
    return render_template('register.html', form=form)


@app.route('/page')
def second_page():
    return render_template('second.html')


if __name__ == '__main__':
    app.run(debug=True)