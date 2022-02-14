import qrcode


data = "Don't Forget to Subscribe"

img = qrcode.make(data)

img.save("/home/webmob/Krunal_Work_space/Python/Python_Project/Pro-7:Generate_QRcode/1.png")