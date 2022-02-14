from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("/home/webmob/Krunal_Work_space/Python/Python_Project/Pro-7:Generate_QRcode/1.png")

result = decode(img)

print(result)