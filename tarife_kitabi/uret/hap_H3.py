#!/usr/bin/env python3
"""Hap bilgi sayfaları – Grup H3: Fasıl 25–38 (Bölüm V kısmen ve Bölüm VI)."""
import json
import os
import re

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(KITAP, "hap")

F = {}

# ---------------------------------------------------------------- 25
F[25] = {
 "kademe": "B",
 "sinavda": "Son 5 sınavda 2 kez: dişçilikte kullanılan alçının pozisyonu (25.20; 30.06, 68.09, 90.21 "
            "çeldirici) ve “22. fasılda yer almaz” kalıbında deniz suyu (25.01; sirke, kar, bal şarabı Fasıl 22’de).",
 "pozisyonlar": [
  ["25.01", "Tuz, saf sodyum klorür, deniz suyu"],
  ["25.15", "Mermer, traverten; belirgin yoğunluk ≥ 2,5"],
  ["25.17", "Çakıl, makadam, taş granül ve tozu (öncelikli)"],
  ["25.20", "Alçı taşı, alçılar; dişçilik alçısı dahil"],
  ["25.23", "Su altında sertleşen çimento, klinker"],
  ["25.30", "Artık: vermikülit, perlit, toprak boyası, kehribar"],
 ],
 "hap": [
  "<b>Not 1 – izin verilen işlemler:</b> yıkama, ezme, öğütme, eleme, flotasyon, manyetik ayırma. Kavurma, "
  "kalsinasyon, karıştırma ve kristalizasyon fasıl dışına çıkarır; pozisyon izin veriyorsa kalır (kaolin, dolomit, alçı, kireç).",
  "<b>Not 3:</b> 25.17’ye ve başka bir Fasıl 25 pozisyonuna girebilen ürün 25.17’dedir: mermer tozu, agrega "
  "olarak kırılmış dolomit 25.17.",
  "<b>Taş sınırı:</b> ham, kabaca yontulmuş veya testereyle dikdörtgen kesilmiş taş Fasıl 25; cilalı, şevli, "
  "oyulmuş taş ile kaldırım, döşeme ve mozaik taşları Fasıl 68.",
  "<b>Eşikler:</b> kireçli taş belirgin yoğunluğu ≥ 2,5 ise 25.15, altı 25.16; silisli fosil unu ≤ 1 (25.12); "
  "Fe2O3 ≥ %70 toprak boya 28.21; tabii borik asit H3BO3 ≤ %85 (25.28).",
  "<b>Saf muadiller Fasıl 28’e gider, tuz istisnadır:</b> süblime kükürt 28.02, saf kalsiyum oksit 28.25, "
  "rafine boraks 28.40; saf sodyum klorür ve deniz suyu 25.01’de kalır.",
 ],
 "karistirilan": [
  ["Dişçilikte kullanılan özel kalsine alçı", "25.20", "Alçı esaslı dişçilik müstahzarı 34.07, dişçi çimentosu 30.06"],
  ["Deniz suyu", "25.01", "Fasıl 22 değil; tabii su, buz ve kar 22.01"],
  ["Yazı ve terzi tebeşiri", "96.09", "Not 2; tabii tebeşir 25.09, bilardo tebeşiri 95.04"],
 ],
}

# ---------------------------------------------------------------- 26
F[26] = {
 "kademe": "C",
 "sinavda": "Son 5 sınavda doğrudan sorulmadı, seçeneklerde de yer almadı; önceki sınavlarda “farklı fasıl” "
            "kalıbında cüruf (Fasıl 26) tuz, zımpara taşı ve amyanttan (Fasıl 25) ayrıldı.",
 "pozisyonlar": [
  ["26.01", "Demir cevheri; kavrulmuş demir piriti dahil"],
  ["26.18", "Demir-çelik imalatından granüle cüruf"],
  ["26.19", "Diğer demir-çelik cürufu, tufal, moloz"],
  ["26.21", "Diğer cüruf ve küller; şehir atığı külü"],
 ],
 "hap": [
  "<b>Metal cevheri (Not 2):</b> metalurji sanayiinde metal çıkarmak için fiilen kullanılan mineral; kavurma, "
  "kalsinasyon, sinterleme, peletleme fasıldan çıkarmaz. Kuru ağırlıkta Mn %20’den az 26.01, ≥ %20 26.02.",
  "<b>Not 1 – fasıl dışı:</b> makadam halindeki cüruf 25.17, cüruf yünü 68.06, bazik (Thomas) cüruf Fasıl 31; "
  "bakır, nikel, kobalt matları Bölüm XV; kıymetli metal döküntüsü 71.12 veya 85.49.",
  "<b>Başka yerde sayılan mineraller:</b> kavrulmamış pirit 25.02, barit 25.11, dolomit 25.18, magnezit 25.19, "
  "karnalit 31.04; kuru pil için hazırlanmış pirolüsit 25.30.",
 ],
 "karistirilan": [
  ["Kavrulmamış demir piriti", "25.02", "İsmen Fasıl 25’te; kavrulmuşu 26.01"],
  ["Bazik (Thomas) cürufu", "31.03", "Not 1; diğer küller gübre olsa da 26.21"],
 ],
}

# ---------------------------------------------------------------- 27
F[27] = {
 "kademe": "B",
 "sinavda": "Son 5 sınavda 2 kez: “27. fasılda sınıflandırılamaz” kalıbında hidrojen gazı (28.04) havagazı, "
            "turba, elektrik ve vazelinden ayrıldı; “aynı fasıl” sorusunda elektrik enerjisi–vazelin–turb üçlüsü "
            "Fasıl 27 olarak verildi.",
 "pozisyonlar": [
  ["27.03", "Turb; tarımda kullanılsa da burada"],
  ["27.05", "Havagazı, su gazı, fakir gaz"],
  ["27.10", "Petrol yağları, ≥ %70’lik müstahzarlar, atık yağlar"],
  ["27.11", "Doğal gaz, LPG; saf metan ve propan"],
  ["27.12", "Vazelin, parafin, mineral mumlar"],
  ["27.16", "Elektrik enerjisi"],
 ],
 "hap": [
  "<b>Not 1:</b> kimyaca belirli izole organik bileşikler Fasıl 29’dadır; <b>saf metan ve propan</b> istisnadır, "
  "27.11’de kalır. Hidrojen ise element olarak 28.04’tedir.",
  "<b>27.10 için %70 + esas unsur:</b> ağırlıkça ≥ %70 petrol yağı içeren ve bu yağın esas unsur olduğu "
  "müstahzarlar 27.10; %70’in altı 34.03, 38.19, 38.26 gibi pozisyonlara gider.",
  "<b>Not 2:</b> aromatik olmayan unsurlar ağırlıkça baskınsa 27.10; aromatik unsurlar baskınsa 27.07 (benzol, "
  "toluol, kreozot yağı).",
  "<b>Not 3 – atık yağlar 27.10’dadır:</b> kullanılmış motor, hidrolik, transformatör yağı, tank tortusu yağları, "
  "suyla karışık kesme yağları; 38.25’e gitmez.",
  "<b>Vazelin ve turb:</b> ham vazelin 27.12, perakende cilt bakımı vazelini 33.04; esas karakteri turb olan "
  "saksı toprağı 27.03, bahçe toprağı 25.30.",
 ],
 "karistirilan": [
  ["Hidrojen gazı", "28.04", "Element; Fasıl 27 değil (havagazı ise 27.05)"],
  ["Biyodizel (petrol yağı %70’ten az)", "38.26", "≥ %70 petrol yağı içeren karışımı 27.10"],
  ["Çakmak doldurma bütanı (≤ 300 cm3 kap)", "36.06", "Çakmağın gaz haznesi 96.13; dökme LPG 27.11"],
 ],
}

# ---------------------------------------------------------------- 28 (+ Bölüm VI Not 1–2)
F[28] = {
 "kademe": "C",
 "sinavda": "Son 5 sınavda 1 kez: “27. fasılda sınıflandırılamaz” sorusunun cevabı hidrojen gazıydı (element → "
            "28.04). Bölüm VI notları (öncelik ve perakende kuralı) bütün kimya fasıllarında kullanılır.",
 "pozisyonlar": [
  ["28.04", "Hidrojen, asal gazlar, diğer ametaller"],
  ["28.43", "Kıymetli metal bileşikleri; Bölüm VI içinde öncelikli"],
  ["28.44", "Radyoaktif element ve izotoplar; tüm tarifeye öncelikli"],
  ["28.53", "Damıtık su, sıvı hava, amalgamlar, fosfürler"],
 ],
 "hap": [
  "<b>Bölüm VI Not 1:</b> 28.44 ve 28.45 tanımına uyan ürün tarifenin başka pozisyonuna girmez; 28.43, 28.46, "
  "28.52 yalnız Bölüm VI içinde önceliklidir (gümüş kazeinat 28.43, gadolinit 25.30).",
  "<b>Bölüm VI Not 2:</b> dozlandırıldığı veya perakende hazırlandığı için 30.04–30.06, 32.12, 33.03–33.07, "
  "35.06, 37.07 veya 38.08’e giren ürün orada kalır (perakende tutkal dekstrin 35.06).",
  "<b>Fasıl 28 Not 1 ve 3:</b> yalnız izole element ve belirli yapıda inorganik bileşik (sulu çözeltisi dahil); "
  "saf olsa da sodyum klorür 25.01, magnezyum oksit 25.19, gübre tuzları Fasıl 31.",
 ],
 "karistirilan": [
  ["Kimyaca saf sodyum klorür", "25.01", "Not 3(a): Bölüm V ürünü; saf MgO da 25.19"],
  ["Perakende fotoğrafçılık gümüş nitratı", "28.43", "Bölüm VI Not 1(B): 37.07’ye değil 28.43’e"],
 ],
}

# ---------------------------------------------------------------- 29
F[29] = {
 "kademe": "C",
 "sinavda": "Son 5 sınavda doğrudan sorulmadı; seçeneklerde çeldirici oldu: B12 vitamini (29.36, Fasıl 30 değil) "
            "ve sınai yağ alkolleri sorusunda 29.34 (doğrusu 38.23).",
 "pozisyonlar": [
  ["29.05", "Asiklik alkoller; gliserol ≥ %95 (etanol hariç)"],
  ["29.36", "Vitaminler, provitaminler (dozlandırılmamış)"],
  ["29.41", "Antibiyotikler; kimyaca belirli olmasa da"],
 ],
 "hap": [
  "<b>Not 1 – kimyaca belirli izole organik bileşik:</b> izomer karışımı, sulu çözelti, stabilizör katkısı faslı "
  "değiştirmez; 29.36–29.39 ve 29.41 ürünleri belirli yapıda olmasa da buradadır.",
  "<b>Fasıl dışı (Not 2, eşikler):</b> etil alkol 22.07 / 22.08, metan-propan 27.11, üre Fasıl 31, sakkaroz "
  "17.01, enzimler 35.07 (saf olsa da); ham gliserol 15.20, eşik altı yağ alkolü 38.23.",
  "<b>Not 3:</b> iki pozisyona giren bileşik numara sırasına göre sonuncusunda (askorbik asit 29.36). "
  "Dozlandırılmış vitamin 30.04, radyoaktif bileşik 28.44’tedir (Bölüm VI Not 1–2).",
 ],
 "karistirilan": [
  ["Sınai yağ alkolleri (%90’dan az saflık)", "38.23", "Saflığı %90 ve üstü yağ alkolü 29.05"],
  ["Ham gliserin, gliserinli sular ve lesivler", "15.20", "Not 2(a); %95 ve üstü saf gliserol 29.05"],
 ],
}

# ---------------------------------------------------------------- 30
F[30] = {
 "kademe": "A",
 "sinavda": "Son 5 sınavda 4 kez: ilk yardım kutusu 30.06 (biri GYK sorusu: 1 ve 6, set değil), miadı dolmuş "
            "ilaç 30.06 (30.04, 38.25 çeldirici), “30’da sınıflandırılmaz” kalıbında tedavi amaçlı olmayan kan "
            "albümini (35.02). Nikotin bandı, tıbbi sabun, akne kremi ve B12 çeldirici olarak kullanıldı.",
 "pozisyonlar": [
  ["30.01", "Kurutulmuş organ, organ hülasası, heparin"],
  ["30.02", "Kan, aşı, serum, antikor, toksin, kültür"],
  ["30.03", "Karışık ilaç; dozlandırılmamış, dökme"],
  ["30.04", "İlaç; dozlandırılmış veya perakende (transdermal dahil)"],
  ["30.05", "İlaçlı veya tıbbi perakende pamuk, gazlı bez, bandaj"],
  ["30.06", "Yalnız Not 4 listesi (ilk yardım, miadı dolmuş)"],
 ],
 "hap": [
  "<b>Not 1 – tedavi edici olsa da fasıl dışı:</b> nikotinli sigara bırakma bandı ve cikleti 24.04, 33.03–33.07 "
  "kozmetikleri (akne kremi 33.04), tıbbi madde içeren sabun 34.01.",
  "<b>Not 1 – diğer hariçler:</b> gıda takviyesi ve maden suyu (Bölüm IV; damardan beslenme hariç), dişçilik "
  "alçısı 25.20, alçı esaslı dişçilik müstahzarı 34.07, tedavi için hazırlanmamış kan albümini 35.02.",
  "<b>Not 4 – 30.06 kapalı listesi:</b> steril katgüt ve dikiş malzemesi, kontrast madde, dişçi/kemik "
  "çimentosu, ilk yardım kutusu, kimyasal gebelik önleyici, tıbbi jel, miadı dolmuş ilaç, ostomi torbası, plasebo.",
  "<b>30.02 sunumdan bağımsızdır:</b> kan, antiserum, aşı, toksin, mikroorganizma kültürü her sunumda 30.02; "
  "30.03’teki karışık ilaç ise dozlandırılınca veya perakende ambalajlanınca 30.04 olur.",
  "<b>Not 3 – karışım olmayan dökme madde:</b> Fasıl 28–29 ürünleri ve standardize 13.02 hülasaları dökme halde "
  "kendi fasıllarında (dökme B12 29.36); dozlandırılmış veya perakende ise 30.04.",
  "<b>İlk yardım kutusu:</b> Not 4(g) ile ismen 30.06’dadır; sınıflandırma GYK 1 ve 6 ile yapılır, GYK 3(b) set "
  "kuralına gerek yoktur.",
  "<b>Teşhis reaktifi:</b> hastaya uygulanan reaktif ve X ışını kontrast müstahzarı 30.06; laboratuvarda "
  "numune üzerinde kullanılan reaktif 38.22. Steril olmayan katgüt 42.06.",
  "<b>Bölüm VI Not 2:</b> dozlandırıldığı veya perakende hazırlandığı için 30.04–30.06’ya giren ürün orada kalır; "
  "ancak kolloidal gümüş gibi 28.43 ürünleri önceliklidir (Not 1).",
 ],
 "karistirilan": [
  ["Tedavi amaçlı olmayan kan albümini", "35.02", "Not 1(h); tedavi veya korunma için hazırlanmışsa 30.02"],
  ["Nikotinli sigara bırakma bandı", "24.04", "Not 1(b); diğer transdermal ilaç bantları 30.04"],
  ["Akne azaltan yüz bakım müstahzarı", "33.04", "Not 1(e): 33.03–33.07 ürünü tedavi edici olsa da kozmetiktir"],
  ["Kullanım süresi geçmiş hazır ilaç", "30.06", "Not 4(k); 30.04 veya atık 38.25 değil"],
  ["Dişçilikte kullanılan alçı", "25.20", "Not 1(c); dişçi çimentosu ve diş dolgusu 30.06"],
  ["Dökme (dozlandırılmamış) B12 vitamini", "29.36", "Not 3: karışım olmayan Fasıl 29 ürünü; dozlanırsa 30.04"],
 ],
}

# ---------------------------------------------------------------- 31
F[31] = {
 "kademe": "C",
 "sinavda": "Son 5 sınavda yalnız fasıl eşleştirmesinde: “Gübre 31. fasılda yer alır” doğru ifade olarak "
            "verildi; tarımda kullanılan turbun Fasıl 27’de olduğu ayrıca soruldu.",
 "pozisyonlar": [
  ["31.02", "Azotlu: üre, amonyum nitrat (Not 2 listesi)"],
  ["31.03", "Fosfatlı: süperfosfat, Thomas cürufu, kalsine fosfat"],
  ["31.04", "Potaslı: potasyum klorür ve sülfat, karnalit"],
  ["31.05", "NPK, MAP, DAP; tablet, ≤ 10 kg ambalaj"],
 ],
 "hap": [
  "<b>Kapalı listeler (Not 2–4):</b> 31.02–31.04 yalnız sayılan ürünleri kapsar ve bunlar gübre olarak "
  "kullanılmasa da buradadır. Listede olmayan bileşik gübre olsa da Fasıl 28’dedir (potasyum nitrat 28.34).",
  "<b>31.05:</b> N, P, K’dan ikisini veya üçünü içerenler, MAP ve DAP (saf olsa da), organik + kimyasal "
  "karışımlar; tablet halinde veya brüt ağırlığı 10 kg’ı geçmeyen ambalajdaki her fasıl ürünü.",
  "<b>Islah maddeleri fasıl dışı:</b> kireç 25.22, bahçe ve bitkisel toprak 25.30, turb 27.03 (tarımda "
  "kullanılsa da); kalsine edilmemiş tabii fosfat 25.10, hayvan kanı 05.11.",
 ],
 "karistirilan": [
  ["Tarımda kullanılan turb", "27.03", "Islah maddesi; gübre değil, Fasıl 31 dışı"],
  ["Tek başına amonyum klorür", "28.27", "Not 2 listesinde yok; gübre karışımı ise 31.02"],
 ],
}

# ---------------------------------------------------------------- 32 (+ Bölüm VI Not 3)
F[32] = {
 "kademe": "C",
 "sinavda": "Son 5 sınavda doğrudan sorulmadı, seçeneklerde de yer almadı; önceki sınavlarda Not 4 (%50 çözücü → "
            "32.08; 27.10, 34.03, 38.14 çeldirici) ve “ayakkabı boyası” (34.05; 32.05 çeldirici) soruldu.",
 "pozisyonlar": [
  ["32.08", "Sentetik polimer esaslı boya, vernik; susuz ortam"],
  ["32.09", "Sentetik polimer esaslı boya, vernik; sulu ortam"],
  ["32.12", "Perakende ev boyaları; ıstampacılık varakları"],
  ["32.13", "Ressam, eğitim, afiş boyaları (tüp, tablet)"],
 ],
 "hap": [
  "<b>Not 4:</b> 39.01–39.13 polimerlerinin uçucu organik çözücüdeki çözeltisi, çözücü ağırlığı çözeltinin "
  "%50’sinden fazlaysa 32.08; değilse Fasıl 39. Kollodyon her durumda 39.12.",
  "<b>Boya adlı ama Fasıl 32 değil:</b> ayakkabı boyası ve cilası 34.05, saç boyası 33.05, makyaj boyası ve "
  "tırnak cilası 33.04, boya kalemi ve pastel 96.09.",
  "<b>Bölüm VI Not 3:</b> birbirine karıştırılmak üzere birlikte sunulan, birbirini tamamlayan bileşenler (iki "
  "bileşenli boya, vernik, macun) elde edilecek ürünün pozisyonunda sınıflandırılır.",
 ],
 "karistirilan": [
  ["Ayakkabı boyası", "34.05", "34.05 metninde ismen; boyayıcı lak 32.05 değil"],
  ["Karışmamış, yüzey işlem görmemiş titan dioksit", "28.23", "Pigment olarak hazırlanmışı 32.06"],
 ],
}

# ---------------------------------------------------------------- 33
F[33] = {
 "kademe": "A",
 "sinavda": "Son 5 sınavda 3 kez: perakende kontak lens solüsyonu 33.07 (38.24, 34.01, 34.02 çeldirici); el "
            "sabununun (34.01) diş macunu, diş ipliği, saç boyası ve lens solüsyonundan farklı fasılda olduğu; "
            "parfüm + not defterinin set olmadığı (GYK 3(b)). Ruj–diş macunu–parfüm–şampuan sıralaması çeldiriciydi.",
 "pozisyonlar": [
  ["33.01", "Uçucu yağlar, rezinoitler; damıtık aromatik sular"],
  ["33.02", "Koku verici karışımlar; içecek aroma bazları"],
  ["33.03", "Parfüm, tuvalet suyu, kolonya"],
  ["33.04", "Makyaj, cilt bakımı, güneş; manikür-pedikür"],
  ["33.05", "Saç: şampuan, perma, sprey, saç boyası"],
  ["33.06", "Ağız-diş: diş macunu, ağız suyu, diş ipliği"],
  ["33.07", "Tıraş, deodorant, banyo, oda kokusu, lens solüsyonu"],
 ],
 "hap": [
  "<b>Sıralama:</b> parfüm 33.03 → ruj ve oje 33.04 → şampuan 33.05 → diş macunu 33.06 → tıraş köpüğü, "
  "deodorant, lens solüsyonu 33.07.",
  "<b>Not 4 – 33.07’de ismen:</b> kontak lens ve suni göz solüsyonları, koku yastıkları, yakılarak kullanılan "
  "kokulu müstahzarlar, parfümlü veya kozmetikli kağıt, vatka, keçe; hayvan tuvalet müstahzarları.",
  "<b>Fasıl 34 Not 1(c):</b> sabun veya yüzey aktif madde içerse de şampuan 33.05, diş macunu 33.06, tıraş "
  "kremi ve köpüğü ile banyo müstahzarları 33.07; kalıp sabun ise 34.01.",
  "<b>Tedavi edici özellik çıkarmaz:</b> 33.03–33.07 ürünleri eczacılık maddesi içerse de Fasıl 33’te kalır "
  "(Fasıl 30 Not 1(e)); asıl kullanımı tedavi olan müstahzar ise Fasıl 30.",
  "<b>Not 3:</b> karışım olmayan ürün de bu kullanıma uygun ve perakende ambalajlıysa 33.03–33.07’ye girer; "
  "uçucu yağların damıtık suları (gül suyu) her halde 33.01.",
  "<b>Ayrımlar:</b> saça uygulanan 33.05, vücut tüyü ve tüy dökücü 33.07; oje 33.04, ayak deodorantı ve tırnak "
  "tedavisi 33.07; tuvalet sirkesi 33.04, tıraş losyonu 33.07.",
  "<b>Set değil (GYK 3(b)):</b> parfüm veya tıraş losyonu, not defteri ya da kemer gibi ilgisiz eşyayla "
  "birlikte paketlense de set sayılmaz; her eşya kendi pozisyonunda.",
  "<b>Not 1 hariçleri:</b> 13.02 bitkisel hülasaları ve tabii yağ reçineleri, 34.01 sabunları, terebentin "
  "esansı 38.05. Ham vazelin 27.12; parfümlü mum 34.06.",
 ],
 "karistirilan": [
  ["El sabunu (kalıp veya perakende sıvı)", "34.01", "Sabun Fasıl 34; sabunlu şampuan ve diş macunu 33"],
  ["Perakende kontak lens solüsyonu", "33.07", "Not 4’te ismen; 34.02 veya 38.24 değil"],
  ["Ham vazelin", "27.12", "Perakende cilt bakımı için hazırlanmışı 33.04"],
  ["Ekzema kremi gibi tıbbi müstahzar", "30.04", "Asıl kullanımı tedavi; dökme ise 30.03"],
  ["Parfümlü mum", "34.06", "Tütsü ve yakılan kokulu müstahzar ise 33.07"],
  ["Gül suyu (perakende olsa da)", "33.01", "Not 3: damıtık aromatik sular 33.03–33.07’ye girmez"],
 ],
}

# ---------------------------------------------------------------- 34
F[34] = {
 "kademe": "B",
 "sinavda": "Son 5 sınavda 1 kez doğrudan: el sabununun (34.01) diş macunu, diş ipliği, saç boyası ve lens "
            "solüsyonundan (Fasıl 33) farklı fasılda olduğu. Seçeneklerde 34.05 (ayakkabı boyası) ve lens "
            "solüsyonu, tıbbi sabun sorularında 34.01 / 34.02 çeldirici.",
 "pozisyonlar": [
  ["34.01", "Sabun; perakende cilt yıkama sıvısı; sabunlu kağıt"],
  ["34.02", "Yüzey aktif maddeler, deterjanlar, temizleme müstahzarları"],
  ["34.03", "Yağlama müstahzarları (petrol yağı %70’ten az)"],
  ["34.04", "Suni ve müstahzar mumlar"],
  ["34.05", "Ayakkabı boyası, cilalar, ovma tozları"],
  ["34.07", "Model patı, dişçi mumu, alçı esaslı dişçilik müstahzarı"],
 ],
 "hap": [
  "<b>Not 1(c):</b> sabun veya yüzey aktif madde içeren şampuan, diş macunu, tıraş kremi ve köpüğü, banyo "
  "müstahzarları Fasıl 33’tedir; blok tıraş sabunu ise 34.01.",
  "<b>Not 2 – sabun:</b> yalnız suda eriyen sabun; dezenfektan, ilaç veya aşındırıcı içerebilir. Aşındırıcılı "
  "sabun kalıp, çubuk, topak halindeyse 34.01; toz veya macunsa 34.05.",
  "<b>Cilt yıkama:</b> sentetik yüzey aktif esaslı sıvı veya krem cilt yıkama müstahzarı perakende ise 34.01, "
  "dökme ise 34.02. Tıbbi madde içeren sabun da 34.01’dedir (Fasıl 30 değil).",
  "<b>Not 3 – yüzey aktif:</b> 20 °C’de %0,5 oranında suyla karıştırılıp 1 saat bekletilince stabil emülsiyon "
  "vermeli ve suyun yüzey gerilimini 45 dyn/cm veya daha aza indirmeli.",
  "<b>Mumlar (Not 5):</b> karıştırılmamış tabii mum 15.21, mineral mum ve karışımları 27.12, kimyasal yolla "
  "elde edilen veya karışık mum 34.04; ışık mumu 34.06.",
 ],
 "karistirilan": [
  ["Sabunlu şampuan", "33.05", "Not 1(c); diş macunu 33.06, tıraş köpüğü 33.07"],
  ["Ayakkabı boyası (cila, krem)", "34.05", "Pozisyonda ismen; 32.05 veya 38.24 değil"],
  ["≥ %70 petrol yağlı yağlama yağı", "27.10", "34.03 yalnız petrol yağı %70’ten az olanlar"],
 ],
}

# ---------------------------------------------------------------- 35
F[35] = {
 "kademe": "B",
 "sinavda": "Son 5 sınavda 2 kez: “30. fasılda sınıflandırılmaz” kalıbında tedavi amaçlı hazırlanmamış kan "
            "albümini (35.02); “aynı fasılda sınıflandırılmaz” kalıbında jelatin ve enzimin (Fasıl 35) yanında "
            "sertleştirilmiş protein (39.13).",
 "pozisyonlar": [
  ["35.01", "Kazein, kazeinatlar, kazein tutkalları"],
  ["35.02", "Albüminler; tedavi amaçlı olmayan kan albümini"],
  ["35.03", "Jelatin (dikdörtgen yaprak), hayvansal tutkal"],
  ["35.05", "Dekstrin (indirgen şeker ≤ %10), tadil nişasta"],
  ["35.06", "Müstahzar tutkal; net ≤ 1 kg perakende tutkal"],
  ["35.07", "Enzimler; peynir mayası (rennin) dahil"],
 ],
 "hap": [
  "<b>Not 1 – fasıl dışı:</b> mayalar 21.02, kan fraksiyonları Fasıl 30 (tedavi için hazırlanmamış "
  "kan albümini 35.02’de kalır), ön dabaklama enzimi 32.02, enzimli deterjan Fasıl 34, sertleştirilmiş protein 39.13.",
  "<b>Not 2 – dekstrin:</b> dekstroz olarak indirgen şeker kuru maddede %10 veya daha az; fazlası 17.02.",
  "<b>Tutkal:</b> kazein, hayvansal ve nişasta tutkalları dökme ise kendi pozisyonlarında; net ağırlığı 1 kg’ı "
  "geçmeyen perakende tutkal ambalajı hepsini 35.06’ya çeker (Bölüm VI Not 2).",
  "<b>Jelatin şekli:</b> dikdörtgen veya kare yaprak 35.03; başka şekilde kesilmiş veya kalıplanmış "
  "sertleştirilmemiş jelatin (kapsül) 96.02; sertleştirilmiş jelatin 39.13.",
  "<b>Eşikler:</b> peyniraltı suyu proteini kuru maddede %80’den fazla ise 35.02, değilse 04.04; protein "
  "izolatı (35.04) en az %90 protein içerir.",
 ],
 "karistirilan": [
  ["Sertleştirilmiş protein (kazein, jelatin)", "39.13", "Not 1(e); plastik sayılır, Fasıl 35 dışı"],
  ["Bira ve ekmek mayası", "21.02", "Not 1(a); peynir mayası enzimdir, 35.07"],
  ["Tedavi amaçlı hazırlanmış kan albümini", "30.02", "Hazırlanmamışı 35.02; kurutulmuş kan 05.11"],
 ],
}

# ---------------------------------------------------------------- 36
F[36] = {
 "kademe": "C",
 "sinavda": "Son 5 sınavda doğrudan sorulmadı, seçeneklerde de yer almadı; önceki sınavlarda LPG dolu plastik "
            "çakmak gaz haznesinin 96.13’te olduğu (27.11, 39.26 çeldirici) soruldu.",
 "pozisyonlar": [
  ["36.02", "Müstahzar patlayıcılar: dinamit, ANFO"],
  ["36.04", "Havai fişek, işaret fişeği, oyuncak kapsülü"],
  ["36.05", "Kibritler (Bengal kibriti hariç)"],
  ["36.06", "Çakmak taşı; ≤ 300 cm3 çakmak yakıtı"],
 ],
 "hap": [
  "<b>Not 1:</b> kimyaca belirli izole bileşikler fasıl dışıdır (TNT 29.04, civa fulminat 28.52); Fasıl 36 "
  "karışımları kapsar. Nitroselüloz (pamuk barutu) 39.12, fişek kovanı 93.06.",
  "<b>Not 2 – ateş alıcı maddeler yalnız:</b> tablet veya çubuk halinde metaldehit ve hekzamin yakıtı, katı "
  "alkol yakıtları; çakmak için ≤ 300 cm3 kaptaki sıvı yakıt; reçineli meşale, ateş yakıcılar.",
  "<b>Çakmak ayrımı:</b> çakmak taşı (ferro-seryum) her şekilde 36.06; çakmağın parçası olan doldurulabilir gaz "
  "haznesi veya kartuş 96.13; dökme LPG 27.11.",
 ],
 "karistirilan": [
  ["LPG dolu plastik çakmak gaz haznesi", "96.13", "Çakmak aksamı; 27.11 veya 39.26 değil"],
  ["Bengal kibriti", "36.04", "Sürtünmeyle tutuşsa da pirotekni; kibrit 36.05 değil"],
 ],
}

# ---------------------------------------------------------------- 37
F[37] = {
 "kademe": "C",
 "sinavda": "Son 5 sınavda doğrudan sorulmadı, seçeneklerde de yer almadı; boş → dolu → develope sırası, "
            "kağıt/film ayrımı ve 37.07’nin sunum şartı yeterlidir.",
 "pozisyonlar": [
  ["37.01", "Boş hassas düz levha ve film"],
  ["37.04", "Dolu fakat develope edilmemiş her malzeme"],
  ["37.05", "Develope levha ve film; slayt, mikrofilm"],
  ["37.07", "Fotoğraf kimyasalları, flaş maddeleri"],
 ],
 "hap": [
  "<b>Sıra:</b> boş düz levha ve film 37.01, boş rulo film 37.02, boş kağıt-karton-mensucat 37.03, dolu "
  "develope edilmemiş 37.04, develope levha ve film 37.05, develope sinema filmi 37.06.",
  "<b>Develope kağıt fasıl dışı:</b> hassas kağıt, karton, mensucat yalnız develope edilmemiş halde Fasıl 37’de; "
  "basılı fotoğraf Fasıl 49. Döküntüler fasıl dışı (Not 1); kıymetli metalli olanlar 71.12.",
  "<b>37.07:</b> karışımlar her sunumda, karışmamış maddeler yalnız ölçülü veya perakende kullanıma hazır halde; "
  "gümüş nitrat perakende olsa da 28.43 (Bölüm VI Not 1).",
 ],
 "karistirilan": [
  ["Yalnız manyetik ses izli sinema filmi", "85.23", "37.06 için ses izi fotoelektrik olmalı"],
  ["Fotoğraf makinesi, flaş lambası", "90.06", "Fasıl 37 yalnız hassas malzeme ve kimyasalları kapsar"],
 ],
}

# ---------------------------------------------------------------- 38 (+ Bölüm VI Not 4)
F[38] = {
 "kademe": "B",
 "sinavda": "Son 5 sınavda 1 kez doğrudan: sınai yağ alkolleri 38.23 (15.18, 15.20, 29.34, 38.24 çeldirici). "
            "Seçeneklerde 38.25 (miadı dolmuş ilaç 30.06), 38.24 (lens solüsyonu 33.07) ve sıralamada biyodizel 38.26.",
 "pozisyonlar": [
  ["38.08", "Haşarat, ot öldürücü, dezenfektan (perakende veya müstahzar)"],
  ["38.22", "Laboratuvar teşhis reaktifleri; sertifikalı referans maddeler"],
  ["38.23", "Sınai yağ asitleri ve yağ alkolleri"],
  ["38.24", "Başka yerde yer almayan kimyasal ürünler"],
  ["38.25", "Şehir atığı, kanalizasyon çamuru, klinik atık"],
  ["38.26", "Biyodizel (petrol yağı %70’ten az)"],
 ],
 "hap": [
  "<b>Not 1(a):</b> kimyaca belirli izole bileşik Fasıl 28–29’dadır; istisnalar suni grafit 38.01, 38.08 "
  "şekilli ürünler, söndürücü dolgular 38.13, sertifikalı referans maddeler, Not 3(a)/(c) ürünleri.",
  "<b>38.23 saflık sınırı:</b> yağ alkolü ve yağ asidi %90’dan (oleik asit %85’ten) az saflıktaysa 38.23; daha "
  "safı 29.05, 29.15, 29.16; ham gliserol 15.20.",
  "<b>%70 petrol yağı:</b> fren sıvısı 38.19 ve biyodizel 38.26 için petrol yağı %70’ten az olmalı (fazlası "
  "27.10); karma çözücü ve tinerde (38.14) oran önemsiz.",
  "<b>Atıklar (Not 4–6):</b> şehir atığı, kanalizasyon çamuru, klinik atık, atık çözücü 38.25; petrol yağı "
  "esaslı atık 27.10, miadı dolmuş ilaç 30.06, stabilize gübre çamuru Fasıl 31.",
  "<b>Bölüm VI Not 4:</b> ismen veya işleviyle başka bir Bölüm VI pozisyonuna uyan halojenli karışım 38.27’de "
  "değil o pozisyonda sınıflandırılır; 38.27 son duraktır.",
 ],
 "karistirilan": [
  ["Kullanım süresi geçmiş hazır ilaç", "30.06", "Fasıl 30 Not 4(k); 38.25 atık değil"],
  ["Hastaya uygulanan teşhis reaktifi", "30.06", "38.22 yalnız laboratuvarda kullanılan reaktifler"],
  ["Doldurulmuş yangın söndürme cihazı", "84.24", "Yalnız dolgu ve söndürücü bombalar 38.13"],
 ],
}

LIM = {"A": ((8, 12), (6, 8), (4, 6)), "B": ((4, 6), (4, 5), (2, 3)), "C": ((2, 4), (2, 3), (1, 2))}


def wc(s):
    return len(re.sub(r"</?[bi]>|<br/>", " ", s).split())


def kontrol(n, d):
    msgs = []
    (pmin, pmax), (hmin, hmax), (kmin, kmax) = LIM[d["kademe"]]
    if not pmin <= len(d["pozisyonlar"]) <= pmax:
        msgs.append(f"pozisyonlar {len(d['pozisyonlar'])} ({pmin}-{pmax})")
    if not hmin <= len(d["hap"]) <= hmax:
        msgs.append(f"hap {len(d['hap'])} ({hmin}-{hmax})")
    if not kmin <= len(d["karistirilan"]) <= kmax:
        msgs.append(f"karistirilan {len(d['karistirilan'])} ({kmin}-{kmax})")
    for c, t in d["pozisyonlar"]:
        if not re.fullmatch(r"\d\d\.\d\d", c) or not c.startswith(f"{n:02d}."):
            msgs.append(f"kod {c}")
        if wc(t) > 8:
            msgs.append(f"poz uzun ({wc(t)}): {t}")
    for h in d["hap"]:
        if wc(h) > 30:
            msgs.append(f"hap uzun ({wc(h)}): {h[:50]}")
    for g, c, w in d["karistirilan"]:
        if wc(g) > 8:
            msgs.append(f"eşya uzun ({wc(g)}): {g}")
        if wc(w) > 12:
            msgs.append(f"neden uzun ({wc(w)}): {w}")
        if not re.fullmatch(r"\d\d\.\d\d", c):
            msgs.append(f"kod {c}")
    return msgs


def main():
    os.makedirs(OUT, exist_ok=True)
    for n, d in sorted(F.items()):
        rec = {"tur": "hap", "fasil": n, "kademe": d["kademe"], "sinavda": d["sinavda"],
               "pozisyonlar": d["pozisyonlar"], "hap": d["hap"], "karistirilan": d["karistirilan"]}
        for m in kontrol(n, d):
            print(f"  fasıl {n}: {m}")
        with open(os.path.join(OUT, f"fasil_{n:02d}.json"), "w", encoding="utf-8") as f:
            json.dump(rec, f, ensure_ascii=False, indent=1)
            f.write("\n")
    print("yazıldı:", ", ".join(f"fasil_{n:02d}.json" for n in sorted(F)))


if __name__ == "__main__":
    main()
