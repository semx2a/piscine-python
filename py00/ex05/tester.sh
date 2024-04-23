#!/bin/bash

SEP="____________________________________"
RESET=$(tput sgr0)
BOLD=$(tput bold)

function test
{
	echo $BOLD
	echo "testing \"$1\""
	echo -n -e "Result:\n$RESET"
	python building.py "$1"
	if [ -z "$1" ] # This checks if the length of the string is equal to 0
	then
		echo -e 
	fi
	echo -e $SEP
	sleep 1
}

test "Python 3.0, released in 2008, was a major revision that is not completely backwardcompatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
test "Hello World!"
test ""
test "123456789"
test "!@#\$%^\&\*'('')'-=,./;'['']' "
