from flask import Flask, render_template, request
import qrcode
import time
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    app_link = request.form['app_link']
    random_suffix = str(int(time.time()))
    unique_link = f"{app_link}?random={random_suffix}"
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(unique_link)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image to a BytesIO object
    img_bytes = io.BytesIO()
    img.save(img_bytes)
    img_bytes.seek(0)  # Move to the beginning of the BytesIO buffer
    
    # Encode the image to base64 for inline display
    img_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')
    
    return render_template('index.html', qr_code=img_base64)

if __name__ == '__main__':
    app.run(debug=True)