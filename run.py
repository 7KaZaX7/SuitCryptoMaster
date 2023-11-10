from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime
from flask import request

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
@app.route('/CryptoMaster')
def index():
    return render_template('CryptoMaster.html')


@app.route('/Codings')
def codings():
    return render_template('Codings.html')


@app.route('/Ciphers')
def ciphers():
    return render_template('Ciphers.html')


@app.route('/QR-codings')
def qr_codings():
    return render_template('QR-codings.html')


@app.route('/Support', methods=['GET', 'POST'])
def support():
    if request.method == 'POST':
        email = request.form.getlist('email')
        message = request.form.getlist('message')
        article = Atricle(email=email[0], content=message[0])
        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/Support')
        except:
            return redirect('/Support')
    else:
        return render_template('Support.html')


@app.route('/Base64')
def base64():
    return render_template('codings/Base64.html')


@app.route('/ASCII')
def ASCII():
    return render_template('codings/ASCII.html')


@app.route('/Morse_code')
def morse_code():
    return render_template('codings/Morse_code.html')


@app.route('/Bacon')
def bacon():
    return render_template('codings/Bacon.html')


@app.route('/Caesar')
def caesar():
    return render_template('ciphers/Caesar.html')


@app.route('/Xor')
def xor():
    return render_template('ciphers/Xor.html')


@app.route('/Atbash')
def atbash():
    return render_template('ciphers/Atbash.html')


if __name__ == '__main__':
    app.run(debug=True)
