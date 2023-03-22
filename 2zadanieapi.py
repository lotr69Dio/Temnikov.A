from flask import Flask, request

app = Flask(__name__)

@app.route('/sum2/', methods=['POST'])
def hello_world():
    print(request.json)
    dataa = request.json['data']
    print(dataa)
    summa = 0
    for i in dataa:
        summa += i
    return {'sum': summa}

@app.route('/sum3/', methods=['POST'])
def sum3():
    print(request.json)
    dataa = request.json['data']
    print(dataa)
    summa = 0
    for i in dataa:
        summa += i
    return {'sum': summa}

app.run(host="0.0.0.0", port=5000)