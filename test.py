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

    def calc(self, m, n):
        '''
        Räknar ut ljusstyrkan med hjälp av skalärprodukt
        :return: Sträng fylld med karaktärer som passar värdena på ljusstyrkan inom
        koordinaterna [-r, r]
        '''
        light = [' ', '.', '-', '+', '*', 'M', ' ']
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
                    # result += light[6]
                    shadow_x = x + 2*origin_x
                    shadow_y = y + 2*origin_y
                    try:
                        origin_z = math.sqrt(
                            math.pow(r, 2) - math.pow(shadow_x, 2) - math.pow(shadow_y, 2))
                        z = math.sqrt(math.pow(r, 2) -
                                      math.pow(shadow_x, 2) - math.pow(shadow_y, 2))
                        b = (shadow_x * origin_x + shadow_y * origin_y +
                             z * origin_z)/(math.pow(r, 2))

                        result += 'Y'
                    except:
                        result += light[6]

                # P är punkt i bakgrunden: b == 2
                # O är ursprungspunkten: (origin_x, origin_y)
                # i är en skalär
                # Linjen ges av P + iO
            result += '\n'
        return result

    def show(self):
        '''
        Skriver ut klotet i terminalen
        :print: Strängen
        '''
        art = self.calc(10, 10)
        print(art)

    def save(self):
        '''
        Skriver ut klotet till en textfil
        :param file: Filen där klotet sparas
        :write: Skriver klotet till filen
        '''
        text_file = input(
            'Enter the text file you want to save the sphere to: ')
        if '.txt' in text_file[len(text_file)-4:]:
            write_file = open(text_file, 'w')
        else:
            write_file = open(text_file+'.txt', 'w')

        write_file.write(self.calc())
        write_file.close()


def prompt():
    '''
    Tar in input för att skapa ett nytt klot
    :Sphere: klot: Skapa nytt klotobjekt
    '''
    try:
        r = int(input('Enter the sphere\'s radius: '))
        origin_x = int(input('Enter the sphere\'s x origin: '))
        origin_y = int(input('Enter the sphere\'s y origin: '))
        klot = Sphere(r, origin_x, origin_y)
        klot.show()
    except ValueError:
        print("Your input    is logically incorrect. Please enter new values...")
        return prompt()

    wrongs = 0
    while True:
        answer = input(
            'Would you like to save the sphere to a file? Answer with Y/N: ')
        if answer.upper() == 'Y':
            klot.save()
            print('Successfully Saved!')
            return False
        elif answer.upper() == 'N':
            print('Have a nice day!')
            return False
        else:
            if wrongs < 2:
                print('Please answer with Y/N...\n')
                wrongs += 1
            else:
                print('Can\'t follow instructions, can you...?')
                return False


prompt()
