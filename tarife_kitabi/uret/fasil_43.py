#!/usr/bin/env python3
# Fasıl 43 modülü üreticisi
import json, os

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

E4 = "Eşya → 4’lü pozisyon"
OT = "Olumsuz teşhis"
FA = "Farklı/aynı pozisyon veya fasıl"
FN = "Fasıl notu · Tanım/Eşik"
GY = "Genel Yorum Kuralı"
ES = "Eşleştirme / Boşluk doldurma"
CC = "Çoktan-çoğa (I–IV)"
SN = "Senaryo"

d = {
 "tur": "fasil",
 "fasil": 43,
 "baslik": "Postlar, kürkler ve taklit kürkler; bunların mamulleri",
 "bolum": "VIII",
 "oz": {
  "vurgu": "Fasıl 43 dört basamaklı bir merdivendir: ham kürk (43.01), dabaklanmış kürk (43.02), kürkten eşya (43.03) ve taklit kürk (43.04). İlk soru tüylü derinin ham halde Fasıl 41’de mi kaldığıdır (sığır, at, koyun, keçi, domuz, geyik, ceylan, deve, köpek); ikinci soru ise kürkün başka maddeyle birleştirilip birleştirilmediği veya eşya şekline girip girmediğidir.",
  "maddeler": [
   "“Kürk” (Not 1): 43.01’deki ham kürkler hariç, tüm hayvanların tüyü veya yünü alınmamış dabaklanmış veya aprelenmiş derileridir; hayvan türü önemsizdir (kılıyla dabaklanmış buzağı, tay, koyun derisi de kürktür).",
   "Ham kürk temizlenmiş, kurutulmuş, tuzlanmış, kaba kılı alınmış veya etli yüzü kazınmış olabilir; baş, kuyruk ve pençe dahildir; kürkçülüğe elverişsiz döküntü 05.11’dedir.",
   "43.02: dabaklanmış kürk, birleştirilmemiş ya da başka madde katılmadan birleştirilmiş (plaka, haç, torba, drope kürk); 43.03: diğer maddeyle birleştirilmiş veya eşya şeklinde dikilmiş kürk (Not 3).",
   "Kürk astarlı ya da dışında süsü aşan kürk bulunan giysi 43.03 / 43.04’tedir (Not 4); yaka, kol kıvrımı, cep ve etek kenarı kürkü basit süstür.",
   "Taklit kürk (Not 5) liflerin deri veya mensucat üzerine yapıştırılması ya da dikilmesiyle elde edilir; dokuma veya örme tüylü kumaşlar 58.01 / 60.01’dedir."
  ]
 },
 "karar_tablosu": {
  "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
  "satirlar": [
   ["1", "Tüylü kuş derisi veya tüylü kuş derisi parçası mı?", "<b>05.05</b> / <b>67.01</b>"],
   ["2", "Tüylü HAM deri ve hayvan Fasıl 41 Not 1(c) istisnasında mı? (sığır, at, koyun-kuzu, keçi, domuz, dağ keçisi, ceylan, deve, geyik, ren geyiği, karaca, köpek)*", "<b>41.01</b> / <b>41.02</b> / <b>41.03</b>"],
   ["3", "Ayakkabı, başlık veya oyuncak-oyun-spor eşyası mı?", "Fasıl <b>64</b> / <b>65</b> / <b>95</b>"],
   ["4", "Deri ve kürkten (veya deri ve taklit kürkten) eldiven mi?", "<b>42.03</b> (tamamen kürkten eldiven 43.03)"],
   ["5", "42.02’nin ilk kısmındaki bir mahfaza mı? (bavul, valiz vb.)", "<b>42.02</b>"],
   ["6", "Dabaklanmamış ham kürk mü? (baş, kuyruk, pençe dahil)", "<b>43.01</b> (kürkçülüğe elverişsiz döküntü 05.11)"],
   ["7", "Dabaklanmış-aprelenmiş; birleştirilmemiş veya başka madde katılmadan birleştirilmiş mi?", "<b>43.02</b>"],
   ["8", "Kürkten giysi, aksesuar veya diğer eşya; kürk astarlı ya da süsü aşan kürklü giysi; başka maddeyle birleştirilmiş kürk mü?", "<b>43.03</b>"],
   ["9", "Taklit kürk ya da taklit kürkten eşya mı?", "<b>43.04</b> (dokuma-örme tüylü kumaş 58.01 / 60.01)"]
  ],
  "dipnot": "* İstisnanın da istisnası: Astragan, Karakul, Persaniye, breitschwanz ve benzerleri ile Hint, Çin, Moğol, Tibet kuzuları ve Yemen, Moğol, Tibet keçi ve oğlakları Fasıl 41’de kalmaz, ham kürk olarak 43.01’e gider."
 },
 "pozisyon_haritasi": [
  ["43.01", "Ham kürkler", "Fasıl 41’de kalanlar hariç; baş, kuyruk, pençe dahil", "Ham vizon, tilki, Karakul kuzusu derisi"],
  ["43.02", "Dabaklanmış veya aprelenmiş kürkler", "Başka madde eklenmeden birleştirilmiş olabilir", "Dabaklı vizon derisi, kürk plaka, drope kürk"],
  ["43.03", "Kürkten giyim eşyası ve diğer eşya", "Kürk astarlı veya süsü aşan kürklü giysi dahil", "Kürk manto, manşon, kürk el çantası"],
  ["43.04", "Taklit kürk ve eşyası", "Lif yapıştırılmış veya dikilmiş; dokuma-örme hariç", "Taklit kürk mont, taklit kuyruk"]
 ],
 "notlar": [
  ["Fasıl 43 Not 1", "Tarifenin neresinde geçerse geçsin “kürk”: 43.01’deki ham kürkler hariç, tüm hayvanların dabaklanmış veya aprelenmiş, tüyü veya yünü alınmamış post ve derileri."],
  ["Fasıl 43 Not 2", "Hariç: (a) kuşların tüylü derileri ve tüylü diğer kısımları (05.05, 67.01); (b) Fasıl 41 Not 1(c)’de yer alan tüylü ham post ve deriler; (c) deri ve kürkten veya deri ve taklit kürkten eldivenler (42.03); (d) Fasıl 64 eşyası; (e) Fasıl 65 başlıkları ve aksamı; (f) Fasıl 95 eşyası (oyuncak, oyun ve spor malzemesi)."],
  ["Fasıl 43 Not 3", "43.03, diğer maddeler ilavesiyle birleştirilmiş kürk ve parçalarını ve giysi, giysi aksamı, aksesuar veya diğer eşya şeklinde dikilmiş kürk ve parçalarını kapsar."],
  ["Fasıl 43 Not 4", "İçi kürk veya taklit kürkle kaplı ya da dışında basit süs mahiyetini aşan kürk veya taklit kürk tutturulmuş giyim eşyası ve aksesuarları (Not 2 ile hariç tutulanlar dışında) hale göre 43.03 veya 43.04’tedir. Bölüm XI Not 1(k) de bu eşyayı dokumaya elverişli maddeler bölümünden çıkarır."],
  ["Fasıl 43 Not 5", "“Taklit kürk”: deri, mensucat veya diğer maddeler üzerine yapıştırılmış ya da dikilmiş yün, kıl veya diğer liflerden oluşan taklit kürkler. Dokuma veya örme yoluyla elde edilen taklit kürkler bu tabirin dışındadır (genellikle 58.01 veya 60.01)."],
  ["Genel Açıklamalar", "Fasıl; 41.01–41.03 dışındaki ham kürkleri, kıl veya yünüyle dabaklanmış ya da aprelenmiş (birleştirilmiş veya birleştirilmemiş) deri ve postları, kürkten giysi, aksesuar ve diğer eşyayı ve taklit kürk ile eşyasını kapsar. Tüylü kuş derileri kürk sayılmaz (05.05 veya 67.01)."],
  ["43.01 Açıklama Notu", "Fasıl 41’de kalan hayvanlar (sığır, at türü, koyun-kuzu, keçi-oğlak, domuz, dağ keçisi, ceylan, geyik, köpek; egzotik kuzu ve keçiler hariç) dışındaki tüm hayvanların yün ve kılları üzerindeki ham derileri. Temizlenmiş, kurutulmuş, kuru veya ıslak tuzlanmış, kaba kılları çıkarılmış, traş edilmiş veya etli yüzü kazınmış olanlar da hamdır. Ham baş, kuyruk, pençe dahil; kürkçülüğe elverişsiz olduğu belli döküntüler 05.11."],
  ["43.02 Açıklama Notu", "Özel bir kullanım için şekline göre kesilmemiş dabaklanmış-aprelenmiş kürkler (örtü olarak hemen kullanılabilse bile); başka madde eklenmeden dikdörtgen, kare, trapez veya haç şeklinde birleştirilmiş kürkler ve “drope kürkler” (V veya W şeklinde kesilip daha uzun ve dar post için yeniden birleştirilen kürkler); ceket-kaban yapmaya elverişli birleştirilmiş parçalar. 43.01 dışında kalan tüylü deriler (tay, buzağı, koyun derisi) dabaklanınca buradadır."],
  ["43.02 hariç tutmaları", "Giysi, aksam, aksesuar veya diğer eşya şeklinde kabaca şekil verilmiş kürkler ve birleştirilmiş parçalar; kullanıma hazır süsler veya yalnız boyuna kesilerek süs olarak kullanılabilecekler; kürklerin diğer maddelerle birleşimleri (ör. deri veya mensucatla birleştirilmiş kuyruklar) 43.03’tedir."],
  ["43.03 Açıklama Notu", "Kürkten, astarı kürk olan veya dışında süsü aşan kürk bulunan diğer maddelerden giysi ve aksesuarlar (manşon, atkı, yaka, boyun bağı). Yaka veya devrik yaka (pelerin ya da bolero oluşturacak kadar büyük değilse), kol kıvrımı, cep, etek ve manto kenarı kürkü basit süstür. Ayrıca esas karakteri kürk olan eşya: yer örtüsü, yatak örtüsü, içi doldurulmamış minder, mahfaza, el çantası, av ve oyun torbası, sanayi amaçlı cilalama derileri."],
  ["43.03 hariç tutmaları", "42.02’nin birinci kısmındaki eşya (bavul, valiz vb.); deri ve kürkten eldivenler (42.03; tamamen kürkten olanlar 43.03’te); Fasıl 64 eşyası; Fasıl 65 başlıkları (kürk şapka 65.06); Fasıl 95 eşyası."],
  ["43.04 Açıklama Notu", "Kürkü taklit edecek şekilde deri, dokunmuş mensucat ve başka maddeler üzerine yün, kıl veya diğer liflerin (tırtıl iplik dahil) yapıştırılması veya dikilmesiyle elde edilen ürünler ve bunlardan eşya; mesnede yün ve kıl yapıştırılarak yapılan taklit kuyruklar dahil. Hariç: uzun tüylü dokuma veya örme kumaşlar (58.01, 60.01), gerçek kürke tüy eklenmiş “iğne işi” kürkler, hakiki kuyruk veya kürk parçalarından yapılmış kuyruklar (43.03)."]
 ],
 "sinir_komsulari": [
  ["Telekleri üzerinde kuş derisi", "05.05 / 67.01", "Fasıl 43 Not 2(a)"],
  ["Kürkçülüğe elverişsiz ham kürk döküntüsü", "05.11", "43.01 Açıklama Notu"],
  ["Kılı alınmamış ham sığır, at, geyik, köpek derisi", "41.01 / 41.03", "Fasıl 41 Not 1(c); Fasıl 43 Not 2(b)"],
  ["Yünü alınmamış ham koyun derisi (sıradan koyun)", "41.02", "Fasıl 41 Not 1(c)"],
  ["Deri ve kürkten eldiven", "42.03", "Fasıl 43 Not 2(c)"],
  ["Dış yüzü kürkle kaplı bavul veya valiz", "42.02", "43.03 hariç tutması (42.02 ilk kısım)"],
  ["Kürk astarlı bot", "Fasıl 64", "Not 2(d)"],
  ["Kürkten veya taklit kürkten şapka", "65.06", "Not 2(e)"],
  ["Kürkten oyuncak", "Fasıl 95", "Not 2(f)"],
  ["Uzun tüylü dokuma kadife-pelüş (“kürk kumaş”)", "58.01", "Not 5"],
  ["Örme uzun tüylü mensucat", "60.01", "Not 5"],
  ["Yalnız yakası kürkle süslenmiş dokuma yün manto", "62.02", "Kürk basit süs; Not 4 uygulanmaz"],
  ["Kılıyla dabaklanmış buzağı veya koyun derisi", "43.02", "Fasıl 41 değil; Not 1 kürk tanımı"],
  ["Hakiki kürk parçalarından yapılmış kuyruk", "43.03", "43.04 hariç tutması"]
 ],
 "tuzaklar": [
  "<b>Kürk = kılıyla dabaklanmış deri, hayvan fark etmez.</b> Not 1’e göre dabaklanmış-aprelenmiş tüylü deri kürktür; kılıyla dabaklanmış buzağı, tay veya koyun derisi de 43.02’dedir.",
  "<b>Ham halde hayvan türü belirleyicidir.</b> Sığır, at, koyun, keçi, domuz, geyik, ceylan, deve ve köpeğin tüylü ham derisi Fasıl 41’de; vizon, tilki, Karakul-Astragan kuzusu, Tibet-Yemen keçisi gibi hayvanlarınki 43.01’dedir.",
  "<b>Temizleme, tuzlama, kazıma ham kürkü değiştirmez.</b> Bu işlemlerden geçen kürk 43.01’de kalır; kürkçülüğe elverişsiz döküntü ise 05.11.",
  "<b>Birleştirme tek başına eşya yapmaz.</b> Başka madde katılmadan dikilerek birleştirilen kürk plakaları, haç, torba ve drope kürkler 43.02’de kalır; giysi şeklinde kabaca şekillendirilen veya başka maddeyle birleştirilen kürk 43.03’e geçer.",
  "<b>Kürk yaka giysiyi kürk yapmaz.</b> Yaka, kol kıvrımı, cep ve etek kenarı basit süstür; kürk astar veya süsü aşan kürk giysiyi 43.03 / 43.04’e götürür.",
  "<b>Eldivenin kendi kuralı vardır.</b> Deri ve kürkten (veya taklit kürkten) eldiven 42.03’te, tamamen kürkten eldiven 43.03’te.",
  "<b>Kürk el çantası 43.03, kürk kaplı valiz 42.02.</b> 42.02’nin ilk kısmındaki eşya her maddeden olabileceği için 43.03’ten hariçtir; el çantası için kürk 42.02’de izin verilen madde değildir.",
  "<b>Kürk şapka, kürk bot, kürk oyuncak Fasıl 43 değildir.</b> Başlıklar Fasıl 65, ayakkabılar Fasıl 64, oyuncaklar Fasıl 95 (Not 2).",
  "<b>Dokunmuş veya örülmüş “kürk kumaş” taklit kürk değildir.</b> Taklit kürk liflerin mesnede yapıştırılması veya dikilmesiyle olur (43.04); uzun tüylü dokuma ve örme kumaşlar 58.01 / 60.01.",
  "<b>Kuyruğun malzemesine bakın.</b> Yün veya kılın mesnede yapıştırılmasıyla yapılan taklit kuyruk 43.04; hakiki kuyruklardan veya kürk parçalarından yapılan kuyruk 43.03."
 ],
 "hafiza": {
  "kanca": "HAM – DABAK – EŞYA – TAKLİT (43.01 · 43.02 · 43.03 · 43.04)",
  "aciklama": "Bir kürkçü dükkânı düşünün: arka depoda ham kürkler (43.01), atölyede dabaklanıp dikilen plakalar (43.02), vitrinde manto, manşon ve çantalar (43.03), köşedeki reyonda taklit kürkler (43.04). Kapıdaki bekçi Fasıl 41’dir: sığır, at, koyun, keçi, domuz, geyik, deve ve köpeğin ham tüylü derisi dükkâna giremez."
 },
 "sinav_odagi": [
  "Fasıl 41 Not 1(c) ile Fasıl 43 ayrımı: “hangi hayvanın tüyleri ve yünleri alınmamış ham derisi 43. Fasılda sınıflandırılır” sorusunda Tibet keçisi doğru cevap, at, hecin devesi ve ren geyiği çeldiricidir.",
  "Bölüm VIII kapsamı: kürklerin, köselelerin, çantaların ve kedi-köpek elbiselerinin bölümde yer aldığı, ayakkabıların yer almadığı soruldu.",
  "Taklit kürk (43.04), pozisyon numaralarını küçükten büyüğe sıralama sorularında seçeneklerden birinde kullanılmıştır.",
  "Fasıl 43 doğrudan az sorulmuştur; daha çok tüylü ham derinin Fasıl 41 ile ayrımı ve bölüm kapsamı sorularında yer almıştır."
 ],
 "cikmis_ornekler": [
  {
   "soru": "Aşağıdaki hayvanlardan hangisinin tüyleri ve yünleri alınmamış ham derileri 43. Fasılda sınıflandırılır?",
   "secenekler": ["Tibet keçisi", "İngiliz atı", "Hecin devesi", "Ren geyiği"],
   "cevap": "A",
   "aciklama": "Fasıl 41 Not 1(c), Yemen, Moğol ve Tibet keçi ve oğlaklarını Fasıl 41’de kalan hayvanlar istisnasının dışında tutar; tüylü ham Tibet keçisi derisi ham kürk olarak 43.01’dedir. At, deve ve ren geyiğinin tüylü ham derileri Fasıl 41’dedir."
  },
  {
   "soru": "Aşağıdakilerden hangisi VIII’inci Bölümde yer alan eşyalardan değildir?",
   "secenekler": ["Kürkler", "Köseleler", "Çantalar", "Ayakkabılar", "Kedi / Köpek elbiseleri"],
   "cevap": "D",
   "aciklama": "Bölüm VIII; deri ve köseleleri (Fasıl 41), çantalar ve köpek elbiseleri gibi saraciye eşyasını (Fasıl 42) ve kürkleri (Fasıl 43) kapsar. Ayakkabılar Fasıl 64’tedir; Fasıl 42 ve 43 notları da Fasıl 64 eşyasını açıkça hariç tutar."
  }
 ],
 "ozet": [
  "Kürk (Not 1): ham kürkler hariç, tüyü veya yünü alınmamış dabaklanmış-aprelenmiş deri; hayvan türü önemsiz.",
  "Tüylü ham deri: Fasıl 41 hayvanları (sığır, at, koyun, keçi, domuz, geyik, ceylan, deve, köpek) 41.01–41.03; diğerleri (vizon, tilki, egzotik kuzu ve keçiler) 43.01.",
  "43.02: dabaklanmış kürk; birleştirilmemiş veya başka madde katılmadan birleştirilmiş (plaka, haç, torba, drope).",
  "43.03: kürkten giysi, aksesuar ve eşya; kürk astarlı veya süsü aşan kürklü giysi; başka maddeyle birleştirilmiş kürk; tamamen kürkten eldiven.",
  "43.04: lif yapıştırılarak veya dikilerek yapılan taklit kürk ve eşyası; dokuma-örme tüylü kumaş 58.01 / 60.01.",
  "Hariç: tüylü kuş derisi 05.05 / 67.01, deri-kürk eldiven 42.03, kürk kaplı valiz 42.02, ayakkabı 64, başlık 65, oyuncak 95."
 ],
 "sorular": [
  {
   "soru": "Tarife Cetveline göre, temizlenmiş ve kuru tuzlanarak muhafaza edilmiş, dabaklanmamış, bütün halindeki tilki postu hangi pozisyonda sınıflandırılır?",
   "secenekler": ["41.03", "43.02", "43.01", "05.11", "41.06"],
   "cevap": "C", "tip": E4,
   "gerekce": "43.01 Açıklama Notuna göre temizlenmiş, kurutulmuş veya tuzlanmış, hatta kaba kılları alınmış ya da etli yüzü kazınmış kürkler ham sayılır. Tilki, Fasıl 41 Not 1(c)’de sayılan hayvanlardan olmadığından tüylü ham derisi 41.03’e değil 43.01’e girer; dabaklanmadığı için 43.02 söz konusu değildir.",
   "dayanak": "43.01 pozisyon metni ve Açıklama Notu; Fasıl 41 Not 1(c)."
  },
  {
   "soru": "Tarife Cetvelinin 43. Fasıl notlarına göre “kürk” tabiri ile ilgili aşağıdakilerden hangisi doğrudur?",
   "secenekler": [
    "Yalnız vizon, tilki ve benzeri kürk hayvanlarının dabaklanmış veya aprelenmiş derilerini ifade eder.",
    "Tüyü veya yünü alınmış dabaklanmış derileri de kapsar.",
    "43.01’deki ham kürkler dahil, tüylü tüm ham ve dabaklanmış derileri ifade eder.",
    "Sığır ve at türü hayvanların derileri hiçbir halde kürk sayılmaz.",
    "Ham kürkler hariç, tüm hayvanların tüyü veya yünü alınmamış dabaklanmış ya da aprelenmiş derileridir."
   ],
   "cevap": "E", "tip": FN,
   "gerekce": "Fasıl 43 Not 1’e göre “kürk” tabiri, 43.01’deki ham kürkler hariç, tüm hayvanların dabaklanmış veya aprelenmiş, tüyü veya yünü alınmamış post ve derilerini ifade eder. Hayvan türü önemsiz olduğundan kılıyla dabaklanmış tay veya buzağı derisi de kürktür (43.02 Açıklama Notu); D bu nedenle yanlıştır.",
   "dayanak": "Fasıl 43 Not 1; 43.02 Açıklama Notu."
  },
  {
   "soru": "Aşağıdakilerden hangisi Tarife Cetvelinin 43. Faslında <b>sınıflandırılmaz</b>?",
   "secenekler": [
    "Kürkten manşon",
    "Deri ve kürkten yapılmış eldiven",
    "Tamamen kürkten yapılmış eldiven",
    "İçi kürk astarlı deri palto",
    "Yünü ile birlikte dabaklanmış koyun postundan yer örtüsü"
   ],
   "cevap": "B", "tip": OT,
   "gerekce": "Fasıl 43 Not 2(c) gereği deri ve kürkten (veya deri ve taklit kürkten) eldivenler 42.03’tedir. Tamamen kürkten eldiven, kürk manşon ve kürk astarlı palto 43.03’te; yünüyle dabaklanmış koyun postundan yer örtüsü de kürk olarak Fasıl 43’te yer alır.",
   "dayanak": "Fasıl 43 Not 2(c) ve Not 4; 43.03 Açıklama Notu ve hariç tutmalar."
  },
  {
   "soru": "Aşağıdakilerden hangisi Tarife Cetvelinde diğerlerinden farklı bir fasılda sınıflandırılır?",
   "secenekler": [
    "Ham vizon derisi",
    "Kılı alınmamış ham Tibet keçisi derisi",
    "Yünü alınmamış ham Persaniye kuzusu derisi",
    "Kılı alınmamış ham geyik derisi",
    "Ham tilki derisi"
   ],
   "cevap": "D", "tip": FA,
   "gerekce": "Geyik, Fasıl 41 Not 1(c)’de tüylü ham derisi Fasıl 41’de kalan hayvanlar arasında sayılır (41.03). Vizon ve tilki kürk hayvanıdır; Tibet keçisi ve Persaniye kuzusu ise istisnanın dışında tutulduğundan tüylü ham derileri 43.01’dedir.",
   "dayanak": "Fasıl 41 Not 1(c); Fasıl 43 Not 2(b); 43.01 Açıklama Notu."
  },
  {
   "soru": "Bir kürk atölyesi; dabaklanmış vizon derilerini V şeklinde şeritler halinde kesip daha uzun ve dar bir post elde edecek şekilde yeniden birleştirmiş ve başka hiçbir madde eklemeden dikdörtgen plakalar haline getirmiştir. Plakalar daha sonra manto yapımında kullanılacaktır. Bu ürün Tarife Cetveline göre hangi pozisyonda sınıflandırılır?",
   "secenekler": ["43.02", "43.03", "43.01", "43.04", "62.02"],
   "cevap": "A", "tip": SN,
   "gerekce": "43.02 Açıklama Notuna göre başka madde eklenmeksizin dikdörtgen, trapez veya haç şeklinde dikilerek birleştirilmiş dabaklanmış kürkler ve “drope kürkler” (V veya W şeklinde kesilip yeniden birleştirilmiş kürkler) bu pozisyondadır. Giysi şeklinde kabaca şekil verilmediği ve başka maddeyle birleştirilmediği için 43.03’e gitmez.",
   "dayanak": "43.02 pozisyon metni ve Açıklama Notu; Fasıl 43 Not 3."
  },
  {
   "soru": "Tarife Cetveline göre, tüyleri ile birlikte dabaklanmış, birleştirilmemiş ve özel bir kullanım için kesilmemiş tay derisi hangi pozisyonda sınıflandırılır?",
   "secenekler": ["41.04", "41.07", "43.01", "43.02", "43.03"],
   "cevap": "D", "tip": E4,
   "gerekce": "43.02 Açıklama Notu, 43.01 dışında kalan tüylü veya yünlü derilerin (tay, buzağı, koyun derisi gibi) dabaklanmış veya aprelenmiş halde 43.02’de yer aldığını belirtir. Fasıl 41 Not 1(c)’deki istisna yalnız ham deriler içindir; 41.04 ve 41.07 kılı alınmış deriler içindir.",
   "dayanak": "43.02 Açıklama Notu; Fasıl 43 Not 1; 41.04 hariç tutması (c)."
  },
  {
   "soru": "43.03 Açıklama Notuna göre, kürk ve deri parçalarından oluşan ve esas karakterini kürkün verdiği bir yatak örtüsü kürkten eşya olarak 43.03’te sınıflandırılır. Bu değerlendirmede kullanılan “esas karakter” ölçütü hangi Genel Yorum Kuralının ilkesidir?",
   "secenekler": ["GYK 2(a)", "GYK 3(b)", "GYK 3(c)", "GYK 5(a)", "GYK 4"],
   "cevap": "B", "tip": GY,
   "gerekce": "Farklı maddelerden oluşan eşya GYK 2(b) yoluyla GYK 3’e tabidir ve GYK 3(b) uyarınca esas niteliğini veren maddeye göre sınıflandırılır. 43.03 Açıklama Notu kürkten yapılmış veya esas karakteri kürk olan eşyayı bu pozisyona alarak bu ilkeyi uygular. GYK 3(c) numara sırası, 2(a) tamamlanmamış eşya, 5(a) mahfazalar, 4 benzerlik kuralıdır.",
   "dayanak": "43.03 Açıklama Notu; GYK 2(b) ve 3(b)."
  },
  {
   "soru": "Aşağıdakilerden hangisi 43.03 pozisyonunda <b>sınıflandırılmaz</b>?",
   "secenekler": [
    "Kürkten yapılmış el çantası",
    "Kürkten atkı ve boyun bağı",
    "Kürk astarlı deri ceket",
    "Kürkten av torbası",
    "Dış yüzü kürkle kaplı valiz"
   ],
   "cevap": "E", "tip": OT,
   "gerekce": "43.03 Açıklama Notu, 42.02’nin birinci kısmında yer alan eşyayı (sandık, bavul, valiz vb.) hariç tutar; bu eşya her maddeden olabileceği için kürkle kaplı valiz 42.02’dedir. Kürkten el çantası, atkı, av torbası ve kürk astarlı ceket 43.03’te sayılır.",
   "dayanak": "43.03 Açıklama Notu ve hariç tutmalar; 42.02 Açıklama Notu."
  },
  {
   "soru": "Tarife Cetvelinin 43. Fasıl notlarına göre “taklit kürk” tabiri ile ilgili aşağıdakilerden hangisi doğrudur?",
   "secenekler": [
    "Uzun tüylü ipliklerle dokunmuş kadife ve pelüş kumaşları da taklit kürk olarak kapsar.",
    "Örme veya kroşe yöntemiyle elde edilen uzun tüylü mensucatı da taklit kürk olarak kapsar.",
    "Deri, mensucat vb. üzerine yapıştırılmış veya dikilmiş yün, kıl ya da diğer liflerden oluşan ürünlerdir.",
    "Gerçek kürke ilave tüyler geçirilerek elde edilen “iğne işi” kürkleri ifade eder.",
    "Yalnız sentetik liflerden yapılmış olan kürk görünümlü ürünleri kapsar."
   ],
   "cevap": "C", "tip": FN,
   "gerekce": "Not 5’e göre taklit kürk; deri, mensucat veya diğer maddeler üzerine yapıştırılmış ya da dikilmiş yün, kıl veya diğer liflerden oluşur. Dokuma veya örme yoluyla elde edilen taklit kürkler bu tabirin dışındadır (genellikle 58.01 veya 60.01). 43.04 Açıklama Notu gerçek kürke tüy geçirilmiş “iğne işi” kürkleri de taklit kürk saymaz.",
   "dayanak": "Fasıl 43 Not 5; 43.04 Açıklama Notu."
  },
  {
   "soru": "Tarife Cetveline göre, deri bir mesnet üzerine yün ve kıl yapıştırılarak elde edilmiş taklit hayvan kuyrukları hangi pozisyonda sınıflandırılır?",
   "secenekler": ["43.04", "43.03", "43.02", "58.01", "05.11"],
   "cevap": "A", "tip": E4,
   "gerekce": "43.04 Açıklama Notu, deriden veya ipten bir mesnet üzerine yün ve kılların yapıştırılmasıyla elde edilen taklit kuyrukları bu pozisyonda sayar. Birkaç hakiki kuyruktan veya gerçek kürk parçalarının bir mesnede dikilmesiyle yapılan kuyruklar ise 43.03’tedir. Dokuma ürünü olmadığından 58.01 söz konusu değildir.",
   "dayanak": "43.04 Açıklama Notu; Fasıl 43 Not 5."
  },
  {
   "soru": "Aşağıdaki ürünlerin pozisyonlarla eşleştirilmesi hangi seçenekte doğru verilmiştir? I. Kuru tuzlanmış, dabaklanmamış ham vizon derisi; II. Başka madde eklenmeden haç şeklinde dikilerek birleştirilmiş dabaklanmış kürk parçaları; III. Kürkten yapılmış manşon; IV. Dokuma mensucat üzerine akrilik lifler yapıştırılarak elde edilmiş taklit kürkten yelek — a) 43.03 b) 43.01 c) 43.04 d) 43.02",
   "secenekler": [
    "I-d, II-b, III-a, IV-c",
    "I-b, II-a, III-d, IV-c",
    "I-b, II-d, III-c, IV-a",
    "I-a, II-d, III-b, IV-c",
    "I-b, II-d, III-a, IV-c"
   ],
   "cevap": "E", "tip": ES,
   "gerekce": "Ham vizon derisi 43.01’de; başka madde katılmadan haç şeklinde birleştirilmiş dabaklanmış kürkler 43.02’de; kürk manşon giyim aksesuarı olarak 43.03’te; mensucata lif yapıştırılarak elde edilen taklit kürkten yelek 43.04’tedir.",
   "dayanak": "43.01–43.04 pozisyon metinleri ve Açıklama Notları; Fasıl 43 Not 5."
  },
  {
   "soru": "Aşağıdaki kürkten veya kürk içeren eşyalardan hangisi diğerlerinden farklı bir fasılda sınıflandırılır?",
   "secenekler": ["Kürk manto", "Kürk astarlı deri yelek", "Kürkten şapka", "Kürkten yatak örtüsü", "Kürkten el çantası"],
   "cevap": "C", "tip": FA,
   "gerekce": "Fasıl 43 Not 2(e) başlıkları ve aksamını Fasıl 65’e gönderir; kürkten şapka 65.06’dadır. Kürk manto, kürk astarlı yelek, kürkten yatak örtüsü ve el çantası 43.03’te sayılır.",
   "dayanak": "Fasıl 43 Not 2(e); 43.03 Açıklama Notu; 65.06 Açıklama Notu."
  },
  {
   "soru": "Tarife Cetveline göre aşağıdaki ifadelerden hangileri doğrudur? I. Giysinin yakasını oluşturan, pelerin veya bolero oluşturacak büyüklükte olmayan kürk basit süs sayılır. II. Kol kıvrımları ve etek kenarlarındaki kürk basit süs sayılır. III. İçi tamamen kürkle astarlanmış dokuma mantoda kürk basit süs sayılır ve manto Fasıl 62’de kalır. IV. Bir giysinin dış kısmında basit süs mahiyetini aşan kürk bulunması onu 43.03’e götürür.",
   "secenekler": ["I, II ve IV", "I ve III", "II ve III", "I, III ve IV", "II, III ve IV"],
   "cevap": "A", "tip": CC,
   "gerekce": "43.03 Açıklama Notu yaka veya devrik yaka (pelerin ya da bolero oluşturacak kadar büyük değilse), kol kıvrımı, cep ve etek kenarlarındaki kürkü basit süs sayar (I, II). Not 4 uyarınca kürk astarlı veya dışında süsü aşan kürk bulunan giysiler 43.03 veya 43.04’tedir; IV doğru, III yanlıştır.",
   "dayanak": "Fasıl 43 Not 4; 43.03 Açıklama Notu."
  },
  {
   "soru": "Aşağıdakilerden hangisi 43.01 pozisyonunda <b>yer almaz</b>?",
   "secenekler": [
    "Kaba kılları alınmış, etli yüzü kazınmış ham Karakul kuzusu derisi",
    "Kılı alınmamış, tuzlanmış ham köpek derisi",
    "Ham tilki kuyruğu",
    "Kurutulmuş ham vizon derisi",
    "Kılı alınmamış ham Moğol keçisi derisi"
   ],
   "cevap": "B", "tip": OT,
   "gerekce": "Köpek, Fasıl 41 Not 1(c)’de tüylü ham derisi Fasıl 41’de kalan hayvanlardan olduğundan bu deri 41.03’tedir; 43.01 metni 41.01–41.03’teki ham derileri hariç tutar. Karakul kuzusu ve Moğol keçisi istisnanın dışında kaldığından 43.01’dedir; ham kuyruk gibi parçalar ve kurutulmuş vizon derisi de 43.01’dedir.",
   "dayanak": "43.01 pozisyon metni ve Açıklama Notu; Fasıl 41 Not 1(c)."
  },
  {
   "soru": "Tarife Cetveline göre, deri içermeyen ve tamamen kürkten yapılmış eldiven hangi pozisyonda sınıflandırılır?",
   "secenekler": ["42.03", "61.16", "62.16", "43.03", "43.04"],
   "cevap": "D", "tip": E4,
   "gerekce": "Fasıl 43 Not 2(c) yalnız deri ve kürkten (veya deri ve taklit kürkten) eldivenleri 42.03’e gönderir; 43.03 Açıklama Notu tamamen kürkten yapılmış eldivenlerin 43.03’te yer aldığını belirtir. Dokumaya elverişli maddeden eldivenler (61.16, 62.16) ve taklit kürk (43.04) söz konusu değildir.",
   "dayanak": "Fasıl 43 Not 2(c); 43.03 Açıklama Notu, hariç tutma (b)."
  },
  {
   "soru": "Tarife Cetvelinin 43. Fasıl notlarına göre 43.03 pozisyonu aşağıdakilerden hangisini kapsar?",
   "secenekler": [
    "Diğer maddelerle birleştirilmiş kürkleri ve giysi, aksesuar veya diğer eşya şeklinde dikilmiş kürkleri",
    "Başka madde eklenmeden dikdörtgen veya haç şeklinde birleştirilmiş dabaklanmış kürk plakalarını",
    "Temizlenmiş, kurutulmuş veya tuzlanmış, dabaklanmamış bütün halindeki kürkleri",
    "Deri ve kürkten veya deri ve taklit kürkten yapılmış eldivenleri",
    "Liflerin dokuma mensucat üzerine dikilmesiyle elde edilen taklit kürkleri"
   ],
   "cevap": "A", "tip": FN,
   "gerekce": "Not 3’e göre 43.03, diğer maddeler ilavesiyle birleştirilmiş kürk ve parçalarını ve giysi, giysi aksamı, aksesuar veya diğer eşya şeklinde dikilmiş kürkleri kapsar. Başka madde eklenmeden birleştirilmiş plakalar 43.02’de, ham kürkler 43.01’de, deri-kürk eldivenler 42.03’te, taklit kürk 43.04’tedir.",
   "dayanak": "Fasıl 43 Not 3; 43.02 Açıklama Notu."
  },
  {
   "soru": "Bir firma; dokunmuş yün kumaştan dikilmiş, yalnızca yakası ve kol kenarları tilki kürküyle süslenmiş kadın mantoları ithal etmektedir. Kürk yaka, pelerin veya bolero oluşturacak büyüklükte değildir. Bu eşya Tarife Cetveline göre hangi pozisyonda sınıflandırılır?",
   "secenekler": ["43.03", "43.04", "43.02", "62.02", "42.03"],
   "cevap": "D", "tip": SN,
   "gerekce": "43.03 Açıklama Notu, giysi üzerindeki yaka veya devrik yaka (pelerin ya da bolero oluşturacak kadar büyük değilse) ve kol kıvrımlarındaki kürkü basit süs sayar. Kürk basit süs olduğundan Fasıl 43 Not 4 uygulanmaz ve dokunmuş yün kadın mantosu 62.02’de kalır; Fasıl 62 Genel Açıklamaları da süs niteliğindeki kürkün sınıflandırmayı etkilemediğini belirtir.",
   "dayanak": "Fasıl 43 Not 4; 43.03 Açıklama Notu; Fasıl 62 Genel Açıklamalar."
  },
  {
   "soru": "Aşağıdakilerden hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır?",
   "secenekler": [
    "Yünü ile birlikte dabaklanmış, birleştirilmemiş koyun derisi",
    "Kılı ile birlikte dabaklanmış buzağı derisi",
    "Deri şeritle birleştirilmiş tilki kuyruklarından süs şeridi",
    "Dabaklanmış, birleştirilmemiş vizon derisi",
    "Başka madde eklenmeden dikdörtgen biçimde birleştirilmiş dabaklanmış tavşan kürkü plakası"
   ],
   "cevap": "C", "tip": FA,
   "gerekce": "43.02 Açıklama Notu, kürklerin diğer maddelerle birleşimlerini (ör. deri veya dokumaya elverişli mensucatla birleştirilmiş kuyruklar) 43.03’e gönderir. Yünüyle dabaklanmış koyun derisi, kılıyla dabaklanmış buzağı derisi, dabaklanmış vizon derisi ve başka madde katılmadan birleştirilmiş plaka 43.02’dedir.",
   "dayanak": "43.02 Açıklama Notu ve hariç tutmalar; Fasıl 43 Not 3."
  },
  {
   "soru": "Kürkten, giysi şeklinde kabaca şekil verilmiş, henüz astarı ve düğmeleri takılmamış bir manto taslağının pozisyonu ve sınıflandırma kuralı hangi seçenekte doğru verilmiştir?",
   "secenekler": ["43.02 – GYK 1 ve 6", "43.03 – GYK 3(b) ve 6", "43.02 – GYK 2(b) ve 6", "43.04 – GYK 4 ve 6", "43.03 – GYK 1, 2(a) ve 6"],
   "cevap": "E", "tip": GY,
   "gerekce": "Giysi şeklinde kabaca şekil verilmiş kürk, bitmiş giysinin esas niteliğini taşıyan son şeklini almamış eşyadır; GYK 2(a) uyarınca bitmiş eşya gibi 43.03’te sınıflandırılır ve 43.02 Açıklama Notu da bunları 43.02’den hariç tutar. Henüz şekil verilmemiş, ceket yapmaya elverişli birleştirilmiş kürk parçaları ise 43.02’de kalır.",
   "dayanak": "GYK 1 ve 2(a); 43.02 Açıklama Notu, hariç tutma (a)."
  },
  {
   "soru": "Tarife Cetveline göre, kürkten yapılmış, içi doldurulmamış minder kılıfı hangi pozisyonda sınıflandırılır?",
   "secenekler": ["94.04", "43.03", "42.05", "43.02", "63.04"],
   "cevap": "B", "tip": E4,
   "gerekce": "43.03 Açıklama Notu, kürkten yapılmış veya esas karakteri kürk olan eşya arasında içi doldurulmamış minderleri sayar. Doldurulmuş olsaydı 94.04’e giderdi; deriden olsaydı 42.05’te, dokumaya elverişli maddeden olsaydı 63.04’te yer alırdı. Eşya şekli verildiğinden 43.02 söz konusu değildir.",
   "dayanak": "43.03 Açıklama Notu; 42.05 Açıklama Notu (minder yüzleri)."
  },
  {
   "soru": "Fasıl 41 Not 1(c)’ye göre boşlukları doğru tamamlayan seçenek hangisidir? “Koyun ve kuzuların yünü alınmamış ham derileri Fasıl 41’de kalır; ancak Astragan, Karakul, Persaniye, breitschwanz ve benzerleri ile ....., ....., Moğol veya Tibet kuzuları hariçtir ve bunların ham derileri ham kürk olarak 43.01’de yer alır.”",
   "secenekler": ["İran – Afgan", "Hint – Çin", "Kafkas – Kırım", "Hint – Afgan", "Çin – Kırgız"],
   "cevap": "B", "tip": ES,
   "gerekce": "Fasıl 41 Not 1(c) ve 43.01 Açıklama Notu, Astragan, Karakul, Persaniye ve benzeri kuzular ile Hint, Çin, Moğol ve Tibet kuzularının yünlü ham derilerini Fasıl 41’in dışında bırakır. Bu deriler ham kürk olarak 43.01’dedir; diğer koyun ve kuzuların yünlü ham derileri 41.02’de kalır.",
   "dayanak": "Fasıl 41 Not 1(c); Fasıl 43 Not 2(b); 43.01 Açıklama Notu."
  },
  {
   "soru": "Tarife Cetveline göre aşağıdakilerden hangisi kürk veya kürkten eşya sayılmadığından 43. Fasılda <b>yer almaz</b>?",
   "secenekler": [
    "Kürkten av torbası",
    "Taklit kürkten yelek",
    "Dabaklanmış tilki derisi",
    "Telekleri üzerinde bulunan kuş derisi",
    "Ham Persaniye kuzusu derisi"
   ],
   "cevap": "D", "tip": OT,
   "gerekce": "Fasıl 43 Not 2(a) ve Genel Açıklamalar tüylü kuş derilerini kürk saymaz; bunlar 05.05 veya 67.01’dedir. Kürkten av torbası 43.03’te, taklit kürk yelek 43.04’te, dabaklanmış tilki derisi 43.02’de, ham Persaniye kuzusu derisi 43.01’dedir.",
   "dayanak": "Fasıl 43 Not 2(a); Fasıl 43 Genel Açıklamalar."
  },
  {
   "soru": "Tarife Cetveline göre aşağıdaki eşyalardan hangileri Fasıl 43 kapsamı <b>dışındadır</b>? I. Kürk astarlı botlar; II. Kürkten oyuncak ayı; III. Kürkten başlık; IV. Kürkten manşon",
   "secenekler": ["I, II ve III", "I ve IV", "II ve IV", "I, III ve IV", "II, III ve IV"],
   "cevap": "A", "tip": CC,
   "gerekce": "Fasıl 43 Not 2; Fasıl 64 eşyasını (ayakkabılar), Fasıl 65 başlıklarını ve Fasıl 95 eşyasını (oyuncaklar) dışlar; I, II ve III bu nedenle Fasıl 43 dışındadır. Kürkten manşon giyim aksesuarı olarak 43.03’tedir.",
   "dayanak": "Fasıl 43 Not 2 (d), (e), (f); 43.03 Açıklama Notu."
  },
  {
   "soru": "Aşağıdaki eşyalardan hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır?",
   "secenekler": [
    "Vizon derilerinden dikilmiş kürk manto",
    "Tilki kürkünden yapılmış boyun atkısı",
    "İçi kürk astarlı deri ceket",
    "Kürk parçalarından yapılmış yatak örtüsü",
    "Mensucata lif yapıştırılmış taklit kürkten manto"
   ],
   "cevap": "E", "tip": FA,
   "gerekce": "Taklit kürk ve taklit kürkten eşya 43.04’tedir. Kürk manto, kürk atkı, kürk astarlı deri ceket ve kürk parçalarından yapılmış yatak örtüsü 43.03’te yer alır.",
   "dayanak": "Fasıl 43 Not 4 ve Not 5; 43.03 ve 43.04 Açıklama Notları."
  },
  {
   "soru": "Tarife Cetvelinin 43. Fasıl notlarına göre, içi kürk veya taklit kürkle kaplı ya da dışında basit süs mahiyetini aşan kürk bulunan giyim eşyası ve aksesuarları hangi pozisyonlarda yer alır?",
   "secenekler": [
    "Giysinin dış maddesine göre Fasıl 61 veya 62",
    "42.03 veya 43.02",
    "Hale göre 43.03 veya 43.04",
    "Yalnız 43.03",
    "43.02 veya 43.04"
   ],
   "cevap": "C", "tip": FN,
   "gerekce": "Fasıl 43 Not 4 uyarınca içi kürk veya taklit kürkle kaplı ya da dışında basit süsü aşan kürk veya taklit kürk bulunan giyim eşyası ve aksesuarları (Not 2 ile hariç tutulanlar dışında) hale göre 43.03 veya 43.04’tedir. Bölüm XI Not 1(k) de bu eşyayı dokumaya elverişli maddeler bölümünden çıkarır; eldivenler ise Not 2(c) gereği 42.03’te kalır.",
   "dayanak": "Fasıl 43 Not 4; Bölüm XI Not 1(k)."
  }
 ]
}

out = os.path.join(KITAP, "data", "fasil_43.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=1)
print("yazıldı:", out)
