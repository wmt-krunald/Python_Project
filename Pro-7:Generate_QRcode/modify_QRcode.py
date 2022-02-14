import qrcode

data = "Don't Forget to Subscribe"

qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)

qr.add_data(data)

qr.make(fit = True)

img = qr.make_image(fill_color = "red", back_color = "white")

img.save("/home/webmob/Krunal_Work_space/Python/Python_Project/Pro-7:Generate_QRcode/2.png")