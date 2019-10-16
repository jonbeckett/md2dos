# Script         : md2dos
# Author         : Jonathan Beckett
# Compatibility  : Python 3.x
# Pre-Requisites : None


# path where markdown files reside
root_path = "c:\\temp\\blog"

# Import modules
import os
import os.path

i=0

post_file = open("c:\\temp\\blog.dos\index.txt", "w")

for subdir, dirs, files in os.walk(root_path):
	for file in sorted(files):
		if '.txt' in file and 'README.md' not in file:

			print("Processing " + file)

			i = i + 1
			
			file = file.replace( u'\U0001f499', '')
			file = file.replace( u'\U0001f49a', '')
			file = file.replace( u'\U0001f49b', '')
			file = file.replace( u'\U0001f49c', '')
			file = file.replace( u'\U0001f633', '')
			file = file.replace( u'\u2018', u'\'')
			file = file.replace( u'\u2019', u'\'')
			file = file.replace( u'\u201c', u'\'')
			file = file.replace( u'\u201d', u'\'')
			file = file.replace( u'\u2013', '-')
			file = file.replace( u'\u2026', '...')
			file = file.replace( u'\u2033', '\'')
			file = file.replace( u'\u2032', '\'')
			file = file.replace( u'\xd7', 'x')
			file = file.replace( u'\xc2', ' ')
			file = file.replace( u'\u01c3','-')
			file = file.replace( u'\u01f6','e')
			
			post_file.write(f'{i:04}' + " " + file + "\n")
			
			
print(str(i) + " files processed")
post_file.close()