import qrcode
import os
from datetime import datetime

def generate_qr_code(text, filename):
    if len(str(filename).split('')) <= 1:  filename = f"{datetime.now().strftime('%d%m%Y')}-{filename}.png"
    else: filename = f"{datetime.now().strftime('$d$m$Y')}-{filename}"

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=12, border=4)
    qr.add_data(text)
    if not os.path.exists("public"):
        os.makedirs("public")
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    save_path = f"public/{filename}"
    img.save(save_path)
    return save_path, img