#!/usr/bin/python
# Creditcard Generator Coded By ./Exorcism1337

from random import Random
import copy


class Exorcism1337:

    randomInteger = Random()
    randomInteger.seed()
    red = "\033[1;31;40m"
    green = "\033[1;32;40m"
    visa = [
        ['4', '5', '3', '9'],
        ['4', '5', '5', '6'],
        ['4', '9', '1', '6'],
        ['4', '5', '3', '2'],
        ['4', '9', '2', '9'],
        ['4', '0', '2', '4', '0', '0', '7', '1'],
        ['4', '4', '8', '6'],
        ['4', '7', '1', '6'],
        ['4']]
    mastercard = [
        ['5', '1'], ['5', '2'], ['5', '3'], ['5', '4'], ['5', '5']]
    amex = [['3', '4'], ['3', '7']]
    discover = [['6', '0', '1', '1']]
    diners = [
        ['3', '0', '0'],
        ['3', '0', '1'],
        ['3', '0', '2'],
        ['3', '0', '3'],
        ['3', '6'],
        ['3', '8']]
    enRoute = [['2', '0', '1', '4'], ['2', '1', '4', '9']]
    jcb = [['3', '5']]
    voyager = [['8', '6', '9', '9']]

    def __init__(self):
        self.author()
        self.main()

    def author(self):

        print("""\n   _____ _____    _____                           _             
  / ____/ ____|  / ____|                         | |            
 | |   | |      | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | |   | |      | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |___| |____  | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
  \_____\_____|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                
                                                                """)
        print("""
            Author   : ./Exorcism1337
	    Contact  : c4tchMe1fY0uC4n@hackermail.com
	    Facebook : https://www.facebook.com/Yudas1337
	    Github   : https://github.com/Yudas1337
	    Version  :  1.0.1  \n""")

    def luhnAlgorithm(self, prefix, length):
        sum = 0
        pos = 0
        ccnumber = prefix
        while len(ccnumber) < (length - 1):
            digit = str(self.randomInteger.choice(range(0, 10)))
            ccnumber.append(digit)
        reversedCCnumber = []
        reversedCCnumber.extend(ccnumber)
        reversedCCnumber.reverse()
        while pos < length - 1:
            odd = int(reversedCCnumber[pos]) * 2
            if odd > 9:
                odd -= 9
            sum += odd
            if pos != (length - 2):
                sum += int(reversedCCnumber[pos + 1])
            pos += 2
        checkdigit = ((sum / 10 + 1) * 10 - sum) % 10
        ccnumber.append(str(checkdigit))
        return ''.join(ccnumber)

    def generateNumber(self, random, prefix, length, total):
        result = []
        while len(result) < total:
            ccnumber = copy.copy(random.choice(prefix))
            result.append(self.luhnAlgorithm(ccnumber, length))
        return result

    def toolsMenu(self):
        print("******************************")
        print("1. Mastercard")
        print("2. VISA 16 digit")
        print("3. VISA 13 digit")
        print("4. American Express")
        print("******************************")

    def result(self, numbers):
        result = []
        result.append('\n'.join(numbers))
        result.append('')
        return '\n'.join(result)

    def main(self):
        self.toolsMenu()
        mode = int(input("Your Choice : "))
        try:
            while mode >= 1 and mode <= 4:
                length = int(input("Total Result: "))
                if mode == 1:
                    mastercard = self.generateNumber(
                        self.randomInteger, self.mastercard, 16, length)
                    print(f'{self.green}******************')
                    print('Mastercard')
                    print('******************')
                    print(f'{self.green}{self.result(mastercard)}')
                    break
                elif mode == 2:
                    visa = self.generateNumber(
                        self.randomInteger, self.visa, 16, length)
                    print(f'{self.green}******************')
                    print('Visa 16 Digit')
                    print('******************')
                    print(f'{self.green}{self.result(visa)}')
                    break
                elif mode == 3:
                    visa = self.generateNumber(
                        self.randomInteger, self.visa, 13, length)
                    print(f'{self.green}******************')
                    print('Visa 13 Digit')
                    print('******************')
                    print(f'{self.green}{self.result(visa)}')
                    break
                elif mode == 4:
                    amex = self.generateNumber(
                        self.randomInteger, self.amex, 15, length)
                    print(f'{self.green}******************')
                    print('American Express')
                    print('******************')
                    print(f'{self.green}{self.result(amex)}')
                    break
                else:
                    print(f'{self.red}Wrong Options')
        except KeyboardInterrupt:
            print(f'{self.red}Program Terminated By User')


if __name__ == "__main__":
    Exorcism1337()
