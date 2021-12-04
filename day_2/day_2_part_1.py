with open('./input.txt') as f:
  directions = list(map(lambda line: line.split(), f))
  depth = 0
  aim = 0
  horizontal_position = 0
  for pair in directions:
    mag = int(pair[1])
    direction = pair[0]
    if direction == 'forward':
      horizontal_position += mag
      depth += aim * mag
    elif direction == 'down':
      aim += mag
    else:
      aim -= mag
  print('depth: ' + str(depth))
  print('horiz: ' + str(horizontal_position))
  print('depth * horiz: ' + str(depth * horizontal_position))
