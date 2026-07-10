import qrcode

# The data you want to encode in the QR code
data = "https://forms.gle/KxtKLWSnBUN35gau9"

# Configure the QR code generator
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # About 7% error correction
    box_size=10,  # How many pixels each "box" of the QR code is
    border=4,  # Thickness of the border (minimum is 4)
)

# Add the website link to the QR code object
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code instance
# You can customize the fill color and background color here
img = qr.make_image(fill_color="black", back_color="white")

# Display the QR code image on your screen
print("Displaying QR code for Class Registration...")
img.show()

# Optional: Save the image to your computer
# img.save("reg_qr.png")