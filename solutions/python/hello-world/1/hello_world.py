#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=''):
	if name == '' or name == None:
		return 'Hello, World!'
	else:
		return 'Hello, ' + name + '!'