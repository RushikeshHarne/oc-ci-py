from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from a Dockerized Python App!'

if __name__ == '__main__':
    # Run the application on all interfaces (0.0.0.0) and a standard port (5000)
    app.run(host='0.0.0.0', port=5000)
