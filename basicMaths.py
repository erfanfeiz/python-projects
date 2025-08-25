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

'''
Palindrome is like 121 or 1001 or 11 or 7
'''
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
    # other way is to save n in another variable then reverse it, at the end compare two
'''
sum of any number digit for which each digit power to number of digits is equal to n itself like 371
'''
def isArmstrong(n):
    sum = 0
    duplicate = n
    while(n > 0):
        sum += (n % 10) ** int(math.log10(duplicate) + 1)
        n = int(n / 10)
    if (duplicate == sum):
        print(True)
    else:
        print(False)

def getAllDivisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            divisors.append(int(i)) 
            if((n/i) != i):
                divisors.append(int(n/i))
    print(divisors)

def isPrime(n):
    count = 0
    for i in range(1,int(math.sqrt(n)) + 1):
        if (n % i == 0):
            count += 1
            if ((n / i) != i):
                count += 1
    if (count == 2):
        print(True)
        return
    print(False)
'''
GCD (Greatest Common Divisor of two numbers) 
or
HCF (Highest Common Factor of two numbers)
'''
def getGCH(n1, n2):
    for i in (min(n1, n2), 1, -1):
        if (n1 % i == 0 and n2 % i == 0):
           print(i)
           return 
        
'''
Equilateral algorithm:
gcd(a, b) a > b => gcd(a-b, b)
for instance with given two numbers of 52 and 10
the gcd(10, 52) is :
gcd(52, 10) = gcd(42, 10) = gcd(32, 10) = gcd(22, 10) = gcd(12, 10) = gcd(2, 10) = gcd(8, 2) = gcd(6, 2) = gcd(4, 2)
= gcd(2, 2) = gcd(0, 2) that is 2 but as we can see instead of subtracting each time we could divide a on b and the
remaining would be 2 in the first place so gcd(52, 10) could be gcd(52%10, 10) which is gcd(2, 10) and since now a is less
than b the variables changes to gcd(10, 2) now we can do the same gcd(10%2, 2) now we reach to 0 so the answer is 2
O(log(min(a, b)))
'''
def getGCDwithEquilateral(a, b):
    while(a > 0 and b > 0):
        if (b > a):
            b = int(b % a)
        elif (a > b):
            a = int(a % b)
    if (a == 0): print(b)
    print(a)

getGCDwithEquilateral(15, 10)