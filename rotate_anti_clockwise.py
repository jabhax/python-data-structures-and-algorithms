def rotateImageClockwise(a):
    n = len(a)
    for row in range(int(n/2)):
        for col in range(row, n-row-1):
            temp = a[row][col]
            a[row][col] = a[n-1-col][row]
            a[n-1-col][row] = a[n-1-row][n-1-col]
            a[n-1-row][n-1-col] = a[col][n-1-row]
            a[col][n-1-row] = temp
    return a


def rotateImageAntiClockwise(a):
    n = len(a)
    for row in range(int(n/2)):
        for col in range(row, n-row-1):
            temp = a[row][col]
            # Move value from Right -> Top
            a[row][col] = a[col][n-1-row]
            # Move value from Bottom -> Right
            a[col][n-1-row] = a[n-1-row][n-1-col]
            # Move values from Left -> Bottom
            a[n-1-row][n-1-col] = a[n-1-col][row]
            # Move temp -> Left
            a[n-1-col][row] = temp
    return a

