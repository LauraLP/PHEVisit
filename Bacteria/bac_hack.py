import csv
import re
def bac_parser(fn):
    '''
    Input: file output from the aligner ('aligner.py'), positions of interest as a column and genes of interest (PR or RT)
    Output: tab-delimited file with the PR positions of interest ('DR_PR_variants.txt')
    '''
    #Read in the file with the required positions and create a list of strings
    #position = []
    #allele = []
    #info = []
    #genotype = []
    with open(fn,'r') as f:
        vcf=csv.reader(f,delimiter='\t')
        outputfilename = fn.split('.')[0]
        o = open(str(outputfilename)+'filtered.tsv', "w") #Write to same directory as input file (filepath will be part of this)
        vcfwriter = csv.writer(o, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for line in vcf:
            if line[0].startswith('#'):
                continue    
            else:
                #position.append(line[1])
                #allele.append(line[4])
                #info.append(line[7])
                #genotype.append(line[9])
                #print type (line[7])
                templine9 = (line[9]).split(':')
                #print templine9
                line9 = templine9[0] + '\t' + templine9[1] + '\t' + templine9[2] +'\t' + templine9[3]
                #print line9
                #In here filter on- if filter fails don't write
                #if templine9[0] != '1/1' or templine9[0] != '0/0':



                vcfwriter.writerow([line[1], line[4], line[7], line[9], line9])     


print bac_parser('/Users/laura/clin_bio/snp_pipeline_results_n/test.vcf')

#def splitlist(lst):
    #'''
    #break the list by ; or : in order to easily access the individual data.
    #'''
    #for item in lst:

    #vcf = vcfhandle.read()
    #vcf = vcf.split()
    #print vcf
    #vcf = re.sub(r'(?m)^\#.*\n?', '', vcf) #If line starts with a # then remove
    #print vcf
    #line = vcf.split('\n')
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

