import re

digit_re = re.compile(r'[0-9]+')

i = 90052

for x in range(0,910):
   with open(str(i)+'.txt') as nnFile:
      content = nnFile.read()
      print content
      i = digit_re.search(content).group(0)

#46145
