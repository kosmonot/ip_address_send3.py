#! /usr/bin/env python


# Check for internet connection

import urllib2
import time
import string

def internet_on():
    try:
        response=urllib2.urlopen('http://www.google.com/',timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False

#loop_value = 1
#while (loop_value == 1):
#    try:
#	urllib2.urlopen("http://www.google.com")
#    except urllib2.URLError, e:
#	time.sleep( 10 )
#    else:
#	loop_value = 0
	
# Commands to be run if internet connection is present:
if internet_on():
	# Get external IP from canyouseeme.org by searching html page for an IP address
	import urllib
	import re 
	f = urllib.urlopen("http://myip.dnsdynamic.org/")
	html_doc = f.read()
	f.close()
	m = re.search('(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)',html_doc)
	# print html_doc
	#print m.group(0)
	current_ipaddress = m.group(0)

	# Look at last line of ip log file
	IPlog = open ('iplog.txt')
	lineList = IPlog.readlines()
	IPlog.close()
	# print (lineList)
	# print ("The last line is:")
	# print (lineList[len(lineList)-1])
	# or simply
	# print (lineList[-1])
	# print current_ipaddress

	# See if current IP has changed from last logged
	if current_ipaddress + "\n" <> lineList[-1]:
		#Append ip address to ip log file
		f = open('iplog.txt','a')
		localtime = time.asctime( time.localtime(time.time()) )
		f.write(localtime + "\n" + current_ipaddress + "\n")
		# python will convert \n to os.linesep
		f.close()
	
		# Mail new ip	 
		import smtplib
 		smtp_server = 'smtp.gmail.com'
		smtp_port = 587
 		sender = '****@gmail.com'
		# recipients = ["*****2001@hotmail.com", "john@***.com"]
		recipients = ["*****@***.com"]


		subject = 'SERVER ALERT'
		body = 'Server IP address has changed to: ' + current_ipaddress
		password = '**********************'
		smstext = body 
		body = "" + body + ""
 	
		headers = ["From: " + sender,
	           "Subject: " + subject,
	           #"To: " + "Fred and John",
	           "To: " + "John",
	           "MIME-Version: 1.0",
	           "Content-Type: text/html"]
		headers = "\r\n".join(headers)
 
		session = smtplib.SMTP(smtp_server, smtp_port)
 
		session.ehlo()
		session.starttls()
		session.ehlo
		session.login(sender, password)
 
		session.sendmail(sender, recipients, headers + "\r\n\r\n" + body)
		session.quit()


		# Google Voice SMS send
		import pygvoicelib
		conn = pygvoicelib
                                                                                                             
		username="**************"
		apppass="****************************"
		auth_token="***********************************"
		client = conn.GoogleVoice(username,apppass,auth_token,rnr_se)
		#phone number below
		client.sms('1212673****',smstext)

                                                                        

	
