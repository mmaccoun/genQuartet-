# FILE NAME: convertRawGetFinalIBD.py
# CREATED : 5.27.2019 
# LAST UPDATED: 5.27.2019
#
# status: complete
# 
# MODULE THAT CONVERTS CROSSOVER POSITIONS AND RAW IBD ASSIGNMENT TO IBD LIST OF SEGMENTS OF 
#               CHILDS GENOME
#
# #sort positions of crossovers on each chromosome
# calculate the length of genomic segment depending on crossover location on chromosome 
# take assigned "rawIBD" number which indicate maternal/paternal crossovers and the change of inheritance state
#       then convert to IBD state (0/1/2/3) = (identical/haploid maternal identical/haploid paternal identical/ non identical)
# computes sum of segments in various IBD states and returns a final list with the sum of segments in various IBD states  

from globalVar import * 

import rawToIBD

def compute(dict_with_rawIBD = {}): 
    RETURN_finalIBD = [0, 0, 0, 0]
    segmentLength = 0
    for i in range(len(KEYS)): 
        crossovers = dict_with_rawIBD[KEYS[i]]
        xover_loc = crossovers.keys()
        xover_loc = sorted(xover_loc)
        #print(xover_loc)
        for j in range(len(xover_loc)):
            rawIBDstate = crossovers[xover_loc[j]]
            #print("spot: " + str(xover_loc[j]) + " raw IBD state: " + str(rawIBDstate))
            if j == 0 :
                segmentLength = xover_loc[j] 
            else: 
                segmentLength = xover_loc[j] - xover_loc[j - 1]
            
            rawToIBD.getIBD(rawIBDstate, RETURN_finalIBD, segmentLength)
        
        #print("segment length: " + str(segmentLength) + " at rawIBD state: " + rawIBDstate + " at spot:" + str(xover_loc[j]))

        #outside of list of crossovers 
        last_index = len(xover_loc) - 1
        FINAL_segmentLength = INDIV_CHR_LENGTH[KEYS[i]] - xover_loc[last_index] #get the length of the final segment 
        rawIBDstate = crossovers[xover_loc[last_index]]
        rawToIBD.getIBD(rawIBDstate, RETURN_finalIBD, FINAL_segmentLength)
    return RETURN_finalIBD