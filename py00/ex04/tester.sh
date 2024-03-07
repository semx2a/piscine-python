#!/bin/bash

SEP="____________________________________"
RESET=$(tput sgr0)
BOLD=$(tput bold)

function test
{
	echo $BOLD
	echo "testing $1"
	echo -n -e "Result: $RESET"
	python whatis.py $1
	if [ -z "$1" ] 
	then
		echo -e 
	fi
	echo -e $SEP
}

test "14"
test "-5"
test "0"
test ""
test "Hi!"
test "13 5"