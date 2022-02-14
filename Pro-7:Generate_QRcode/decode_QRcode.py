import cv2

detector = cv2.QRCodeDetector()

data,point,s_qr = detector.detectAndDecode(cv2.imread("/home/webmob/Krunal_Work_space/Python/Python_Project/Pro-7:Generate_QRcode/2.png"))
print("\n", data)

print("\nPoints: ")
print("\n", point)

print("\n", s_qr)

# img = Image.open("/home/webmob/Krunal_Work_space/Python/Python_Project/Pro-7:Generate_QRcode/1.png")

# result = decode(img)

# print(result)