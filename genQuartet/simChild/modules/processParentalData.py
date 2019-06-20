# FILE NAME: selectXover.py
# CREATED : 5.25.2019 
# LAST UPDATED: 6.17.2019 
#
# STATUS: complete 
#
# this module creates a final dictionary of all parental crossovers
#   output dict = { "chr#" : {crossover position, 0/1 ....} .....}
#                   0 = maternal crossover
#                   1 = paternal crossover  
#
#ASSUMPTIONS: input is a dictionary from combParentalXovers.merge 
#
# GLOBAL VARIABLES: 
from globalVar import *

def format( mergedDict = {}) : 
    child1_combine_parentalXovers = {}
    for i in range(len(KEYS)):
        parental_dict = mergedDict[KEYS[i]] 
        
        #print(parental_dict)

        # only 2 keys in dict, 0 = maternal crossover 
        #                      1 = paternal crossover
        xover_loc_combine_crossovers = []
        getMaternal = parental_dict[0]
        getPaternal = parental_dict[1]
        #print(getMaternal)
        #print(getPaternal)
        #print(getMaternal)
        internal_dict = {}
        for j in range(len(getMaternal)):
            xover_loc_combine_crossovers.append(getMaternal[j])
            internal_dict.setdefault(getMaternal[j], 0)
        child1_combine_parentalXovers.setdefault(KEYS[i], internal_dict)
        for k in range(len(getPaternal)):
            xover_loc_combine_crossovers.append(getPaternal[k])
            internal_dict.setdefault(getPaternal[k], 1)
        child1_combine_parentalXovers.setdefault(KEYS[i], internal_dict)
    return child1_combine_parentalXovers