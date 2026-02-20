from flask import Flask 
app = Flask(__name__)
@app.route('/')
def index():
    return "language translator"
if __name__ == '__main__':    
    app.run(debug=True)