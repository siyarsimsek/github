# -*- coding: cp1254 -*-
#1.�RNEK
"""
+++
s1=raw_input("bir de�er giriniz")

print "s1 t�r�", type(s1)

#
#try:
#   #hata olu�acak kod / hatalar�n, denemelerin oldu�u alan.
#    s1_int = int(s1)
#    print "ba�ar�l�"
#except ValueError:
#    #try i�erisinde hata olu�tu�unda �al��acak b�l�m.
#    print "ba�ar�s�z"
#

+++
"""

#2.�RNEK

"""
def sayi_mi():
    try:
        int(s1)
        int(s2)
        return True
    except ValueError:
        return False
s1=raw_input("ilk say�")
s2=raw_input("ikinci say�")
islem=raw_input("i�lem se�, (+,-,/,*)")

/////burada say� girildikten sonra if'e gelir. if'de gelen bu say� de�erini
/////sayi_mi() fonksiyonuna g�nderir. fonksiyon gelen de�ere bakar. e�er ki
/////int'se yani fonksiyonun tan�mland��� gibi ise True de�erini al�p if'e gider.
/////e�er kurala uymazsa False de�erini al�p if'teki False'dan Else'ye ge�er.

if sayi_mi()==True:
    if islem=="+":
        print "toplam :", (int(s1)+int(s2))
    if islem=="-":
        print "fark :", (int(s1)-int(s2))
    if islem=="/":
        print "bolme :", (int(s1)/int(s2))
    if islem=="*":
        print "�arpma :", (int(s1)*int(s2))
else:
    print "s1 veya s2 sayi degil"

"""

#3.�RNEK

#parametreli parametreli fonksiyonlar

#def yaz(param1, param2,..,param3):
#    parametreleri kullanarak i�lemler yapar.

"""
def imza(ad,unvan,tel,mail,site):
    print "ad\t:",ad
    print "�nvan\t:",unvan
    print "telefon\t:",tel
    print "e-mail\t:",mail
    print "site\t:",site

imza("Sel�uk Kara","��retmen","02124536895","selcukara@gmail.com","slckr.com")
print("")
imza("Durdur","��retmen","02124536895","selcukara@gmail.com","slckr.com")
print("")
imza("Ska","��retmen","02124536895","selcukara@gmail.com","slckr.com")
"""

#Bilgisayardaki a��k ve kapal� portlar� listeleyiniz.

#4.�RNEK
"""
#soru: g�nderilen herhangi bir ifadeyi istenen t�rden olup olmad���n� kontrol eden bir fonksiyon.

def control(degisken, tur):
    try:
        #burada bir de�i�ken daha atanabilir.
        if tur=='int':
            int(degisken)
        if tur=='str':
            str(degisken)
        return True #---->Bunu yazmad���nda her seferinde al tarafta say�n�n de�i�ken old. s�yler.
    except ValueError:
        return False

#x=1
x=raw_input("de�er giriniz\t:")

if control(x,'int'):
    print "%s de�i�keni say�d�r"%(x)
else:
    print "%s de�i�keni say� de�ildir"%(x)

#http://www.pythondersleri.com/2013/05/fonksiyonlar_10.html

"""

#pythonda isimli arg�manlar(parametreler)

#5.�RNEK
"""
def imza(x,y,z,t,u):

    print "ad\t:",x         #-->x str
    print "�nvan\t:",y      #-->y str
    print "telefon\t:",z    #-->z int
    print "e-mail\t:",t     #-->t str
    print "site\t:",u       #-->u str
    
imza(y="doctor",u="msn.com",x="ece",z="02145",t="k@x.au")
"""

#6.�RNEK

x = 4
def y():
    x=12
    global isim
    isim="karanl�k"
    print "isim de�i�keni",isim
    print "fonksiyon i�indeki de�i�ken:",x
y()
print "isim de�i�keni",isim    
print "fonksiyon d���ndaki de�i�ken",x
#y() burada yaz�l�rsa hata ile kar��la��l�r. ��nk� y() �a�r�lmadan nas�l �al��s�n ki? �a�r�ld�ktan sonra i�e yarar eleman.













































