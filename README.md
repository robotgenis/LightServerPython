



# JSON Format

## MAIN LEVEL

- timestamp: Float - latest update time
- active: element[] - current active actions
- presets: element[] - presets for easier use

## TYPES

### element - anything that can be put in active

### action: element
- type: string - specific type of the action
- selection: selection[]

### fill: action
- color: color
Inherited
- type: "fill"
- selection: selection[]

### animationFill: action
- colorAnimation: colorAnimation
Inherited
- type: "animation_fill"
- selection: selection[]

### colorAnimationRGB
- r: Transformation[]
- g: Transformation[]
- b: Transformation[]

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


### point
- x: number
- y: number