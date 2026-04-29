from flask import Flask, request, jsonify, send_from_directory
import re

app = Flask(__name__, static_folder='.', static_url_path='')

CALM_PATTERNS = re.compile(r"\b(kiitos|hyvä|ok|okei|selvä|kiitokset|anteeksi|sorry)\b", re.IGNORECASE)
RAGE_PATTERNS = re.compile(
    r"\b(paska|vitun|saatana|olet huono|et ole|typerä|hitto|vittu)\b|mee töihin|sama housut|näytät ihan pete|pete parkkoselta|näytät biz|n-sana",
    re.IGNORECASE
)

RESPONSES = {
    'calm': 'Mauricio: Kiitos. Yritän rauhoittua.',
    'rage': 'MAURICIO SAA RAGEBAITIN! FAAH!!!',
    'neutral': 'Mauricio: Huh, yritän pysyä rauhallisena...'
}

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
    calmness = int(data.get('calmness', 100))

    if not user_message:
        return jsonify(error='Viestikenttä ei voi olla tyhjä.'), 400

    if RAGE_PATTERNS.search(user_message):
        reply_text = RESPONSES['rage']
        calm_change = -35
        rage = True
    elif CALM_PATTERNS.search(user_message):
        reply_text = RESPONSES['calm']
        calm_change = 10
        rage = False
    else:
        reply_text = RESPONSES['neutral']
        calm_change = -5
        rage = False

    calmness = max(0, min(calmness + calm_change, 120))
    game_over = calmness == 0

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
