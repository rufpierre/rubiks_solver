#! /usr/bin/env python

"""
Very simple demo in which organisms try to minimise
the output value of a function
"""

from pygene.gene import BaseGene, FloatGene, FloatGeneMax
from pygene.organism import Organism, MendelOrganism
from pygene.population import Population
from random import random, uniform










class FloatGeneMine(BaseGene):
    """
    A gene whose value is a floating point number

    Class variables to override:

        - mutAmt - default 0.1 - amount by which to mutate.
          The gene will will move this proportion towards
          its permissible extreme values

        - randMin - default -1.0 - minimum possible value
          for this gene. Mutation will never allow the gene's
          value to be less than this

        - randMax - default 1.0 - maximum possible value
          for this gene. Mutation will never allow the gene's
          value to be greater than this
    """
#==============================================================================
#     # amount by which to mutate, will change value
#     # by up to +/- this amount
#     mutAmt = 0.1
#     
#     # used for random gene creation
#     # override in subclasses
#     randMin = -1.0
#     randMax = 1.0
#==============================================================================
    
    
    # genes get randomly generated within this range
    randMin = -100.0
    randMax = 100.0
    
    # probability of mutation
    mutProb = 0.1
    
    # degree of mutation
    mutAmt = 0.1
    
    
    
#==============================================================================
#     def __add__(self, other):
#         """
#         Combines two genes in a gene pair, to produce an effect
#     
#         This is used to determine the gene's phenotype
#     
#         This class computes the arithmetic mean
#         of the two genes' values, so is akin to incomplete
#         dominance.
#     
#         Override if desired
#         """
#         return (self.value + other.value) / 2
#==============================================================================
    
    def mutate(self):
        """
        Mutate this gene's value by a random amount
        within the range, which is determined by
        multiplying self.mutAmt by the distance of the
        gene's current value from either endpoint of legal values
        
        perform mutation IN-PLACE, ie don't return mutated copy
        """
        if random() < 0.5:
            # mutate downwards
            self.value -= uniform(0, self.mutAmt * (self.value-self.randMin))
        else:
            # mutate upwards:
            self.value += uniform(0, self.mutAmt * (self.randMax-self.value))
    
    def randomValue(self):
        """
        Generates a plausible random value
        for this gene.
        
        Override as needed
        """
        min = self.randMin
        range = self.randMax - min
    
        return random() * range + min

    def __add__(self, other):
        """
        produces phenotype of gene pair, as the greater of this
        and the other gene's values
        """
        return max(self.value, other.value)



class Converger(MendelOrganism):
    """
    Implements the organism which tries
    to converge a function
    """
    genome = {'x':FloatGeneMine, 'y':FloatGeneMine}
    
    def fitness(self):
        """
        Implements the 'fitness function' for this species.
        Organisms try to evolve to minimise this function's value
        """
        return self['x'] ** 2 + self['y'] ** 2

    def __repr__(self):
        return "<Converger fitness=%f x=%s y=%s>" % (
            self.fitness(), self['x'], self['y'])


# create an empty population

pop = Population(species=Converger, init=2, childCount=50, childCull=20)


# now a func to run the population

def main():
    try:
        while True:
            # execute a generation
            pop.gen()

            # get the fittest member
            best = pop.best()
            
            # and dump it out
            print best

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()

