from src.reader import readData


class Chromosome:
    mat = []
    numberOfClasses = 0
    initialized = False

    def __init__(self, val=0, size=20):
        if not self.initialized:
            self.initialized = True
            Chromosome.numberOfClasses, Chromosome.mat = readData(val, size)
