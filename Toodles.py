import os
import keyword
import sys

def walkAndList():
	for dirname, dirnames, filenames in os.walk('.'):
	    # print path to all subdirectories first.
	    for subdirname in dirnames:
	        print os.path.join(dirname, subdirname)

	    # print path to all filenames.
	    for filename in filenames:
	        workingFilename = os.path.join(dirname, filename)
            if(isSourceFile(workingFilename)):
		        listOccurrencesOfToDoInFile(workingFilename)

	    # Advanced usage:
	    # editing the 'dirnames' list will stop os.walk() from recursing into there.
	    if '.git' in dirnames:
	        # don't go into any .git directories.
	        dirnames.remove('.git')
	
# 	Find occurences of "todo" and "fixme" in a file
#	If we find such an occurence, print the filename, 
#	the line number, and the line itself.
def listOccurrencesOfToDoInFile(file):
	input = open(file)
	currentLine = 1;
	for line in input:
		line = line.lower()
		currentLine = currentLine + 1
		needle = "todo"
		if (needle in line):
			sys.stdout.write(file + " (" + str(currentLine) + ")" + line)
			
#Todo: add a comment
def isSourceFile(name):
	fileName, fileExtension = os.path.splitext(name)
	if (".m" in fileExtension or ".c" in fileExtension or ".h" in fileExtension):
		return True
	return False
	
walkAndList()