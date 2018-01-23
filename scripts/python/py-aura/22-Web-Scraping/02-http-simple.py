#!/usr/bin/env python
import http.client
import urllib.parse


def my_http_request(url):
	"""Get the Content-Type of the given url, using a HEAD request"""
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
		print('Invalid connection type :', scheme)
	return ' '

	conn = ConnClass(server)
	try:
		conn.request('GET', path, headers={'Host': server})

		#return response.getheader('Content-Type') or ''
		response = conn.getresponse()
		return reponse
	finally:
		conn.close()

def main():
	url = "http://www.python.org/index.html"
	response = my_http_request(url)
	data = response.read()
	print(data)
	message = response.msg
	print(message)

	if (response.status != 200):
		print("Error response", response.status, response.reason)


if (__name__ == "__main__"):
	main()
