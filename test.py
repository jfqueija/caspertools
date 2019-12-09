#! usr/bin/python
# -*- coding: utf-8 *-* 

import argparse 
from caspertools.hiddenav import TorIp

parser = argparse.ArgumentParser(description='DNS Information')
parser.add_argument('-ps','--password',help='Tor password')
parser.add_argument('-pt','--port',help='Tor Port. Sample: 9051')
parser.add_argument('-lp','--proxy',help='Local proxy. Sample: 127.0.0.1:8118')
parser.add_argument('-u','--url',help='Url for test library.')
parser = parser.parse_args()

def main():
    if parser.password:
        if parser.port:
            if parser.proxy:
                if  parser.url:
                    testTorIp(parser.password,parser.port,parser.proxy,parser.url)
                else:
                    print('Url test is required. Please, look help with parameter -h')
            else:
                print('Local Proxy is required. Please, look help with parameter -h')
        else:
            print('Tor port is required. Please, look help with parameter -h')
    else:
        print('Tor password is required. Please, look help with parameter -h')

def testTorIp(password,port,proxy,urlTest):    
    tor = TorIp(password,port,proxy)
    print(tor.renew_ip())
    print(tor.request_get(urlTest).text)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
    