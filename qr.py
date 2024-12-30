import qrcode
import random
import time

# Define the base app link
base_app_link = "https://www.youtube.com"

# Generate a random number or use the current time to make the link unique
random_suffix = str(int(time.time()))  # Using current timestamp as a unique suffix
# random_suffix = str(random.randint(1000, 9999))  # Alternatively, use a random number

# Create the full app link with a unique suffix
app_link = f"{base_app_link}?random={random_suffix}"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(app_link)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("app_link_qr.png")

print("QR code generated and saved as 'app_link_qr.png'")