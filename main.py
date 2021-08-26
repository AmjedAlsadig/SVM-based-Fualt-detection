from flask import Flask,render_template,request, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
from model import predict
from numpy import double

@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/request', methods=["POST"])
# @cross_origin()
def predicto():
    v1 = float(request.form["v1"])
    v2 = float(request.form["v2"])
    v3 = float(request.form["v3"])
    i1 = float(request.form["i1"])
    i3 = float(request.form["i3"])
    i2 = float(request.form["i2"])
    # return v1 * 3
    arr2 = [[v1, v2, v3, i1, i2, i3]]
    result = predict(arr2)[0]
    # print(result)
    output = {
        1 : "No fault",
        2 : "Single phasing",
        3 : "unbalanced voltage",
        4 : "under voltage",
        5 : "over voltage",
        6 : "locked rotor",
        7 : "overload",
    }
    return jsonify(output[result])

# if __name__ == '__main__' :
#     app.run(debug=True,port=5000)
