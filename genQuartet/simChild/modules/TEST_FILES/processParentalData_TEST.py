# FILE NAME: TEST_processParentalData.py
# CREATED: 5.25.2019
# LAST UPDATED: 6.17.2019
#
# STATUS: complete
#
#run code to see processParentalData module function

import sys
sys.path.append("/Users/mmaccoun/Desktop/IBD_xover_analysis/simulation/createSimulation/genQuartet/simChild/modules")

from globalVar import * 

# MODULES: 
from selectXover import parentXover
from combParentalXovers import merge 
from processParentalData import format 


#get crossover location for maternal genome 
NUM_MATERNAL_CROSSOVERS = 2 #2 crossover per chr 
maternal_genome = parentXover(NUM_MATERNAL_CROSSOVERS, AUTOSOMES, INDIV_CHR_LENGTH)

#get crossover location for paternal genome 
NUM_PATERNAL_CROSSOVERS = 1 #1 crossover per chr 
paternal_genome = parentXover(NUM_PATERNAL_CROSSOVERS, AUTOSOMES, INDIV_CHR_LENGTH)

child_genome = merge(maternal_genome, paternal_genome) #get combined dictionary (pre process)

child_genome = format(child_genome)

#see new format of data where 
# dict = { "chr #" : { xover-location (float #), 0 / 1} }
#           where 0 = maternal crossover
#                 1 = paternal crossover

print(" MAT CROSSOVERS * * * * ")
print(maternal_genome)
print(" PAT CROSSOVERS * * * * ")
print(paternal_genome)
print("STATE OF CHILD GENOME ... ")
print(child_genome)