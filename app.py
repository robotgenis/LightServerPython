
import time, flask
app = flask.Flask(__name__)

data = {}

@app.route('/set')
def routeSet():
    global data
    data = {"timestamp": time.time(), "value": flask.request.args.get("value", default="")}
    return data
   

@app.route('/get')
def routeGet():
    global data
    return data


if __name__ == '__main__':
   app.run()