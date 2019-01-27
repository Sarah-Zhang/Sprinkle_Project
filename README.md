# project Sprinkle

**An application that accepts and processes HTTP post requests.**  

- my_flask.py
  + start a Flask application which accepts HTTP post requests on port 8080
  + log the requests to */srv/runme/prefix/Raw.txt*
  + rotate *Raw.txt* every 2 minutes
- proc_json.py
  + parse approapriately formatted json blobs in *Raw.txt*
  + log the parse results to */srv/runme/prefix/proc.txt*
  + rotate *proc.txt* every 2 minutes
