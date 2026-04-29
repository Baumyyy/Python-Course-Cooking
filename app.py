from flask import Flask, request, jsonify, send_from_directory
import re

from session import GameSession
from characters import Mauricio
from analyzer import MessageAnalyzer
from game import CalmnessEngine

app = Flask(__name__, static_folder='.', static_url_path='')

CALM_PATTERNS = re.compile(
    r"\b(kiitos|hyvä|ok|okei|selvä|kiitokset|anteeksi|sorry)\b",
    re.IGNORECASE
)

RAGE_PATTERNS = re.compile(
    r"\b(paska|vitun|saatana|olet huono|et ole|typerä|hitto|vittu)\b"
    r"|mee töihin|sama housut|näytät ihan pete|pete parkkoselta|näytät biz|n-sana",
    re.IGNORECASE
)

# responses
RESPONSES = {
    'calm': 'Mauricio: Kiitos. Yritän rauhoittua.',
    'rage': 'MAURICIO SAA RAGEBAITIN! FAAH!!!',
    'neutral': 'Mauricio: Huh, yritän pysyä rauhallisena...'
}

# Create a single game session instance
session = GameSession(CALM_PATTERNS, RAGE_PATTERNS, RESPONSES)


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)


@app.route('/api/reply', methods=['POST'])
def reply():
    data = request.get_json(silent=True) or {}
    user_message = data.get('message', '').strip()

    if not user_message:
        return jsonify(error='Viestikenttä ei voi olla tyhjä.'), 400

    # Process message through the OOP game session
    reply_text, calm_change, calmness = session.process_message(user_message)

    game_over = calmness == 0
    rage = calm_change == -35  # same logic as before

    if game_over:
        reply_text = 'this is fine...'

    return jsonify(
        reply=reply_text,
        calmChange=calm_change,
        calmness=calmness,
        rage=rage,
        gameOver=game_over,
    )


if __name__ == '__main__':
    app.run(debug=True)
