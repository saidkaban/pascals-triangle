def generate(numRows):
    result = [[1]]
    if numRows == 1:
        return result
    elif numRows == 2:
        result.append([1, 1])
        return result
    else:
        result.append([1, 1])
        for n in range(3, numRows + 1):
            row_result = [1]
            for i in range(1, n - 1):
                a = sum(result[n - 2][(i-1):(i+1)])
                row_result.append(a)
            row_result.append(1)
            result.append(row_result)
        return result
