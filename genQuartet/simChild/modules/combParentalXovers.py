# FILE NAME: combineParentalXovers.py
# FILE CREATED: 5.25.2019 
# LAST UPDATED: 6.17.2019
#
# STATUS: complete
#
# this module takes two dictionaries -- one that holds all the maternal crossovers per chromosome
#                                        and one that holds all the paternal crossovers per chromosome 
#
#   final data structure returned is a dict where 
#   { "chr num" : { 0/1 : [ list of crossovers ] }}
#       where 0 = maternal crossovers,  1 = paternal crossovers 

import sys
sys.path.append("/Users/mmaccoun/Desktop/IBD_xover_analysis/simulation/createSimulation/genQuartet/simChild/modules")

# GLOBAL VARIABLES: 
from globalVar import * 


def merge( MAT = {}, PAT = {}) : 
    child = {}
    for i in range(0, AUTOSOMES):
        chrName = "chr"  + str(i + 1)
        ID_and_LOC_for_chr = {}
        MAT_xover = MAT[chrName] #list of xovers in mother
        PAT_xover = PAT[chrName] 

        MAT_crossoverList = []
        for i in range(len(MAT_xover)): #for each crossover loc in mother
            MAT_crossoverList.append(MAT_xover[i])
        ID_and_LOC_for_chr.setdefault(0, MAT_crossoverList)
        child.setdefault(chrName, ID_and_LOC_for_chr)

        PAT_crossoverList = []
        for i in range(len(PAT_xover)): #for each crossover loc in mother
            PAT_crossoverList.append(PAT_xover[i])
        ID_and_LOC_for_chr.setdefault(1, PAT_crossoverList)
        child.setdefault(chrName, ID_and_LOC_for_chr)
    return child

