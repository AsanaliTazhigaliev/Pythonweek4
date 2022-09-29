matrix = []
sum_pos = 0
for i in range(len(matrix) - 1):
    for j in range(i + 1, len(matrix[i])):
        if matrix[i][j] > 0:
            sum_pos += matrix[i][j]
print('Sum of positive elements —', sum_pos)
