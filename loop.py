import json
import os
import time
import datetime

def calculateDate(start, end):
    startSec = time.mktime(time.strptime(start, '%Y-%m-%d'))
    endSec = time.mktime(time.strptime(end, '%Y-%m-%d'))
    days = int((endSec - startSec)/(24*60*60))
    return days

def addDays(d, num):
    sec = num * 24 * 60 * 60
    nowSec = time.mktime(time.strptime(d, '%Y-%m-%d')) + sec
    return time.strftime("%Y-%m-%d", time.localtime(nowSec))

def commit(flag):
    if flag:
        for n in xrange(49):
            with open('./record.txt','a') as record:
                record.write('.')
                record.close()
                os.system('git commit -a -m \"HeartBeat\"')
        with open('./record.txt', 'a') as record:
            record.write('\n')
            record.close()
            os.system('git commit -a -m \"HeartBeat\"')
    else:
        with open('./record.txt', 'a') as record:
            record.write(now + '\n')
            record.close()
            os.system('git commit -a -m \"HeartBeat\"')

with open('../model.json') as f:
    PATTEN = json.loads(f.read())
    f.close()
PERIOD = len(PATTEN[0])
START_DATE = '2018-7-01'
now = datetime.datetime.now().strftime('%Y-%m-%d')

os.system('timedatectl set-ntp false')

while calculateDate(START_DATE, now) >= 0:
    row = calculateDate(START_DATE, now) % 7
    col = int(calculateDate(START_DATE, now)/7) % PERIOD
    commit(PATTEN[row][col])

    now = addDays(now, -1)
    os.system('timedatectl set-time ' + now)

os.system('timedatectl set-ntp 1 && timedatectl set-local-rtc 1')