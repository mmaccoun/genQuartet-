# FILE NAME: genChild
# FILE CREATED: 5.25.2019 
# LAST UPDATED: 6.5.2019
#
# STATUS: complete
# 
# file returns a dict of maternal and paternal crossovers combined
#   child = { "chr #" : [ 0,[sorted list of maternal xover locations] ],
#                       [ 1, [sorted list of paternal xover locations] ]      
#           }
#
# ASSUMPTIONS: crossover rates on maternal and paternal genome are unequal 
#       child inherets crossovers from both parents 
#       *CROSSOVER_LOC = crossover locations on each chromosome 
#
#

# MODULES: 
import sys
sys.path.append("/Users/mmaccoun/Desktop/IBD_xover_analysis/simulation/createSimulation/genQuartet/simChild/modules")
from selectXover import parentXover 
from combParentalXovers import merge 
import processParentalData as process 
from globalVar import * 

def generateChild(NUM_MATERNAL_CROSSOVERS = [], NUM_PATERNAL_CROSSOVERS = []):
    #get crossover location for maternal genome 
    maternal_genome = parentXover(NUM_MATERNAL_CROSSOVERS, AUTOSOMES, INDIV_CHR_LENGTH)
    #get crossover location for paternal genome 
    paternal_genome = parentXover(NUM_PATERNAL_CROSSOVERS, AUTOSOMES, INDIV_CHR_LENGTH)
    #combine maternal and paternal genome to generate a simulated child's genome 
    child_genome= merge(maternal_genome, paternal_genome)
    child_genome = process.format(child_genome)
    return child_genome

