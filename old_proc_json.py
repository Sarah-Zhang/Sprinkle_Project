import sys
import json
import os

proc_log = []

# We add debug file to check the progress
try:
    import datetime
    proc_log.append(datetime.datetime.now())
except:
    pass

prefix = sys.argv[1]
path = '/srv/runme/'
output = []

if not os.path.isdir(path):
        os.makedirs(path)

files = [filename for filename in os.listdir(path) if filename.startswith(prefix)]
proc_log.append('\nfound ' + str(len(files)) + ' file(s)')

# check all files under the folder
for file in files:
    with open(path+file) as json_data:  # give full path of the file since we are in home directory...?
        # Go over each line in json
        for line in json_data:
            # Check if each line is in proper json format
            try:
                json_line = json.loads(line)
                # filter out wrong hierarchy - if wrong, a KeyError will be returned
                try:
                    # Get rid of empty lines and filter out the target entries with empty string:
                    if (bool(json_line)) and (json_line['name'] != '') and (json_line['prop']['age'] >= 0) and (json_line['prop']['age'] != ''):
                        output.append((json_line['name'],json_line['prop']['age']))
                    else:
                       pass
                except (KeyError):
                    pass
            except (ValueError):
                pass

proc_log.append('\nprocessed ' + str(len(output)) + ' records')

#File output
with open(path + prefix+'.txt', 'w') as f:
     for i in range(len(output)):
            f.write(str(output[i][0]) + " " + str(output[i][1]) + "\n")

proc_log.append('\nrecords saved to file')

with open('proc_log.txt', 'a') as d:
    d.write(str(proc_log)+'\n\n')
