# ***  LENGTHS OF CHROMOSOMES BASED on HG19 *** 
AUTOSOMES = 22 #global variable, number of autosomes considered 

#global dict to get lengths of individual chroomosomes (from hg19 database)
# dict { "chr #" : int( #) }
INDIV_CHR_LENGTH = { "chr1"	: 249250621,
                    "chr2" :	243199373,
                    "chr3" :	198022430,
                    "chr4" :	191154276,
                    "chr5" :	180915260,
                    "chr6" :	171115067,
                    "chr7" :	159138663,
                    "chr8"	: 146364022,
                    "chr9" :	141213431,
                    "chr10" :	135534747,
                    "chr11" :	135006516,
                    "chr12" :	133851895,
                    "chr13" :	115169878,
                    "chr14" :	107349540,
                    "chr15" :	102531392,
                    "chr16" :	90354753,
                    "chr17" :	81195210,
                    "chr18" :	78077248,
                    "chr20" :	63025520,
                    "chr19" :	59128983,
                    "chr22" :	51304566,
                    "chr21" :	48129895
                   }

KEYS = INDIV_CHR_LENGTH.keys()

# *** COMPUTE CUMULATIVE GENOMIC LENGTH ***
# final varialbe = hg19_genomicSum
# is cumulative sum of all individual chr                
#
# final dict = { 'chr #' : #}
# is cumulative sum of all individual chr up to that chr [ length chr number 1 , length this chr ]        

hg19_genomicSum = INDIV_CHR_LENGTH["chr" + str(1)]
hg19_wholeGenome = dict()
hg19_wholeGenome["chr1"] = 249250621
for i in range(2,23):
    hg19_genomicSum = hg19_genomicSum + INDIV_CHR_LENGTH["chr" + str(i) ]
    #print(hg19Sum)
    hg19_wholeGenome.setdefault(str("chr")+ str(i), hg19_genomicSum )
