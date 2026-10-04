# -*- coding: utf-8 -*-
"""Karma test 10 üreticisi → karma/karma_10.json"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "karma", "karma_10.json")

ESYA = "Eşya → 4’lü pozisyon"
POZESYA = "Pozisyon → eşya"
OLUMSUZ = "Olumsuz teşhis"
FARKLI = "Farklı/aynı pozisyon veya fasıl"
FASBUL = "Fasıl/Bölüm bulma"
TANIM = "Fasıl notu · Tanım/Eşik"
GYK = "Genel Yorum Kuralı"
YAPI = "Tarife yapısı"

S = []


def Q(soru, secenekler, cevap, dogru, tip, gerekce, dayanak, fasil):
    assert len(secenekler) == 5, soru
    assert len(set(secenekler)) == 5, soru
    assert secenekler["ABCDE".index(cevap)] == dogru, (soru, cevap, dogru)
    assert len(gerekce) <= 420, (len(gerekce), soru[:40])
    assert len(re.sub(r"<[^>]+>", " ", gerekce).split()) <= 45, (len(gerekce.split()), soru[:40])
    S.append({"soru": soru, "secenekler": secenekler, "cevap": cevap, "tip": tip,
              "gerekce": gerekce, "dayanak": dayanak, "fasil": fasil})


# 1 ─ Genel: tarife yapısı
Q("Tarife Cetvelinde aşağıdaki bölümlerden hangisi en fazla sayıda fasıl içerir?",
  ["Bölüm IV", "Bölüm VI", "Bölüm XI", "Bölüm XV", "Bölüm II"], "C", "Bölüm XI", YAPI,
  "XI. Bölüm, Fasıl 50 ile 63 arasındaki 14 faslı kapsar. XV. Bölüm 72–83 (saklı Fasıl 77 dahil 12), VI. Bölüm "
  "28–38 (11) fasıldan oluşur; II. ve IV. Bölümler ise dokuzar fasıl içerir.",
  "Tarife Cetveli bölüm–fasıl listesi (XI. Bölüm: Fasıl 50–63).", "Genel")

# 2 ─ Fasıl 82: fasıl bulma
Q("Krank kollu ve dişli mekanizmalı, elle çalıştırılan, ağırlığı 2 kg olan, adi metalden mutfakta kullanılan buz "
  "ufalama cihazı Tarife Cetvelinin hangi faslında yer alır?",
  ["Fasıl 82", "Fasıl 84", "Fasıl 85", "Fasıl 73", "Fasıl 83"], "A", "Fasıl 82", FASBUL,
  "Ağırlığı 10 kg’ı geçmeyen, krank veya dişli gibi bir mekanizma içeren, elle işleyen buz ufalayıcılar 82.10’da, "
  "yani Fasıl 82’dedir. 10 kg’ı aşan benzerleri 82.05 veya Fasıl 84’te kalır; makine görünümüne bakıp 84’ü seçmek tuzaktır.",
  "82.10 pozisyon metni ve Açıklama Notu.", 82)

# 3 ─ Fasıl 18: bölüm bulma
Q("Fermente edilmiş, kavrulmamış bütün kakao daneleri Tarife Cetvelinin hangi bölümünde yer alır?",
  ["Bölüm II", "Bölüm III", "Bölüm VI", "Bölüm IV", "Bölüm I"], "D", "Bölüm IV", FASBUL,
  "Kakao daneleri ham veya kavrulmuş olsun 18.01’de, yani IV. Bölümün Fasıl 18’indedir. Kahve 09.01 ile II. "
  "Bölümde yer aldığından kakaoyu da bitkisel ürünler bölümünde sanmak tipik tuzaktır.",
  "18.01 pozisyon metni; IV. Bölüm (Fasıl 16–24).", 18)

# 4 ─ Fasıl 4: olumsuz teşhis
Q("Aşağıdaki ürünlerden hangisi Tarife Cetvelinin 4. faslında <b>yer almaz</b>?",
  ["Şeker ve kakao katılmış, yoğurdun esas karakterini koruyan yoğurt",
   "Kakao ile aromalandırılmış, sütten yapılmış içime hazır meşrubat",
   "Penicillium roqueforti ile elde edilen küflü peynir",
   "Kurutulmuş, kabuksuz bıldırcın yumurtası",
   "Tuz ve gıda boyası içeren, emülsifiye edici katılmamış tereyağı"], "B",
  "Kakao ile aromalandırılmış, sütten yapılmış içime hazır meşrubat", OLUMSUZ,
  "Kakao ile aromalandırılmış sütten meşrubat 04.02 Açıklama Notu gereği 22.02’dedir. Kakaolu yoğurt Not 2 ile "
  "04.03’te kalır; küflü peynir 04.06, kabuksuz kurutulmuş yumurta 04.08, tuzlu ve boyalı tereyağı 04.05’tir.",
  "04.02 Açıklama Notu; Fasıl 4 Not 2 ve 3(a).", 4)

# 5 ─ Fasıl 89: eşya → pozisyon
Q("Tarife Cetveline göre; demiryolu vagonlarını rayları üzerinde taşıyarak bir kıyıdan diğerine geçiren, kendinden "
  "hareketli tren feribotu hangi pozisyonda sınıflandırılır?",
  ["86.06", "89.04", "89.05", "89.06", "89.01"], "E", "89.01", ESYA,
  "89.01 Açıklama Notu, araba ve tren feribotları dahil her cins feribotu yolcu ve yük gemileriyle birlikte sayar. "
  "Taşıdığı vagonlar nedeniyle Fasıl 86’yı, gemi türü nedeniyle 89.06’yı seçmek tuzaktır; 89.05 ise sabit noktada "
  "çalışan gemiler içindir.",
  "89.01 Açıklama Notu (2); 89.05 Açıklama Notu.", 89)

# 6 ─ Fasıl 24: eşya → pozisyon
Q("Tarife Cetveline göre; tütün ile gliserol karışımından oluşan, melas ve meyve aroması katılmış, nargilede "
  "içilmek üzere hazırlanmış tütün hangi pozisyonda sınıflandırılır?",
  ["24.01", "24.04", "24.03", "21.06", "24.02"], "C", "24.03", ESYA,
  "Nargile tütünü içilen tütün olarak 24.03’tedir; fasıl alt pozisyon notu da tütün-gliserol karışımı nargile "
  "tütünlerini bu pozisyon içinde tanımlar. Yanmadan solunmak üzere tasarlanmadığından 24.04’e, işlenmiş olduğundan "
  "24.01’e girmez.",
  "24.03 Açıklama Notu; Fasıl 24 alt pozisyon notu (nargile tütünleri).", 24)

# 7 ─ Fasıl 95: eşya → pozisyon
Q("Tarife Cetveline göre; evlerde kullanılmak üzere tasarlanmış, tıbbi tedavi amacı taşımayan, pedallı ve direnci "
  "ayarlanabilen sabit egzersiz (kondisyon) bisikleti hangi pozisyonda sınıflandırılır?",
  ["87.12", "90.19", "95.03", "95.06", "95.04"], "D", "95.06", ESYA,
  "Bisiklete binme egzersiz aletleri 95.06’daki kültürfizik eşyası arasında sayılır. 90.19 yalnız tıbbi kontrol "
  "altında kullanılan mekanoterapi cihazlarını kapsar ve evde kullanılan sıradan egzersiz donanımını 95.06’ya bırakır; "
  "yol bisikleti olmadığından 87.12 de değildir.",
  "95.06 Açıklama Notu (A); 90.19 Açıklama Notu.", 95)

# 8 ─ Fasıl 11: olumsuz teşhis
Q("Aşağıdakilerden hangisi Tarife Cetvelinin 11. faslında <b>sınıflandırılmaz</b>?",
  ["Kavurma ve şişirme yoluyla elde edilen kabartılmış pirinç", "Patates flokonları", "Muz unu", "İnülin",
   "Malt unu"], "A", "Kavurma ve şişirme yoluyla elde edilen kabartılmış pirinç", OLUMSUZ,
  "Kavurma ve şişirmeyle elde edilen kabartılmış pirinç, Fasıl 11 Not 1 ve Genel Açıklamalar gereği 19.04’tedir. "
  "Patates flokonu 11.05, muz unu 11.06, inülin 11.08, malt unu ise 11.07’de yer alır.",
  "Fasıl 11 Not 1(c); Fasıl 11 Genel Açıklamalar.", 11)

# 9 ─ Fasıl 42: olumsuz teşhis
Q("Aşağıdaki deriden eşyadan hangisi Tarife Cetvelinin 42. faslında <b>yer almaz</b>?",
  ["Deriden kaynakçı önlüğü", "Deriden köpek ağızlığı", "Dış yüzü deri kaplı mücevher kutusu",
   "Deriden tütün kesesi", "Deriden kasket"], "E", "Deriden kasket", OLUMSUZ,
  "Başlıklar ve aksamı Fasıl 42 Not 2 ile dışarıda bırakılıp 65. Fasla gönderilir; deriden kasket de buraya girer. "
  "Önlük Not 4 gereği 42.03’te, ağızlık 42.01’de, mücevher kutusu ve tütün kesesi 42.02’dedir.",
  "Fasıl 42 Not 2 ve Not 4; 42.01 ve 42.02 pozisyon metinleri.", 42)

# 10 ─ Fasıl 12: olumsuz teşhis
Q("Aşağıdaki ürünlerden hangisi Tarife Cetvelinin 12. faslında <b>sınıflandırılmaz</b>?",
  ["Shea fıstığı (karite fıstığı)", "Ekilmek amacıyla ithal edilen kişniş tohumu",
   "Ekilmek amacıyla ithal edilen orman ağacı tohumu", "Kurutulmuş biberiye yaprakları",
   "Taze, yenilebilir deniz yosunu"], "B", "Ekilmek amacıyla ithal edilen kişniş tohumu", OLUMSUZ,
  "Fasıl 12 Not 3’e göre 9. Fasıldaki baharat ve diğer ürünler ekilmeye mahsus olsalar da 12.09’a girmez; kişniş "
  "tohumu 09.09’da kalır. Shea fıstığı 12.07, orman ağacı tohumu 12.09, biberiye 12.11, deniz yosunu 12.12’dedir.",
  "Fasıl 12 Not 1, 3 ve 4; 09.09 pozisyon metni.", 12)

# 11 ─ Fasıl 13: eşya → pozisyon
Q("Tarife Cetveline göre; ilaç olarak hazırlanmamış, yalnızca saflaştırılmış Kanada pelesengi hangi pozisyonda "
  "sınıflandırılır?",
  ["13.01", "13.02", "33.01", "30.04", "38.06"], "A", "13.01", ESYA,
  "Pelesenkler 13.01’deki tabii sakız ve yağ reçineleri arasında sayılır; saflaştırılmaları sınıflandırmayı "
  "değiştirmez. Pelesenk içeren ilaçlar 30.03 veya 30.04’e, bunlardan çıkarılan rezinoitler 33.01’e, ısıyla işlenmiş reçineler "
  "38.06’ya gider.",
  "13.01 pozisyon metni ve Açıklama Notu.", 13)

# 12 ─ Fasıl 85: eşya → pozisyon
Q("Tarife Cetveline göre; bebek biberonlarını ısıtmaya mahsus, evlerde kullanılan türden elektrikli şişe ısıtıcısı "
  "hangi pozisyonda sınıflandırılır?",
  ["85.09", "84.19", "85.43", "85.16", "85.14"], "D", "85.16", ESYA,
  "Şişe ısıtıcıları, ev işlerinde kullanılan elektrotermik cihazlar olarak 85.16 Açıklama Notunda sayılır. 85.09 "
  "elektromekanik ev aletlerini, 84.19 evlerde kullanılmayan türden ısıtma cihazlarını kapsar; 85.43 artık "
  "pozisyondur.",
  "85.16 Açıklama Notu (E)(11).", 85)

# 13 ─ Fasıl 39: farklı pozisyon
Q("Aşağıdaki plastik eşyadan hangisi diğerlerinden farklı bir tarife pozisyonunda yer alır?",
  ["Plastikten yatak lazımlığı", "Plastikten mutfak hunisi",
   "Banyo duvarına vidayla daimi tespit edilecek plastik tuvalet kâğıdı tutacağı",
   "Plastikten ekmek kutusu",
   "Duvara tespit edilmeden lavabo kenarında kullanılan plastik sabunluk"], "C",
  "Banyo duvarına vidayla daimi tespit edilecek plastik tuvalet kâğıdı tutacağı", FARKLI,
  "Bina duvarına daimi tespit edilmek üzere hazırlanan tutacaklar Fasıl 39 Not 11 gereği inşaat malzemesi olarak "
  "39.25’tedir. Lazımlık, huni, ekmek kutusu ve duvara tespit edilmeyen sabunluk 39.24’teki ev ve tuvalet eşyasıdır.",
  "Fasıl 39 Not 11; 39.22, 39.24 ve 39.25 Açıklama Notları.", 39)

# 14 ─ Fasıl 58: farklı fasıl
Q("Aşağıdaki şeritçi ve süs eşyasından hangisi diğerlerinden farklı bir fasılda sınıflandırılır?",
  ["Ropdöşambr kuşağı yapımında kullanılan, parça halindeki milanez",
   "Yazısı dokuma yoluyla oluşturulmuş, işlemesiz, şerit halinde giysi etiketi",
   "Elastik iplik içeren, iki kenarı dokuma kenarlı, eni 2 cm olan kordela",
   "Kısa ipliklerin orta yerinden tutturulmasıyla yapılmış mobilya ponponu",
   "Dokumaya elverişli maddeyle kaplanmış, şapka çevresinde kullanılan çelik tel"], "E",
  "Dokumaya elverişli maddeyle kaplanmış, şapka çevresinde kullanılan çelik tel", FARKLI,
  "Dokumaya elverişli maddeyle kaplı şapkacı telleri 58.08 Açıklama Notu gereği 72.17’de, yani Fasıl 72’dedir. "
  "Milanez ve ponpon 58.08, işlemesiz dokuma etiket 58.07, dar kordela 58.06 ile Fasıl 58’de kalır.",
  "58.08 Açıklama Notu; 58.06 ve 58.07 Açıklama Notları; Fasıl 58 Not 5.", 58)

# 15 ─ Fasıl 97: pozisyon → eşya
Q("Aşağıdakilerin hangisinde sayılan eşyanın tümü 97.05 pozisyonunda sınıflandırılır?",
  ["Fosil numunesi – Mineral koleksiyonu için sunulan işlenmemiş zümrüt",
   "Kazıda bulunmuş yazılı kil tablet – Kurutulmuş bitki (herbaryum) koleksiyonu",
   "Koleksiyon için kutuya yerleştirilmiş böcekler – Tamamen elle yapılmış pastel resim",
   "Etnografik değeri olan törensel giysi – Kullanılmış posta pulu koleksiyonu",
   "Osteolojik iskelet numunesi – Eskiliği 150 yıl olan sarkaçlı duvar saati"], "B",
  "Kazıda bulunmuş yazılı kil tablet – Kurutulmuş bitki (herbaryum) koleksiyonu", POZESYA,
  "Arkeolojik değeri olan yazılı kil tablet ile kurutulmuş ot koleksiyonu 97.05’te sayılır. Zümrüt Fasıl 97 Not 1(c) "
  "gereği 71.03’e, pastel resim 97.01’e, kullanılmış pullar 97.04’e, 150 yıllık saat 97.06’ya gider.",
  "97.05 Açıklama Notu (A) ve (B); Fasıl 97 Not 1(c).", 97)

# 16 ─ GYK: takım kavramı
Q("Genel Yorum Kuralı 3(b) Açıklama Notuna göre aşağıdaki birlikteliklerden hangisi “perakende olarak satılacak "
  "hale getirilmiş takım” sayılır?",
  ["Aynı kutuda sunulan, aynı tipte altı adet çelik tatlı kaşığı",
   "Toptancıda yeniden paketlenip satılmak üzere aynı koliye konulmuş çay ve şeker paketleri",
   "Aynı hediye kutusunda sunulan bir şişe likör ile bir şişe şarap",
   "Pilav hazırlamada birlikte kullanılmak üzere bir kutuda son kullanıcıya sunulan pirinç, baharat ve tereyağı",
   "Aynı karton pakette sunulan bir kutu karides konservesi, bir kutu ciğer ezmesi ve bir kutu peynir"], "D",
  "Pilav hazırlamada birlikte kullanılmak üzere bir kutuda son kullanıcıya sunulan pirinç, baharat ve tereyağı", GYK,
  "Takımda farklı pozisyonlara giren en az iki eşya, belirli bir işlev için bir araya getirilme ve yeniden "
  "paketlenmeden son kullanıcıya satış birlikte aranır; pilav seti bunları taşır. Aynı tip kaşıklar, yeniden "
  "paketlenecek ürünler, içki-şarap ve konserve karışımı takım değildir.",
  "GYK 3(b) Açıklama Notu (X).", "GYK")

# 17 ─ Fasıl 63: fasıl notu / tanım
Q("Daha geniş bir parçadan başka işçilik görmeksizin yalnızca dikdörtgen şeklinde kesilmiş, kullanıldıktan sonra "
  "atılan dokunmamış mensucattan yatak çarşafları; Fasıl 63 Not 1 ve Bölüm XI Not 7’deki “hazır eşya” tanımı "
  "dikkate alındığında hangi pozisyonda sınıflandırılır?",
  ["56.03", "63.02", "63.07", "96.19", "63.04"], "A", "56.03", TANIM,
  "I. tali fasıl yalnız hazır eşyaya uygulanır; yalnızca dikdörtgen kesilmiş mensucat Bölüm XI Not 7 anlamında "
  "hazır eşya değildir. Fasıl 63 Genel Açıklamaları bu çarşafları 56.03’e gönderir; adına bakıp 63.02’yi seçmek "
  "tuzaktır.",
  "Fasıl 63 Not 1 ve Genel Açıklamalar; Bölüm XI Not 7.", 63)

# 18 ─ Fasıl 40: fasıl notu / tanım
Q("Fasıl 40 Not 4’e göre bir doymamış sentetik maddenin “sentetik kauçuk” sayılıp sayılmadığını belirlemek için "
  "yapılan vulkanizasyon ve uzama testinde, aşağıdakilerden hangisinin numuneye katılmasına <b>izin verilmez</b>?",
  ["Çapraz bağ oluşumu için gerekli vulkanizasyon hızlandırıcıları",
   "Vulkanizasyonu aktive edici maddeler",
   "Not 5(B)’de sayılan, emülsiyonu yok edici az miktardaki ürünler",
   "Not 5(B)’de sayılan, çok küçük miktardaki antioksidanlar",
   "Çapraz bağ oluşumu için gerekli olmayan doldurucu maddeler"], "E",
  "Çapraz bağ oluşumu için gerekli olmayan doldurucu maddeler", TANIM,
  "Not 4(a), testte çapraz bağ için gerekli aktive edici ve hızlandırıcılara, ayrıca Not 5(B)(ii) ve (iii)’teki "
  "maddelere izin verir. Çapraz bağ için gerekli olmayan genişletici, plastikleştirici ve doldurucular kullanılamaz.",
  "Fasıl 40 Not 4(a) ve Not 5(B).", 40)

# 19 ─ GYK: eksik eşya
Q("Elektrik motoru henüz takılmamış, bunun dışında tamamlanmış aletin asli niteliklerini taşıyan, elle kullanılan "
  "elektromekanik matkap hangi pozisyonda ve hangi Genel Yorum Kuralı uyarınca sınıflandırılır?",
  ["84.67 – GYK 2(b)", "84.67 – GYK 2(a)", "84.66 – GYK 1", "82.05 – GYK 4", "85.01 – GYK 3(b)"], "B",
  "84.67 – GYK 2(a)", GYK,
  "Bölüm XVI Genel Açıklamaları, normalde elektrik motorlu olan 84.67 aletlerinin motorsuz sunulsa da motorlu "
  "olanlarla aynı pozisyonda kalacağını belirtir; bu, eksik eşyaya ilişkin GYK 2(a)’dır. 2(b) maddelerin "
  "karışımıyla ilgilidir; aksam pozisyonları uygulanmaz.",
  "GYK 2(a); Bölüm XVI Genel Açıklamalar (IV).", "GYK")

# 20 ─ GYK: yanlış gösterilen kural
Q("Aşağıdaki sınıflandırma örneklerinden hangisinde dayanılan Genel Yorum Kuralı <b>yanlış</b> gösterilmiştir?",
  ["Tüm parçaları birlikte sunulan, yalnızca cıvatalarla monte edilecek çocuk bahçesi kaydırağı → 95.06: GYK 2(a)",
   "Kendine göre yapılmış, uzun süre kullanılabilen kutusuyla birlikte sunulan altın kolye → 71.13: GYK 5(a)",
   "Ağırlıkça eşit oranda karabiber ve kimyon tohumundan oluşan karışım → 09.10: GYK 3(c)",
   "Kendinden elektrik motorlu saç ve sakal tıraş makinesi → 85.10: GYK 3(a)",
   "Kahve yerine kullanılan kavrulmuş malt → 21.01: GYK 1"], "C",
  "Ağırlıkça eşit oranda karabiber ve kimyon tohumundan oluşan karışım → 09.10: GYK 3(c)", GYK,
  "Farklı pozisyonlara giren baharatların karışımı Fasıl 9 Not 1(b) hükmüyle 09.10’dadır; dayanak GYK 1’dir. "
  "09.10’un numara sırasında son olması 3(c)’yi gerektirmez; notta hüküm varken GYK 3 uygulanmaz.",
  "Fasıl 9 Not 1(b); GYK 1; GYK 3 Açıklama Notu (II).", "GYK")


assert len(S) == 20
from collections import Counter
cnt = Counter(q["cevap"] for q in S)
assert all(cnt[L] == 4 for L in "ABCDE"), cnt
json.dump({"tur": "karma", "no": 10, "sorular": S}, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("yazıldı:", OUT, dict(cnt))
