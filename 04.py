import urllib2
import re

digit_re = re.compile(r'[0-9]+')

url_root = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
url_data = '?nothing='
#i = 12345
#i = 25357
i = 63579

#get data from  url
for x in range(0,400):
   response = urllib2.urlopen(url_root+url_data+str(i)).read()
   print response
   start= response.find('next nothing')
   nextNothing= response[start:len(response)]   
   i = digit_re.search(nextNothing).group(0)

#answer at 66831
