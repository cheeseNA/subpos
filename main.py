import subprocess
import re
from collections import defaultdict
from pprint import pprint

cmd = '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s'

process = (subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]).decode('utf-8')
res = process.splitlines()[1:]

airports = []

for data in res:
    splitdata = re.split('\s+', data)[1:-1]
    air = defaultdict(str)
    air['ssid'] = splitdata[0]
    air['bssid'] = splitdata[1]
    air['rssi'] = splitdata[2]
    air['channel'] = splitdata[3]
    air['ht'] = splitdata[4]
    air['cc'] = splitdata[5]
    air['security'] = ' '.join(splitdata[6:])

    airports.append(air)

pprint(airports)