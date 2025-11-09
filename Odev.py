# Python Algoritma Soruları ve Çözümleri #

# bölüm 1 çözümler:



def enBuyukSayiyiBulma():
    while True:
        sayiList = []
        i = 0
        sayi = int()
        sayiMiktari = int(input("Girilecek Sayi Miktari: \t"))

        if sayiMiktari <= 0 or sayiMiktari == int():
         print("Lütfen Geçerli Bir Sayi Giriniz.")  
         continue
        else:

            for i in range(sayiMiktari):
                sayi = int(input("Lütfen Sayi Giriniz: \t"))
                sayiList.append(sayi)

        sayiList.sort()
        print( "Girilen En büyük Sayi: ",sayiList[-1])


# enBuyukSayiyiBulma()


def stringTersCevirme():
   while True:
      girdi= str(input("Yazi Giriniz: "))
      cikti = girdi[: : -1]
      print ("Ters Cikti = ",cikti)

#stringTersCevirme()




def faktoriyelhesaplama():
    while True:
        girdi = int()
        faktoriyel = 1

        girdi = int(input(" Sayı giriniz: \t"))
        if girdi < 0:
            print("Lutfen pozitif bir sayi giriniz.\n")
            continue
        elif girdi == 0 or girdi == 1:
            print("Sonuc = 1")
        elif girdi > 1:
            for i in range(1, girdi +1):
                faktoriyel *= i
                print("Sonuç :", faktoriyel)

#faktoriyelhesaplama()

def ciftsayifilter():
    while True:
        girdi = 0
        list = []

        sayiAdet = int(input("Miktar girin: \t"))
        if sayiAdet < 0 or sayiAdet ==0:
            print("Lutfen gecerli miktar giriniz.\n")
            continue
        else:
            for i in range(sayiAdet):
                girdi = int(input("Sayi giriniz: \t"))
                if girdi % 2 == 0:
                    list.append(girdi)

        print("Cift sayilar: ", list ,"\n")

#ciftsayifilter()


def listeBirlestirme():
    list1 = [4, 5, 6]
    list2 = [6, 7, 8]
    liste = list1 + list2
    return list(set(liste))

#print(listeBirlestirme)

def Palindrom():
    girdi = str(input("Kelime: "))
    girdi = girdi.replace(" ", "")
    cikti = girdi[::-1]
    print("girdi : ", girdi)
    print(" Cikti : ", cikti)
    if cikti == girdi:
        print("BU bir palindrum .")
    else:
        print("Bu Bir palindrum değil.")
    
#Palindrom()


