#! /bin/bash

echoerr() { echo "$@" 1>&2; }

which python3 1>&/dev/null
if [ $? -ne 0 ] 
then
	echoerr "Please install python3 to run this project\n"
exit 1
fi

python3 setup.py sdist
pip install ./dist/ft_package-0.0.1.tar.gz