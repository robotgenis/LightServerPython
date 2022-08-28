



# JSON Format

## MAIN LEVEL

- timestamp: float - latest update time
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

### selection
- name: string
- startIndex (optional): int
- endIndex (optional): int

### color
- type: "rgb" @Future "hsv"
- value: integer[3] - range[0-255]
