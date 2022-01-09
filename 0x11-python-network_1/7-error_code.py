#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body of the response.
"""
if __name__ == '__main__':
    import urllib.request as request
    from sys import argv
    r = request.get(argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)