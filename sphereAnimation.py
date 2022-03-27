import math
import time

# r = int(input('Enter the sphere\'s radius: '))
# origin_x = int(input('Enter the sphere\'s x origin: '))
# origin_y = int(input('Enter the sphere\'s y origin: '))

r = 15
origin_x = 0
origin_y = 0

b = 0
z = 0
turner = 1

while True:
  origin_z = math.sqrt(math.pow(r, 2) - math.pow(origin_x, 2) - math.pow(origin_y, 2))

  for y in range (-r, r+1):
    for x in range (-r, r+1):
      try:
        z = math.sqrt(math.pow(r, 2) - math.pow(x, 2) - math.pow(y, 2))
        b = (x * origin_x + y * origin_y + z * origin_z)/(math.pow(r, 2))
      except:
        b = 2
      # if b <= 0:
      #   print(' ', end='')
      # elif b > 0 and b <= 0.3:
      #   print('*', end='')
      # elif b > 0.3 and b <= 0.5:
      #   print('=', end='')
      # elif b > 0.5 and b <= 0.7:
      #   print('#', end='')
      # elif b > 0.7 and b <= 0.9:
      #   print('€', end='')
      # elif b > 0.9 and b <= 1:
      #   print('@', end='')
      
      if b <= 0:
        print('M', end='')
      elif b > 0 and b <= 0.3:
        print('*', end='')
      elif b > 0.3 and b <= 0.5:
        print('+', end='')
      elif b > 0.5 and b <= 0.7:
        print('-', end='')
      elif b > 0.7 and b <= 0.9:
        print('.', end='')
      elif b > 0.9 and b <= 1:
        print(' ', end='')
      elif b == 2:
        print(' ', end='')
    print('')
  origin_x += turner

  if (origin_x == r):
    turner = -1
  if (origin_x == -r):
    turner = 1

  time.sleep(0.1)
