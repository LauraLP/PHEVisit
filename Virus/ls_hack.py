import csv
def dr_parser(fn, roi_fn, gene):
    '''
    Input: file output from the aligner ('aligner.py'), positions of interest and genes of interest (PR or RT)
    Output: tab-delimited file with the PR positions of interest ('DR_PR_variants.txt')
    '''
    o = open('DR_PR_variants.txt', "w") 
    drugresistancehandle = open(roi_fn, 'r')
    drugresistance = []
    for ln in drugresistancehandle:
        ln = ln.strip('\r\n')
        drugresistance.append(ln)
#print drugresistance
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









print dr_parser('R.out', 'PR_positions.txt', 'PR')


#Future developments:
#Would be good to be able to specify the location of the files (GUI?)
#More testing in the code including informative errors