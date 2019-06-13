#python script for automating the whole process of project creation.

#This script creates a repository in github with provided name, using github API.
import json
import requests
import platform
import sys
import os

OS = platform.system()

if len(sys.argv) == 3:
	repo = sys.argv[1]
	token = sys.argv[2]
elif len(sys.argv) == 2:
	repo = sys.argv[1]
	token = input("Enter PAT (Personal Access Token) ")
else:
	repo = input("Enter repository name ")
	token = input("Enter PAT (Personal Access Token) ")

endpoint = "https://api.github.com/user/repos?access_token="+token

#Making API call for creation of repository and making the initial commit.

req_body = '{"name":"'+repo+'","description": "Repo created using script. < Change >","private":false}'

req_body = json.loads(req_body)
r = requests.post(url = endpoint ,json = req_body)
r.json()

# Decode UTF-8 bytes to Unicode, and convert single quotes
# to double quotes to make it valid JSON
my_json = r.content.decode('utf8').replace("'", '"')

# Load the JSON to a Python list & dump it back out as formatted JSON
data = json.loads(my_json)

# Display errors if found any
if 'documentation_url' in data:
	if('errors' in data):
		print(data['errors'][0]['message'])
	else:
		print(data['message'])
else:
	# Creating the origin url with PAT
	origin = "https://"+data['owner']['login']+":"+token+"@github.com/"+data['full_name']+".git"
	if (OS == 'Darwin' or OS == 'Linux'):
		os.system("chmod u+x ./new_file.sh")
		cmd = "./new_file.sh "+ repo + " " + origin
	else:
		cmd = "new_file.bat "+ repo + " " + origin


	os.system(cmd)

print("="*40)
print("Successfully created the project")
