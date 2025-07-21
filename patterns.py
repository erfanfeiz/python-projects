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
pattern2(5)