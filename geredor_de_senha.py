from flask import Flask, render_template, request, redirect, jsonify
import string
import secrets

app = Flask(__name__)

def generate_password(length=28):
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            return password

@app.route('/gerar_senha')
def gerar_senha():
    password = generate_password()
    return jsonify({'password': password})

@app.route('/')
def index():
    return render_template('login.html')

registered_users = []

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    registered_users.append({'username': username, 'password': password})
    return redirect('/users')

@app.route('/users')
def users():
    return render_template('users.html', users=registered_users)

if __name__ == '__main__':
    app.run(debug=True)
