import os
import sys
import datetime

def auto_tasks():

    prefix = sys.argv[1]

    # rename part
    ts = str(datetime.datetime.now())[:-7]
    
    target_dir = '/srv/runme/' + prefix
#    target_dir = '/Users/chenxi.ge/Desktop/project_Sprint/' + prefix

    os.rename(target_dir + '/Raw.txt',
              target_dir + '/Raw_' + ts + '.txt')

    os.rename(target_dir + '/proc.txt',
              target_dir + '/proc_' + ts + '.txt')
    
    with open(target_dir + '/Raw.txt', 'w'): pass
    with open(target_dir + '/proc.txt', 'w'): pass

 
if __name__ == '__main__':
    auto_tasks()