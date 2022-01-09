#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""
if __name__ == '__main__':
    import urllib.request as request
    url =  request.get('https://intranet.hbtn.io/status')
    text = url.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))