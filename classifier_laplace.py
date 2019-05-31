import numpy as np
import sys

def filereader(filename):
	readfileobj = open(filename,'r')
	data = []
	line = readfileobj.readline()
	while line != '':
		line.strip('\n')
		line.strip('\r')
		line = line.split(",")
		line = map(int,line)
		# ?print line
		data.append(line)
		line = readfileobj.readline()

	# print data

	return data

def stripoutcome(data):
	labels = []
	for i in range(0,len(data)):
		for j in range(0,len(data[i])):
			if(j==0):
				labels.append(data[i][0])


	return labels
def testprobC(traindata):
	countfor0 = 0
	countfor1 = 0

	Listfor0_1 = []
	Listfor0_0 = []
	Listfor1_0 = []
	Listfor1_1 = []
	for x in xrange(0,len(traindata[0])):
		Listfor0_1.append(0)
		Listfor0_0.append(0)
		Listfor1_1.append(0)
		Listfor1_0.append(0)
	
	for i in xrange(0,len(traindata)):
		if traindata[i][0]==1:
			countfor1 = countfor1 + 1
		else:
			countfor0 = countfor0 + 1

		for j in xrange(1, len(traindata[i])):

			if traindata[i][0]==0:

				if traindata[i][j] == 1: 		 		
			   		Listfor0_1[j] = Listfor0_1[j] + 1
			   	else:
					Listfor0_0[j] =Listfor0_0[j] + 1
			if traindata[i][0]==1:
				if traindata[i][j] == 1: 		 		
			   		Listfor1_1[j] = Listfor1_1[j] + 1
			   	else:
					Listfor1_0[j] =Listfor1_0[j] + 1 	
			   	   								
	# print counter
	# print Listfor1_1
	for x in xrange(0,len(Listfor0_0)):
		Listfor0_0[x] = Listfor0_0[x] +1 
		Listfor0_1[x] = Listfor0_1[x] +1 
		Listfor1_0[x] = Listfor1_0[x] +1 
		Listfor1_1[x] = Listfor1_1[x] +1 
		
	Listfor0_0 = np.array(Listfor0_0)/float(countfor0+22)
	Listfor0_1 = np.array(Listfor0_1)/float(countfor0+22)
	Listfor1_0 = np.array(Listfor1_0)/float(countfor1+22)
	Listfor1_1 = np.array(Listfor1_1)/float(countfor1+22)
	# print Listfor1_1
	# print Listfor0_1
	Returnlist = []
	Returnlist.append(Listfor0_0)
	Returnlist.append(Listfor0_1)
	Returnlist.append(Listfor1_1)
	Returnlist.append(Listfor1_0)
	return Returnlist

def classifierProb(traindata):
	countfor0 = 0
	countfor1 = 0
	# train data is labels in this case
	for i in xrange(0,len(traindata)):
		if traindata[i]==0:
		 	countfor0 = countfor0+ 1	
		if traindata[i]==1:
			countfor1 = countfor1 + 1 

	
	probfor0= float(countfor0+1/float(len(traindata)+22))
	probfor1= float(countfor1+1/float(len(traindata)+22))

	classifierlist = []
	classifierlist.append(probfor0)
	classifierlist.append(probfor1)

	return classifierlist

def testfunction(Listfor0_0,Listfor0_1,Listfor1_0,Listfor1_1, testdata, testlabels,classifierlist):
	hits = 0
	labels= []

	print "Testing for", len(testlabels) , "points"
	for i in xrange(0,len(testlabels)):
		probfor0 = classifierlist[0]
		probfor1 = classifierlist[1]
		
		for j in xrange(1,len(testdata[i])):

			if testdata[i][j]==1:
			   probfor0 =  probfor0 * Listfor0_1[j]	
			   probfor1	=  probfor1 * Listfor1_1[j]
			   # print Listfor1_1[j]
			   # break
			else:
				probfor0 = probfor0 * (1-Listfor0_1[j])	
				probfor1 = probfor1 * (1-Listfor1_1[j])

		if(probfor0>probfor1):
		   labels.append(0)
		else:
			labels.append(1)
		# print probfor0
		# print probfor1	
				
	for i in xrange(0,len(testlabels)):
		if testlabels[i]==labels[i]:
			hits = hits + 1

	# print labels
	print "hits", hits
	print "Total Accuracy:" , float(hits*100/float(len(testlabels))) ,"%"
	
			   
		

def main(trainfile,testfile):
	# Reading data
	traindata = filereader(trainfile)
	testdata = filereader(testfile)

	# Reading labels
	trainlabels = stripoutcome(traindata)
	testlabels = stripoutcome(testdata)

	# frequency for 1's and 0's
	probclassifier = classifierProb(trainlabels)
	print "\n\n"
	print "Starting to train data "
	Problist = testprobC(traindata)
	print "Training complete\n\n"
	Listfor0_0 = Problist[0]
	Listfor0_1 = Problist[1]
	Listfor1_1 = Problist[2]
	Listfor1_0 = Problist[3]
	# print Problist
	testfunction(Listfor0_0,Listfor0_1,Listfor1_0,Listfor1_1, testdata, testlabels,probclassifier)



train = sys.argv[1]
test = sys.argv[2]
main(train,test)	
