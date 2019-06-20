# FILE NAME: rawIBD.py
# CREATED : 5.27.2019 
# LAST UPDATED: 5.28.2019 
#
# STATUS: complete 
#
# this module creates sorts crossover positions and determines the rawIBD state depending on
#   if the crossover observed is maternal or paternal
#
# GLOBAL VARIABLES: 
from globalVar import *

import random

def checkCurrent(currentParent = 0) : 
    if currentParent == 0:
        currentParent = 1
    else: 
        currentParent = 0 
    return currentParent

def setCurrent(currentMat = 0, currentPat = 0):
    currentState = str(currentMat) + str(currentPat)
    return currentState

# returns a dict where { "chr#": {crossover location: rawIBDstate, .....}......}
# ASSUMES: input dict is a dictionary of crossovers merged from two children
#           output from processChildren.mergeChildren()
# initialMat and initialPat will set the currentIBD state 
def getRawIBD(combo = {}) : 
    final = {}
    #print(currentState)
    for i in range(len(KEYS)): #for each chr
        #pick random starting IBD state 
        currentMat = random.randint(0,1)
        currentPat = random.randint(0,1)
        currentState = setCurrent(currentMat, currentPat)
        #print(currentState)
        crossovers = combo[KEYS[i]] #dict of where crossovers / chr 
        #print(crossovers)
        xover_loc = crossovers.keys()
        xover_loc = sorted(xover_loc) #list of xovers in chromosome
        subDict = {} 
        for j in range(len(xover_loc)): #for each crossover on a chr
            xover_type = crossovers[xover_loc[j]] # 0 or 1 for mat/pat crossover 
            #print("crossover type :" + str(xover_type) + " spot: " + str(xover_loc[j]))
            #xover_type indicates maternal or paternal crossover
            #xover_loc[j] == crossover location 
            # print(xover_loc[j]) #SEE CURRENT LOCATION 
            if xover_type == 1:
                #print("paternal") #TYPE OF CROSSOVER 
                currentPat = checkCurrent(currentPat)
            else:
                #print("maternal") #TYPE OF CROSSOVER
                currentMat = checkCurrent(currentMat)
            currentState = setCurrent(currentMat, currentPat)
            subDict.setdefault(xover_loc[j], currentState)
        final.setdefault(KEYS[i], subDict)
    return final
