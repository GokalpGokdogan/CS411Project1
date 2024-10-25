import os
import sqlite3
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__) 

app.secret_key = 'abcdefgh'
  
USER_TABLE = "data"
USER_DB_FILE = "user.db"
  
def checkPassword(username, password):
    db_file = os.path.join(USER_TABLE, USER_DB_FILE)
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    cursor.execute(f"SELECT id, user FROM user WHERE user = '{username}' and password = '{password}'")
    user = cursor.fetchall()
    connection.close()
    return user

@app.route('/')

@app.route('/login', methods =['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        result = checkPassword(username, password)
        if len(result) > 0:
            user = result[0]              
            session['loggedin'] = True
            session['userid'] = user[0]
            session['username'] = user[1]
            message = 'Logged in successfully!'
            return redirect(url_for('main_page'))
        else:
            message = 'Please enter correct email / password!'
    return render_template('login.html', message = message), 401

@app.route('/main_page')
def main_page():
    return render_template('main_page.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
