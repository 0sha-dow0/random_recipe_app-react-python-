from flask import Flask
from main import generateData

app = Flask(__name__)


@app.route('/dish')
def message():
    return generateData()

if __name__ =='__main__':
    app.run(debug=True,port=8888)