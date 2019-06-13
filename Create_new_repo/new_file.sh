#!/bin/sh

#Automating the whole project creation phase.

#The script is the intializing file.
#Goes to location (i.e is Documents/Projects, in my case) and creates a folder for project a initializes it in git.)

project_name=$1
remote=$2


#Intializing/Creating the project file locally.
cd
cd Documents/Projects #You can change the location of the project creation here.

mkdir $project_name
cd $project_name
echo "=============================="
echo "Project file created locally"
echo "=============================="


#intializing the project in github.

echo "Intial commit" >> README.md
git init
git add README.md
git commit -m "Initial commit"
git remote add origin $remote
git push -u origin master
