#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
./Xi4u7 - AndroSec1337 Cyber Team
2k18 - Die :v
Error ? Report Cuk Ke.
Email : androsec1337@gmail.com
Fb : https://fb.com/Xi4u7
"""
print("""
          .:'
      __ :'__
   .'`__`-'__``.
  :__________.-'
  :_________: Valid Email
   :_________`-;  Checker
    `.__.-.__.'
""")
import requests, re, sys
try:
	filelist = sys.argv[1]
	loglive = open('live.txt','a')
	logdie = open('die.txt','a')
	logun = open('uncheck.txt','a')
except Exception as Err:
	print("ERROR : File List Not Found!")
	sys.exit()
list = open(filelist, "r")
while True:
	email = list.readline().replace("\n","")
	if not email:
		break
	s = requests.session()
	head1 = {"User-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 YaBrowser/18.10.2.119.00 Mobile Safari/537.36","Referer":"https://appleid.apple.com/account","Accept-Encoding":"gzip, deflate, sdch, br","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}
	html1 = s.get("https://appleid.apple.com/account#!&page=create", headers=head1)
	scnt = re.findall("scnt: '(.*?)'", html1.text)[0]
	apikey = re.findall("apiKey: '(.*?)'", html1.text)[0]
	sessionId = re.findall("sessionId: '(.*?)", html1.text)[0]
	head2 = {"User-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 YaBrowser/18.10.2.119.00 Mobile Safari/537.36","Origin":"https://appleid.apple.com","Referer":"https://appleid.apple.com/account","X-Apple-Request-Context":"create","Requested-With":"XMLHttpRequest","scnt":scnt,"X-Apple-Api-Key":apikey,"X-Apple-ID-Session-Id":sessionId,"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","Content-Type":"application/json",'X-Apple-I-FD-Client-Info':'{"U":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 YaBrowser/18.10.2.119.00 Mobile Safari/537.36","L":"id-ID","Z":"GMT+07:00","V":"1.1","F":"kWa44j1e3NlY5BSo9z4ofjb75PaK4Vpjt1szHVXU3vtnTDovyhbQ3zIRbPhj03x.dXnYbFdH6PEwHXXTSHCSPmtd0wVYPIG_qvoPfybYb5EvYTrYesR2hQnH6hAOfUftmF5wMQE5nXxQD6CKaMhQWx2KlTTpZHgfLMC7AeLd7FmrpwoNN5uQ4s5uQ1szHVzZrefOJQuyPB94UXuGlfUm4ly_03y8rnawSdrxQDq8yatDpQT18u0I4b6DWHZDoUs_43wuZPup_nH2t05oaYAhrcpMxE6DBUr5xj6Kks6PraZEPLnLzMnZVCsiqTCb4uqRDPfBjPr2u5fXwxf7_OLgiPFMqbN0TUMpwoNRe98vPSb_GGEOpBSKxUC56MnGWpwoNSUC53ZXnN87gq1a293lio8dOHr_i.uJtHoqvynx9MsFyxYMH0XKJ7lrHay.9aB.KB4D93tG2hixAwlMsITxYMJ5uFBHeNNW5BNlYicklY5BqNAE.lTjV.5Ec"}'}
	data = '{"emailAddress":"'+email+'"}'
	test = s.post("https://appleid.apple.com/account/validation/appleid", data=data, headers=head2).json()
	if test["valid"] == False:
		print("\033[33mUNCHECK\033[0m : "+email)
		logun.write(email+"\n")
		pass
	elif test["used"] == True:
		print("\033[32mLIVE\033[0m : "+email)
		loglive.write(email+"\n")
		pass
	elif test["used"] == False:
		print("\033[31mDIE\033[0m : "+email)
		logdie.write(email+"\n")
		pass