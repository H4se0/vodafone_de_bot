#!/usr/bin/env python

import sys, time
from daemon import daemon
from urllib.request import urlopen, Request
import subprocess, platform
import json
import requests

# first we need to ping network to get connection status
def checkNet():
    try:
        subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower()=="windows" else 'c', "google.com"), shell=True)
        return "connected"
    except Exception:
        return "disconnected"


# here we download our stamp data from the server.
def get_session():
    url = "https://hotspot.vodafone.de/api/v4/session"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    rs = urlopen(req)
    raw_data = rs.read()
    result = json.loads(raw_data.decode('utf8'))
    session = result['session']
    return session

def connect():
    purl = "https://hotspot.vodafone.de/api/v4/login"
    data = {"loginProfile": 2, "session": get_session(), "accessType": "termsOnly"}
    requests.post(purl, data, headers={'User-Agent': 'Mozilla/5.0'})

# loop which keeps this script alive
class MyDaemon(daemon):
    def run(self):
        while True:
            try:
                if checkNet() == 'connected':
                    time.sleep(10)

                elif checkNet() == 'disconnected':
                    connect()
                    time.sleep(600)

                else:
                    print('error')

            except Exception:
                sys.exit(1)

# magic which allows to run script as standalone daemon.
if __name__ == "__main__":
    daemon = MyDaemon('/var/tmp/vodafone.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)