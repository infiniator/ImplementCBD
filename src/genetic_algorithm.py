import random
from src import converter
from src.chromosome import Chromosome


def initialisation(myChromosome):
    num = Chromosome.numberOfClasses  # number of classes
    temp = myChromosome()
    for i in range(num):
        temp.append(random.randrange(num / 10, num / 2))
    temp = converter.matrixToSequence(converter.sequenceToMatrix(temp),
                                      myChromosome)
    return temp


def mutateMergeComponents(seq, myChromosome):
    matrix = converter.sequenceToMatrix(seq)
    candidateA = 0
    candidateB = 0
    while candidateA == candidateB:
        candidateA = random.randrange(0, len(matrix))
        candidateB = random.randrange(0, len(matrix))
    matrix[candidateA] = matrix[candidateA] + matrix[candidateB]
    del matrix[candidateB]
    return converter.matrixToSequence(matrix, myChromosome)


def mutateSplitComponents(seq, myChromosome):
    matrix = converter.sequenceToMatrix(seq)
    candidate = None
    while candidate is None or len(matrix[candidate]) <= 1:
        candidate = random.randrange(0, len(matrix))
    splitID = random.randrange(1, len(matrix[candidate]))
    matrix.append(matrix[candidate][:splitID])
    matrix.append(matrix[candidate][splitID:])
    del matrix[candidate]
    return converter.matrixToSequence(matrix, myChromosome)


def mutateSplitMergeProbabilistic(seq, probSplit, probMerge, myChromosome):
    import numpy as np
    return np.random.choice([mutateSplitComponents, mutateMergeComponents],
                            p=[probSplit, probMerge])(seq, myChromosome)


def crossoverSwapComponentSequences(seqA, seqB, myChromosome):
    matA = converter.sequenceToMatrix(seqA)
    matB = converter.sequenceToMatrix(seqB)
    concA = []
    concB = []
    for i in matA:
        concA = concA + i
    for i in matB:
        concB = concB + i
    resA = []
    resB = []
    a = 0
    b = 0
    for i in matA:
        resB.append(concB[a:a + len(i)])
        a = a + len(i)
    for i in matB:
        resA.append(concA[b:b + len(i)])
        b = b + len(i)
    return converter.matrixToSequence(resA,
                                      myChromosome), converter.matrixToSequence(
        resB, myChromosome)
