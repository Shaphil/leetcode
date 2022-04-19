"""
985. Sum of Even Numbers After Queries
"""


def sumEvenAfterQueries(A, queries):
    output = []
    even_sum = 0
    for i in A:
        if i % 2 == 0:
            even_sum += i

    for query in queries:
        val, index = query[0], query[1]

        if A[index] % 2 == 0 and val % 2 == 0:
            A[index] += val
            even_sum += val
        elif A[index] % 2 == 0 and val % 2 != 0:
            even_sum -= A[index]
            A[index] += val
        elif A[index] != 0 and val % 2 == 0:
            A[index] += val
        elif A[index] % 2 != 0 and val % 2 != 0:
            A[index] += val
            even_sum += A[index]

        output.append(even_sum)

    return output


if __name__ == "__main__":
    A = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    output = sumEvenAfterQueries(A, queries)
    print(output)
