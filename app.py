from flask import Flask, request, jsonify
from flask_cors import CORS
from jeologic import * 
from cases import *

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/generateJeopardy/make=<make>', methods=['POST'])
@app.route('/generateJeopardy/make=<make>/levels=<levels>', methods=['POST'])
@app.route('/generateJeopardy/make=<make>/levels=<levels>/subtopics=<subtopics>', methods=['POST'])
def generate_jeopardy(make, levels=500, subtopics=5):
    # Your logic here
    if levelTest(levels):
        if subtopicTest(subtopics):
            return generateJeopardy(str(make), int(levels), int(subtopics))
        else:
            return ("Invalid")
    else:
        return ("Invalid")



#@app.route("/generateJeopardy/make=<make>/level=<level>/numberoftopics=<>")

#@app.route("")

if __name__ == '__main__':
    app.run(debug=True)