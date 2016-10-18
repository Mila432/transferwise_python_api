import requests
import json

base='https://transferwise.com/api/v1/'

head={'User-Agent':'TransferWise/7925 (iPad; iOS 9.3.3; Scale/2.00)',
'X-Authorization-key':'pfwk97car71rtatr1656zqyatd343dsq'}

s=requests.session()
s.verify=False
s.headers.update(head)
proxies = {
	'http': 'http://127.0.0.1:8888',
	'https': 'http://127.0.0.1:8888',
}
s.proxies.update(proxies)

def login(user,pasw):
	print '[!] trying login'
	data={'lifeTime':'two_months',
		'login':user,
		'password':pasw}
	r=s.post(base+'token/create',data=data)
	return r.content
	
def main():
	data= login('mai1l@mail.com','password')
	if 'CRD_NOT_VALID' in data:
		print '[-] login invalid'
	elif 'USER_DEACTIVATED' in data:
		print '[-] account blocked'
	else:
		print '[+] login working'
		
if __name__ == '__main__':
	main()