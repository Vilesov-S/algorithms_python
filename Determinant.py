
def determinant (matrix):
    result = 0
    if len(matrix) == 1:
        return (matrix[0][0])
    
    column_index = 0
    for row_index in range(len(matrix)):
        minor = []
        minor_row_index = 0
        for i in range(len(matrix)):
            if i != row_index:
                minor.append([])
                for j in range(len(matrix[i])):
                    if j != column_index:
                        minor[minor_row_index].append(matrix[i][j])
                minor_row_index += 1
    
        if (row_index+column_index) % 2 == 0:
            alalgebraic_complement = matrix[row_index][column_index]
        else:
            alalgebraic_complement = -matrix[row_index][column_index]
        result += determinant(minor) * alalgebraic_complement
    return result


def main():
    matrix = [[1, 4, 7],
              [5, 3, 8],
              [9, 6, 8]]
    print(determinant(matrix)) # 125

    matrix = [[54,  5,   78, 32],
              [9,   10,  5,  88],
              [11,  12,  33, 45],
              [109, 999, 56, 44]]
    print(determinant(matrix)) # -95289005

if __name__ == "__main__":
    main()
