# -*- coding: utf-8 -*-
print "Vigenere cipher"
print u"ヴィジュネル暗号"
#鍵
key="CTF"
#暗号文
q="XBLGGJTX HKIMGK NU ITNRLTTUJBH UNGUMNVNYKHS EBUJXW" 
#exec
def decryption(cipher,key):    
    ans=""
    cont=0
    for x in cipher:
        if x.isalpha():
            ans += chr((ord(x)-ord(key[(cont)%len(key)]) +26) % 26 + ord("a"))
            cont+=1
        else:
            ans += x
    return ans
print decryption(q,key)