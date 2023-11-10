#First we have to install the library from the terminal like: pip install qrcode Image
import qrcode

inp = input("Enter the data you want to make a QR CODE: ")

qr = qrcode.QRCode(
    version = 1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(inp)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")
print("That's it! Your QR Code is ready! Check your folder.")
