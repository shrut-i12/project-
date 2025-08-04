from flask import Flask, render_template, request, redirect, url_for, session
import random
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "your_secret_key_here"
app.permanent_session_lifetime = timedelta(minutes=30)

EMOJIS = ['🍕', '🍔','🍟','🌭','🍿','🥞','🧇','🥯','🌯','🌮','🥪','🍘','🍱','🍜','🧁','🍧' ]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=['POST'])
def game():
    level = request.form.get('level')
    size = {'easy': 4, 'medium': 6, 'hard': 8}[level]
    total_cards = (size * size) // 2

    selected_emojis = random.sample(EMOJIS * 2, total_cards) * 2
    random.shuffle(selected_emojis)

    session['score'] = 0
    session['moves'] = 0

    return render_template('game.html', emojis=selected_emojis, size=size, level=level)

@app.route('/quit')
def quit_game():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
