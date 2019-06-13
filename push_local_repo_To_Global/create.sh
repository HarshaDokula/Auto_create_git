#!/bin/bash

# Function to retrive a particular key from JSON
function jsonValue() {
KEY=$1
num=$2
awk -F"[,:}]" '{for(i=1;i<=NF;i++){if($i~/'$KEY'\042/){print $(i+1)}}}' | tr -d '"' | sed -n ${num}p
}

if [ "$1" == "" ]; then
  echo -n "Enter repo name: "
  read repo
else
  repo=$1
fi
if ["$2" == ""]; then
  echo -n "Enter PAT (Personal Access Token): "
  read pat
else
  pat=$2
fi

# Creating the endpoint using the PAT
endpoint="https://api.github.com/user/repos?access_token=$pat"

# Making an curl request
op=`curl -d "{\"name\": \"$repo\", \"private\": false}" $endpoint`

echo $op | jsonValue message

# Creating the origin url with PAT token
origin="https://$(echo $op | jsonValue login):$pat@github.com/$(echo $op | jsonValue full_name).git"

# Creating an .gitignore file to ignore these script files
echo create.sh>>.gitignore

# Git commands to commit and push all files
git init
git add .
git commit -m "Initial commit"
git remote add origin $origin
git push -u origin master
