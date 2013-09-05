'''
The WebPype Class file. WebPype follows the spec of WebPipes ( webpipes.org )

'''
import json
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

class WebPype(object):

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
