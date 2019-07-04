import json
import os
import time
import datetime

def calculateDate(start, end):
    startSec = time.mktime(time.strptime(start, '%Y-%m-%d'))
    endSec = time.mktime(time.strptime(end, '%Y-%m-%d'))
    days = int((endSec - startSec)/(24*60*60))
    return days

def commit(flag):
    if flag:
        for n in xrange(49):
            with open('./record.txt','a') as record:
                record.write('.')
                record.close()
                os.system('\"HeartBeat\"')
    else:
        with open('./record.txt', 'a') as record:
            record.write('.')
            record.close()
            os.system('git commit -a -m \"HeartBeat\"')
    os.system('git pull && git push origin master')
with open('../model.json') as f:
    PATTEN = json.loads(f.read())
    f.close()
PERIOD = len(PATTEN[0])
START_DATE = '2018-7-01'
now = datetime.datetime.now().strftime('%Y-%m-%d')
row = calculateDate(START_DATE, now) % 7
col = int(calculateDate(START_DATE, now)/7) % PERIOD
commit(PATTEN[row][col])
