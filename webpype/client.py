'''
This file contains the functionality for the using of webpipes.
'''
from __future__ import print_function
import json
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

from exceptions import TypeError

class WebPypeBaseClient(object):
    '''
    Base class for implementing the client aspects of the spec. Inherit from
    or use this class for a more fundamental 'WebPipe' client.

    '''

    def _request(self, url, method=None):
        request = Request(url)
        if method:
            if isinstance(method, str):
                request.get_method = lambda: method
        resp = urlopen(request)
        return resp.read()

    def options(self, url):
        return self._request(url, method='OPTIONS')

    def execute(self, url, inputs):
        if not isinstance(inputs, dict) and not isinstance(inputs, str):
            raise TypeError('Your input value must be a dictionary or string. Got: %s' % inputs)
        if isinstance(inputs, dict):
            data = json.dumps({'inputs': [inputs]})
        if isinstance(inputs, str):
            data = "{'inputs' : [%s]}" % inputs

        request = Request(url, data, headers={'Content-Type': 'application/json'})
        resp = urlopen(request)
        return resp.read()


class WebPypeClient(WebPypeBaseClient):
    '''
    A class for interacting with webpipes that is a bit more full featured.

    '''

    def print_options(self, url):
        resp = self.options(url)
        return print(resp)

    def execute_from_file(self, url, file_var):
        '''
        Identical to WebPypeClient.execute(), except this function accepts a
        file path or file type instead of a dictionary.

        '''
        if isinstance(file_var, file):
            f = file_var
        elif isinstance(file_var, str):
            try:
                f = open(file_var)
            except IOError, e:
                raise e
        else:
            raise TypeError("This function only accepts a 'file' type  or file path")

        inputs = f.read()
        resp = self.execute(url, inputs)
        return resp

    def execute_from_url(self, url, input_url):
        '''
        Identical to WebPypeClient.execute(), except this function accepts a
        url instead of a dictionary or string.

        '''
        inputs = self._request(input_url)
        resp = self.execute(url, inputs)
        return resp
