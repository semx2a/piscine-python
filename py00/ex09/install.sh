#! /bin/bash

echoerr() { echo "$@" 1>&2; }

which python3 &>/dev/null
if [ $? -ne 0 ] 
then
	echoerr "Please install python3 to run this project\n"
	exit 1
fi
install() {
	python3 setup.py sdist bdist_wheel
	pip install ./dist/ft_package-0.0.1.tar.gz
}

uninstall() {
	pip uninstall -y ft_package
}

case "$1" in
	install)
		install
		;;
	uninstall)
		uninstall
		;;
	*)
		echoerr "Usage: $0 {install|uninstall}"
		exit 1
		;;
esac
