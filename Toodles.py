	import os
	import keyword
	import sys


	class Toodles:
		
		def walkAndList(self, directory):
			for dirname, dirnames, filenames in os.walk(directory):

				# print path to all filenames.
				for filename in filenames:
					workingFilename = os.path.join(dirname, filename)
					if(self.isSourceFile(filename) and self.isNYTFile(filename)):
						self.listOccurrencesOfToDoInFile(workingFilename)
			
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
					directory, filename = os.path.split(aFileName)
					print(filename + " (" + str(currentLine) + ")" + line)
				
		#	Returns true if the file is a
		#	valid source file - .m, .h, 
		#	or .c
		def isSourceFile(self, name):
			fileName, fileExtension = os.path.splitext(name)
			if (".m" in fileExtension or ".c" in fileExtension or ".h" in fileExtension):
				return True
			return False
			
		#	Return True if the file is an NYT file
		def isNYTFile(self, file):
			return "NYT" in file

	if __name__ == "__main__":
		a = Toodles()
		a.walkAndList(".")

