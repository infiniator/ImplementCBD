from src.chromosome import Chromosome


def sequenceToMatrix(sequence):
    components = {}
    for i in range(len(sequence)):
        if sequence[i] in components:
            components[sequence[i]].append(i + 1)
        else:
            components[sequence[i]] = [i + 1]
    return list(components.values())


def matrixToSequence(matrix, myList):
    sequence = myList()
    for i in range(Chromosome.numberOfClasses):
        sequence.append(0)
    for i in range(len(matrix)):
        for j in matrix[i]:
            sequence[j - 1] = i + 1
    return sequence


"""
print(sequenceToMatrix([4, 1, 1, 4, 2, 4, 1, 2]))
print(matrixToSequence(sequenceToMatrix([4, 1, 1, 4, 2, 4, 1, 2]), list))
print(matrixToSequence([[4, 1, 2], [6, 3], [8, 5, 7]], list))
"""
