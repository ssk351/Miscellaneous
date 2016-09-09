from csvread import readcsv

ismr  = readcsv('ismr.csv')
nino3 = readcsv('nino3.csv')
no_of_months = len(ismr)

ismr_nino3 = [ [ [None],[None] ] for x in xrange(no_of_months) ]


for i in range(no_of_months):
	ismr_nino3[i][0][0] = ismr[i]
	ismr_nino3[i][1][0] = nino3[i]

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




