# FILE NAME: trim_for_gaps.py
# CREATED : 6.5.2019 
# LAST UPDATED: 6.18.2019 
#
# STATUS: COMPLETE 
#
# PURPOSE: trim gaps from crossover segments, transfer raw IBD states from untrimmed segments
#           and process to calculate IBD states of a quartet  



import io 
import sys 
sys.path.append("/Users/mmaccoun/Desktop/IBD_xover_analysis/simulation/createSimulation/genQuartet/simChild/modules")
import pybedtools as BED
import pandas as pd
import random
import os
from globalVar import * #dict CHR_LENGTH 

def checkCurrent(currentParent = 0) : # binary to check if crossover occurred/not 
    if currentParent == 0:
        currentParent = 1
    else: 
        currentParent = 0 
    return currentParent

def setCurrent(currentMat = 0, currentPat = 0): # randomly assign a starting 0 or 1 for maternal or paternal 
    currentState = str(currentMat) + str(currentPat)
    return currentState

#assumes input is dict generated from modules.compSib.proccessChildren()
def BED_toBeTrimmed(combo = {} ): 
    chr_nums = combo.keys()
    OG_segments = open('./untrimmed_segments.txt', 'w+') 
    for i in range(len(chr_nums)):
        thisChr = chr_nums[i]
        xover_and_rawIBD = combo[thisChr]

        currentMat = random.randint(0,1)
        currentPat = random.randint(0,1)
        currentState = setCurrent(currentMat, currentPat) #pick some random way to start 

        get_xovers_per_chr = xover_and_rawIBD.keys()
        xover_per_chr = sorted(get_xovers_per_chr)
        xover_per_chr.insert(0,0) #add starting value of 0 to list 
        xover_per_chr.append(INDIV_CHR_LENGTH[thisChr])
        for j in range(1, len(xover_per_chr) - 1, 1): 
            startPt = xover_per_chr[j - 1]
            endPt = xover_per_chr[j]
            xover_PARENT = xover_and_rawIBD[xover_per_chr[j]]
            if xover_PARENT == 1:
                    #print("paternal") #TYPE OF CROSSOVER 
                currentPat = checkCurrent(currentPat)
            else:
                    #print("maternal") #TYPE OF CROSSOVER
                currentMat = checkCurrent(currentMat)
            currentState = setCurrent(currentMat, currentPat)
            segment = startPt - endPt 
            
            string_for_TXT = str(thisChr) + '\t' + str(int(startPt)) + '\t' + str(int(endPt)) + '\t' + str(currentState) + "\n"
            #print(string_for_TXT)
            OG_segments.write(string_for_TXT)
    OG_segments.close()

    # * # * # * # * TRIM SEGMENTS FOR GAPS (bedtools) # * # * # * # * #
    trimGaps = 'bedtools subtract -b filtered_gaps.txt -a untrimmed_segments.txt > trimmed_seg_with_rawIBD.txt'
    os.system(trimGaps)


        # * # * # * # * get IBD # * # * # * # * #
    get_IBD_breakdown = pd.read_table("./trimmed_seg_with_rawIBD.txt", sep = "\t", header = None)
    IBD_states = [0 ,0, 0, 0]
    for i in range(len(get_IBD_breakdown.iloc[:, 0])):
        segment = get_IBD_breakdown.iloc[i, 2] - get_IBD_breakdown.iloc[i, 1] #calculated from sum of ALL "crossover" segments 
        #print(segment)
        raw_ibd_state = str(get_IBD_breakdown.iloc[i, 3])
        #print("raw ibd state: " +  str(raw_ibd_state))
        if raw_ibd_state == '0':
            #print("hit 1")
            IBD_states[0] = IBD_states[0] + int(segment) 
        if raw_ibd_state == '1':
            #print("hit 2")
            IBD_states[1] = IBD_states[1] + int(segment) 
        if raw_ibd_state == '10':
            #print("hit 3")
            IBD_states[2] = IBD_states[2] + int(segment) 
        if raw_ibd_state == '11':
            #print("hit 4")
            IBD_states[3] = IBD_states[3] + int(segment)
    # GEMONIC SUM BASED ON SUM OF SEGMENTS (93.14% of hg19 genomic sum with gaps removed covered )
    #           likely 7% of genome lost when rounding 
    
    #print(IBD_states)

    #GENOMIC_SUM = 0
    #for i in range(len(get_IBD_breakdown.iloc[:, 0])):
    #    segment = get_IBD_breakdown.iloc[i, 2] - get_IBD_breakdown.iloc[i, 1]
    #    GENOMIC_SUM = GENOMIC_SUM + segment 

    #print(GENOMIC_SUM)

    # get printed output 
    #print("PORTION OF QUART GENOME IN IBD:" + str(IBD_states))
    TEST_PERCENT = 0
    GENOMIC_SUM = 2736096286  #gaps removed 
    IBD_STATE_PERCENTS = []
    for i in range(len(IBD_states)):
        value = IBD_states[i]
        #print(value)
        TEST_PERCENT = float(value)/ GENOMIC_SUM + TEST_PERCENT
        
        #print( "IBD" + str(i + 1) + ": " + str( (float(value)/ GENOMIC_SUM) * 100) + " %" ) 
        IBD_STATE_PERCENTS.append((float(value)/ GENOMIC_SUM) * 100)
        #print("SUM IBD PORTIONS = " + str(TEST_PERCENT))
        
    return IBD_states

    