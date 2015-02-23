# Assumptions: 
# If a word is not longer than column width then do not split
# If a word is longer than column width then start it on a new line and 
# write to column until complete, using as many lines as needek
# Input file is nonempty

# INPUT FILE SHOULD BE NAMED 'example.txt' AND BE IN SAME DIRECTORY
# OUTPUT SENT TO FILE 'output.txt'

import sys

# Input words is array containing all words
def wrapText(words, colwidth):
	output = ""
	curr_line_count = 0

	for word in words:
		# if a word is not longer than the column width then add to current line if
		# doing so does not make line too long
		if len(word) <= colwidth:
			if curr_line_count + len(word) + 1 > colwidth:
				output += "\n" + word
				curr_line_count = len(word)
			else:
				output += " " + word
				curr_line_count += len(word) + 1
		# if word is longer than column width then use as many lines needed to write word out,
		# beginning from a new line
		else:
			output += "\n"
			while len(word) > 0:
				if curr_line_count == colwidth:
					output += "\n"
				curr_line_count = min(colwidth, len(word))
				output += word[:curr_line_count]
				word = word[curr_line_count:]

	# removes any unnecessary new lines added at beginning
	return output.strip()


# Read input, containing column width and all words
words = []
with open('example.txt','r') as f:
    for line in f:
        for word in line.split():
           words.append(word)
colwidth = int(words.pop(0))

sys.stdout = open('output.txt', 'w')
print wrapText(words, colwidth)
