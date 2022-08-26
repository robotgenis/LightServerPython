



# JSON Format

## MAIN LEVEL

- timestamp: float - latest update time
- active: element[] - current active actions

## TYPES

### element - anything that can be put in active

### action: element
- type: string - specific type of the action
- selection: selection[]

### fill: action
- color: color

### selection: string

### color
- type: "rgb" @Future "hsv"
- value: integer[3] - range[0-255]