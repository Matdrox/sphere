import math

class Sphere:
  b = 0
  z = 0
  def __init__(self, r, origin_x, origin_y):
    self.r = r
    self.origin_x = origin_x
    self.origin_y = origin_y
  
  def calc(self):
    result = ''
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
          # print('M', end='')
          result += 'M'
        elif b > 0 and b <= 0.3:
          # print('*', end='')
          result += '*'
        elif b > 0.3 and b <= 0.5:
          # print('+', end='')
          result += '+'
        elif b > 0.5 and b <= 0.7:
          # print('-', end='')
          result += '-'
        elif b > 0.7 and b <= 0.9:
          # print('.', end='')
          result += '.'
        elif b > 0.9 and b <= 1:
          # print(' ', end='')
          result += ' '
      result += '\n'
      origin_z = math.sqrt(math.pow(r, 2) - math.pow(origin_x, 2) - math.pow(origin_y, 2))
    return result

  def show(self):
    art = self.calc()
    print(art)

  def save(self, text_file):
    write_file = open(text_file, 'w')
    write_file.write(self.calc())
    write_file.close()

r = int(input('Enter the sphere\'s radius: '))
origin_x = int(input('Enter the sphere\'s x origin: '))
origin_y = int(input('Enter the sphere\'s y origin: '))

klot = Sphere(r, origin_x, origin_y)
klot.calc()
klot.show()

text_file = input('Enter the text file you want to save the sphere to: ')
if '.txt' in text_file[len(text_file)-4:]:
  klot.save(text_file)
else:
  klot.save(text_file+'.txt')