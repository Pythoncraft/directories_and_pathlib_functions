from pathlib import Path
path = Path() 
# print(path.exists()) returns true/false if directory exists
# path.mkdir() will create a directory in Path('')
# path.rmdir() #will remove directory if exists
# path.glob('*.py') # .glob function grabs all the specified file types in a directory
for files in path.glob('*.py'):
	print(files)