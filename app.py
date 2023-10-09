from flask import Flask, jsonify
from apis.convert_to_qr import convert_to_qr_blueprint
from apis.show_color import show_color_blueprint
from apis.random_number import random_number_blueprint

app = Flask(__name__)
app.register_blueprint(convert_to_qr_blueprint)
app.register_blueprint(show_color_blueprint)
app.register_blueprint(random_number_blueprint)

# Add a route to display all registered routes as clickable links
@app.route('/list_routes')
def list_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':  # Exclude static routes
            route_info = {
                'endpoint': rule.endpoint,
                'methods': ','.join(rule.methods),
                'path': rule.rule
            }
            # Generate clickable HTML links
            route_info['link'] = f'<a href="{rule.rule}">{rule.rule}</a>'
            routes.append(route_info)
    
    # Create an HTML list of clickable links
    links_html = '<ul>'
    for route_info in routes:
        links_html += f'<li>{route_info["link"]} - Methods: {route_info["methods"]}</li>'
    links_html += '</ul>'
    
    return links_html

if __name__ == '__main__':
    app.run(debug=True)
