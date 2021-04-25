#!/usr/bin/env python

import sys, time
from daemon import daemon
import urllib.request
from urllib.request import urlopen, Request
import os
import subprocess, platform
import json
import requests

def checkNet():
    try:
        output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower()=="windows" else 'c', "google.com"), shell=True)

    except Exception as err:
        connect()


    return True
def get_session():
    url="https://hotspot.vodafone.de/api/v4/session"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    rs = urlopen(req)
    raw_data = rs.read()
    result = json.loads(raw_data.decode('utf8'))
    session = result['session']
    return session
def connect():
    purl = "https://hotspot.vodafone.de/api/v4/login"
    data = {"loginProfile":2,"session":get_session(),"accessType":"termsOnly"}
    post = requests.post(purl, data, headers={'User-Agent': 'Mozilla/5.0'})




class MyDaemon(daemon):
        def run(self):
                while checkNet() == True:
                    time.sleep(15)
                else:
                    checkNet()
                    time.sleep(1560)

if __name__ == "__main__":
        daemon = MyDaemon('/var/run/vodafone.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
                else:
                        print ("Unknown command")
                        sys.exit(2)
                sys.exit(0)
        else:
                print ("usage: %s start|stop|restart" % sys.argv[0])
                sys.exit(2)