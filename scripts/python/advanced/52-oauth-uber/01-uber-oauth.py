#Step 1: User authorizes your app
# https://login.uber.com/oauth/v2/authorize?client_id=<YOUR_CLIENT_ID>&response_type=code&redirect_uri=<YOUR_REDIRECT_URI>

#s1_login_url = "https://login.uber.com/oauth/v2/authorize?client_id=<YOUR_CLIENT_ID>&response_type=code&redirect_uri=<YOUR_REDIRECT_URI>"

# AUTHORIZATION_CODE
# bFyFa1xpFdkCNQzqUFPwIHThglidXe#_


import http.client
import urllib.parse


def send_http_request(url):
	scheme, server, path, query, fragment = urllib.parse.urlsplit(url)

	print("scheme :", scheme)
	print("server :", server)
	print("path   :", path)
	print("query  :", query)
	print("fragment :", fragment)
    
	if scheme == 'http':
		ConnClass = http.client.HTTPConnection
	elif scheme == 'https':
		ConnClass = http.client.HTTPSConnection
	else:
		print('scheme error')

	conn = ConnClass(server)
	try:
		conn.request('GET', path, headers={'Host': server})
		response = conn.getresponse()

		'''
		print ("resp, status :", response.status)
		print ("resp  reason :", response.reason)
		print (10 * "*")
		print ("msg          :")
		print (response.msg)
		print (10 * "*")
		'''

		if response.status != 200:
			print("error in status")

		data = response.read()

		return (response, response.status, data)

	finally:
		conn.close()

Client_ID = "qWrCuXWBnZ46gve_Aj-yLBd_WZMQbJZE"
redirect_uri = "http://127.0.0.1"
auth_code = "bFyFa1xpFdkCNQzqUFPwIHThglidXe#_"

def step_1_authorize(s1_login_format, Client_ID, redirect_uri):
	url = s1_login_format % (Client_ID, redirect_uri)
	print (url)

	(response, retcode, data) = send_http_request(url)
	print("retcode      :", retcode)
	print("resp, status :", response.status)
	print("resp  reason :", response.reason)
	print (response.msg)
	url = response.getheader('Location')
	print("1. Location  :", url)

	scheme, server, path, query, fragment = urllib.parse.urlsplit(url)
	print("scheme :", scheme)
	print("server :", server)
	print("path   :", path)
	print("query  :", query)
	print("fragment :", fragment)
	url = query.lstrip("next_url=")
	url = urllib.parse.unquote(url)
	print ("url :", url)

	url =  url + "/?code=%s" % auth_code

	print ("url :", url)
	print (10 * "*")

	(response, retcode, data) = send_http_request(url)
	print("retcode      :", retcode)
	print("resp, status :", response.status)
	print("resp  reason :", response.reason)
	print (response.msg)

	print (10 * "*")

	url = response.getheader('Location')
	(response, retcode, data) = send_http_request(url)
	print("retcode      :", retcode)
	print("resp, status :", response.status)
	print("resp  reason :", response.reason)
	print (response.msg)
	print (10 * "*")

	url = query.lstrip("next_url=")
	url = urllib.parse.unquote(url)
	print ("url :", url)

def main():
	s1_login_format = "https://login.uber.com/oauth/v2/authorize?client_id=%s&response_type=code&redirect_uri=%s"
	step_1_authorize(s1_login_format, Client_ID, redirect_uri)

if (__name__ == "__main__"):
	main()
