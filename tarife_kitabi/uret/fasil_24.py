#!/usr/bin/env python3
import json, os

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

T_ESYA = "Eşya → 4’lü pozisyon"
T_OLUMSUZ = "Olumsuz teşhis"
T_FARKLI = "Farklı/aynı pozisyon veya fasıl"
T_NOT = "Fasıl notu · Tanım/Eşik"
T_GYK = "Genel Yorum Kuralı"
T_ESLES = "Eşleştirme / Boşluk doldurma"
T_COKTAN = "Çoktan-çoğa (I–IV)"
T_SENARYO = "Senaryo"


def q(soru, secenekler, cevap, tip, gerekce, dayanak):
    return {"soru": soru, "secenekler": secenekler, "cevap": cevap, "tip": tip,
            "gerekce": gerekce, "dayanak": dayanak}


d = {
 "tur": "fasil",
 "fasil": 24,
 "baslik": "Tütün ve tütün yerine geçen işlenmiş maddeler; nikotin içersin içermesin yanma olmadan solunan ürünler; insan vücuduna nikotin almak için kullanılan nikotin içeren diğer ürünler",
 "bolum": "IV",
 "oz": {
  "vurgu": "Fasıl 24’te ilk soru şudur: Ürün yakılarak mı tüketiliyor, yanmadan mı soluyor, yoksa tütün içermeden nikotini başka bir yolla (ağız, deri) mi veriyor? Yanmadan solunan ürünler ile tütünsüz nikotin ürünleri 24.04’tedir ve Not 2 gereği bu faslın diğer pozisyonlarına göre önceliklidir. Yakılan veya çiğnenen tütünde ayrım işlenmişlik derecesine göre yapılır: yaprak 24.01, sarılmış ürün 24.02, diğer mamul tütün 24.03.",
  "maddeler": [
   "Fasıl yalnızca yaprak ve işlenmiş tütünü değil, tütün içermeyen ve tütün yerine kullanılan işlenmiş ürünleri de kapsar (ör. marul yaprağından sigara, tütünsüz içilen karışımlar).",
   "Hem 24.04 hem de bu faslın başka bir pozisyonuna girebilen ürün 24.04’te sınıflandırılır (Fasıl 24 Not 2).",
   "Tıbbi sigaralar Fasıl 30’a gider; buna karşılık sigarayı bırakmaya yardımcı nikotinli sakız, tablet ve bantlar Fasıl 30 ve 21.06 dışında kalır ve 24.04’tedir.",
   "Nikotinin kendisi (tütünden çıkarılmış veya sentetik) 29.39’da; yeniden doldurulabilir e-sigara cihazı 85.43’te; sıvı içeren kartuş ve tanklar ile tek kullanımlık e-sigaralar ise 24.04’tedir."
  ]
 },
 "karar_tablosu": {
  "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
  "satirlar": [
   ["1", "Kimyasal olarak izole nikotin veya tuzu mu? (tütünden çıkarılmış ya da sentetik)", "<b>29.39</b>"],
   ["2", "Tıbbi sigara mı?", "Fasıl <b>30</b>"],
   ["3", "Yeniden doldurulabilir veya değiştirilebilir kartuşla kullanılan e-sigara ya da ısıtma cihazı mı?", "<b>85.43</b>"],
   ["4", "Yanma olmadan solunması amaçlanan ürün mü? (e-sıvı, kartuş, tank, ısıtılan tütün çubuğu, tek kullanımlık e-sigara)", "<b>24.04</b> (tütün içerse bile, Not 2)"],
   ["5", "Tütün içermeyen, nikotinli ve soluma dışında bir yolla (ağız, deri) kullanılan ürün mü?", "<b>24.04</b> (NRT ürünleri dahil)"],
   ["6", "Puro, uçları açık puro, sigarillo veya sigara mı?", "<b>24.02</b> (tütün oranı önemsiz)"],
   ["7", "İçime hazır tütün, çiğneme tütünü, enfiye, homojenize tütün, tütün hülasası veya tütünsüz içilen karışım mı?", "<b>24.03</b> (kenevir hariç → <b>12.11</b>)"],
   ["8", "Yaprak tütün (kesilmiş, sapı koparılmış, salçalanmış olsa bile) veya tütün döküntüsü mü?", "<b>24.01</b>"]
  ],
  "dipnot": "* Fasıl dışı komşular: ekim amaçlı tütün tohumu 12.09; sigara kağıdı 48.13; pipo, nargile ve ağızlık 96.14; çakmak 96.13; 38.08’deki böcek öldürücüler; tütün işleme makineleri 84.78."
 },
 "pozisyon_haritasi": [
  ["24.01", "Yaprak tütün; tütün döküntüleri", "İçime hazır olmayan yaprak; kesilmiş, sapı koparılmış, salçalanmış olabilir", "Kurutulmuş veya fermente yaprak; sap, orta damar, kırpıntı, toz"],
  ["24.02", "Puro, uçları açık puro, sigarillo ve sigaralar", "Tütün veya ikamesinden; karışımda oran önemsiz; yakılarak içilir", "Sigara, sigarillo, marul yaprağından tütünsüz sigara"],
  ["24.03", "Diğer mamul tütün ve ikameleri; homojenize tütün; hülasa ve esanslar", "Yakılarak içilen, çiğnenen veya koklanan tütün; sarılmamış", "Pipo ve sarmalık tütün, nargile tütünü, çiğneme tütünü, enfiye"],
  ["24.04", "Yanma olmadan solunan ürünler; nikotin içeren diğer ürünler", "Yanma yok; ya da tütünsüz nikotin ağız veya deri yoluyla; Not 2 önceliği", "E-sıvı, ısıtılan tütün çubuğu, tek kullanımlık e-sigara, nikotinli sakız ve bant"]
 ],
 "notlar": [
  ["Fasıl 24 Not 1", "Tıbbi sigaralar bu fasla dahil değildir → Fasıl 30."],
  ["Fasıl 24 Not 2", "Hem 24.04 hem de bu faslın başka bir pozisyonunda sınıflandırılabilen ürünler <b>24.04</b>’te sınıflandırılır. (Not 2 ve Not 3, Türkçe metinde “Altpozisyon Notları” başlığı altında basılmıştır; 24.04 Açıklama Notu da “bu Faslın 3 no’lu Notu”na atıf yapar.)"],
  ["Fasıl 24 Not 3", "24.04 anlamında “yanma olmadan solunan”: <b>ısı yoluyla veya diğer yollarla</b> yanma olmadan soluma. Açıklama Notu ısıtma yollarını elektrikli cihaz, kimyasal reaksiyon ve karbon ısı kaynağı; ısıtma dışı yolları kimyasal işlem ve ultrasonik buharlaştırma olarak örnekler."],
  ["Genel Açıklamalar", "Fasıl, yaprak ve işlenmiş tütünün yanında tütün içermeyen, tütün yerine kullanılan işlenmiş ürünleri de kapsar. Kurutma yöntemleri: güneşte, havada, hava akımında ve ateşte kurutma; ardından kontrollü tabii fermantasyon veya suni olarak tekrar kurutma."],
  ["24.01 Açıklama Notu", "Yaprak tütün bütün bitki veya yaprak halinde olabilir; sapı koparılmış, damarı çıkarılmış, kırılmış veya kesilmiş (şekil verilerek kesilmiş dahil) olabilir, ancak <b>içime hazır tütün hariçtir</b>. Harmanlanmış ve uygun bir sıvı ile salçalanmış veya likörlenmiş yapraklar da buradadır. Döküntüler: saplar, gövdeler, orta damarlar, kırpıntılar, tozlar."],
  ["24.02 Açıklama Notu", "Pozisyon puro, uçları açık puro, sigarillo ve sigara ile sınırlıdır; diğer içilen tütün 24.03’tedir. Tütün ile ikamesinin karışımında <b>oran dikkate alınmaz</b>. Ne tütün ne nikotin içeren, marul yaprağından yapılan sigaralar da buradadır. Benzer görünümlü ancak yanmadan solunması amaçlanan ürünler 24.04’e, tıbbi sigaralar Fasıl 30’a gider; sigara içme alışkanlığını kırmak üzere formüle edilmiş, tıbbi özelliği olmayan özel sigaralar 24.02’de kalır."],
  ["24.03 Açıklama Notu", "Kapsam: içilen tütün (pipo için veya sigara yapmak için imal edilmiş), çiğneme tütünü, enfiye, enfiye imali için sıkıştırılmış veya likörlenmiş tütün, tütünsüz içilen karışımlar (kenevir gibi ürünler hariç → 12.11), homojenize veya yeniden tertip edilmiş tütün (tütün yaprakları, döküntü ve tozlardan ayrılmış tütünün aglomere edilmesiyle; sargı için tabaka, dolgu için şerit) ve tütün hülasa ve ıtırları (esas olarak böcek ve parazit öldürücü imalatında kullanılır). Hariç: nikotin (29.39), 38.08’deki böcek öldürücüler."],
  ["24.04 Açıklama Notu", "(A) Yanmadan solunması amaçlanan ürünler: e-sigaralar için nikotinli solüsyonlar; elektrikle, kimyasal reaksiyonla veya karbon ısı kaynağıyla ısıtılan sistemlerde kullanılan tütün ürünleri; tütün veya nikotin içermeyip ikame içeren e-sigara ürünleri; ultrasonik vb. aerosol ürünleri; ürün ile dağıtım mekanizmasını tek gövdede birleştiren, yeniden doldurulamayan ve şarj edilemeyen tek kullanımlık e-sigaralar. (B) Tütün içermeyen ve nikotini soluma dışında bir yolla (ör. çiğneme, çözme, koklama, deri yoluyla emilim) vücuda veren ürünler; eğlence amaçlı ürünler ile nikotin replasman tedavisi (NRT) ürünleri dahil. Hariç: yakılarak solunan ürünler (24.02, 24.03), çiğneme tütünü ve enfiye (24.03), nikotin (29.39)."],
  ["Fasıl 30 Not 1", "Nikotin içeren, sigarayı bırakmaya yardımcı tablet, ciklet veya bant (transdermal sistemler) Fasıl 30’a girmez → 24.04. Nikotin içeren sakız 21.06’dan da hariç tutulur (21.06 Açıklama Notu)."],
  ["85.43 Açıklama Notu", "Yeniden doldurulabilir veya değiştirilebilir kartuşla kullanılan e-sigaralar ve ısıtılan tütün cihazları 85.43’tedir. Sıvı veya çözelti içeren kartuş ve tanklar (ısıtma elemanı veya atomizörle sunulsa bile) ve tek kullanımlık e-sigaralar 85.43 dışında, 24.04’tedir. Pipo veya nargile şeklindeki e-sigaralar da 96.14’te değil, 85.43’tedir."]
 ],
 "sinir_komsulari": [
  ["Ekim amaçlı tütün tohumu", "12.09", "Ekime mahsus tohumlar pozisyonu"],
  ["Kenevir (cannabis) gibi içilen bitkiler", "12.11", "24.03 hariç tutması"],
  ["Tütün hülasası ve ıtırı", "24.03", "13.02’deki bitkisel hülasalardan hariç tutulur, Fasıl 24’e gelir"],
  ["Nikotin (tabii veya sentetik alkaloid) ve tuzları", "29.39", "24.03 ve 24.04 hariç tutması"],
  ["Nikotinli sakız", "24.04", "21.06 hariç tutması"],
  ["Sigarayı bırakmaya yardımcı nikotinli tablet, ciklet, bant", "24.04", "Fasıl 30 Not 1 hariç tutması"],
  ["Tıbbi sigara", "Fasıl 30", "Fasıl 24 Not 1"],
  ["Tütün esaslı hazır böcek öldürücüler", "38.08", "24.03 hariç tutması"],
  ["Yeniden doldurulabilir e-sigara cihazı, ısıtılan tütün cihazı", "85.43", "Cihaz; sarf ürünü (sıvı, kartuş, tütün çubuğu) 24.04"],
  ["Tek kullanımlık e-sigara (nargile veya pipo şeklinde olsa bile)", "24.04", "85.43 hariç tutması; 24.04 Açıklama Notu (A)(5)"],
  ["Sigara kağıdı (defter veya boru halinde)", "48.13", "Kağıt; tütün içermez"],
  ["Pipo, nargile, puro ve sigara ağızlıkları", "96.14", "Tütün içme aleti; elektronik olanı 85.43"],
  ["Çakmak", "96.13", "Ateşleyici"],
  ["Deri veya plastikten tütün kesesi, sigara tabakası", "42.02", "Mahfaza pozisyonu"],
  ["Tütün kıyma ve sap ayırma makineleri", "84.78", "Tütün işleme makinesi"]
 ],
 "tuzaklar": [
  "<b>Yanmadan solunan tütün ürünü 24.03 değil, 24.04’tür.</b> Isıtılan tütün çubukları yeniden tertip edilmiş tütün içerse de Fasıl 24 Not 2 gereği 24.04 önceliklidir.",
  "<b>Çiğneme tütünü ≠ nikotinli sakız.</b> Tütün içerdikleri için çiğneme tütünü ve enfiye 24.03’te; tütün içermeyen nikotinli sakız 24.04’te.",
  "<b>“Sigarayı bırakmaya yardımcı” ibaresi Fasıl 30 demek değildir.</b> Nikotinli bant, tablet ve ciklet 24.04’te; tıbbi özelliği olmayan alışkanlık kırıcı sigaralar 24.02’de; yalnızca tıbbi sigaralar Fasıl 30’da.",
  "<b>Nikotinin kendisi Fasıl 24’te değildir.</b> Tütünden çıkarılmış veya sentezle elde edilmiş nikotin 29.39’dadır; tütün hülasası ise 24.03’te kalır.",
  "<b>Cihaz ile sarf ürünü ayrılır.</b> Yeniden doldurulabilir e-sigara 85.43; sıvı, kartuş ve tank 24.04; tek kullanımlık e-sigara bütün olarak 24.04.",
  "<b>Kesilmiş tütün her zaman mamul tütün değildir.</b> Kesilmiş veya şekil verilerek kesilmiş yaprak 24.01’de kalır; içime hazır hale getirilince 24.03’e geçer.",
  "<b>Karışım oranına bakılmaz.</b> Tütün ile tütün ikamesi karışımından sigara, oran ne olursa olsun 24.02’dedir; hiç tütün içermeyen sigara da 24.02’dedir.",
  "<b>Tütünsüz içilen karışım 24.03’tür; kenevir ise 12.11.</b>",
  "<b>Pipo ve nargile Fasıl 24’te değildir.</b> 96.14’tedir; nargile tütünü 24.03’te, elektronik nargile ise 85.43’te (tek kullanımlıksa 24.04)."
 ],
 "hafiza": {
  "kanca": "YAPRAK – SARMA – DİĞER – DUMANSIZ",
  "aciklama": "<b>YAPRAK</b> 24.01 (tarladan gelen yaprak ve döküntü) · <b>SARMA</b> 24.02 (puro, sigarillo, sigara) · <b>DİĞER</b> 24.03 (pipo, çiğneme, enfiye, homojenize, hülasa) · <b>DUMANSIZ</b> 24.04 (buhar, ısıtma ya da ağız-deri yoluyla nikotin). Sıra işlenmişliği izler; son sözü her zaman 24.04 söyler (Not 2)."
 },
 "sinav_odagi": [
  "Bu fasıl çıkmış sorularda daha çok seçeneklerde ve çeldirici olarak yer almıştır; doğrudan Fasıl 24’ü soran soru azdır.",
  "Elektronik sigara cihazı, kartuşu, tütün içeren sigara ve sigara kağıdı üzerinden boşluk doldurma: cihaz (85.43) ile sarf ürününün (24.04) ayrılması, sigaranın 24.02’de, kağıdının 48.13’te kalması.",
  "“Hangisi Fasıl 30’da yer almaz?” kalıbında sigarayı bırakmaya yardımcı nikotinli bandın Fasıl 30 dışında, 24.04’te olması.",
  "Bölüm yapısı: tütünün gıda sanayii ürünleriyle birlikte Bölüm IV’ün son faslı olması; “aynı bölümde yer alan eşya” ve tarife sıralaması (içki → sigara → sigara tabakası → çakmak) soruları.",
  "Tütün çevresindeki eşyanın ayrılması: sigara kağıdının Fasıl 49’da değil 48.13’te, sigara kutusu ve tütün kesesinin malzemesine göre 42.02 veya başka fasıllarda yer alması."
 ],
 "cikmis_ornekler": [
  {
   "soru": "Elektronik sigaralar ……… pozisyonunda; söz konusu cihazlarda kullanılan kartuşlar ………, tütün içeren sigaralar ………, sigara kağıdı ……… pozisyonlarında sınıflandırılır. Yukarıdaki cümlede boşlukları tamamlayan ifadeler hangi seçenekte doğru olarak verilmiştir?",
   "secenekler": ["85.43 / 24.02 / 24.04 / 48.13", "24.02 / 24.04 / 85.43 / 48.13", "24.04 / 85.43 / 24.02 / 48.13", "85.43 / 24.04 / 24.02 / 48.13", "48.13 / 24.04 / 24.02 / 85.43"],
   "cevap": "D",
   "aciklama": "Yeniden doldurulabilir e-sigara cihazı 85.43’tedir; sıvı içeren kartuş ve tanklar 85.43 Açıklama Notunda hariç tutularak 24.04’e gönderilir. Tütün içeren sigara 24.02’de, sigara kağıdı 48.13’te yer alır."
  },
  {
   "soru": "Tarife Cetveline göre aşağıdakilerden hangisi 30. Fasılda yer almaz?",
   "secenekler": ["İnsan kanı", "Gaz bezi", "Sigara bırakmaya yardımcı bant", "Kızamık aşısı"],
   "cevap": "C",
   "aciklama": "Fasıl 30 Not 1, nikotin içeren ve sigarayı bırakmaya yardımcı tablet, ciklet ve bantları (transdermal sistemler) Fasıl 30 dışında bırakır; bunlar 24.04’te sınıflandırılır."
  }
 ],
 "ozet": [
  "Yaprak ve döküntü 24.01; içime hazır hale getirilen tütün 24.03.",
  "Puro, sigarillo ve sigara 24.02; tütün oranı önemsizdir, hiç tütün içermeyebilir.",
  "Pipo ve sarmalık tütün, nargile tütünü, çiğneme tütünü, enfiye, homojenize tütün ve tütün hülasası 24.03.",
  "Yanma yoksa ya da tütünsüz nikotin ağız veya deri yoluyla alınıyorsa 24.04; Not 2 ile fasıl içinde önceliklidir.",
  "Fasıl dışı: nikotin 29.39, tıbbi sigara Fasıl 30, e-sigara cihazı 85.43, kenevir 12.11, sigara kağıdı 48.13, pipo ve nargile 96.14.",
  "“Sigarayı bırakmaya yardımcı” nikotinli bant, sakız ve tablet ilaç değil, 24.04 ürünüdür."
 ],
 "sorular": [
  q("Tarife Cetveline göre, elektronik sigaralarda kullanılmak üzere şişelenmiş, nikotin içeren aromalı solüsyon (e-sıvı) hangi pozisyonda sınıflandırılır?",
    ["24.03", "85.43", "29.39", "24.04", "38.24"], "D", T_ESYA,
    "24.04 Açıklama Notu (A)(1), e-sigaralarda veya benzeri kişisel elektrikli buharlaştırma cihazlarında kullanılması amaçlanan nikotinli solüsyonları açıkça sayar. 85.43 yalnızca cihazı kapsar; sıvı içeren kartuş ve tanklar bile 24.04’e gönderilir. Nikotinin kendisi 29.39’dadır ama çözelti yanmadan solunmak üzere hazırlanmış bir üründür; Fasıl 38 de 24.04 ürünlerini kapsam dışı bırakır.",
    "24.04 Açıklama Notu (A)(1); 85.43 Açıklama Notu, hariç tutmalar; Fasıl 38 Not 1."),
  q("Tarife Cetveline göre, perakende kutularda sunulan, az çok kokulandırılmış enfiye hangi pozisyonda sınıflandırılır?",
    ["24.01", "24.02", "24.03", "24.04", "12.11"], "C", T_ESYA,
    "Enfiye, çiğneme tütünüyle birlikte 24.03’te sayılmıştır. 24.04 (B) yalnızca tütün içermeyen nikotinli ürünleri kapsar ve 24.04 Açıklama Notu çiğneme tütünü ile enfiyeyi açıkça 24.03’e gönderir. Tütün tozu döküntü olarak 24.01’de olsa da kokulandırılmış enfiye mamul tütündür.",
    "24.03 Açıklama Notu; 24.04 Açıklama Notu, hariç tutma (a)."),
  q("Tarife Cetveline göre, sigara imalatı sırasında ortaya çıkan tütün kırpıntıları, yaprak orta damarları ve tütün tozları hangi pozisyonda sınıflandırılır?",
    ["24.01", "24.03", "23.08", "14.04", "24.02"], "A", T_ESYA,
    "24.01 Açıklama Notu (2), tütün yapraklarının işlenmesinden veya tütün ürünlerinin imalinden çıkan artıkları (saplar, gövdeler, orta damarlar, kırpıntılar, tozlar) tütün döküntüsü olarak sayar. Mamul tütün imalatından çıkmış olmaları onları 24.03’e taşımaz. Fasıl 23 ve Fasıl 14’teki bitkisel artık ve ürün pozisyonları, tütün döküntüsü özel olarak 24.01’de sayıldığı için uygulanmaz.",
    "24.01 pozisyon metni ve Açıklama Notu (2)."),
  q("Tarife Cetveline göre, ne tütün ne de nikotin içeren, bir çeşit marulun yapraklarının özel olarak işlenmesiyle yapılmış sigaralar hangi pozisyonda sınıflandırılır?",
    ["24.03", "24.02", "12.11", "24.04", "30.04"], "B", T_ESYA,
    "24.02, tütün yerine geçen maddelerden yapılan sigaraları da kapsar; Açıklama Notu marul yaprağından yapılan, ne tütün ne nikotin içeren sigaraları örnek olarak verir. Tütünsüz içilen karışımlar 24.03’tedir, ancak sigara formuna getirilmiş ürün 24.02’dir. Yakılarak içildiği için 24.04 söz konusu değildir; nikotin içermemesi sonucu değiştirmez.",
    "24.02 pozisyon metni ve Açıklama Notu."),
  q("Tarife Cetveline göre, tütün içermeyen, nikotin içeren ve sigarayı bırakmaya yardımcı olarak sunulan çiğneme tableti hangi pozisyonda sınıflandırılır?",
    ["30.04", "21.06", "17.04", "29.39", "24.04"], "E", T_ESYA,
    "Fasıl 30 Not 1, nikotin içeren ve sigarayı bırakmaya yardımcı tablet, ciklet ve bantları Fasıl 30 dışında bırakıp 24.04’e gönderir; 24.04 (B) grubu nikotin replasman tedavisi ürünlerini de kapsar. Fasıl 21 de nikotinli sakızı 21.06’dan hariç tutar. Nikotinin kendisi 29.39’dadır, nikotin içeren ürün ise 24.04’tedir.",
    "Fasıl 30 Not 1; 24.04 Açıklama Notu (B); 21.06 Açıklama Notu."),
  q("Aşağıdakilerden hangisi Tarife Cetvelinin 24. Faslında <b>sınıflandırılmaz</b>?",
    ["Yüksek derecede fermente edilmiş ve likörlenmiş çiğneme tütünü",
     "Tütün artıklarının suda kaynatılmasıyla elde edilen tütün hülasası",
     "Tütün yapraklarından çıkarılmış, alkaloid halindeki nikotin",
     "Tütün tozlarının aglomere edilmesiyle elde edilen yeniden tertip edilmiş tütün tabakası",
     "Harmanlanmış ve likörlenmiş, damarı çıkarılmış tütün yaprakları"], "C", T_OLUMSUZ,
    "Nikotin (tütünden çıkarılan toksik alkaloid veya sentezle elde edilen alkaloid) 24.03 ve 24.04 hariç tutmalarıyla 29.39’dadır. Çiğneme tütünü, tütün hülasası ve yeniden tertip edilmiş tütün 24.03’te; likörlenmiş yapraklar 24.01’dedir. Tuzak, hülasanın da tütünden çıkarılan bir madde olmasıdır: hülasa 24.03’te kalır, izole alkaloid 29.39’a gider.",
    "24.03 Açıklama Notu, hariç tutmalar; 24.04 Açıklama Notu (b); 24.01 Açıklama Notu."),
  q("Aşağıdakilerden hangisi 24.04 pozisyonunda <b>sınıflandırılmaz</b>?",
    ["Elektrikle ısıtılan sistemlerde kullanılmak üzere tütün içeren çubuklar",
     "E-sıvı ile dağıtım mekanizmasını tek gövdede birleştiren, yeniden doldurulamayan ve şarj edilemeyen e-sigara",
     "Tütün içermeyen, nikotin içeren ve ağız yoluyla kullanılan ürünler",
     "E-sigaralar için atomizörle birlikte sunulan, sıvı içeren kartuş",
     "Değiştirilebilir kartuşlarla kullanılmak üzere tasarlanmış, şarj edilebilir e-sigara cihazı"], "E", T_OLUMSUZ,
    "Yeniden doldurulmak veya değiştirilebilir kartuşlarla kullanılmak üzere tasarlanmış e-sigara cihazları 85.43’tedir. Sıvı içeren kartuş ve tanklar, ısıtma elemanı veya atomizörle sunulsa bile 85.43 dışında bırakılıp 24.04’e gönderilir. Tek kullanımlık e-sigaralar 24.04 Açıklama Notu (A)(5), ısıtılan tütün çubukları (A)(2), tütünsüz ağızdan nikotin ürünleri (B) uyarınca 24.04’tedir.",
    "24.04 Açıklama Notu (A) ve (B); 85.43 Açıklama Notu."),
  q("Aşağıdakilerden hangisi 24.02 pozisyonunda <b>yer almaz</b>?",
    ["Sigara görünümünde, yeniden tertip edilmiş tütün içeren ve yakılmadan ısıtılarak solunan çubuk",
     "Tütün ve tütün yerine geçen madde karışımından yapılmış sigara",
     "İç sargılı veya sargısız uçları açık puro",
     "Sigara içme alışkanlığını kıracak şekilde formüle edilmiş, tıbbi özelliği olmayan sigara",
     "Tütün içeren sigarillo"], "A", T_OLUMSUZ,
    "24.02 Açıklama Notu, purolara ve sigaralara benzeyen ancak yanmadan solunması amaçlanan ürünleri 24.04’e gönderir; Fasıl 24 Not 2 de 24.04’ü öncelikli kılar. Karışımdan yapılmış sigara (oran önemsiz), uçları açık puro ve sigarillo 24.02’dedir. Tıbbi özelliği olmayan alışkanlık kırıcı sigaralar da 24.02’de kalır; yalnızca tıbbi sigaralar Fasıl 30’a gider.",
    "24.02 Açıklama Notu; Fasıl 24 Not 2."),
  q("Aşağıdaki ürünlerden hangisi Tarife Cetvelinin 24. Faslı kapsamında <b>yer almaz</b>?",
    ["Tütün içermeyen, bitkisel içilen karışım",
     "Enfiye imali için sıkıştırılmış tütün",
     "Ateşte kurutulmuş, sapları koparılmamış yaprak tütün",
     "İçilmek üzere hazırlanmış kenevir (cannabis) otu",
     "Pipoda içilmek üzere hazırlanmış kıyılmış tütün"], "D", T_OLUMSUZ,
    "24.03 Açıklama Notu, tütün içermeyen içilen karışımları mamul tütün yerine geçen ürün olarak kapsar, ancak kenevir (cannabis) gibi ürünleri açıkça 12.11’e gönderir. Enfiye imali için sıkıştırılmış tütün ve pipo tütünü 24.03’te; ateşte kurutulmuş yaprak tütün 24.01’dedir.",
    "24.03 Açıklama Notu; 24.01 Açıklama Notu; Fasıl 24 Genel Açıklamalar."),
  q("Aşağıdakilerden hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır?",
    ["Çiğneme tütünü", "Tütün içermeyen nikotinli sakız", "Enfiye", "Homojenize tütün", "Pipo tütünü"], "B", T_FARKLI,
    "Tütün içermeyen nikotinli sakız, nikotini soluma dışında bir yolla veren ürün olarak 24.04 (B) kapsamındadır; 21.06 ve Fasıl 30 de onu 24.04’e gönderir. Çiğneme tütünü, enfiye, homojenize tütün ve pipo tütünü 24.03’tedir. Tuzak, “çiğneme” ortak kelimesidir: tütün içeren çiğneme tütünü 24.04 dışında kalır.",
    "24.03 Açıklama Notu; 24.04 Açıklama Notu (B) ve hariç tutma (a)."),
  q("Aşağıdakilerden hangisi diğerlerinden farklı bir fasılda yer alır?",
    ["Ekim amacıyla kullanılan tütün tohumu", "Tütün döküntüsü", "Tütün hülasası", "Sigarillo", "Nikotinli transdermal bant"], "A", T_FARKLI,
    "Ekim amacıyla kullanılan tohumlar 12.09’dadır ve bu pozisyonun Açıklama Notu tütün tohumlarını açıkça sayar. Tütün döküntüsü 24.01, tütün hülasası 24.03, sigarillo 24.02, nikotinli transdermal bant 24.04 ile Fasıl 24’tedir. Bandın Fasıl 30 sanılması ikinci tuzaktır.",
    "12.09 Açıklama Notu; 24.01, 24.02, 24.03 Açıklama Notları; Fasıl 30 Not 1."),
  q("Aşağıdaki eşya çiftlerinden hangisinde her iki eşya da <b>aynı</b> pozisyonda sınıflandırılır?",
    ["Şarj edilebilir e-sigara cihazı – e-sigara kartuşu",
     "Nikotin – nikotinli bant",
     "Sigara kağıdı – sigara",
     "Nargile – nargile tütünü",
     "Nikotinli sakız – nikotinli transdermal bant"], "E", T_FARKLI,
    "Tütün içermeyen nikotinli sakız ve bant, nikotini ağız veya deri yoluyla veren ürünler olarak ikisi de 24.04’tedir. E-sigara cihazı 85.43, kartuşu 24.04; nikotin 29.39; sigara kağıdı 48.13, sigara 24.02; nargile 96.14, nargile tütünü 24.03’tür.",
    "24.04 Açıklama Notu (B); Fasıl 30 Not 1; 85.43 ve 96.14 Açıklama Notları."),
  q("Aşağıdaki tütün ürünlerinden hangisi diğerlerinden farklı bir pozisyonda yer alır?",
    ["Sapları tamamen koparılmış tütün yaprakları",
     "Şekil verilerek kesilmiş, içime hazır olmayan tütün yaprakları",
     "Fermente edilmiş bütün tütün bitkisi",
     "Sigara sarmak için hazırlanmış, içime hazır kıyılmış tütün",
     "Tütün yapraklarının işlenmesinden kalan saplar ve gövdeler"], "D", T_FARKLI,
    "24.01 Açıklama Notu, kesilmiş ve şekil verilerek kesilmiş yaprakları kapsar ama içime hazır tütünü hariç tutar; sigara yapmak için imal edilmiş içilen tütün 24.03’tedir. Sapı koparılmış yaprak, fermente bütün bitki ve saplar-gövdeler (döküntü) 24.01’dedir. Tuzak, “kesilmiş” ile “içime hazır” arasındaki farktır.",
    "24.01 Açıklama Notu (1) ve (2); 24.03 Açıklama Notu."),
  q("Tarife Cetvelinin 24. Fasıl notlarına göre, hem 24.04 pozisyonunda hem de bu faslın başka bir pozisyonunda sınıflandırılabilen bir ürün için aşağıdakilerden hangisi <b>doğrudur</b>?",
    ["Esas niteliğini veren maddeye göre sınıflandırılır.",
     "24.04 pozisyonunda sınıflandırılır.",
     "Yakılarak tüketilip tüketilmediğine bakılmaksızın 24.03’te sınıflandırılır.",
     "Eşyayı en özel şekilde niteleyen pozisyonda sınıflandırılır.",
     "Tütün içeriyorsa 24.03’te, içermiyorsa 24.04’te sınıflandırılır."], "B", T_NOT,
    "Fasıl 24 Not 2, hem 24.04 hem de bu faslın diğer bir pozisyonunda sınıflandırılabilen ürünlerin 24.04’te sınıflandırılacağını hükme bağlar. Not bir öncelik kuralı koyduğu için esas nitelik (A) veya en özel tanım (D) araştırmasına gerek yoktur. Tütün içermek 24.04’ü engellemez; ısıtılan tütün ürünleri 24.04’tedir (E yanlış).",
    "Fasıl 24 Not 2; 24.04 Açıklama Notu (A)(2)."),
  q("Tarife Cetvelinin 24. Fasıl notlarına göre, 24.04 pozisyonu anlamında “yanma olmadan solunan” ifadesinden ne anlaşılır?",
    ["Yalnızca elektrikle ısıtılarak gerçekleştirilen soluma",
     "Yalnızca nikotin içeren sıvıların buharlaştırılarak solunması",
     "Isı yoluyla veya diğer yollarla yanma olmadan soluma",
     "Tütün içermeyen ürünlerin ağız yoluyla alınması",
     "Yakıldıktan sonra filtre yoluyla soğutularak soluma"], "C", T_NOT,
    "Fasıl 24 Not 3’e göre yanma olmadan solunan ürünlerden ısı yoluyla veya diğer yollarla yanma olmadan soluma anlaşılır. Açıklama Notu ısıtmayı elektrikli cihazla sınırlamaz (kimyasal reaksiyon, karbon ısı kaynağı) ve ultrasonik buharlaştırmayı da sayar; nikotin içermeyen ikame ürünler de dahildir. Ağız yoluyla alım soluma değil, 24.04’ün (B) grubudur.",
    "Fasıl 24 Not 3; 24.04 Açıklama Notu (A)."),
  q("Fasıl 24 notu ile 24.02 Açıklama Notu birlikte dikkate alındığında aşağıdaki ifadelerden hangisi <b>doğrudur</b>?",
    ["Tıbbi sigaralar, tütün içeriyorlarsa 24.02 pozisyonunda kalır.",
     "Sigara içme alışkanlığını kıracak şekilde formüle edilmiş bütün sigaralar Fasıl 30’da sınıflandırılır.",
     "Nikotin içeren ve sigarayı bırakmaya yardımcı bantlar Fasıl 30’da sınıflandırılır.",
     "Tütün içermeyen sigaralar Fasıl 24 dışında, bitkisel ürün olarak sınıflandırılır.",
     "Tıbbi sigaralar Fasıl 30’da; tıbbi özelliği olmayan, alışkanlık kırıcı özel sigaralar 24.02’de sınıflandırılır."], "E", T_NOT,
    "Fasıl 24 Not 1 tıbbi sigaraları Fasıl 30’a gönderir; 24.02 Açıklama Notu ise sigara içme alışkanlığını kırmak üzere formüle edilmiş ancak tıbbi özelliği olmayan sigaraları 24.02’de bırakır. Nikotinli bantlar Fasıl 30 Not 1 gereği 24.04’tedir. Tütün içermeyen sigaralar da 24.02 kapsamındadır.",
    "Fasıl 24 Not 1; 24.02 Açıklama Notu; Fasıl 30 Not 1."),
  q("Tarife Cetveline göre, tütün ile tütün yerine geçen maddelerin karışımından yapılmış sigaraların sınıflandırılmasında karışımdaki tütün oranı için aşağıdakilerden hangisi <b>doğrudur</b>?",
    ["Oran dikkate alınmaz; sigara 24.02’de sınıflandırılır.",
     "Tütün ağırlıkça %50’den fazla ise 24.02’de, değilse 24.03’te sınıflandırılır.",
     "Tütün ağırlıkça %20’den az ise ürün tütün yerine geçen madde sayılır ve 24.03’e girer.",
     "Esas niteliği tütün veriyorsa 24.02’de, vermiyorsa Fasıl 12’de sınıflandırılır.",
     "Tütün oranından bağımsız olarak 24.04’te sınıflandırılır."], "A", T_NOT,
    "24.02 Açıklama Notu, tütün ile tütün yerine geçen maddelerin karışımından yapılmış sigaraların, karışımdaki oranlara bakılmaksızın 24.02’de yer aldığını belirtir; hiç tütün içermeyen sigaralar da buradadır. Fasıl 24’te yüzde eşiği yoktur; %50 veya %20 gibi oranlar çeldiricidir. Yakılarak içildiği için 24.04 söz konusu değildir.",
    "24.02 Açıklama Notu."),
  q("Yeniden tertip edilmiş tütün içeren ve elektrikle ısıtılan sistemlerde yanma olmadan solunmak üzere tasarlanmış tütün çubukları, hem 24.03 (yeniden tertip edilmiş tütün) hem de 24.04 kapsamına girebilecek niteliktedir. Bu ürünün 24.04’te sınıflandırılması hangi kurala dayanır?",
    ["GYK 3(a) – eşyayı en özel şekilde niteleyen pozisyon",
     "GYK 3(b) – esas niteliği veren madde",
     "GYK 3(c) – numara sırasına göre sonuncu pozisyon",
     "GYK 1 – pozisyon metinleri ve fasıl notları",
     "GYK 2(b) – karışım ve bileşik eşya"], "D", T_GYK,
    "GYK 1’e göre sınıflandırma pozisyon metinlerine ve bölüm veya fasıl notlarına göre yapılır. Fasıl 24 Not 2, hem 24.04 hem de bu faslın diğer bir pozisyonuna girebilen ürünleri doğrudan 24.04’e verdiği için GYK 3’e başvurmaya gerek kalmaz. GYK 3(c) de aynı sonucu verir gibi görünür (tuzak), ancak hukuki dayanak fasıl notudur.",
    "GYK 1; Fasıl 24 Not 2; 24.04 Açıklama Notu (A)(2)."),
  q("24.04 pozisyonunda yer aldığı kesinleşen nikotinli bir ürünün, bu pozisyonun “yanma olmadan solunan ürünler” ile “diğerleri” şeklindeki alt ayrımlarından hangisine gireceği hangi Genel Yorum Kuralına göre belirlenir?",
    ["GYK 1", "GYK 6", "GYK 3(a)", "GYK 4", "GYK 5(b)"], "B", T_GYK,
    "Bir pozisyonun alt pozisyonları arasındaki sınıflandırma GYK 6’ya göre, yalnızca aynı seviyedeki alt pozisyonlar karşılaştırılarak, alt pozisyon metinleri ve alt pozisyon notları esas alınarak yapılır. GYK 1 dört rakamlı pozisyonun belirlenmesine yöneliktir. GYK 4 hiçbir pozisyona girmeyen eşya, GYK 5(b) ambalaj içindir.",
    "GYK 6; GYK 1."),
  q("Tütünden elde edilen hülasa ……… pozisyonunda, tütünden çıkarılmış nikotin ……… pozisyonunda, ekim amaçlı tütün tohumu ……… pozisyonunda, pipolar ise ……… pozisyonunda sınıflandırılır. Boşlukları sırasıyla doğru tamamlayan seçenek hangisidir?",
    ["13.02 / 29.39 / 12.09 / 96.14",
     "24.03 / 24.04 / 12.09 / 96.14",
     "24.03 / 29.39 / 12.09 / 96.14",
     "24.03 / 29.39 / 24.01 / 96.13",
     "13.02 / 24.04 / 24.01 / 96.13"], "C", T_ESLES,
    "Tütün hülasa ve ıtırları 24.03’tedir ve 13.02 bitkisel hülasalar pozisyonundan açıkça hariç tutulur. Nikotin 29.39’da, ekim amaçlı tütün tohumu 12.09’da, pipolar 96.14’tedir. 96.13 çakmaklar pozisyonudur; nikotinin kendisi 24.04’te değildir.",
    "24.03 Açıklama Notu; 13.02 Açıklama Notu; 12.09 Açıklama Notu; 96.14 Açıklama Notu."),
  q("Aşağıdaki eşya ile pozisyonlar eşleştirildiğinde hangi seçenek doğrudur? I. Çiğneme tütünü · II. Tütün döküntüsü · III. Sigarillo · IV. Nikotinli transdermal bant — a) 24.01 · b) 24.02 · c) 24.03 · d) 24.04",
    ["I-a, II-c, III-b, IV-d", "I-d, II-a, III-b, IV-c", "I-c, II-a, III-d, IV-b", "I-c, II-b, III-a, IV-d", "I-c, II-a, III-b, IV-d"], "E", T_ESLES,
    "Çiğneme tütünü 24.03’te (tütün içerdiği için 24.04 dışındadır), tütün döküntüsü 24.01’de, sigarillo 24.02’de, nikotinli transdermal bant 24.04’tedir. B seçeneği çiğneme tütününü nikotinli ürün sanma tuzağını kullanır.",
    "24.01, 24.02, 24.03, 24.04 Açıklama Notları; Fasıl 30 Not 1."),
  q("24.04 pozisyonu ile ilgili aşağıdaki ifadelerden hangileri <b>doğrudur</b>? I. Elektrikle ısıtılan sistemlerde kullanılan, tütün içeren ürünler bu pozisyondadır. II. Nikotin replasman tedavisi ürünleri, tütün içermemeleri kaydıyla bu pozisyondadır. III. Çiğneme tütünü, nikotini ağız yoluyla verdiği için bu pozisyondadır. IV. Sentez yoluyla elde edilmiş nikotin bu pozisyondadır.",
    ["I ve II", "I ve III", "II ve IV", "I, II ve III", "II, III ve IV"], "A", T_COKTAN,
    "I doğrudur: 24.04 Açıklama Notu (A)(2) elektrikle ısıtılan tütün ürünlerini sayar. II doğrudur: (B) grubu, tütün içermeyen nikotinli ürünler arasında NRT ürünlerini sayar. III yanlıştır: çiğneme tütünü ve enfiye 24.03’e gönderilir. IV yanlıştır: tütünden veya sentezle elde edilen nikotin 29.39’dadır.",
    "24.04 Açıklama Notu (A)(2), (B) ve hariç tutmalar (a), (b)."),
  q("Tarife Cetveline göre aşağıdaki ifadelerden hangileri <b>doğrudur</b>? I. Kenevir (cannabis) gibi içilen ürünler 24.03 dışında, 12.11’de yer alır. II. Tütün hülasaları 13.02’deki bitkisel hülasalarla birlikte sınıflandırılır. III. 38.08’de yer alan böcek öldürücüler, tütün esaslı olsalar bile Fasıl 24 dışındadır. IV. Pipo ve nargileler, tütünle kullanıldıkları için 24.03’te yer alır.",
    ["I ve II", "I ve III", "II ve IV", "I, III ve IV", "II, III ve IV"], "B", T_COKTAN,
    "I doğrudur (24.03 Açıklama Notu, kenevir gibi ürünleri 12.11’e gönderir). III doğrudur (24.03, 38.08’deki böcek öldürücüleri hariç tutar). II yanlıştır: tütün hülasaları 24.03’tedir ve 13.02’den açıkça hariç tutulur. IV yanlıştır: pipo ve nargileler 96.14’tedir.",
    "24.03 Açıklama Notu; 13.02 Açıklama Notu; 96.14 Açıklama Notu."),
  q("Bir tütün işleme tesisinden gelen eşya; harmanlanmış, sapları koparılmış ve damarları çıkarılmış, kurumayı ve küflenmeyi önlemek, tat ve kokuyu korumak amacıyla uygun bir sıvı ile salçalanmış tütün yapraklarından oluşmaktadır. Yapraklar içime hazır hale getirilmemiş ve balyalar halinde sıkıştırılmıştır. Bu eşya hangi pozisyonda sınıflandırılır?",
    ["24.03", "24.02", "24.04", "24.01", "21.06"], "D", T_SENARYO,
    "24.01 Açıklama Notu, harmanlanmış, sapı koparılmış, damarı çıkarılmış ve kurumayı, küflenmeyi önlemek ve tat-kokuyu korumak için uygun bir sıvı ile salçalanmış veya likörlenmiş tütün yapraklarını açıkça kapsar. İçime hazır olmadığı için 24.03’e geçmez. Tuzak, uygulanan işlemleri “mamul tütün” saymaktır.",
    "24.01 Açıklama Notu (1)."),
  q("Plastik gövdeli, nargile görünümünde küçük bir cihaz; içinde nikotinli e-sıvı ve şarj edilemeyen bir pil bulunmaktadır. Cihaz yeniden doldurulamaz; sıvı veya pil bittiğinde atılmak üzere tasarlanmıştır. Bu eşya Tarife Cetvelinde hangi pozisyonda sınıflandırılır?",
    ["85.43", "96.14", "24.04", "24.03", "24.02"], "C", T_SENARYO,
    "Ürün ile dağıtım mekanizmasını tek gövdede birleştiren, yeniden doldurulamayan ve şarj edilemeyen tek kullanımlık e-sigaralar 24.04 Açıklama Notu (A)(5) uyarınca 24.04’tedir ve 85.43 Açıklama Notunda hariç tutulur. Nargile veya pipo şeklindeki e-sigaralar 96.14’e girmez; yeniden doldurulabilir olsalardı 85.43’te yer alırlardı. Nargile tütünü (24.03) yakılarak içilir.",
    "24.04 Açıklama Notu (A)(5); 85.43 Açıklama Notu; 96.14 Açıklama Notu.")
 ]
}

out = os.path.join(KITAP, "data", "fasil_24.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=1)
print(out)
