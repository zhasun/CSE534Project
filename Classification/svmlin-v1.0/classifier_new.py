import os,sys
import math

labels = ["Natural disaster", "Censorship", "Network attacks", "Maintenance",\
"Device failure", "Fiber cut", "Power outage", "Server",\
"Operator error mistakes", "Routing", "Congestion",\
"DNS resolution", "Mobile data network", "Unknown"]
total_type=14
test=158
train=157
label=test+train
classfiedThreads=[13, 14, 6, 13, 13, 1, 14, 14, 7, 6, 6, 14, 1, 4, 3, 11, 6, 6, 14, 10, 14, 14, 10, 10, 7, 4, 4, 7, 3, 3, 12, 7, 4, 4, 3, 14, 14, 4, 14, 1, 13, 1, 14, 7, 1, 10, 6, 6, 6, 1, 1, 8, 6, 6, 
6, 14, 11, 11, 9, 6, 5, 11, 10, 14, 1, 6, 10, 10, 8, 3, 3, 4, 4, 4, 4, 4, 4, 4, 14, 14, 4, 10, 6, 8, 11, 4, 4, 4, 4, 4, 6, 6, 10, 1, 10, 10, 4, 4, 4, 4, 4, 6, 4, 4, 4, 4, 6, 7, 10, 6, 11, 10, 13, 4, 4, 4, 
4, 4, 4, 4, 10, 10, 10, 4, 5, 13, 10, 14, 5, 4, 10, 4, 4, 4, 4, 4, 4, 4, 13, 5, 11, 4, 4, 4, 4, 10, 10, 10, 6, 1, 6, 6, 6, 10, 3, 4, 10, 2, 2, 2, 2, 9, 9 , 9 , 9, 10, 4, 4, 10, 10, 6, 4, 6, 7, 4, 4, 4, 10, 
1, 6, 4, 4, 4, 4, 4, 6, 4, 6, 4, 4, 4, 4, 4, 4, 4, 8, 10, 4, 4, 4, 4, 4, 4, 4, 10, 10, 4, 4, 4, 4, 10, 4, 4, 7, 4, 6, 7, 7, 5, 6, 4, 6, 10, 10, 4, 8, 7, 11, 4, 4, 13, 13, 10, 14, 10, 13, 13, 4, 4, 4, 4, 4, 
4, 14, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 12, 10, 4, 1, 1, 4, 6, 6, 6, 10, 6, 6, 6, 6, 6, 6, 5, 10, 10, 8, 3, 10, 8, 10, 10, 12, 10, 10, 13, 6, 14, 1, 10, 6, 10, 
6, 14, 2, 2, 2, 2, 9, 9, 9]

with open("caculate_words_cnt-3.txt", "r") as f:
        data = f.read().splitlines()
"""
newclass = [[0 for col in range(len(classfiedThreads))] for row in range(total_type)]
unlabel = [["0" for col in range(len(data)-len(classfiedThreads))] for row in range(total_type)]
for i in range(total_type):
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



test_labels=[["" for j in range(test)] for i in range(total_type)]
train_labels=[["" for j in range(len(unlabel[0])+train)] for i in range(total_type)]

for i in range(total_type):
	for j in range(test):
		test_labels[i][j]=newclass[i][j]

for i in range(total_type):
	for j in range(train):
		train_labels[i][j]=newclass[i][j+test]
	for j in range(len(data)-len(classfiedThreads)):
		train_labels[i][j+train]=unlabel[i][j]

train_data=list()
train_data=data[test:]
test_labeldata=list()
test_labeldata=data[0:test]
test_unlabeldata = list()
test_unlabeldata = data[label:]

out_rootdir = "./RealTime/"

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

for i in range(len(test_labels)):
	output3 = open(out_rootdir+"test_label"+str(i+1)+".txt", 'w')
	for j in range(len(test_labels[i])):
		output3.write(test_labels[i][j]+"\n")
	output3.close()

for i in range(len(train_labels)):
	output4 = open(out_rootdir+"train_label"+str(i+1)+".txt", 'w')
	for j in range(len(train_labels[i])):
		output4.write(train_labels[i][j]+"\n")
	output4.close()


for i in range(total_type):
	os.system("./svmlin -A 3 -W 0.001 -U 1 -R 0.5 ./RealTime/train_data.txt ./RealTime/train_label" + str(i+1)+ ".txt" )
	os.system("mv ./train_data.txt.outputs ./realtime_result/train_data" + str(i+1) + ".txt.outputs")
	os.system("./svmlin -f train_data.txt.weights ./RealTime/test_label_data.txt ./RealTime/test_label" + str(i+1) + ".txt" )
	os.system("mv ./test_label_data.txt.outputs ./realtime_result/test_label_data" + str(i+1) + ".txt.outputs")
	os.system("./svmlin -f train_data.txt.weights ./RealTime/test_unlabel_data.txt")
	os.system("mv ./train_data.txt.weights ./realtime_result/train_data" + str(i+1) + ".txt.weights")	
	os.system("mv ./test_unlabel_data.txt.outputs ./realtime_result/test_unlabel_data" + str(i+1) + ".txt.outputs")


"""
accuracy_list=[0 for i in range(total_type)]
returnrate_list=[0 for i in range(total_type)]
neg_returnrate_list=[0 for i in range(total_type)]
anti_returnrate_list=[0 for i in range(total_type)]
neg_anti_returnrate_list=[0 for i in range(total_type)]
for n in range(total_type):
	with open("./realtime_result/test_label_data" + str(n+1) + ".txt.outputs", "r") as f:
	        data1 = f.read().splitlines()

	with open("./RealTime/test_label"+ str(n+1) + ".txt", "r") as f:
	        data2 = f.read().splitlines()

	for i in range(len(data1)):
		if(float(data1[i])>0):
			data1[i]=1
		else:
			data1[i]=-1

	count=0
	count_return=0
	anti_count=0
	count_anti_return=0
	temp=0
	for i in range(len(data1)):
		if(data1[i]==int(data2[i])):
			temp=temp+1
		if(int(data2[i])==1):
			count = count+1
			if(data1[i] == 1):
				count_return=count_return+1
		if(int(data2[i])==-1):
			anti_count = anti_count+1
			if(data1[i] == -1):
				count_anti_return=count_anti_return+1
	returnrate_list[n]=count_return*1.0/count
	anti_returnrate_list[n]=count_anti_return*1.0/anti_count
	accuracy_list[n]=temp*1.0/len(data1)
for i in range(len(returnrate_list)):
	neg_returnrate_list[i]=1-returnrate_list[i]
for i in range(len(anti_returnrate_list)):
	neg_anti_returnrate_list[i]=1-anti_returnrate_list[i]
print accuracy_list
print returnrate_list
print neg_returnrate_list
print anti_returnrate_list
print neg_anti_returnrate_list


average_accuracy=0
for i in range(len(accuracy_list)):
	average_accuracy += accuracy_list[i]
average_accuracy = average_accuracy/len(accuracy_list)

variance=0
for i in range(len(accuracy_list)):
	variance = variance+(accuracy_list[i]-average_accuracy)*(accuracy_list[i]-average_accuracy)
variance=variance*1.0/14
print "variance of accuracy: " + str(variance)
print "average accuracy: " + str(average_accuracy)


prediction = ["" for i in range(total_type)]
for i in range(total_type):
	with open("./realtime_result/test_unlabel_data" + str(i+1) + ".txt.outputs", "r") as f:
		prediction[i] = f.read().splitlines()

for i in range(len(prediction[0])):
	for j in range(len(prediction)):
		if(float(prediction[j][i])>0):
			prediction[j][i]=1
		else:
			prediction[j][i]=-1

count=[0 for i in range(len(prediction[0]))]
for i in range(len(prediction[0])):
	for j in range(len(prediction)):
		if(prediction[j][i]==1):
			count[i] = count[i]+1

temp=[0 for i in range(15)]
for i in range(15):
	for j in range(len(count)):
		if(count[j]==i):
			temp[i]=temp[i]+1

print temp



"""
final_class=[0 for i in range(len(prediction[0]))]
for i in range(len(prediction[0])):
	belong=set()
	for j in range(len(prediction)):
		if(prediction[j][i]==1):
			belong.add(j)
	max_returnrate=0
	for j in range(len(prediction)):
		if(j in belong):
			if(returnrate_list[j] > max_returnrate):
				max_returnrate = returnrate_list[j]
				final_class[i]=j+1

for i in range(len(final_class)):
	if(final_class[i]==0):
		final_class[i]=anti_returnrate_list.index(min(anti_returnrate_list))+1



new_label=[0 for i in range(len(data))]
for i in range(len(classfiedThreads)):
	new_label[i]=classfiedThreads[i]
for i in range(len(final_class)):
	new_label[i+label]=final_class[i]
print new_label



count=[0 for i in range(total_type)]
for i in range(total_type):
	for j in range(len(new_label)):
		if(new_label[j]==i+1):
			count[i]=count[i]+1
print count
"""







