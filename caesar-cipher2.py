# -*- coding: utf-8 -*-
print "Caesar cipher"
print u"シーザー暗号"
#val
ROT = 13 
#exec
import string
q="synt_fxlnepu_argjbexf_ebg13" #問題文
t = string.maketrans(string.ascii_lowercase,
                     string.ascii_lowercase[ROT:]
                     + string.ascii_lowercase[:ROT])
print q.translate(t)
