import csv
def dr_parser(fn, roi_fn, gene):
    '''
    Input: file output from the aligner ('aligner.py'), positions of interest as a column and genes of interest (PR or RT)
    Output: tab-delimited file with the PR positions of interest ('DR_PR_variants.txt')
    '''
    #Read in the file with the required positions and create a list of strings
    o = open('DR_PR_variants.txt', "w") 
    drugresistancehandle = open(roi_fn, 'r')
    drugresistance = drugresistancehandle.read()
    drugresistance = drugresistance.split()

    #Read in the text file output from aligner.py
    thefilehandle = open(fn,'r')
    thefile = thefilehandle.read()
    
    g = thefile.split(s[, '>'[, -1]])
    print g

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








print dr_parser('R.out', 'PR_positions.txt', 'PR')


#Future developments:
#Would be good to be able to specify the location of the files (GUI?)
#More testing in the code including informative errors