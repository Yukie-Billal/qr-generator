import qrcode

def generate_qr_code(text, filename):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=12, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

text = "https://yukie.site/portofolio"
filename = "yukie_qr_link.png"

generate_qr_code(text, filename)
print(f"File saved at {filename}")
