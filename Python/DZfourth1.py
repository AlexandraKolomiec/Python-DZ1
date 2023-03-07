#Напишите функцию для транспонирования матрицы

def matrix_turn (m: list) -> list[str]:

    mt = [[0 for j in range(len(m))] for i in range (len(m[0]))]
   
    for i in range (len(m)):
        for j in range (len (m[0])):
            mt [j][i] = m [i][j]
    return mt

print(matrix_turn([[1, 2], [3, 4], [5, 6]]))

