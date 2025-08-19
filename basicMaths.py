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
    i = 0
    while(n > 0):
        lastDigit = n % 10
        if (lastDigit != 0):
            reversed = reversed * 10 + lastDigit    
        n = int (n / 10)
        i += 1
    print(reversed)

def isPalindrome(n):
    count = int(math.log10(n) + 1)
    while(count > 0):
        lastDigit = n % 10
        firstDigit = int(n / 10 ** (count - 1))
        n = int(n % 10 ** (count - 1))
        n = int(n / 10)
        if (lastDigit != firstDigit):
            print(False)
            return
        count -= 2
    print(True)
isPalindrome(10051)