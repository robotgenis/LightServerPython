



# JSON Format

## MAIN LEVEL

- timestamp: Float - latest update time
- active: element[] - current active actions
- presets: element[] - presets for easier use

## TYPES

### element - anything that can be put in active

### abstract action: element
- type: string - specific type of the action
- selection: selection[]

### abstract thread: element
- id: string
Inherited
- type: string - specific type of the action

### abstract animation: thread, element
Inherited
- id: string
- type: string - specific type of the action
- selection: selection[]

### sequence: thread
- elements: element[] with attribute "delay": float (waiting time)
Override
- type: "sequence
Inherited
- id: string

### fill: action
- color: color
Inherited
- type: "fill"
- selection: selection[]

### animationStop: element
- id (optional): string - id of animation to stop, if not present all will stop

### animationFill: animation
- colorAnimation: colorAnimation
Override
- type: "animation_fill"
Inherited
- id: string
- selection: selection[]

### colorAnimation
Notes: Last point in each transformation must be the same as the first point in the next one.
- type: "rgb" @future "hsv"
- value: [transformation[], transformation[], transformation[]] - [r, g, b] 

### selection
- name: string
- startIndex (optional): integer
- endIndex (optional): integer

### color
- type: "rgb" @Future "hsv"
- value: integer[3] - range[0-255]

### transformation
- type: "transformation"
- points: point[]

### bezier: transformation
Override
- type: "bezier"
- points: point[4]
- divisions: integer - default 10

### point: array[2]
- [x, y]