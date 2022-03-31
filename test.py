import math

#Hämtar input på alla kända variabler
r = int(input("Enter radius:"))
x0 = int(input("Enter x0:"))
y0 = int(input("Enter y0:"))

#Beräknar ljusets infallningspunkt
z0 = math.sqrt(r ** 2 - x0 ** 2 - y0 ** 2)
""""
def calculate_source():
 z0 = math.sqrt(r ** 2 - x0 ** 2 - y0 ** 2)
   if r ** 2 - x0 ** 2 - y0 ** 2 < 0:
    raise ValueError("Negative Squareroot")
"""""


def calculate_illumination():
  a = ""
  for x in range(-r, r + 1):
    for y in range(-r, r + 1):
      try:
        z = math.sqrt(r ** 2 - x ** 2 - y ** 2)
        b = ((x * x0 + y * y0 + z * z0) / (r ** 2))

      except ValueError:
        if (r ** 2 - x ** 2 - y ** 2) < 0:
            b = 0
              # a += "\n"
      if b <= 0:
        # a += "M"
        print('M',end="")

      elif 0 < b <= 0.3:
        # a += "*"
        print('*',end="")

      elif 0.3 < b <= 0.5:
        # a += "+"
        print('+',end="")

      elif 0.5 < b <= 0.7:
        # a += "-"
        print('-',end="")

      elif 0.7 < b <= 0.9:
        # a += "."
        print('.',end="")

      elif 0.9 < b <= 1:
        # a += " "
        print(' ',end="")
      # print(a, end="")
      #Writes string to another file
      # file1 = open("write.py", "w")
      # file1.write(a)
      # file1.close()
    print('')
#Gör senare


calculate_illumination()
