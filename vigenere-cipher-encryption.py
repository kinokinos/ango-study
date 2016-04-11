# -*- coding: utf-8 -*-
print "Vigenere cipher"
print u"ヴィジュネル暗号"
#鍵
key="CTF"
#暗号文
q="XBLGGJTX HKIMGK NU ITNRLTTUJBH UNGUMNVNYKHS EBUJXW" 
#exec
#注意　caution
#TODO:大文字+大文字，小文字+小文字だと結果に違いがでる．
#R+F:152,r+f:216
def encryption(plain,key):
    cipher=""
    cont=0
    for x in plain.upper():
        if x.isalpha():
            k=key[cont%len(key)].upper()
            cipher += chr( (ord(x)+ord(k))%26 + ord("a") )
            cont+=1
        else:
            cipher += x
    return cipher
    
def decryption(cipher,key):    
    cipher=cipher.lower()
    key=key.lower()
    ans=""
    cont=0
    for x in cipher:
        if x.isalpha():
            ans += chr((ord(x)-ord(key[cont%len(key)]) +26) % 26 + ord("a"))
            cont+=1
        else:
            ans += x
    return ans
print decryption(q,key)
print encryption(decryption(q,key),key)
