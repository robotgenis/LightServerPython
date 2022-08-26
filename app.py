
import time, flask
from flask import request
app = flask.Flask(__name__)


exampleFill = {"type":"fill","color":{"type":"rgb","value":[255,0,0]},"selection":["hexagon"]}

data = {"active":[{"type":"fill","color":{"type":"rgb","value":[255,0,0]},"selection":["hexagon"]}],"timestamp":time.time()}

# use rgb or hsv?

# {index:"main.two.:2",value:[x,y,z]}     
# localhost:5000/set?index=main.two[2]&value=[x,y,z]

@app.route('/set', methods=["post"])
def routeSet():
    global data, tempData
    requestData = request.get_json()
    requestData["type"] = "set"
    index = requestData["index"]
    value = requestData["value"]
    
    content = data
    for i in index[:-1]:
        content = content[i]
    content[index[-1]] = value

    data["timestamp"] = time.time()
    data["lastrequest"] = requestData
    return data


@app.route('/append', methods=["post"])
def routeAppend():
    global data
    requestData = request.get_json()
    requestData["type"] = "append"
    index = requestData["index"]
    value = requestData["value"]
    
    content = data
    for i in index:
        content = content[i]

    content.append(value)

    data["timestamp"] = time.time()
    data["lastrequest"] = requestData
    return data   

@app.route('/pop', methods=["post"])
def routePop():
    global data
    requestData = request.get_json()
    requestData["type"] = "pop"
    index = requestData["index"]
    
    content = data
    for i in index[:-1]:
        content = content[i]

    content.pop(index[-1])

    data["timestamp"] = time.time()
    data["lastrequest"] = requestData
    return data 

@app.route('/get')
def routeGet():
    global data
    return data


if __name__ == '__main__':
   app.run()