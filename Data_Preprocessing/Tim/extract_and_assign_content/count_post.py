import os, sys
path = "outages/"
dirs = os.listdir(path)
total_count = 0
total_count2 = 0
for filename in dirs:
	count = 0
	count2 = 0
	with open(path+filename, "r") as f:
		lines = f.readlines()
		for line in lines:	
			word = line.split(" ")
			if word and word[0] == "Message-ID:":
				count+=1
			if word and word[0] == "In-Reply-To:":
				count2+=1
		print(filename+ " has " + str(count) + " posts.")
		print(filename+ " has " + str(count2) + " repliess.")
		total_count +=count
		total_count2 +=count2
print("Total posts = " + str(total_count))
print("Total replies = " + str(total_count2))
'''
In-Reply-To:
'''