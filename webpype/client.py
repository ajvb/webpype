'''
This file contains the functionality for the using of webpipes.
'''
import json
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

class WebPypeClient(object):

    def options(self, url):
        request = Request(url)
        request.get_method = lambda: 'OPTIONS'
        resp = urlopen(request)
        return resp.read()

    def execute(self, url, inputs):
        data = json.dumps({'inputs': [inputs]})
        request = Request(url, data, {'Content-Type': 'application/json'})
        resp = urlopen(request)
        return resp.read()
