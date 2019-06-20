* - * READ ME * - *

PROJECT: IBD STATES USING CROSSOVERS ANALYSIS  
WORKING DIRECTORY: ~/Desktop/IBD_xover_analysis/simulation/createSimulation/genQuartet
FILE CREATED: 6.18.2019
LAST UPDATED: 6.18.2019

This directory contains the scripts which simulates data for a quartet 

* - * File Names/Subdirectories & Descriptions * - *

getQuartet.py : generates a simulated quartet, will accept 2 lists as parameters, with list 1  = maternal [list of crossovers per chromosome] and list 2  = paternal [list of crossovers per chromosome]
	from getQuartet import genQuartet 
	genQuartet(MAT_xover_per_chr[], PAT_xover_per_chr[])



getQuart_TEST.py : script which prints IBD results of genQuartet module

simChild/ : subdir which contains scripts that simulate one sibling in a quartet (modules  in this dir used in getQuartet.py)

compSib/ : subdir which contains scripts that computes IBD states for a quartet (2 siblings simulated per quartet) 

ORIGINAL_SIM/ : subdir which contains the ORIGINAL AND OUT OF DATE (before documentation/edits) version to simulate a quartet **likely delete/remove from project

