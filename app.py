from flask import Flask
from apis.convert_to_qr import convert_to_qr_blueprint
from apis.show_color import show_color_blueprint
from apis.random_number import random_number_blueprint

app = Flask(__name__)
app.register_blueprint(convert_to_qr_blueprint)
app.register_blueprint(show_color_blueprint)
app.register_blueprint(random_number_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
