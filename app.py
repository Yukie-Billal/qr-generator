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

        return {
            "result_file": result_file
        }
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

        matrix_to_image(qr_code_matrix)

        return {"message": "success"}, 200
    except Exception as e:
        print(e)
        return {'message': 'Internal server error'}, 500
    

@app.route('/barcode', methods=["POST"])
def barcode_simple():
    par = request.values

    try:
        from utils.binary_to_barcode import generate_simple_barcode
        print(par)

        filename = f"qr_code-{datetime.now().strftime('%d%m%Y')}.png"

        barcode_data = '101010101011110010100101010101010101010101011110010101010'  # Example binary string

        generate_simple_barcode(barcode_data)
        return {"message": "success"}, 200
    except Exception as e:
        print(e)
        return {'message': 'Internal server error'}, 500
    

if __name__ == "__main__":
    app.run(debug=True)
