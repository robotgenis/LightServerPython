



# JSON Format

## MAIN LEVEL

- timestamp: float - latest update time
- active: current active actions

## CATEGORIES
### action
- selection: selection[]

## TYPES

### color
- type: "rgb" @Future "hsv
- value: integer[3] - range[0-255]

### fill: action
- color: color

### selection: string