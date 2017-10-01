# -*- coding: cp1254 -*-
"""
print ""
\t\t\tHESAP MAKİNESİ\t\t\t\n
\t\t\t1-TOPLAMA İŞLEMİ\n
\t\t\t2-ÇIKARMA İŞLEMİ\n
\t\t\t3-BÖLME İŞLEMİ\n
\t\t\t4-ÇARPMA İŞLEMİ\n
""

a=1
while a<=3:
    x=int(input("ilk sayıyı giriniz.\t"))
    y=int(input("ikinci sayıyı giriniz.\t"))
    z=int(input("yapacağınız işlemi seçiniz.\t"))
    if z==1:
        print x+y
    elif z==2:
        print x-y
    elif z==3:
        print float(x/y)
    elif z==4:
        print x*y
    else:
        print("1 ile 4 arasında bir sayı yazınız.")

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

#for ile while arasında değişik bir durum var gibi. for, while'dan daha efektif.
""""
"""
def ile fonksiyonu tanımlarız.
    def fonksiyon_adı():
        fonksiyon içeriği
"""

def isim_yaz():
    print "siyar simsek"
isim_yaz()
