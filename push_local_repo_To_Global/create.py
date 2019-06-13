import requests
import json
import subprocess
import os.path
import sys

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

req_body = {
  "name": repo,
  "description": "Repo created using script. < Change >",
  "private":"false"
}

r = requests.post(url = endpoint ,json = req_body)
r.json()

# Decode UTF-8 bytes to Unicode, and convert single quotes to double quotes to make it valid JSON
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

	# Creating an .gitignore file to ignore these script files
	if os.path.exists(".gitignore"):
		f = open(".gitignore","a")
		f.write("\n")
	else:
		f=open(".gitignore","w")
	f.write("# Script files to create and upload repo\n")
	f.write("create.py\n")
	f.close()

	# Checking if the folder is initialized with git or not
	if not os.path.exists(".git"):
		subprocess.call("git init")
	# Git commands to commit and push all files
	subprocess.call("git add .")
	subprocess.call('git commit -m "Initial commit"')
	cmd = "git remote add origin "+origin
	subprocess.call(cmd)
	subprocess.call("git push -u origin master")

	print("Successfully created and pushed at: "+data['clone_url'])
