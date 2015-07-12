import imaplib
import email

def get_subjects(email_id,username, password):
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login(username, password)
	mail.list()
	mail.select('inbox')
	subject = ""
	result, data = mail.fetch(email_id, '(BODY[HEADER.FIELDS (SUBJECT)])')
	for letter in data[0][1]:
		if letter!= '\n' and letter!='\r':
			subject+=letter
	return subject

username = ''
password = ''
targetEmailAddress = ''
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(username, password)
while True:
	mail.list()
	mail.select('inbox')
	result, data = mail.search(None, '(UNSEEN)', '(FROM "%s")' % (targetEmailAddress))
	ids = data[0]
	id_list = ids.split()
	for email_id in id_list:
		result, data = mail.fetch(email_id, "(RFC822)")
		raw_email = email.message_from_string(data[0][1])
		for part in raw_email.walk():
			if part.get_content_maintype()=='multipart':
				continue
			if part.get_content_subtype()!='plain':
				continue
			payload = part.get_payload()
			lines = payload.split('\n')
			subject = get_subjects(email_id, username, password)
			print subject
			for line in lines:
				if '> On' in line:
					break
				else:
					print line
			mail.store(email_id, '+FLAGS', '\Seen')
