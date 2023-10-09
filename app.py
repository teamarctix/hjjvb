from flask import Flask, jsonify
from apis.convert_to_qr import convert_to_qr_blueprint
from apis.show_color import show_color_blueprint
from apis.random_number import random_number_blueprint

app = Flask(__name__)
app.register_blueprint(convert_to_qr_blueprint)
app.register_blueprint(show_color_blueprint)
app.register_blueprint(random_number_blueprint)

# Add a route to display all registered routes
@app.route('/list_routes')
def list_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':  # Exclude static routes
            routes.append({
                'endpoint': rule.endpoint,
                'methods': ','.join(rule.methods),
                'path': rule.rule
            })
    return jsonify({'routes': routes})

if __name__ == '__main__':
    app.run(debug=True)
