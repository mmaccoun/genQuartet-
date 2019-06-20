# FILE NAME: calculatePercent.py
# CREATED : 5.27.2019 
# LAST UPDATED: 6.18.2019 
#
# STATUS: complete 
#
# this module returns the percentage breakdown of IBD states 
# input would be a list with the sum of lengths of the segments that account for each IBD state
#
# GLOBAL VARIABLES 
import sys 
sys.path.append("/Users/mary/Desktop/IBD_xover_analysis/simulation/createSimulation/genQuartet/simChild/modules")
from globalVar import *

def percent(IBDstates = [0,0,0,0]): 
    percList = []
    for i in range(len(IBDstates)): 
        IBDsum = IBDstates[i]
        this_perc = IBDsum / float(hg19_genomicSum)
        percList.append(this_perc)
    return percList
