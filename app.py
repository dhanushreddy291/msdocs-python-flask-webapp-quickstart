from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_data():
    data = {
        'name': 'Dhanush',
        'age': 20,
        'city': 'Hyderabad'
    }
    return jsonify(data)

if __name__ == '__main__':
   app.run()
