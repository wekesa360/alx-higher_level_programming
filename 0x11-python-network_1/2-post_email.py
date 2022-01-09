#!/usr/bin/python3
""" 
takes in a URL and an email, sends 
a POST request to the passed URL with the email as
a parameter, and displays the body of the response (decoded in utf-8)
"""
if __name__ == '__main__':
    from sys import argv
    import urllib.parse as parse
    import urllib.request as request
    data = {'email': argv[2]}
    data = parse.urlencode(data).encode('utf8')
    binded_url = request.Request(argv[1], data)
    with request.urlopen(binded_url) as r:
        print(r.read().decode('utf8'))

