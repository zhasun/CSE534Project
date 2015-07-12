import os, sys
import math
labels = ["Natural disaster", "Censorship", "Network attacks", "Maintenance",\
"Device failure", "Fiber cut", "Power outage", "Server",\
"Operator error mistakes", "Routing", "Congestion",\
"DNS resolution", "Mobile data network", "Unknown"]


classfiedThreads=[13, 14, 6, 13, 13, 1, 14, 14, 7, 6, 6, 14, 1, 4, 3, 11, 6, 6, 14, 10, 14, 14, 10, 10, 7, 4, 4, 7, 3, 3, 12, 7, 4, 4, 3, 14, 14, 4, 14, 1, 13, 1, 14, 7, 1, 10, 6, 6, 6, 1, 1, 8, 6, 6, 
6, 14, 11, 11, 9, 6, 5, 11, 10, 14, 1, 6, 10, 10, 8, 3, 3, 4, 4, 4, 4, 4, 4, 4, 14, 14, 4, 10, 6, 8, 11, 4, 4, 4, 4, 4, 6, 6, 10, 1, 10, 10, 4, 4, 4, 4, 4, 6, 4, 4, 4, 4, 6, 7, 10, 6, 11, 10, 13, 4, 4, 4, 
4, 4, 4, 4, 10, 10, 10, 4, 5, 13, 10, 14, 5, 4, 10, 4, 4, 4, 4, 4, 4, 4, 13, 5, 11, 4, 4, 4, 4, 10, 10, 10, 6, 1, 6, 6, 6, 10, 3, 4, 10, 2, 2, 2, 2, 9, 9 , 9 , 9, 10, 4, 4, 10, 10, 6, 4, 6, 7, 4, 4, 4, 10, 
1, 6, 4, 4, 4, 4, 4, 6, 4, 6, 4, 4, 4, 4, 4, 4, 4, 8, 10, 4, 4, 4, 4, 4, 4, 4, 10, 10, 4, 4, 4, 4, 10, 4, 4, 7, 4, 6, 7, 7, 5, 6, 4, 6, 10, 10, 4, 8, 7, 11, 4, 4, 13, 13, 10, 14, 10, 13, 13, 4, 4, 4, 4, 4, 
4, 14, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 12, 10, 4, 1, 1, 4, 6, 6, 6, 10, 6, 6, 6, 6, 6, 6, 5, 10, 10, 8, 3, 10, 8, 10, 10, 12, 10, 10, 13, 6, 14, 1, 10, 6, 10, 
6, 14, 2, 2, 2, 2, 9, 9, 9]
"""
count=[0 for i in range(14)]

for i in range(14):
	for j in range(len(classfiedThreads)):
		if(classfiedThreads[j]==i+1):
			count[i]=count[i]+1

print count
print len(classfiedThreads)
"""



"""
newclass = [[0 for col in range(len(classfiedThreads))] for row in range(14)]
unlabel = [["0" for col in range(1787)] for row in range(14)]
for i in range(14):
	if(i==0):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==1):
				newclass[i][j]=str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==1):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==2):
				newclass[i][j]=str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==2):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==3):
				newclass[i][j]=str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==3):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==4):
				newclass[i][j]=str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==4):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==5):
				newclass[i][j]=str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==5):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==6):
				newclass[i][j]=str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==6):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==7):
				newclass[i][j]=str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==7):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==8):
				newclass[i][j]=str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==8):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==9):
				newclass[i][j]=str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==9):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==10):
				newclass[i][j]=str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==10):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==11):
				newclass[i][j]=str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==11):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==12):
				newclass[i][j]=str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==12):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==13):
				newclass[i][j]=str(1)
			else:
				newclass[i][j]=str(-1)
	if(i==13):
		for j in range(len(classfiedThreads)):
			if(classfiedThreads[j]==14):
				newclass[i][j]=str(1)
			else:
				newclass[i][j]=str(-1)



test_labels=[["" for j in range(158)] for i in range(14)]
train_labels=[["" for j in range(1944)] for i in range(14)]

for i in range(14):
	for j in range(158):
		test_labels[i][j]=newclass[i][j]

for i in range(14):
	for j in range(157):
		train_labels[i][j]=newclass[i][j+158]
	for j in range(1787):
		train_labels[i][j+157]=unlabel[i][j]
"""


"""
with open("new_caculate_words_cnt.txt", "r") as f:
        data = f.read().splitlines()


train_data=list()
train_data=data[158:]
test_labeldata=list()
test_labeldata=data[0:158]
test_unlabeldata = list()
test_unlabeldata = data[315:]
"""



"""
out_rootdir = "./Test_new/"
for i in range(len(test_labels)):
	output = open(out_rootdir+"test_label"+str(i+1)+".txt", 'w')
	for j in range(len(test_labels[i])):
		output.write(test_labels[i][j]+"\n")
	output.close()


out_rootdir = "./Test_new/"
for i in range(len(train_labels)):
	output = open(out_rootdir+"train_label"+str(i+1)+".txt", 'w')
	for j in range(len(train_labels[i])):
		output.write(train_labels[i][j]+"\n")
	output.close()
"""

"""
out_rootdir = "./Test_new/"
output = open(out_rootdir+"train_data.txt", 'w')
for i in range(len(train_data)):
	output.write(train_data[i]+"\n")
output.close()

output1 = open(out_rootdir+"test_label_data.txt", 'w')
for i in range(len(test_labeldata)):
	output1.write(test_labeldata[i]+"\n")
output1.close()

output2 = open(out_rootdir+"test_unlabel_data.txt", 'w')
for i in range(len(test_unlabeldata)):
	output2.write(test_unlabeldata[i]+"\n")
output2.close()
"""


return_rate = [0.1, 0.0, 0.2857, 0.7347, 0.25, 0.3913, 0.5, 0.3333, 0.0, 0.5217, 0.4286, 0.0, 0.8571, 0.1875]
outage_Type_modify = [0.791139, 0.829114, 0.810127, 0.689873, 0.797468, 0.696203, 0.841772, 0.860759, 0.841772, 0.734117, 0.810127, 0.85443, 0.829114, 0.759494]
average_modify=0
variance=0
for i in range(len(outage_Type_modify)):
	average_modify += outage_Type_modify[i]
average_modify = average_modify/14
print average_modify
for i in range(len(outage_Type_modify)):
	variance = variance+(outage_Type_modify[i]-average_modify)*(outage_Type_modify[i]-average_modify)
variance=variance*1.0/14
print variance

data = ["" for i in range(14)]

with open("./new_result/test_unlabel_data1.txt.outputs", "r") as f:
        data[0] = f.read().splitlines()

with open("./new_result/test_unlabel_data2.txt.outputs", "r") as f:
        data[1] = f.read().splitlines()

with open("./new_result/test_unlabel_data3.txt.outputs", "r") as f:
        data[2] = f.read().splitlines()

with open("./new_result/test_unlabel_data4.txt.outputs", "r") as f:
        data[3] = f.read().splitlines()

with open("./new_result/test_unlabel_data5.txt.outputs", "r") as f:
        data[4] = f.read().splitlines()

with open("./new_result/test_unlabel_data6.txt.outputs", "r") as f:
        data[5] = f.read().splitlines()

with open("./new_result/test_unlabel_data7.txt.outputs", "r") as f:
        data[6] = f.read().splitlines()

with open("./new_result/test_unlabel_data8.txt.outputs", "r") as f:
        data[7] = f.read().splitlines()

with open("./new_result/test_unlabel_data9.txt.outputs", "r") as f:
        data[8] = f.read().splitlines()

with open("./new_result/test_unlabel_data10.txt.outputs", "r") as f:
        data[9] = f.read().splitlines()

with open("./new_result/test_unlabel_data11.txt.outputs", "r") as f:
        data[10] = f.read().splitlines()

with open("./new_result/test_unlabel_data12.txt.outputs", "r") as f:
        data[11] = f.read().splitlines()

with open("./new_result/test_unlabel_data13.txt.outputs", "r") as f:
        data[12] = f.read().splitlines()

with open("./new_result/test_unlabel_data14.txt.outputs", "r") as f:
        data[13] = f.read().splitlines()

for i in range(len(data[0])):
	for j in range(len(data)):
		if(float(data[j][i])>0):
			data[j][i]=1
		else:
			data[j][i]=-1

final_class=[0 for i in range(1787)]
for i in range(len(data[0])):
	belong=set()
	for j in range(len(data)):
		if(data[j][i]==1):
			belong.add(j)
	max_returnrate=0
	for j in range(len(data)):
		if(j in belong):
			if(return_rate[j] > max_returnrate):
				max_returnrate = return_rate[j]
				final_class[i]=j+1
	
for i in range(len(final_class)):
	if(final_class[i]==0):
		final_class[i]=14

new_label=[0 for i in range(2102)]

for i in range(len(classfiedThreads)):
	new_label[i]=classfiedThreads[i]
for i in range(len(final_class)):
	new_label[i+315]=final_class[i]
print new_label

count=[0 for i in range(14)]

for i in range(14):
	for j in range(len(new_label)):
		if(new_label[j]==i+1):
			count[i]=count[i]+1

print count












