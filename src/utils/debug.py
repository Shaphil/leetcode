def solution(a):

    indexOfMinimum = -1
    minimalSum = float('inf')

    for i in range(len(a)):
        curSum = 0
        for j in range(len(a)):
            curSum += abs(a[j] - a[i])
        if curSum < minimalSum:
            minimalSum = curSum
            indexOfMinimum = i

    return a[indexOfMinimum]



def main():
    a = [2, 4, 7]
    print(solution(a))


if __name__ == '__main__':
    main()
