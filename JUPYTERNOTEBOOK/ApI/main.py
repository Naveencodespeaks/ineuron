# Api explanations:-
from flask import Flask, request, jsonify
# method are like GET,POST,PUT,UPDATE,DELETE
app = Flask(__name__)
# GET means posting a data in the form of URL
# POST  means posting the data in the form of Body

@app.route('/abc',methods = ['GET','POST'])
def test1():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        return jsonify((str(result)))
if __name__==('__main__'):
    app.run()
def test(a,b):
    return a+b

print(test(5,6))


