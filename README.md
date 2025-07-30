# Secure_Messaging_App-using-Fernet-and-Caesar

A responsive and user-friendly web application that allows users to send encrypted messages using two different cryptographic techniques:

- **Fernet Encryption** (Symmetric AES-based)
- **Caesar Cipher** (Shift-based classical cipher)

## ⚙️ Technologies Used
### 🔹 Frontend
- HTML5 + CSS3 (with animations)
- JavaScript (ES6)
### 🔹 Backend
- Python 3.x
- Flask web framework
- Cryptography (Fernet encryption)


## 📁 Project Structure
secure_messaging_app/
│
├── app.py # Main Flask application
├── secret.key # Auto-generated Fernet key file
│
├── templates/
│ └── index.html # Main web page
│
├── static/
│ ├── style.css # Styling and animations
│ └── script.js # Frontend logic for Caesar cipher & interaction
│
└── README.md 

## 📥 Installation & Running

### 🔧 Prerequisites
- Python 3.7+
- pip package manager

### 💻 Steps to Run
Install dependencies:
pip install flask cryptography

Run the app:
python app.py

Open in browser:
Navigate to http://localhost:5000 in your browser.

