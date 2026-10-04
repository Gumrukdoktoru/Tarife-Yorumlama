"""Hap bilgi sayfaları: GYK (fasıl 0) ve Fasıl 1–5.

Kaynak: data/fasil_00..05.json modülleri, kaynak/gyk.txt, kaynak/fasillar/FASIL01..05.txt,
kaynak/son5_analiz.json. Çıktı: hap/fasil_00.json … hap/fasil_05.json
"""
import json
import os

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(KITAP, "hap")

SINIR = {"A": (8, 12, 6, 8, 4, 6), "B": (4, 6, 4, 5, 2, 3), "C": (2, 4, 2, 3, 1, 2)}


def kelime(s):
    import re
    return len(re.sub(r"<[^>]+>", "", s).split())


def kontrol(d):
    k = d["kademe"]
    pmin, pmax, hmin, hmax, kmin, kmax = SINIR[k]
    f = d["fasil"]
    assert pmin <= len(d["pozisyonlar"]) <= pmax, (f, "pozisyonlar", len(d["pozisyonlar"]))
    assert hmin <= len(d["hap"]) <= hmax, (f, "hap", len(d["hap"]))
    assert kmin <= len(d["karistirilan"]) <= kmax, (f, "karistirilan", len(d["karistirilan"]))
    for p, a in d["pozisyonlar"]:
        if kelime(a) > 8:
            print(f"  ! {f} pozisyon {p}: {kelime(a)} kelime")
    for h in d["hap"]:
        if kelime(h) > 30:
            print(f"  ! {f} hap: {kelime(h)} kelime: {h[:50]}")
    for e, p, n in d["karistirilan"]:
        if kelime(e) > 8:
            print(f"  ! {f} karıştırılan eşya: {kelime(e)} kelime: {e}")
        if kelime(n) > 12:
            print(f"  ! {f} karıştırılan neden: {kelime(n)} kelime: {n}")


def yaz(d):
    kontrol(d)
    yol = os.path.join(OUT, "fasil_%02d.json" % d["fasil"])
    with open(yol, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print("yazıldı:", yol)


# ---------------------------------------------------------------- GYK
GYK = {
    "tur": "hap",
    "fasil": 0,
    "kademe": "A",
    "sinavda": "Son 5 sınavda 16 kez, çoğu “hangi kurala göre hangi pozisyonda” kalıbıyla: kuralların sırası "
               "(doğru/yanlış ifade), perakende takım şartları ve takım sayılmayan paketler, mahfaza (5(a)), "
               "demonte set (2(a) + 3(c)), yalnız GYK 1 ve 6 ile çözülen eşya, başlığın bağlayıcı olmaması, "
               "2(a)’nın Bölüm I–VI’ya uygulanmaması ve GYK 6 seviye seçimi.",
    "pozisyonlar": [
        ["GYK 1", "Başlık gösterici; pozisyon metni ve notlar bağlayıcı"],
        ["GYK 2(a)", "Eksik/demonte eşya, ayırt edici nitelik varsa tamamlanmış gibi"],
        ["GYK 2(b)", "Maddeye atıf karışımını ve bileşimini de kapsar"],
        ["GYK 3(a)", "Eşyayı en özel tanımlayan pozisyon önce gelir"],
        ["GYK 3(b)", "Karışım, bileşik eşya, takım: esas nitelik"],
        ["GYK 3(c)", "Geçerli pozisyonların numara sırasına göre sonuncusu"],
        ["GYK 4", "1–3 yetmezse en çok benzeyen eşyanın pozisyonu"],
        ["GYK 5(a)", "Eşyaya özgü, dayanıklı mahfaza eşyayla birlikte"],
        ["GYK 5(b)", "Normal ambalaj eşyayla; tekrar kullanılabilir olan hariç"],
        ["GYK 6", "Alt pozisyon: yalnız aynı tire seviyesi karşılaştırılır"],
    ],
    "hap": [
        "<b>Sıra:</b> 1 → 2 → 3(a) → 3(b) → 3(c) → 4; pozisyon bulununca sonrakine geçilmez "
        "(3 ile bulunduysa 4 uygulanmaz). 5 eşyaya göre eklenir; 6 alt pozisyonu belirler.",
        "<b>Başlık değil not:</b> başlıklar yasal dayanak değildir. Notta veya pozisyon metninde aksine hüküm "
        "varsa 2(b) ve 3 uygulanmaz (15.03 “karıştırılmamış”, Fasıl 97 Not 5(b)).",
        "<b>Yalnız GYK 1 ve 6:</b> not veya pozisyon metni eşyayı adıyla karşılıyorsa takım görünse de 3(b) "
        "gerekmez: ilk yardım kutusu 30.06 (Fasıl 30 Not 4), seyahat dikiş takımı 96.05.",
        "<b>2(a):</b> eksik eşya tamamlanmışın ayırt edici niteliğini taşımalı; demonte = vida, cıvata, perçin "
        "veya kaynakla birleşen parçalar. Çubuk, disk, boru taslak sayılmaz; normalde Bölüm I–VI’ya uygulanmaz.",
        "<b>Perakende takım üç şart:</b> farklı pozisyonlara girebilen en az iki farklı eşya; belirli ihtiyaç "
        "veya işlev; yeniden paketlemeden son kullanıcıya satış. Altı fondü çatalı veya kahve + fincan takım değildir.",
        "<b>Esas nitelik (3(b)):</b> içerik, hacim, ağırlık, miktar, kıymet veya kullanımdaki önem belirler: "
        "spagetti + rendelenmiş peynir + sos 19.02, çizim takımı 90.17, saç tuvalet takımı 85.10.",
        "<b>3(a):</b> isimle tanım sınıf tanımından, açık tanım eksik tanımdan önce gelir: tıraş makinesi 85.10 "
        "(84.67/85.09 değil), taşıt halısı 57.03 (87.08 değil), uçak emniyet camı 70.07.",
        "<b>5(a) şartları:</b> eşyaya göre şekillendirilmiş, uzun süre kullanılabilir, eşyayla birlikte sunulan ve "
        "normal olarak onunla satılan kap; bütünüyle esas niteliği kap olan eşyaya (gümüş çay kupası) uygulanmaz.",
    ],
    "karistirilan": [
        ["Keman veya av tüfeği ile özel mahfazası", "GYK 5(a)",
         "Birlikte sunulursa eşyanın pozisyonunda; ayrı gelirse kendi pozisyonunda"],
        ["Demonte masa ve 2 sandalye, tek kutuda", "GYK 3(c)",
         "GYK 1, 2(a), 3(c), 6: esas nitelik yok → sonuncu 94.03"],
        ["İki not defteri ve bir şişe parfüm", "GYK 1",
         "Takım değil: ortak ihtiyaç yok; her biri kendi pozisyonunda"],
        ["İlk yardım kutusu (ilaç, sargı, makas)", "GYK 1, 6",
         "Fasıl 30 Not 4 doğrudan 30.06’ya gönderir; 3(b) gerekmez"],
        ["Yenilebilir hayvan bağırsağı ve midesi", "GYK 1",
         "Fasıl 2 başlığına rağmen not gereği 05.04"],
        ["Tüm parçalarıyla demonte bisiklet", "GYK 2(a)",
         "Monte edilmiş bisiklet gibi 87.12; GYK 1, 2(a), 6"],
    ],
}

# ---------------------------------------------------------------- Fasıl 1
F1 = {
    "tur": "hap",
    "fasil": 1,
    "kademe": "C",
    "sinavda": "Son 5 sınavda 1 kez, “hangisi 3. fasılda sınıflandırılmaz” kalıbıyla: balina memeli olduğundan "
               "canlı hali 01.06’dadır. Gezici hayvan sergilerinin (95.08) faslı ayrıca bir Fasıl 95 sorusunda "
               "soruldu.",
    "pozisyonlar": [
        ["01.01", "At, eşek, katır, bardo; evcil veya yabani"],
        ["01.05", "Yalnız evcil kümes: tavuk, ördek, kaz, hindi, beç"],
        ["01.06", "Artık: memeli (balina, yunus, fok), sürüngen, kuş, arı"],
    ],
    "hap": [
        "<b>Fasıl 1 Notu (dışı):</b> balık ve su omurgasızları (03.01, 03.06–03.08), mikroorganizma kültürleri "
        "(30.02), sirk ve gezici hayvan gösterisi hayvanları (95.08).",
        "<b>Yabanilik pozisyonu değiştirmez:</b> yabani at, sığır, domuz, koyun-keçi kendi pozisyonunda; yalnız "
        "01.05 evcil türlerle sınırlı (yabani ördek, sülün, güvercin 01.06). Yavru ana türün pozisyonundadır.",
        "<b>Cansız hayvan:</b> nakliyede ölen hayvan eti yenilebilirse Fasıl 2 veya 04.10, değilse 05.11.",
    ],
    "karistirilan": [
        ["Canlı balina, yunus, fok", "01.06", "Memelidir; Fasıl 3 yalnız balık ve su omurgasızları"],
        ["Canlı deniz kaplumbağası", "01.06", "Sürüngen; deniz kulağı 03.07, deniz hıyarı 03.08"],
    ],
}

# ---------------------------------------------------------------- Fasıl 2
F2 = {
    "tur": "hap",
    "fasil": 2,
    "kademe": "C",
    "sinavda": "Son 5 sınavda 1 kez, GYK sorusu olarak: başlık “Etler ve yenilen sakatat” olmasına rağmen "
               "bağırsak, mesane ve midenin 05.04’e gitmesi GYK 1’in (notlar bağlayıcı) gereğidir.",
    "pozisyonlar": [
        ["02.06", "Sığır, domuz, koyun, keçi, at ailesi sakatatı"],
        ["02.08", "01.06 hayvanlarının eti: tavşan, kurbağa, balina"],
        ["02.10", "Tuzlu, salamura, kurutulmuş, tütsülenmiş et; et unu"],
    ],
    "hap": [
        "<b>Fasıl 2 Notu (dışı):</b> yenmeyen et ve sakatat 05.11; bağırsak, mesane, mide 05.04; hayvan kanı "
        "05.11 veya 30.02; yenilen cansız böcek 04.10; 02.09 dışı hayvansal yağlar Fasıl 15.",
        "<b>Hazırlık sınırı:</b> kıyma, enzimle yumuşatma, pişirmeden ön haşlama, nakliye tuzu ve MAP ambalaj "
        "Fasıl 2’de; pişirme, baharat, ekmek kırıntısı kaplama, sosis ve pate Fasıl 16.",
    ],
    "karistirilan": [
        ["Yenilebilir işkembe, bağırsak, mesane", "05.04", "Sakatat sayılmaz; başlık değil not bağlayıcı (GYK 1)"],
        ["Dondurulmuş balina eti", "02.08", "01.06 memelisinin eti; Fasıl 3 değil"],
    ],
}

# ---------------------------------------------------------------- Fasıl 3
F3 = {
    "tur": "hap",
    "fasil": 3,
    "kademe": "B",
    "sinavda": "Son 5 sınavda 2 kez, “hangisi … fasılda yer almaz” kalıbıyla: balina memeli olduğundan Fasıl 3 "
               "dışı (01.06), deniz kulağı ve deniz hıyarı içeride; alabalık yumurtası Fasıl 3’tür, Fasıl 4’te "
               "yer almaz.",
    "pozisyonlar": [
        ["03.02", "Taze/soğutulmuş balık; yenilebilir yumurta, karaciğer dahil"],
        ["03.04", "Fileto ve kılçığı alınmış balık eti"],
        ["03.05", "Kurutulmuş, tuzlu, salamura, tütsülenmiş balık"],
        ["03.06", "Kabuklular; kabuğunda buharda veya suda pişmiş dahil"],
        ["03.07", "Yumuşakçalar: midye, ahtapot, kalamar, salyangoz, deniz kulağı"],
        ["03.08", "Diğer su omurgasızları: deniz hıyarı, kestanesi, anası"],
    ],
    "hap": [
        "<b>Fasıl 3 Not 1 (dışı):</b> 01.06 memelileri ve etleri (02.08, 02.10); yenmeyen cansız balık ve su "
        "hayvanları (Fasıl 5); yenmeyen un-pellet (23.01); havyar ve havyar benzerleri (16.04).",
        "<b>Pişirme Fasıl 16’ya gönderir</b> (balık 16.04, diğerleri 16.05). İstisna: tütsülerken pişme, kabuğu "
        "içinde buharda/suda pişmiş kabuklu, kabuk açmak için ısı şoku, yenilebilir un-pellet (03.09).",
        "<b>Balık yumurtası:</b> yenilebilir ve yalnız Fasıl 3 işlemi görmüşse balığın haline göre 03.02, 03.03 "
        "veya 03.05; havyar 16.04; kuluçkalık veya yem amaçlı 05.11.",
        "<b>Fileto (03.04):</b> omurgaya paralel kesilmiş yan et şeridi; deri ve küçük kılçık kalması bozmaz, "
        "iki yanın birleşik kalması bozar. Ekmek kırıntısıyla kaplanmış fileto 16.04.",
        "<b>Fasıl 16 Not 2:</b> müstahzarda balık, kabuklu, yumuşakça ağırlıkça %20’den fazlaysa Fasıl 16; "
        "doldurulmuş makarna (karidesli mantı 19.02) ile 21.03 ve 21.04 hariç.",
    ],
    "karistirilan": [
        ["Canlı balina, yunus, fok", "01.06", "Memeli; eti 02.08, tuzlu veya tütsülü 02.10"],
        ["Alabalık yumurtası (yenilebilir, taze)", "03.02",
         "Balık sakatatı; dondurulmuş 03.03, tuzlu 03.05. Fasıl 4 değil"],
        ["Kabuğu çıkarılıp kaynatılmış karides", "16.05", "Kabuğu içinde pişirilseydi 03.06’da kalırdı"],
    ],
}

# ---------------------------------------------------------------- Fasıl 4
F4 = {
    "tur": "hap",
    "fasil": 4,
    "kademe": "A",
    "sinavda": "Son 5 sınavda 2 kez doğrudan, 4 kez seçeneklerde: yenilebilir kurutulmuş-tuzlu çekirge 04.10 "
               "(yenmeyen böcek 05.11); “hangisi 4. fasılda yer almaz” kalıbında alabalık yumurtası (Fasıl 3) "
               "ve kaplumbağa yumurtası (04.10); eşleştirmelerde suni bal 17.02, yumurta sarısı 04.08.",
    "pozisyonlar": [
        ["04.01", "Süt ve krema; konsantre edilmemiş, tatlandırılmamış"],
        ["04.02", "Konsantre veya tatlandırılmış süt, krema; süt tozu"],
        ["04.03", "Yoğurt, kefir, yayıkaltı; şekerli, meyveli olabilir"],
        ["04.04", "Peyniraltı suyu; tabii süt bileşenlerinden ürünler"],
        ["04.05", "Tereyağı, diğer süt yağları, sürülerek yenilen süt ürünü"],
        ["04.06", "Peynir ve lor; kaplanmış peynir dahil"],
        ["04.07", "Kabuklu kuş yumurtası; pişmiş, kuluçkalık dahil"],
        ["04.08", "Kabuksuz yumurta ve yumurta sarısı"],
        ["04.09", "Tabii bal; şeker veya başka madde katılmamış"],
        ["04.10", "Yenilebilir böcek, kaplumbağa yumurtası, salangan yuvası"],
    ],
    "hap": [
        "<b>Tereyağı (Not 3(a)):</b> yalnız sütten; süt yağı %80 veya fazla, %95’i geçmeyen; yağsız katı madde "
        "en fazla %2, su en fazla %16; ilave emülsifiye edici içermez.",
        "<b>Sürülerek yenilen süt ürünü (Not 3(b)):</b> tek katı yağı süt yağı; süt yağı %39 veya fazla fakat "
        "%80’den az; yağ içinde su emülsiyonu → 04.05.",
        "<b>Peyniraltı suyu peyniri (Not 4) → 04.06:</b> kuru maddede süt yağı %5 veya fazla; kuru madde "
        "%70–85; kalıplanmış veya kalıba getirilmeye müsait.",
        "<b>Fasıl dışı (Not 5):</b> yenmeyen cansız böcek 05.11; kuru maddede %95’ten fazla laktozlu peyniraltı "
        "suyu ürünü 17.02; tabii bileşeni değiştirilmiş süt ürünü 19.01/21.06; albüminler 35.02.",
        "<b>Yoğurt (Not 2):</b> şeker, meyve, kakao, çikolata, kahve, hububat içerebilir; katkı süt içeriğini "
        "ikame etmemeli ve yoğurt karakteri korunmalı → 04.03.",
        "<b>Böcek (Not 6) → 04.10:</b> insan tüketimine uygun cansız böcek; taze, dondurulmuş, kurutulmuş, "
        "tütsülenmiş, tuzlanmış, salamura ya da unu. Başka şekilde hazırlanmışı genellikle Bölüm IV.",
        "<b>Yumurtada ölçüt kabuk:</b> kabuklu (pişmiş olsa da) 04.07; kabuksuz ve sarısı 04.08; baharatlı "
        "yumurta ürünü 21.06. Balık yumurtası Fasıl 3, kaplumbağa yumurtası 04.10.",
        "<b>Bal:</b> şeker veya başka madde katılmamış tabii bal 04.09; suni bal ve tabii balla karışımı 17.02.",
    ],
    "karistirilan": [
        ["Diyabetik suni bal (tabii balla karışık)", "17.02", "Suni bal ve karışımı 04.09’a girmez"],
        ["Alabalık yumurtası", "Fasıl 3", "Fasıl 4 yalnız kuş ve kümes hayvanı yumurtası"],
        ["Yenmeyen cansız böcek", "05.11", "Not 5(a); insan tüketimine uygunsa 04.10"],
        ["Süt yağı yerine bitkisel yağlı süt ürünü", "19.01", "Not 5(c): tabii bileşen değiştirilmiş; ya da 21.06"],
        ["Kakao ile aromalandırılmış sütten içecek", "22.02", "04.02 dışı (açıklama notu); dondurma ise 21.05"],
        ["Yumurta beyazı (albümin)", "35.02", "04.08 yalnız kabuksuz yumurta ve sarısını kapsar"],
    ],
}

# ---------------------------------------------------------------- Fasıl 5
F5 = {
    "tur": "hap",
    "fasil": 5,
    "kademe": "B",
    "sinavda": "Son 5 sınavda 2 kez doğrudan, 2 kez seçeneklerde: yenmeyen cansız böcek 05.11 (yenilebilen "
               "04.10) ve başlığa rağmen bağırsak-mide 05.04 (GYK 1); “4. fasılda yer almaz” sorusunda salyangoz "
               "kabuğu unu (05.08) seçenekteydi.",
    "pozisyonlar": [
        ["05.04", "Bağırsak, mesane, mide (yenilebilir olsa da; balığınki hariç)"],
        ["05.05", "Kuş derisi, tüy; yalnız temizlenmiş veya korunmuş"],
        ["05.07", "Fildişi, boynuz, toynak, gaga; şekil verilmemiş"],
        ["05.08", "Mercan, yumuşakça kabuğu, mürekkep balığı kemiği; tozu"],
        ["05.11", "Artık: kan, sperm, at kılı, sünger, yenmeyen böcek"],
    ],
    "hap": [
        "<b>Fasıl 5 Not 1 (dışı):</b> yenilebilir ürünler (bağırsak, mesane, mide ve kan hariç); ham deri ve "
        "kürk (Fasıl 41/43); dokumaya elverişli madde (Bölüm XI; at kılı hariç); fırça başları (96.03).",
        "<b>Fildişi (Not 3, tüm tarifede):</b> fil, hipopotam, mors, deniz gergedanı, yaban domuzu dişleri, "
        "gergedan boynuzu ve bütün hayvanların dişleri.",
        "<b>At kılı (Not 4, tüm tarifede):</b> at veya sığır türü hayvanların yele ve kuyruk kılları → 05.11; "
        "eğrilmiş veya uçları düğümlenmiş at kılı Fasıl 51.",
        "<b>Basit hazırlama sınırı:</b> kemik, fildişi, boynuz, mercan, kabuk kesilip temizlenmişse burada; "
        "levha, çubuk, boru veya kalıplanmış hali 96.01. İşlenmiş saç 67.03, işlenmiş tüy 67.01.",
        "<b>Eczacılık guddesi:</b> taze, dondurulmuş veya geçici korunmuş 05.10; kurutulmuş veya öz halinde 30.01. "
        "Ak amber ve misk 05.10; sarı amber 25.30.",
    ],
    "karistirilan": [
        ["Yenilebilir hayvan bağırsağı, işkembe", "05.04", "Fasıl 2 başlığına rağmen; Not 1(a) istisnası (GYK 1)"],
        ["Yenmeyen cansız böcek", "05.11", "Yenilebilir böcek 04.10 (Fasıl 4 Not 6)"],
        ["Salyangoz kabuğu unu", "05.08", "Kabuk tozu; yenilebilir ürün değil, Fasıl 4 dışı"],
    ],
}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for d in (GYK, F1, F2, F3, F4, F5):
        yaz(d)
