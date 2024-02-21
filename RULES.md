# GENERAL RULES

1. You have to render your modules from a computer in the cluster either using a
virtual machine:
	- You can choose the operating system to use for your virtual machine
	- Your virtual machine must have all the necessary software to realize your project. This software must be configured and installed.

2. Or you can use the computer directly in case the tools are available.
	- Make sure you have the space on your session to install what you need for all
	the modules (use the goinfre if your campus has it)
	- You must have everything installed before the evaluations

3. Your functions should not quit unexpectedly (segmentation fault, bus error, double
free, etc) apart from undefined behaviors. If this happens, your project will be
considered non functional and will receive a 0 during the evaluation.
4. We encourage you to create test programs for your project even though this work
won’t have to be submitted and won’t be graded. It will give you a chance
to easily test your work and your peers’ work. You will find those tests especially
useful during your defence. Indeed, during defence, you are free to use your tests
and/or the tests of the peer you are evaluating.
5. Submit your work to your assigned git repository. Only the work in the git
repository will be graded. If Deepthought is assigned to grade your work, it will be
done after your peer-evaluations. If an error happens in any section of your work
during Deepthought’s grading, the evaluation will stop.
6. You must use the Python 3.10 version
7. You can use any built-in function if it is not prohibited in the exercise.
8. Your lib imports must be explicit, for example you must "import numpy as np".
Importing "from pandas import *" is not allowed, and you will get 0 on the exercise.
9. Global variables are prohibited.
