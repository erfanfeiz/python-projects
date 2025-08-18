import math
def extractDigits(n):
    while(n > 0):
        lastDigit = n % 10
        print(f"last digit {lastDigit}")
        n = int(n / 10)

def getDigitsCount(n):
    count = int(math.log10(n)) + 1
    return count

def reverseNumber(n):
    reversed = 0
    count = getDigitsCount(n)
    i = 0
    while(i < count):
        lastDigit = n % 10
        reversed = reversed * 10 + lastDigit    
        n = int (n / 10)
        i += 1
    print(reversed)

reverseNumber(7789)