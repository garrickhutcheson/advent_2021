from functools import reduce

def part_1(f):
  bit_values = map(lambda line:\
    map(lambda bit: 1 if bit == '1' else -1, line[:len(line)-1]), f)
  totals = reduce(lambda bits1, bits2:\
    [a + b for a,b in zip(bits1, bits2)], bit_values)
  print(totals)
  most_freq = map(lambda num: '0' if num < 0 else '1', totals)
  least_freq = map(lambda num: '0' if num > 0 else '1', totals)
  gamma_string = reduce(lambda a, b: a + b, most_freq)
  epsilon_string = reduce(lambda a, b: a + b, least_freq)
  gamma = int(gamma_string, 2)
  epsilon = int(gamma_string, 2) 
  print(gamma)
  print(gamma * epsilon)

def part_2(f):
  # convert 0's and 1's to -1's and 1's in integer form
  bit_values = list(map(lambda line:\
    list(map(lambda bit: 1 if bit == '1' else -1, line[:len(line)-1])), f)) 
  for i in range(len(bit_values[0])):
    # total up all remaining rows of -1 and 1
    totals = reduce(lambda bits1, bits2:\
      [a + b for a,b in zip(bits1, bits2)], bit_values)

    # print the totals just so that we can be sure we're on track
    print(totals)

    # if < 0, 0 was more common, else 1, favor tie to 1
    most_freq = list(map(lambda num: -1 if num < 0 else 1, totals))

    # filter out based on most common value of current column
    filter_values = [x for x in bit_values if x[i] == most_freq[i]]
    
    # more printing just to make sure things are going right
    for value in filter_values:
      print(value)
    print(len(filter_values))
    if (len(filter_values) > 1 and i < len(bit_values[0])-1): # more filtering to do
      bit_values = filter_values
    else: # either down to last number or would have filtered out everything. grab the last number
      number = map(lambda bit: '0' if bit == -1 else '1', filter_values[-1])
      o2 = int(reduce(lambda a,b: a+b, number),2)
      break

  f.seek(0)
  bit_values = list(map(lambda line:\
    list(map(lambda bit: 1 if bit == '1' else -1, line[:len(line)-1])), f)) 
  for i in range(len(bit_values[0])):
    # total up all remaining rows of -1 and 1
    totals = reduce(lambda bits1, bits2:\
      [a + b for a,b in zip(bits1, bits2)], bit_values)

    # print the totals just so that we can be sure we're on track
    print(totals)

    # if < 0, 1 was less common, else 0 was less common, favor tie to 1
    least_freq = list(map(lambda num: 1 if num < 0 else -1, totals))

    # filter out based on least common value of current column
    filter_values = [x for x in bit_values if x[i] == least_freq[i]]
    
    # more printing just to make sure things are going right
    for value in filter_values:
      print(value)
    print(len(filter_values))
    if (len(filter_values) > 1 and i < len(bit_values[0])-1): # more filtering to do
      bit_values = filter_values
    else: # either down to last number or would have filtered out everything. grab the last number
      number = map(lambda bit: '0' if bit == -1 else '1', filter_values[-1])
      co2 = int(reduce(lambda a,b: a+b, number),2)
      break
  print(co2)
  print(o2)
  print(co2 * o2)

with open('./input.txt') as f:
  part_1(f)
  f.seek(0)
  part_2(f)
