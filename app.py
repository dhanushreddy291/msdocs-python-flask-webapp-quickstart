from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_data():
    data = {
        'name': 'John',
        'age': 30,
        'city': 'New York'
    }
    return jsonify(data)

if __name__ == '__main__':
   app.run()
