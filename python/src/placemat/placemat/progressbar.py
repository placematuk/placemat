'''
function progress(numerator, denominator)
	You can call this function at any point in your code to print a progress bar to stdout. Subsequent calls will update the progress bar as long as nothing else has been output in between calls. The progress bar will automatically terminate when it is called with numerator=denominator. However, if you need to finish early, just call the finish() function.

function finish()
	If a progress bar is currently running, then terminate it, regardless of the progress.
'''

import subprocess


# This class gives the progressbar module a little bit of self awareness.
# By initialising it on import, the module can automatically manage carriage
# returns without having to be explicitly told to start and finish.
class ProgressBarManager():

	def __init__(self):
		# Initialise variables
		self.running = False

	def start(self):
		# If we're not already running a progress bar,
		# print to a new line and don't print the final
		# new line.
		if not self.running:
			print '',
		self.running = True

	def progress(self, numerator, denominator):
		self.running = True

		# How wide is the display?
		columns = int(subprocess.check_output(['stty', 'size']).split()[1])
		
		percentage = float(numerator) / float(denominator)

		# Prepare a message to print. By starting with a carriage return, this message
		# replaces the current line instead of appending to it.
		message = "\r{}/{} {}% [".format(numerator, denominator, int(percentage*100))

		# Work out the numbers for printing the progress bar
		length = columns - len(message) - 1
		filled = int(length * percentage)
		unfilled = length - filled
		
		# Add the progress bar on to the message
		message += "=" * (filled-1)
		message += ">"
		message += " " * (unfilled)
		message += "]"

		# Print the progress bar. Note we're not printing the new line character.
		# This will be done by the finish() function.
		print message,

	def finish(self):
		# If the progress bar is currently running, print a new line character
		if self.running:
			print ''
			self.running = False


def progress(numerator, denominator):
	'''Update the progress bar with progress numerator/denominator'''
	if not manager.running:
		manager.start()
	manager.progress(numerator, denominator)
	if numerator >= denominator:
		manager.finish()

def finish():
	'''Terminate the progress bar early'''
	manager.finish()

manager = ProgressBarManager()
