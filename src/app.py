from flask import Flask, jsonify

app = Flask(__name__)

def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers."""
    return a + b

@app.route('/health')
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy"})

@app.route('/sum/<int:a>/<int:b>')
def sum_numbers(a: int, b: int):
    """Endpoint to sum two numbers."""
    result = calculate_sum(a, b)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 