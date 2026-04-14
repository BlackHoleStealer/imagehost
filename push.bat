@echo off
cd /d %~dp0

echo Adding files...
git add .

echo Committing...
git commit -m "update"

echo Pushing...
git push

echo Done.
pause