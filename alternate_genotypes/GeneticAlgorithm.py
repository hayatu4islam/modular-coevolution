from diversity.AlternateDiversity import genetic_algorithm_diversity
from Evolution.BaseGenotype import BaseGenotype

import random

MAX_VALUE = 10
MUTATION_RATE = 0.33


class GeneticAlgorithm(BaseGenotype):
    def __init__(self, parameters):
        super().__init__(parameters)
        if "values" in parameters:
            self.genes = parameters["values"].copy()
            return

        if "length" in parameters:
            self.genes = list()
            for _ in range(parameters["length"]):
                self.genes.append(random.random() * MAX_VALUE)
        else:
            raise TypeError("If \"values\" is not provided, a \"length\" must be.")

    def mutate(self):
        for i in range(len(self.genes)):
            if random.random() < MUTATION_RATE:
                self.genes[i] = self.genes[i] + random.gauss(0, MAX_VALUE / 10)
                self.genes[i] = max(0, min(self.genes[i], MAX_VALUE))
        self.creation_method = "Mutation"

    def recombine(self, donor):
        for i in range(len(self.genes)):
            if random.random() < 0.5:
                self.genes[i] = donor.genes[i]
        self.parents.append(donor)
        self.creation_method = "Recombination"

    def clone(self, copy_objectives={}):
        parameters = {"values": self.genes}
        cloned_genotype = GeneticAlgorithm(parameters)
        if copy_objectives:
            for objective in self.objectives:
                cloned_genotype.objectives[objective] = self.objectives[objective]
                cloned_genotype.objective_statistics[objective] = self.objective_statistics[objective]
                cloned_genotype.objectives_counter[objective] = self.objectives_counter[objective]
                cloned_genotype.past_objectives[objective] = self.past_objectives[objective]
        cloned_genotype.parents.append(self)
        cloned_genotype.creation_method = "Cloning"
        return cloned_genotype

    def get_fitness_modifier(self):
        return 0

    def get_raw_genotype(self):
        return {"values": self.genes}

    def diversity_function(self, population, reference=None):
        return genetic_algorithm_diversity(population, reference)

    def __str__(self):
        return str(self.genes)