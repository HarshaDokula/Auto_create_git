@echo offf

rem Automating the whole project creation phase.

rem The script is the intializing file.
rem Goes to location (i.e is Documents/Projects, in my case) and creates a folder for project a initializes it in git.)

set project_name=%1
set remote=%2

rem Intializing/creating the project file locally.

cd Documents/Projects

mkdir %project_name%
cd %project_name%

rem Project created locally.

rem Intializing the project in github.

echo "Intial commit" >> README.md
git init
git add README.md
git commit -m "Initial commit"
git remote add origin %remote%
git push -u origin master
