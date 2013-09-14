parsedString = ''

f = open('ocr.data', 'r')

for line in f:
   for e in line:
      if e.isalpha():
         parsedString += e
f.close()

print parsedString


