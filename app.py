from flask import Flask, render_template, url_for, redirect
from flask import request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from scripts.send_message import send
from scripts.ciphers import caesar_cipher
from scripts.codings import base64_coder, morse_code_coder, bacon_coder, ascii_coder

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///email.db'

db = SQLAlchemy(app)


class Atricle(db.Model):
    date = str(datetime.now())[:-7]

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.String, default=date)

    def __repr__(self):
        return '<Article %r>' % self.id


with app.app_context():
    db.create_all()


@app.route('/')
def redirect_to_index():
    return redirect('/CryptoMaster')


@app.route('/CryptoMaster')
def index():
    return render_template('CryptoMaster.html')


@app.route('/CryptoMaster/QR-codings')
def qr_codings():
    return render_template('QR-codings.html')


@app.route('/CryptoMaster/Support', methods=['GET', 'POST'])
def support():
    if request.method == 'POST':
        email = request.form.getlist('email')
        message = request.form.getlist('message')
        article = Atricle(email=email[0], content=message[0])
        try:
            db.session.add(article)
            db.session.commit()
            send(message_data=str(message[0]), subject_data=str(email[0]))
            return redirect('/CryptoMaster/Support')
        except:
            return redirect('/CryptoMaster/Support')
    else:
        return render_template('Support.html')


@app.route('/CryptoMaster/Codings/Base64', methods=['GET', 'POST'])
def base64():
    if request.method == 'POST':
        input = request.form.getlist('input')
        radio = request.form.getlist('radio-group')
        try:
            if radio[0] == "encode":
                output = base64_coder.encode_base64(
                    str(input[0]))
            else:
                output = base64_coder.decode_base64(
                    str(input[0]))
        except:
            return render_template('codings/Base64.html', input=input[0], output="Error")
        return render_template('codings/Base64.html', input=input[0], output=output)
    else:
        return render_template('codings/Base64.html')


@app.route('/CryptoMaster/Codings/ASCII', methods=['GET', 'POST'])
def ASCII():
    if request.method == 'POST':
        input = request.form.getlist('input')
        radio = request.form.getlist('radio-group')
        try:
            if radio[0] == "encode":
                output = ascii_coder.encoder_ascii(
                    str(input[0]))
            else:
                output = ascii_coder.decoder_ascii(
                    str(input[0]))
        except:
            return render_template('codings/ASCII.html', input=input[0], output="Error")
        return render_template('codings/ASCII.html', input=input[0], output=output)
    else:
        return render_template('codings/ASCII.html')


@app.route('/CryptoMaster/Codings/Morse_code', methods=['GET', 'POST'])
def morse_code():
    if request.method == 'POST':
        input = request.form.getlist('input')
        radio = request.form.getlist('radio-group')
        try:
            if radio[0] == "encode":
                output = morse_code_coder.encoder_morse_code(
                    str(input[0]))
            else:
                output = morse_code_coder.decoder_morse_code(
                    str(input[0]))
        except:
            return render_template('codings/Morse_code.html', input=input[0], output="Error")
        return render_template('codings/Morse_code.html', input=input[0], output=output)
    else:
        return render_template('codings/Morse_code.html')


@app.route('/CryptoMaster/Codings/Bacon', methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        input = request.form.getlist('input')
        radio = request.form.getlist('radio-group')
        try:
            if radio[0] == "encode":
                output = bacon_coder.encoder_bacon(
                    str(input[0]))
            else:
                output = bacon_coder.decoder_bacon(
                    str(input[0]))
        except:
            return render_template('codings/Bacon.html', input=input[0], output="Error")
        return render_template('codings/Bacon.html', input=input[0], output=output)
    else:
        return render_template('codings/Bacon.html')


@app.route('/CryptoMaster/Ciphers/Caesar', methods=['GET', 'POST'])
def caesar():
    if request.method == 'POST':
        input = request.form.getlist('input')
        radio = request.form.getlist('radio-group')
        key = request.form.getlist('key')
        try:
            if radio[0] == "encrypt":
                output = caesar_cipher.encrypt_caesar(
                    str(input[0]), int(key[0]))
            else:
                output = caesar_cipher.decrypt_caesar(
                    str(input[0]), int(key[0]))
        except:
            return render_template('ciphers/Caesar.html', input=input[0], output="Error")
        return render_template('ciphers/Caesar.html', input=input[0], output=output)
    else:
        return render_template('ciphers/Caesar.html')


@app.route('/CryptoMaster/Ciphers/Xor')
def xor():
    return render_template('ciphers/Xor.html')


@app.route('/CryptoMaster/Ciphers/Atbash')
def atbash():
    return render_template('ciphers/Atbash.html')


if __name__ == '__main__':
    app.run(debug=True)
