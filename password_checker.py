import requests 
import hashlib 

def api_get_request_connection(query):
	url = "https://api.pwnedpasswords.com/range/" + query 
	res = requests.get(url) 
	if res.status_code != 200: 
		raise RuntimeError(f'this seems to be a bad gateway with the webpage, {res.status_code}, so please try again.') 
	return res 

def check_password_hash_api(password):
	sha1password=hashlib.sha1(password.encode('utf-8')).hexdigest().upper() 
	head,tail = sha1password[:5],sha1password[:5]
	print(head,tail) 
	response=api_get_request_connection(head) 
	print(response) 
	return response


check_password_hash_api("password123")