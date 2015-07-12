import os,sys
import math 
import string
import re
import os.path



def remove_words(parent,filename):
    with open(os.path.join(parent,filename), "r") as f:
        data = f.read().splitlines()

    output = open(out_rootdir+filename, 'w')

    dic =[]

    print "Begin load data"
    cnt = 0
    subject = ""
    contain = ""
    i = 0
    while i< len(data)-2:
    	#print "&&&&&&& "+ str(i)
        row = data[i]
        if ("##############################################" in data[i] and ("END" != data[i+1]) and (data[i+1]!="") and "####################################################" in data[i+2]):
            subject_word = re.findall(r"[\w']+|[.,!?;_]",data[i+1])
            for j in range(len(subject_word)):
                if (subject_word[j].lower() not in stop_words) and (subject_word[j] not in string.punctuation) and subject_word[j].isdigit()==False:
                    subject += subject_word[j].lower()+" "
            dic.append(subject)
            #print "SB "+subject+" "+str(i)
            i=i+3
        elif re.search("<http:", row):
            #print "I here"+str(i)
            while (">" not in data[i]):
                i += 1
            i += 1
        elif re.search("<mailto:", row):
            #print "I here"+str(i)
            while (">" not in data[i]):
                i += 1
            i += 1
        elif re.search("\[mailto:", row):
            while ("]" not in data[i]):
                i += 1
            i += 1
        elif ("BEGIN PGP SIGNED MESSAGE" in data[i] or "Hash: SHA1" in data[i] or "Original Message" in data[i] or "---" in data[i] or "__" in data[i] or " Name:" in data[i]):
            i += 1
        elif ("Subject:" in data[i] or "Date:" in data[i] or "From:" in data[i] or "http:" in data[i] or " Reply-To:" in data[i] or "URL:" in data[i] or "Sent:" in data[i] or "Cc:" in data[i]):
            i += 1
        elif ("###########################################" in data[i] and "END" == data[i+1] and "######################################################" in data[i+2]):
            dic[cnt] += contain
            subject = ""
            contain = ""
            cnt += 1
            i=i+3
        else:
            row = data[i]
            if ( data[i].find('<') >=0 and data[i].find('>')>=0 ):
    			row = data[i][:data[i].find('<') ]
    			row += data[i][data[i].find('>')+1:]
            if ( data[i].find('|') >=0 and data[i].find('|')>=0 ):
                row = row[:row.find('|') ]
                row += row[row.find('|')+1:]

            #print "**********" + row 
            word = re.findall(r"[\w']+|[.,!?;]",row)
            #word = row.split()  # as default using the ' ' to split item
            for j in range(len(word)):
                if (word[j].lower() not in stop_words) and (word[j] not in string.punctuation) and word[j].isdigit()==False and re.search(r'[0-9]',word[j])==None :
                	#if word[j]== "\n":
                	#	continue
                    contain += word[j].lower()+" "
            i += 1
                    
    for i in range(len(dic)):
        output.write(dic[i]+"\n")
    output.close()
    print "End"

rootdir = './Semifinished/'
out_rootdir = './Data_Source/'

with open("stop_words_en.txt", "r") as f:
    stop_words = f.read().splitlines()


for j in range(len(stop_words)):
    stop_words[j] = stop_words[j].lower()

for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        if filename[0] == '.':
            continue
        print "Dealing with:" +os.path.join(parent,filename)
        remove_words(parent,filename)
        #break






