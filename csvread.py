import csv
import numpy as np

def readcsv(file):
	f = open(file, 'rt')
	try:
	    reader = csv.reader(f)
	    for row in reader:
				size = len(row)
				ismr = np.zeros(size)
				for i in range(size):
					ismr[i] = row[i]
	#				print(ismr[i])
	#			print(size)
	finally:
	    f.close()
	return ismr	


# Testing
#			test = readcsv('ismr.csv')
#			print(test[1])
#def

# Using this function in a file
# from csvread import readcsv
# test = readcsv(filename) 
