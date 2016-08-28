import csv
def lineNumber(file1, file2):
	if len(list(readera)) == len(list(readerb)):
		return True
	else:
		return False

with open('filea.csv', 'rU') as filea,  open('fileb.csv', 'rU') as fileb:
	readera = csv.DictReader(filea)
	readerb = csv.DictReader(fileb)
	count = 0
	for rowa,rowb in zip(readera, readerb):
		if lineNumber(filea,fileb):
			diffkeys = [k for k in rowa if rowa[k] != rowb[k]]
			count = count+1
			for k in diffkeys:
			 	print "Line:", count,"Column:", k, ':', "Expected:",rowa[k], '->', "Actual:", rowb[k] 
		else:
	  		print "The two files have different line number. Check sources"
	filea.close()
	fileb.close()