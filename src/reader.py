def readData(test, size):
    fileID = 'data/data' + str(test) + f'{size:04d}' + '.txt'
    file = open(fileID, 'r')
    size = int(file.readline().strip())
    mat = []
    for i in range(size):
        temp = file.readline().strip().split()
        mat.append([])
        for j in temp:
            mat[i].append(int(j))
    return size, mat
