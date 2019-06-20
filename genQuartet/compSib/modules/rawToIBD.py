# FILE NAME: rawToIBD.py
# CREATED : 5.27.2019 
# LAST UPDATED: 5.27.2019 
#
# STATUS: complete 
#
# this module will take the rawIBD assignment of a crossover location
#  and will add the length of the segment to the appropriate IBD state

# RAW IBD to IBD conversion:
# '00' = IBD0 / identical
# '01' = IBD1 / haploid paternal identical
# '10' = IBD0 / haploid maternal identical
# '11'= IBD3 / not identical
#
#ASSUMPTIONS: use rawIBD state for position as parameter 

def getIBD( rawIBDstate = '', IBDstates = [0, 0, 0, 0], segmentLength = 0):
    if rawIBDstate == '00':
        IBDstates[0] = IBDstates[0] + segmentLength
    elif rawIBDstate == '01':
        IBDstates[1] = IBDstates[1] + segmentLength
    elif rawIBDstate == '10':
        IBDstates[2] = IBDstates[2] + segmentLength
    else: #rawIBDstate == '11'
        IBDstates[3] = IBDstates[3] + segmentLength