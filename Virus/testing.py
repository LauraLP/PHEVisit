import csv
o = open("DRvariants.txt", "w") 
drugresistance=['Apos','10','11','16','20','24','30','32','33','34','36','43','46','47','48','50']
with open('R.out','r') as f:
    reader=csv.reader(f,delimiter='\t')
    for line in reader:
    	if line[0]=='>PR':
    		continue
    	elif line[0]=='>RT':
    		break
    	else:
    		if line[15] in drugresistance:
				for char in line:
					o.write(char+"\t")
				o.write("\n")
