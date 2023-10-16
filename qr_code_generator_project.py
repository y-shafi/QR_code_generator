import qrcode

qr = qrcode.QRCode(
    version= 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data('INSERT YOUR LINK HERE')

img = qr.make_image()
img.save('qrcode.jpg')