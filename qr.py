import qrcode

# Data jo QR code mein hona chahiye
data = "https://youtu.be/KhVIzqMqTYY?si=HnkdqCKkYGgL6J8f"

# QR code banane ka process
qr = qrcode.QRCode(
    version=1,  # Version control karta hai QR code ka size (1 se 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Ek box ka size (pixels mein)
    border=4,  # Border ka size (boxes mein)
)

# Data add karna
qr.add_data(data)
qr.make(fit=True)

# QR code ka image banana
img = qr.make_image(fill='black', back_color='red')

# Image ko save karna
img.save("qrcode.png")

print("QR code successfully generated and saved as qrcode.png")
