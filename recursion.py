import numpy as np

'''
Sum of first n numbers
1) parameterised or
2) functional way
'''
def parameterisedSum(i, sum):
    if (i < 1):
        return sum
    return parameterisedSum(i - 1, sum + i)


def functionalSum(n):
    if (n == 1):
        return 1
    return n + functionalSum(n - 1)

'''
parameterised factoriel
'''
def parameterisedFactoriel(i , fact):
    if (i == 1):
        return fact
    return parameterisedFactoriel(i - 1, fact * i)

'''
reversing an array
1) with for loop
2) recursive
'''
def reverseArray1(myArr):
    for i in range(len(myArr)):
        fromLast = len(myArr) - i - 1
        if (fromLast > i):
            temp = myArr[fromLast]
            myArr[fromLast] = myArr[i]
            myArr[i] = temp
    print(myArr)

def reverseArray2(arr, firstIndex, lastIndex):
    if (firstIndex >= lastIndex):
        print(arr)
        return
    temp = arr[lastIndex]
    arr[lastIndex] = arr[firstIndex]
    arr[firstIndex] = temp
    reverseArray2(arr, firstIndex + 1, lastIndex - 1)

# print(parameterisedFactoriel(4, 1))

reverseArray2(np.array([1, 3, 5, 7, 9, 6]), 0, 5)