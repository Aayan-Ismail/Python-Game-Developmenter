matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix)
print(len(matrix))
print(len(matrix[0]))
print(matrix[1][2])
print(matrix[2][1])
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j],end=' ')
    print('\n')

rows = int(input("enter the number of rows: "))
columns = int(input("enter the number of columns: "))
matrix_user = [
    
]
for i in range(rows):
    tem = []
    for j in range(columns):
        x = int(input('enter the element of choice for the future of this world: '))
        tem.append(x)
    matrix.append(tem)
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j],end=' ')
    print('\n')

BENEVOLENT_MATRIX = [
    [14,23],
    [32,24]
]

MALEVOLENT_MATRIX = [
    [57,68],
    [75,86]
]

addition_result = [
    [0,0],
    [0,0]
]

subtraction_result = [
    [0,0],
    [0,0]
]

for i in range(2):
    for j in range(2):
        addition_result[i][j] = MALEVOLENT_MATRIX[i][j] + BENEVOLENT_MATRIX[i][j]
        subtraction_result[i][j] = MALEVOLENT_MATRIX[i][j] - BENEVOLENT_MATRIX[i][j]

print('addition result: ')
for i in range(2):
    for j in range(2):
        print(addition_result[i][j],end=' ')
    print('\n')

print('subtraction result: ')
for i in range(2):
    for j in range(2):
        print(subtraction_result[i][j],end=' ')
    print('\n')

