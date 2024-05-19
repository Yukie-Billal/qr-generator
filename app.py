from flask import Flask, request, send_file
from generate_qr import generate_qr_code
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return "welcome, to generate qr access endpoint: POST /qrcode"


@app.route('/qrcode', methods=["POST"])
def qr_code():
    par = request.json

    try:
        filename = par['filename']
        text_qr = par['body']

        result_file , _ = generate_qr_code(text_qr, filename)

        return send_file(result_file)
    except Exception as e:
        print(e)
        return {'error': str(e)}


@app.route('/qrcode/matrix', methods=["POST"])
def qr_code_matrix():
    par = request.values

    try:
        from assets.qr_code_matrix import qr_code_matrix
        from utils.matrix_to_image import matrix_to_image
        print(par)

        filename = f"qr_code-{datetime.now().strftime('%d%m%Y')}.png"

        image = matrix_to_image(qr_code_matrix)
        image.save(f'public/{filename}')

        return send_file(), 200
    except Exception as e:
        print(e)
        return {'message': 'Internal server error'}, 500
    

if __name__ == "__main__":
    app.run(debug=True)
