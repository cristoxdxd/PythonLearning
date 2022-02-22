def createMatrix():
    matrix = []
    nRows = int(input('Enter the rows number: '))
    nColumns = int(input('Enter the columns number: '))
    for i in range(nRows):
        matrix.append([0] * nColumns)
    size = (nRows,nColumns)
    return matrix, size

def showMatrix(matrix, size):
    rows, columns = size
    for i in range(rows):
        for j in range(columns):
            print(matrix[i][j], end='\t')
        print('')

def fillMatrix(matrix, nRows, nColumns):
    matrix[nRows-1][nColumns-1] = input(f'Enter de value of the row {nRows} in column {nColumns}: ')

def main():
    Board, size = createMatrix()
    showMatrix(Board, size)
    fillMatrix(Board,2,2)
    showMatrix(Board, size)

main()