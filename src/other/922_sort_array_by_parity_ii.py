def sortArrayByParityII(A):
    even = []
    odd = []
    for i in A:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    sorted_arr = []
    for i in range(len(even)):
        sorted_arr.append(even[i])
        sorted_arr.append(odd[i])

    return sorted_arr


if __name__ == "__main__":
    a = [4, 2, 5, 7]
    x = sortArrayByParityII(a)
    print(x)
