def identity_matrix(n):
    return [[1 if i==j else 0 for i in range(n)] for j in range(n)]


a = identity_matrix(3)



for row in a:
    print(*row)