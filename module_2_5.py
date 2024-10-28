def get_matrix(n,m,value):
    matrix=[]

    for i in range(n):
        row = []

        for j in range(m):
            row.append(value)

        matrix.append(row)


    return matrix
result1 = get_matrix(5,2,10)
print(result1)
