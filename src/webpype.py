import json
import urllib2

class WebPype(object):

    def __init__(self):
        pass

    def options(self, url):
        request = urllib2.Request(url)
        request.get_method = lambda: 'OPTIONS'
        resp = urllib2.urlopen(request)
        return resp.read()

    def print_options(self, url):
        resp = self.options(url)
        print resp
        return

    def execute(self, url, inputs):
        data = json.dumps({'inputs': [inputs]})
        request = urllib2.Request(url, data, {'Content-Type': 'application/json'})
        resp = urllib2.urlopen(request)
        return resp.read()
