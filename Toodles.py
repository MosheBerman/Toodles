import os
import keyword
import sys


class Toodles:
	
	def walkAndList(self, directory):
		for dirname, dirnames, filenames in os.walk(directory):

			# print path to all filenames.
			for filename in filenames:
				workingFilename = os.path.join(dirname, filename)
				if(self.isSourceFile(filename)):
					self.listOccurrencesOfToDoInFile(filename)
		
			# Advanced usage:
			# editing the 'dirnames' list will stop os.walk() from recursing into there.
			if '.git' in dirnames:
				# don't go into any .git directories.
				dirnames.remove('.git')
				
			for dirs in dirnames:
				self.walkAndList(os.path.join(dirname, dirs))


	# 	Find occurences of "todo" and "fixme" in a file
	#	If we find such an occurence, print the filename, 
	#	the line number, and the line itself.
	def listOccurrencesOfToDoInFile(self, aFileName):
		input = open(aFileName)
		currentLine = 1
		for line in input:
			line = line.lower()
			currentLine = currentLine + 1
			needle = "todo"
			if (needle in line):
				print(aFileName + " (" + str(currentLine) + ")" + line)
			
	#Todo: add a comment
	def isSourceFile(self, name):
		fileName, fileExtension = os.path.splitext(name)
		if (".m" in fileExtension or ".c" in fileExtension or ".h" in fileExtension):
			return True
		return False


if __name__ == "__main__":
	a = Toodles()
	a.walkAndList(".")

