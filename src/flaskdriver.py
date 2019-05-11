import os
from flask import Flask, request, jsonify, redirect
from pocowork import readLongURL, saveShortURL, generateShortURL
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

app = Flask(__name__)
dbname = 'data/Urls.db'
strlen = 10
host = os.environ['BASEURL']
port = os.environ['PORT']

@app.route('/<path>')
def getLongURL(path):
    if request.method == 'GET':
        print('Getting longURL for ' + path)
        result, error = readLongURL(dbname, path)
        if error is None and result is not None:
            return redirect(result)
        else:
            result = '''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /> 
<title></title> 
</head>
<body>
<PRE> 
Move along now, there's nothing to see here.

~~____)-)
/   -(0 0)-
\_____\~/
 // \\ `
Don't be a goat. 
</PRE> 
</body>
</html>
            '''
            return result

@app.route("/add", methods=['POST'])
def getShortURL():
    if request.method == 'POST':
        try:
            longURLParm = request.values['text']
        except Exception as e:
            error = str(e)
            return jsonify(["error:" + error])
        print('About to process ' + longURLParm)
        shortUrl = generateShortURL(strlen, longURLParm)
        print('\nPersisting shortURL: ' + shortUrl)
        result, error = saveShortURL(dbname, shortUrl, longURLParm)
        if error is None and result is not None:
            return "Your shortened URL is: " + host + shortUrl
        else:
            return jsonify(["error:" + error])

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=os.environ["PORT"])
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(int(port), address="0.0.0.0")
    IOLoop.instance().start()

