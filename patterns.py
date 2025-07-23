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
pattern 11
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
pattern11(5)
