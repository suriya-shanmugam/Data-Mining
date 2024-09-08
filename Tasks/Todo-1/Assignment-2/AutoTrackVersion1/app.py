from flask import Flask, request, jsonify, render_template
from spends_handler import SpendsHandler
from image_processor import process_image
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
spends_handler = SpendsHandler()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/expense', methods=['GET', 'POST', 'PUT', 'DELETE'])
def expense_action():
    if request.method == 'GET':
        expenses = spends_handler.get_expenses()
        return jsonify(expenses)
    elif request.method == 'POST':
        data = request.json
        result = spends_handler.create_expense(data)
        return jsonify(result)
    elif request.method == 'PUT':
        data = request.json
        result = spends_handler.update_expense(data)
        return jsonify(result)
    elif request.method == 'DELETE':
        expense_id = request.args.get('id')
        result = spends_handler.delete_expense(expense_id)
        return jsonify(result)

@app.route('/fetch_expense_from_image', methods=['POST'])
def fetch_expense_from_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        expense_data = process_image(filename)
        os.remove(filename)  # Remove the file after processing
        return jsonify(expense_data)

@app.route('/monthly_total')
def monthly_total():
    total = spends_handler.get_monthly_total()
    return jsonify({'total': total})

@app.route('/all_time_total')
def all_time_total():
    total = spends_handler.get_all_time_total()
    return jsonify({'total': total})

if __name__ == '__main__':
    app.run(debug=True)