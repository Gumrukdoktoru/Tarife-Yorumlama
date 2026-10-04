#!/usr/bin/env python3
"""Fasıl 95 modülü üreteci."""
import json
import os

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EP = "Eşya → 4’lü pozisyon"
OT = "Olumsuz teşhis"
FA = "Farklı/aynı pozisyon veya fasıl"
TN = "Fasıl notu · Tanım/Eşik"
GY = "Genel Yorum Kuralı"
ES = "Eşleştirme / Boşluk doldurma"
CC = "Çoktan-çoğa (I–IV)"
SN = "Senaryo"


def S(soru, dogru, yanlislar, harf, tip, gerekce, dayanak):
    assert len(yanlislar) == 4, soru
    opts = list(yanlislar)
    opts.insert("ABCDE".index(harf), dogru)
    return {"soru": soru, "secenekler": opts, "cevap": harf, "tip": tip,
            "gerekce": gerekce, "dayanak": dayanak}


sorular = [
    # 1 EP
    S("Tarife Cetveline göre, çocukların binebileceği büyüklükte, minyatür jip şeklinde yapılmış ve pedallar yardımıyla gücü tekerleklere aktarılan oyuncak araba hangi pozisyonda sınıflandırılır?",
      "95.03", ["87.12", "87.03", "95.08", "95.06"], "B", EP,
      "Pedallı arabalar (sıklıkla minyatür spor araba, jip, kamyon şeklinde) 95.03 Açıklama Notunun (A) tekerlekli oyuncaklar grubunda sayılır. Fasıl 87 Not 4’e göre çocuklar için bisikletler 87.12’de, çocuklar için diğer tekerlekli araçlar ise 95.03’tedir. Eşya bir motorlu taşıt (87.03) veya panayır eğlencesi aracı (95.08) değildir.",
      "95.03 Açıklama Notu (A); Fasıl 87 Not 4."),
    # 2 EP
    S("Tarife Cetveline göre, mantardan yapılmış bir hedef tahtası ile bu tahtaya atılan oklardan oluşan dart oyunu takımı hangi pozisyonda sınıflandırılır?",
      "95.04", ["95.06", "45.04", "95.03", "95.07"], "D", EP,
      "Dart tahtaları ve dartlar 95.04 Açıklama Notunda (10) adıyla sayılır. Fasıl 45 notu 95. Fasıldaki eşyayı (oyuncak, oyun, spor malzemesi) kapsam dışı bıraktığından mantardan yapılmış olması 45.04’e götürmez. Okçuluk malzemesi 95.06’da, avcılık ve atıcılık levazımatı 95.07’dedir; dart ise salon oyunudur.",
      "95.04 Açıklama Notu (10); Fasıl 45 Not 1(c)."),
    # 3 EP
    S("Tarife Cetveline göre, kauçuktan yapılmış dalgıç paletleri hangi pozisyonda sınıflandırılır?",
      "95.06", ["40.16", "64.01", "90.20", "95.07"], "A", EP,
      "95.06 Açıklama Notu (B)(2), su sporu aletleri arasında dalgıç paletlerini açıkça sayar. Fasıl 40 notu 95. Fasıldaki eşyayı kauçuk faslının dışında bırakır; palet ayakkabı olmadığından Fasıl 64’e de girmez. 90.20 ise oksijen veya sıkıştırılmış hava tüpüyle kullanılan teneffüs cihazlarına aittir.",
      "95.06 Açıklama Notu (B)(2); Fasıl 40 Not 2."),
    # 4 EP
    S("Tarife Cetveline göre, kuş avında yem olarak kullanılan, ses çıkarmayan ahşap yapma ördek hangi pozisyonda sınıflandırılır?",
      "95.07", ["92.08", "97.05", "44.20", "95.03"], "C", EP,
      "95.07 pozisyon metni kuş avcılığına mahsus yapma kuşları açıkça sayar; yalnızca her türden öten tuzak nesneleri (92.08) ve 97.05’teki doldurulmuş kuşlar hariçtir. Ahşaptan olması 44.20’ye götürmez; Fasıl 44 oyun ve spor malzemelerini kapsamaz. Eşya eğlence oyuncağı değil av levazımatı olduğundan 95.03 de yanlıştır.",
      "95.07 pozisyon metni ve Açıklama Notu (4)."),
    # 5 EP
    S("Tarife Cetveline göre, bir lunaparkta kurulmak üzere getirilen çarpışan araba (dodge’em) tesisatı hangi pozisyonda sınıflandırılır?",
      "95.08", ["87.03", "95.03", "95.04", "95.06"], "E", EP,
      "Çarpışan araba tesisatı 95.08 Açıklama Notunda eğlence parkı gezinti eşyası olarak adıyla sayılır; Fasıl 87 açıklamaları da fuar ve eğlence parkı araçlarını 95.08’e gönderir. Çocukların binip sürdüğü oyuncak arabalar 95.03’te, salon ve masa oyunları ile ödeme aracıyla çalışan eğlence makineleri 95.04’tedir.",
      "Fasıl 95 Not 6(a); 95.08 Açıklama Notu."),
    # 6 OT
    S("Aşağıdakilerden hangisi Tarife Cetvelinin 95. faslında <b>sınıflandırılmaz</b>?",
      "Doğum günü pastası için renkli mum",
      ["Plastikten yapılmış oyuncak tabanca", "Masa tenisi için ahşap raket", "Kağıttan kesilmiş renkli konfeti", "Misina takılı çelik olta iğnesi"], "C", OT,
      "Mumlar Fasıl 95 Not 1(a) uyarınca fasıl dışıdır ve 34.06’da yer alır; 95.05 Açıklama Notu da mumları ayrıca hariç tutar. Oyuncak tabanca 95.03’te, masa tenisi raketi 95.06’da, konfeti 95.05’te, olta iğnesi 95.07’dedir. Tuzak, kutlama amaçlı mumu bayram eşyası sanmaktır.",
      "Fasıl 95 Not 1(a); 95.05 Açıklama Notu, hariç tutmalar."),
    # 7 OT
    S("Aşağıdakilerden hangisi 95.06 pozisyonunda <b>sınıflandırılmaz</b>?",
      "Yüzücüler için koruyucu gözlük",
      ["Kayak sopası", "Golf topu", "Dağcıların kullandığı buz baltası", "Eskrim maskesi"], "D", OT,
      "Spor ve açık hava oyunları için gözlükler ve koruyucu gözlükler Not 1(r) uyarınca 90.04’tedir; 95.06 Açıklama Notu da kurbağa adam gözlüklerini hariç tutar. Kayak sopası, golf topu, buz baltası ve eskrim maskesi 95.06 Açıklama Notunda adıyla sayılır.",
      "Fasıl 95 Not 1(r); 95.06 Açıklama Notu (B) ve hariç tutma (k)."),
    # 8 OT
    S("Aşağıdakilerden hangisi 95.03 pozisyonunda <b>sınıflandırılmaz</b>?",
      "Çocuklar için resim ve boyama kitabı",
      ["Plastikten oyuncak bebek elbisesi", "Kağıt ve çıtadan yapılmış uçurtma", "Çocuklar için ahşap salıncaklı at", "Karton parçalardan oluşan yapboz (puzzle)"], "A", OT,
      "95.03 Açıklama Notu, çocuklar için resim, çizim veya boyama yapmaya mahsus albüm ve kitapları hariç tutar (49.03). Oyuncak bebek giysileri bebeklerin aksesuarı olarak, uçurtma ve salıncaklı at diğer oyuncaklar grubunda, bulmacalar ise (F) grubunda 95.03’tedir.",
      "95.03 Açıklama Notu, hariç tutma (c); (C), (D), (F) grupları."),
    # 9 OT
    S("Aşağıdakilerden hangisi 95.05 pozisyonunda <b>sınıflandırılmaz</b>?",
      "Noel için kesilmiş doğal çam ağacı",
      ["Plastikten suni Noel ağacı", "Kağıttan karnaval şapkası",
       "Sihirbazlık gösterisi için özel yapılmış oyun kağıtları", "Şaka amaçlı aksırtma tozu"], "E", OT,
      "Hakiki Noel ağaçları 95.05 Açıklama Notunda hariç tutulmuştur ve Fasıl 6’da yer alır. Suni Noel ağacı ve kağıt şapka bayram-karnaval eşyası, sihirbazlık için özel yapılmış oyun kağıtları ve aksırtma tozu sihirbazlık-sürpriz eşyası olarak 95.05’tedir. Tuzak, sihirbazlık kağıtlarını 95.04’teki oyun kağıtlarıyla karıştırmaktır.",
      "95.05 Açıklama Notu (A), (B) ve hariç tutmalar."),
    # 10 FA
    S("Aşağıdakilerden hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır?",
      "Ahşap bulmaca (puzzle)",
      ["Satranç tahtası ve taşları", "Bilardo istekası", "Futbol oyun masası (langırt)", "İskambil kağıdı destesi"], "B", FA,
      "Bulmacalar 95.03’tedir; 95.04 Açıklama Notu bulmacaları (puzzles) açıkça hariç tutar. Satranç tahtası ve taşları, bilardo istekası, futbol oyun masası ve oyun kağıtları 95.04 Açıklama Notunda sayılmıştır. Tuzak, “masa oyunu” gibi görünen bulmacayı 95.04’e koymaktır.",
      "95.03 pozisyon metni; 95.04 Açıklama Notu (1), (5), (11), (12) ve hariç tutmalar."),
    # 11 FA
    S("Aşağıdaki eşyadan hangisi diğerlerinden farklı bir fasılda sınıflandırılır?",
      "Tek kişilik spor kanosu",
      ["Buz pateni takılmış bot", "Karda kayan motorsuz kızak", "Rüzgar sörfü", "Paten tahtası"], "C", FA,
      "Spor deniz taşıtları (kano, kayık) Not 1(q) uyarınca Fasıl 89’dadır. Paten takılmış bot Not 1(g)’deki istisna nedeniyle, kızak Not 1(n)’deki istisna nedeniyle 95.06’dadır; rüzgar sörfü ve paten tahtası da 95.06’da sayılır. Tuzak, kızağı Bölüm XVII taşıtı sanmaktır.",
      "Fasıl 95 Not 1(g), (n), (q); 95.06 Açıklama Notu (B)(2), (7), (14)."),
    # 12 FA
    S("Aşağıdaki oyun ve eğlence ekipmanlarından hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır?",
      "Lunaparkta kurulu atlıkarınca",
      ["Çocuk bahçesi salıncağı", "Çocuk oyun alanı kaydırağı", "Okul bahçesine kurulan tahterevalli", "Jimnastik salonu için halter seti"], "D", FA,
      "Atlıkarıncalar, salıncaklar ve döner platformlar eğlence parkı gezinti eşyası olarak 95.08’dedir. Not 6(a) ise konutlarda veya oyun alanlarında yaygın olarak kurulan türden ekipmanı bu tanımın dışında bırakır; çocuk bahçesi salıncağı, kaydırak ve tahterevalli 95.06 Açıklama Notunun (B)(12) bendindedir. Halter de 95.06’dadır.",
      "Fasıl 95 Not 6(a); 95.06 Açıklama Notu (A), (B)(12); 95.08 Açıklama Notu."),
    # 13 FA
    S("Aşağıdaki spor malzemelerinden hangisi diğerlerinden farklı bir fasılda sınıflandırılır?",
      "Deriden boks eldiveni",
      ["Kriket pedi", "Tekmelik", "Eskrim maskesi", "Spor için dizlik ve dirseklik"], "A", FA,
      "Eldivenler Not 1(y) uyarınca mamul oldukları maddeye göre sınıflandırılır; 95.06 Açıklama Notu spor eldivenlerini genellikle 42.03’e gönderir, Fasıl 42 de deriden spor eldivenlerini 42.03’te tutar. Kriket pedi, tekmelik, eskrim maskesi ve dizlik-dirseklik 95.06’daki koruyucu spor malzemeleridir.",
      "Fasıl 95 Not 1(y); 95.06 Açıklama Notu (B)(13) ve hariç tutma (c)."),
    # 14 TN
    S("Tarife Cetvelinin 95. Fasıl 6 no.lu Notuna göre aşağıdakilerden hangisi <b>doğrudur</b>?",
      "Eğlence parkı gezinti eşyası, konutlarda veya oyun alanlarında yaygın olarak kurulan türden ekipmanı içermez.",
      ["Su parkı eğlence eşyası, su içeren alanda amaçla inşa edilmiş bir yol boyunca kişiyi taşıyan cihaz olarak tanımlanır.",
       "Fuar alanı eğlence eşyası, 95.04 pozisyonundaki teçhizatı da kapsar.",
       "Eğlence parkı gezinti eşyası, su yolları üzerinde çalışan cihazları kapsamaz.",
       "Fuar alanı eğlenceleri yalnızca kalıcı binalara kurulabilen oyunlardır."], "E", TN,
      "Not 6(a), eğlence parkı gezinti eşyasını su yolları dahil sabit veya sınırlı bir parkur üzerinde kişiyi taşıyan ya da yönlendiren cihaz olarak tanımlar ve konut ile oyun alanı ekipmanını dışarıda bırakır. Su parkı eğlencesinin ayırt edici özelliği, amaçla inşa edilmiş yolunun olmamasıdır. Fuar alanı eğlenceleri 95.04 teçhizatını kapsamaz; kalıcı binalara veya bağımsız imtiyaz tezgahlarına kurulabilir.",
      "Fasıl 95 Not 6(a), (b), (c)."),
    # 15 TN
    S("Tarife Cetvelinin 95. Fasıl notlarına göre, kıymetli metal veya kıymetli taş içeren eşya ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
      "Önemsiz sayılacak ölçüde kıymetli taş veya kıymetli metal içeren eşya Fasıl 95’e dahildir.",
      ["Kıymetli metal içeren her oyuncak Fasıl 71’de sınıflandırılır.",
       "Yalnızca sentetik taş içeren eşya Fasıl 95’te kalabilir; tabii taş içerenler fasıl dışıdır.",
       "Kıymetli metalle kaplanmış metalden parça içeren eşya hiçbir durumda Fasıl 95’e giremez.",
       "Kültür incisi içeren oyuncak bebekler 95.05’te sınıflandırılır."], "B", TN,
      "Not 2’ye göre önemsiz sayılacak ölçüde tabii veya kültür incisi, kıymetli veya yarı kıymetli taş (tabii, sentetik veya terkip yoluyla elde edilmiş), kıymetli metal ya da kıymetli metal kaplama içeren eşya bu fasıla dahildir. Fasıl 71 notu da 95. Fasıl Not 2 kapsamındaki eşyayı kendi kapsamı dışında bırakır. Taşın tabii veya sentetik olması sonucu değiştirmez.",
      "Fasıl 95 Not 2; Fasıl 95 Genel Açıklamalar; Fasıl 71 Not 3(n)."),
    # 16 TN
    S("Biçimi, şekli ve yapıldığı madde itibarıyla yalnızca köpekler için tasarlandığı anlaşılan kauçuktan çiğneme oyuncağı ile ilgili olarak Tarife Cetveline göre aşağıdakilerden hangisi <b>doğrudur</b>?",
      "95.03 pozisyonu kapsamı dışındadır; kendi uygun pozisyonunda sınıflandırılır.",
      ["Diğer oyuncaklar grubunda 95.03 pozisyonunda yer alır.",
       "Perakende satışa hazır ambalajda ise 95.03, değilse 95.06 pozisyonunda yer alır.",
       "Eğlence amaçlı olduğundan 95.05 pozisyonunda yer alır.",
       "Hayvanlara mahsus olduğundan 95.08 pozisyonunda gezici hayvan sergisi eşyası sayılır."], "D", TN,
      "Not 5, biçimleri, şekilleri veya yapıldıkları maddeye dayanılarak münhasıran hayvanlar için tasarlandığı anlaşılan eşyayı (evcil hayvan oyuncakları) 95.03 kapsamı dışında bırakır; 95.03 Açıklama Notu bunların kendi uygun pozisyonlarında sınıflandırılacağını belirtir. Ambalaj şekli sonucu değiştirmez; 95.05 ve 95.08 ile ilgisi yoktur.",
      "Fasıl 95 Not 5; 95.03 Açıklama Notu (D)."),
    # 17 TN
    S("95.04 pozisyonu Açıklama Notuna göre “otomatik bowling oyunu ekipmanları” ifadesi ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
      "Labutların kare şeklinde dizildiği tipleri de kapsar.",
      ["Yalnızca labutların üçgen şeklinde dizildiği teçhizatı kapsar.",
       "Yalnızca elektro-mekanik özellikleri ve motoru olan teçhizatı kapsar.",
       "Bowling malzemeleri spor malzemesi olarak 95.06 pozisyonunda yer alır.",
       "Jetonla çalışan otomatik bowling ekipmanları 95.08 pozisyonuna girer."], "B", TN,
      "95.04 Açıklama Notu, otomatik bowling ekipmanlarının elektro-mekanik özellikleri ve motorları olsun olmasın bu pozisyonda yer aldığını ve ifadenin yalnız üçgen dizilişli değil kare dizilişli gibi diğer tipleri de kapsadığını belirtir. 95.06 her tür bowling malzemesini 95.04’e bırakır; 95.08 de ödeme aracıyla çalışan eğlence makinelerini hariç tutar.",
      "95.04 Açıklama Notu (7); 95.06 Açıklama Notu, hariç tutma (p)."),
    # 18 GY
    S("Tüm parçaları aynı ambalajda, birleştirilmemiş (demonte) halde gelen ve monte edildiğinde komple bir bilardo masası oluşturan eşyanın 95.04 pozisyonunda sınıflandırılmasını sağlayan Genel Yorum Kuralı hangisidir?",
      "GYK 2(a)", ["GYK 2(b)", "GYK 3(b)", "GYK 4", "GYK 5(a)"], "A", GY,
      "GYK 2(a), bir pozisyonda belirtilen eşyaya yapılan atfın bu eşyanın sökülerek veya monte edilmeden getirilmiş halini de kapsadığını hükme bağlar; bilardo masaları 95.04’te sayıldığından demonte masa da oraya girer. 2(b) madde karışımlarına, 3(b) karışık eşya ve setlere, 5(a) kutu ve mahfazalara ilişkindir; GYK 4 başka hiçbir pozisyona girmeyen eşya içindir.",
      "GYK 2(a); 95.04 Açıklama Notu (1)."),
    # 19 GY
    S("Perakende satış için tek ambalajda bir araya getirilmiş, plastik bir oyuncak figür ile az miktarda şekerlemeden oluşan, GYK 3(b)’ye göre set sayılmayan fakat oyuncağın esas karakterini taşıyan birleşim, Fasıl 95 Not 4 uyarınca 95.03 pozisyonunda sınıflandırılmaktadır. Bu sınıflandırmanın dayandığı Genel Yorum Kuralı hangisidir?",
      "GYK 1", ["GYK 3(b)", "GYK 3(c)", "GYK 2(b)", "GYK 5(b)"], "C", GY,
      "Sınıflandırma doğrudan bir fasıl notuna (Not 4) dayandığından pozisyon metinleri ve notları esas alan GYK 1 uygulanır. Not 4 birleşimin GYK 3(b)’ye göre set sayılmadığını açıkça öngördüğünden 3(b) ve onun yetmediği hallerde başvurulan 3(c) devreye girmez. 5(b) ambalaj malzemelerine, 2(b) madde karışımlarına ilişkindir.",
      "GYK 1; Fasıl 95 Not 4; 95.03 Açıklama Notu."),
    # 20 ES
    S("Tarife Cetvelinin 95. Fasıl 1 no.lu Notuna göre, spor ve açık hava oyunları için koruyucu gözlükler ……… pozisyonunda, düdükler ve avcı düdükleri ise ……… pozisyonunda sınıflandırılır. Boşluklara sırasıyla gelmesi gerekenler hangi seçenekte verilmiştir?",
      "90.04 – 92.08", ["95.06 – 92.08", "90.04 – 95.07", "90.18 – 92.08", "95.06 – 95.07"], "E", ES,
      "Not 1(r) spor ve açık hava oyunları gözlüklerini 90.04’e, Not 1(s) düdükleri ve avcı düdüklerini 92.08’e gönderir. 95.06 spor, 95.07 avcılık levazımatını kapsasa da bu iki eşya notla fasıl dışına çıkarılmıştır; 90.18 tıbbi alet pozisyonudur.",
      "Fasıl 95 Not 1(r) ve (s)."),
    # 21 ES
    S("Aşağıdaki eşyalar ile Tarife Cetvelindeki pozisyonları doğru eşleştirildiğinde hangi seçenek elde edilir?<br/>I. Oyun kağıtları<br/>II. Kağıttan karnaval şapkası<br/>III. Kayak bağlayıcısı<br/>IV. Olta makarası",
      "I–95.04, II–95.05, III–95.06, IV–95.07",
      ["I–95.03, II–95.05, III–95.06, IV–95.07",
       "I–95.04, II–95.03, III–95.06, IV–95.07",
       "I–95.04, II–95.05, III–95.06, IV–95.06",
       "I–95.05, II–95.05, III–95.06, IV–95.07"], "A", ES,
      "Oyun kağıtları 95.04’te (95.03 Açıklama Notu da onları 95.04’e gönderir), kağıt şapkalar ve maskeler 95.05’te, kayak bağlayıcıları 95.06’da, olta makaraları 95.07’dedir. Karnaval şapkasının 95.03’e, olta makarasının spor malzemesi olarak 95.06’ya konması tipik hatalardır.",
      "95.03 Açıklama Notu, hariç tutma (h) ve (ij); 95.04, 95.05, 95.06, 95.07 pozisyon metinleri."),
    # 22 CC
    S("Fasıl 95 Not 4 ile ilgili aşağıdaki ifadelerden hangileri <b>doğrudur</b>?<br/>I. 95.03 pozisyonu, GYK 3(b)’ye göre set sayılmayan ve ayrı geldiklerinde başka pozisyonlarda yer alan eşyalarla birleştirilmiş oyuncakları da kapsayabilir.<br/>II. Bunun için eşyaların perakende satış için bir araya getirilmiş olması gerekir.<br/>III. Birleşimin oyuncağın mümeyyiz vasfını (esas karakterini) taşıması gerekir.<br/>IV. Not 4 hükmü, Not 1 ile fasıl dışında bırakılan eşyalar için de uygulanır.",
      "I, II ve III", ["I ve II", "II ve III", "I, II ve IV", "II, III ve IV"], "D", CC,
      "Not 4, 1 no.lu Not hükmü saklı kalmak şartıyla, GYK 3(b)’ye göre set sayılmayan birleşimleri perakende satış için bir araya getirilmiş olmaları ve oyuncağın mümeyyiz vasfını taşımaları şartıyla 95.03’e alır. “Saklı kalmak şartıyla” ifadesi Not 1 dışlamalarının önceliğini korur; bu yüzden IV yanlıştır.",
      "Fasıl 95 Not 4; 95.03 Açıklama Notu."),
    # 23 CC
    S("Aşağıdakilerden hangileri 95.06 pozisyonunda sınıflandırılır?<br/>I. Karda kayan motorsuz kızak<br/>II. Dalgıçlar için sıkıştırılmış hava tüpü ile birlikte kullanılan solunum cihazı<br/>III. Yüzücüler için şnorkel (basit nefes alma tüpü)<br/>IV. Tenis raketi için ip (kordon)",
      "I ve III", ["I ve II", "II ve IV", "I, III ve IV", "II, III ve IV"], "C", CC,
      "Kızaklar ve benzeri motorsuz taşıtlar ile şnorkel ve tüpsüz solunum maskeleri 95.06’dadır. Oksijen veya sıkıştırılmış hava tüpüyle kullanılan teneffüs aletleri 90.20’de; raket ipleri ise Not 1(y) ve 95.06 Açıklama Notu uyarınca Fasıl 39, 42.06 veya Bölüm XI’dedir.",
      "Fasıl 95 Not 1(n), (y); 95.06 Açıklama Notu (B)(2), (14) ve hariç tutmalar (a), (n)."),
    # 24 SN
    S("Bir televizyona bağlanarak görüntü veren, esas işlevi oyun oynamak olan, oyun kumandası ile birlikte sunulan ve teknik olarak 84. Fasıl Not 5(A)’daki otomatik bilgi işlem makinesi şartlarını da karşılayan cihaz Tarife Cetveline göre hangi pozisyonda sınıflandırılır?",
      "95.04", ["84.71", "85.28", "85.43", "95.03"], "E", SN,
      "95.04 Açıklama Notuna göre esas işlevi eğlence (oyun oynama) olan video oyun konsolları, 84. Fasıl Not 5(A) şartlarını sağlasın sağlamasın 95.04’tedir; oyun kumandası da konsolun aksesuarı olarak aynı pozisyona girer. Ekranı olmadığından televizyon-monitör (85.28) değildir; eşya bir oyuncak (95.03) değil, video oyun konsoludur.",
      "95.04 Açıklama Notu (2); Fasıl 95 Not 3."),
    # 25 SN
    S("Perakende satışa hazır bir kutuda; birkaç plastik deney tüpü, az miktarda kimyasal madde, bir büyüteç ve deney kitapçığından oluşan, açıkça çocukların eğitici amaçla oynaması için tertiplenmiş “küçük kimyager” takımı Tarife Cetveline göre hangi pozisyonda sınıflandırılır?",
      "95.03", ["38.22", "90.23", "39.26", "95.04"], "B", SN,
      "Her unsuru ayrı geldiğinde başka pozisyonlara giren eşya koleksiyonları, oyuncak olarak kullanıldıkları açıkça anlaşılacak şekilde takım halinde ambalajlanmışsa Fasıl 95’te yer alır; 95.03 Açıklama Notu eğitici oyuncaklar arasında oyuncak kimya takımlarını sayar. Laboratuvar reaktifleri (38.22) veya teşhir amaçlı modeller (90.23) takımın karakterini vermez; 95.04 salon ve masa oyunlarına aittir.",
      "95.03 Açıklama Notu (D)(xviii) ve takımlara ilişkin paragraf."),
]

obj = {
    "tur": "fasil",
    "fasil": 95,
    "baslik": "Oyuncaklar, oyun ve spor malzemeleri; bunların aksam, parça ve aksesuarı",
    "bolum": "XX",
    "oz": {
        "vurgu": "Fasıl 95, eğlence ve spor amaçlı eşyanın faslıdır: oyuncaklar (95.03), salon-masa oyunları ve video oyun konsolları (95.04), bayram-karnaval eşyası (95.05), spor malzemeleri (95.06), olta ve av levazımatı (95.07), eğlence parkı ve panayır eşyası (95.08). Sınavın asıl sorusu şudur: Eşya gerçekten oyun-spor eşyası mı, yoksa Not 1’in fasıl dışına attığı bir fayda eşyası, giyim, ayakkabı, taşıt veya alet mi?",
        "maddeler": [
            "Not 1 uzun bir dışlama listesidir: mum, havai fişek, spor çantası, spor giyimi, spor ayakkabısı ve başlığı, eldiven, çadır, çocuk bisikleti, insansız hava taşıtı, kano, spor gözlüğü, düdük, silah, elektrikli çelenk, tripod.",
            "95.06 “bu faslın diğer pozisyonlarında yer almayan” spor eşyasıdır; oyuncak spor takımları 95.03’e, bowling ve masa oyunları 95.04’e, eğlence parkı havuzları 95.08’e gider.",
            "Aksam, parça ve aksesuar (Not 3) ait olduğu eşyanın pozisyonunda sınıflandırılır; ama elektrik motoru, transformatör, uzaktan kumanda, kayıt mesnetleri ve genel kullanım parçaları Not 1 ile dışarıdadır.",
            "Önemsiz ölçüde inci, kıymetli taş veya kıymetli metal içeren eşya fasılda kalır (Not 2); yalnız hayvanlar için tasarlanmış oyuncaklar 95.03’e girmez (Not 5).",
        ],
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı yeri verir.",
        "satirlar": [
            ["1", "Not 1’deki dışlamalardan mı? (mum, havai fişek, spor çantası, spor giyimi, spor ayakkabısı veya başlığı, eldiven, çadır, gözlük, düdük, silah, elektrikli çelenk, tripod, bisiklet, drone, kano)", "Kendi pozisyonu (Not 1)"],
            ["2", "Biçimi, şekli veya maddesi itibarıyla yalnızca hayvanlar için mi tasarlanmış?", "95.03 dışı; kendi pozisyonu (Not 5)"],
            ["3", "Gezici sirk, gezici hayvan sergisi, gezici tiyatro; eğlence parkı, su parkı veya panayır eğlencesi mi?", "<b>95.08</b>"],
            ["4", "Video oyun konsolu, bilardo, kumarhane masası, ödeme aracıyla çalışan eğlence makinesi, oyun kağıdı, satranç, dart, langırt, bowling mi?", "<b>95.04</b>"],
            ["5", "Bayram, karnaval, Noel eşyası; sihirbazlık veya şaka-sürpriz eşyası mı?", "<b>95.05</b>"],
            ["6", "Tekerlekli oyuncak (üç tekerlekli bisiklet, skuter, pedallı araba), oyuncak bebek, diğer oyuncak, eğlencelik model veya bulmaca mı?", "<b>95.03</b>"],
            ["7", "Olta takımı, el kepçesi, kelebek ağı veya yapma av kuşu mu?", "<b>95.07</b>"],
            ["8", "Kültürfizik, jimnastik, atletizm, spor veya açık hava oyunu eşyası; yüzme veya oyun havuzu mu?", "<b>95.06</b>"],
            ["9", "Yukarıdakilerden birinin yalnızca veya esas itibarıyla kullanılan aksamı mı?*", "Eşyanın pozisyonu (Not 3)"],
        ],
        "dipnot": "* Not 1 saklıdır: Bölüm XV Not 2’deki genel kullanım parçaları, plastikten benzerleri, elektrik motorları (85.01), transformatörler (85.04), uzaktan kumandalar (85.26 / 85.43) ve kayıt mesnetleri (85.23) aksam olsa da fasıl dışındadır.",
    },
    "pozisyon_haritasi": [
        ["95.01 / 95.02", "Boş pozisyonlar", "Cetvelde köşeli parantez içinde; metni yok", "—"],
        ["95.03", "Tekerlekli oyuncaklar, oyuncak bebekler, diğer oyuncaklar, scale modeller, bulmacalar",
         "Esas amaç eğlence; hayvanlara mahsus olanlar hariç", "Üç tekerlekli bisiklet, pedallı araba, uçurtma, oyuncak tren, puzzle"],
        ["95.04", "Video oyun konsolları, bilardo, kumarhane masaları, salon-masa oyunları, ödeme araçlı eğlence makineleri",
         "Bulmacalar hariç", "Konsol, isteka, iskambil, satranç, dart, langırt"],
        ["95.05", "Bayram, karnaval, eğlence eşyası; sihirbazlık ve sürpriz eşyası",
         "Genellikle dayanıksız madde; fayda eşyası hariç", "Suni Noel ağacı, konfeti, maske, aksırtma tozu"],
        ["95.06", "Kültürfizik, jimnastik, atletizm, spor ve açık hava oyunu eşyası; havuzlar",
         "Fasılın diğer pozisyonlarında yer almayanlar", "Kayak, sörf, golf, raket, top, paten, kızak"],
        ["95.07", "Olta takımları; el kepçeleri, kelebek ağları; yapma av kuşları",
         "92.08 ve 97.05 hariç", "Olta kamışı, iğne, makara, suni yem, şamandıra"],
        ["95.08", "Gezici sirk ve hayvan sergileri; eğlence parkı ve su parkı eşyası; panayır eşyası; gezici tiyatrolar",
         "Not 6 tanımları; esaslı unsurlar tam", "Hız treni, atlıkarınca, çarpışan araba, atış standı"],
    ],
    "notlar": [
        ["Fasıl 95 Not 1 (a)–(h)",
         "Fasıl dışı: (a) mumlar (34.06); (b) havai fişek ve diğer pirotekni eşyası (36.04); (c) balık avı için uzunlamasına kesilmiş fakat olta haline getirilmemiş iplik, monofilament, misina, kaytan (Fasıl 39, 42.06, Bölüm XI); (d) spor çantaları ve diğer taşıma eşyası (42.02, 43.03, 43.04); (e) dokumaya elverişli maddeden karnaval giyim eşyası ile spor ve özel giyim eşyası, pedli koruyucu bileşen içersin içermesin (eskrim kıyafeti, futbol kaleci pantolonu) (Fasıl 61, 62); (f) tekstil bayrak, flama ve yelkenler (Fasıl 63); (g) spor ayakkabıları (buz pateni veya tekerlekli patenler hariç) (Fasıl 64) ve spor başlıkları (Fasıl 65); (h) baston, kırbaç, kamçı (66.02) ve aksamı (66.03)."],
        ["Fasıl 95 Not 1 (ij)–(m)",
         "(ij) oyuncak bebeklere veya diğer oyuncaklara mahsus takılmamış cam gözler (70.18); (k) Bölüm XV Not 2’deki adi metalden genel kullanıma mahsus aksam ve plastikten benzeri eşya (Fasıl 39); (l) ziller, gonklar (83.06); (m) sıvı pompaları (84.13), filtre-arıtma cihazları (84.21), elektrik motorları (85.01), transformatörler (85.04), disk, bant, katı hal depolama aleti, akıllı kart ve diğer kayıt mesnetleri (85.23), uzaktan kumanda aletleri (85.26) ve kablosuz kızılötesi uzaktan kumandalar (85.43)."],
        ["Fasıl 95 Not 1 (n)–(z)",
         "(n) Bölüm XVII’deki spor taşıtları (kızaklar, yarış kızakları ve benzerleri hariç); (o) çocuk bisikletleri (87.12); (p) insansız hava taşıtları (88.06); (q) spor deniz taşıtları (kano, kayık) (Fasıl 89) ve bunları harekete geçiren tertibat (ahşapsa Fasıl 44); (r) spor ve açık hava oyunları için gözlükler, koruyucu gözlükler (90.04); (s) düdükler ve avcı düdükleri (92.08); (t) Fasıl 93’teki silahlar; (u) her tür elektrikli çelenk (94.05); (v) monopod, bipod, tripod (96.20); (y) raket telleri, çadırlar ve diğer kamp eşyası, eldivenler (maddesine göre); (z) sofra ve mutfak takımları, tuvalet eşyası, halılar, giyim eşyası, yatak, masa, tuvalet ve mutfak örtüleri gibi fayda sağlayan eşya (maddesine göre)."],
        ["Fasıl 95 Not 2",
         "Önemsiz sayılacak ölçüde tabii veya kültür incisi, kıymetli veya yarı kıymetli taş (tabii, sentetik, terkip), kıymetli metal veya kıymetli metal kaplama içeren eşya bu fasıla dahildir (Fasıl 71 de bu eşyayı kapsamaz)."],
        ["Fasıl 95 Not 3",
         "Not 1 saklı kalmak şartıyla, sadece veya esas itibarıyla bu fasıl eşyasıyla kullanılmaya elverişli aksam, parça ve aksesuar ait olduğu eşyanın pozisyonunda sınıflandırılır."],
        ["Fasıl 95 Not 4",
         "Not 1 saklı kalmak şartıyla 95.03; GYK 3(b)’ye göre set sayılmayan ve ayrı geldiklerinde başka pozisyonlara giren eşyalarla birleştirilmiş oyuncakları, <b>perakende satış</b> için bir araya getirilmiş olmaları ve <b>oyuncağın mümeyyiz vasfını</b> taşımaları şartıyla kapsar (ör. oyuncak + küçük promosyon eşyası veya az miktarda şekerleme)."],
        ["Fasıl 95 Not 5",
         "Biçimi, şekli veya yapıldığı maddeye dayanılarak münhasıran hayvanlar için tasarlandığı anlaşılan eşya (evcil hayvan oyuncakları) 95.03’e girmez; kendi uygun pozisyonunda sınıflandırılır."],
        ["Fasıl 95 Not 6",
         "95.08 anlamında: (a) <b>eğlence parkı gezinti eşyası</b>: kişiyi su yolları dahil sabit veya sınırlı bir parkurda ya da eğlence için tanımlanmış alanda taşıyan veya yönlendiren cihaz; konut ve oyun alanlarında yaygın kurulan ekipman hariç; (b) <b>su parkı eğlence eşyası</b>: amaçla inşa edilmiş yolu olmayan, su içeren belirli alanla karakterize cihaz; yalnız su parkları için tasarlanmış ekipman; (c) <b>fuar alanı eğlence eşyası</b>: genellikle bir operatör kullanan, kalıcı binalara veya bağımsız imtiyaz tezgahlarına kurulabilen şans, güç veya beceri oyunları; 95.04 teçhizatı hariç. Başka yerde daha özel sınıflandırılan teçhizat 95.08’e girmez."],
        ["95.03 Açıklama Notu",
         "Tekerlekli oyuncaklar: üç tekerlekli çocuk bisikletleri (87.12 bisikletleri hariç), gençler ve yetişkinler için de tasarlanmış skuterler, pedallı arabalar, motorlu çocuk arabaları. Oyuncak bebek arabaları ve pusetler; dekoratif ve kukla bebekler dahil oyuncak bebekler ve bunların aksamı (cam gözler hariç). Eğitici oyuncaklar (kimya, matbaa, dikiş takımları), oyuncak müzik aletleri, oyun çadırları, eğlencelik modeller ve her çeşit bulmaca."],
        ["95.03 Açıklama Notu (hariç)",
         "Çocuk boyaları (32.13), oyun hamuru (34.07), resim-boyama kitapları (49.03), çıkartmalar (49.08), ziller (83.06), insansız hava taşıtları (88.06), oyuncak bebek figürüyle birleşik müzik kutuları (92.08), oyun kağıtları (95.04), kağıt şapka ve maskeler (95.05), pastel ve mum boyalar (96.09), taş ve kara tahtalar (96.10), vitrin modelleri ve otomatlar (96.18)."],
        ["95.04 Açıklama Notu",
         "Esas işlevi oyun olan video oyun konsolları, 84. Fasıl Not 5(A) şartlarını sağlasın sağlamasın buradadır; kasalar, oyun kasetleri, kumandalar, direksiyonlar dahil. Hariç: 84. Fasıl Not 5(C)’yi sağlayan klavye, fare, depolama birimi (Bölüm XVI); oyun yazılımı kaydedilmiş optik diskler (85.23); mekanik sayaçlar (90.29); piyango biletleri (49.11); bulmacalar (95.03)."],
        ["95.05 Açıklama Notu",
         "Genellikle dayanıklı olmayan maddeden bayram, karnaval, Noel eşyası; maskeler, kağıt şapkalar, konfeti; sihirbazlık ve şaka eşyası. Hariç: hakiki Noel ağaçları (Fasıl 6), mumlar (34.06), ambalaj malzemesi (Fasıl 39 veya 48), Noel ağacı dayanakları (maddesine göre), tekstil bayraklar (63.07), elektrikli çelenkler (94.05), tapınak heykelleri ve bayram motifli fayda eşyası."],
        ["95.06 Açıklama Notu",
         "Jimnastik ve atletizm aletleri, kayak, su sporu, golf, masa tenisi, raketler, toplar, patenler (paten takılı botlar dahil), koruyucu spor malzemeleri, çocuk bahçesi aletleri, kızaklar, yüzme ve oyun havuzları. Hariç: spor eldivenleri (genellikle 42.03), taşıma ve saha fileleri (56.08), tüplü teneffüs aletleri (90.20), mekano-terapi cihazları (90.19), bowling malzemeleri (95.04), eğlence parkı aktivite ve dalga havuzları (95.08)."],
        ["95.07 ve 95.08 Açıklama Notları",
         "95.07: olta iğneleri, kepçeler, olta kamışları ve takımları, yapma av kuşları ve tarlakuşu aynaları; av tuzakları maddesine göre, traplar 95.06. 95.08: eğlence eşyası normal çalışması için gerekli esaslı unsurları içeriyorsa buradadır; yardımcı eşya (çadır, hayvan, jeneratör, oturak) birlikte gelirse dahil, ayrı gelirse kendi pozisyonunda. Ödeme aracıyla çalışan eğlence makineleri 95.04’tedir."],
    ],
    "sinir_komsulari": [
        ["İki tekerlekli çocuk bisikleti", "87.12", "Not 1(o); üç tekerlekli çocuk bisikleti ise 95.03 (Fasıl 87 Not 4)"],
        ["Gerçek bebek arabası, puset", "87.15", "Oyuncak bebek arabası ise 95.03"],
        ["İnsansız hava taşıtı (drone)", "88.06", "Not 1(p); yalnız eğlence amaçlı uçan oyuncak ise 95.03"],
        ["Kano, kayık; ahşap kürek", "Fasıl 89 / Fasıl 44", "Not 1(q); kızak ise 95.06"],
        ["Spor ayakkabısı, spor başlığı", "Fasıl 64 / Fasıl 65", "Not 1(g); paten takılı bot ise 95.06"],
        ["Spor eldiveni, boks eldiveni", "42.03 (genellikle)", "Not 1(y): maddesine göre"],
        ["Eskrim kıyafeti, kaleci pantolonu (tekstil)", "Fasıl 61 / 62", "Not 1(e); eskrim maskesi ise 95.06"],
        ["Spor çantası, olta kamışı kılıfı", "42.02 / 43.03 / 43.04", "Not 1(d)"],
        ["Yüzücü ve kayak gözlüğü", "90.04", "Not 1(r); oyuncak gözlük 95.03, karnaval gözlüğü 95.05"],
        ["Avcı düdüğü, öten tuzak nesnesi", "92.08", "Not 1(s); yapma av kuşu ise 95.07"],
        ["Elektrikli çelenk (Noel ışıkları)", "94.05", "Not 1(u)"],
        ["Mum; havai fişek", "34.06 / 36.04", "Not 1(a), (b)"],
        ["Oyun hamuru; çocuk boyası; pastel boya", "34.07 / 32.13 / 96.09", "95.03 Açıklama Notu hariç tutmaları"],
        ["Kamp çadırı; tripod", "63.06 / 96.20", "Not 1(y), (v); çocuk oyun çadırı ise 95.03"],
        ["Takılmamış, mekanizmasız cam bebek gözü", "70.18", "Not 1(ij); açılıp kapanan mekanizmalı göz 95.03"],
    ],
    "tuzaklar": [
        "<b>Üç tekerlekli çocuk bisikleti oyuncaktır, iki tekerlekli çocuk bisikleti değildir.</b> Üç tekerlekli 95.03; diğer çocuk bisikletleri 87.12 (Not 1(o), Fasıl 87 Not 4).",
        "<b>Paten takılı bot spor eşyasıdır.</b> Buz veya tekerlekli patenli bot 95.06’dadır; patensiz spor ayakkabısı Fasıl 64’te kalır.",
        "<b>Kızak Fasıl 95’te, kano Fasıl 89’da.</b> Not 1(n) spor taşıtlarını dışlarken kızakları ayrıca istisna tutar; spor deniz taşıtları ise Not 1(q) ile dışarıdadır.",
        "<b>Oyuncak drone ≠ insansız hava taşıtı.</b> Yalnızca eğlence için tasarlanmış uçan oyuncak 95.03’te; faydacı işlevli insansız hava taşıtı 88.06’da.",
        "<b>Oyun kağıdı 95.04, bulmaca 95.03.</b> 95.04 bulmacaları dışlar; 95.03 de oyun kağıtlarını 95.04’e gönderir. Sihirbazlık için özel yapılmış kağıtlar ise 95.05’tir.",
        "<b>Noel süsü olsa da elektrikli çelenk 94.05’tir.</b> Hakiki Noel ağacı Fasıl 6, mum 34.06, Noel ağacı dayanağı maddesine göre.",
        "<b>Evcil hayvan oyuncağı 95.03 değildir.</b> Münhasıran hayvanlar için tasarlandığı anlaşılan eşya kendi pozisyonuna gider (Not 5).",
        "<b>Konsol 84.71 şartlarını sağlasa da 95.04’tür.</b> Ancak oyun yazılımı yüklü optik disk 85.23’te; klavye, fare, depolama birimi Bölüm XVI’da kalır.",
        "<b>Yüzme havuzu 95.06, su parkı dalga havuzu 95.08.</b> Çocuk bahçesi salıncağı 95.06, lunapark salıncağı 95.08 (Not 6(a)).",
        "<b>Bayram desenli fayda eşyası 95.05 değildir.</b> Noel motifli masa örtüsü, tabak, havlu maddesine göre sınıflandırılır (Not 1(z)).",
    ],
    "hafiza": {
        "kanca": "3 OYUNCAK – 4 MASA – 5 BAYRAM – 6 SPOR – 7 OLTA – 8 LUNAPARK",
        "aciklama": "Son rakamı sırayla sayın: 95.0<b>3</b> çocuk odası, 95.0<b>4</b> oyun salonu ve konsol, 95.0<b>5</b> parti ve sihirbaz, 95.0<b>6</b> spor salonu ve kayak pisti, 95.0<b>7</b> göl kıyısı, 95.0<b>8</b> lunapark. Bir eğlence gününü sabahtan akşama yaşar gibi düşünün; ama kapıda Not 1 bekçisi durur: mum, çanta, ayakkabı, eldiven, gözlük, düdük, bisiklet ve kano içeri giremez.",
    },
    "sinav_odagi": [
        "Bu fasıl çıkmış sorularda sınırlı sayıda ve çoğunlukla seçeneklerde veya çeldirici olarak yer almıştır; doğrudan sorulan konular tekerlekli oyuncaklar ve patenlerdir.",
        "Üç tekerlekli bisikletin 95.03’te sınıflandırıldığı ve 87.12’nin (çocuk bisikletleri) çeldirici olduğu sorular; “gezici hayvan sergileri ile aynı fasılda” kalıbında üç tekerlekli bisikletin orijinal heykel, zooloji koleksiyonu, tiyatro dekoru ve kamp çadırı arasından seçilmesi.",
        "Tabanına sökülemeyecek şekilde tekerlek yerleştirilmiş ayakkabının paten olarak 95.06’ya gitmesi; spor ayakkabısı kavramının (güreş, kayak, bisiklet ayakkabısı) Fasıl 64 ile karşılaştırılması.",
        "Not 1 dışlamaları: elektrikli çelengin 94.05’te olduğu, 95.04’ün çeldirici olarak verildiği sorular.",
        "Başka fasılların “hangisi bu fasılda sınıflandırılır” sorularında Fasıl 95 eşyasının çeldirici olması: mantardan dart tablası (Fasıl 45 dışı), kayak merkezinde kullanılacak tabii kar (22.01, 95.06 çeldirici), golf arabası (Fasıl 87).",
    ],
    "cikmis_ornekler": [
        {
            "soru": "Üç tekerlekli bisikletler, Türk Gümrük Tarife Cetvelinde hangi tarife pozisyonunda sınıflandırılır?",
            "secenekler": ["95.03", "84.79", "87.12", "87.15"],
            "cevap": "A",
            "aciklama": "95.03 pozisyon metni üç tekerlekli bisikletleri adıyla sayar; Fasıl 87 Not 4 ve Fasıl 95 Not 1(o) yalnızca diğer çocuk bisikletlerini 87.12’ye gönderir. 87.15 bebek arabalarına aittir.",
        },
        {
            "soru": "Elektrikli çelenk isimli eşya, Tarife Cetvelinde hangi tarife pozisyonunda sınıflandırılır?",
            "secenekler": ["94.05", "95.04", "85.39", "84.79"],
            "cevap": "A",
            "aciklama": "Fasıl 95 Not 1(u) her tür elektrikli çelengi fasıl dışında bırakarak 94.05’e gönderir; 95.05 Açıklama Notu da Noel süsü niteliğindeki elektrikli çelenkleri hariç tutar.",
        },
    ],
    "ozet": [
        "Önce Not 1: mum, havai fişek, spor çantası, spor giyimi, ayakkabısı ve başlığı, eldiven, çadır, gözlük, düdük, bisiklet, drone, kano, silah, elektrikli çelenk ve tripod Fasıl 95 dışındadır.",
        "95.03 oyuncaktır: üç tekerlekli bisiklet, pedallı araba, oyuncak bebek, eğlencelik model, bulmaca; yalnız hayvanlara mahsus olanlar hariç.",
        "95.04 salon, masa ve kumarhane oyunları ile video oyun konsollarıdır; oyun kağıtları da buradadır.",
        "95.05 bayram, karnaval, Noel, sihirbazlık ve şaka eşyasıdır; fayda eşyası ve elektrikli çelenk hariç.",
        "95.06 fasılın artık spor pozisyonudur; paten takılı bot, kızak, şnorkel ve yüzme havuzu dahil.",
        "95.07 olta ve av levazımatı; 95.08 gezici sirk, eğlence parkı, su parkı, panayır ve gezici tiyatro.",
        "Aksam ait olduğu eşyayı izler (Not 3); elektrik motoru, uzaktan kumanda ve genel kullanım parçaları hariç.",
    ],
    "sorular": sorular,
}

if __name__ == "__main__":
    out = os.path.join(KITAP, "data", "fasil_95.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    print("yazıldı:", out)
