# FILE NAME: processChildren.py
# CREATED : 5.27.2019 
# LAST UPDATED: 5.27.2019 
#
# STATUS: complete 
#
# this module creates a final dictionary of all crossovers in two children
# returns a dict where { "chr#" : { crossover location: 0/1 ...} .... }
#                   0 = maternal crossover
#                   1 = paternal crossover 
#
#ASSUMPTIONS: input is are dictionaries generated from build.generateChild 
#
# GLOBAL VARIABLES: 
from globalVar import *

def mergeChildren(child1 = {}, child2 = {}):
    merged = {}
    for i in range(len(KEYS)):
        child1_xovers = child1[KEYS[i]]
        child2_xovers = child2[KEYS[i]]
        child1_keys = child1_xovers.keys()
        child2_keys = child2_xovers.keys()
        allCrossovers = {}
        for j in range(len(child1_keys)):
            key = child1_keys[j]
            value = child1_xovers[child1_keys[j]]
            allCrossovers.setdefault(key, value)
        for k in range(len(child2_keys)): 
            key = child2_keys[k]
            value = child2_xovers[child2_keys[k]]
            allCrossovers.setdefault(key, value)
        merged.setdefault(KEYS[i], allCrossovers)
    return merged