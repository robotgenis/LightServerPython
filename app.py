
import time, flask
app = flask.Flask(__name__)


presets = {
    "on":[{"type": "animationStop"},{"type":"fill","color":{"type":"rgb","value":[130,80,60]},"selection":[{"name":"hexagon"}, {"name":"x"}]},{"type":"fill","color":{"type":"rgb","value":[0,0,0]},"selection":[{"name":"vertical"},{"name":"line"},{"name":"bed"}]}],
    "daylight":[{"type": "animationStop"},{"type":"fill","color":{"type":"rgb","value":[0,0,0]},"selection":[{"name":"vertical"},{"name":"line"},{"name":"hexagon"},{"name":"x"},{"name":"bed"}]},{
			"type":"sequence",
			"id":"seq",
			"elements":[
				{
					"delay": 0,
					"type": "animationFill",
					"id": "fill1",
					"selection": [{"name":"hexagon"}, {"name":"x"}, {"name":"line"}],
					"colorAnimation": {
						"type": "rgb",
						"value": [
							[{"type":"transformation","points":[[0,1],  [2,130], [8, 130]]}],
							[{"type":"transformation","points":[[0,1], [2,80], [8, 80]]}],
							[{"type":"transformation","points":[[0,1],  [2,10], [8, 10]]}]
						]
					}
				},
				{
					"delay": 3,
					"type": "animationStop"
				}
			]
		}
	],    
    "night":[{"type": "animationStop"},{"type":"fill","color":{"type":"rgb","value":[0,0,1]},"selection":[{"name":"hexagon"},{"name":"bed"}, {"name":"line"}]},{"type":"fill","color":{"type":"rgb","value":[0,0,0]},"selection":[{"name":"vertical"},{"name":"x"}]}],
    "off":[{"type": "animationStop"},{"type":"fill","color":{"type":"rgb","value":[0,0,0]},"selection":[{"name":"vertical"},{"name":"line"},{"name":"hexagon"},{"name":"x"},{"name":"bed"}]}]
}

data = {"active":[],"timestamp":time.time()}

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
    return "Success"


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
    return "Success"

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
    return "Success"

@app.route('/preset/<path:path>')
def routePreset(path):
    global data

    if path in presets:
        preset = presets[path]

        data["active"].extend(preset)
        data["timestamp"] = time.time()
        return "Success"
    
    return "ERROR"

@app.route('/get')
def routeGet():
    global data
    return data


@app.route('/time')
def routeTime():
    global data
    return str(data["timestamp"])

@app.route('/ack')
def routeAck():
    global data

    data["active"] = []

    return "Success"

if __name__ == '__main__':
   app.run()