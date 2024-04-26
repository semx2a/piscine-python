#! /bin/bash

echoerr() { echo "$@" 1>&2; }

which python3 1>&/dev/null
if [ $? -ne 0 ] 
then
	echoerr "Please install python3 to run this project\n"
exit 1
fi

pip show twine 1>&/dev/null
if [ $? -ne 0 ]
then
	python3 -m pip install twine
fi