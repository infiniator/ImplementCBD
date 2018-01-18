import random

for i in range(10):
    n = 20
    fileID = 'data' + str(i) + f'{n:04d}' + '.txt'
    file = open('../data/' + fileID, 'w')
    file.write(str(n))
    file.write('\n')
    for i in range(n):
        for j in range(n):
            if i != j:
                cost = random.randrange(0, 101)
            else:
                cost = 0
            file.write(str(cost))
            file.write(' ')
        file.write('\n')
    file.close()
