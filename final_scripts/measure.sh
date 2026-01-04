#!/bin/bash
echo "Welcome to glare measuring program"

cd /home/hosovluc/measurements

# create a directory with date and time. The $dir variable is also used for filenames
dir=`date +"%Y%m%d_%H%M"`
mkdir $dir
cd $dir

echo "Press M for one-time measurement"
read -n 1 key  # waits for a single key press
echo "You pressed: $key"

echo ""  # newline after key press

if [[ $key == "m" || $key == "M" ]]; then
	echo "You selected one-time measurement"
	# 1 - CAPTURE
	python3 "/home/hosovluc/Documents/GLAREMETER/Scripts/Capture_RAW_bracket.py"
	# 2 - HDR GEN
	python3 "/home/hosovluc/Documents/GLAREMETER/Scripts/auto_hdrgen.py" 
		
else
    echo "Invalid key pressed"
fi

echo "End"
