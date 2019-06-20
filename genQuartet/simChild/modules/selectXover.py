# FILE NAME: selectXover.py
# CREATED : 5.25.2019 
# LAST UPDATED: 6.17.2019 
#
#  STATUS: complete 
#
# parameter crossover determines the number of crossovers on a chromosome 
# a random point on the chromosome is selected as a crossover location 
# returns a sorted dictionary of the crossover locations on each chromosome 
# dict = { "chr #" : [ list of sorted xover positions, len() = crossover ]}

import numpy as np
from globalVar import *

np.random.seed(100) #reproduce data 


#crossover[] is equal to the number of crossovers per 
def parentXover(crossover = [], autosome = 0, chrLengthDict = {}) : 
    final = {}
    for i in range(1, autosome + 1 ) :
        key = "chr" + str(i)
        value = []
        chrLength = chrLengthDict.get(key)
        xover_per_chr = [0]
        for j in range(len(crossover)):
            #np.random.random_sample() selects random number [0, 1)
            # that number * (length of given chr) = crossover location
            point = np.random.random_sample() * float(chrLength) 
            point = int(point) #round xover location to closest whole number since pybedtools will not accept 
            #                   float
            value.append(point)
        value = sorted(value) #list locations in order
        value.append(chrLengthDict[key])
        final.setdefault(key, value)
    return final #list 

