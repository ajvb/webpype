'''
The WebPype Class file. WebPype follows the spec of WebPipes ( webpipes.org )

'''
import json
import urllib2

class WebPype(object):

    def options(self, url):
        request = urllib2.Request(url)
        request.get_method = lambda: 'OPTIONS'
        resp = urllib2.urlopen(request)
        return resp.read()

    def execute(self, url, inputs):
        data = json.dumps({'inputs': [inputs]})
        request = urllib2.Request(url, data, {'Content-Type': 'application/json'})
        resp = urllib2.urlopen(request)
        return resp.read()
