from flask import Flask, render_template, request, jsonify
from cryptography.fernet import Fernet
import os

app = Flask(__name__)

# Fernet Key Setup
if not os.path.exists("secret.key"):
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)
else:
    with open("secret.key", "rb") as f:
        key = f.read()

cipher = Fernet(key)

def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    mode = data.get('mode')
    message = data.get('message')

    if mode == 'fernet':
        encrypted = cipher.encrypt(message.encode()).decode()
        return jsonify({
            'status': 'success',
            'mode': 'fernet',
            'encrypted': encrypted,
            'key': key.decode()
        })

    elif mode == 'caesar':
        shift = int(data.get('shift', 0))
        encrypted = caesar_encrypt(message, shift)
        decrypted = caesar_decrypt(encrypted, shift)
        return jsonify({
            'status': 'success',
            'mode': 'caesar',
            'original': message,
            'encrypted': encrypted,
            'decrypted': decrypted,
            'shift': shift
        })

    return jsonify({'status': 'error', 'message': 'Invalid mode'})

if __name__ == "__main__":
    app.run(debug=True)
