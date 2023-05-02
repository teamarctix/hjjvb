import qrcode

from io import BytesIO
from flask import Blueprint, request, make_response

convert_to_qr_blueprint = Blueprint('convert_to_qr', __name__)


@convert_to_qr_blueprint.route('/api/convert-to-qr-code', methods=['GET'])
def convert_to_qr():
    url = request.args.get('q')
    if url is None:
        return "Error: No link provided. Please specify a URL."

    # Create QR code instance
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)

    # Create image from QR code instance
    img = qr.make_image(fill_color='black', back_color='white')

    # Save image to buffer
    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)

    # Return image as response
    response = make_response(buffer.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response
