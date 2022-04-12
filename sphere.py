'''
Författare: Matei Cananau
Datum: 2022-04-09
Revisionsdatum: 2022-04-13
'''

import math


class Sphere:
    '''
    Attributer:
    b: Heltalsvariabel för ljusstyrkan (0)
    z: Heltalsvariabel för z-koordinaten (0)
    '''
    b = 0
    z = 0

    def __init__(self, r, origin_x, origin_y):
        '''
        Initierar ett klot
        :param r: Den önskade radien
        :param origin_x: Den önskade startpositionen för koordinaten x
        :param origin_y: Den önskade startpositionen för koordinaten y
        '''
        self.r = r
        self.origin_x = origin_x
        self.origin_y = origin_y

    def calc(self):
        '''
        Räknar ut ljusstyrkan med hjälp av skalärprodukt
        :return: Sträng fylld med karaktärer som passar värdena på ljusstyrkan inom
        koordinaterna [-r, r]
        '''
        light = ['.', ':', '-', '+', '=', '!', ' ',
                 '¨']            # Array för karaktärer (fonten kan inte visa * så jag behövde ändra karaktärerna för fin output).
        result = ''
        n = 50
        m = 50
        r = self.r
        origin_x = self.origin_x
        origin_y = self.origin_y
        origin_z = math.sqrt(
            math.pow(r, 2) - math.pow(origin_x, 2) - math.pow(origin_y, 2))

        for y in range(-m, m+1):                # Synintervall m
            for x in range(-n, n+1):            # Synintervall n
                try:
                    z = math.sqrt(math.pow(r, 2) -
                                  math.pow(x, 2) - math.pow(y, 2))
                    b = (x * origin_x + y * origin_y +
                         z * origin_z)/(math.pow(r, 2))
                except:
                    b = 2

                if b <= 0:
                    result += light[5]
                elif 0 < b <= 0.3:
                    result += light[4]
                elif 0.3 < b <= 0.5:
                    result += light[3]
                elif 0.5 < b <= 0.7:
                    result += light[2]
                elif 0.7 < b <= 0.9:
                    result += light[1]
                elif 0.9 < b <= 1:
                    result += light[0]
                # Om formeln inte är giltig - skapa en cirkel med en offset (skugga)
                elif b == 2:
                    shadow_x = x + 0.5*origin_x
                    shadow_y = y + 0.5*origin_y
                    try:
                        origin_z = math.sqrt(
                            math.pow(r, 2) - math.pow(shadow_x, 2) - math.pow(shadow_y, 2))
                        z = math.sqrt(math.pow(r, 2) -
                                      math.pow(shadow_x, 2) - math.pow(shadow_y, 2))
                        b = (shadow_x * origin_x + shadow_y * origin_y +
                             z * origin_z)/(math.pow(r, 2))

                        result += light[7]
                        origin_z = math.sqrt(
                            math.pow(r, 2) - math.pow(origin_x, 2) - math.pow(origin_y, 2))
                    except:
                        # Om formeln fortfarande inte funkar, blir punkten inte belyst
                        result += light[6]
            result += '\n'
        return result

    def show(self):
        '''
        Skriver ut klotet i terminalen
        :print: Strängen
        '''
        art = self.calc()
        print(art)

    def save(self, text_file):
        '''
        Skriver ut klotet till en textfil
        :param file: Filen där klotet sparas
        :write: Skriver klotet till filen
        '''
        write_file = open(text_file, 'w')
        write_file.write(self.calc())
        write_file.close()


def prompt(r, origin_x, origin_y):        # För GUI
    '''
    Tar in input för att skapa ett nytt klot
    :Sphere: klot: Skapa nytt klotobjekt
    '''
    try:
        klot = Sphere(r, origin_x, origin_y)
        klot.calc()
        # klot.show()               # Activate if no GUI
    except ValueError:
        print("Your input is mathematically incorrect. Please enter new values...")
        return prompt()

    text_file = input('Enter the text file you want to save the sphere to: ')
    if '.txt' in text_file[len(text_file)-4:]:
        klot.save(text_file)
    else:
        klot.save(text_file+'.txt')


def terminal():
    r = int(input('Enter the sphere\'s radius: '))
    origin_x = int(input('Enter the sphere\'s x origin: '))
    origin_y = int(input('Enter the sphere\'s y origin: '))
    prompt(r, origin_x, origin_y)


# terminal()                        # Activate if no GUI
