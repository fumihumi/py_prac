import flask 
import urllib.request, json, requests

app = flask.Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/ISC')
def hello2():
    return 'ISC routing'

@app.route('/XSS')
def XSS():
    return "<script>alert('alert')</script>"

@app.route("/ISC/<id>")
def parameter(id=0):
    return f'parameter is : {id}'

@app.route("/zip/<zipcode>")
def zip(zipcode):
    address = zip2address(zipcode)
    return address

def zip2address(zipcode):
    hostUrl = "http://zipcloud.ibsnet.co.jp/api/search"
    headers = {
        'Content-Type' : 'application/json',
    }
    payload = {'zipcode': zipcode}
    r = requests.get(hostUrl, params = payload).text
    print(r)
    return r

if __name__ == '__main__':
    app.run(debug=True)

