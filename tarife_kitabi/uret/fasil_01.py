"""Fasıl 1 – Canlı hayvanlar → data/fasil_01.json"""
from yardim_00_03 import q, yaz, T_E, T_O, T_F, T_N, T_G, T_B, T_C, T_S

modul = {
    "tur": "fasil",
    "fasil": 1,
    "baslik": "Canlı hayvanlar",
    "bolum": "I",
    "oz": {
        "vurgu": "Fasıl 1 tek bir soru sorar: Eşya canlı bir hayvan mı? Canlıysa; balıklar ve su omurgasızları (Fasıl 3), mikroorganizma kültürleri (30.02) ve sirk ya da gezici hayvan gösterisi hayvanları (95.08) dışında, amacı ne olursa olsun buradadır ve türüne göre 01.01–01.06’dan birine yerleşir.",
        "maddeler": [
            "Evcil veya yabani ayrımı çoğu pozisyonda önemsizdir (at, sığır, domuz, koyun, keçi); 01.05 ise yalnızca adı geçen evcil kümes hayvanlarını kapsar.",
            "Bölüm I Not 1: bir hayvan cins veya türüne yapılan atıf, aksi belirtilmedikçe yavrusunu da kapsar (tay, kuzu, oğlak).",
            "01.06 artık pozisyondur: memeliler (balina, yunus, fok dahil), sürüngenler, kuşlar, böcekler ve diğerleri (kurbağa).",
            "Nakliye sırasında ölen hayvan artık canlı değildir: eti yenilebiliyorsa Fasıl 2 veya 04.10, değilse 05.11."
        ]
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Hayvan cansız mı? (ör. nakliye sırasında ölmüş)", "Yenilebilirse <b>02.01–02.05</b>, <b>02.07</b>, <b>02.08</b> veya <b>04.10</b>; değilse <b>05.11</b>"],
            ["2", "Balık, kabuklu, yumuşakça veya diğer su omurgasızı mı?", "Fasıl 3: <b>03.01</b> / <b>03.06</b> / <b>03.07</b> / <b>03.08</b>"],
            ["3", "Mikroorganizma kültürü mü?", "<b>30.02</b>"],
            ["4", "Sirk, hayvan sergisi veya benzeri gezici hayvan gösterisinin parçası mı?", "<b>95.08</b>"],
            ["5", "At, eşek, katır veya bardo mu?", "<b>01.01</b>"],
            ["6", "Sığır, manda, bizon gibi büyükbaş mı?*", "<b>01.02</b>"],
            ["7", "Domuz mu? (evcil veya yabani)", "<b>01.03</b>"],
            ["8", "Koyun veya keçi mi? (evcil veya yabani)", "<b>01.04</b>"],
            ["9", "Horoz, tavuk, ördek, kaz, hindi veya beç tavuğu gibi evcil kümes hayvanı mı?", "<b>01.05</b>"],
            ["10", "Hiçbiri değilse (diğer memeliler, sürüngenler, kuşlar, böcekler, kurbağalar)", "<b>01.06</b>"]
        ],
        "dipnot": "* 01.02, dört boynuzlu antilopu ve Taurotragus ile Tragelaphus cinsi sarmal boynuzlu antilopları da kapsar; Bovinae alt familyası dışındaki antiloplar 01.06’dadır. Yabani ördek, yabani kaz, keklik, sülün ve güvercin evcil kümes hayvanı sayılmaz → 01.06."
    },
    "pozisyon_haritasi": [
        ["01.01", "Canlı atlar, eşekler, katırlar ve bardolar", "Evcil veya yabani; katır = erkek eşek × kısrak, bardo = aygır × dişi eşek", "Midilli, tay, katır, bardo"],
        ["01.02", "Canlı büyükbaş hayvanlar", "Sığırlar (Bos cinsi), bufalolar (Bubalus, Syncerus, Bizon), beeffalo, bazı antiloplar", "Zebu, yak (Tibet sığırı), manda, bizon"],
        ["01.03", "Canlı domuzlar", "Evcil ve yabani", "Yabani erkek domuz"],
        ["01.04", "Canlı koyun ve keçiler", "Evcil veya yabani", "Koç, kuzu, oğlak"],
        ["01.05", "Canlı kümes hayvanları", "Yalnız sayılan evcil türler", "Tavuk, besili horoz, hindi, ördek, kaz, beç tavuğu"],
        ["01.06", "Diğer canlı hayvanlar", "Memeliler, sürüngenler, kuşlar, böcekler, diğerleri", "Maymun, yunus, deve, tavşan, yılan, papağan, devekuşu, arı, kurbağa"]
    ],
    "notlar": [
        ["Bölüm I Not 1", "Bu bölümde adı geçen belirli bir hayvan cins veya türüne yapılan atıf, metinde aksi belirtilmedikçe bu cins veya türün yavrusuna da yapılmış sayılır."],
        ["Bölüm I Not 2", "Metinde aksi belirtilmedikçe Tarifede “kurutulmuş” ürünlere yapılan atıf; suyu alınmış, buharlaştırılmış veya dondurularak kurutulmuş (liyofilize) ürünlere de yapılmış sayılır."],
        ["Fasıl 1 Notu", "Fasıl, şunlar dışındaki bütün canlı hayvanları kapsar: 03.01, 03.06, 03.07 veya 03.08’e giren balıklar, kabuklu hayvanlar, yumuşakçalar ve suda yaşayan diğer omurgasız hayvanlar; 30.02’deki mikroorganizma kültürleri ve diğer ürünler; 95.08’deki hayvanlar."],
        ["Genel Açıklamalar", "Canlı hayvanlar gıda veya diğer amaçlar için olsun bu fasıldadır. 95.08 hariç tutması: sirk, hayvan sergileri veya benzeri gezici hayvan gösterilerinde yer alan hayvanlar."],
        ["Genel Açıklamalar", "Nakliye sırasında ölen hayvanlar (böcekler dahil): insan tüketimine uygun eti yenilebilen hayvanlarsa 02.01–02.05, 02.07, 02.08 veya 04.10; diğer durumlarda 05.11."],
        ["01.01 Açıklama Notu", "Evcil veya yabani atlar (kısrak, aygır, beygir, tay, midilli), eşekler, katırlar ve bardolar. Katır: erkek eşek ile kısrağın melez dölü; bardo: aygır ile dişi eşeğin melezi."],
        ["01.02 Açıklama Notu", "Sığırlar: Bos cinsi (Bos, Bibos, Novibos, Poephagus alt grupları) – adi öküz, zebu, Watussi öküzü; gaur, gayal, banteng; Tibet sığırı. Bufalo: Bubalus (manda, anoa), Syncerus (Afrika mandaları) ve Bizon cinsi; beeffalo (bizon × evcil sığır). Diğerleri: dört boynuzlu antilop, Taurotragus ve Tragelaphus cinsi sarmal boynuzlu antiloplar."],
        ["01.03 ve 01.04 Açıklama Notları", "01.03 evcil ve yabani domuzları (ör. yabani erkek domuz) kapsar. 01.04 evcil veya yabani koyunları (koç, koyun, kuzu) ve evcil veya yabani keçi ve oğlakları kapsar."],
        ["01.05 Açıklama Notu", "Yalnız pozisyonda belirtilen canlı evcil kanatlılar: Gallus domesticus türü horoz ve tavuklar (kısırlaştırılmış besili horozlar dahil), ördekler, kazlar, hindiler, beç tavukları. Keklik, sülün, güvercin, yabani ördek ve yabani kaz gibi diğer canlı kuşlar 01.06’dadır."],
        ["01.06 Açıklama Notu", "(A) Memeliler: maymunlar; balinalar, yunuslar, domuz balıkları; manati ve deniz inekleri; fok, deniz aslanı, deniz aygırı; diğerleri (ren geyiği, kedi, köpek, aslan, ayı, fil, deve, zebra, tavşan, geyik, Bovinae dışı antiloplar, tilki, gelincik ve kürk için yetiştirilen çiftlik hayvanları). (B) Sürüngenler (yılan, kaplumbağa). (C) Kuşlar: yırtıcı kuşlar, papağanımsılar, diğerleri (bıldırcın, güvercin, yabani ördek, tavus kuşu, kuğu; devekuşu ve emu). (D) Böcekler (arılar; kovanda olsun olmasın). (E) Diğerleri (kurbağa). Sirk ve gezici hayvan gösterisi hayvanları hariç (95.08)."]
    ],
    "sinir_komsulari": [
        ["Canlı süs balığı, canlı alabalık, canlı yılan balığı", "03.01", "Fasıl 1 Notu: balıklar hariç"],
        ["Canlı ıstakoz, yengeç, karides", "03.06", "Kabuklu hayvan"],
        ["Canlı istiridye, midye, ahtapot, salyangoz", "03.07", "Yumuşakça"],
        ["Canlı deniz kestanesi, deniz hıyarı, deniz anası", "03.08", "Diğer su omurgasızı"],
        ["Mikroorganizma kültürleri", "30.02", "Fasıl 1 Notu"],
        ["Sirk, hayvan sergisi veya gezici gösteri hayvanları", "95.08", "Fasıl 1 Notu"],
        ["Nakliyede ölmüş, eti yenilebilir sığır, kuzu, tavuk", "02.01–02.05 / 02.07", "Cansız; yenilebilir et"],
        ["Nakliyede ölmüş, yenilebilir böcekler", "04.10", "Cansız; yenilebilir"],
        ["Yenilmeye elverişsiz cansız hayvanlar", "05.11", "Cansız; yenilmez"],
        ["Balina, yunus, fok eti; kurbağa bacağı", "02.08 / 02.10", "01.06 hayvanlarının eti"],
        ["Canlı yabani ördek, yabani kaz, sülün, keklik", "01.06 (01.05 değil)", "01.05 yalnız evcil türleri kapsar"],
        ["Canlı manda, bizon, yak, beeffalo", "01.02 (01.06 değil)", "Büyükbaş hayvan tanımına girer"],
        ["Canlı yabani domuz, yabani koyun, yabani keçi", "01.03 / 01.04 (01.06 değil)", "Bu pozisyonlar yabani olanları da kapsar"],
        ["Canlı deniz kaplumbağası", "01.06 (Fasıl 3 değil)", "Sürüngendir; balık veya su omurgasızı değildir"]
    ],
    "tuzaklar": [
        "<b>Yunus ve balina balık değildir.</b> Canlı halleri deniz memelisi olarak 01.06’dadır; Fasıl 3 Not 1 bunları Fasıl 3 dışında bırakır.",
        "<b>Her canlı su hayvanı Fasıl 1 değildir.</b> Canlı balık 03.01, canlı kabuklu 03.06, canlı yumuşakça 03.07, canlı deniz kestanesi 03.08.",
        "<b>Kabuk taşıyan her canlı “kabuklu hayvan” değildir.</b> Kaplumbağa sürüngendir → 01.06; salyangoz ise yumuşakçadır → 03.07.",
        "<b>Ördek her zaman 01.05 değildir.</b> Evcil ördek ve kaz 01.05; yabani ördek ve yabani kaz 01.06.",
        "<b>Yabanilik 01.06’ya göndermez.</b> Yabani at 01.01, yabani sığır 01.02, yabani domuz 01.03, yabani koyun ve keçi 01.04’te kalır.",
        "<b>Sirk hayvanı Fasıl 1’de değildir.</b> Sirk, hayvan sergisi veya gezici gösteri hayvanları türüne bakılmaksızın 95.08’dedir.",
        "<b>Cansız hayvan canlı hayvan pozisyonunda kalmaz.</b> Nakliyede ölen hayvan yenilebilirse Fasıl 2 veya 04.10’a, değilse 05.11’e gider.",
        "<b>Mikroorganizma canlıdır ama Fasıl 1 değildir.</b> Kültürleri 30.02’dedir.",
        "<b>Antiloplar ikiye ayrılır.</b> Dört boynuzlu antilop ile Taurotragus ve Tragelaphus cinsi sarmal boynuzlular 01.02’de; Bovinae dışındaki antiloplar 01.06’da.",
        "<b>Katır ile bardo karıştırılır.</b> İkisi de 01.01’dedir; katır erkek eşek × kısrak, bardo aygır × dişi eşek melezidir."
    ],
    "hafiza": {
        "kanca": "AT – SIĞIR – DOMUZ – KOYUN – KÜMES – DİĞER",
        "aciklama": "01.01 <b>at</b> ailesi (eşek, katır, bardo), 01.02 <b>sığır</b> ve mandalar, 01.03 <b>domuz</b>, 01.04 <b>koyun</b>-keçi, 01.05 evcil <b>kümes</b>, 01.06 geri kalan her canlı. Görsel benzetme: bir çiftliği kapıdan içeri doğru gezin; ahır, büyükbaş ağılı, domuz ahırı, koyun ağılı, kümes; çiftliğin dışındaki her şey (orman, gökyüzü, deniz memelileri, kovan) 01.06’dır. Balık havuzu ve sirk çadırı çiftliğe dahil değildir."
    },
    "sinav_odagi": [
        "Bu fasıl çıkmış sorularda daha çok seçeneklerde/çeldirici olarak yer almıştır; doğrudan Fasıl 1 pozisyonu soran soru azdır.",
        "Deniz memelilerinin (balina) Fasıl 3 yerine 01.06’da yer alması, “3. fasılda sınıflandırılmaz” kalıbıyla sorulmuştur.",
        "01.06 hayvanlarının etinin (dondurulmuş balina eti) 02.08’e gitmesi; canlı hayvan ile et pozisyonları arasındaki bağ.",
        "Hayvan türü bilgisi (katır, yak, lama, Tibet keçisi, ren geyiği gibi) kıl, deri ve kürk gibi başka fasıllara ait sorularda seçenek olarak kullanılmıştır.",
        "İnsan tüketimine uygunluk ölçütü: yenilebilir böcekler ve kaplumbağa yumurtası 04.10, yenmeyen cansız hayvanlar 05.11."
    ],
    "cikmis_ornekler": [
        {
            "soru": "Aşağıdaki canlılardan hangisi Türk Gümrük Tarife Cetveli’nin 3. faslında <b>sınıflandırılmaz</b>?",
            "secenekler": ["Alabalık", "Köpek balığı", "Balina", "Deniz kulağı", "Deniz hıyarı"],
            "cevap": "C",
            "aciklama": "Balina deniz memelisidir; Fasıl 3 Not 1 onu Fasıl 3 dışında bırakır ve canlı balina 01.06’da memeliler arasında sınıflandırılır. Alabalık ve köpek balığı balık (03.01), deniz kulağı yumuşakça (03.07), deniz hıyarı diğer su omurgasızı (03.08) olarak Fasıl 3’tedir."
        }
    ],
    "ozet": [
        "Canlı her hayvan Fasıl 1’dedir; istisnalar: balık ve su omurgasızları (Fasıl 3), mikroorganizma kültürleri (30.02), sirk ve gezici gösteri hayvanları (95.08).",
        "At ailesi 01.01, büyükbaş 01.02, domuz 01.03, koyun-keçi 01.04, evcil kümes 01.05, geri kalanlar 01.06.",
        "Evcil veya yabani olmak kural olarak pozisyonu değiştirmez; istisna 01.05: yalnız evcil kümes hayvanları.",
        "Yavru, ana türün pozisyonundadır (Bölüm I Not 1).",
        "Deniz memelileri, sürüngenler (kaplumbağa dahil), arılar ve kurbağalar 01.06’dadır.",
        "Nakliyede ölen hayvan: yenilebilirse Fasıl 2 / 04.10, değilse 05.11."
    ],
}

S = []
# 1
S.append(q("Tarife Cetveline göre, bizon ile evcil sığırın melezi olan canlı “beeffalo” hangi pozisyonda sınıflandırılır?",
           ["01.01", "*01.02", "01.03", "01.04", "01.06"], T_E,
           "01.02 Açıklama Notu, bufalo kategorisinde Bubalus, Syncerus ve Bizon cinsi hayvanlarla birlikte beeffalo’yu (bizon ile evcil sığırların melezi) açıkça sayar. Melez olması onu 01.06’ya (diğer canlı hayvanlar) göndermez; 01.01 at ailesi, 01.04 koyun ve keçi pozisyonudur.",
           "01.02 Açıklama Notu."))
# 2
S.append(q("Tarife Cetveline göre, aygır ile dişi eşeğin melezi olan canlı bardo hangi pozisyonda sınıflandırılır?",
           ["*01.01", "01.02", "01.04", "01.06", "95.08"], T_E,
           "01.01 pozisyonu canlı atları, eşekleri, katırları ve bardoları kapsar; bardolar aygır ile dişi eşeğin melezidir. Melez hayvanın 01.06’ya gittiğini sanmak tuzaktır. 95.08 ancak sirk veya gezici hayvan gösterisinin parçası olan hayvanlar içindir.",
           "01.01 pozisyon metni ve Açıklama Notu."))
# 3
S.append(q("Tarife Cetveline göre canlı kara salyangozları (deniz salyangozları hariç) hangi pozisyonda sınıflandırılır?",
           ["01.06", "03.06", "*03.07", "03.08", "05.08"], T_E,
           "Salyangozlar yumuşakçadır; 03.07 Açıklama Notu salyangozları başlıca yumuşakçalar arasında sayar ve pozisyon canlı yumuşakçaları da kapsar. Fasıl 1 Notu 03.07’ye giren yumuşakçaları hariç tuttuğundan 01.06 yanlıştır. 03.06 kabuklu hayvanlar, 03.08 diğer su omurgasızları, 05.08 ise yumuşakça kabukları içindir.",
           "Fasıl 1 Notu; 03.07 pozisyon metni ve Açıklama Notu."))
# 4
S.append(q("Tarife Cetveline göre canlı deniz kaplumbağası hangi pozisyonda sınıflandırılır?",
           ["*01.06", "03.01", "03.06", "03.08", "04.10"], T_E,
           "Kaplumbağalar sürüngendir; 01.06 Açıklama Notu (B) sürüngenleri “yılanlar ve kaplumbağalar dahil” olarak sayar. Denizde yaşaması onu balık (03.01), kabuklu hayvan (03.06) veya su omurgasızı (03.08) yapmaz. 04.10 ise kaplumbağa yumurtası gibi yenilebilir hayvansal ürünlerin pozisyonudur.",
           "Fasıl 1 Notu; 01.06 Açıklama Notu (B)."))
# 5
S.append(q("Tarife Cetveline göre canlı ren geyiği hangi pozisyonda sınıflandırılır?",
           ["01.01", "01.02", "01.04", "*01.06", "95.08"], T_E,
           "01.06 Açıklama Notu memeliler arasında ren geyiklerini açıkça sayar. Ren geyiği büyükbaş hayvan tanımına (Bos, Bubalus, Syncerus, Bizon cinsleri) girmediği için 01.02’de değildir. Sirk veya gezici gösterinin parçası olmadıkça 95.08 uygulanmaz.",
           "01.06 Açıklama Notu (A); 01.02 Açıklama Notu."))
# 6
S.append(q("Aşağıdakilerden hangisi Tarife Cetvelinin 1. faslında <b>sınıflandırılmaz</b>?",
           ["Canlı yunus", "Canlı kurbağa", "*Canlı ahtapot", "Canlı papağan", "Canlı tavşan"], T_O,
           "Ahtapot bir yumuşakçadır; Fasıl 1 Notu 03.07’ye giren yumuşakçaları hariç tuttuğundan canlı ahtapot 03.07’dedir. Yunus (deniz memelisi), kurbağa (diğerleri), papağan (papağanımsılar) ve tavşan (memeliler) 01.06’da sayılmıştır. Tuzak, deniz canlısı olan yunusu Fasıl 3’e göndermektir.",
           "Fasıl 1 Notu; 01.06 Açıklama Notu; 03.07 pozisyon metni."))
# 7
S.append(q("Aşağıdakilerden hangisi 01.05 pozisyonunda <b>sınıflandırılmaz</b>?",
           ["Canlı beç tavuğu", "Canlı hindi", "Kısırlaştırılmış canlı besili horoz", "Canlı evcil kaz", "*Canlı yabani ördek"], T_O,
           "01.05 yalnızca pozisyonda belirtilen evcil kümes hayvanlarını kapsar; yabani ördekler ve yabani kazlar 01.06’dadır. Beç tavuğu, hindi ve evcil kaz pozisyon metninde sayılmıştır; Gallus domesticus türüne kısırlaştırılmış besili horozlar da dahildir.",
           "01.05 pozisyon metni ve Açıklama Notu; 01.06 Açıklama Notu (C)."))
# 8
S.append(q("Aşağıdakilerden hangisi 01.06 pozisyonunda <b>sınıflandırılmaz</b>?",
           ["Canlı deve", "Canlı tavşan", "*Canlı manda", "Canlı fil", "Canlı aslan"], T_O,
           "Manda (Bubalus cinsi) 01.02 Açıklama Notunda bufalo kategorisinde sayıldığından canlı büyükbaş hayvan olarak 01.02’dedir. Deve, tavşan, fil ve aslan 01.06 Açıklama Notunda “diğer memeliler” arasında sayılmıştır.",
           "01.02 Açıklama Notu; 01.06 Açıklama Notu (A)."))
# 9
S.append(q("Aşağıdaki canlı hayvanlardan hangisi 01.02 pozisyonunda <b>yer almaz</b>?",
           ["Zebu (hörgüçlü öküz)", "Amerikan bizonu", "Gaur", "Anoa (cüce manda)", "*Geyik"], T_O,
           "01.02 Bos cinsi sığırları (zebu, gaur), Bubalus cinsi mandaları (anoa) ve Bizon cinsi hayvanları (Amerikan bizonu) kapsar. Geyikler ise 01.06 Açıklama Notunda diğer memeliler arasında sayılmıştır. Boynuzlu ve otçul olması geyiği büyükbaş pozisyonuna sokmaz.",
           "01.02 Açıklama Notu; 01.06 Açıklama Notu (A)."))
# 10
S.append(q("Tarife Cetveline göre aşağıdaki canlı hayvanlardan hangisi diğerlerinden <b>farklı</b> bir pozisyonda sınıflandırılır?",
           ["Midilli", "Katır", "Bardo", "*Zebra", "Eşek"], T_F,
           "Midilli (at), katır, bardo ve eşek 01.01’de yer alır. Zebra at ailesine benzese de 01.01’de sayılmamış, 01.06 Açıklama Notunda diğer memeliler arasında gösterilmiştir.",
           "01.01 Açıklama Notu; 01.06 Açıklama Notu (A)."))
# 11
S.append(q("Evcil ve yabani hayvanlara ilişkin açıklama notları dikkate alındığında, aşağıdaki canlılardan hangisi diğer dördünden <b>farklı</b> bir pozisyonda yer alır?",
           ["Kuzu", "*Yabani erkek domuz", "Oğlak", "Yabani koyun", "Yabani keçi"], T_F,
           "Kuzu, oğlak, yabani koyun ve yabani keçi 01.04’tedir; pozisyon evcil veya yabani koyun ve keçileri kapsar. Yabani erkek domuz ise 01.03 Açıklama Notunda evcil ve yabani domuzlar arasında örnek gösterilmiştir. Tuzak, yabani hayvanların hepsini 01.06’ya göndermektir.",
           "01.03 ve 01.04 Açıklama Notları; Bölüm I Not 1."))
# 12
S.append(q("Aşağıdaki canlılardan hangisi diğerlerinden <b>farklı</b> bir fasılda sınıflandırılır?",
           ["*Canlı deniz hıyarı", "Canlı fok", "Canlı deniz aslanı", "Canlı manati (deniz güzeli)", "Canlı yunus"], T_F,
           "Fok, deniz aslanı, manati ve yunus deniz memelileri olarak 01.06’da, yani Fasıl 1’dedir. Deniz hıyarı ise kabuklu ve yumuşakça dışındaki su omurgasızı olarak 03.08’dedir; Fasıl 1 Notu 03.08’e giren hayvanları hariç tutar.",
           "Fasıl 1 Notu; 01.06 Açıklama Notu (A); 03.08 Açıklama Notu."))
# 13
S.append(q("Aşağıdaki canlı kuşlardan hangisi diğerlerinden <b>farklı</b> bir pozisyonda sınıflandırılır?",
           ["Sülün", "Keklik", "Güvercin", "*Beç tavuğu", "Bıldırcın"], T_F,
           "Beç tavuğu 01.05 pozisyon metninde sayılan evcil kümes hayvanlarındandır. Sülün, keklik, güvercin ve bıldırcın 01.05’te ismen geçmeyen diğer kuşlar olarak 01.06’da yer alır. Kanatlı ve yenilebilir olmak tek başına 01.05 için yeterli değildir.",
           "01.05 pozisyon metni ve Açıklama Notu; 01.06 Açıklama Notu (C)."))
# 14
S.append(q("Bölüm I notlarına göre, bu bölümde adı geçen belirli bir hayvan cins veya türüne yapılan atıf için aşağıdakilerden hangisi doğrudur?",
           ["*Metinde aksi belirtilmedikçe, o cins veya türün yavrusunu da kapsar.",
            "Yalnızca erişkin hayvanları kapsar; yavrular 01.06’da sınıflandırılır.",
            "Yalnızca evcil hayvanları kapsar; yabani olanlar 01.06’ya girer.",
            "Yavruları ancak ağırlıkları belirli bir sınırı aşmıyorsa kapsar.",
            "Yalnızca damızlık olarak kullanılan hayvanları kapsar."], T_N,
           "Bölüm I Not 1’e göre bir hayvan cins veya türüne yapılan atıf, metinde aksi belirtilmedikçe bu cins veya türün yavrusuna da yapılmış sayılır; bu nedenle tay 01.01’de, kuzu ve oğlak 01.04’te kalır. Not evcil-yabani ayrımı veya ağırlık sınırı getirmez.",
           "Bölüm I Not 1."))
# 15
S.append(q("Bölüm I notlarına göre, metinde aksi belirtilmedikçe Tarifede “kurutulmuş” ürünlere yapılan atıf aşağıdakilerden hangisini de kapsar?",
           ["Tütsülenmiş ürünleri", "*Dondurularak kurutulmuş (liyofilize) ürünleri", "Salamura edilmiş ürünleri", "Tuzlanmış ürünleri", "Pişirilmiş ürünleri"], T_N,
           "Bölüm I Not 2, “kurutulmuş” ürünlere yapılan atfın suyu alınmış, buharlaştırılmış veya dondurularak kurutulmuş (liyofilize) ürünleri de kapsadığını belirtir. Tütsüleme, tuzlama ve salamura ise pozisyon metinlerinde kurutmadan ayrı sayılan işlemlerdir (ör. 02.10, 03.05); pişirme bu nota girmez.",
           "Bölüm I Not 2."))
# 16
S.append(q("Fasıl 1 notuna göre Fasıl 1 dışında bırakılanlar arasında aşağıdakilerden hangisi <b>yer almaz</b>?",
           ["03.01 pozisyonuna giren canlı balıklar",
            "03.06 pozisyonuna giren canlı kabuklu hayvanlar",
            "30.02 pozisyonundaki mikroorganizma kültürleri",
            "95.08 pozisyonundaki hayvanlar",
            "*Balinalar, yunuslar ve foklar gibi deniz memelileri"], T_N,
           "Fasıl 1 Notu yalnızca 03.01, 03.06, 03.07, 03.08’e giren su hayvanlarını, 30.02’deki mikroorganizma kültürlerini ve 95.08’deki hayvanları hariç tutar. Deniz memelileri Fasıl 1 dışında değildir; aksine Fasıl 3 Not 1 ile Fasıl 3’ten çıkarılıp 01.06’da memeliler arasında sayılır.",
           "Fasıl 1 Notu; Fasıl 3 Not 1; 01.06 Açıklama Notu."))
# 17
S.append(q("Fasıl 1 Genel Açıklamalarına göre nakliye sırasında ölen hayvanlar için aşağıdakilerden hangisi doğrudur?",
           ["Ölüm nakliye sırasında gerçekleştiğinden, canlı olarak sevk edildikleri için canlı hayvan pozisyonunda kalırlar.",
            "*İnsan tüketimine uygun eti yenilebilen hayvanlarsa Fasıl 2’deki ilgili pozisyonlarda veya 04.10’da, değilse 05.11’de sınıflandırılırlar.",
            "Türleri ve insan tüketimine uygun olup olmadıkları dikkate alınmaksızın her durumda 05.11 pozisyonunda sınıflandırılırlar.",
            "İnsan tüketimine uygun olsalar bile hayvan beslemede kullanılan ürünler olarak 23.01 pozisyonunda sınıflandırılırlar.",
            "Böcek iseler, ölmüş olsalar da canlı hayvanlar gibi 01.06 pozisyonunda sınıflandırılmaya devam ederler."], T_N,
           "Genel Açıklamalara göre nakliye sırasında ölen böcekler dahil hayvanlar, insan tüketimine uygun eti yenilebilen hayvanlarsa 02.01–02.05, 02.07, 02.08 veya 04.10’da; diğer durumlarda 05.11’de sınıflandırılır. Canlı olmayan hayvan Fasıl 1’de kalmaz; 23.01 ise yenmeyen un, kaba un ve pelletler içindir.",
           "Fasıl 1 Genel Açıklamalar."))
# 18
S.append(q("Canlı tayların 01.01 pozisyonunda sınıflandırılmasının dayanağı aşağıdakilerden hangisidir?",
           ["*GYK 1; pozisyon metni ve Bölüm I Not 1 uyarınca bir türe yapılan atıf yavrusunu da kapsar.",
            "GYK 2(a); tay henüz gelişimini tamamlamamış at sayıldığından tamamlanmış at gibi sınıflandırılır.",
            "GYK 3(a); 01.01 pozisyonu tayları 01.06 pozisyonuna göre daha özel şekilde tanımlar.",
            "GYK 3(b); taya esas niteliğini at türü verdiğinden atın pozisyonunda sınıflandırılır.",
            "GYK 4; taya en çok benzeyen hayvan at olduğundan atın pozisyonunda sınıflandırılır."], T_G,
           "Sınıflandırma GYK 1’e göre pozisyon metni ve notlarla yapılır: 01.01 atları kapsar, Bölüm I Not 1 de türe yapılan atfın yavruyu kapsadığını söyler (01.01 Açıklama Notu tayları ayrıca sayar). GYK 2(a) eksik veya demonte eşya içindir ve normal olarak Bölüm I–VI’ya uygulanmaz; tay iki pozisyona birden girmediğinden GYK 3 ve GYK 4’e de gerek yoktur.",
           "GYK 1; Bölüm I Not 1; 01.01 Açıklama Notu; GYK 2(a) Açıklama Notu (III)."))
# 19
S.append(q("Canlı domuzlar 01.03 pozisyonunda yer alır; pozisyon içinde tek tireli “damızlıklar” ve “diğerleri” alt pozisyonları, “diğerleri” altında ise ağırlığa göre iki tireli alt pozisyonlar bulunur. Damızlık olmayan 80 kg’lık bir canlı domuzun hangi iki tireli alt pozisyona gireceğinin belirlenmesinde esas alınan kural hangisidir?",
           ["GYK 2(a)", "GYK 3(a)", "GYK 3(c)", "GYK 4", "*GYK 6"], T_G,
           "Pozisyon (01.03) belirlendikten sonra alt pozisyon seçimi GYK 6’ya göre yapılır: önce aynı seviyedeki tek tireliler (“damızlıklar” – “diğerleri”), sonra yalnızca seçilen tek tirelinin iki tirelileri karşılaştırılır. Alt pozisyon açıklama notuna göre ağırlık sınırı her bir hayvanın ağırlığıyla ilgilidir. GYK 3(c) ve GYK 4 pozisyonu saptanamayan eşya içindir.",
           "GYK 6; 01.03 pozisyon metni ve alt pozisyon açıklama notu."))
# 20
S.append(q("Aşağıdaki canlı hayvan – pozisyon eşleştirmelerinden hangisi <b>yanlıştır</b>?",
           ["Watussi öküzü – 01.02", "Hindi – 01.05", "Maymun – 01.06", "*Gaur – 01.06", "Kısrak – 01.01"], T_B,
           "Gaur (Bos gaurus), 01.02 Açıklama Notunda Bibos cinsi Asya öküzleri arasında sayılır; doğru pozisyonu 01.02’dir. Watussi öküzü 01.02’de, hindi 01.05’te, maymun 01.06’da, kısrak 01.01’de yer alır. Yabani ve egzotik olması gauru 01.06’ya göndermez.",
           "01.02 Açıklama Notu; 01.01, 01.05 ve 01.06 Açıklama Notları."))
# 21
S.append(q("01.01 açıklama notuna göre katırlar, ........ ile ........ melez döllerdir. Boşlukları doğru tamamlayan seçenek hangisidir?",
           ["aygır – dişi eşek", "erkek eşek – dişi bufalo", "*erkek eşek – kısrak", "aygır – kısrak", "erkek zebra – kısrak"], T_B,
           "01.01 Açıklama Notuna göre katırlar erkek eşek ile kısrağın, bardolar ise aygır ile dişi eşeğin melezleridir; ikisi de 01.01’dedir. “Aygır – dişi eşek” bardonun tanımıdır (tuzak); aygır ile kısrak at, zebra melezleri ise notta sayılmamıştır.",
           "01.01 Açıklama Notu."))
# 22
S.append(q("Tarife Cetveline göre aşağıdaki ifadelerden hangileri doğrudur?  I. Canlı balinalar 01.06 pozisyonunda sınıflandırılır.  II. Canlı karidesler canlı hayvan oldukları için Fasıl 1’de sınıflandırılır.  III. Canlı kurbağalar 01.06 pozisyonunda sınıflandırılır.  IV. Nakliye sırasında ölen, eti yenilebilir kümes hayvanları 01.05 pozisyonunda kalır.",
           ["I ve II", "*I ve III", "II ve IV", "I, III ve IV", "II, III ve IV"], T_C,
           "I doğrudur: balinalar deniz memelisi olarak 01.06’dadır. III doğrudur: kurbağalar 01.06’da “diğerleri” arasında sayılır. II yanlıştır: canlı kabuklular Fasıl 1 Notu gereği 03.06’dadır. IV yanlıştır: nakliyede ölen yenilebilir kümes hayvanı 02.07’ye gider.",
           "Fasıl 1 Notu; Fasıl 1 Genel Açıklamalar; 01.06 Açıklama Notu."))
# 23
S.append(q("Aşağıdaki ifadelerden hangileri doğrudur?  I. Bölüm I’de bir hayvan türüne yapılan atıf, metinde aksi belirtilmedikçe o türün yavrusunu da kapsar.  II. Fasıl 1 yalnızca gıda amacıyla ticarete konu olan canlı hayvanları kapsar.  III. Canlı arılar seyyar kutu, kafes veya kovan içinde sunulsalar da 01.06’da sınıflandırılır.  IV. 30.02 pozisyonundaki mikroorganizma kültürleri Fasıl 1’in kapsamı dışındadır.",
           ["I ve III", "II ve IV", "I, II ve III", "*I, III ve IV", "I, II, III ve IV"], T_C,
           "I Bölüm I Not 1’e, III 01.06 Açıklama Notuna (D), IV Fasıl 1 Notuna uygundur. II yanlıştır: Genel Açıklamalara göre fasıl canlı hayvanları gıda veya diğer amaçlar için olsun kapsar.",
           "Bölüm I Not 1; Fasıl 1 Notu ve Genel Açıklamalar; 01.06 Açıklama Notu (D)."))
# 24
S.append(q("Bir çiftlik, kürkleri için yetiştirdiği tilki ve gelincikleri havalandırmalı kafeslerde canlı olarak ihraç etmektedir; hayvanların postları varış ülkesinde işlenecektir. Bu hayvanlar hangi pozisyonda sınıflandırılır?",
           ["01.02", "01.04", "*01.06", "43.01", "95.08"], T_S,
           "01.06 Açıklama Notu tilkileri, gelincikleri ve kürk elde etmek için yetiştirilen diğer çiftlik hayvanlarını memeliler arasında sayar. Kürk amacı hayvanı ham kürk pozisyonuna (43.01) göndermez; hayvan canlı olarak sunulmaktadır. Sirk veya gezici gösteri söz konusu olmadığından 95.08 uygulanmaz.",
           "01.06 Açıklama Notu (A); Fasıl 1 Genel Açıklamalar."))
# 25
S.append(q("Gezici bir sirkin gösterilerinde yer alan atlar, filler ve köpekler, bir sonraki gösteri için sirkin diğer donanımıyla birlikte sınırdan geçirilmektedir. Bu hayvanların sınıflandırılmasıyla ilgili aşağıdakilerden hangisi doğrudur?",
           ["Atlar 01.01’de, filler ve köpekler 01.06’da sınıflandırılır.",
            "Tümü canlı hayvan olduğundan 01.06’da sınıflandırılır.",
            "Atlar 01.01’de, filler ve köpekler 95.08’de sınıflandırılır.",
            "Tümü GYK 3(b) uyarınca sirk donanımıyla birlikte perakende takım olarak sınıflandırılır.",
            "*Tümü, Fasıl 1 notu gereğince Fasıl 1 dışında kalarak 95.08’de sınıflandırılır."], T_S,
           "Fasıl 1 Notu 95.08’deki hayvanları hariç tutar; Genel Açıklamalara göre sirk, hayvan sergileri veya benzeri gezici hayvan gösterilerinde yer alan hayvanlar türüne bakılmaksızın 95.08’dedir. Atın ayrıca 01.01’de sayılması bu hükmü değiştirmez. Sınıflandırma not hükmüne (GYK 1) dayanır; perakende takım söz konusu değildir.",
           "Fasıl 1 Notu ve Genel Açıklamalar; 01.06 Açıklama Notu."))

modul["sorular"] = S
yaz(1, modul)
