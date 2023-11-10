from flask import Flask, render_template, url_for

app = Flask(__name__)


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


@app.route('/Support')
def support():
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
