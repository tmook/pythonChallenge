import pickle

pFile = pickle.load(open('banner.p','r'))
temp = ''
for line in pFile:
   for e in line:
      for i in range(0,e[1]):
         temp += e[0]
   print temp
   temp=''

# channel.html
