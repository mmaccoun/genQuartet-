* - * READ ME * - *

PROJECT: IBD STATES USING CROSSOVERS ANALYSIS  
WORKING DIRECTORY: ~/IBDd_xover_analysis/simulation/createSimulation/genQuartet/simChild/modules
FILE CREATED: 6.17.2019
LAST UPDATED: 6.18.2019
CONTACT: mmaccoun@systemsbiology.org

This directory contains scripts with modules which are used to simulate a child's genome randomly selecting crossover locations along 
the maternal and paternal genome. 

* - * File Names/Subdirectories & Descriptions * - *

globalVar.py : file with global variables which are constantly referred to ... data from hg19 

selectXover.py : selects a random point on the chromosome as a crossover location
                returns a sorted dictionary of the crossover locations on each chromosome 
                 * OUTPUT : dict = {'chr# : [list of all crossover points on the chromosome] }
        *MODULE: 
                from selectXover import parentXover
                parentXover(crossover = 0, autosome = 0, chrLengthDict = {})
                    crossover = number of crossovers per chromosome 
                    autosome = number of chromosomes to select a crossover for 
                    chrLengthDict = length of each chromosome, lengths defined by hg19

combParentalXovers.py : combine crossover locations from maternal and paternal genome 
                         * OUTPUT = {"chr#" : {0 : [sorted_list_of_maternal_crossovers], 
                                               1 : [list_of_paternal_crossovers] } }
        *MODULE:
            from combineParentalXovers import merge 
            merge(MAT = {}, PAT = {})
                MAT = dict with crossovers along the maternal genome 
                PAT = dict with crossovers along the paternal genome 

processParentalData.py : process dict that represents child's genome from merge module (combParentalXovers.py)
                            to be used to simulate a quartet 
            * MODULE:
                from processParentalData import format
                format(mergedDict {} )
                mergedDict = output dict generated from merge module (combParentalXovers.py)


TEST_FILES/ : scripts that show how modules in this directory work 

data/ : subdir with data needed about chromosome lengths (according to hg19)
