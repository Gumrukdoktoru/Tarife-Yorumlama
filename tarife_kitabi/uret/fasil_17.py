from yardim_14_18 import q, yaz

T_E = "Eşya → 4’lü pozisyon"
T_O = "Olumsuz teşhis"
T_F = "Farklı/aynı pozisyon veya fasıl"
T_N = "Fasıl notu · Tanım/Eşik"
T_G = "Genel Yorum Kuralı"
T_B = "Eşleştirme / Boşluk doldurma"
T_C = "Çoktan-çoğa (I–IV)"
T_S = "Senaryo"

sorular = [
    # 1
    q("Tarife Cetveline göre, kakao içermeyen, şekerle kaplanmış ciklet hangi pozisyonda sınıflandırılır?",
      "17.04", ["18.06", "21.06", "17.02", "19.05"], "E", T_E,
      "17.04 kakao içermeyen şeker mamullerini kapsar; açıklama notu şekerli sakızları (tatlandırılmış ciklet ve benzerleri) açıkça sayar. Kakao içerseydi 18.06’ya; şeker yerine sorbitol gibi sentetik tatlandırıcı içerseydi 21.06’ya giderdi. Şekerle kaplanmış olması 17.04’ü değiştirmez.",
      "17.04 pozisyon metni ve Açıklama Notu."),
    # 2
    q("Aşağıdakilerden hangisi Tarife Cetvelinin 17. faslında <b>sınıflandırılmaz</b>?",
      "Çikolatalı nuga", ["Türk lokumu", "Badem ezmesi (marzipan)", "Karamel", "Doğal bala dayalı, şekercilik mamulü formunda helva"], "C", T_O,
      "Fasıl 17 Not 1(a) kakao içeren şeker mamullerini 18.06’ya gönderir; 18.06 açıklama notu çikolatalı nugayı açıkça sayar. Türk lokumu, marzipan ve bala dayalı helva 17.04’te, karamel 17.02’de (şekerleme olarak karameller 17.04’te) yer alır; hepsi Fasıl 17’dedir.",
      "Fasıl 17 Not 1(a); 17.04 ve 18.06 Açıklama Notları."),
    # 3
    q("Tarife Cetvelinin 17. Fasıl notlarına göre, aşağıdaki kimyaca saf şekerlerden hangileri 29.40 pozisyonuna gitmeyip Fasıl 17’de kalır?",
      "Sakkaroz, laktoz, maltoz, glikoz ve fruktoz",
      ["Yalnızca sakkaroz", "Sakkaroz, laktoz ve maltoz", "Yalnızca glikoz ve fruktoz", "Kimyaca saf şekerlerin tamamı 29.40’ta yer alır"], "A", T_N,
      "Fasıl 17 Not 1(b), sakkaroz, laktoz, maltoz, glikoz ve fruktoz hariç kimyaca saf şekerleri fasıl dışında bırakır (29.40). Kimyaca saf katı sakkaroz 17.01’de, kimyaca saf laktoz, maltoz, glikoz ve fruktoz 17.02’de yer alır.",
      "Fasıl 17 Not 1(b); 17.01 ve 17.02 pozisyon metinleri."),
    # 4
    q("Tarife Cetveline göre, akçaağaç ağacının özsuyunun rafine edilmeden konsantre edilip kristalleştirilmesiyle elde edilen katı akçaağaç şekeri hangi pozisyonda yer alır?",
      "17.02", ["17.01", "13.02", "21.06", "17.04"], "D", T_E,
      "17.01 yalnız kamış veya pancar şekeri ile kimyaca saf sakkarozu kapsar. Şeker pancarı ve kamışı dışındaki bitkilerden elde edilen sakkaroz şekerleri (en önemlisi akçaağaç şekeri) 17.02 açıklama notunda “diğer şekerler” arasında sayılmıştır. 13.02 bitkisel özsu ve hülasalar içindir; burada ürün kristal şekerdir.",
      "17.01 ve 17.02 Açıklama Notları."),
    # 5
    q("Tarife Cetveline göre aşağıdakilerden hangisi diğerlerinden farklı bir tarife pozisyonunda yer alır?",
      "Esmer şeker", ["Glikoz şurubu", "Fruktoz şurubu", "İnvert şeker şurubu", "Akçaağaç şurubu"], "B", T_F,
      "Glikoz, fruktoz, invert şeker ve akçaağaç şurupları ilave aroma ve renk verici içermedikçe 17.02’deki şeker şuruplarıdır. Esmer şeker ise az miktarda karamel veya melasla karışık beyaz şekerden oluşan katı şeker olarak 17.01 açıklama notunda sayılmıştır.",
      "17.01 ve 17.02 Açıklama Notları."),
    # 6
    q("Tarife Cetveline göre aşağıdakilerden hangileri 17.04 pozisyonunda sınıflandırılır?  I. Doğal bala dayalı, şekercilik mamulü formunda helva  II. Badem ezmesi (marzipan)  III. Meyve reçeli  IV. Yalnızca şeker ve mentolden oluşan boğaz pastili",
      "I, II ve IV", ["I ve III", "II ve III", "Yalnız IV", "III ve IV"], "B", T_C,
      "17.04 açıklama notu bala dayalı şekercilik mamulü formundaki müstahzarları (helva), badem ezmesini ve esası şeker ile aroma maddelerinden (mentol vb.) oluşan boğaz pastillerini sayar (I, II, IV). Meyve reçelleri ise hariç tutulmuştur; 20.07’de yer alır (III).",
      "17.04 Açıklama Notu ve hariç tutmaları."),
    # 7
    q("Tarife Cetveline göre, şeker pancarından şeker çıkarılması sırasında yan ürün olarak elde edilen, kolayca kristalleştirilemeyen şeker içeren koyu kahverengi melas hangi pozisyonda sınıflandırılır?",
      "17.03", ["17.02", "23.03", "21.06", "17.01"], "E", T_E,
      "17.03, yalnızca şeker ekstraksiyonu veya rafinasyonu sonucunda elde edilen melasları kapsar; pancar melası normalde yenilmeye elverişli olmasa da buradadır. 23.03 şeker pancarının etli kısımları ve kamış bagası gibi şeker sanayii artıklarını kapsar; melas ise ismen 17.03’te belirtilmiştir.",
      "17.03 pozisyon metni ve Açıklama Notu."),
    # 8
    q("Aşağıdakilerden hangisi Tarife Cetvelinin 17.02 pozisyonunda <b>sınıflandırılmaz</b>?",
      "Kimyaca saf katı sakkaroz",
      ["Kuru madde üzerinden %99 laktoz içeren ticari laktoz", "Glikoz şurubu", "Tabii bal ile karıştırılmış suni bal", "Kimyaca saf fruktoz"], "A", T_O,
      "17.01 pozisyon metni kimyaca saf katı sakkarozu (menşei ne olursa olsun) kapsar; bu nedenle 17.02’de değil 17.01’dedir. Laktoz, glikoz şurubu, suni bal (tabii bal ile karışık olsa da) ve kimyaca saf fruktoz 17.02’de sayılmıştır.",
      "17.01 pozisyon metni ve Açıklama Notu; 17.02 pozisyon metni."),
    # 9
    q("Tarife Cetveline göre aşağıdakilerden hangisi diğerlerinden farklı bir fasılda yer alır?",
      "Çikolata kaplı badem şekeri", ["Şekerle kaplanmış ciklet", "Fındıklı Türk lokumu", "Kakao yağı içeren beyaz çikolata", "Beyaz badem şekeri"], "C", T_F,
      "Ciklet, Türk lokumu, beyaz çikolata ve badem şekeri kakao içermeyen şeker mamulleri olarak 17.04’tedir (beyaz çikolatadaki kakao yağı kakao sayılmaz). Çikolata ile kaplanmış badem şekeri ise kakao içerdiğinden Fasıl 17 Not 1(a) gereği 18.06’dadır (Fasıl 18).",
      "Fasıl 17 Not 1(a); 17.04 Açıklama Notu."),
    # 10
    q("Tarife Cetveline göre, şeker, kakao yağı, süt tozu ve aroma verici maddelerden oluşan, eser miktardan fazla kakao içermeyen tablet halindeki beyaz çikolata hangi pozisyonda yer alır?",
      "17.04", ["18.06", "18.04", "19.01", "21.06"], "D", T_E,
      "17.04 pozisyon metni beyaz çikolatayı ismen kapsar; açıklama notuna göre kakao yağı kakao olarak mütalaa edilmez. Fasıl 18 genel açıklamaları ve 18.06 açıklama notu da beyaz çikolatayı hariç tutar. 18.04 tek başına kakao yağı içindir.",
      "17.04 pozisyon metni ve Açıklama Notu; 18.06 Açıklama Notu."),
    # 11
    q("Aşağıdakilerden hangisi Tarife Cetvelinin 17.04 pozisyonunda <b>sınıflandırılmaz</b>?",
      "Şekerle kaplanarak kristalleştirilmiş portakal kabuğu",
      ["Bonbon", "Fondan", "Yalnızca şeker ve aroma maddesi içeren öksürük pastili", "Şekerli sakız"], "C", T_O,
      "17.04 açıklama notu, şekerle muhafaza edilen sebze, meyve ve meyve kabuklarını hariç tutar; bunlar 20.06’dadır. Bonbon, fondan, şekerli sakız ve tıbbi madde içermeyen (yalnız aromalı) öksürük pastilleri 17.04’te açıkça sayılmıştır.",
      "17.04 Açıklama Notu (hariç tutmalar)."),
    # 12
    q("Açıklama notlarına göre, peynir altı suyundan elde edilen laktozun 17.02 pozisyonunda sınıflandırılabilmesi için kuru madde üzerinden hesaplandığında ağırlık itibariyle ne kadar laktoz (susuz laktoz olarak) içermesi gerekir?",
      "%95’ten fazla", ["%99 veya daha fazla", "%80’den fazla", "%95 veya daha az", "%50’den fazla"], "B", T_N,
      "17.02 açıklama notuna göre bu ürünler kuru madde üzerinden ağırlıkça %95’ten fazla susuz laktoz içermelidir; %95 veya daha az laktoz içeren peynir altı suyu ürünleri genellikle 04.04’tedir. %99 eşiği yalnızca bir alt pozisyon ayrımıdır, pozisyona giriş şartı değildir (tuzak).",
      "17.02 Açıklama Notu; Fasıl 4 Not 5."),
    # 13
    q("Tarife Cetvelinin 17. faslı ile ilgili aşağıdaki ifadelerden hangileri doğrudur?  I. Fasıldaki katı şekerler, şeker karakterini korudukça aspartam veya stevia gibi yapay tatlandırıcılar içerebilir.  II. Kakao içeren şeker mamulleri, kakao oranı düşükse 17.04’te kalır.  III. Tatlandırılmış hayvan yemleri 17.02’de yer alır.  IV. 17.01’deki pancar ve kamış şekeri yalnızca katı haldeki ürünleri kapsar.",
      "I ve IV", ["I ve II", "II ve III", "I, II ve IV", "III ve IV"], "E", T_C,
      "Genel açıklamalara göre katı şekerler ve melaslar şeker karakterini korudukça renk, aroma veya yapay tatlandırıcı içerebilir (I doğru). Kakao hangi oranda olursa olsun 18.06’ya götürür (II yanlış). Tatlandırılmış hayvan yemleri 23.09’dadır (III yanlış). 17.01 yalnız katı (toz dahil) şekerleri kapsar (IV doğru).",
      "Fasıl 17 Genel Açıklamalar; 17.01 Açıklama Notu."),
    # 14
    q("Tarife Cetveline göre, şeker hastaları için üretilmiş, şeker yerine sorbitol içeren şekersiz sakız hangi pozisyonda sınıflandırılır?",
      "21.06", ["17.04", "17.02", "18.06", "19.05"], "A", T_E,
      "17.04 açıklama notu, şeker yerine sentetik tatlandırıcı maddeler (sorbitol gibi) içeren tatlıları ve sakızları (özellikle şeker hastaları için) hariç tutarak 21.06’ya gönderir. Ürün “ciklet” olsa da şeker mamulü sayılmaz. Kakao içermediğinden 18.06 da söz konusu değildir.",
      "17.04 Açıklama Notu (hariç tutmalar)."),
    # 15
    q("17.02 açıklama notuna göre malto-dekstrinlerin bu pozisyonda yer alabilmesi için kuru madde üzerinden dekstroz olarak ifade edilen indirgen şeker oranı ne olmalıdır?",
      "%10’dan fazla (fakat %20’den az)", ["%10 veya daha az", "%20 veya daha fazla", "%5’ten fazla (fakat %10’dan az)", "%50’den fazla"], "D", T_N,
      "17.02 açıklama notu, pozisyonun yalnızca %10’dan fazla (fakat %20’den az) indirgen şeker içeren malto-dekstrinleri kapsadığını, %10’u geçmeyenlerin 35.05’te yer aldığını belirtir. %20 ve üzeri indirgen şeker ise ticari glikozun özelliğidir.",
      "17.02 Açıklama Notu; Fasıl 35 Not 2."),
    # 16
    q("Aşağıdakilerden hangisi Tarife Cetvelinin 17. faslında <b>yer almaz</b>?",
      "Kuru madde üzerinden %8 indirgen şeker içeren dekstrin",
      ["Karamelize şeker", "Golden şurup", "İnvert şeker", "Kuru madde üzerinden %15 indirgen şeker içeren malto-dekstrin"], "D", T_O,
      "İndirgen şeker oranı %10’u geçmeyen ürünler dekstrin olarak 35.05’tedir. Karamelize şeker, golden şurup, invert şeker ve %10’dan fazla (fakat %20’den az) indirgen şeker içeren malto-dekstrin 17.02’de yer alır.",
      "17.02 Açıklama Notu; Fasıl 35 Not 2."),
    # 17
    q("17.04 açıklama notuna göre, şekercilik mamulü halinde olmayan meyan kökü hülasası hangi durumda 17.04 pozisyonunda sınıflandırılır?",
      "Ağırlık itibariyle %10’dan fazla sakkaroz içeriyorsa",
      ["Ağırlık itibariyle %5’ten fazla sakkaroz içeriyorsa", "Ağırlık itibariyle %20’den fazla sakkaroz içeriyorsa", "Ağırlık itibariyle %10 veya daha az sakkaroz içeriyorsa", "Şeker oranına bakılmaksızın her durumda"], "A", T_N,
      "17.04 açıklama notu, ağırlık itibariyle %10’dan fazla sakkaroz içeren meyan kökü hülasasını (kalıp, blok, çubuk vb.) 17.04’e alır; %10 veya daha az şekerli olanlar şekercilik mamulü değilse 13.02’dedir. Şeker oranına bakılmaması yalnız şekercilik mamulü halindekiler için geçerlidir (tuzak).",
      "17.04 Açıklama Notu; 13.02 pozisyonu."),
    # 18
    q("Tarife Cetveline göre aşağıdaki eşya çiftlerinden hangisinde her iki eşya da aynı pozisyonda yer alır?",
      "Suni bal – karamel",
      ["Tabii bal – suni bal", "Aromasız glikoz şurubu – aroma katılmış glikoz şurubu", "Kimyaca saf sakkaroz – kimyaca saf laktoz", "Pancar şekeri – pancar melası"], "C", T_F,
      "Suni bal ve karamel 17.02 pozisyon metninde birlikte sayılmıştır. Tabii bal 04.09 – suni bal 17.02; aromasız şurup 17.02 – aromalı şurup 21.06; saf sakkaroz 17.01 – saf laktoz 17.02; pancar şekeri 17.01 – pancar melası 17.03’tür.",
      "17.01, 17.02 ve 17.03 pozisyon metinleri; 04.09 Açıklama Notu."),
    # 19
    q("Esası glikoz ve invert şeker olan, tabii balı taklit etmek amacıyla aroma ve renk verici maddeler katılmış, ayrıca bir miktar tabii bal da içeren koyu kıvamlı bir karışım kavanozlarda perakende satılmaktadır. Tarife Cetveline göre bu eşya hangi pozisyonda sınıflandırılır?",
      "17.02", ["04.09", "21.06", "17.04", "17.03"], "E", T_S,
      "17.02 açıklama notuna göre suni bal, esası sakkaroz, glikoz veya invert şeker olan ve tabii balı taklit maksadıyla aroma ve renk verici maddeler katılmış karışımlardır; tabii ve suni bal karışımları da bu pozisyona dahildir. 04.09 yalnız katkısız tabii balı kapsar; 04.09 açıklama notu suni balı 17.02’ye gönderir.",
      "17.02 pozisyon metni ve Açıklama Notu; 04.09 Açıklama Notu."),
    # 20
    q("Tabii bal ile karıştırılmış suni bal, 17.02 pozisyon metninde “suni bal (tabii bal ile karıştırılmış olsun olmasın)” ifadesiyle açıkça yer aldığından 17.02’de sınıflandırılır. Bu sınıflandırmada aşağıdaki Genel Yorum Kurallarından hangisi esas alınır?",
      "GYK 1", ["GYK 2(b)", "GYK 3(b)", "GYK 3(c)", "GYK 4"], "B", T_G,
      "Karışım pozisyon metninde açıkça tarif edildiğinden sınıflandırma GYK 1’e (pozisyon metinleri ve notlar) göre yapılır. GYK 2(b) açıklama notu da bir pozisyon metninde belirtilen hazır karışımların 1 No.lu Kurala göre sınıflandırılacağını söyler. 3(b) ve 3(c) ancak eşya ilk bakışta birden fazla pozisyona girebiliyorsa uygulanır.",
      "GYK 1; GYK 2(b) Açıklama Notu (X); 17.02 pozisyon metni."),
    # 21
    q("Tarife Cetveline göre, kamış ve pancardan elde edilen sulu şeker çözeltilerinden ibaret şeker şurupları, ilave renk ve aroma verici madde içermiyorsa …… pozisyonunda, içeriyorsa …… pozisyonunda yer alır. Boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?",
      "17.02 – 21.06", ["17.01 – 21.06", "17.02 – 17.04", "17.03 – 21.06", "21.06 – 17.02"], "A", T_B,
      "17.01 açıklama notu açıktır: kamış ve pancardan elde edilen sulu şeker çözeltilerinden ibaret şeker şurupları ilave renk ve aroma verici içermemeleri halinde 17.02’de, aksi halde 21.06’da yer alır. 17.01 yalnız katı şekeri kapsar; katı şekerde aroma ve renk pozisyonu değiştirmez.",
      "17.01 Açıklama Notu; 17.02 pozisyon metni."),
    # 22
    q("Tarife Cetveline göre aşağıdaki eşya – pozisyon eşleştirmelerinden hangisi <b>yanlıştır</b>?",
      "Kakaolu şekerleme – 17.04",
      ["Kimyaca saf fruktoz – 17.02", "Karamel – 17.02", "Kamış melası – 17.03", "Beyaz çikolata – 17.04"], "E", T_B,
      "Kakao içeren şeker mamulleri Fasıl 17 Not 1(a) gereği 18.06’dadır; 17.04 başlığı da “kakao içermeyen” şeker mamullerini kapsar. Saf fruktoz ve karamel 17.02, kamış melası 17.03, beyaz çikolata 17.04 eşleştirmeleri doğrudur.",
      "Fasıl 17 Not 1(a); 17.02, 17.03 ve 17.04 pozisyon metinleri."),
    # 23
    q("Tarife Cetveline göre aşağıdaki aromalı veya renkli şeker ürünlerinden hangisi diğerlerinden farklı bir pozisyonda yer alır?",
      "Aroma katılmış pancar şekeri şurubu",
      ["Aroma verici madde katılmış küp şeker", "Vanilya ile aromalandırılmış toz şeker", "Renk verici katılmış kristal şeker", "Karamel ile karışık esmer şeker"], "D", T_F,
      "17.01’deki katı pancar ve kamış şekerlerine aroma veya renk verici maddeler katılmış olabilir; küp, vanilyalı toz, renkli kristal ve esmer şeker 17.01’dedir. Aroma katılmış şeker şurubu ise 17.01 açıklama notu gereği 21.06’ya gider. Ayrımı fiziksel hal (katı – şurup) belirler.",
      "17.01 Açıklama Notu."),
    # 24
    q("Hediye olarak hazırlanmış bir karton kutuda bir paket Türk lokumu ile bir adet porselen kahve fincanı birlikte perakende satışa sunulmuştur. Bu eşyanın sınıflandırılmasında aşağıdakilerden hangisi doğrudur?",
      "Takım sayılmaz; lokum ve fincan kendi uygun pozisyonlarında ayrı ayrı sınıflandırılır.",
      ["GYK 3(b) uyarınca takım olarak lokumun pozisyonunda (17.04) sınıflandırılır.",
       "GYK 3(b) uyarınca takım olarak fincanın pozisyonunda sınıflandırılır.",
       "GYK 3(c) uyarınca numara sırasına göre sonuncu pozisyonda sınıflandırılır.",
       "GYK 5(b) uyarınca karton kutu ile birlikte kutunun pozisyonunda sınıflandırılır."], "B", T_G,
      "GYK 3(b) açıklama notuna göre takım, özel bir gereksinmeyi karşılamak veya belirli bir işlevi yerine getirmek üzere bir araya getirilmiş eşyadan oluşmalıdır. Açıklama notu, hazır kahve kavanozu ile seramik fincanın birlikte sunulmasını takım saymaz; lokum ile fincan da böyledir. Lokum 17.04’te, fincan kendi pozisyonunda ayrı sınıflandırılır.",
      "GYK 3(b) Açıklama Notu (X)."),
    # 25
    q("Peynir altı suyundan elde edilmiş, kuru madde üzerinden ağırlıkça %97 laktoz (susuz laktoz olarak) içeren beyaz toz halinde bir ürün, bebek maması üretiminde kullanılmak üzere ithal edilmiştir. Tarife Cetveline göre bu eşya hangi pozisyonda sınıflandırılır?",
      "17.02", ["04.04", "29.40", "19.01", "35.02"], "C", T_S,
      "Kuru madde üzerinden ağırlıkça %95’ten fazla laktoz içeren peynir altı suyu ürünleri 17.02’dedir; %97 bu eşiği aşar. %95 veya daha az laktoz içerseydi genellikle 04.04’te kalırdı. Laktoz Not 1(b)’deki istisnalardan olduğu için 29.40’a gitmez; kullanım amacı (bebek maması) sınıflandırmayı değiştirmez.",
      "17.02 Açıklama Notu; Fasıl 17 Not 1(b); Fasıl 4 Not 5."),
]

obj = {
    "tur": "fasil",
    "fasil": 17,
    "baslik": "Şeker ve şeker mamulleri",
    "bolum": "IV",
    "oz": {
        "vurgu": "Fasıl 17 şekeri dört basamakta ele alır: katı kamış-pancar şekeri ve kimyaca saf sakkaroz 17.01; diğer şekerler, aromasız şeker şurupları, suni bal ve karamel 17.02; şeker üretiminin yan ürünü melas 17.03; kakao içermeyen şeker mamulleri (beyaz çikolata dahil) 17.04. En önemli sınır kakaodur: hangi oranda olursa olsun kakao içeren şeker mamulü 18.06’ya gider.",
        "maddeler": [
            "Katı şekerler ve melaslar şeker karakterini korudukça renk, aroma (sitrik asit, vanilya) veya yapay tatlandırıcı (aspartam, stevia) içerebilir.",
            "Şeker şurubu: ilave aroma veya renk verici yoksa 17.02; varsa 21.06.",
            "Kimyaca saf şekerlerden yalnız sakkaroz (17.01) ile laktoz, maltoz, glikoz, fruktoz (17.02) Fasıl 17’de kalır; diğerleri 29.40.",
            "Şekerli her gıda Fasıl 17 değildir: şekerlenmiş meyve 20.06, reçel 20.07, sorbitollü şekerleme 21.06, tıbbi pastil Fasıl 30.",
        ],
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Kakao veya çikolata içeriyor mu? (beyaz çikolata hariç; kakao yağı kakao sayılmaz)", "<b>18.06</b>"],
            ["2", "Tedavi edici veya koruyucu dozda tıbbi madde içeren pastil ya da şekerli ilaç mı?", "Fasıl 30"],
            ["3", "Sakkaroz, laktoz, maltoz, glikoz ve fruktoz dışında kimyaca saf şeker mi?", "<b>29.40</b>"],
            ["4", "Şekerle muhafaza edilmiş meyve-kabuk ya da reçel, jöle, marmelat mı?", "<b>20.06</b> / <b>20.07</b>"],
            ["5", "Şeker yerine sorbitol gibi sentetik tatlandırıcı içeren tatlı-sakız ya da çok yağlı şeker ezmesi mi?", "<b>21.06</b>"],
            ["6", "Olduğu gibi yenmeye hazır şeker müstahzarı mı? (şekerleme, ciklet, lokum, marzipan, helva, beyaz çikolata)", "<b>17.04</b>"],
            ["7", "Şeker ekstraksiyonu veya rafinajından elde edilen melas mı?", "<b>17.03</b>"],
            ["8", "Katı kamış veya pancar şekeri ya da kimyaca saf katı sakkaroz mu?", "<b>17.01</b>"],
            ["9", "Diğer katı şeker*, aromasız şeker şurubu, suni bal veya karamel mi?", "<b>17.02</b> (aromalı-renkli şurup <b>21.06</b>)"],
        ],
        "dipnot": "* Laktoz: kuru madde üzerinden %95’ten fazla laktoz 17.02, %95 veya daha az genellikle 04.04. Malto-dekstrin: indirgen şeker %10’dan fazla 17.02, %10 veya daha az 35.05.",
    },
    "pozisyon_haritasi": [
        ["17.01", "Kamış veya pancar şekeri; kimyaca saf sakkaroz (katı)", "Yalnız katı halde; aroma veya renk katılmış olabilir", "Toz şeker, küp şeker, esmer şeker, ham şeker"],
        ["17.02", "Diğer şekerler; aromasız şeker şurupları; suni bal; karamel", "Laktoz, glikoz, fruktoz, maltoz, akçaağaç şekeri", "Glikoz şurubu, akçaağaç şurubu, suni bal"],
        ["17.03", "Melaslar", "Şeker ekstraksiyonu veya rafinajı yan ürünü", "Kamış melası, pancar melası"],
        ["17.04", "Kakao içermeyen şeker mamulleri (beyaz çikolata dahil)", "Olduğu gibi yenmeye hazır şekerlemeler", "Ciklet, lokum, bonbon, marzipan, beyaz çikolata"],
    ],
    "notlar": [
        ["Fasıl 17 Not 1", "Fasıl 17 kapsamaz: (a) kakao içeren şeker mamulleri (18.06); (b) kimyaca saf şekerler (sakkaroz, laktoz, maltoz, glikoz ve fruktoz hariç) veya 29.40’taki diğer ürünler; (c) Fasıl 30’daki ilaçlar ve diğer ürünler."],
        ["Genel Açıklamalar", "Fasıl yalnız şekerleri değil şeker şuruplarını, suni balı, karamelize şekerleri ve melasları da kapsar. Katı şeker ve melaslar şeker veya melas karakterini korudukça renk verici, aroma verici (sitrik asit, vanilya) veya yapay tatlandırıcı (aspartam, stevia) içerebilir. Hariç: hangi oranda olursa olsun kakao veya çikolata (beyaz çikolata hariç) içeren şeker mamulleri ve tatlandırılmış kakao tozları (18.06); Fasıl 19–22’deki tatlandırılmış müstahzarlar; tatlandırılmış hayvan yemleri (23.09)."],
        ["17.01 Açıklama Notu", "Yalnız katı haldeki (toz dahil) kamış ve pancar şekeri; esmer şeker ve iri kristalli şekerlemeler dahil. Ham şeker: kuru halde sakkaroz miktarı polarimetre okuması olarak 99,5°’den az. Kamış ve pancar şurupları aromasız ise 17.02, aromalı veya renkli ise 21.06. İçecek yapımında kullanılan, şeker karakterini kaybetmiş katı müstahzarlar 21.06. Menşei ne olursa olsun kimyaca saf katı sakkaroz 17.01; pancar ve kamış dışındaki kaynaklardan sakkaroz (saf olmayan) 17.02."],
        ["17.02 Açıklama Notu", "Laktoz kuru madde üzerinden ağırlıkça <b>%95’ten fazla</b> (susuz) laktoz içermelidir; %95 veya daha az laktozlu peynir altı suyu ürünleri genellikle 04.04. İnvert şeker eşit oranda glikoz ve fruktozdan oluşur. Ticari glikoz en az %20 indirgen şeker içerir. Malto-dekstrinler: indirgen şeker <b>%10’dan fazla</b> (fakat %20’den az) olanlar 17.02; %10’u geçmeyenler 35.05."],
        ["17.02 Açıklama Notu", "Şeker şurupları ilave aroma ve renk verici katılmamışsa 17.02’dedir (basit şuruplar, golden şurup dahil). Suni bal: esası sakkaroz, glikoz veya invert şeker olan, tabii balı taklit için aroma ve renk verici katılmış karışımlar; tabii bal ile karışımları dahil. Karamel: şeker veya melasın 120–180 °C’de uzun süre ısıtılmasıyla elde edilir."],
        ["17.03 Açıklama Notu", "Melas yalnızca şeker ekstraksiyonu veya rafinasyonunun sonucu olarak elde edilir (kamış veya pancar şekeri, mısırdan fruktoz imalatı). Rengi giderilmiş, renklendirilmiş veya aromalandırılmış olabilir; toz haline getirilebilir."],
        ["17.04 Açıklama Notu", "Olduğu gibi yenmeye elverişli katı veya yarı katı şeker müstahzarları: şekerli sakızlar, bonbonlar, karameller, pastiller, nugalar, fondanlar, badem şekerleri, Türk lokumu, marzipan, yalnız aroma maddeli boğaz pastilleri, beyaz çikolata, şeker mamulü halinde meyve jöleleri, fondan ve nuga ezmeleri, bala dayalı şekercilik müstahzarları (helva)."],
        ["17.04 Açıklama Notu", "Meyan kökü hülasası ağırlıkça <b>%10’dan fazla</b> sakkaroz içeriyorsa 17.04; şekercilik mamulü halindeyse şeker oranına bakılmaz; %10 veya daha az şekerli ve şekerleme halinde olmayan hülasa 13.02. Hariç: kakaolu şekerlemeler 18.06; şekerle muhafaza edilen meyve ve kabuklar 20.06; reçel ve pelteler 20.07; sentetik tatlandırıcılı tatlılar ve çok yağlı şeker ezmeleri 21.06; tıbbi dozda pastiller Fasıl 30."],
    ],
    "sinir_komsulari": [
        ["Çikolata, kakaolu şekerleme, tatlandırılmış kakao tozu", "18.06", "Fasıl 17 Not 1(a)"],
        ["Katkısız tabii bal", "04.09", "Suni bal ve karışımları ise 17.02"],
        ["%95 veya daha az laktozlu peynir altı suyu ürünü", "04.04", "17.02 laktoz eşiği"],
        ["Diğer kimyaca saf şekerler", "29.40", "Fasıl 17 Not 1(b)"],
        ["Aroma veya renk katılmış şeker şurubu", "21.06", "17.01 Açıklama Notu"],
        ["İçecek yapımına mahsus, şeker karakterini kaybetmiş katı müstahzar", "21.06", "17.01 Açıklama Notu"],
        ["Sorbitol gibi sentetik tatlandırıcılı şekerleme ve sakız", "21.06", "17.04 hariç tutması"],
        ["İndirgen şekeri %10’u geçmeyen dekstrin", "35.05", "17.02 Açıklama Notu"],
        ["%10 veya daha az şekerli meyan kökü hülasası", "13.02", "17.04 hariç tutması"],
        ["Şekerle muhafaza edilmiş (şekerlenmiş) meyve ve kabuklar", "20.06", "17.04 hariç tutması"],
        ["Reçel, jöle, marmelat", "20.07", "17.04 hariç tutması"],
        ["Tedavi edici dozda tıbbi madde içeren pastil", "Fasıl 30", "Fasıl 17 Not 1(c)"],
        ["Şeker pancarı, şeker kamışı", "12.12", "Hammadde"],
        ["Şeker pancarı posası, kamış bagası", "23.03", "Şeker sanayii artığı; melas ise 17.03"],
        ["Tatlandırılmış hayvan yemleri", "23.09", "Fasıl 17 Genel Açıklamalar"],
    ],
    "tuzaklar": [
        "<b>Beyaz çikolata çikolata sayılmaz.</b> Şeker, kakao yağı ve süt tozundan oluşur; kakao yağı kakao sayılmadığından 17.04’tedir. Eser miktardan fazla kakao içerirse 18.06.",
        "<b>Kakao “hangi oranda olursa olsun” belirleyicidir.</b> Çok az kakao içeren şekerleme ya da çikolata kaplı badem şekeri 18.06’dadır.",
        "<b>Katıda aroma serbest, şurupta değil.</b> Aroma veya renk katılmış katı şeker 17.01’de kalır; aroma veya renk katılmış şeker şurubu 21.06’ya gider.",
        "<b>Saf şeker her zaman Fasıl 29 değildir.</b> Kimyaca saf sakkaroz 17.01; saf laktoz, maltoz, glikoz, fruktoz 17.02; yalnız diğer saf şekerler 29.40.",
        "<b>Sakkarozun kaynağı önemlidir.</b> Pancar ve kamış şekeri 17.01; akçaağaç, tatlı sorgum, palmiye gibi diğer kaynaklardan sakkaroz 17.02.",
        "<b>Laktozda eşik %95.</b> Kuru madde üzerinden %95’ten fazla laktoz 17.02; %95 veya daha az ise genellikle 04.04. %99 yalnız alt pozisyon ayrımıdır.",
        "<b>Malto-dekstrinde eşik %10.</b> İndirgen şeker %10’dan fazla 17.02; %10 veya daha az dekstrin olarak 35.05.",
        "<b>Meyan kökü hülasası şeker oranına göre ayrılır.</b> %10’dan fazla sakkaroz 17.04; %10 veya daha az 13.02; şekerleme halindeyse oran ne olursa olsun 17.04.",
        "<b>Sorbitollü sakız 17.04 değildir.</b> Şeker yerine sentetik tatlandırıcı içeren şekersiz sakız ve tatlılar 21.06’dadır.",
        "<b>Suni bal tabii balla karışsa da 17.02’dedir.</b> Yalnız katkısız tabii bal 04.09’dadır.",
    ],
    "hafiza": {
        "kanca": "ŞEker – DİĞeri – MElas – MAmul; kakao gelirse kapı 18",
        "aciklama": "17.01 <b>ŞE</b>ker (pancar-kamış, katı) · 17.02 <b>Dİ</b>ğer şekerler, şurup, suni bal, karamel · 17.03 <b>ME</b>las · 17.04 şeker <b>MA</b>mulü. Üç eşik ezberi: laktoz <b>%95</b>, malto-dekstrin <b>%10</b>, meyan kökü <b>%10</b>.",
    },
    "sinav_odagi": [
        "Bu fasıl çıkmış sorularda az sayıda; çoğunlukla Bölüm IV’ün kapsamı (şeker, kakao, sirke, meşrubat Bölüm IV’te; kahve Bölüm II’de) üzerinden sorulmuştur.",
        "Tabii bal ile karıştırılmış olsun olmasın (diyabetik) suni balın Fasıl 4’te değil 17.02’de yer aldığı; seçeneklerde baharat, tabii bal ve Fasıl 19 pozisyonlarının çeldirici olarak kullanılması.",
        "Ciklet gibi şeker mamullerinin, “aynı bölümde yer alan eşya” sorularında Bölüm IV’ün diğer ürünleriyle (şarap tortusu, tütün) birlikte seçeneklerde yer alması.",
        "Şeker oranının hangi fasıllarda sınıflandırma ölçütü olduğu (Fasıl 20’de evet, Fasıl 11’de hayır); Fasıl 17’de ise ayrım şekerin türüne, haline (katı-şurup) ve katkılarına (aroma, renk, kakao) dayanır.",
    ],
    "cikmis_ornekler": [
        {
            "soru": "Aşağıdakilerden hangisi IV’üncü Bölüm kapsamında değildir?",
            "secenekler": ["Sirke", "Kakao", "Şeker", "Kahve", "Meşrubat"],
            "cevap": "D",
            "aciklama": "Bölüm IV Fasıl 16–24’ü kapsar: şeker Fasıl 17, kakao Fasıl 18, meşrubat ve sirke Fasıl 22. Kahve ise Fasıl 9’da, yani Bölüm II’de (bitkisel ürünler) yer alır.",
        }
    ],
    "ozet": [
        "17.01 katı pancar-kamış şekeri ve saf sakkaroz · 17.02 diğer şekerler, aromasız şurup, suni bal, karamel · 17.03 melas · 17.04 kakaosuz şeker mamulleri.",
        "Kakao hangi oranda olursa olsun 18.06; beyaz çikolata ise 17.04 (kakao yağı kakao sayılmaz).",
        "Aroma-renk: katı şekerde serbest (17.01), şurupta 21.06’ya götürür.",
        "Saf şekerlerden yalnız sakkaroz, laktoz, maltoz, glikoz, fruktoz Fasıl 17’de; diğerleri 29.40.",
        "Eşikler: laktoz %95 (altı 04.04), malto-dekstrin %10 (altı 35.05), meyan kökü %10 (altı 13.02).",
        "Komşular: tabii bal 04.09, şekerlenmiş meyve 20.06, reçel 20.07, sorbitollü şekerleme 21.06, tıbbi pastil Fasıl 30.",
    ],
    "sorular": sorular,
}

yaz(17, obj)
