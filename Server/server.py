from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_airlines', methods=['GET'])
def get_airlines():
    response1 = jsonify({
        'airlines': util.get_airlines()
    })
    response1.headers.add('Access-Control-Allow-Origin', '*')
    return response1

@app.route('/get_deptime', methods=['GET'])
def get_deptime():
    response2 = jsonify({
        'departure_time': util.get_deptime()
    })
    response2.headers.add('Access-Control-Allow-Origin', '*')
    return response2

@app.route('/get_source', methods=['GET'])
def get_source():
    response3 = jsonify({
        'sources': util.get_source()
    })
    response3.headers.add('Access-Control-Allow-Origin', '*')
    return response3

@app.route('/get_destination', methods=['GET'])
def get_destination():
    response4 = jsonify({
        'destinations': util.get_destination()
    })
    response4.headers.add('Access-Control-Allow-Origin', '*')
    return response4

@app.route('/get_clstype', methods=['GET'])
def get_clstype():
    response5 = jsonify({
        'cls_types': util.get_clstype()
    })
    response5.headers.add('Access-Control-Allow-Origin', '*')
    return response5

@app.route('/predict_price', methods=['GET','POST'])
def predict_price():
    airline = request.form['airline']
    time = request.form['time']
    source = request.form['source']
    destination = request.form['destination']
    class_type = request.form['class_type']

    response = jsonify({
        'estimated_price': util.get_estimated_price(airline,time,source,destination,class_type)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    #response =  "123"
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run('localhost', 5000)
