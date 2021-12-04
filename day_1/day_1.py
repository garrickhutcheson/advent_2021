with open('./input.txt') as f:
  numbers = list(map(lambda line: int(line), f))
  last_number = 0
  deeper_readings = -1
  window = numbers[:3]
  iter = 2
  for number in numbers[2:]:
    window[iter] = number
    iter = (iter + 1) % 3
    sum_ = sum(window)
    print(str(window) + ' ' + str(sum_))
    if last_number < sum_:
      deeper_readings += 1
      print(str(last_number) + ' < ' + str(sum_) + ' ' + str(deeper_readings))
    last_number = sum_
  print(str(deeper_readings))
  print(len(numbers[3:]))
