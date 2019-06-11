#python script for automating the whole process of project creation.

#This script creates a repository in github with provided name, using github API.

import requests
import platform

OS = platform.system()
script_use = ""

if(OS == 'Darwin' or 'Linux'):
    script_use = "shell"
else:
    script_use = "bat"

#Making API call for creation of repository and making the initial commit.

#url = "https://api.github.com/user/harshadokula/repos?access_token=<your token here>"
API_endpoint = "https://api.github.com/user/repos?access_token=<your token here>"
req_head={ }
req_body = {
  "name": "CreateRepo",
  "description": "Testing api" ,
  "homepage": "https://github.com",
  "private": 'true',
}
#req_payload = {'reqHeader' : '', 'reqBody' : req_body}

r = requests.post(url = API_endpoint ,json = req_body)
r.json()
print("="*40)
print(type(r.content))

import json

# Decode UTF-8 bytes to Unicode, and convert single quotes
# to double quotes to make it valid JSON
my_json = r.content.decode('utf8').replace("'", '"')
#print(my_json)
print('- ' * 20)

# Load the JSON to a Python list & dump it back out as formatted JSON
data = json.loads(my_json)
s = json.dumps(data, indent=4, sort_keys=True)
print(s)
