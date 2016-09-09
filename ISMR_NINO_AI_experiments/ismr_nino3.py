from csvread import readcsv
from neuron3to4lyr import NN

ismr  = readcsv('ismr.csv')
nino3 = readcsv('nino3.csv')
no_of_months = len(ismr)

ismr_nino3 = [ [ [None],[None] ] for x in xrange(no_of_months) ]
ismr_nino3_train = [ [ [None],[None] ] for x in xrange(no_of_months-500) ]
ismr_nino3_test = [ [ [None],[None] ] for x in xrange(500) ]


for i in range(no_of_months):
	ismr_nino3[i][0][0] = ismr[i]
	ismr_nino3[i][1][0] = nino3[i]

ismr_nino3_train = ismr_nino3[0:no_of_months-500-1]
ismr_nino3_test  = ismr_nino3[no_of_months-500:no_of_months-1]
# create a network with two input, two hidden, and one output nodes
n = NN(1, 4, 2 , 1)
# train it with some patterns
n.train(ismr_nino3_train)
# save a network
# test it
n.test(ismr_nino3_test)

#pat = [
#        [[0,0], [0]],
#        [[0,1], [1]],
#        [[1,0], [1]]
##        [[1,1], [1]]
#    ]
#
#
##	Testing for patterns
#print(pat[1])
#B = [ [ [None, None],[None] ] for x in xrange(3) ]
#for i in range(3):
#	B[i] = pat[i]
#print(B[0])
#print(B[0][0])
#print(B[0][0][0])

#pat = [
#        [[0], [0]],
#        [[0], [1]],
#        [[1], [1]]
##        [[1,1], [1]]
#    ]
#
#
#B = [ [ [None],[None] ] for x in xrange(3) ]
#for i in range(3):
#	B[i] = pat[i]
#print(B[1])
#print(B[1][1][0])
#print(B[1][0][0])
#
#print(B[1][1][1])




