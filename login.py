import requests
import time
while True:
	r = requests.post('http://phc.prontonetworks.com/cgi-bin/authlogin',data={'userId':'16XXX0007','password':'jo bhi hoga(case sensitive)','serviceName':'prontoAuthentication','service22':'Login'})
	print(r.status_code,r.reason)
	time.sleep(10)