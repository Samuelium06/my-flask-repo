from flask import Flask 

app = Flask(__name__)

@app.route('/')
def head():
    return 'Hello world, my name is Samuel!!!'


@app.route('/second')
def second():
    return 'This is second page and this is the second step!!!'

@app.route('/third')
def third():
    return 'This is third page and this is the thirth step!!!'

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id of this page is {id}'


if __name__ == '__main__':

    #app.run(debug=True)
    app.run(host= '0.0.0.0', port=80)