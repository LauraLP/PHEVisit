import csv
import re
def bac_parser(fn):
    '''
    Input: file output from the aligner ('aligner.py'), positions of interest as a column and genes of interest (PR or RT)
    Output: tab-delimited file with the PR positions of interest ('DR_PR_variants.txt')
    '''
    #Read in the file with the required positions and create a list of strings
    vcfhandle = open(fn, 'r')
    outputfilename = fn.split('.')[0]
    o = open(str(outputfilename)+'filtered.txt', "w") #Write to same directory as input file (filepath will be part of this)
    vcf = vcfhandle.read()
    #vcf = vcf.split()
    #print vcf
    vcf = re.sub(r'(?m)^\#.*\n?', '', vcf) #If line starts with a # then remove
    print vcf
    line = vcf.split('\n')
    #for str in line:

    #subset = line.split('\t')
    #print subset
    #print line
    #for character in vcf:
        #print character
        #f = character.split(' ')
        #print f
        #print f[0]

    #g = thefile.split(s[, '>'[, -1]])
    #print g

    #print thefile
    
    #for line in thefilehandle:
        #print line
    


'''
    with open(fn,'r') as f:
        reader=csv.reader(f,delimiter='\t')
        for line in reader:
            if line[0]=='>'+gene:
                continue
            elif line[0]=='>RT':
                break
            else:
                if line[15] in drugresistance:
                    for char in line:
                        o.write(char+"\t")
                    o.write("\n")
    return 'complete'
'''








print bac_parser('/Users/laura/clin_bio/snp_pipeline_results_n/test.vcf')



#Future developments:
#Would be good to be able to specify the location of the files (GUI?)
#More testing in the code including informative errors