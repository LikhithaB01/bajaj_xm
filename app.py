from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Ensure 'index.html' is in the 'templates' folder

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        # Extract data from the POST request
        data = request.json.get('data')
        if not data:
            return jsonify({
                "is_success": False,
                "error": "Invalid input"
            }), 400

        # Initialize arrays for numbers and alphabets
        numbers = []
        alphabets = []
        highest_lowercase = []

        # Separate numbers and alphabets
        for item in data:
            if item.isdigit():
                numbers.append(item)
            elif item.isalpha():
                alphabets.append(item)
                if item.islower():
                    highest_lowercase.append(item)

        # Determine the highest lowercase alphabet
        highest_lowercase.sort(reverse=True)
        highest_lowercase = highest_lowercase[:1]

        # Prepare the response
        response = {
            "is_success": True,
            "user_id": "21BEC2013",  # Replace with actual user_id if necessary
            "email": "bolineni.likhitha2021@vit.student.ac.in",  # Replace with actual email
            "roll_number": "21BEC2013",  # Replace with actual roll number
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": str(e)
        }), 500

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({
        "operation_code": 1
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
