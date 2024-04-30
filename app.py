import qrcode
from flask import Flask, request, send_file
from generate_qr import generate_qr_code

app = Flask(__name__)

@app.route('/')
def index():
    return "welcome, to generate qr access endpoint: POST /qrcode"

@app.route('/qrcode', methods=["POST"])
def qr_code():
    par = request.json
    print(par)

    try:
        filename = par['filename']
        text_qr = par['body']

        result_file , _ = generate_qr_code(text_qr, filename)

        return send_file(result_file)
    except Exception as e:
        print(e)
        return {'error': str(e)}

if __name__ == "__main__":
    app.run()
