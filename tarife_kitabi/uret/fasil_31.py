#!/usr/bin/env python3
"""Fasıl 31 (Gübreler) modülünü üretir."""
import json
import os
from collections import Counter

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CIKTI = os.path.join(KITAP, "data", "fasil_31.json")

T_ESYA = "Eşya → 4’lü pozisyon"
T_OLUMSUZ = "Olumsuz teşhis"
T_FARKLI = "Farklı/aynı pozisyon veya fasıl"
T_NOT = "Fasıl notu · Tanım/Eşik"
T_GYK = "Genel Yorum Kuralı"
T_ESL = "Eşleştirme / Boşluk doldurma"
T_COK = "Çoktan-çoğa (I–IV)"
T_SEN = "Senaryo"


def Q(tip, soru, dogru, yanlislar, harf, gerekce, dayanak):
    assert len(yanlislar) == 4, soru
    i = "ABCDE".index(harf)
    secenekler = list(yanlislar)
    secenekler.insert(i, dogru)
    return {"soru": soru, "secenekler": secenekler, "cevap": harf, "tip": tip,
            "gerekce": gerekce, "dayanak": dayanak}


sorular = [
    # 1
    Q(T_ESYA,
      "Brüt ağırlığı 50 kg olan çuvallarda, hayvan yemine katılmak üzere ithal edilen üre Tarife Cetvelinde hangi pozisyonda sınıflandırılır?",
      "31.02", ["23.09", "29.24", "31.05", "38.24"], "C",
      "Üre, Fasıl 31 Not 2(a)’daki sınırlı listede sayılmıştır ve açıklama notuna göre bu listedeki ürünler gübre olarak kullanılmayacakları açıkça belli olsa bile 31.02’de sınıflandırılır. Ambalaj brüt 10 kg’ı geçtiği için 31.05’e gitmez; yem amacı ürünü 23.09’a taşımaz.",
      "Fasıl 31 Not 2(a); 31.02 Açıklama Notu."),
    # 2
    Q(T_ESYA,
      "Bahçe kullanımı için brüt ağırlığı 5 kg olan torbalarda perakende satılan amonyum sülfat hangi pozisyonda yer alır?",
      "31.05", ["31.02", "28.33", "31.04", "38.24"], "A",
      "31.05 pozisyon metni, bu fasıldaki ürünlerin tablet veya benzeri şekillerde ya da brüt ağırlığı 10 kg’ı geçmeyen ambalajlarda olanlarını kapsar. Amonyum sülfat dökme veya büyük ambalajda 31.02’de olurdu; 31.02 notu da “31.05’te belirtilen şekillerde olmamak” şartını taşır.",
      "31.05 pozisyon metni; Fasıl 31 Not 2."),
    # 3
    Q(T_ESYA,
      "Kuru susuz ürün üzerinden hesaplandığında ağırlıkça %0,1 flor içeren kalsiyum hidrojenortofosfat (dökme) hangi pozisyonda sınıflandırılır?",
      "28.35", ["31.03", "31.05", "25.10", "23.09"], "D",
      "Fasıl 31 Not 3(a)(iv) yalnız kuru susuz ürün üzerinden ağırlıkça %0,2 veya daha fazla flor içeren kalsiyum hidrojenortofosfatları 31.03’e alır. Açıklama notuna göre %0,2’den az flor içerenler 28.35’tedir. Eşik altında kalan ürün gübre olarak kullanılsa da 31.03’e giremez.",
      "Fasıl 31 Not 3; 31.03 Açıklama Notu."),
    # 4
    Q(T_ESYA,
      "Deniz kuşlarının gübre ve artıklarının birikiminden oluşan guano, brüt ağırlığı 25 kg olan torbalarda sunulmuştur. Eşya hangi pozisyonda yer alır?",
      "31.01", ["05.11", "31.05", "25.30", "31.03"], "B",
      "Guano, 31.01 açıklama notunda hayvansal veya bitkisel gübre olarak ismen sayılmıştır. Ambalajın brüt ağırlığı 10 kg’ı geçtiği için 31.05’in küçük ambalaj kuralı uygulanmaz; kimyasal gübreyle karışık olmadığı için de 31.05’e gitmez.",
      "31.01 Açıklama Notu; 31.05 pozisyon metni."),
    # 5
    Q(T_ESYA,
      "Bazik sıvalı fırınlarda veya konvertörlerde fosforlu demirden çelik imali sırasında yan ürün olarak elde edilen defosforasyon cürufu (Thomas cürufu) hangi pozisyonda sınıflandırılır?",
      "31.03", ["26.19", "31.05", "26.21", "25.10"], "E",
      "Fasıl 31 Not 3(a)(i) bazik cürufu 31.03’te sayar; açıklama notu bunu “Thomas fosfatları” veya defosforasyon cürufu olarak tanımlar. Fasıl 26 Not 1 de 31. Fasılda yer alan bazik cürufu cüruf pozisyonlarının dışında bırakır; bu yüzden 26.19 ve 26.21 çeldiricidir.",
      "Fasıl 31 Not 3(a); 31.03 Açıklama Notu; Fasıl 26 Not 1."),
    # 6 — Olumsuz
    Q(T_OLUMSUZ,
      "Aşağıdakilerden hangisi Tarife Cetvelinin 31. faslında <b>sınıflandırılmaz</b>?",
      "Potasyum nitrat",
      ["Kalsiyum siyanamit", "Karnalit", "Süperfosfat", "Diamonyum fosfat"], "D",
      "31.05 açıklama notu, Not 2–5’te tanımlanmayan kimyasal olarak belirli bileşiklerin (potasyum nitrat 28.34, potasyum fosfat 28.35) gübre olarak kullanılsalar bile fasıl dışında kaldığını belirtir. Kalsiyum siyanamit Not 2’de, karnalit Not 4’te, süperfosfat Not 3’te, diamonyum fosfat Not 5’te sayılmıştır.",
      "Fasıl 31 Not 1(b), Not 2–5; 31.05 Açıklama Notu."),
    # 7
    Q(T_OLUMSUZ,
      "Aşağıdakilerden hangisi 31.02 pozisyonunda <b>yer almaz</b>?",
      "Saf amonyum klorür",
      ["Sodyum nitrat (saf olsun olmasın)",
       "Amonyum nitratın sulu çözeltisi şeklindeki sıvı gübre",
       "Kalsiyum nitrat ve amonyum nitratın çift tuzları",
       "Amonyum nitratın tebeşirle karışımından oluşan gübre"], "B",
      "Amonyum klorür Not 2(a) listesinde yoktur; tek başına kimyasal olarak belirli bileşik olarak 28.27’dedir. Buna karşılık amonyum klorürün tebeşir, alçı taşı gibi besin maddesi olmayan inorganik maddelerle karışımı Not 2(c) ile 31.02’ye girer. Sodyum nitrat ve çift tuzlar Not 2(a), sıvı amonyum nitrat çözeltisi Not 2(d) kapsamındadır.",
      "Fasıl 31 Not 2; 31.02 Açıklama Notu."),
    # 8
    Q(T_OLUMSUZ,
      "Aşağıdakilerden hangisi 31. fasılda <b>sınıflandırılmaz</b>?",
      "Az miktarda doğal azot ve fosfor içeren bitkisel toprak",
      ["Potasyum klorürün kükürtle karışımından oluşan gübre",
       "Kurutulmuş kan ve kemik unu karışımından oluşan gübre",
       "Gübre olarak kullanılmaya elverişli stabilize kanalizasyon çamuru",
       "Tablet şeklinde hazırlanmış potasyum sülfat"], "A",
      "Fasıl 31 genel açıklamaları, toprağı verimli kılmaktan çok ıslah eden maddeleri (kireç 25.22, kireçli ve bitkisel toprak 25.30, turb 27.03) yapısında az miktarda gübre unsuru bulunsa bile fasıl dışında bırakır. Kan-kemik unu karışımı ve stabilize çamur 31.01’de, tablet halindeki potasyum sülfat ile potasyum klorür-kükürt karışımı 31.05’tedir.",
      "Fasıl 31 Genel Açıklamalar; 31.01 ve 31.05 Açıklama Notları."),
    # 9
    Q(T_OLUMSUZ,
      "Aşağıdakilerden hangisi 31.04 pozisyonunda <b>sınıflandırılmaz</b>?",
      "Her biri 2,5 g veya daha ağır kültür potasyum klorür kristalleri",
      ["Gübre olarak kullanılan, dökme halde ham kainit",
       "Magnezyum potasyum sülfat (saf olsun olmasın)",
       "Potasyum klorür ile potasyum sülfat karışımından oluşan gübre",
       "Ham tabii potasyum tuzu olan silvit (dökme halde)"], "E",
      "Fasıl 31 Not 1(c), her birinin ağırlığı 2,5 g veya daha fazla olan potasyum klorür kristallerini (optik elemanlar hariç) 38.24’e, optik elemanları 90.01’e gönderir. Kainit ve silvit ham tabii potasyum tuzu, magnezyum potasyum sülfat ise Not 4(a)’da sayılmıştır; bunların birbiriyle karışımları Not 4(b) ile 31.04’tedir.",
      "Fasıl 31 Not 1(c) ve Not 4."),
    # 10 — Farklı / aynı
    Q(T_FARKLI,
      "Aşağıdaki gübrelerden hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır?",
      "Süperfosfatların dolomit ile karışımından oluşan gübre",
      ["Süperfosfatların potasyum sülfatla karışımından oluşan gübre",
       "Amonyum nitrat, süperfosfat ve potasyum klorür karışımı",
       "Diamonyum hidrojenortofosfat",
       "Monoamonyum fosfat"], "C",
      "Süperfosfatların dolomit gibi besin maddesi olmayan inorganik maddelerle karışımı Not 3(c) ile 31.03’te kalır; açıklama notu bu örneği ismen verir. Diğer karışımlar iki veya üç besin maddesini (N, P, K) birlikte içerdiğinden, MAP ve DAP ise Not 5 gereği 31.05’tedir.",
      "Fasıl 31 Not 3(c) ve Not 5; 31.03 ve 31.05 Açıklama Notları."),
    # 11
    Q(T_FARKLI,
      "Aşağıdakilerden hangisi diğerlerinden farklı bir fasılda yer alır?",
      "Potasyum karbonat",
      ["Üre", "Amonyum sülfat", "Potasyum sülfat", "Monoamonyum fosfat"], "A",
      "31.04 açıklama notu, listede tanımlanmayan potaslı ürünlerin (ör. potasyum karbonat, 28.36) gübre olarak kullanılsalar dahi bu pozisyona girmediğini belirtir. Üre ve amonyum sülfat 31.02, potasyum sülfat 31.04, monoamonyum fosfat 31.05’tedir; hepsi Fasıl 31’dir.",
      "Fasıl 31 Not 1(b) ve Not 2, 4, 5; 31.04 Açıklama Notu."),
    # 12
    Q(T_FARKLI,
      "Aşağıdaki eşya çiftlerinden hangisinde her iki eşya da aynı tarife pozisyonunda yer alır?",
      "Amonyum sülfat – Amonyum sülfat ve amonyum nitratın çift tuzları",
      ["Guano – Guanonun kimyasal gübrelerle karışımı",
       "Kalsiyum siyanamit – Kalsiyum siyanamidin defosforasyon cürufu ile karışımı",
       "Potasyum klorür – Potasyum nitrat",
       "Süperfosfat – Kalsine edilmemiş ham tabii kalsiyum fosfat"], "E",
      "Amonyum sülfat ve amonyum sülfat-amonyum nitrat çift tuzları Not 2(a)’da birlikte sayıldığından ikisi de 31.02’dedir. Guano 31.01, kimyasal gübreyle karışımı 31.05; kalsiyum siyanamit 31.02, cürufla karışımı (N + P) 31.05; potasyum klorür 31.04, potasyum nitrat 28.34; süperfosfat 31.03, ham tabii fosfat 25.10’dur.",
      "Fasıl 31 Not 2, 3, 4; 31.01 ve 31.05 Açıklama Notları."),
    # 13
    Q(T_FARKLI,
      "Aşağıdakilerden hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır?",
      "Brüt ağırlığı 40 kg olan torbalarda amonyum nitrat",
      ["Brüt ağırlığı 8 kg olan torbalarda guano",
       "Brüt ağırlığı 8 kg olan torbalarda süperfosfat",
       "Tablet halinde hazırlanmış üre",
       "Dökme halde monoamonyum fosfat"], "B",
      "Brüt 40 kg’lık torbadaki amonyum nitrat 10 kg sınırını aştığından Not 2 listesine göre 31.02’de kalır. Brüt 10 kg’ı geçmeyen ambalajdaki guano ve süperfosfat ile tablet halindeki üre 31.05 metni gereği, monoamonyum fosfat ise Not 5 gereği 31.05’tedir.",
      "31.05 pozisyon metni; Fasıl 31 Not 2 ve Not 5."),
    # 14 — Not / eşik
    Q(T_NOT,
      "31.05 pozisyon metnine göre, bu fasıldaki ürünlerin hangi ambalajlarda bulunanları 31.05’te sınıflandırılır?",
      "Brüt ağırlığı 10 kg’ı geçmeyen ambalajlar",
      ["Net ağırlığı 10 kg’ı geçmeyen ambalajlar",
       "Brüt ağırlığı 25 kg’ı geçmeyen ambalajlar",
       "Net ağırlığı 50 kg’ı geçmeyen ambalajlar",
       "Brüt ağırlığı 5 kg’ı geçmeyen ambalajlar"], "D",
      "31.05 metni “tablet veya benzeri şekillerde veya brüt ağırlığı 10 kg’ı geçmeyen ambalajlarda” olan ürünleri kapsar. Ölçüt net değil brüt ağırlıktır; tuzak, net ağırlık ifadesini doğru sanmaktır. Bu kural 31.01’deki tabii gübreler dahil fasıldaki tüm ürünlere uygulanır.",
      "31.05 pozisyon metni ve Açıklama Notu."),
    # 15
    Q(T_NOT,
      "Fasıl 31 Not 3’e göre kalsiyum hidrojenortofosfatın 31.03’te sınıflandırılabilmesi için ne kadar flor içermesi gerekir?",
      "Kuru susuz ürün üzerinden ağırlıkça %0,2 veya daha fazla",
      ["Kuru susuz ürün üzerinden ağırlıkça %2 veya daha fazla",
       "Kuru susuz ürün üzerinden ağırlıkça %0,2’den az",
       "Ağırlıkça %35 veya daha fazla",
       "Flor oranı aranmaksızın herhangi bir oranda"], "C",
      "Not 3(a)(iv), kuru anhidrit ürün üzerinden hesaplandığında ağırlıkça %0,2 veya daha fazla flor içeren kalsiyum hidrojenortofosfatları 31.03’e alır; daha az flor içerenler 28.35’tedir. Flor limiti yalnız bu ürünün tek başına sunulduğu hal için aranır; Not 3(b) ve (c) karışımlarında dikkate alınmaz.",
      "Fasıl 31 Not 3; 31.03 Açıklama Notu."),
    # 16
    Q(T_NOT,
      "Fasıl 31 Not 6’ya göre 31.05 pozisyonu anlamında “diğer gübreler” tabiri için aşağıdakilerden hangisi <b>doğrudur</b>?",
      "Sadece gübre olarak kullanılan ve en az bir ana bitki besin maddesi içeren ürünler",
      ["Azot, fosfor ve potasyumun üçünü birden ana unsur olarak içeren ürünler",
       "Gübre olarak da kullanılabilen her türlü kimyasal olarak belirli bileşik",
       "Tohumun filizlenmesine yardım eden ve az miktarda besin içeren mikrobesin müstahzarları",
       "Toprağı ıslah eden ve az miktarda besin içeren kireçli topraklar"], "A",
      "Not 6, “diğer gübreler”i yalnız gübre olarak kullanılan ve azot, fosfor, potasyum gibi bitki besin maddelerinden en az birini ana unsur olarak içeren ürünlerle sınırlar. Üç besin birden şart değildir. Mikrobesin müstahzarları 38.24, kireçli topraklar 25.30’dadır; listede olmayan belirli kimyasal bileşikler Fasıl 28–29’da kalır.",
      "Fasıl 31 Not 6; Genel Açıklamalar."),
    # 17
    Q(T_NOT,
      "Fasıl 31 notlarına göre potasyum klorür ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
      "2,5 g veya daha ağır kültür kristalleri 38.24’te, optik elemanları 90.01’dedir.",
      ["Saf potasyum klorür kimyasal olarak belirli olduğundan her durumda 28.27’dedir.",
       "Potasyum klorür yalnız gübre olarak kullanılacağı belli ise 31.04’tedir.",
       "Her biri 2,5 g’ı geçmeyen kristaller optik eleman sayılır ve 90.01’dedir.",
       "Potasyum klorürün potasyum sülfatla karışımı gübre olarak 31.05’tedir."], "E",
      "Not 1(c) iki istisna koyar: 2,5 g veya daha ağır kültür kristalleri (optik elemanlar hariç) 38.24, optik elemanlar 90.01. Bunun dışında potasyum klorür saf olsun olmasın Not 4(a) ile 31.04’tedir ve listedeki ürünler kullanım amacına bakılmaksızın burada kalır. Potasyum sülfatla karışımı da Not 4(b) ile 31.04’tedir.",
      "Fasıl 31 Not 1(c) ve Not 4; 31.04 Açıklama Notu."),
    # 18 — GYK
    Q(T_GYK,
      "Saf amonyum nitrat, gübre olarak değil başka bir amaçla kullanılacağı açıkça belli olsa bile 31.02’de sınıflandırılır. Bu sınıflandırma hangi kurala dayanır?",
      "GYK 1 ve 6 (pozisyon metni ve Fasıl 31 Not 2)",
      ["GYK 3(a) ve 6 (en özel tanım)",
       "GYK 3(c) ve 6 (numara sırasına göre en son pozisyon)",
       "GYK 4 ve 6 (en çok benzeyen eşya)",
       "GYK 2(b) ve 6 (karışım ve bileşimler)"], "B",
      "Amonyum nitrat Fasıl 31 Not 2(a)’da “saf olsun olmasın” ibaresiyle ismen sayılmıştır; açıklama notu listedeki ürünlerin gübre olarak kullanılmayacakları belli olsa da burada sınıflandırılacağını söyler. Sınıflandırma doğrudan pozisyon metni ve fasıl notuyla, yani GYK 1 ile yapılır; başka kurala geçilmez.",
      "GYK 1; Fasıl 31 Not 2(a); 31.02 Açıklama Notu."),
    # 19
    Q(T_GYK,
      "Genel Yorum Kuralı 1’in açıklama notuna göre, Fasıl 31 notlarının bazı pozisyonların yalnızca belirli eşyayı kapsadığını hükme bağlaması hangi kuralın bu pozisyonlarda uygulanmasını önlemektedir?",
      "GYK 2(b)",
      ["GYK 3(b)", "GYK 5(b)", "GYK 4", "GYK 3(c)"], "D",
      "GYK 1 açıklama notu, “pozisyon ve notlarda aksine bir hüküm bulunmadıkça” ifadesini 31. Faslın notlarıyla örnekler: bu notlar bazı pozisyonların belli eşyayı kapsadığını hükme bağladığından, 2(b) kuralıyla (başka maddelerle karışım veya bileşim) bu pozisyonlara girebilecek eşyanın kapsama alınması önlenir. Bu nedenle 31.02–31.04’e yalnız notlarda sayılan karışımlar girebilir.",
      "GYK 1 Açıklama Notu (III)(b); Fasıl 31 Not 2–4."),
    # 20 — Eşleştirme / boşluk
    Q(T_ESL,
      "31.03 Açıklama Notuna göre tek süperfosfat, tabii fosfat veya kemik tozu üzerine ……… etkisiyle; çift ve üçlü süperfosfatlar ise aynı maddeler üzerine ……… etkisiyle elde edilir. Boşluklara sırasıyla hangisi gelmelidir?",
      "sülfürik asidin – fosforik asidin",
      ["fosforik asidin – sülfürik asidin",
       "nitrik asidin – fosforik asidin",
       "sülfürik asidin – nitrik asidin",
       "hidroklorik asidin – sülfürik asidin"], "C",
      "Açıklama notu, tek süperfosfatın tabii fosfat veya kemik tozu üzerine sülfürik asidin, çift ve üçlü süperfosfatların ise fosforik asidin etkisiyle elde edildiğini belirtir. Nitrik asit, 31.05 açıklama notundaki kompleks gübre üretim örneğinde geçer; çeldirici bu karışıklığa dayanır.",
      "31.03 Açıklama Notu (A)(1)."),
    # 21
    Q(T_ESL,
      "Aşağıdaki eşya – pozisyon eşleştirmelerinden hangisi <b>yanlıştır</b>?",
      "Potasyum nitratlı stabilize kanalizasyon çamuru – 31.01",
      ["Kemik, odun veya turb külleri – 26.21",
       "Deri kırpıntıları, deri talaşı tozu ve unu – 41.15",
       "Ağır metal içeren, gübre olarak kullanılamayan çamur – 38.25",
       "Sıvı veya kuru haldeki hayvan kanı – 05.11"], "E",
      "31.01 açıklama notu, potasyum veya amonyum nitratlı stabilize kanalizasyon çamurunu bu pozisyondan hariç tutar ve 31.05’e gönderir; kimyasal gübre katılmış tabii gübre artık 31.01’de değildir. Diğer eşleştirmeler aynı notun hariç tutma listesiyle uyumludur.",
      "31.01 Açıklama Notu; Fasıl 31 Not 1(a)."),
    # 22 — Çoktan-çoğa
    Q(T_COK,
      "Aşağıdakilerden hangileri 31.02 pozisyonunda sınıflandırılır? I. Kalsiyum nitrat ve magnezyum nitratın çift tuzları II. Üre ve amonyum nitratın sulu çözelti içindeki karışımından oluşan sıvı gübre III. Amonyum dihidrojenortofosfat (monoamonyum fosfat) IV. Amonyum klorürün alçı taşı ile karışımından oluşan gübre",
      "I, II ve IV",
      ["I ve III", "II ve III", "I, III ve IV", "II, III ve IV"], "A",
      "I, Not 2(a)(vi); II, Not 2(d) (ürenin veya amonyum nitratın ya da karışımlarının sulu veya amonyaklı çözeltileri); IV, Not 2(c) kapsamındadır. Monoamonyum fosfat ise azot ve fosforu birlikte içerir ve Not 5 gereği 31.05’tedir.",
      "Fasıl 31 Not 2 ve Not 5."),
    # 23
    Q(T_COK,
      "Fasıl 31 ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Tohumun filizlenmesine yardım eden ve az miktarda azot, fosfor, potasyum içeren mikrobesin müstahzarları 31.05’tedir. II. Esası turb olan saksı toprağı 27.03’tedir. III. Hayvansal gübrelerin kimyasal gübrelerle karışımları 31.05’tedir. IV. 31.02–31.04 gübrelerinin safsızlık olarak çok az başka bitki besin maddesi içermesi onları 31.05’e taşımaz.",
      "II, III ve IV",
      ["I ve II", "II ve III", "I, III ve IV", "I, II ve IV"], "D",
      "Genel açıklamalar mikrobesin müstahzarlarını 38.24’e, turb esaslı yetiştirme ortamlarını 27.03’e gönderir (I yanlış, II doğru). 31.05 açıklama notu hayvansal-bitkisel gübrelerle kimyasal gübrelerin karışımlarını sayar (III) ve safsızlık halindeki az miktar diğer besin maddesinin bileşik gübre yaratmadığını belirtir (IV).",
      "Fasıl 31 Genel Açıklamalar; 31.05 Açıklama Notu."),
    # 24 — Senaryo
    Q(T_SEN,
      "Tabii kalsiyum fosfatların nitrik asitle muamele edilmesi, ayrılan kalsiyum nitratın uzaklaştırılması, eriyiğin amonyakla nötralize edilip potasyum tuzları katılması ve kurutulmasıyla elde edilen, ticarette bazen “potasyum nitrofosfat” denilen granül gübre brüt 50 kg’lık çuvallarda ithal edilmektedir. Ürün kimyasal olarak belirli bir bileşik değildir. Eşya hangi pozisyonda sınıflandırılır?",
      "31.05",
      ["28.34", "28.35", "31.03", "31.02"], "B",
      "31.05 açıklama notu bu üretim yöntemini kimyasal işlemle elde edilen kompleks gübre örneği olarak verir ve adının yanıltıcı olduğunu, ürünün belirli bir kimyasal bileşik olmadığını vurgular. Azot, fosfor ve potasyumu birlikte içerdiğinden 31.02 veya 31.03’e girmez; belirli bileşik olmadığından Fasıl 28 de uygulanmaz.",
      "31.05 pozisyon metni ve Açıklama Notu."),
    # 25
    Q(T_SEN,
      "Şehir atık sularını arıtan bir tesisten elde edilen; kalburdan geçirilip açık havada kurutulmuş, büyük oranda organik madde ile bir miktar fosfor ve azot içeren, ağır metal oranı gübre olarak kullanılmasına engel olmayan stabilize kanalizasyon çamuru, brüt 500 kg’lık büyük çuvallarda ithal edilmektedir. Eşya hangi pozisyonda sınıflandırılır?",
      "31.01",
      ["38.25", "31.05", "27.03", "25.30"], "C",
      "31.01 açıklama notu stabilize kanalizasyon çamurunu ismen sayar. Ağır metal gibi maddeler nedeniyle gübre olarak kullanılamayan çamur 38.25’e, potasyum veya amonyum nitrat katılmış çamur 31.05’e gider; burada iki şart da yoktur ve ambalaj brüt 10 kg’ı aştığı için 31.05’in küçük ambalaj kuralı da uygulanmaz.",
      "31.01 Açıklama Notu."),
]

modul = {
    "tur": "fasil",
    "fasil": 31,
    "baslik": "Gübreler",
    "bolum": "VI",
    "oz": {
        "vurgu": "Fasıl 31 kapalı listeler faslıdır: 31.02, 31.03 ve 31.04 yalnızca notlarda sayılan ürünleri kapsar ve bu ürünler gübre olarak kullanılmasalar bile buradadır. Listede olmayan kimyasal olarak belirli bileşikler gübre olarak kullanılsa da Fasıl 28’e gider. Tablet şekli veya brüt 10 kg’ı geçmeyen ambalaj, faslın her ürününü 31.05’e taşır.",
        "maddeler": [
            "31.01: hayvansal veya bitkisel gübreler (guano, stabilize kanalizasyon çamuru dahil); kimyasal gübreyle karışınca 31.05.",
            "31.02 azotlu, 31.03 fosfatlı, 31.04 potaslı: tek besin maddeli ve Not 2, 3, 4’teki sınırlı listelerle bağlı.",
            "31.05: azot, fosfor ve potasyumdan ikisini veya üçünü içerenler, MAP ve DAP, diğer gübreler; ayrıca tablet veya brüt ≤ 10 kg ambalajdaki tüm fasıl ürünleri.",
            "Toprağı verimli kılmaktan çok ıslah eden maddeler (kireç 25.22, kireçli ve bitkisel toprak 25.30, turb 27.03) ve mikrobesin müstahzarları (38.24) fasıl dışındadır.",
        ],
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Toprağı ıslah eden madde, turb, saksı toprağı veya mikrobesin müstahzarı mı?", "<b>25.22</b> / <b>25.30</b> / <b>27.03</b> / <b>38.24</b>"],
            ["2", "Notlardaki listelerde olmayan, kimyasal olarak belirli bileşik mi? (amonyum klorür, potasyum nitrat, potasyum karbonat, sodyum fosfat)", "Fasıl 28 (<b>28.27</b>, <b>28.34</b>, <b>28.36</b>, <b>28.35</b>)"],
            ["3", "Fasıl ürünü tablet veya benzeri şekilde ya da brüt ağırlığı 10 kg’ı geçmeyen ambalajda mı?", "<b>31.05</b>"],
            ["4", "Monoamonyum veya diamonyum fosfat ya da bunların karışımı mı?", "<b>31.05</b> (saf olsa bile)"],
            ["5", "Hayvansal veya bitkisel gübre mi? (karışık veya kimyasal işlem görmüş olabilir)", "<b>31.01</b> (kimyasal gübreyle karışıksa 31.05)"],
            ["6", "Azot, fosfor ve potasyumdan ikisini veya üçünü içeren mineral/kimyasal gübre mi?", "<b>31.05</b>"],
            ["7", "Yalnız azotlu ve Not 2 listesinde mi? (üre, amonyum nitrat, amonyum sülfat, sodyum nitrat, kalsiyum siyanamit…)", "<b>31.02</b>"],
            ["8", "Yalnız fosfatlı ve Not 3 listesinde mi? (süperfosfat, bazik cüruf, kalsine tabii fosfat, ≥ %0,2 F’li kalsiyum hidrojenortofosfat)", "<b>31.03</b>"],
            ["9", "Yalnız potaslı ve Not 4 listesinde mi? (potasyum klorür, potasyum sülfat, ham tabii potasyum tuzları, magnezyum potasyum sülfat)", "<b>31.04</b>"],
            ["10", "Diğer gübreler (besin maddesi + besin olmayan madde karışımı vb.)*", "<b>31.05</b>"],
        ],
        "dipnot": "* Azotlu veya fosfatlı ürünlerin tebeşir, alçı taşı veya besin maddesi olmayan diğer inorganik maddelerle karışımları Not 2(c) ve 3(c) ile 31.02 / 31.03’te kalır; potaslılar için böyle bir hüküm yoktur.",
    },
    "pozisyon_haritasi": [
        ["31.01", "Hayvansal veya bitkisel gübreler", "Karışık veya kimyasal işlem görmüş olabilir; kimyasal gübre içermez", "Guano, stabilize kanalizasyon çamuru, kan-kemik unu karışımı"],
        ["31.02", "Azotlu mineral veya kimyasal gübreler", "Not 2 sınırlı listesi; kullanım amacı önemsiz", "Üre, amonyum nitrat, amonyum sülfat, kalsiyum siyanamit"],
        ["31.03", "Fosfatlı mineral veya kimyasal gübreler", "Not 3 sınırlı listesi; %0,2 flor eşiği", "Süperfosfat, Thomas cürufu, kalsine tabii fosfat"],
        ["31.04", "Potaslı mineral veya kimyasal gübreler", "Not 4 sınırlı listesi", "Potasyum klorür, potasyum sülfat, karnalit, kainit, silvit"],
        ["31.05", "NPK’dan ikisini/üçünü içerenler; MAP, DAP; diğer gübreler; küçük ambalajlar", "İki-üç besin; organik + kimyasal; tablet veya brüt ≤ 10 kg", "NPK kompoze gübre, DAP, 5 kg torbada üre"],
    ],
    "notlar": [
        ["Fasıl 31 Not 1", "Fasıl dışı: (a) 05.11’deki hayvan kanı; (b) kimyasal olarak belirli izole bileşikler (Not 2(a), 3(a), 4(a) ve 5’tekiler hariç); (c) her birinin ağırlığı 2,5 g veya daha fazla olan potasyum klorür kristalleri (optik elemanlar hariç) 38.24; potasyum klorür optik elemanları 90.01."],
        ["Fasıl 31 Not 2", "31.02 (31.05 şekil ve ambalajında olmamak şartıyla) <b>sadece</b>: (a) sodyum nitrat, amonyum nitrat, amonyum sülfat-amonyum nitrat çift tuzları, amonyum sülfat, kalsiyum nitrat-amonyum nitrat ve kalsiyum nitrat-magnezyum nitrat çift tuzları veya karışımları, kalsiyum siyanamit, üre (saf olsun olmasın); (b) bunların birbirleriyle karışımları; (c) amonyum klorürün veya (a)–(b) ürünlerinin tebeşir, alçı taşı veya besin maddesi olmayan inorganik maddelerle karışımları; (d) amonyum nitrat veya ürenin ya da karışımlarının sulu veya amonyaklı çözeltisi halindeki sıvı gübreler."],
        ["Fasıl 31 Not 3", "31.03 <b>sadece</b>: (a) bazik cüruf; 25.10’daki tabii fosfatlardan kalsine edilmiş veya ileri ısıl işlem görmüş olanlar; süperfosfatlar (tek, çift, üçlü); kuru susuz ürün üzerinden ağırlıkça <b>%0,2 veya daha fazla flor</b> içeren kalsiyum hidrojenortofosfat; (b) bunların karışımları; (c) bunların tebeşir, alçı taşı veya besin maddesi olmayan inorganik maddelerle karışımları. (b) ve (c)’de flor limiti aranmaz."],
        ["Fasıl 31 Not 4", "31.04 <b>sadece</b>: (a) ham tabii potasyum tuzları (karnalit, kainit, silvit), potasyum klorür (Not 1(c) saklı), potasyum sülfat, magnezyum potasyum sülfat (saf olsun olmasın); (b) bunların birbirleriyle karışımları."],
        ["Fasıl 31 Not 5", "Monoamonyum fosfat ve diamonyum fosfat (saf olsun olmasın) ve birbirleriyle karışımları 31.05’tedir."],
        ["Fasıl 31 Not 6", "31.05’teki “diğer gübreler”: sadece gübre olarak kullanılan ve azot, fosfor, potasyum gibi bitki besin maddelerinden en az birini ana unsur olarak içeren ürünler."],
        ["Genel Açıklamalar", "Toprağı verimli kılmaktan çok ıslah eden kireç (25.22), kireçli ve bitkisel toprak (25.30), turb (27.03) fasıl dışıdır. Mikrobesin müstahzarları ve toprak-kum-kil esaslı yetiştirme ortamları 38.24, turb esaslı olanlar 27.03’tedir."],
        ["31.01 Açıklama Notu", "Guano, gübre dışında kullanılamayan pislikler ve çürümüş bitkisel ürünler, kan-kemik unu karışımları, stabilize kanalizasyon çamuru buradadır. Ağır metalli çamur 38.25; potasyum veya amonyum nitratlı çamur ve tabii gübrelerin kimyasal gübrelerle karışımı 31.05; toz kemik ve boynuz Fasıl 5; küller 26.21."],
        ["31.02 Açıklama Notu", "31.02, 31.03 ve 31.04 açıklama notlarında ortak kural: sınırlı listedeki ürünler gübre olarak kullanılmayacakları açıkça belli olsa da buradadır. Listede olmayan ürünler (amonyum klorür 28.27, sodyum fosfat 28.35, potasyum karbonat 28.36) gübre olarak kullanılsa da hariçtir. Listedeki karışımlar ise yalnız gübre olarak kullanılan türdense buradadır."],
        ["31.05 Açıklama Notu", "Potasyum nitrat (28.34) ve potasyum fosfat (28.35) gübre olarak kullanılsa da hariçtir; tesiri kalmamış oksit 38.25. 31.02–31.04 gübrelerinin safsızlık olarak az miktar başka besin maddesi içermesi onları bileşik gübre yapmaz."],
    ],
    "sinir_komsulari": [
        ["Sıvı veya kuru hayvan kanı", "05.11", "Fasıl 31 Not 1(a)"],
        ["Toz haline getirilmiş kemik, boynuz, tırnak, balık artıkları", "Fasıl 5", "31.01 Açıklama Notu"],
        ["Yenmeyen et, balık unları; yağlı küspeler", "23.01 / Fasıl 23", "Yem hammaddeleri"],
        ["Kalsine edilmemiş ham tabii kalsiyum fosfat", "25.10", "Not 3 yalnız kalsine veya ısıl işlem görmüşü alır"],
        ["Kireç; kireçli toprak, bitkisel toprak", "25.22 / 25.30", "Islah maddesi (Genel Açıklamalar)"],
        ["Turb; turb esaslı saksı toprağı", "27.03", "Islah maddesi (Genel Açıklamalar)"],
        ["Kemik, odun, turb veya kömür külleri", "26.21", "31.01 Açıklama Notu"],
        ["Amonyum klorür (tek başına)", "28.27", "Not 2 listesinde yok"],
        ["Potasyum nitrat", "28.34", "31.05 Açıklama Notu"],
        ["Sodyum fosfat, potasyum fosfat; %0,2’den az F’li kalsiyum hidrojenortofosfat", "28.35", "Liste dışı / flor eşiği"],
        ["Potasyum karbonat", "28.36", "31.04 Açıklama Notu"],
        ["Mikrobesin müstahzarı; toprak-kum-kil esaslı yetiştirme ortamı; ≥ 2,5 g potasyum klorür kristali", "38.24", "Genel Açıklamalar; Not 1(c)"],
        ["Ağır metalli kanalizasyon çamuru; tesiri kalmamış oksit", "38.25", "31.01 ve 31.05 Açıklama Notları"],
        ["Deri kırpıntıları, deri talaşı tozu", "41.15", "31.01 Açıklama Notu"],
        ["Potasyum klorür optik elemanları", "90.01", "Fasıl 31 Not 1(c)"],
    ],
    "tuzaklar": [
        "<b>Kullanım amacı değil liste belirler.</b> Not 2–4’te sayılan ürünler (ör. yem veya reçine imali için üre) gübre olarak kullanılmayacak olsalar bile 31.02–31.04’tedir.",
        "<b>Gübre olarak kullanılan her kimyasal gübre değildir.</b> Listede olmayan belirli kimyasal bileşikler (amonyum klorür 28.27, potasyum nitrat 28.34, potasyum fosfat 28.35, potasyum karbonat 28.36) Fasıl 28’de kalır.",
        "<b>Amonyum klorür iki yerde.</b> Tek başına 28.27; tebeşir, alçı taşı veya besin maddesi olmayan inorganik maddelerle karışık gübre ise Not 2(c) ile 31.02.",
        "<b>10 kg kuralı brüt ağırlıktır ve herkese uygulanır.</b> Fasıldaki herhangi bir ürün tablet halinde veya brüt ağırlığı 10 kg’ı geçmeyen ambalajda ise 31.05’e geçer; 31.01’deki guano dahil.",
        "<b>MAP ve DAP saf olsa da 31.05.</b> Kimyasal olarak belirli olmalarına rağmen Not 5 bunları 31.05’e verir; gübre olarak kullanılıp kullanılmamaları önemsizdir.",
        "<b>%0,2 flor eşiği.</b> Kalsiyum hidrojenortofosfat kuru susuz ürün üzerinden ağırlıkça %0,2 veya daha fazla flor içeriyorsa 31.03, daha azsa 28.35. Karışımlarda bu limit aranmaz.",
        "<b>Islah eden ≠ verimli kılan.</b> Kireç 25.22, bitkisel toprak 25.30, turb 27.03; doğal olarak az miktarda azot, fosfor, potasyum içerseler de Fasıl 31’e girmezler.",
        "<b>Organik + kimyasal = 31.05.</b> Tabii gübrelerin kimyasal gübrelerle karışımı ve potasyum ya da amonyum nitratlı stabilize kanalizasyon çamuru 31.05’tedir.",
        "<b>Ham tabii fosfat Fasıl 25’tedir.</b> 25.10’daki tabii fosfatlar ancak kalsine edilmiş veya safsızlıkların giderilmesi için ileri ısıl işlem görmüşse 31.03’e girer.",
        "<b>2(b) burada işlemez.</b> GYK 1 açıklama notu, Fasıl 31 notlarının belirli pozisyonları belirli eşyayla sınırladığını ve 2(b) kuralıyla bu pozisyonlara başka karışımların girmesini önlediğini örnek verir.",
    ],
    "hafiza": {
        "kanca": "1 HAYVAN – 2 AZOT – 3 FOSFOR – 4 POTAS – 5 KARMA ve KÜÇÜK TORBA",
        "aciklama": "Pozisyonlar NPK sırasını izler: <b>01</b> doğal gübre, <b>02</b> N, <b>03</b> P, <b>04</b> K, <b>05</b> ikili-üçlü karma, MAP-DAP ve 10 kg’dan hafif torba. Görsel benzetme: bir çiftlik deposunda en başta ahır ve guano yığını, sonra N, P, K yazılı üç ayrı silo; en sonda karışım makinesi ve yanında perakende küçük torbalar rafı.",
    },
    "sinav_odagi": [
        "Bu fasıl çıkmış sorularda doğrudan değil, daha çok fasıl–eşya eşleştirmesi ve çeldirici seçenek olarak yer almıştır.",
        "“Hangisi yanlıştır” kalıbında fasıl numarası doğrulaması: “Gübre 31. fasılda yer alır” ifadesinin doğru seçenek olarak kullanılması.",
        "Turb (turba): tarımda kullanılsa bile Fasıl 27’de olduğu; havagazı, elektrik, vazelin ile aynı fasıl grubunda sorulması.",
        "“Aynı fasılda yer almayan” sorularında turbun elektrik enerjisi ve vazelinle birlikte Fasıl 27 grubunda verilmesi; kullanım yerinin değil tarife tanımının belirleyici olduğunun test edilmesi.",
    ],
    "cikmis_ornekler": [
        {
            "soru": "Tarife Cetveli’ne göre aşağıdaki ifadelerden hangisi <b>yanlıştır</b>?",
            "secenekler": ["Hububat 10. fasılda yer alır.", "Gübre 31. fasılda yer alır.", "Pamuk 53. fasılda yer alır.", "Cam 70. fasılda yer alır.", "Saat 91. fasılda yer alır."],
            "cevap": "C",
            "aciklama": "Pamuk Fasıl 52’de yer alır; Fasıl 53 dokumaya elverişli diğer bitkisel lifleri kapsar. Gübreler Fasıl 31’in konusudur.",
        },
        {
            "soru": "Aşağıdakilerden hangisi Tarife Cetveli’nin 27. Faslı altında <b>sınıflandırılamaz</b>?",
            "secenekler": ["Havagazı", "Tarımda kullanılan turba", "Elektrik", "Hidrojen gazı", "Vazelin"],
            "cevap": "D",
            "aciklama": "Hidrojen bir kimyasal element olarak Fasıl 28’dedir (28.04). Turba tarımda kullanılsa da gübre sayılmaz; Fasıl 31 genel açıklamaları toprağı ıslah eden turbu 27.03’e gönderir.",
        },
    ],
    "ozet": [
        "31.02, 31.03 ve 31.04 yalnız notlardaki sınırlı listeleri kapsar; listedeki ürün kullanım amacına bakılmaksızın buradadır.",
        "Listede olmayan belirli kimyasal bileşik gübre olarak kullanılsa da Fasıl 28’dedir.",
        "İki veya üç besin maddesi (N, P, K), MAP ve DAP, organik + kimyasal karışım 31.05’tedir.",
        "Tablet veya brüt ağırlığı 10 kg’ı geçmeyen ambalaj, faslın her ürününü 31.05’e taşır.",
        "Hayvansal ve bitkisel gübreler 31.01; ağır metalli çamur 38.25, nitratlı çamur 31.05.",
        "Islah maddeleri (kireç, bitkisel toprak, turb) ve mikrobesin müstahzarları fasıl dışıdır.",
    ],
    "sorular": sorular,
}

if __name__ == "__main__":
    harfler = Counter(q["cevap"] for q in sorular)
    assert len(sorular) == 25, len(sorular)
    assert all(harfler[h] == 5 for h in "ABCDE"), harfler
    with open(CIKTI, "w", encoding="utf-8") as f:
        json.dump(modul, f, ensure_ascii=False, indent=1)
    print("yazıldı:", CIKTI, dict(harfler))
