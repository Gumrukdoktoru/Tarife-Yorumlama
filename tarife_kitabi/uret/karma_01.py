# -*- coding: utf-8 -*-
"""Karma test 1 üreticisi → karma/karma_01.json"""
import json
import os
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "karma", "karma_01.json")

ESYA = "Eşya → 4’lü pozisyon"
POZ_ESYA = "Pozisyon → eşya"
OLUMSUZ = "Olumsuz teşhis"
FARKLI = "Farklı/aynı pozisyon veya fasıl"
BULMA = "Fasıl/Bölüm bulma"
TANIM = "Fasıl notu · Tanım/Eşik"
GYK = "Genel Yorum Kuralı"
SIRA = "Sıralama"
COKTAN = "Çoktan-çoğa / Eşleştirme"
YAPI = "Tarife yapısı"

S = []


def Q(soru, secenekler, cevap, dogru, tip, gerekce, dayanak, fasil):
    assert len(secenekler) == 5, soru
    assert secenekler["ABCDE".index(cevap)] == dogru, (soru, cevap, dogru)
    assert len(gerekce) <= 420, (len(gerekce), soru[:60])
    assert len(gerekce.split()) <= 45, (len(gerekce.split()), soru[:60])
    S.append({"soru": soru, "secenekler": secenekler, "cevap": cevap, "tip": tip,
              "gerekce": gerekce, "dayanak": dayanak, "fasil": fasil})


# 1 ─ Genel (Tarife yapısı)
Q("Tarife Cetvelinde aşağıdaki fasıllardan hangisi tali fasıllara <b>ayrılmamıştır</b>?",
  ["Fasıl 39", "Fasıl 72", "Fasıl 84", "Fasıl 63", "Fasıl 69"], "C", "Fasıl 84", YAPI,
  "Fasıl 39 (I–II), 63 (I–III), 69 (I–II) ve 72 (I–IV) tali fasıllara ayrılmıştır; Fasıl 84 ise tali fasıla "
  "bölünmeden doğrudan pozisyonlardan oluşur. GYK 1’e göre bölüm, fasıl ve tali fasıl başlıkları yalnız gösterici "
  "niteliktedir.",
  "GYK 1; Fasıl 39, 63, 69 ve 72 tali fasıl başlıkları.", "Genel")

# 2 ─ Fasıl 89 (Fasıl/Bölüm bulma)
Q("Limanlarda seyir güvenliği için kullanılan, üzerinde ışık düzeneği bulunan ışıklı işaret şamandırası Tarife "
  "Cetvelinin hangi faslında yer almaktadır?",
  ["Fasıl 94", "Fasıl 85", "Fasıl 73", "Fasıl 39", "Fasıl 89"], "E", "Fasıl 89", BULMA,
  "89.07 pozisyon metni şamandıraları ve işaret kulelerini sayar; Açıklama Notu bağlama, işaret, ışıklı ve zilli "
  "şamandıraları açıkça bu pozisyona alır. Üzerindeki ışık düzeneği veya yapıldığı madde eşyayı Fasıl 94, 85, 73 "
  "ya da 39’a götürmez.",
  "89.07 pozisyon metni ve Açıklama Notu.", 89)

# 3 ─ Fasıl 9 (Eşya → 4’lü pozisyon)
Q("Tarife Cetveline göre, Piper longum türüne ait kurutulmuş “uzun biber” meyveleri hangi tarife pozisyonunda "
  "sınıflandırılır?",
  ["09.04", "12.11", "09.10", "09.08", "07.09"], "A", "09.04", ESYA,
  "09.04 Açıklama Notu, Kübabe biberi (Piper cubeba) hariç Piper cinsinin bütün biberlerini kapsar ve uzun biberi "
  "(Piper longum) açıkça sayar. Tuzak: Fasıl 9 Not 2 yalnız Piper cubeba’yı 12.11’e gönderir; 07.09 ise taze "
  "Capsicum ve Pimenta içindir.",
  "Fasıl 9 Not 2; 09.04 Açıklama Notu.", 9)

# 4 ─ Fasıl 4 (Farklı/aynı fasıl)
Q("Aşağıdaki eşya çiftlerinden hangisinde her iki eşya da Tarife Cetvelinin <b>aynı</b> faslında sınıflandırılır?",
  ["Tabii bal – Tabii bal ile suni bal karışımı",
   "Yoğurt – Süt ürünlerinden yapılmış dondurma",
   "Kurutulmuş yumurta sarısı – Yumurta sarısı yağı",
   "Kefir – Ghee (Hint tereyağı)",
   "İnsan tüketimine uygun kurutulmuş çekirge – İnsan tüketimine uygun olmayan cansız çekirge"],
  "D", "Kefir – Ghee (Hint tereyağı)", FARKLI,
  "Kefir 04.03’te, ghee 04.05 Açıklama Notu uyarınca 04.05’te yer aldığından ikisi de Fasıl 4’tedir. Diğer "
  "çiftlerde ikinci eşya fasıl dışındadır: suni bal karışımı 17.02, dondurma 21.05, yumurta sarısı yağı 15.06, "
  "yenmeyen böcek 05.11.",
  "Fasıl 4 Not 5(a) ve Genel Açıklamalar; 04.03, 04.05, 04.08, 04.09 Açıklama Notları.", 4)

# 5 ─ Fasıl 96 (Olumsuz teşhis)
Q("Aşağıdakilerden hangisi 96.09 pozisyonunda <b>sınıflandırılmaz</b>?",
  ["Sabun taşından terzi tebeşiri",
   "Bilardo ıstakalarında kullanılan bilardo tebeşiri",
   "Kayağan taşından arduvaz kalem",
   "Seramik boyamaya mahsus kurşun boya kalemi",
   "Kömür kalem"],
  "B", "Bilardo ıstakalarında kullanılan bilardo tebeşiri", OLUMSUZ,
  "96.09 Açıklama Notu terzi tebeşirini, arduvaz kalemleri, kömür kalemleri ve seramiğe mahsus boya kalemlerini "
  "bu pozisyonda sayarken bilardo tebeşirlerini hariç tutar (95.04). Ham tebeşir 25.09’da, kaş kalemi 33.04’te "
  "kalır.",
  "96.09 Açıklama Notu; Fasıl 25 Not 2.", 96)

# 6 ─ Fasıl 40 (Eşya → 4’lü pozisyon)
Q("Tarife Cetveline göre, el arabalarında kullanılan, katı kauçuktan yapılmış ve kapalı bir iç hava boşluğuna "
  "sahip tekerlek bandajı hangi tarife pozisyonunda sınıflandırılır?",
  ["40.12", "40.11", "40.13", "40.16", "87.16"], "A", "40.12", ESYA,
  "40.12 pozisyon metni dolgu lastiklerini ve tekerlek bandajlarını açıkça sayar; Açıklama Notu bandajların el "
  "arabalarında kullanıldığını belirtir. 40.11 yeni dış lastikler, 40.13 iç lastikler içindir; Bölüm XVII Genel "
  "Açıklamaları kauçuk lastikleri taşıt aksamı (87.16) dışında bırakır.",
  "40.12 pozisyon metni ve Açıklama Notu; Bölüm XVII Genel Açıklamalar (C).", 40)

# 7 ─ Fasıl 68 (Olumsuz teşhis)
Q("Aşağıdakilerden hangisi Tarife Cetvelinin 68. faslında <b>sınıflandırılmaz</b>?",
  ["Elektrikli el taşlama makinesine takılan, aglomere silisyum karbürden bileme diski",
   "Alçıdan dökülmüş tavan rozeti",
   "Betondan prefabrik merdiven basamağı",
   "Genleştirilmiş vermikülitten ısı yalıtım levhası",
   "Dişçi tornalarına mahsus, aglomere aşındırıcıdan küçük uçlar"],
  "E", "Dişçi tornalarına mahsus, aglomere aşındırıcıdan küçük uçlar", OLUMSUZ,
  "Fasıl 68 Not 1(h), 90.18’deki dişçi tornalarına mahsus küçük uçları fasıl dışında bırakır; 68.04 Açıklama Notu "
  "da dişçi tornalarını hariç tutar. Bileme diski 68.04, alçı rozet 68.09, beton basamak 68.10, genleştirilmiş "
  "vermikülit levha 68.06’dadır.",
  "Fasıl 68 Not 1(h); 68.04, 68.09, 68.10 Açıklama Notları.", 68)

# 8 ─ Fasıl 71 (Pozisyon → eşya)
Q("Tarife Cetveline göre aşağıdakilerden hangisi 71.15 pozisyonunda sınıflandırılır?",
  ["Platinden yapılmış ekstrüzyon (çekme) memesi",
   "Gümüşten masa şamdanı",
   "Laboratuvarda kullanılan platinden pota",
   "Köpük platinden yapılmış gazlı çakmak",
   "Altından kol düğmesi"],
  "C", "Laboratuvarda kullanılan platinden pota", POZ_ESYA,
  "71.15 Açıklama Notu, teknik işlerde veya laboratuvarlarda kullanılan platinden potaları bu pozisyonda sayar. "
  "Ekstrüzyon memesi Bölüm XVI’ya, gazlı çakmak Fasıl 96’ya gider; şamdan kuyumcu eşyası (71.14), kol düğmesi "
  "mücevherci eşyasıdır (71.13).",
  "71.15 Açıklama Notu; Fasıl 71 Not 9 ve 10.", 71)

# 9 ─ Fasıl 19 (Olumsuz teşhis)
Q("Aşağıdakilerden hangisi 19.02 pozisyonunda <b>sınıflandırılmaz</b>?",
  ["Kıymalı dolgusu ürün ağırlığının %35’ini oluşturan, uçları açık doldurulmuş makarna (cannelloni)",
   "Ağırlıkça %35 kıyma içeren, kıymalı sosla karıştırılmış hazır spagetti yemeği",
   "Kurutulmamış (taze) yumurtalı erişte",
   "İrmiğin ısıl işleme tabi tutulmasıyla elde edilen kuskus",
   "Taze gnocchi"],
  "B", "Ağırlıkça %35 kıyma içeren, kıymalı sosla karıştırılmış hazır spagetti yemeği", OLUMSUZ,
  "Fasıl 19 Not 1(a) ve 19.02 Açıklama Notu, doldurulmuş makarna hariç ağırlıkça %20’den fazla et içeren "
  "müstahzarları Fasıl 16’ya gönderir. Doldurulmuş cannelloni et oranına bakılmaksızın 19.02’de kalır; tuzak, %20 "
  "eşiğinin doldurulmuş makarnaya uygulanmamasıdır.",
  "Fasıl 19 Not 1(a); 19.02 Açıklama Notu.", 19)

# 10 ─ Fasıl 84 (Sıralama)
Q("Aşağıdaki eşyanın Tarife Cetvelindeki pozisyon numaralarına göre küçükten büyüğe doğru dizilişi hangi "
  "seçenekte doğru verilmiştir?<br/>I. Yürüyen merdiven<br/>II. Merkezi ısıtma (kalorifer) kazanı<br/>"
  "III. Para bozma makinası<br/>IV. Ev tipi bulaşık yıkama makinası<br/>V. Ot ve saman balyalama makinası",
  ["IV – II – I – V – III", "II – IV – V – I – III", "II – I – IV – V – III", "II – IV – I – V – III",
   "II – IV – I – III – V"], "D", "II – IV – I – V – III", SIRA,
  "Kalorifer kazanı 84.03, ev tipi bulaşık makinası 84.22, yürüyen merdiven 84.28, balyalama makinası 84.33, "
  "para bozma makinası 84.76’dadır. Para bozma makinalarının otomatik satış makinalarıyla birlikte 84.76’da yer "
  "alması tuzaktır.",
  "84.03, 84.22, 84.28, 84.33 ve 84.76 pozisyon metinleri.", 84)

# 11 ─ GYK (3(b) – bileşik eşya, esas karakter)
Q("Bütün dış yüzeyi işlenmiş bağa (kaplumbağa kabuğu) levhalarıyla kaplanmış ve tamamlanmış eşyaya esas "
  "karakterini bu kaplamanın verdiği ağaçtan puro kutusu hangi tarife pozisyonunda ve hangi Genel Yorum Kuralına "
  "göre sınıflandırılır?",
  ["44.20 – GYK 1", "96.01 – GYK 3(b)", "96.01 – GYK 3(c)", "44.20 – GYK 3(a)", "42.02 – GYK 3(b)"],
  "B", "96.01 – GYK 3(b)", GYK,
  "Ağaç (44.20) ve bağa (96.01) pozisyonları bileşik eşyanın maddelerinden yalnız birine atıfta bulunduğundan "
  "3(a) sonuç vermez. 96.01 Açıklama Notu, kaplamanın esas karakteri oluşturduğu ahşap kutuları 96.01’e alır; bu, "
  "esas niteliğe göre sınıflandırma (3(b)) uygulamasıdır.",
  "GYK 3(a) ve 3(b) Açıklama Notu; 96.01 Açıklama Notu.", "GYK")

# 12 ─ Fasıl 39 (Eşya → 4’lü pozisyon)
Q("Tarife Cetveline göre, sertleştirilmiş proteinden yapılmış, yassılaştırılmış düz boru şeklinde sunulan sucuk "
  "ve salam kılıfları (suni bağırsaklar) hangi tarife pozisyonunda sınıflandırılır?",
  ["39.13", "05.04", "39.23", "42.06", "39.17"], "E", "39.17", ESYA,
  "Fasıl 39 Not 8, 39.17 anlamında boru ve hortum tabirine sucuk ve salam kılıflarını ve diğer yassılaştırılmış "
  "düz boruları dahil eder. Sertleştirilmiş protein 39.13’te yalnız ilk şekillerde kalır; tabii bağırsak 05.04, "
  "yarılmış tabii bağırsaktan suni bağırsak 42.06’dadır.",
  "Fasıl 39 Not 8; 39.17 ve 05.04 Açıklama Notları.", 39)

# 13 ─ Fasıl 73 (Farklı/aynı pozisyon)
Q("Aşağıdaki seçeneklerin hangisinde aynı 4’lü pozisyonda <b>yer almayan</b> eşya bulunmaktadır?",
  ["Ayakkabı tabanlarına çakılan koruyucu demir – Marangoz tel çivisi",
   "Çelik toron (demetlenmiş tel) – Elektrik için izole edilmemiş çelik halat",
   "Oksijen tüpü – Sıvılaştırılmış bütan gazı tüpü",
   "Gemi çapası – Dört tırnaklı filika demiri",
   "Taşıt süspansiyonu için yaprak yay – Helezoni kompresyon yayı"],
  "A", "Ayakkabı tabanlarına çakılan koruyucu demir – Marangoz tel çivisi", FARKLI,
  "73.17 Açıklama Notu, ayakkabı tabanlarına çakılan koruyucu demirleri hariç tutar; bunlar 73.26’da, tel çiviler "
  "73.17’dedir. Toron ve halat 73.12, gaz tüpleri 73.11, çapa ve filika demiri 73.16, yaprak ve helezoni yaylar "
  "73.20’de birlikte yer alır.",
  "73.17, 73.26, 73.12, 73.11, 73.16 ve 73.20 Açıklama Notları.", 73)

# 14 ─ Fasıl 88 (Olumsuz teşhis)
Q("Aşağıdakilerden hangisi 88.05 pozisyonunda <b>sınıflandırılmaz</b>?",
  ["Gemilerin bordasında kullanılan, uçağın kalkış hareketini sağlayan metal fırlatma rampası",
   "Pilotları eğitmeye mahsus hava muharebe simülatörü",
   "Roket fırlatma rampası ve havalanma süresince rehberlik eden roket kulesi",
   "Hava alanlarında iniş yapan uçağın durma mesafesini kısaltan durdurma tertibatı",
   "Mesnet üzerinde dönebilen, pilot kabini olarak teçhiz edilmiş “link trainer”"],
  "C", "Roket fırlatma rampası ve havalanma süresince rehberlik eden roket kulesi", OLUMSUZ,
  "88.05 Açıklama Notu, roket fırlatma rampalarını ve havalanma süresince rehberlik eden roket kulelerini hariç "
  "tutarak 84.79’a gönderir. Uçak fırlatma rampası, iniş durdurma tertibatı, hava muharebe simülatörü ve link "
  "trainer 88.05’in üç grubundadır.",
  "88.05 Açıklama Notu (A), (B), (C).", 88)

# 15 ─ Fasıl 25 (Eşya → 4’lü pozisyon)
Q("Tarife Cetveline göre, saf çöktürülmüş magnezyum hidroksitin 600–900 °C’de kalsine edilmesiyle elde edilen ve "
  "ilaç ile kozmetik sanayiinde kullanılan hafif magnezyum oksit hangi tarife pozisyonunda sınıflandırılır?",
  ["28.16", "28.25", "25.30", "25.19", "28.36"], "D", "25.19", ESYA,
  "25.19 pozisyon metni saf olsun olmasın magnezyum oksidi kapsar; Açıklama Notu hafif ve ağır magnezyum "
  "oksitleri sayar. Fasıl 28 Not 3(a) magnezyum oksidi kimyaca saf olsa da Fasıl 28 dışında bırakır; 28.16 "
  "yalnız magnezyum hidroksit ve peroksidi kapsar.",
  "25.19 pozisyon metni ve Açıklama Notu; Fasıl 28 Not 3(a).", 25)

# 16 ─ Fasıl 55 (Çoktan-çoğa)
Q("Aşağıdakilerden hangileri Tarife Cetvelinin 55. faslı <b>dışında</b> sınıflandırılır?<br/>I. Cam lifleri<br/>"
  "II. Karbon lifleri<br/>III. Viskoz liflerinden vatka<br/>IV. Akrilik paçavraların ditilmesiyle elde edilmiş, "
  "karde edilmemiş döküntü lifleri",
  ["I ve II", "I, II ve III", "II ve IV", "I, III ve IV", "III ve IV"], "B", "I, II ve III", COKTAN,
  "Fasıl 55 Genel Açıklamaları cam liflerini (70.19) ve karbon liflerini (68.15) fasıl dışında bırakır; 55.05 "
  "Açıklama Notu vatkaları 30.05 veya 56.01’e gönderir. Ditme döküntüleri ise karde edilmemişse 55.05’te kalır.",
  "Fasıl 55 Genel Açıklamalar; 55.05 Açıklama Notu.", 55)

# 17 ─ GYK (1 – pozisyonun kapsadığı takım)
Q("Perakende satış için karton bir kutuda sunulan; tüpler içinde ressam yağlı boyaları, iki adet fırça, bir palet "
  "ve bir palet spatülünden oluşan resim takımı hangi tarife pozisyonunda ve hangi Genel Yorum Kuralına göre "
  "sınıflandırılır?",
  ["32.13 – GYK 1", "96.03 – GYK 3(c)", "32.13 – GYK 2(b)",
   "Takım sayılmaz; her eşya kendi pozisyonunda ayrı ayrı – GYK 1", "96.03 – GYK 3(b)"],
  "A", "32.13 – GYK 1", GYK,
  "32.13 Açıklama Notu, resim boyalarının fırça, palet, palet spatülü gibi teferruatlı takımlarını da bu pozisyona "
  "dahil eder; sınıflandırma GYK 1 ile yapılır. Takım (3(b)) veya numara sırası (3(c)) kurallarına başvurulmaz; "
  "2(b) madde karışımlarına ilişkindir.",
  "GYK 1; 32.13 pozisyon metni ve Açıklama Notu.", "GYK")

# 18 ─ Fasıl 72 (Eşya → 4’lü pozisyon)
Q("Tarife Cetveline göre, Fasıl 72 Not 1(p)’deki tanıma uyan, alaşımsız çelikten, dış kesitinin en geniş boyutu "
  "32 mm olan ve maden aramalarında kullanılan altıgen kesitli içi boş sondaj çubuğu hangi tarife pozisyonunda "
  "sınıflandırılır?",
  ["72.15", "73.04", "82.07", "72.14", "72.28"], "E", "72.28", ESYA,
  "72.28 pozisyon metni, diğer alaşımlı çelik çubuklarla birlikte alaşımlı veya alaşımsız çelikten sondaj için "
  "içi boş çubukları da kapsar. Tuzak, alaşımsız diye 72.14 veya 72.15’i seçmektir; tanıma uymayan içi boş "
  "çubuklar 73.04’e, sondaj matkabı uçları 82.07’ye gider.",
  "Fasıl 72 Not 1(p); 72.28 pozisyon metni ve Açıklama Notu.", 72)

# 19 ─ Fasıl 85 (Fasıl notu · Tanım)
Q("Tarife Cetvelinin 85. Fasıl Not 12’sine göre, “yarı iletken tabanlı dönüştürücüler” olarak tanımlanan ayrık "
  "yarı iletken türleri arasında aşağıdakilerden hangisi <b>yer almaz</b>?",
  ["Yarı iletken tabanlı sensörler", "Yarı iletken tabanlı aktüatörler",
   "Yarı iletken tabanlı yükselteçler (amplifikatörler)", "Yarı iletken tabanlı rezonatörler",
   "Yarı iletken tabanlı osilatörler"],
  "C", "Yarı iletken tabanlı yükselteçler (amplifikatörler)", TANIM,
  "Fasıl 85 Not 12, fiziksel veya kimyasal olayı elektrik sinyaline ya da elektrik sinyalini fiziksel olaya "
  "dönüştüren yarı iletken tabanlı dönüştürücüleri sensörler, aktüatörler, rezonatörler ve osilatörler olarak "
  "sayar; yükselteç bu sayımda yoktur.",
  "Fasıl 85 Not 12(i).", 85)

# 20 ─ GYK (3(c) – çok işlevli tezgâh)
Q("Otomatik takım değiştirme tertibatı bulunmayan; metalleri talaş kaldırarak delen ve ayrıca taşlama yoluyla "
  "tamamlayabilen, esas fonksiyonu belirlenemeyen takım tezgâhı hangi tarife pozisyonunda ve hangi Genel Yorum "
  "Kuralına göre sınıflandırılır?",
  ["84.59 – GYK 1 ve 3(c)", "84.57 – GYK 1 ve 3(a)", "84.60 – GYK 1 ve 3(b)", "84.60 – GYK 1 ve 3(c)",
   "84.59 – GYK 1 ve 4"], "D", "84.60 – GYK 1 ve 3(c)", GYK,
  "Bölüm XVI Not 3 ve Genel Açıklamalarına göre esas fonksiyonu belirlenemeyen çok işlevli makinada GYK 3(c) "
  "uygulanır; delme 84.59’a, taşlama 84.60’a girdiğinden numara sırasında sonuncusu olan 84.60 seçilir. Otomatik "
  "takım değiştirme olmadığından 84.57 uygulanmaz.",
  "Bölüm XVI Not 3 ve Genel Açıklamalar; 84.57 Açıklama Notu; GYK 3(c).", "GYK")


assert len(S) == 20
cnt = Counter(q["cevap"] for q in S)
assert all(cnt[L] == 4 for L in "ABCDE"), cnt

with open(OUT, "w", encoding="utf-8") as f:
    json.dump({"tur": "karma", "no": 1, "sorular": S}, f, ensure_ascii=False, indent=1)
print("yazıldı:", OUT, dict(cnt))
