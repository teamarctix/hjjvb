from flask import Blueprint, jsonify
import random

random_number_blueprint = Blueprint('random_number', __name__)

@random_number_blueprint.route('/api/random-number/<int:num1>/<int:num2>')
def random_number(num1, num2):
    if num1 < num2:
        response = jsonify({'random_number': random.randint(num1, num2)})
        response.status_code = 200
        return response
    else:
        response = jsonify({'message': 'Invalid input, num2 should be greater than num1'})
        response.status_code = 400
        return response
