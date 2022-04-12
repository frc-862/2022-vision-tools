#!/bin/sh

"""
USAGE: Run the script with ./grab_imgs.sh and provide a single word argument that corresponds with the match number.
"""

# Check to make sure input is provided in the right format; if it's in the wrong input exit
if [ -z "$1" ]
then
	echo "You didn't provide a one word match number ya dum dum"
	return
elif [ -n -z "$2" ]
then
	echo "Please provide a one word argument after the command (i.e. ./grab_logs.sh [match_num])"
	return
fi

# make directory based on user input
mkdir "$1"

scp -r lvuser@10.8.62.2:~/log/ ./$1/
