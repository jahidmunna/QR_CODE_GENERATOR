import io
import base64
import qrcode
from flask import Flask, render_template, request

app = Flask(__name__)
app.title = 'QR CODE GENERATOR'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    # get the employee id from the form
    employee_id = request.form['employee_id']

    # generate the QR code image using qrcode module
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(employee_id)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # convert the image to bytes using io module
    img_bytes = io.BytesIO()
    # img.save(img_bytes, format='PNG')
    img.save(img_bytes)
    img_bytes = img_bytes.getvalue()

    # encode the image as a base64-encoded string using base64 module
    img_b64 = base64.b64encode(img_bytes)

    # render the QR code image as a base64-encoded string on the qr.html template
    return render_template('qr.html', qr_image=img_b64)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1111, debug=True)
