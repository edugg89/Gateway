'''
Created on 13 abr. 2017

@author: Edu
'''
import signal
import sys
import time

def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    print 'Press Ctrl+C'
    while True:
        time.sleep(1)