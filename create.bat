@echo off 

if [%1]==[] (set /p repo="Enter repository name: ") else (set repo=%1)
if [%2]==[] (set /p username="Enter username name: ") else (set username=%2)
if [%3]==[] (set /p pat="Enter PAT (Personal Access Token): ") else (set pat=%3)

set endpoint="https://api.github.com/user/repos?access_token=%pat%"

rem Making an curl request
curl -i -d "{\"name\": \"%repo%\", \"private\": false}" %endpoint%

rem Creating an .gitignore file to ignore these script files
echo create.bat>>.gitignore

rem Git commands to commit and push all files
git init
git add .
git commit -m "Initial commit"
git remote add origin "https://%username%:%pat%@github.com/%username%/%repo%.git"
git push -u origin master
