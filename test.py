def findMinAndMax(L):
    if L != []:
        min = max = L[0]
        for number in L:
            if min > number:
                min = number
            if max < number:
                max = number
        return (min, max)
    else:
        return (None, None)

if findMinAndMax([]) != (None, None):
    print('测试失败')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败')
elif findMinAndMax([7, 1, 9, 4, 5]) != (1, 9):
    print('测试失败')
else:
    print('测试成功')


