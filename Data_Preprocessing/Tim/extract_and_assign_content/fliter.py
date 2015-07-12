import os, sys
'''
=====================================================
-  Functions : Skip Unimportant Information         -
=====================================================
'''
def skipInformation(str):
	if str == ">" or str == "In-Reply-To:" or str =="References:"\
		or str =="Message-ID:" or str =="To:" or str =="CC:"\
		or str ==">>":
		return 1
	else:
		return 0
def skipPGPSIGNATURE(str):
	if str == "-----BEGIN PGP SIGNATURE-----\n":
		return 1
	elif str == "-----END PGP SIGNATURE-----\n":
		return 0
	else:
		return 2

'''
=====================================================
-  Functions : Skip Information for Final content   -
=====================================================
'''
def skipFinalContentInformation(str):
	if str == "From:" or str == "Sent:" or str =="Subject:"\
		or str =="Status:" or str =="To:" or str =="CC:"\
		or str =="Status" or str =="Name:" or str =="Hash:":
		return 1
	else:
		return 0

'''
=====================================================
-  Functions : Clean up and extract subject         -
=====================================================
'''
def removeEndSymbol(str, eliminate_symbol):
	xx = str.split(eliminate_symbol)
	if len(xx) > 1:
		return xx[0]
	else:
		return xx[0]

def removeStartSymbol(str, eliminate_symbol):
	xx = str.split(eliminate_symbol)
	if len(xx) > 1:
		return xx[1]
	else:
		return xx[0]

def cleanUpSubject(str):
	x = str.split("Fwd: ")
	if len(x) > 1:
		yy = x[1].split("Re: ")
		if len(yy)>1:
			pre_subject = yy[1]
		else:
			pre_subject = yy[0]
	elif len(x) == 1:
		pre_subject = x[0]
	
	pre_subject = removeEndSymbol(pre_subject, "(fwd)")
	pre_subject = removeEndSymbol(pre_subject, "\n")
	pre_subject = removeStartSymbol(pre_subject, "FW: ")
	pre_subject = removeStartSymbol(pre_subject, "RE: ")	
	pre_subject.lstrip('')
	return pre_subject

'''
=====================================================
-   Main function                                   -
=====================================================
Initial Setting:
- subject_list = all Subjects
- message_list = all Message-ID
- reference_id_list = all Reference-ID
- Usubject_id_list = all Subjects without duplicate
- Umessage_id_list = all Message-ID without duplicate
-----------------------------------------------------
'''

#---------------- Open and Read File ----------------
path = "proccessed/fixed/"
dirs = os.listdir( path )

#for filename in dirs:
subject_list = []
message_id_list = []
reference_id_list = []
reply_id_list = []
Usubject_list = []
Umessage_id_list = []
Ucontent_id_list = []
filename = "2014-September.txt"
with open("proccessed/fixed/"+filename, "rw+") as f:
		lines = f.readlines()
#---------------- Subject Processing ----------------
pre_word=[]
for index in range(len(lines)):
	word = lines[index].split()
	if index-1 > 0:
		pre_word = lines[index-1].split()
	if index+1 < len(lines):
		nlword = lines[index+1].split()
	if not word:
		continue
	else:
		if pre_word and len(word)>2:
			exist = 0
			if word[0] == "Subject:" and word[1] =="[Outages]" and pre_word[0]=="Date:":
				word = lines[index].split("[Outages] ")
				subject_list.append(cleanUpSubject(word[1]))
			elif word[0] == "Subject:" and word[1] =="[outages]" and pre_word[0]=="Date:":
				word = lines[index].split("[outages] ")
				subject_list.append(cleanUpSubject(word[1]))

#--------------- Message-ID Processing --------------		
	if word[0] == "Message-ID:":
		message_id_list.append(word[1])

#--------------- In-Reply-To Processing -------------
nlword = []
for index in range(len(lines)):
	word = lines[index].split()
	if index+1 < len(lines):
		nlword = lines[index+1].split()
	if not word:
		continue
	else:
		#print "###############################################################\n"
		#print lines[index]
		#print len(word)
		#print len(nlword)
		#print "###############################################################"
		if nlword and len(word)>2:
			if word[0] == "Subject:" and word[1] =="[Outages]" and nlword[0]=="In-Reply-To:":
				reply_id_list.append(nlword[1])
			elif word[0] == "Subject:" and word[1] =="[Outages]" and nlword[0]!="In-Reply-To:":
				reply_id_list.append("0")

			if word[0] == "Subject:" and word[1] =="[outages]" and nlword[0]=="In-Reply-To:":
				reply_id_list.append(nlword[1])
			elif word[0] == "Subject:" and word[1] =="[outages]" and nlword[0]!="In-Reply-To:":
				reply_id_list.append("0")



#-------------- References ID Processing ------------
for index in range(len(lines)):
	word = lines[index].split()
	if index+1 < len(lines):
		nlword = lines[index+1].split()
	if not word:
		continue
	else:
		if nlword:
			if word[0] == "In-Reply-To:" and nlword[0]=="References:":
				reference_id_list.append(nlword[1])
			elif word[0] == "In-Reply-To:" and nlword[0]=="Message-ID:":
				reference_id_list.append("0")
		if nlword and len(word)>2:
			if word[0] == "Subject:" and word[1] =="[Outages]" and nlword[0]=="References:":
				reference_id_list.append(nlword[1])
			elif word[0] == "Subject:" and word[1] =="[outages]" and nlword[0]=="References:":
				reference_id_list.append(nlword[1])
			elif word[0] == "Subject:" and word[1] =="[Outages]" and nlword[0]!="In-Reply-To:" and nlword[0]!="Date:" and nlword[0]!="Sent:":
				reference_id_list.append("0")
			elif word[0] == "Subject:" and word[1] =="[outages]" and nlword[0]!="In-Reply-To:" and nlword[0]!="Date:" and nlword[0]!="Sent:":
				reference_id_list.append("0")


print len(subject_list)
print len(message_id_list)
print len(reply_id_list)
print len(reference_id_list)

for x in reference_id_list:
	print x


#--------------- Content Processing -----------------
#set the same number of space as number of subject for the content list
content = []
startPoint = 0
content_text =" "
count = 0
skip = 0
pre_word=[]
next_word=[]
for index in range(len(lines)):
	word = lines[index].split()
	if index-1 > 0:
		pre_word = lines[index-1].split()
	if index+1 < len(lines):
		next_word = lines[index+1].split()
	if not word:
		continue
	else:
        #====== skip unimportant information =======
		if skipInformation(word[0])==1:
			continue
		if skipPGPSIGNATURE(lines[index])==1:
			skip = 1
		if skipPGPSIGNATURE(lines[index])==0:
			skip = 0
			continue
		if skip == 1:
			continue
        #===========================================
        try:
		if word[0]=="From" and next_word[0]=="From:" and startPoint==1:
			content.append(content_text)
			content_text = ""
			startPoint = 0
		if startPoint == 1:
			content_text = content_text + " " + lines[index]
		if word[0]=="Subject:" and pre_word[0]=="Date:":
			startPoint = 1
	except:
			if (1==0):
				print ""
content.append(content_text)
#--------- Find host-post and its Message-ID --------
for index in range(len(subject_list)):
	subject_title = subject_list[index]
	message_title = message_id_list[index]
	if subject_title not in Usubject_list:
		Usubject_list.append(subject_title)
		Umessage_id_list.append(message_title)
	elif subject_title in Usubject_list and reference_id_list[index]=="0":
		Usubject_list.append(subject_title)
		Umessage_id_list.append(message_title)

#------ Assign Content To Subject Accordingly -------
#Ucontent = [None] * len(Usubject_list)
Ucontent = [None]*len(Usubject_list)
uindex = ""
for index in range(len(reference_id_list)):
	if message_id_list[index] in Umessage_id_list:
		uindex = Umessage_id_list.index(message_id_list[index])
		if Ucontent[uindex] == None:
			Ucontent[uindex] = content[index]
		else:
			Ucontent[uindex] = Ucontent[uindex]+ content[index]
	elif reference_id_list[index] in Umessage_id_list:
		uindex = Umessage_id_list.index(reference_id_list[index])
		if Ucontent[uindex] == None:
			Ucontent[uindex] = content[index]
		else:
			Ucontent[uindex] = Ucontent[uindex]+content[index]
'''
for x in Ucontent:
	print "###############################################################\n"
	print x
	print "###############################################################\n"
'''
#-------- Combine the content for same topic ---------
Fsubject = []
for subject in Usubject_list:
	if subject not in Fsubject:
		Fsubject.append(subject)

Fcontent = [None]*len(Fsubject)
for index in range(len(Usubject_list)):
	location = Fsubject.index(Usubject_list[index])
	if Fcontent[location] == None:
		Fcontent[location] = Ucontent[index]
	else:
		Fcontent[location] = Fcontent[location] + Ucontent[index]

f = open("New2-"+filename,'w')

for index in range(len(Fcontent)):
	f.write("###############################################################\n")
	f.write(Fsubject[index]+"\n")
	f.write("###############################################################\n")
	if Fcontent[index]==None:
		f.write("None")
	else:
		f.write(Fcontent[index])
	f.write("###############################################################\n")
	f.write("END\n")
	f.write("###############################################################\n")
	f.write("\n")
f.close()
print "Output "+ filename +" succeed."




	
		

