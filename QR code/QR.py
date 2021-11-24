import qrcode
qr = qrcode.QRCode(
    version=6,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=100,
    border=4,
)
img = qrcode.make("https://www.google.com/")
img = qr.make_image(fill_color="rgb(66, 133, 244)", back_color="rgb(52, 168, 83)")
img.save("Google1.jpg")