import math
''' 
pattern 1 
****
****
****
'''
def pattern1(n):
    for i in range(0, n, 1):
        for j in range (0, n, 1):
            print('*', end='')
        print("")

'''
pattern 2
*
**
***
****
*****
'''
def pattern2(n):
    for i in range(0, n, 1):
        for j in range(0, i + 1, 1):
            print('*', end='')
        print("")
'''
pattern 3
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
def pattern3(n):
    for i in range(1, n + 1, 1):
        for j in range(1, i  + 1, 1):
            print(f"{j} ", end='')
        print("\n")    

'''
pattern 4 
1
22
333
4444
55555
'''
def pattern4(n):
    for i in range(1, n + 1, 1):
        for j in range(1, i + 1, 1):
            print (f"{i} ", end = "")
        print("\n")

'''
pattern 5
*****
****
***
**
*
'''
def pattern5(n):
    for i in range (0, n + 1, 1):
        for j in range (1, n + 1 - i, 1):
            print("*", end='')
        print("")
'''
pattern 6
12345
1234
123
12
1
'''
def pattern6(n):
    for i in range (0, n + 1, 1):
        for j in range (1, n + 1 - i, 1):
            print(f"{j} ", end='')
        print("\n")

'''
pattern 7
    *
   ***
  *****
 *******
*********
'''
def pattern7(n):
    for i in range (0, n , 1):
        for x in range(n - 1 - i, 0, -1):
                print(" ", end='')
        for j in range(0, 2 * i + 1 , 1):
            print("*", end='')
        for x in range(n - 1 - i, 0, -1):
            print(" ", end='')
        print("\n")

'''
pattern 8
*********
 *******
  *****
   ***
    *
'''
def pattern8(n):
    for i in range (n, 0 , -1):
        for x in range(i , n , 1):
                print(" ", end='')
        for j in range(0, 2 * i - 1 , 1):
            print("*", end='')
    
        print("\n")

'''
pattern 9
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
'''
def pattern9(n):
    pattern7(n)
    pattern8(n)

'''
pattern 10
*
**
***
****
*****
****
***
**
*
'''
def pattern10(n):
    #one way
    #pattern2(n)
    #pattern5(n-1)
    # the other way
    for i in range(1, 2 * n - 1 + 1, 1):
        stars = i
        if i > n :
            stars = 2 * n - i
        for j in range (0, stars, 1):
            print("*", end='')
        print("\n")
'''
pattern 11 ** this was challenging**
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
'''
def pattern11(n):
    start = 1
    for i in range(0, n , 1):
        if (i % 2 == 0):
            start = 1
        else:
            start = 0
        for j in range(0, i + 1 , 1):
            print( f"{start} ", end = '')
            start = 1 - start 
        print("\n")

'''
pattern 12

1      1
12    21
123  321
12344321

'''
def pattern12(n):
    for i in range(1, n + 1, 1):
        spaces = n * 2 - i * 2
        for j in range(1, i + 1, 1):
            print(j, end='')
        for x in range(spaces):
            print(" ", end = '')
        for j in range(i, 0, -1):
            print(j, end='')
        
        print("\n")        
'''
pattern 13

1
2 3
4 5 6
7 8 9 10 
11 12 13 14 15
'''
def pattern13(n):
    number = 1
    for i in range(1, n + 1, 1):
        for j in range(0, i , 1):
            print(f"{number} ", end='')
            number+=1
        print("\n")
'''
pattern 14
A
AB
ABC
ABCD
ABCDE
'''
def pattern14(n):
    for i in range(0, n, 1):
        for j in range(0, i  + 1 , -1):
            print(chr(65 + j), end='')
        print("\n")
'''
pattern 15
ABCDE
ABCD
ABC
AB
A
'''
def pattern15(n):
    for i in range(n+1):
        for j in range (0, n - i, 1):
            print(chr(65 + j), end='')
        print("\n")    

'''
pattern 16
A
BB
CCC
DDDD
EEEEE
'''
def pattern16(n):
    for i in range(n):
        for j in range(0, i + 1, 1):
            print(chr(65 + i), end='')
        print("\n")

'''
pattern 17
   A   
  ABA  
 ABCBA
ABCDCBA
'''
def pattern17(n):
    for i in range(1, n + 1, 1):
        space = 2 * (n - i)
        lastChar = 64
        breakpoint = math.floor((2 * i + 1) / 2)
        for x in range (math.floor(space /  2)):
            print(" ", end='')
        for j in range(2 * i - 1):
            if (j < breakpoint):
                lastChar += 1
                print(chr(lastChar), end='')
            else : 
                lastChar -= 1
                print(chr(lastChar), end='')
        for y in range(math.floor(space /  2)):
            print(" ", end='')
        print(" ")
'''
 pattern 18
 E
 D E
 C D E
 B C D E
 A B C D E
 '''
def pattern18(n):
    ch = 69
    for i in range(n):
        for j in range(ch - i, i+1, 1):
            print(chr(ch), end='')
        print("\n")

pattern18(5)
