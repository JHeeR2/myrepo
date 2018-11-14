from flask import Flask, request
import datetime
import os
os.chdir('C:\\Users\\d104-1\\Desktop\\work')

app = Flask(__name__)
with open("phone.txt") as f:
    lines = f.readlines()


@app.route('/')
def index():
    name=request.args.get('name')
    print(name, flush=True)

    for k in lines:
        a = k.split(',')
        if a[0] == name:
            print(a, flush=True)
            return a[0] +','+ a[1]
    return "not found"

@app.route('/cakes')
def cakes():
    print("/cakes", flush=True)
    return 'Yakes cakes!'

print("Waiting at port 5000", flush=True)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
