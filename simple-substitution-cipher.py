# -*- coding: utf-8 -*-
print "Simple substitution cipher"
print u"単一換字式暗号"
#sample
Cipher = "PXFR}QIVTMSZCNDKUWAGJB{LHYEO" #暗号文字列
Plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ{}" #平文
#exec
q="A}FFDNEVPFSGV}KZPN}GO" #問題文

a=""
for char in q:
    a+=Plain[Cipher.index(char)]
print a