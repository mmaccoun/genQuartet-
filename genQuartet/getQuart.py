# FILE NAME: getQuart.py
# CREATED : 5.29.2019 
# LAST UPDATED: 6.19.2019 

#this module simulates a quartet and returns a list of values for the portion of two siblings 
#   genotype in IBD state 0/1/2/3

import sys 
sys.path.append("/Users/mmaccoun/Desktop/IBD_xover_analysis/simulation/createSimulation/genQuartet/simChild/")
sys.path.append("/Users/mmaccoun/Desktop/IBD_xover_analysis/simulation/createSimulation/genQuartet/simChild/modules/")

sys.path.append("/Users/mmaccoun/Desktop/IBD_xover_analysis/simulation/createSimulation/genQuartet/compSib/modules/")
sys.path.append("/Users/mmaccoun/Desktop/IBD_xover_analysis/simulation/createSimulation/genQuartet/compSib/")



#GLOBAL VARIABLES:
from globalVar import *
# KEYS[] contains keys to the dictionaries 
# int AUTOSOMES = 22, for the 22 autosomes in a human 
# INDIVID_CHR_LENGTH{} contains key = "chr#", value = int(length of chr according to HG19)

# MODULES:
from simChild import generateChild  
import processChildren 
import rawIBD
import rawToIBD
import trim_for_gaps


def genQuartet(MAT_xover_per_chr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], PAT_xover_per_chr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]) : 
    x = generateChild(MAT_xover_per_chr, PAT_xover_per_chr) #set number of crossovers per chr for maternal and paternal
    y = generateChild(MAT_xover_per_chr, PAT_xover_per_chr) 

    #print("child 1 " + str(x))
    #print()
    #print("child 2 " + str(y))

    combo = processChildren.mergeChildren(x, y) #takes two children crossovers(dict) as parameter returns one dict

    #print(combo)

    # METHOD: rawIBD.getRawIBD(combo = {}, initialMat = 0, initialPat = 0)
    #          combo = merged crossovers --  { 'chr#' : { crossover location: 0/1 ...}... }
    #                                                   where 0 = maternal crossover
    #                                                         1 = paternal crossover 
    #          initialMat = initial raw state of maternal crossover (0 = no crossover, 1 = crossover)
    #          initialPat = initial raw state of paternal crossover (0 = no crossover, 1 = crossover)
    #
    #       returns dict of { "chr#" : {crossover location, raw IBD state ...} ...}  
    SET1_position_w_rawIBD = rawIBD.getRawIBD(combo) #initially, raw IBD is "00", change parameter to change initial IBD state
    #print(SET1_position_w_rawIBD)

    #convert {'chr#' : {crossover_location : rawIBDnumber ...} .... } to portion of siblings genome in IBD states [identical, haploid maternal ID, 
    #                                                                                                             haploid paternal ID, non identical]
    #print("final verion " + str(defVersionIBD))
    
    #  CHECK BEFORE TRIM SEGMENTS
    #chr_num = SET1_position_w_rawIBD.keys()
    #for i in range(len(chr_num)):
    #    print( str(chr_num[i]) + " : ")
    #    xover_list = SET1_position_w_rawIBD[chr_num[i]]
    #    xover_list = sorted(xover_list)
    #    print(xover_list)


    #print(SET1_position_w_rawIBD)

    IBD_states = trim_for_gaps.BED_toBeTrimmed(combo)
    return IBD_states




        
        
