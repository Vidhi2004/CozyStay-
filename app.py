from flask import Flask, render_template, jsonify
from db import db
app = Flask(__name__)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html'), 201


@app.route('/guest', methods=['GET'])
def fetch_patients():
    cursor.execute('USE cozy')
    cursor.execute('SELECT * FROM guests')
    ans = cursor.fetchall()
    return jsonify(ans)

if __name__ == '__main__':
    app.run(debug=True)

#login 

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from db import db
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key
bcrypt = Bcrypt(app)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html'), 201

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        cursor.execute('USE cozy')
        cursor.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)', (username, email, hashed_password))
        db.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute('USE cozy')
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()

        if user and bcrypt.check_password_hash(user[3], password):  # Assuming user[3] is the password
            session['user_id'] = user[0]
            session['username'] = user[1]
            return redirect(url_for('index'))
        else:
            return 'Invalid credentials', 401
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/guest', methods=['GET'])
def fetch_patients():
    cursor.execute('USE cozy')
    cursor.execute('SELECT * FROM guests')
    ans = cursor.fetchall()
    return jsonify(ans)

if __name__ == '__main__':
    app.run(debug=True)
