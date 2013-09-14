import re

#regular expressions
prog = re.compile(r"[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}")
nextLevelString = ''

f = open('equality.data', 'r')
for line in f:
   if prog.search(line):
      print prog.search(line).group(0)
      nextLevelString += prog.search(line).group(0)[4]
f.close()

print '\n'+nextLevelString

# linkedlist.html
