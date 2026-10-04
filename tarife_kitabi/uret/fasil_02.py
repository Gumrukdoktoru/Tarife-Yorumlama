"""Fasıl 2 – Etler ve yenilen sakatat → data/fasil_02.json"""
from yardim_00_03 import q, yaz, T_E, T_O, T_F, T_N, T_G, T_B, T_C, T_S

modul = {
    "tur": "fasil",
    "fasil": 2,
    "baslik": "Etler ve yenilen sakatat",
    "bolum": "I",
    "oz": {
        "vurgu": "Fasıl 2 iki soru sorar: Et veya sakatat insanların yemesine elverişli mi? Elverişliyse yalnızca fasılda sayılan hallerde mi (taze, soğutulmuş, dondurulmuş, tuzlanmış, salamura edilmiş, kurutulmuş, tütsülenmiş)? İkisi de evetse et hayvanın türüne göre 02.01–02.08’e, etsiz domuz yağı ve kümes yağı 02.09’a, muhafaza işlemi görmüş et 02.10’a gider; pişirilmiş, baharatlanmış, sosis veya pate halindeki et Fasıl 16’dadır.",
        "maddeler": [
            "Taze, soğutulmuş veya dondurulmuş et türe göre ayrılır: sığır 02.01–02.02, domuz 02.03, koyun-keçi 02.04, at-eşek-katır-bardo 02.05, kümes 02.07, diğer hayvanlar (01.06) 02.08.",
            "Yenilen sakatat: sığır, domuz, koyun, keçi, at ailesi 02.06; kümes 02.07; diğerleri 02.08; tuzlanmış, kurutulmuş veya tütsülenmiş sakatat 02.10.",
            "Fasıl dışı: bağırsak, mesane, mide (yenilebilir olsa bile) 05.04; hayvan kanı 05.11 veya 30.02; yenmeyen et ve sakatat 05.11; yenilebilir cansız böcekler 04.10.",
            "Hava geçirmez kutu ve modifiye atmosfer (MAP) ambalajı faslı değiştirmez; hazırlama şekli değiştirir."
        ]
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "İnsanların yemesine elverişsiz mi?", "<b>05.11</b> (un, kaba un, pellet ise <b>23.01</b>)"],
            ["2", "Bağırsak, mesane veya mide mi? (yenilebilir olsa bile)", "<b>05.04</b>"],
            ["3", "Hayvan kanı mı?", "<b>05.11</b> veya <b>30.02</b>"],
            ["4", "Yalnızca eczacılık için kullanılan sakatat mı? (safra kesesi, böbreküstü bezi, plasenta)", "Geçici muhafazalı <b>05.10</b> · kurutulmuş <b>30.01</b>"],
            ["5", "Sosis, sucuk mu; pişirilmiş, baharatla işlenmiş, hamur veya ekmek kırıntısıyla kaplanmış mı; pate mi?*", "Fasıl 16: <b>16.01</b> / <b>16.02</b>"],
            ["6", "Yağsız et kısmı içermeyen domuz yağı veya kümes hayvanı yağı mı? (eritilmemiş)", "<b>02.09</b> (eritilmiş veya çıkarılmışsa <b>15.01</b>)"],
            ["7", "Tuzlanmış, salamura edilmiş, kurutulmuş veya tütsülenmiş et ya da sakatat mı; yenilebilir et unu mu?", "<b>02.10</b>"],
            ["8", "01.05’teki kümes hayvanlarının eti veya sakatatı mı?", "<b>02.07</b>"],
            ["9", "Sığır, domuz, koyun, keçi, at, eşek, katır veya bardo sakatatı mı?", "<b>02.06</b>"],
            ["10", "Sığır eti mi?", "Taze veya soğutulmuş <b>02.01</b> · dondurulmuş <b>02.02</b>"],
            ["11", "Domuz / koyun-keçi / at-eşek-katır-bardo eti mi?", "<b>02.03</b> / <b>02.04</b> / <b>02.05</b>"],
            ["12", "Hiçbiri değilse (01.06 hayvanlarının eti ve sakatatı)", "<b>02.08</b>"]
        ],
        "dipnot": "* Fasıl 2’de kalan işlemler: kesme, küçük parçalara ayırma, kıyma; papain gibi proteolitik enzimlerle yumuşatma; hafifçe şeker veya şekerli su serpme; pişirme olmaksızın önceden haşlama; nakliye için tuzla paketleme; hava geçirmez kap ve MAP ambalajı."
    },
    "pozisyon_haritasi": [
        ["02.01", "Sığır eti (taze veya soğutulmuş)", "01.02 hayvanları; evcil veya yabani", "Soğutulmuş dana karkası, taze manda eti"],
        ["02.02", "Sığır eti (dondurulmuş)", "02.01 ile aynı kapsam, dondurulmuş", "Dondurulmuş bizon eti"],
        ["02.03", "Domuz eti (taze, soğutulmuş, dondurulmuş)", "Evcil ve yabani; lifli domuz eti ve yapışık yağ dahil", "Yaban domuzu eti, domuz butu"],
        ["02.04", "Koyun ve keçi eti", "Evcil veya yabani; kuzu ve oğlak dahil", "Kuzu karkası, dondurulmuş keçi eti"],
        ["02.05", "At, eşek, katır, bardo eti", "01.01 hayvanları", "Dondurulmuş at eti"],
        ["02.06", "02.01–02.05 hayvanlarının yenilen sakatatı", "Yalnız taze, soğutulmuş, dondurulmuş", "Sığır dili, kuzu böbreği, dana uykuluğu"],
        ["02.07", "Kümes hayvanlarının eti ve yenilen sakatatı", "01.05’teki evcil türler; taze, soğutulmuş, dondurulmuş", "Tavuk but, hindi, kaz ve ördek yağlı karaciğeri"],
        ["02.08", "Diğer etler ve yenilen sakatat", "01.06 hayvanları; taze, soğutulmuş, dondurulmuş", "Tavşan, kurbağa, ren geyiği, balina, kaplumbağa eti"],
        ["02.09", "Etsiz domuz yağı ve kümes hayvanı yağı", "Eritilmemiş; sanayide kullanılmaya elverişli olsa bile", "Domuz iç yağı, eritilmemiş kaz yağı"],
        ["02.10", "Tuzlanmış, salamura, kurutulmuş, tütsülenmiş et ve sakatat; yenilebilir et unu", "Tüm hayvan türleri; muhafaza işlemi", "Tütsülenmiş domuz butu, kurutulmuş sığır dili, yenilebilir et unu"]
    ],
    "notlar": [
        ["Bölüm I Not 1", "Bir hayvan cins veya türüne yapılan atıf, aksi belirtilmedikçe yavrusunu da kapsar: dana eti 02.01–02.02’de, kuzu ve oğlak eti 02.04’te yer alır."],
        ["Bölüm I Not 2", "“Kurutulmuş” ürünlere yapılan atıf, suyu alınmış, buharlaştırılmış veya dondurularak kurutulmuş (liyofilize) ürünleri de kapsar; liyofilize et de kurutulmuş et olarak 02.10’dadır."],
        ["Fasıl 2 Notu", "Fasıl dışı: 02.01–02.08 veya 02.10’a giren ürünlerden insanların yemesine elverişli olmayanlar; yenilen, cansız böcekler (04.10); hayvan bağırsakları, mesaneleri ve mideleri (05.04) veya hayvan kanı (05.11 veya 30.02); 02.09 dışındaki hayvansal yağlar (Fasıl 15)."],
        ["Genel Açıklamalar", "Fasıl 2’deki haller: taze (nakliye sırasında geçici muhafaza için tuzla paketlenmiş dahil); soğutulmuş (dondurmadan, genel olarak 0 °C civarına düşürülmüş); dondurulmuş (donma noktasının altında tamamen donuncaya kadar soğutulmuş); tuzlanmış, salamura edilmiş, kurutulmuş veya tütsülenmiş. Pişirilmemiş olmak şartıyla önceden haşlanmış olabilir."],
        ["Genel Açıklamalar", "Fasılda kalır: hafifçe şeker veya şekerli su serpilmiş; proteolitik enzimlerle (papain) yumuşatılmış; kesilmiş, küçük parçalara ayrılmış veya kıyma haline getirilmiş et; fasılın farklı pozisyonlarındaki ürünlerin karışımı (domuz yağıyla kaplanmış kümes eti); insan tüketimine uygun et ve sakatat unu (pişirilmiş olsun olmasın)."],
        ["Genel Açıklamalar", "Fasıl 16’ya gider: sucuk, sosis ve benzerleri, pişirilmiş olsun olmasın (16.01); kaynatılmış, buharda pişirilmiş, ızgara, yağda kızartılmış veya fırınlanmış et; yalnızca hamur veya ekmek kırıntısıyla kaplanmış ya da biber ve tuz gibi baharatlarla işlem görmüş et; karaciğer ezmesi ve pateler (16.02)."],
        ["Genel Açıklamalar", "Hava geçirmez paket (teneke kutuda kurutulmuş et) ve Modifiye Atmosferde Paketleme (MAP: oksijenin azaltılması, azot veya karbondioksitle değiştirilmesi) faslı değiştirmez; ancak kutuya konulan ürünler çoğu kez farklı hazırlandığından Fasıl 16’ya gider."],
        ["Genel Açıklamalar", "Sakatatın 4 grubu: (1) esasen gıda olanlar (baş, kulak, ayak, kuyruk, kalp, dil, kırpıntı, gırtlak, timus) → yenilebilirse Fasıl 2, değilse 05.11; (2) yalnız eczacılık için olanlar (safra kesesi, böbreküstü bezi, plasenta) → geçici muhafazalı 05.10, kurutulmuş 30.01; (3) her ikisi için olanlar (karaciğer, böbrek, akciğer, beyin, pankreas, dalak) → eczacılık için geçici muhafazalı 05.10, kurutulmuş 30.01, gıdaya uygunsa Fasıl 2, değilse 05.11; (4) deri gibi olanlar → yenilebilirse Fasıl 2, değilse 05.11 veya Fasıl 41."],
        ["Genel Açıklamalar", "Ayrı sunulan hayvansal yağlar Fasıl 15’tedir (02.09 hariç); karkas halindeki etlerin yağları ile et parçalarına yapışık yağlar etle birlikte sınıflandırılır. Bağırsak, mesane ve işkembe (balıklarınki hariç) yenilebilir olsun olmasın 05.04’tedir."],
        ["02.06 Açıklama Notu", "Yenilebilen sakatat: baş ve parçaları (kulak dahil), ayak, kuyruk, kalp, meme, karaciğer, böbrek, timus bezi ve pankreas (uykuluk), beyin, akciğer, gırtlak, kırpıntılar, dalak, dil, amnion zarı, omurilik, yenilebilen deri, üreme organları, tiroid ve hipofiz bezleri. Bu hükümler 02.10’daki sakatata da uygulanır."],
        ["02.07 Açıklama Notu", "Yalnız 01.05’teki evcil kümes hayvanlarının taze, soğutulmuş veya dondurulmuş et ve sakatatı. Kaz veya ördeklerin yağlı karaciğerleri; daha büyük, ağır, sert, yağca zengin ve açık bej ile açık kahverengi arası renkleriyle diğer karaciğerlerden ayrılır."],
        ["02.08 Açıklama Notu", "İnsan tüketimine uygun olmak kaydıyla 01.06’daki hayvanların (tavşan, yabani tavşan, kurbağa, ren geyiği, kunduz, balina, kaplumbağa) et ve sakatatı."],
        ["02.09 Açıklama Notu", "Yağsız et kısmı içermeyen domuz yağı (özellikle iç yağ) ile evcil veya yabani kümes hayvanı yağı; sanayide kullanılmaya elverişli olsa bile buradadır. Eritilince veya başka surette çıkarılınca 15.01’e gider. Lifli domuz eti ve et tabakasına yapışık yağ 02.03 veya 02.10’dadır; deniz memelisi katı yağları Fasıl 15’tedir."],
        ["02.10 Açıklama Notu", "Pozisyon metninde belirtilen şekilde hazırlanmış her çeşit et ve yenilen sakatat (02.09’daki yağlar hariç); lifli domuz eti dahil. Et ve sakatatın yenilebilen un ve kaba unları buradadır; insan tüketimine uygun olmayanlar (ör. hayvan beslemede kullanılanlar) 23.01’dedir."]
    ],
    "sinir_komsulari": [
        ["Yenilmeye elverişsiz et ve sakatat", "05.11", "Fasıl 2 Notu"],
        ["Yenmeyen et unu, kaba unu, pelleti (yem)", "23.01", "02.10 Açıklama Notu"],
        ["Bağırsak, işkembe, mesane (yenilebilir olsa bile)", "05.04", "Fasıl 2 Notu"],
        ["Hayvan kanı", "05.11 / 30.02", "Fasıl 2 Notu"],
        ["Yenilen cansız böcekler", "04.10", "Fasıl 2 Notu"],
        ["Eritilmiş domuz yağı, eritilmiş kaz yağı", "15.01", "02.09 Açıklama Notu"],
        ["Balina, fok gibi deniz memelilerinin katı yağları", "Fasıl 15", "02.09 Açıklama Notu"],
        ["Eczacılık için geçici muhafazalı safra kesesi, böbreküstü bezi", "05.10", "Yalnız eczacılıkta kullanılan sakatat"],
        ["Kurutulmuş eczacılık sakatatı (safra kesesi, plasenta)", "30.01", "Genel Açıklamalar"],
        ["Yenmeyen deri (deri imalatı için)", "05.11 / Fasıl 41", "Genel Açıklamalar"],
        ["Sucuk, sosis (pişirilmiş olsun olmasın)", "16.01", "Fasıl 2 dışı hazırlık"],
        ["Kaynatılmış, kızartılmış veya baharatlanmış et; ciğer ezmesi, pate", "16.02", "Fasıl 2 dışı hazırlık"],
        ["Balık eti, kabuklu hayvan eti; yenilebilir balık unu", "03.04 / 03.06 / 03.09", "Fasıl 3 ürünleri"],
        ["Kurbağa bacağı, balina eti (taze veya dondurulmuş)", "02.08 (Fasıl 3 değil)", "01.06 hayvanlarının eti"]
    ],
    "tuzaklar": [
        "<b>Bağırsak tarife bakımından sakatat değildir.</b> Hayvan bağırsakları, mesaneleri ve mideleri (işkembe) yenilebilir olsun olmasın 05.04’tedir.",
        "<b>Pişirme Fasıl 16’ya gönderir, ön haşlama göndermez.</b> Pişirilmemiş olmak şartıyla önceden haşlanmış et Fasıl 2’de kalır.",
        "<b>Tuz koruma ise 02.10, baharat ise 16.02.</b> Tuzlanmış et 02.10’dadır; biber ve tuz gibi baharatlarla işlem görmüş veya ekmek kırıntısıyla kaplanmış et 16.02’dir.",
        "<b>Geçici tuz taze sayılır.</b> Nakliye sırasında geçici muhafaza için tuzla paketlenmiş et “taze” kabul edilir.",
        "<b>02.07 yalnız taze, soğutulmuş, dondurulmuştur.</b> Tuzlanmış, kurutulmuş veya tütsülenmiş kümes eti 02.10’a gider.",
        "<b>Kanatlı her et 02.07 değildir.</b> Sülün, keklik, güvercin, yabani ördek eti 01.06 hayvanı olduğundan 02.08’dedir.",
        "<b>Yağ ayrı gelirse Fasıl 15, istisnası 02.09.</b> Etsiz domuz yağı ve kümes yağı eritilmemişse 02.09; eritilince 15.01. Ete yapışık yağ etle birlikte kalır.",
        "<b>Balina eti Fasıl 3 değildir.</b> Taze veya dondurulmuşsa 02.08, tuzlu, kurutulmuş veya tütsülenmişse 02.10.",
        "<b>Eczacılık sakatatı Fasıl 2’de değildir.</b> Geçici muhafazalı ise 05.10, kurutulmuşsa 30.01.",
        "<b>Ambalaj faslı değiştirmez.</b> Teneke kutuda kurutulmuş et ve MAP ambalajlı taze sığır eti Fasıl 2’dedir."
    ],
    "hafiza": {
        "kanca": "SI-SI-DO-KO-AT · SA-KÜ-Dİ · YA-TU",
        "aciklama": "02.01 <b>SI</b>ğır taze · 02.02 <b>SI</b>ğır donuk · 02.03 <b>DO</b>muz · 02.04 <b>KO</b>yun-keçi · 02.05 <b>AT</b> ailesi · 02.06 <b>SA</b>katat · 02.07 <b>KÜ</b>mes · 02.08 <b>Dİ</b>ğer etler · 02.09 <b>YA</b>ğ · 02.10 <b>TU</b>zlu-kuru-tütsülü. Görsel benzetme: bir kasap tezgâhı; soğuk dolapta büyükbaştan küçükbaşa etler, yanında sakatat tepsisi, sonra kümes reyonu ve av eti köşesi; en sonda yağ kalıpları ve tavandan sarkan tütsülenmiş butlar. Sucuk, kavurma ve pate tezgâhı ise karşı dükkândadır (Fasıl 16)."
    },
    "sinav_odagi": [
        "Doğrudan Fasıl 2 sorusu azdır; fasıl daha çok deniz memelisi eti ile başlık–not ilişkisi üzerinden sorulmuştur.",
        "01.06 hayvanlarının (balina) dondurulmuş etinin 02.08’de olduğu; 02.07 (kümes) ve 03.02–03.03 (balık) pozisyonlarının çeldirici olarak kullanılması.",
        "Fasıl başlığı “Etler ve yenilen sakatat” olmasına rağmen bağırsak, mesane ve midenin 05.04’e gitmesi ve bunun GYK 1 (başlıklar gösterici, notlar bağlayıcı) ile açıklanması.",
        "Ürün–pozisyon eşleştirmelerinde et ile ilgili komşu pozisyonlar: et suyunun 21.04’te yer alması gibi Fasıl 2 dışına çıkan ürünler.",
        "Takım ve hazır yemek sorularında et ve deniz ürünü içeriğinin Fasıl 16 notundaki %20 ölçütüyle birlikte değerlendirilmesi."
    ],
    "cikmis_ornekler": [
        {
            "soru": "Dondurulmuş balina eti Tarife Cetvelinde hangi pozisyondadır?",
            "secenekler": ["02.07", "02.08", "03.02", "03.03"],
            "cevap": "B",
            "aciklama": "Balina 01.06’daki deniz memelilerindendir; 02.08, 01.06 hayvanlarının taze, soğutulmuş veya dondurulmuş et ve sakatatını kapsar ve açıklama notunda balina açıkça sayılmıştır. Fasıl 3 Not 1 bu etleri Fasıl 3 dışında bırakır; 02.07 yalnız kümes hayvanları içindir."
        },
        {
            "soru": "Gümrük Tarife Cetvelinde 2. Fasıl başlığı “Etler ve Yenilen Sakatat” olmasına karşın hayvan bağırsakları, mesaneleri veya midelerinin 5. Fasılda “Tarifenin başka yerinde belirtilmeyen veya yer almayan hayvansal menşeli ürünler” olarak sınıflandırılması hangi Genel Yorum Kuralının (GYK) gereğidir?",
            "secenekler": ["GYK 1", "GYK 3", "GYK 4", "GYK 2", "GYK 6"],
            "cevap": "A",
            "aciklama": "GYK 1’e göre fasıl başlıkları sadece gösterici niteliktedir; sınıflandırma pozisyon metinleri ile Bölüm ve Fasıl notlarına göre yapılır. Fasıl 2 notu bağırsak, mesane ve mideleri fasıl dışında bırakıp 05.04’e gönderir."
        }
    ],
    "ozet": [
        "Önce yenilebilirlik: yenmeyen et ve sakatat 05.11, yenmeyen et unu 23.01.",
        "Bağırsak, mesane, mide 05.04; kan 05.11 veya 30.02; eczacılık sakatatı 05.10 veya 30.01.",
        "Taze, soğutulmuş, dondurulmuş et türe göre 02.01–02.08; kümes 02.07, 01.06 hayvanları 02.08.",
        "Tuzlanmış, salamura, kurutulmuş, tütsülenmiş et ve sakatat ile yenilebilir et unu 02.10.",
        "Etsiz domuz yağı ve kümes yağı eritilmemişse 02.09; eritilmişse 15.01.",
        "Pişirme, baharat, kaplama, sosis ve pate → Fasıl 16; kıyma, enzim, hafif şeker, ambalaj → Fasıl 2’de kalır."
    ],
}

S = []
# 1
S.append(q("Tarife Cetveline göre insan tüketimine uygun, taze veya soğutulmuş kurbağa bacakları hangi pozisyonda sınıflandırılır?",
           ["02.06", "*02.08", "03.02", "03.08", "04.10"], T_E,
           "02.08, 01.06’daki hayvanların insan tüketimine uygun et ve sakatatını kapsar; açıklama notu kurbağayı açıkça sayar. Kurbağa balık (03.02) veya su omurgasızı (03.08) değildir; 02.06 yalnız sığır, domuz, koyun, keçi ve at ailesinin sakatatı içindir. Kurbağa eti 02.08’de belirtildiğinden 04.10’a gitmez.",
           "02.08 Açıklama Notu; 01.06 Açıklama Notu (E)."))
# 2
S.append(q("Tarife Cetveline göre dondurulmuş at eti hangi pozisyonda sınıflandırılır?",
           ["02.02", "02.04", "*02.05", "02.08", "02.10"], T_E,
           "02.05, 01.01’deki hayvanların (at, eşek, katır, bardo) taze, soğutulmuş veya dondurulmuş etlerini kapsar. 02.02 dondurulmuş sığır eti, 02.04 koyun ve keçi eti, 02.08 01.06 hayvanlarının eti içindir; 02.10 ise tuzlanmış, salamura, kurutulmuş veya tütsülenmiş etleri kapsar.",
           "02.05 pozisyon metni ve Açıklama Notu."))
# 3
S.append(q("Tarife Cetveline göre insan tüketimine uygun, taze kaz yağlı karaciğeri hangi pozisyonda sınıflandırılır?",
           ["02.06", "*02.07", "02.09", "05.10", "16.02"], T_E,
           "02.07, 01.05’teki kümes hayvanlarının taze, soğutulmuş veya dondurulmuş et ve yenilen sakatatını kapsar; açıklama notu kaz ve ördeklerin yağlı karaciğerlerini ayrıca anlatır. 02.06 memelilerin sakatatı, 02.09 eritilmemiş kümes hayvanı yağı içindir (karaciğer yağ değildir). 16.02 karaciğer ezmesi ve pate gibi hazırlanmış ürünleri, 05.10 eczacılık amaçlı sakatatı kapsar.",
           "02.07 Açıklama Notu; Fasıl 2 Genel Açıklamalar."))
# 4
S.append(q("Tarife Cetveline göre yağsız et kısmı içermeyen, eritilmemiş taze kaz yağı hangi pozisyonda sınıflandırılır?",
           ["02.07", "02.08", "*02.09", "05.11", "15.01"], T_E,
           "02.09, evcil veya yabani kümes hayvanlarının eritilmemiş veya başka surette çıkarılmamış yağlarını kapsar. Eritildiğinde veya başka surette çıkarıldığında 15.01’e geçer (tuzak). 02.07 et ve sakatat pozisyonudur; 02.08 01.06 hayvanları içindir; yenilmeye elverişli olduğundan 05.11 de uygulanmaz.",
           "02.09 pozisyon metni ve Açıklama Notu; Fasıl 2 Notu."))
# 5
S.append(q("Tarife Cetveline göre insan tüketimine uygun, tütsülenmiş ve kurutulmuş sığır dili hangi pozisyonda sınıflandırılır?",
           ["02.01", "02.06", "02.08", "*02.10", "16.02"], T_E,
           "Dil yenilebilen sakatattır; 02.06 yalnız taze, soğutulmuş veya dondurulmuş sakatatı kapsar. Tütsülenmiş veya kurutulmuş et ve yenilen sakatat 02.10’dadır; 02.06 açıklama notu hükümleri bu pozisyondaki sakatata da uygulanır. Tütsüleme ve kurutma Fasıl 2 işlemleri olduğundan 16.02’ye gidilmez.",
           "02.10 pozisyon metni ve Açıklama Notu; 02.06 Açıklama Notu."))
# 6
S.append(q("Aşağıdakilerden hangisi Tarife Cetvelinin 2. faslında <b>sınıflandırılmaz</b>?",
           ["Modifiye atmosferde paketlenmiş (MAP) taze sığır eti",
            "Teneke kutuda hava geçirmez şekilde paketlenmiş kurutulmuş et",
            "Papain ile yumuşatılmış dondurulmuş sığır eti",
            "*Fırında pişirilmiş kuzu but",
            "Üzerine hafifçe şekerli su serpilmiş taze domuz eti"], T_O,
           "Herhangi bir şekilde pişirilmiş (kaynatılmış, buharda pişirilmiş, ızgara, kızartılmış veya fırınlanmış) et Fasıl 2’de yer almaz; 16.02’dedir. MAP ambalajı, hava geçirmez kutu, proteolitik enzimle yumuşatma ve hafif şeker serpme Genel Açıklamalara göre eti Fasıl 2 dışına çıkarmaz.",
           "Fasıl 2 Genel Açıklamalar (Fasıl 16 ile farklar)."))
# 7
S.append(q("Aşağıdakilerden hangisi 02.06 pozisyonunda <b>yer almaz</b>?",
           ["Dondurulmuş sığır dili", "*Dondurulmuş tavuk ciğeri", "Taze kuzu böbreği", "Soğutulmuş dana uykuluğu (timus bezi)", "Taze domuz ayağı"], T_O,
           "02.06 yalnız sığır, domuz, koyun, keçi, at, eşek, katır veya bardoların yenilen sakatatını kapsar. Tavuk ciğeri 01.05’teki kümes hayvanının sakatatı olduğundan 02.07’dedir. Dil, böbrek, timus bezi ve ayak 02.06 açıklama notunda sayılmıştır.",
           "02.06 pozisyon metni ve Açıklama Notu; 02.07 pozisyon metni."))
# 8
S.append(q("Aşağıdakilerden hangisi 02.08 pozisyonunda <b>sınıflandırılmaz</b>?",
           ["Taze tavşan eti", "Dondurulmuş balina eti", "Soğutulmuş ren geyiği eti", "Dondurulmuş kaplumbağa eti", "*Dondurulmuş hindi eti"], T_O,
           "Hindi 01.05’teki evcil kümes hayvanlarındandır; eti 02.07’dedir. 02.08 ise 01.06’daki hayvanların etlerini kapsar ve açıklama notu tavşan, ren geyiği, balina ve kaplumbağayı açıkça sayar.",
           "02.08 Açıklama Notu; 02.07 pozisyon metni."))
# 9
S.append(q("Aşağıdakilerden hangisi 02.09 pozisyonunda <b>sınıflandırılmaz</b>?",
           ["*Eritilerek elde edilmiş domuz yağı",
            "Eritilmemiş domuz iç yağı",
            "Sanayide kullanılmaya elverişli, yağsız et kısmı içermeyen domuz yağı",
            "Tuzlanmış, yağsız et kısmı içermeyen domuz yağı",
            "Eritilmemiş taze kaz yağı"], T_O,
           "02.09 Açıklama Notuna göre domuz yağı ve kümes hayvanı yağı eritildiğinde veya başka şekilde çıkarıldığında bu pozisyondan çıkar ve 15.01’de yer alır. İç yağ, sanayiye elverişli etsiz domuz yağı, tuzlanmış etsiz domuz yağı ve eritilmemiş kaz yağı 02.09’dadır.",
           "02.09 pozisyon metni ve Açıklama Notu."))
# 10
S.append(q("Aşağıdaki taze veya soğutulmuş etlerden hangisi diğerlerinden <b>farklı</b> bir pozisyonda sınıflandırılır?",
           ["Taze manda eti", "Soğutulmuş bizon eti", "Taze zebu eti", "Soğutulmuş dana eti", "*Taze deve eti"], T_F,
           "02.01, 01.02’ye giren evcil veya yabani sığırların taze veya soğutulmuş etlerini kapsar; manda, bizon ve zebu 01.02’dedir, dana ise Bölüm I Not 1 gereği sığırın yavrusudur. Deve 01.06 hayvanı olduğundan eti 02.08’dedir.",
           "02.01 Açıklama Notu; 01.02 ve 01.06 Açıklama Notları; Bölüm I Not 1."))
# 11
S.append(q("Aşağıdaki et ürünlerinden hangisi diğerlerinden farklı bir <b>fasılda</b> yer alır?",
           ["Tütsülenmiş domuz butu", "*Yağda kızartılmış tavuk", "Tuzlanmış sığır eti", "Kurutulmuş at eti", "Salamura edilmiş sığır dili"], T_F,
           "Tütsüleme, tuzlama, kurutma ve salamura Fasıl 2 işlemleridir; bu ürünler 02.10’dadır. Yağda kızartılmış tavuk ise pişirilmiş et olduğundan Fasıl 16’da (16.02) sınıflandırılır.",
           "02.10 pozisyon metni; Fasıl 2 Genel Açıklamalar."))
# 12
S.append(q("İnsan tüketimine uygun aşağıdaki ürünlerden hangisi diğerlerinden farklı bir fasılda sınıflandırılır?",
           ["Taze sığır kalbi", "Dondurulmuş kuzu karaciğeri", "Taze domuz kuyruğu", "*Tuzlanmış sığır bağırsağı", "Soğutulmuş dana beyni"], T_F,
           "Hayvan bağırsakları, mesaneleri ve mideleri, Fasıl 2 notu gereği yenilebilir olsun olmasın 05.04’te, yani Fasıl 5’te sınıflandırılır. Kalp, karaciğer, kuyruk ve beyin yenilen sakatat olarak 02.06’da (Fasıl 2) yer alır.",
           "Fasıl 2 Notu; 02.06 Açıklama Notu; 05.04 pozisyon metni."))
# 13
S.append(q("Aşağıdaki etlerden hangisi diğerleriyle aynı pozisyonda <b>yer almaz</b>?",
           ["*Dondurulmuş sülün eti", "Dondurulmuş tavuk but", "Taze hindi göğsü", "Dondurulmuş bütün ördek", "Taze beç tavuğu eti"], T_F,
           "02.07 yalnız 01.05’teki evcil kümes hayvanlarının (tavuk, hindi, ördek, kaz, beç tavuğu) et ve sakatatını kapsar. Sülün 01.06’daki diğer kuşlardandır; eti 02.08’de sınıflandırılır. Tuzak, kanatlı her eti 02.07’ye koymaktır.",
           "02.07 pozisyon metni ve Açıklama Notu; 01.06 Açıklama Notu (C); 02.08 Açıklama Notu."))
# 14
S.append(q("Fasıl 2 Genel Açıklamalarına göre “soğutulmuş” et için aşağıdakilerden hangisi doğrudur?",
           ["*Dondurulmadan, sıcaklığı genel olarak 0 °C civarına düşürülmüş ettir.",
            "Sıcaklığı eksi 18 °C’ye indirilerek muhafaza edilen ettir.",
            "Donma noktasının altında tamamen donuncaya kadar soğutulmuş ettir.",
            "Tuzla paketlenerek 4 °C’de tutulan ettir.",
            "Sıcaklığı 10 °C’nin altına indirilmiş ettir."], T_N,
           "Genel Açıklamalara göre soğutulmuş ürünler, dondurulmadan, genel olarak sıcaklığı 0 °C civarına düşürülerek soğutulmuş olanlardır. Donma noktasının altında tamamen donuncaya kadar soğutma “dondurulmuş” tanımıdır (tuzak). Metinde başka bir sıcaklık eşiği verilmemiştir.",
           "Fasıl 2 Genel Açıklamalar."))
# 15
S.append(q("Fasıl 2 notu ve Genel Açıklamalarına göre hayvansal yağlarla ilgili aşağıdakilerden hangisi doğrudur?",
           ["Ayrı olarak sunulan bütün hayvansal yağlar 02.09’da sınıflandırılır.",
            "*Karkas halindeki etlerin yağları ile et parçalarına yapışık yağlar etle birlikte sınıflandırılır.",
            "Yağsız et kısmı içermeyen domuz yağı sanayide kullanılmaya elverişliyse Fasıl 15’e gider.",
            "Kümes hayvanı yağları eritilmiş olsalar da 02.09’da kalır.",
            "Deniz memelilerinin katı yağları 02.09’da sınıflandırılır."], T_N,
           "Genel Açıklamalara göre karkas halindeki etlerin yağları ve et parçalarına yapışık yağlar et rejimine tabidir. Ayrı sunulan hayvansal yağlar Fasıl 15’tedir; istisna 02.09’daki etsiz domuz yağı ve eritilmemiş kümes yağıdır ve bunlar sanayiye elverişli olsalar da 02.09’da kalır. Eritilmiş yağlar 15.01’e, deniz memelisi yağları Fasıl 15’e gider.",
           "Fasıl 2 Notu; Fasıl 2 Genel Açıklamalar; 02.09 Açıklama Notu."))
# 16
S.append(q("Fasıl 2 Genel Açıklamalarına göre yalnızca eczacılık mamullerinin hazırlanmasında kullanılan sakatat (ör. safra kesesi, böbreküstü bezleri, plasenta) kurutulmuş olarak sunulduğunda hangi pozisyonda sınıflandırılır?",
           ["02.06", "02.10", "05.10", "05.11", "*30.01"], T_N,
           "Genel Açıklamalara göre yalnız eczacılıkta kullanılan sakatat taze, soğutulmuş, dondurulmuş veya geçici olarak muhafazaya alınmışsa 05.10’da, kurutulmuşsa 30.01’de yer alır. 02.10 insan tüketimine uygun kurutulmuş sakatat içindir (tuzak); 05.11 yenmeyen sakatatı kapsar.",
           "Fasıl 2 Genel Açıklamalar (sakatat grupları)."))
# 17
S.append(q("Fasıl 2 Genel Açıklamalarına göre aşağıdaki işlemlerden hangisi taze eti Fasıl 2 dışına çıkarır?",
           ["Papain gibi proteolitik enzimlerle yumuşatma",
            "Kıyma haline getirme",
            "Hafifçe şekerli su solüsyonu serpme",
            "Nakliye sırasında geçici muhafaza için tuzla paketleme",
            "*Yalnızca ekmek kırıntısıyla kaplama"], T_N,
           "Yalnızca hamur veya ekmek kırıntısıyla kaplanmış et, Fasıl 2’de yer almayan bir şekilde hazırlanmış sayılır ve 16.02’ye gider. Enzimle yumuşatma, kıyma, hafif şeker serpme ve nakliye için tuzla paketleme Genel Açıklamalarda Fasıl 2’de kalan işlemler olarak sayılmıştır.",
           "Fasıl 2 Genel Açıklamalar (Fasıl 16 ile farklar)."))
# 18
S.append(q("Gıda sanayiinde kullanılacak, insan tüketimine uygun sıvı sığır kanı Fasıl 2 notu ile bu fasıl dışında bırakılmış olup 05.11 pozisyonunda sınıflandırılır. Bu sınıflandırma hangi Genel Yorum Kuralına dayanır?",
           ["*GYK 1", "GYK 2(b)", "GYK 3(a)", "GYK 3(c)", "GYK 4"], T_G,
           "GYK 1’e göre sınıflandırma pozisyon metinleri ile Bölüm ve Fasıl notlarına göre yapılır; fasıl başlığı yalnız gösterici niteliktedir. Fasıl 2 notu hayvan kanını fasıl dışında bırakır ve 05.11 açıklama notu kanı yenilsin yenilmesin kapsar. Not hükmü açık olduğundan 3(a), 3(c) veya 4’e başvurulmaz.",
           "GYK 1; Fasıl 2 Notu; 05.11 Açıklama Notu."))
# 19
S.append(q("Hava geçirmez teneke kutuya konulmuş kurutulmuş sığır eti, kutusuyla birlikte 02.10 pozisyonunda sınıflandırılmaktadır. Teneke kutunun ayrıca sınıflandırılmayıp etle birlikte değerlendirilmesi hangi kurala dayanır?",
           ["GYK 2(a)", "GYK 3(b)", "GYK 4", "GYK 5(a)", "*GYK 5(b)"], T_G,
           "Teneke kutu, içindeki eşyanın ambalajında normal olarak kullanılan türden bir ambalaj maddesidir ve tekrar kullanıma elverişli olduğu açıkça belli değildir; GYK 5(b) uyarınca etle birlikte sınıflandırılır. GYK 5(a) belli eşyaya göre yapılmış, uzun süre kullanılacak mahfazalar içindir; kutu bir takım kalemi de değildir. Fasıl 2 Genel Açıklamaları da hava geçirmez paketin faslı değiştirmediğini belirtir.",
           "GYK 5(b); Fasıl 2 Genel Açıklamalar."))
# 20
S.append(q("Aşağıdaki ürün – pozisyon eşleştirmelerinden hangisi <b>yanlıştır</b>?",
           ["Soğutulmuş sığır karkası – 02.01", "Dondurulmuş keçi eti – 02.04", "Taze at eti – 02.05", "*Taze tavşan eti – 02.07", "Dondurulmuş manda eti – 02.02"], T_B,
           "Tavşan 01.06’daki hayvanlardandır; eti 02.08’de sınıflandırılır ve 02.08 açıklama notu tavşanı açıkça sayar. 02.07 yalnız 01.05’teki evcil kümes hayvanları içindir. Diğer eşleştirmeler pozisyon metinleriyle uyumludur; manda 01.02’de olduğundan dondurulmuş eti 02.02’dedir.",
           "02.01–02.05, 02.07 ve 02.08 pozisyon metinleri ve Açıklama Notları."))
# 21
S.append(q("Fasıl 2 Genel Açıklamalarına göre Modifiye Atmosferde Paketleme (MAP) işleminde ürünü çevreleyen ........ değiştirilir veya kontrol edilir; bu şekilde paketlenen taze et ........ . Boşlukları doğru tamamlayan seçenek hangisidir?",
           ["sıcaklık – Fasıl 16’ya geçer", "nem oranı – 02.10’a geçer", "*atmosfer – Fasıl 2’de kalır", "atmosfer – Fasıl 16’ya geçer", "sıcaklık – Fasıl 2’de kalır"], T_B,
           "MAP işleminde ürünü çevreleyen atmosfer değiştirilir veya kontrol edilir (oksijenin çıkarılması veya azaltılması, azot veya karbondioksitle yer değiştirme). Genel Açıklamalar MAP ile paketlenen et ve sakatatın (ör. taze veya soğutulmuş sığır eti) Fasıl 2’de kaldığını açıkça belirtir; ambalaj yöntemi hazırlama sayılmaz.",
           "Fasıl 2 Genel Açıklamalar."))
# 22
S.append(q("Fasıl 2 notuna göre aşağıdakilerden hangileri Fasıl 2’ye dahil <b>değildir</b>?  I. Yenilen, cansız böcekler  II. Hayvan kanı  III. Yenilebilir domuz derisi  IV. Yağsız et kısmı içermeyen, eritilmemiş domuz yağı",
           ["*I ve II", "I ve III", "II ve IV", "I, II ve IV", "II, III ve IV"], T_C,
           "Fasıl 2 Notu yenilen cansız böcekleri (04.10) ve hayvan kanını (05.11 veya 30.02) fasıl dışında bırakır. Yenilebilen deriler 02.06 açıklama notunda sakatat olarak sayılmıştır. Not, yalnız 02.09 dışındaki hayvansal yağları hariç tuttuğundan etsiz, eritilmemiş domuz yağı Fasıl 2’dedir (02.09).",
           "Fasıl 2 Notu; 02.06 ve 02.09 Açıklama Notları."))
# 23
S.append(q("Fasıl 2 Genel Açıklamalarına göre aşağıdakilerden hangileri 16. Fasılda yer alır?  I. Pişirilmemiş sucuk  II. Biber ve tuz gibi baharatlarla işlem görmüş et  III. Nakliye sırasında geçici muhafaza için tuzla paketlenmiş taze et  IV. Karaciğer ezmesi",
           ["I ve II", "II ve III", "*I, II ve IV", "I, III ve IV", "II, III ve IV"], T_C,
           "Sucuk, sosis ve benzerleri pişirilmiş olsun olmasın 16.01’de; baharatla işlem görmüş et ve karaciğer ezmesi 16.02’dedir. Nakliye sırasında geçici muhafaza için tuzla paketlenmiş et ise Genel Açıklamalara göre “taze” sayılır ve Fasıl 2’de kalır.",
           "Fasıl 2 Genel Açıklamalar (Fasıl 16 ile farklar)."))
# 24
S.append(q("Bir firma, temizlenmiş ve dondurulmuş sığır işkembesini (mide) karton kutularda ithal etmektedir. Ürün insan tüketimine uygundur ve başka bir işlem görmemiştir. Bu ürün hangi pozisyonda sınıflandırılır?",
           ["02.06", "02.10", "*05.04", "05.11", "16.02"], T_S,
           "Fasıl 2 notu hayvan mesanelerini, bağırsaklarını ve midelerini fasıl dışında bırakır; 05.04 bunları yenilmeye elverişli olsun olmasın, taze, soğutulmuş, dondurulmuş, tuzlanmış, kurutulmuş veya tütsülenmiş olarak kapsar. Yenilebilir olması ürünü 02.06’ya getirmez; ürün yenilebildiği için 05.11 de değildir.",
           "Fasıl 2 Notu; Fasıl 2 Genel Açıklamalar; 05.04 pozisyon metni."))
# 25
S.append(q("Kemikleri çıkarılmış sığır eti kıyma haline getirilmiş, papain ile yumuşatılmış, karabiber ve tuz gibi baharatlarla tatlandırılmış ve dondurulmuştur; ürün pişirilmemiştir. Bu ürün hangi pozisyonda sınıflandırılır?",
           ["02.02", "02.10", "16.01", "*16.02", "21.06"], T_S,
           "Kıyma haline getirme, enzimle yumuşatma ve dondurma eti Fasıl 2 dışına çıkarmaz; ancak biber ve tuz gibi baharatlarla işlem görmüş et, Fasıl 2’de yer almayan bir şekilde hazırlanmış sayılır ve pişirilmemiş olsa da 16.02’dedir. Tuzlama 02.10 için koruma işlemidir, baharatla hazırlama değildir; ürün sucuk veya sosis olmadığından 16.01 de uygulanmaz.",
           "Fasıl 2 Genel Açıklamalar (Fasıl 16 ile farklar)."))

modul["sorular"] = S
yaz(2, modul)
