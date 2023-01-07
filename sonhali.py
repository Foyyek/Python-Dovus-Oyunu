import random

#oyuncuların canları
player1_hp = player2_hp = 100

#karşılama mesajı
print("-------------------Kafes Dövüşüne Hoşgeldin Yabancı-------------------")
print("-Hey dövüşçüler caymanız için son şansınız buradan yanlızca biriniz sağ çıkabilir-")
print("----------------------------------------------------------------------\n")

#sırayla kullanıcıdan isim alıp (benzer olmayan) ilk kısmı başlatıyoruz
def oyuncu_giris():
    global oyuncubir
    global oyuncuiki
    print("\n--------- İlk Kahraman ---------")
    oyuncubir = str(input("Birinci oyuncunun ismi:"))
    print("Oyunumuza hoşgeldin,",oyuncubir)
    print("--------- İkinci Kahraman ---------")
    oyuncuiki = str(input("İkinci oyuncunun ismi:"))
    if oyuncubir == oyuncuiki:
        print("1.oyuncun ismi ile aynı ismi alamazsın")
        print("\n--------- İkinci Kahraman ---------")
        oyuncuiki = str(input("İsminizi tekrar giriniz:"))
    elif len(oyuncuiki) == 0:
        print("Hatalı isim girişi.")
        input("İsminizi tekrar giriniz:")
    print("oyunumuza hoşgeldin,",oyuncuiki)

    return oyuncubir, oyuncuiki

#yazı tura sistemiyle oyuna başlayacak ilk oyuncuyu seçiyoruz
def kura():
    global hamle1
    global hamle2
    print('---------------------------------------------')
    print("Oyuna Başlayacak Kişi Seçiliyor... \n \n")

    #oyuncuların bulunduğu listeden yani 2 sinden birini seçerek oyuna başlayanı seçiyoruz
    liste = [True, False]
    kazanan = random.choice(liste)
    if kazanan:
        hamle1 = oyuncubir
        hamle2 = oyuncuiki
    if not kazanan:
        hamle1 = oyuncuiki
        hamle2 = oyuncubir
    print(hamle1, "ilk olarak başlıyor!\n")

    return hamle1, hamle2

#can barını iki oyuncu içinde oluşturuyoruz ve bosluk ta yazdığımız gibi can isimleri birbirinden ayırarak can barları hizzasına alıyoruz
def canlar():
    # isimler arası boşluğu barlara göre ayalama
    bosluk = (75 - len(oyuncubir)) * " "

    #("|") çeklinde can barlarını ayarlıyor ve canın yarısı kadar yani 50 çizgi olarak uzatıyoruz
    oyuncu1_can = "|" * (player1_hp // 2)
    oyuncu2_can = "|" * (player2_hp // 2)

    if 10 <= player1_hp <= 99:
        can1_bosluk = (67 - len(oyuncu1_can)) * " "
    elif player1_hp < 10:
        can1_bosluk = (68 - len(oyuncu1_can)) * " "
    else:
        can1_bosluk = (66 - len(oyuncu1_can)) * " "

    print(oyuncubir, bosluk, oyuncuiki, "\n")

    print("HP=[{}]:{}".format(player1_hp, oyuncu1_can), can1_bosluk, "HP=[{}]:{}".format(player2_hp, oyuncu2_can))
    return player1_hp, player2_hp

#asıl fight'ın döndüğü kısım.Burada ilk kısımda vuruş şanslarını ayalıyoruz
#daha sonra hasar tutar ise yani saldırı başarılıysa bar üzerinde yenilen hasar kadarın yarısı kadar azaltıyoruz
#sonrasında aynı işlemi 2. oyuncuda da yapıyoruz
def savas():
    global player1_hp
    global player2_hp
    print("---------------------------------------------")
    print("----",oyuncubir, "Saldırı !! ----")
    player1_vurus = int(input("Lütfen 1 ila 50 arasında bir vuruş gücü seç: "))
    #ilk oyuncuya girilen değerin hatalı olması durumunda
    if player1_vurus > 50 or player1_vurus < 1:
        print("Lütfen geçerli bir vuruş gücü seçiniz!")
        print("---------------------------------------------")
        player1_vurus = int(input(oyuncubir + " Lütfen 1 ila 50 arasında bir vuruş gücü seç: "))
    else:
        print(oyuncubir, "Iskaladı!")
        print("---------------------------------------------")
        canlar()
    player1_sans = 100 - (player1_vurus)
    sans_list = []
    for i in range(player1_vurus):
        sans_list.append(False)
    for i in range(player1_sans):
        sans_list.append(True)
    sonuc = random.choice(sans_list)
    if sonuc:
        print(oyuncubir, "Güçlü bir darbe indirdi!")
        print("---------------------------------------------")
        player2_hp -= player1_vurus
        canlar()
        if player2_hp <= 0:
            player2_hp = 0
            print("********************************************************")
            print("******* Oyun Bitti ve {} kazandı".format(oyuncubir),"*******")
            print("********************************************************")
            canlar()
            yeniden_baslat()
    elif sonuc:
        print(oyuncubir, "Iskaladı!")
        print("---------------------------------------------")
        canlar()

    print("----", oyuncuiki, "Saldırı !! ----")
    player2_vurus = int(input(oyuncuiki + " Lütfen 1 ila 50 arasında bir vuruş gücü seç: "))
    # ikinci oyuncuya girilen değerin hatalı olması durumunda
    if player2_vurus > 50 or player2_vurus < 1:
        print("Lütfen geçerli bir vuruş gücü seçiniz!")
        print("---------------------------------------------")
        player2_vurus = int(input(oyuncuiki + " Lütfen 1 ila 50 arasında bir vuruş gücü seç: "))
    player2_sans = 100 - (player2_vurus)
    sans_list = []
    for i in range(player2_vurus):
        sans_list.append(False)
    for i in range(player2_sans):
        sans_list.append(True)
    sonuc = random.choice(sans_list)
    if sonuc:
        print(oyuncuiki, "Güçlü bir darbe indirdi!")
        print("---------------------------------------------")
        player1_hp -= player2_vurus
        canlar()
        if player1_hp <= 0:
            player1_hp = 0
            print("---------------------------------------------")
            print("********************************************************")
            print("******* Oyun Bitti ve {} kazandı".format(oyuncubir),"*******")
            print("********************************************************")
            yeniden_baslat()
    elif not sonuc:
        print(oyuncuiki, "Iskaladı!")
        canlar()
    if player1_hp >= 1 and not player2_hp <= 0 or player2_hp >= 1 and not player1_hp <= 1:
        savas()
        return player1_hp, player2_hp

#savaş bittikten (yani 1 oyuncunun canı 0'landığı zaman oyun biter) sonra aynı oyuncuylar tekrardan oynamak isteyip istemediği souruluyor
#eğer tekrar oynamak isterlerse evet yazarak yeniden oynayabilir oynamak istemezse hayır yazarak işlemi bitirebilir
def yeniden_baslat():
    global player1_hp
    global player2_hp
    player1_hp = player2_hp = 100
    seçim = str(input("Yeniden başlamak ister misiniz?(Evet/Hayır): "))
    if seçim == "evet":
        kura(), canlar(), savas(), yeniden_baslat()
        return
    elif seçim == "hayır":
        print("Oynadığınız için teşekkürler!")
    else:
        return yeniden_baslat()
    exit()

oyuncu_giris(), kura(), canlar(), savas()