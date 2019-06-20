# FILE NAME: TEST_selectXover.py
# CREATED: 5.25.2019
# LAST UPDATED: 6.17.2019
#run code to see selectXover module function

import sys
#sys.path.insert(0, "~/Desktop/IBD_xover_analysis/simulation/createSimulation/genQuartet/simChild/modules")
sys.path.append("/Users/mary/Desktop/IBD_xover_analysis/simulation/createSimulation/genQuartet/simChild/modules/")
print(sys.path)

from selectXover import parentXover 
from globalVar import * #get global constants 

select_parentXover_test = parentXover(2, AUTOSOMES, INDIV_CHR_LENGTH)
select_parentXover_test2 = parentXover(1, AUTOSOMES, INDIV_CHR_LENGTH)
select_parentXover_test3 = parentXover(5, AUTOSOMES, INDIV_CHR_LENGTH)
select_parentXover_test4 = parentXover(20, AUTOSOMES, INDIV_CHR_LENGTH)
print(select_parentXover_test)
print()
print(select_parentXover_test2)
print()
print(select_parentXover_test3)
print()
print(select_parentXover_test4)

select_parentXover_test4 = parentXover(20, 2, AUTOSOMES, INDIV_CHR_LENGTH) #THROW CASE 