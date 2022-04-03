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
        light = ['.', ':', '-', '+', '=', '!', ' ']
        result = ''
        r = self.r
        origin_x = self.origin_x
        origin_y = self.origin_y
        origin_z = math.sqrt(
            math.pow(r, 2) - math.pow(origin_x, 2) - math.pow(origin_y, 2))

        for y in range(-r, r+1):
            for x in range(-r, r+1):
                try:
                    z = math.sqrt(math.pow(r, 2) -
                                  math.pow(x, 2) - math.pow(y, 2))
                    b = (x * origin_x + y * origin_y +
                         z * origin_z)/(math.pow(r, 2))
                except:
                    b = 2

                if b <= 0:
                    result += light[5]
                elif b > 0 and b <= 0.3:
                    result += light[4]
                elif b > 0.3 and b <= 0.5:
                    result += light[3]
                elif b > 0.5 and b <= 0.7:
                    result += light[2]
                elif b > 0.7 and b <= 0.9:
                    result += light[1]
                elif b > 0.9 and b <= 1:
                    result += light[0]
                elif b == 2:
                    result += light[6]
            result += '\n'
        return result

    def save(self, text_file):
        '''
        Skriver ut klotet till en textfil
        :param file: Filen där klotet sparas
        :write: Skriver klotet till filen
        '''
        write_file = open(text_file, 'w')
        write_file.write(self.calc())
        write_file.close()

    def calc_shadow(self):      # Inte klart än
        '''
        Räknar ut skuggorna
        :return: Sträng med klotet tillsammans med den uträknade skuggan
        '''


def prompt(r, origin_x, origin_y):        # För GUI
    '''
    Tar in input för att skapa ett nytt klot
    :Sphere: klot: Skapa nytt klotobjekt
    '''
    try:
        klot = Sphere(r, origin_x, origin_y)
        klot.calc()
    except ValueError:
        print("Your input is mathematically incorrect. Please enter new values...")
        return prompt()

    text_file = input('Enter the text file you want to save the sphere to: ')
    if '.txt' in text_file[len(text_file)-4:]:
        klot.save(text_file)
    else:
        klot.save(text_file+'.txt')
