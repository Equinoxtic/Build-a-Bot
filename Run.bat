@echo off
echo Loading...
PING localhost -n 5 >NUL
echo Wait for a few more seconds...
PING localhost -n 5 >NUL
echo Almost there...
PING localhost -n 5 >NUL
echo All done!
python -u main.py