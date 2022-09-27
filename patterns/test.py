

# data = {
# 	"index": ["active"],
# 	"value":[
# 		{
# 			"type": "fill",
# 			"selection": [{"name":"vertical"}],
# 			"color": {"type":"rgb", "value":[10,  0, 0]}
# 		},
# 		{
# 			"type":"sequence",
# 			"id":"seq",
# 			"elements":[
# 				{
# 					"delay": 4,
# 					"type": "fill",
# 					"selection": [{"name":"vertical"}],
# 					"color": {"type":"rgb", "value":[0,  10, 0]}
# 				},
# 			]
# 		}
# 	]
# }


# data = {
# 	"index": ["active"],
# 	"value":[{"type": "animationStop"},{"type":"fill","color":{"type":"rgb","value":[0,0,0]},"selection":[{"name":"vertical"},{"name":"line"},{"name":"hexagon"},{"name":"x"},{"name":"bed"}]},{
# 			"type":"sequence",
# 			"id":"seq",
# 			"elements":[
# 				{
# 					"delay": 0,
# 					"type": "animationFill",
# 					"id": "fill1",
# 					"selection": [{"name":"hexagon"}, {"name":"x"}, {"name":"line"}],
# 					"colorAnimation": {
# 						"type": "rgb",
# 						"value": [
# 							[{"type":"transformation","points":[[0,1],  [2,130], [8, 130]]}],
# 							[{"type":"transformation","points":[[0,1], [2,80], [8, 80]]}],
# 							[{"type":"transformation","points":[[0,1],  [2,10], [8, 10]]}]
# 						]
# 					}
# 				},
# 				{
# 					"delay": 3,
# 					"type": "animationStop"
# 				}
# 			]
# 		}
# 	]
# }


data = {
	"index": ["active"],
	"value":[
		{
			"type": "animationFill",
			"id": "fill1",
			"selection": [{"name":"vertical"}, {"name":"line"},{"name":"hexagon"} , {"name":"x"}, {"name":"bed"}],
			"colorAnimation": {
				"type": "rgb",
				"value": [
					[{"type":"transformation","points":[[0,0], [0.5, 128], [0.8,0], [2.0, 0]]}],
					[{"type":"transformation","points":[[0,0], [2.0, 0]]}],
					[{"type":"transformation","points":[[0,0], [0.7,0], [1.0, 128], [1.5, 0], [2.0, 0]]}]
				]
			}
		}
	]
}




import requests
r = requests.post("https://light2.azurewebsites.net/set", json=data)
print(r.status_code, r.reason)
print(r.content)
