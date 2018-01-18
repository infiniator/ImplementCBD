import random
import matplotlib.pyplot as plt
from statistics import mean
from deap import base
from deap import creator
from deap import tools

from src.genetic_algorithm import initialisation
from src.genetic_algorithm import mutateSplitMergeProbabilistic
from src.genetic_algorithm import crossoverSwapComponentSequences
from src.fitness import calculateFitness
from src.chromosome import Chromosome


def main(size, gen, crossover):
    t = Chromosome(0, size)
    # low coupling, high cohesion
    creator.create('FitnessMinMax', base.Fitness, weights=(1.0, -1.0))
    creator.create('Individual', list, fitness=creator.FitnessMinMax)

    MU = size
    NGEN = gen
    CXPB = crossover

    toolbox = base.Toolbox()
    toolbox.register("individual", initialisation, creator.Individual)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", calculateFitness,
                     myChromosome=creator.Individual)
    toolbox.register("select", tools.selNSGA2)
    toolbox.register("mate", crossoverSwapComponentSequences,
                     myChromosome=creator.Individual)
    toolbox.register("mutate", mutateSplitMergeProbabilistic, probSplit=0.6,
                     probMerge=0.4, myChromosome=creator.Individual)

    pop = toolbox.population(n=MU)

    invalid_ind = [ind for ind in pop if not ind.fitness.valid]
    fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit

    pop = toolbox.select(pop, len(pop))

    plotCohesion = []
    plotCoupling = []
    for gen in range(0, NGEN):
        offspring = tools.selTournamentDCD(pop, 2)
        offspring = [toolbox.clone(ind) for ind in offspring]
        print('Iteration %d' % gen)

        for ind1, ind2 in zip(offspring[::2], offspring[1::2]):
            if random.random() <= CXPB:
                toolbox.mate(ind1, ind2)

            toolbox.mutate(ind1)
            toolbox.mutate(ind2)
            del ind1.fitness.values, ind2.fitness.values

        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        pop = toolbox.select(pop + offspring, MU)
        plotCohesion.append(mean([i.fitness.values[0] for i in pop]))
        plotCoupling.append(mean([i.fitness.values[1] for i in pop]))

    plt.plot(plotCohesion)
    plt.xlabel('Number of iterations')
    plt.ylabel('Mean cohesion of the population')
    s = 'cohesion.svg'
    plt.savefig(s, format='svg')
    plt.gcf().clear()

    plt.plot(plotCoupling)
    plt.xlabel('Number of iterations')
    plt.ylabel('Mean coupling of the population')
    s = 'coupling.svg'
    plt.savefig(s, format='svg')
    plt.gcf().clear()
    return pop


size = 20
gen = 100
crossover = 0.95
for i in main(size, gen, crossover):
    print(i)
