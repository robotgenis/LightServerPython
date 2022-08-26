
import time, flask
from flask import request
app = flask.Flask(__name__)


exampleFill = {"type":"fill","color":{"type":"rgb","value":[255,255,255]},"selection":["hexagon"]}

data = {"active":[{"type":"fill","color":{"type":"rgb","value":[255,255,255]},"selection":["hexagon"]}],"timestamp":time.time()}

tempData = {}
# use rgb or hsv?

# {index:"main.two.:2",value:[x,y,z]}     
# localhost:5000/set?index=main.two[2]&value=[x,y,z]

@app.route('/set', methods=["post"])
def routeSet():
    global data, tempData
    requestData = request.get_json()
    tempData = requestData
    index = requestData["index"]
    value = requestData["value"]
    
    content = data
    for i in index[:-1]:
        content = content[i]
    content[index[-1]] = value
    
    return data


@app.route('/append', methods=["post"])
def routeAppend():
    global data
    requestData = request.get_json()
    index = requestData["index"]
    value = requestData["value"]
    
    content = data
    for i in index:
        content = content[i]

    content.append(value)

    return data   

@app.route('/pop', methods=["post"])
def routePop():
    global data
    requestData = request.get_json()
    index = requestData["index"]
    
    content = data
    for i in index[:-1]:
        content = content[i]

    content.pop(index[-1])

    return data 

@app.route('/get')
def routeGet():
    global data
    return data

@app.route('/gettemp')
def routeGetTemp():
    global tempData
    return tempData

if __name__ == '__main__':
   app.run()