#! usr/bin/python
# -*- coding: utf-8 *-* 

import requests

from stem import Signal
from stem.control import Controller

class TorIp(object):
    def __init__(self,tor_password,tor_port,local_http_proxy):
        self._tor_password = tor_password
        self._tor_port = tor_port
        self._local_http_proxy = local_http_proxy

    def get_tor_port(self):
        return self._tor_port
    
    def get_tor_password(self):
        return self._tor_password
    
    def get_local_http_proxy(self):
        return self._local_http_proxy

    '''Function used for test if ip is changed.'''
    def renew_ip(self):
        try:
            with Controller.from_port(port=int(self.get_tor_port())) as controller:
                controller.authenticate(password= self.get_tor_password())
                controller.signal(Signal.NEWNYM)
            return requests.get('http://icanhazip.com/', proxies={'http': self.get_local_http_proxy()}).text.strip()
        except Exception as ex:
            return 'Failed renew Ip: %s'%str(ex)
    
    '''Function used for navigate to url with proxy. Not with our original IP'''
    def request(self,url):
        try:
            with Controller.from_port(port=int(self.get_tor_port())) as controller:
                controller.authenticate(password= self.get_tor_password())
                controller.signal(Signal.NEWNYM)
            return requests.get(url, proxies={'http': self.get_local_http_proxy()})
        except Exception as ex:
            return 'Failed call url %s with error: '%(url,str(ex))