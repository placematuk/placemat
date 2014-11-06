import subprocess

def start():
	print '',

def progress(numerator, denominator):
	columns = int(subprocess.check_output(['stty', 'size']).split()[1])
	percentage = float(numerator) / float(denominator)

	message = "\r{}/{} {}% [".format(numerator, denominator, int(percentage*100))

	length = columns - len(message) - 1
	filled = int(length * percentage)
	unfilled = length - filled
	
	message += "=" * (filled-1)
	message += ">"
	message += " " * (unfilled)
	message += "]"

	print message,

def complete():
	print ''
