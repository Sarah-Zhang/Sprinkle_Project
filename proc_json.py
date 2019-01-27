import datetime

def parser_file(prefix):
    # files = ['/srv/runme/' + prefix + '/Raw.txt']
    files = ['/Users/chenxi.ge/Desktop/project_Sprint/' + prefix + '/Raw.txt']
    output = []
    
    # check all files under the folder
    for file in files:
        with open(file) as json_data:  # give full path of the file since we are in home directory...?
            # Go over each line in json
            for line in json_data:
                # Check if each line is in proper json format
                parsed = parser(line)
                if parsed:
                    output.append(parsed)

    #File output
    # with open('/srv/runme/' + prefix + '/proc_' + str(datetime.datetime.now()) + '.txt', 'w') as f:
    with open('/Users/chenxi.ge/Desktop/project_Sprint/' + prefix + '/proc_' + str(datetime.datetime.now()) + '.txt', 'w') as f:
         for i in range(len(output)):
                f.write(str(output[i][0]) + " " + str(output[i][1]) + "\n")
                
 

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input
               
    
def parser(line):
    json_line = byteify(line)
    try:
        # Get rid of empty lines and filter out the target entries with empty string:
        if (bool(json_line)) and (json_line['name'] != '') and (json_line['prop']['age'] >= 0) and (json_line['prop']['age'] != '') and (type(json_line['prop']['age'])!= str):
            return (json_line['name'],json_line['prop']['age'])
        else:
           return None
    except:
        return None

                