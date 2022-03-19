import math

class Klot:
  def __init__(self, r, origin_x, origin_y):
    b = 0
    z = 0
    self.r = r
    self.origin_x = origin_x
    self.origin_y = origin_y
  
  def show(self):
    r = self.r
    origin_x = self.origin_x
    origin_y = self.origin_y
    for y in range (-r, r+1):
      for x in range (-r, r+1):
        try:
          z = math.sqrt(math.pow(r, 2) - math.pow(x, 2) - math.pow(y, 2))
          b = (x * origin_x + y * origin_y + z * origin_z)/(math.pow(r, 2))
        except:
          b = 0

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
      print('')
      origin_z = math.sqrt(math.pow(r, 2) - math.pow(origin_x, 2) - math.pow(origin_y, 2))

r = int(input('Enter the sphere\'s radius: '))
origin_x = int(input('Enter the sphere\'s x origin: '))
origin_y = int(input('Enter the sphere\'s y origin: '))

klot = Klot(r, origin_x, origin_y)
klot.show()