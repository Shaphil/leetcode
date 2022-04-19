def flip(A):
    flipped = []
    for mat in A:
        length = len(mat)
        rev = [0] * length
        length -= 1
        for elem in mat:
            rev[length] = 0 if elem == 1 else 1
            length -= 1
        
        flipped.append(rev)

    return flipped


if __name__ == '__main__':
    l = [[1,1,0],[1,0,1],[0,0,0]]
    flipped = flip(l)
    print(flipped)

