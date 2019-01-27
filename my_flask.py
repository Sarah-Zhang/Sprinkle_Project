from flask import Flask, request
import os
import sys
from proc_json import parser

app = Flask(__name__)

@app.route('/')
def browser_interface():    
    return '<h1>Don\'t access from the browser interface.</h1>'


@app.route('/', methods=['POST']) 
def save_elements():
    global prefix
    global target_dir

    receive = str(request.json).replace("'",'"').replace('\n','')

    proced = parser(request.json)
    
    with open(target_dir + '/Raw.txt', 'a') as f:
        f.write(receive + '\n')
    
    if proced is not None:
        with open(target_dir + '/proc.txt', 'a') as f:
            f.write(str(proced[0]) + " " + str(proced[1]) + "\n")    
    
    return 'Got it!'


if __name__ == '__main__':
    global prefix
    global target_dir
    
    print('Flask init')

    try:
        prefix = sys.argv[1]
    except:
        prefix = 'alpha'
    
    target_dir = '/srv/runme/' + prefix
#    target_dir = '/Users/chenxi.ge/Desktop/Sprinkle/' + prefix
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        
    with open(target_dir+ '/Raw.txt', 'w'): pass
    with open(target_dir + '/proc.txt', 'w'): pass


    try:
    	# this is one way
#        os.system('echo "* * * * * python /Users/chenxi.ge/Desktop/Sprinkle/auto_tasks.py ' + prefix + '" > task.txt')
        os.system('echo "*/2 * * * * python ~/Sprinkle/auto_tasks.py ' + prefix + '" > task.txt')
        os.system('crontab task.txt')
        os.system('rm task.txt')
        print 'Crontab set' 

    except:
        print 'Failed setting up crontab'
        sys.exit()

    
    app.run(host='0.0.0.0', port=8080)
