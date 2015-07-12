import os, sys
labels = ["Routing", "Power outage", "Packet loss", "Natural disaster",\
"Mobile data network", "Fiber cut", "DNS resolution", "Device failure",\
"Congestion", "Censorship", "Attack", "Application server",\
"Application configuration", "Maintenance"]

classfiedThreads = [1, 10, 10, 6, 1, 13, 13, 10, 10, 10, 13, 7, 3, 4, 3, 7, 7, 7, 0, 3, 5, 5, 3, 7, 3, 3, 7, 5, 3, 7]

newclass = [[0 for col in range(len(classfiedThreads))] for row in range(14)]
for i in range(14):
	if(i==0):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==0):
				newclass[i][j]="+"+str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==1):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==1):
				newclass[i][j]="+"+str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==2):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==2):
				newclass[i][j]="+"+str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==3):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==3):
				newclass[i][j]="+"+str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==4):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==4):
				newclass[i][j]="+"+str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==5):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==5):
				newclass[i][j]="+"+str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==6):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==6):
				newclass[i][j]="+"+str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==7):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==7):
				newclass[i][j]="+"+str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==8):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==8):
				newclass[i][j]="+"+str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==9):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==9):
				newclass[i][j]="+"+str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==10):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==10):
				newclass[i][j]="+"+str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==11):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==11):
				newclass[i][j]="+"+str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==12):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==12):
				newclass[i][j]="+"+str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==13):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==13):
				newclass[i][j]="+"+str(1)
			else:
				newclass[i][j]=str(-1)
with open("caculate_words_cnt.txt", "r") as f:
        data = f.read().splitlines()


newdata=[["" for j in range(len(classfiedThreads))] for i in range(14)]

for i in range(14):
	for j in range(len(data)):
		newdata[i][j] = newdata[i][j] + newclass[i][j]+" "
		thread = data[j].split()
		for k in range(len(thread)):
			newdata[i][j] = newdata[i][j]+ str(k+1)+":"+str(thread[k])+" "


out_rootdir = "./Data_for_try/"
for i in range(len(newdata)):
	output = open(out_rootdir+str(i+1)+".txt", 'w')
	for j in range(len(newdata[i])):
		output.write(newdata[i][j]+"\n")
	output.close()



