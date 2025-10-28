@echo off
echo Adding all changes...
git config set advice.useCoreFSMonitorConfig false
git config --global --add safe.directory .
rem rm .git/index.lock
git saveme
echo Done!
exit