# -*- coding: utf-8 -*-
print "Caesar cipher"
print u"シーザー暗号"
#val
ROT = 13 
#exec
import codecs
q="synt_fxlnepu_argjbexf_ebg13" #問題文

ans=""
for x in q:
    if x.isalpha():
        ans += chr((ord(x) - ord("a") + ROT) % 26 + ord("a"))
    else:
        ans += x
 
print ans
