from flask import Flask
from settings import *
from helpers import *

app = Flask(__name__)

### route that takes in a path param
@app.route('/<path:path>')
def catch_all(path):
    return get_answer(f"generate an html page containing info related to  {path} also generate links to related topics link should be a relative link and use the name of the topic")

if __name__ == '__main__':
    app.run(debug=True)
