from src.converter import sequenceToMatrix
from src.converter import matrixToSequence
from src.chromosome import Chromosome

"""
mat=[[0, 5, 2, 4, 2, 3], [5, 0, 3, 2, 3, 4], [3, 2, 0, 5, 4, 5], [5, 3, 2, 0, 2, 2], [2, 3, 4, 5, 0, 3], [3, 2, 4, 5, 4, 0]]
list1=[]
list1.append([2,3])
list1.append([1,4])
list1.append([5,6])
sum1=0
sum2=0
"""


def cohesion(components):
    sum1 = 0
    for i in range(len(components)):
        for j in range(len(components[i])):
            for k in range(j + 1, len(components[i])):
                sum1 += Chromosome.mat[components[i][j] - 1][
                            components[i][k] - 1] + \
                        Chromosome.mat[components[i][k] - 1][
                            components[i][j] - 1]
    return sum1


def coupling(components):
    sum2 = 0
    for i in range(len(components)):
        for j in range(len(components[i])):
            for k in range(i + 1, len(components)):
                for l in range(len(components[k])):
                    sum2 += Chromosome.mat[components[i][j] - 1][
                                components[k][l] - 1] + \
                            Chromosome.mat[components[k][l] - 1][
                                components[i][j] - 1]
    return sum2


def calculateFitness(sequence, myChromosome):
    sequence = matrixToSequence(sequenceToMatrix(sequence), myChromosome)
    coh = cohesion(sequenceToMatrix(sequence))
    cou = coupling(sequenceToMatrix(sequence))
    return coh, cou,
