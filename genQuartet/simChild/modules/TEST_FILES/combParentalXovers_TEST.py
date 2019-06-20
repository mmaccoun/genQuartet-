# FILE NAME: combineParentalXovers_TEST.py
# FILE CREATED: 6.17.2019 
# LAST UPDATED: 6.17.2019
#
# STATUS: complete
#
# run code to see combineParentalXovers module work 

import sys
sys.path.append("/Users/mary/Desktop/IBD_xover_analysis/simulation/createSimulation/genQuartet/simChild/modules")

from globalVar import *
from selectXover import parentXover 
from combParentalXovers import merge

maternal_genome = parentXover(2, AUTOSOMES, INDIV_CHR_LENGTH)
print("Crossovers on the maternal genome: " + str(maternal_genome))
print()
paternal_genome = parentXover(1, AUTOSOMES, INDIV_CHR_LENGTH)
print("Crossovers on the paternal genome: " + str(paternal_genome))
print()

child_genome = merge(maternal_genome, paternal_genome)
print("Crossovers on the child's genome: " + str(child_genome))
