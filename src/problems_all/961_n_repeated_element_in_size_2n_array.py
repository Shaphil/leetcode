def solve(A):
    unique = {}
    n = len(A) // 2
    for i in A:
        if i not in unique:
            unique[i] = 1 
        else:
            unique[i] += 1

    for u in unique:
        if unique[u] == n:
            return u


if __name__ == '__main__':
    l = [5,1,5,2,5,3,5,4]
    val = solve(l)
    print(val)

