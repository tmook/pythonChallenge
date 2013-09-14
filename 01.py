from string import maketrans

# k->m = 107->109
# o->q = 111->113
# e->g = 101->103

#rot2
#inputString = 'abc koe wxyz'
inputString = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
rot2String = ''

#for e in inputString:
#   temp = ord(e)
#   if temp >= 97 and temp <= 122:
#      temp += 2
#   if temp > 122 and temp < 125:
#      temp = 96 + (temp-122)
#   rot2String += chr(temp)

fromString = 'abcdefghijklmnopqrstuvwxyz'
toString = 'cdefghijklmnopqrstuvwxyzab'
trans = maketrans(fromString,toString)
print inputString.translate(trans)


print rot2String


# ocr.html
