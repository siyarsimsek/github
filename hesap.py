# -*- coding: cp1254 -*-
"""
print ""
\t\t\tHESAP MAK�NES�\t\t\t\n
\t\t\t1-TOPLAMA ��LEM�\n
\t\t\t2-�IKARMA ��LEM�\n
\t\t\t3-B�LME ��LEM�\n
\t\t\t4-�ARPMA ��LEM�\n
""

a=1
while a<=3:
    x=int(input("ilk say�y� giriniz.\t"))
    y=int(input("ikinci say�y� giriniz.\t"))
    z=int(input("yapaca��n�z i�lemi se�iniz.\t"))
    if z==1:
        print x+y
    elif z==2:
        print x-y
    elif z==3:
        print float(x/y)
    elif z==4:
        print x*y
    else:
        print("1 ile 4 aras�nda bir say� yaz�n�z.")

    a=a+1

"""

"""
x=1
while x<=10:
    y=1
    while y<=10:
        print x,"x",y,"=",(x*y),"\t"
        y=y+1

    x=x+1
"""        
""""
for a in range(1,11):
    
    for b in range(1,11):
        print a,"x",b,"=",(a*b)
    print ""

#for ile while aras�nda de�i�ik bir durum var gibi. for, while'dan daha efektif.
""""
"""
def ile fonksiyonu tan�mlar�z.
    def fonksiyon_ad�():
        fonksiyon i�eri�i
"""

def isim_yaz():
    print "siyar simsek"
isim_yaz()
