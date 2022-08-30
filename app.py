
import time, flask
app = flask.Flask(__name__)


data = {"active":[],"preset":{
    "on":[{"type": "animationStop"},{"type":"fill","color":{"type":"rgb","value":[130,80,60]},"selection":[{"name":"hexagon"}, {"name":"x"}]},{"type":"fill","color":{"type":"rgb","value":[0,0,0]},"selection":[{"name":"vertical"},{"name":"line"},{"name":"bed"}]}],
    "daylight":[{"type": "animationStop"},{"type":"fill","color":{"type":"rgb","value":[130,80,10]},"selection":[{"name":"hexagon"}, {"name":"x"}, {"name":"line"}]},{"type":"fill","color":{"type":"rgb","value":[0,0,0]},"selection":[{"name":"vertical"},{"name":"bed"}]}],    
    "night":[{"type": "animationStop"},{"type":"fill","color":{"type":"rgb","value":[0,0,1]},"selection":[{"name":"hexagon"},{"name":"bed"}, {"name":"line"}]},{"type":"fill","color":{"type":"rgb","value":[0,0,0]},"selection":[{"name":"vertical"},{"name":"x"}]}],
    "off":[{"type": "animationStop"},{"type":"fill","color":{"type":"rgb","value":[0,0,0]},"selection":[{"name":"vertical"},{"name":"line"},{"name":"hexagon"},{"name":"x"},{"name":"bed"}]}]
},"timestamp":time.time()}

# use rgb or hsv?

# {index:"main.two.:2",value:[x,y,z]}     
# localhost:5000/set?index=main.two[2]&value=[x,y,z]

@app.route('/set', methods=["post"])
def routeSet():
    global data, tempData
    requestData = flask.request.get_json()
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
    requestData = flask.request.get_json()
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
    requestData = flask.request.get_json()
    requestData["type"] = "pop"
    index = requestData["index"]
    
    content = data
    for i in index[:-1]:
        content = content[i]

    content.pop(index[-1])

    data["timestamp"] = time.time()
    data["lastrequest"] = requestData
    return data 

@app.route('/preset/<path:path>')
def routePreset(path):
    global data

    if path in data["preset"]:
        preset = data["preset"][path]

        data["active"].extend(preset)
        data["timestamp"] = time.time()
        return data
    
    return "ERROR"

@app.route('/get')
def routeGet():
    global data
    return data


if __name__ == '__main__':
   app.run()