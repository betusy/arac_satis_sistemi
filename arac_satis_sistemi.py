
from datetime import datetime
from typing import Callable

class Insan:
    def __init__(self, tckn:int, adi:str, soyadi:str, adres:str, il:str, ilce:str, tel:str):
        self.tckn = tckn
        self.adi = adi
        self.soyadi = soyadi 
        self.adres = adres
        self.il = il
        self.ilce = ilce
        self.tel = tel

class Personel(Insan):
    personel_listesi = {}
    def __init__(self, tckn: int, adi: str, soyadi: str, adres: str, il: str, ilce: str, tel: str, gorevi:str):
        super().__init__(tckn, adi, soyadi, adres, il, ilce, tel)
        self.gorevi = gorevi
    def personel_ekle(self, tckn:int, adi:str,soyadi:str,adres:str,il:str,ilce:str,tel:int, gorevi:str):
        self.personel_listesi[tckn] = [adi,soyadi,adres,il,ilce,tel,gorevi]
        print("personel eklendi....")
    def personeli_listele(self):
        print("------ personel listesi -------")
        for p in self.personel_listesi:
            print(p)
    def personel_sil(self, tckn:int):
        self.personel_listesi.pop(tckn)
        print("personel silindi...")
    def personel_bul(self, tckn:int):
        print(f" personel adi soyadi: {self.personel_listesi[tckn][0]} {self.personel_listesi[tckn][1]}")
    def personel_duzenle(self):
        duzenlenen = int(input("""
        Lütfen düzenlemek istediğiniz bilgiyi seçiniz :
        (0) Personel adı        
        (1) Personel soyadı     
        (2) Personel adresi     
        (3) Personel ili        
        (4) Personel ilçesi     
        (5) Personel telefonu   
        (6) Personel görevi     
        """))
        tckn = input("tckn giriniz: ")
        self.personel_listesi[tckn][duzenlenen] = input(f"Lütfen yeni düzenlemeyi giriniz : ")

class Musteri(Insan):
    musteri_listesi = {}
    def musterileri_listele(self):
        print("------ musteri listesi ------")
        for m in self.musteri_listesi:
            print(m)
    def musteri_ekle(self, tckn:int, adi:str, soyadi:str, adres:str, il:str, ilce:str, tel:int):
        self.musteri_listesi[tckn] = [adi,soyadi,adres,il,ilce,tel]
        print("musteri kaydedildi.....")
    def musteri_sil(self, tckn:int):
        self.musteri_listesi.pop(tckn)
        print("musteri silindi....")
    def musteri_bul(self, tckn:int):
        print(f"musteri adi soyadi: {self.musteri_listesi[tckn][0]} {self.musteri_listesi[tckn][1]}")
    def musteri_duzenle(self):
        self.musterileri_listele()
        tckn = input("tckn giriniz:  ")
        self.musteri_bul(tckn)
        duzenle = int(input("""duzenlemek istediginiz secenegi secin:
        musteri adi, 0
        musteri soyadi, 1
        musteri adresi, 2
        musteri ili, 3
        musteri ilcesi, 4
        musteri telefonu, 5
        msuteri gorevi, 6 """))
        self.musteri_listesi[tckn][duzenle] = input(f"lutfen yeni duzenlemeyi gir: ")

class Arac:
    arac_listesi = {}
    def __init__(self, kodu:int, markasi:str, modeli:str, yili:int, kategorisi:list, fiyati:int, rengi:str):
        self.kodu = kodu
        self.markasi = markasi
        self.modeli = modeli
        self.yili = yili
        self.kategorisi = kategorisi
        self.fiyati = fiyati
        self.rengi = rengi
    def arac_ekle(self, kodu:int, markasi:str, modeli:str, yili:int, kategorisi:list, fiyati:int, rengi:str):
        self.arac_listesi[kodu] = [markasi, modeli, yili, kategorisi, fiyati, rengi]
        print("-------- arac kaydedildi --------")
    def araclari_listele(self):
        print("-------- arac listesi --------")
        for a in self.arac_listesi:
            print(a)
    def arac_sil(self, kodu:int):
        self.arac_listesi.pop(kodu)
        print("-------- arac silindi-------")
    def arac_bul(self, kodu:int):
        print(f"Aracin Markasi: {self.arac_listesi[kodu][0]} Aracin Modeli: {self.arac_listesi[kodu][1]}")
    def arac_duzenle(self):
        self.araclari_listele()
        arac_kodu = input("arac kodunu giriniz: ")
        self.arac_bul(arac_kodu)
        duzenleme = int(input("""lutfen duzenlemek istediginiz secenegi secin:
        arac markasi, 0
        arac modeli, 1
        arac yili, 2
        arac kategorisi, 3
        arac fiyati, 4
        arac rengi, 5 """))
        self.arac_listesi[arac_kodu][duzenleme] = input(f"lutfen duzenlemeyi secin:  ")

class Fatura:
    fatura_listesi = {}
    def __init__(self):
        pass
    def fatura_ekle(self, fatura_no:int, musteri:Musteri, arac:Arac, personel:Personel, fatura_tarihi:Callable, fatura_tutari:float):
        self.fatura_listesi[fatura_no] = [musteri,arac,personel,fatura_tarihi,fatura_tutari]
        print("fatura kaydedildi...")
    def faturalari_listele(self):
        print("-------- fatura listesi --------")
        for f in self.fatura_listesi:
            print(f)
    def fatura_sil(self, fatura_no:int):
        self.fatura_listesi.pop(fatura_no)
        print("fatura silindi....")
    def fatura_bul(self, fatura_no):
        print(f"musteri: {self.fatura_listesi[fatura_no][0]} arac : {self.fatura_listesi[fatura_no][1]}")
    def fatura_duzenle(self):
        fatura_no = input("Fatura numarası giriniz: ")
        duzenlenen = int(input("""
        Lütfen düzenlemek istediğiniz bilgiyi seçiniz :
        (0) Müşteri bilgileri        
        (1) Araç bilgileri
        (2) Personel bilgileri     
        (3) Fatura tarihi          
        (4) Fatura tutarı      
        """))
        self.fatura_listesi[fatura_no][duzenlenen] = input(f"Lütfen yeni düzenlemeyi giriniz : ")
    
class SaatAyar:
    def saat_ayari():
        print("saat ve tarih ayari yapidi...")

class Aciklama:
    print("arac satis sistemine hosgeldiniz............")

musteri = Musteri()
personel = Personel()
fatura = Fatura()
arac = Arac()

class MusteriYonetimSistemi:
    def musteri_yonetim_sistemi():
        while True:
            print(""" ///////// Musteri Yonetim Menusu //////////
            Lutfen bir secenek girin:
            -----------------------
            musteri ekle, 1
            musteri bul, 2
            musteri sil, 3
            musteri duzenle, 4
            ana menuye don, 5
            -----------------------""")
            secenek = input("lutfen seciminizi girin: ")
            if secenek == "1":
                musteri.musteri_ekle(input("tckn:"), input("adi: "), input("syadi: "), input("adres: "),input("il: "),input("ilce: "), input("tel: "))
            elif secenek == "2":
                if musteri.musteri_listesi == {}:
                    print("henuz eklnemis musteri kaydi yok, once musteri ekleyin.")
                else:
                    while True:
                        try:
                            musteri.musteri_bul(input("tckn: "))
                            break
                        except KeyError:
                            print("Lutfen dogru musteri tckn girin. ")
            elif secenek == "3":
                if musteri.musteri_listesi == {}:
                    print("musteri listesinde henuz musteri kaydi yok.")
                else:
                    while True:
                        try:
                            musteri.musterileri_listele()
                            musteri.musteri_sil(input("silmek istediginiz musteri tckn: "))
                        except KeyError:
                            print("dogru tckn girin.")
            elif secenek == "4":
                if musteri.musteri_listesi == {}:
                    print("musteri listesinde henuz musteri kaydi yok.")
                else:
                    while True:
                        try:
                            musteri.musteri_duzenle()
                            break
                        except KeyError:
                            print("hatali giris")
            elif secenek == "5":
                break
            else:
                print("lutfen gecerli bir secenek girin.")

class PersonelYonetimSistemi:
    def personel_yonetim_sistemi():
        while True:
            print(""" ///////// Personel Yonetim Menusu //////////
            Lutfen bir secenek girin:
            -----------------------
            personel ekle, 1
            personel bul, 2
            personel sil, 3
            personel duzenle, 4
            menuye don, 5
            -----------------------""")
            secenek = input("=")
            if secenek == "1":
                personel.personel_ekle(input("tckn: "), input("ad"), input("soyadi:"), input("adres"))
            elif secenek == "2":
                if personel.personel_listesi == {}:
                    print("personel listesi bos.")
                else:
                    while True:
                        try:
                            personel.personeli_listele()
                            personel.personel_bul(input("tckn:"))
                            break
                        except KeyError:
                            print("yanlis giris.")
            elif secenek == "3":
                if personel.personel_listesi == {}:
                    print("henuz personel eklenmemis.")
                else:
                    while True:
                        try:
                            personel.personeli_listele()
                            personel.personel_sil(input("silmek istediginiz personel tckn: "))
                            break
                        except KeyError:
                            print("lutfen dogru bir personel tckn girin.")
            elif secenek == "4":
                if personel.personel_listesi == {}:
                    print("henuz personel listesi bos.")
                else:
                    while True:
                        try:
                            personel.personel_duzenle()
                            break
                        except KeyError:
                            print("lutfen dogru secenegi girin.")
            elif secenek == "5":
                break
            else:
                print("lutfen gecerli bir secenek girin.")

class AracYonetimSistemi:
    def arac_yonetim_sistemi():
        while True:
            print(""" ///////// Arac Yonetim Menusu //////////
            Lutfen bir secenek girin:
            -----------------------
            arac ekle, 1
            arac bul, 2
            arac sil, 3
            arac duzenle, 4
            ana menuye don, 5
            -----------------------""")
            secenek = input("=")
            if secenek == "1":
                arac.arac_ekle(input("Araç kodunu giriniz : "), input("Araç markasını giriniz : "), input("Araç modelini giriniz : "), input("Araç yılını giriniz : "), input("Araç kategorisini giriniz : "), input("Araç fiyatını giriniz : "), input("Araç rengini giriniz : "))
            elif secenek == "2":
                if arac.arac_listesi == {}:
                    print("Arac listesi bos. Lutfen arac ekleyin.")
                else:
                    while True:
                        try:
                            arac.arac_bul(input("arac kodunu girin: "))
                            break
                        except KeyError:
                            print("lutfen dogru arac kodunu giriniz.")
            elif secenek == "3":
                if arac.arac_listesi == {}:
                    print("Henüz eklenmiş bir araç bulunmamaktadır! Lütfen önce araç ekleyiniz.")
                else:
                    while True:
                        try:
                            arac.arac_sil(input("Araç kodunu giriniz : "))
                            break
                        except KeyError:
                            print("Lütfen doğru araç kodunu giriniz!")   
            elif secenek == "4":
                if arac.arac_listesi=={}:
                    print("Henüz eklenmiş bir araç bulunmamaktadır! Lütfen önce araç ekleyiniz.")
                else:
                    while True:
                        try:
                            arac.arac_duzenle()
                            break
                        except KeyError:
                            print("Lütfen doğru araç kodunu giriniz!","\a")     
            elif secenek == "5":
                break
            else:
                print("gecersiz islem ")    

class FaturaYonetimSistemi:
    def fatura_yonetim_sistemi():
        while True:
            print(""" ///////// Fatura Yonetim Menusu //////////
            Lutfen bir secenek girin:
            -----------------------
            fatura ekle, 1
            fatura bul, 2
            fatura sil, 3
            fatura duzenle, 4
            ana menuye don, 5
            -----------------------""")
            secenek = input("Lütfen seçiminizi girin: ")   
            if secenek=="1":
                if arac.arac_listesi == {}:
                    print("arac listesi bos.")
                elif personel.personel_listesi == {}:
                    print("personel listesi bos.")               
                elif musteri.musteri_listesi == {}:
                    print("msuteri listesi bos.")
                else:
                    while True:
                        fatura_num = input("fatura no girin: ")
                        try:
                            musteri.musterileri_listele()
                            musteri_num = musteri.musteri_listesi[input("musteri listesinden musteri tckn girin: ")]
                            personel.personeli_listele()
                            personel_num = personel.personel_listesi[input("personel listesinden personel tckn girin: ")]
                            arac.araclari_listele()
                            arac_num = arac.arac_listesi[input("arac listesinden arac numarasini girin: ")]
                            arac_tut = float(arac_num[5]) * 120/100
                            break
                        except KeyError:
                            print("gecersiz islem")
                fatura.fatura_ekle(fatura_num, musteri_num, arac_num, personel_num, datetime.now, arac_tut )  

            elif secenek == "2":
                fatura.faturalari_listele()
                try:
                    fatura.fatura_bul(input("fatura numarasini girin: "))
                except KeyError:
                    print("yanlis giris yaptiniz.")

            elif secenek == "3":
                fatura.faturalari_listele()
                try:
                    fatura.fatura_sil(input("silmek istediginiz fatura numarasini girin: "))
                    break
                except KeyError:
                    print("yanlis giris yaptiniz. ")
            elif secenek == "4":
                if fatura.fatura_listesi == {}:
                   print("fatura listesi bos.")
                else:
                    try:
                        fatura.fatura_duzenle()
                    except KeyError:
                        print("lutfen dogru fatura numrasi girin.")
            elif secenek == "5":
                break
            else:
                print("gecersiz giris.")
                    
class MenuYonetimi:
    def menu_yonetimi():
        while True:
            print(""" ///////// Ana Menu //////////
            Lutfen bir secenek girin:
            -----------------------
            arac yonetimi, 1
            musteri yonetimi, 2
            perosnel yonetimi, 3
            fatura yonetimi, 4
            cikis, 5
            -----------------------""")
            secenek = input("= ")
            if secenek == "1":
                AracYonetimSistemi.arac_yonetim_sistemi()
            elif secenek == "2":
                MusteriYonetimSistemi.musteri_yonetim_sistemi()
            elif secenek == "3":
                PersonelYonetimSistemi.personel_yonetim_sistemi()
            elif secenek == "4":
                FaturaYonetimSistemi.fatura_yonetim_sistemi()
            elif secenek == "5":
                print("cikis yapildi..........")
            else:
                print("lutfen gecerli bir islem girin.")

MenuYonetimi.menu_yonetimi()
