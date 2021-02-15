from diversity.AlternateDiversity import genetic_algorithm_diversity
from alternate_genotypes.GeneticAlgorithm import GeneticAlgorithm

import random

MUTATION_RATE = 0.1


class BinaryGenotype(GeneticAlgorithm):
    def __init__(self, parameters):
        if "initial_rate" in parameters:
            self.initial_rate = parameters["initial_rate"]
        else:
            self.initial_rate = 0.5

        super().__init__(parameters)

    def random_gene(self):
        return random.random() < self.initial_rate
    
    def mutate(self):
        for i in range(len(self.genes)):
            if random.random() < MUTATION_RATE:
                self.genes[i] = not self.genes[i]
        self.creation_method = "Mutation"
