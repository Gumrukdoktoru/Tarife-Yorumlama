#!/usr/bin/env python3
"""Fasıl 97 modülü üreteci."""
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
    S("Tarife Cetveline göre, bir ressamın tuval üzerine tamamen elle yaptığı, ünlü bir yağlıboya tablonun kopyası hangi pozisyonda sınıflandırılır?",
      "97.01", ["49.11", "97.06", "49.06", "59.07"], "D", EP,
      "97.01 Açıklama Notuna göre orijinal resimlerin tamamen elle yapılmış kopyaları, sanatsal değeri ne olursa olsun bu pozisyonda kalır; yalnızca fotomekanik usullerle yapılan resimler ve basılı çizgiler üzerine elle tamamlananlar hariçtir. 49.06 mimari, mühendislik ve benzeri amaçlı planlara, 59.07 tiyatro dekoru tuvallerine aittir.",
      "97.01 Açıklama Notu (A)."),
    # 2 EP
    S("Tarife Cetveline göre, eskiliği 150 yıl olan, ceviz ağacından oymalı antika konsol (mobilya) hangi pozisyonda sınıflandırılır?",
      "97.06", ["94.03", "44.20", "97.03", "97.05"], "B", EP,
      "97.06, eskiliği 100 yılı aşan ve 97.01–97.05’e girmeyen antika eşyayı kapsar; antika mobilyalar Açıklama Notunda ilk örnektir. Not 5(A) uyarınca Fasıl 97’ye giren eşya başka fasılda (94.03, 44.20) sınıflandırılmaz. Mobilya orijinal heykel eseri (97.03) veya koleksiyon numunesi (97.05) değildir.",
      "Fasıl 97 Not 5(A); 97.06 Açıklama Notu (1)."),
    # 3 EP
    S("Tarife Cetveline göre, koleksiyon amacıyla cam çerçeveli kutular içine yerleştirilmiş, süs eşyası veya taklit mücevher olarak monte edilmemiş kurutulmuş kelebek ve böcekler hangi pozisyonda sınıflandırılır?",
      "97.05", ["05.11", "96.01", "71.17", "97.06"], "E", EP,
      "97.05 Açıklama Notu (B), kutu veya cam çerçeve içindeki böcekleri zoolojik koleksiyon eşyası olarak sayar; yalnızca taklit mücevher veya ufak süs eşyası oluşturmak için monte edilenler hariçtir. 05.11 işlenmemiş diğer hayvansal ürünlere, 97.06 ise 97.01–97.05’e girmeyen antikalara aittir.",
      "97.05 Açıklama Notu (B)(2)."),
    # 4 EP
    S("Tarife Cetveline göre, bir koleksiyoncunun getirdiği, posta damgası vurulmuş kullanılmış posta pullarından oluşan ve pul koleksiyonları için olağan değerde bir albüm içinde sunulan pul koleksiyonu hangi pozisyonda sınıflandırılır?",
      "97.04", ["49.07", "48.20", "97.05", "49.11"], "A", EP,
      "97.04 kullanılmış olsun olmasın posta pullarını kapsar; pullar tek tek veya koleksiyon halinde gelebilir. Pul koleksiyonlarına ait albümler, koleksiyon için mutat değerdeyse koleksiyonun aksamı sayılır ve birlikte sınıflandırılır; bu yüzden 48.20 uygulanmaz. 49.07 yalnızca itibari değeri tanınan kullanılmamış pullara aittir; pullar 97.05’te değil kendi özel pozisyonları olan 97.04’tedir.",
      "97.04 Açıklama Notu; Fasıl 97 Not 1(a)."),
    # 5 EP
    S("Tarife Cetveline göre, bir sanatçının kendi eliyle hazırladığı bakır levhadan, mekanik veya fotomekanik bir usul kullanılmadan doğrudan basılmış sınırlı sayıdaki siyah-beyaz gravür hangi pozisyonda sınıflandırılır?",
      "97.02", ["49.11", "97.01", "84.42", "49.06"], "C", EP,
      "Not 3’e göre orijinal gravür, sanatçının tamamen elle yaptığı bir veya daha fazla levhadan mekanik veya fotomekanik usul olmaksızın doğrudan elde edilen renkli veya siyah-beyaz baskıdır ve 97.02’dedir. Baskıda kullanılan levha (klişe) ise 84.42’ye girer. 97.01 elle yapılmış resimlere, 49.06 planlara aittir.",
      "Fasıl 97 Not 3; 97.02 Açıklama Notu."),
    # 6 OT
    S("Aşağıdakilerden hangisi Tarife Cetvelinin 97. faslında <b>sınıflandırılmaz</b>?",
      "100 yılı aşkın, ipliğe dizilmemiş tabii inciler",
      ["Heykeltıraşın elinden çıkmış orijinal bronz heykel", "Posta pulu taşıyan ve ilk gün damgası vurulmuş zarf",
       "Eskiliği 100 yılı aşan, el dokuması yün duvar halısı", "Paleontolojik değeri olan, koleksiyonluk amonit fosili"], "B", OT,
      "Not 1(c) tabii veya kültür incilerini ve kıymetli-yarı kıymetli taşları Fasıl 97 dışında bırakır (71.01–71.03); 97.06 Açıklama Notu da bunların eskiliklerine bakılmaksızın hariç olduğunu belirtir. Orijinal heykel 97.03’te, pullu ilk gün zarfı 97.04’te, antika halı 97.06’da, fosil 97.05’tedir.",
      "Fasıl 97 Not 1(c); 97.06 Açıklama Notu, son paragraf."),
    # 7 OT
    S("Aşağıdakilerden hangisi 97.01 pozisyonunda <b>sınıflandırılmaz</b>?",
      "Elle boyanmış seramik vazo",
      ["Kağıt üzerine pastel resim", "Kömürle yapılmış karakalem resim",
       "Elle yapılmış, ticari karakter taşımayan mermer mozaik", "Bitki ve hayvan maddeleri yapıştırılarak oluşturulmuş kolaj"], "E", OT,
      "97.01 pozisyon metni ve Açıklama Notu, elle boyanmış veya elle dekore edilmiş fabrikasyon ürünleri (seramik vazo ve tabaklar, hatıra eşyası, kutular) hariç tutar; bunlar kendi pozisyonlarında sınıflandırılır. Pastel ve karakalem resimler, ticari nitelikte olmayan el yapımı mozaikler ve kolajlar 97.01’dedir.",
      "97.01 pozisyon metni; 97.01 Açıklama Notu, hariç tutma (d) ve (B) grubu."),
    # 8 OT
    S("Aşağıdakilerden hangisi 97.05 pozisyonunda <b>sınıflandırılmaz</b>?",
      "Hediyelik kutuda satılan, yasal para birimi olan madeni para",
      ["Osteolojik numune olarak müzeye gönderilen insan kafatası", "Paleontolojik değeri olan, kazıda bulunmuş dinozor fosili",
       "Etnografik değeri olan, elle yazılmış eski bir dini metin", "Arkeolojik kazıda ortaya çıkarılmış, üzeri yazılı kil tablet"], "D", OT,
      "97.05 Açıklama Notuna göre çıkarıldığı ülkede yasal para birimi olan metal paralar, hediyelik kutularda genel satışa sunulsalar bile 71.18’dedir. Osteolojik ve paleontolojik numuneler, etnografik değerdeki el yazmaları ve arkeolojik yazılı tabletler 97.05’te sayılır.",
      "97.05 Açıklama Notu (A), (B), (C)."),
    # 9 OT
    S("Aşağıdakilerden hangisi 97.04 pozisyonunda <b>sınıflandırılmaz</b>?",
      "Pul şeklindeki tenzilat kuponları",
      ["Kullanılmış posta pulları", "Posta pulu taşıyan ilk gün zarfları",
       "Posta pulu taşıyan maksimum kartlar", "Kullanılmış makbuz (damga) pulları"], "A", OT,
      "Özel veya ticari teşekküllerin çıkardığı tasarruf pulları ve perakendecilerin pul şeklindeki tenzilat kuponları 97.04 Açıklama Notunda hariç tutulmuştur (49.11). Kullanılmış posta ve damga pulları, posta pulu taşıyan ilk gün zarfları ve maksimum kartlar 97.04’tedir; pulsuz ilk gün ve maksimum kartları ise 48.17 veya Fasıl 49’a gider.",
      "97.04 Açıklama Notu ve hariç tutmalar (a), (c)."),
    # 10 FA
    S("Aşağıdakilerden hangisi diğerlerinden farklı bir fasılda sınıflandırılır?",
      "Mimari amaçla elle çizilmiş orijinal bina planı",
      ["Sanatçının elle hazırladığı taştan basılmış orijinal litografya", "Heykeltıraşın mermerden yonttuğu orijinal heykel", "Elle yapılmış yağlıboya portre",
       "Eskiliği 100 yılı aşan antika duvar saati"], "C", FA,
      "Sanayi, mimari veya mühendislik amaçları için elle çizilmiş orijinal planlar ve çizimler 97.01’den hariç tutulmuştur ve 49.06’dadır (Fasıl 49). Litografya 97.02, heykel 97.03, yağlıboya portre 97.01, antika saat 97.06 ile Fasıl 97’dedir.",
      "97.01 Açıklama Notu, hariç tutma (a); 97.02, 97.03, 97.06 pozisyon metinleri."),
    # 11 FA
    S("Eskiliği 120 yıl olan aşağıdaki eşyadan hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır?",
      "Orijinal yağlıboya tablo", ["Ceviz ağacından oymalı sandık", "Gümüşten işlemeli şamdan", "El dokuması yün halı", "Sarkaçlı ahşap duvar saati"], "A", FA,
      "Not 5(B) uyarınca 97.06, fasılın önceki pozisyonlarındaki eşyaya uygulanmaz; Genel Açıklamalar da 97.01–97.05 eşyasının 100 yıldan eski olsa bile kendi pozisyonunda kalacağını belirtir. Bu nedenle tablo 97.01’de kalır; sandık, şamdan, halı ve saat 97.06’daki antikalardır.",
      "Fasıl 97 Not 5(B); Fasıl 97 Genel Açıklamalar; 97.06 Açıklama Notu."),
    # 12 FA
    S("Aşağıdaki eşya çiftlerinden hangisinde her iki eşya da aynı pozisyonda sınıflandırılır?",
      "Herbaryum (kurutulmuş ot koleksiyonu) – Mineral numunesi",
      ["Orijinal heykel – Seri üretim alçı heykelcik",
       "Orijinal gravür – Gravürün basıldığı bakır levha",
       "Kullanılmış posta pulu – Tedavüldeki kullanılmamış posta pulu",
       "Antika vazo – Eskiliği 100 yılı aşan orijinal yağlıboya tablo"], "E", FA,
      "Kurutulmuş ot koleksiyonları ve mineral numuneleri (Fasıl 71’deki kıymetli taşlar hariç) 97.05’te birlikte yer alır. Diğer çiftler ayrılır: orijinal heykel 97.03, seri üretim heykelcik maddesine göre; gravür 97.02, levha 84.42; kullanılmış pul 97.04, tedavüldeki kullanılmamış pul 49.07; antika vazo 97.06, eski tablo 97.01.",
      "97.05 Açıklama Notu (B)(3), (4); Fasıl 97 Not 1(a), 4, 5(B)."),
    # 13 FA
    S("Aşağıdakilerden hangisi “zooloji koleksiyonu için içi doldurulmuş hayvan” ile aynı pozisyonda sınıflandırılır?",
      "Taç giyme töreninde kullanılmış tarihi kraliyet amblemi",
      ["Heykeltıraşın elinden çıkmış orijinal bronz büst", "Eskiliği 100 yılı aşan, kristal sarkaçlı antika avize", "Tiyatro sahnesinin dekoru için boyanmış büyük tuval",
       "Tedavülden kalkmış, koleksiyon eşyası sayılmayan kağıt para"], "D", FA,
      "İçi doldurulmuş hayvanlar zoolojik, önemli tarihi olaylarla ilgili kraliyet amblemi ise tarihi değerdeki koleksiyon eşyası olarak 97.05’tedir. Orijinal büst 97.03’te, antika avize 97.06’da, tiyatro dekoru tuvali Not 1(b) uyarınca 59.07’de, koleksiyon eşyası sayılmayan tedavülden kalkmış kağıt para 49.07’dedir.",
      "97.05 Açıklama Notu (A), (B)(1), (C); Fasıl 97 Not 1(b)."),
    # 14 TN
    S("Fasıl 97 Not 3’e göre, 97.02 pozisyonu anlamında “orijinal gravürler, estamplar ve litograflar” tabiri ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
      "Mekanik veya fotomekanik usul olmaksızın, sanatçının elle yaptığı levhadan doğrudan alınan renkli veya siyah-beyaz baskılardır.",
      ["Yalnızca siyah-beyaz baskılar orijinal sayılır; renkli baskılar, levha sanatçı tarafından elle hazırlanmış olsa bile bu tanıma girmez.",
       "Fotomekanik usulle çoğaltılan baskılar, sanatçı tarafından tek tek imzalanıp numaralandırılmışsa orijinal sayılır.",
       "Sanatçının baskı üzerinde sonradan rötuş yaptığı nüshalar orijinal sayılmaz ve 97.01’de sınıflandırılır.",
       "Baskıda kullanılan bakır veya taş levhalar da bu tanıma girer ve baskılarla birlikte 97.02’de sınıflandırılır."], "B", TN,
      "Not 3’e göre kullanılan usul ve madde ne olursa olsun, mekanik ve fotomekanik usuller hariç olmak üzere sanatçının tamamen elle yaptığı levhalardan doğrudan alınan renkli veya siyah-beyaz baskılar orijinaldir. Açıklama Notu rötuşlu orijinalleri ve transfer tekniğiyle elde edilen litografyaları da kapsar; levhalar (klişeler) ise 84.42’dedir.",
      "Fasıl 97 Not 3; 97.02 Açıklama Notu."),
    # 15 TN
    S("Fasıl 97 Not 5 ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
      "97.06 pozisyonu, bu fasılın 97.01 ila 97.05 pozisyonlarında yer alan eşyaya uygulanmaz.",
      ["Eskiliği 100 yılı aşan her eşya, türüne bakılmaksızın 97.06’da sınıflandırılır.",
       "Fasıl 97 eşyası, başka bir fasılda daha özel bir pozisyon bulunuyorsa o fasılda sınıflandırılır.",
       "Not 5 hükmü, Not 1 ila 4’teki dışlamalara göre önceliklidir.",
       "Bir eşyanın 97.06’da sınıflandırılabilmesi için eskiliğinin 250 yılı aşması gerekir."], "C", TN,
      "Not 5(A), Not 1–4 hükümleri saklı kalmak şartıyla fasıl eşyasının başka bir fasılda değil bu fasılda sınıflandırılacağını; Not 5(B) ise 97.06’nın önceki pozisyonlardaki eşyaya uygulanmayacağını öngörür. Bu yüzden 100 yılı aşan bir tablo 97.01’de kalır. 97.06 için eşik 100 yıldır; 250 yıl yalnızca altpozisyon ayrımıdır.",
      "Fasıl 97 Not 5(A), 5(B); 97.06 pozisyon metni."),
    # 16 TN
    S("Fasıl 97 Not 6’ya göre, tamamen elle yapılmış yağlıboya bir tablonun çerçevesi ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
      "Mahiyet ve kıymet itibarıyla tabloya uygunsa tabloyla birlikte sınıflandırılır; uygun değilse ayrı sınıflandırılır.",
      ["Her durumda tabloyla birlikte 97.01’de sınıflandırılır.",
       "Her durumda yapıldığı maddeye göre ayrı sınıflandırılır.",
       "Yalnızca tablo 100 yaşını aşmışsa tabloyla birlikte sınıflandırılır.",
       "Çerçevenin değeri tablonun değerini aşıyorsa tablo da çerçeveyle birlikte çerçevenin yapıldığı maddenin pozisyonunda sınıflandırılır."], "A", TN,
      "Not 6, yağlıboya, karakalem ve pastel resimler, kolajlar, gravürler vb. ile birlikte gelen çerçevelerin mahiyet ve kıymet itibarıyla eserin değerine uygunsa onunla birlikte, değilse ayrı sınıflandırılacağını hükme bağlar; uygun olmayan çerçeveler ağaçtan, metalden vb. eşya olarak kendi pozisyonlarına gider. Not, tablonun yaşına göre bir ayrım yapmaz ve tablonun yerini değiştirmez.",
      "Fasıl 97 Not 6; 97.01 Açıklama Notu, çerçeveler paragrafı."),
    # 17 TN
    S("97.05 pozisyonu Açıklama Notuna göre nümizmatik değeri olan metal paralar ve madalyalar ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
      "Tek tek getirilenler, her neviden birkaç adedi geçmemek ve koleksiyon amacı açıkça belli olmak şartıyla 97.05’tedir.",
      ["Aynı cinsten büyük miktarlarda getirilen metal paralar da nümizmatik değer taşıdıkları kabul edilerek 97.05’te yer alır.",
       "Mücevherci eşyası olarak monte edilmiş metal paralar her durumda 97.05’te kalır.",
       "Yalnızca maden elde etmeye elverişli olacak şekilde bükülmüş veya zedelenmiş paralar 97.05’te yer alır.",
       "Çıkarıldığı ülkede yasal para birimi olan metal paralar, hediyelik kutularda genel satışa sunulduklarında 97.05’te sınıflandırılır."], "E", TN,
      "97.05 Açıklama Notu, bağımsız parça olarak getirilen metal para ve madalyaları her neviden birkaç adedi geçmemesi ve koleksiyon amacı açıkça belli olması şartıyla kabul eder. Aynı cinsten büyük miktarlar genellikle Fasıl 71’e, yalnız maden elde etmeye elverişli bükülmüş paralar ilgili metalin hurda pozisyonuna, yasal para birimi olan paralar hediye kutusunda da 71.18’e, mücevher olarak monte edilenler Fasıl 71 veya 97.06’ya gider.",
      "97.05 Açıklama Notu (C)."),
    # 18 GY
    S("Eskiliği 150 yılı aşan, tamamen elle yapılmış orijinal yağlıboya bir tablo Tarife Cetveline göre hangi gerekçeyle hangi pozisyonda sınıflandırılır?",
      "GYK 1 – 97.01", ["GYK 1 – 97.06", "GYK 3(a) – 97.01", "GYK 3(c) – 97.06", "GYK 4 – 97.06"], "D", GY,
      "Tablo görünüşte hem 97.01’in hem de 97.06’nın kapsamına uysa da çatışmayı Fasıl 97 Not 5(B) çözer: 97.06, fasılın önceki pozisyonlarındaki eşyaya uygulanmaz. Sonuç bir fasıl notundan çıktığı için GYK 1 uygulanır; GYK 3 kurallarına (en özel tanım, en son pozisyon) başvurmaya gerek kalmaz. GYK 4 hiçbir pozisyona girmeyen eşya içindir.",
      "GYK 1; Fasıl 97 Not 5(B); Fasıl 97 Genel Açıklamalar."),
    # 19 GY
    S("Kıymet ve mahiyet bakımından esere uygun, yaldızlı oymalı ahşap çerçevesi içinde sunulan, tamamen elle yapılmış orijinal pastel resmin çerçevesiyle birlikte 97.01 pozisyonunda sınıflandırılması aşağıdakilerden hangisine dayanır?",
      "GYK 1 (Fasıl 97 Not 6)", ["GYK 5(a) (mahfazalar)", "GYK 3(b) (esas karakter)", "GYK 2(a) (eksik eşya)", "GYK 5(b) (ambalajlar)"], "B", GY,
      "Çerçevenin eserle birlikte sınıflandırılması doğrudan Fasıl 97 Not 6’dan kaynaklandığından GYK 1 uygulanır. Çerçeve, eşyayı taşımaya ve saklamaya yarayan bir mahfaza veya ambalaj olmadığından GYK 5(a) ve 5(b) uygulanmaz; not hükmü varken GYK 3(b)’ye de başvurulmaz.",
      "GYK 1; Fasıl 97 Not 6."),
    # 20 ES
    S("Fasıl 97 Not 1’e göre; itibari değeri tanınan kullanılmamış posta veya damga pulları ……… pozisyonunda, tiyatro dekorları için boyanmış tuvaller ……… pozisyonunda, tabii veya kültür incileri ise ……… pozisyonlarında sınıflandırılır. Boşluklara sırasıyla gelmesi gerekenler hangi seçenekte verilmiştir?",
      "49.07 – 59.07 – 71.01 ila 71.03",
      ["97.04 – 59.07 – 71.01 ila 71.03", "49.07 – 97.01 – 71.01 ila 71.03",
       "49.07 – 59.07 – 97.05", "49.11 – 63.07 – 71.01 ila 71.03"], "C", ES,
      "Not 1; (a) 49.07’deki kullanılmamış posta ve damga pullarını, (b) tiyatro dekoru ve atölye fonu olarak boyanmış tuvalleri (97.06’ya girebilecekler hariç 59.07), (c) inci ve kıymetli-yarı kıymetli taşları (71.01–71.03) fasıl dışında bırakır. Pullar ancak 49.07 dışında kalıyorsa 97.04’e girer.",
      "Fasıl 97 Not 1(a), (b), (c)."),
    # 21 ES
    S("Aşağıdaki eşyalar ile sınıflandırıldıkları pozisyonlar doğru eşleştirildiğinde hangi seçenek elde edilir?<br/>I. Orijinal litografya<br/>II. Heykel sanatının orijinal eseri<br/>III. Posta pulu taşıyan ilk gün zarfı<br/>IV. Fosil numunesi",
      "I–97.02, II–97.03, III–97.04, IV–97.05",
      ["I–97.01, II–97.03, III–97.04, IV–97.05",
       "I–97.02, II–97.06, III–97.04, IV–97.05",
       "I–97.02, II–97.03, III–49.07, IV–97.05",
       "I–97.02, II–97.03, III–97.04, IV–97.06"], "E", ES,
      "Orijinal litografyalar 97.02’de, orijinal heykeller 97.03’te, posta pulu taşıyan ilk gün zarfları 97.04’te, fosil numuneleri 97.05’tedir. Çeldiricilerde litografya resimle (97.01), heykel antikayla (97.06), ilk gün zarfı tedavüldeki pullarla (49.07), fosil antikayla (97.06) karıştırılmıştır.",
      "97.02, 97.03, 97.04, 97.05 pozisyon metinleri ve Açıklama Notları."),
    # 22 CC
    S("Aşağıdakilerden hangileri 97.01 pozisyonu <b>dışında</b> kalır?<br/>I. Fotomekanik usulle tuval üzerine yapılmış yağlıboya resim<br/>II. Alelade baskı usulüyle elde edilmiş çizgiler üzerine elle boyanarak yapılmış resim<br/>III. Orijinal bir resmin tamamen elle yapılmış kopyası<br/>IV. Delikli kalıplar yardımıyla elde edilen “hakiki kopyalar”",
      "I, II ve IV", ["I ve II", "II ve III", "I, III ve IV", "II, III ve IV"], "A", CC,
      "97.01 Açıklama Notu, resimlerin tamamen elle yapılmış olmasını şart koşar; fotomekanik usullerle yapılan resimler, basılı çizgiler üzerine elle tamamlananlar ve delikli kalıplarla elde edilen “hakiki kopyalar” (sanatçı onaylı olsa bile) hariçtir. Orijinal resmin tamamen elle yapılmış kopyası ise sanatsal değeri ne olursa olsun 97.01’de kalır.",
      "97.01 Açıklama Notu (A)."),
    # 23 CC
    S("Fasıl 97 ile ilgili aşağıdaki ifadelerden hangileri <b>doğrudur</b>?<br/>I. Tamir veya restore edilmiş antika eşya, orijinal vasfını koruyorsa 97.06’da yer alır.<br/>II. Yeni ağaç üzerine monte edilmiş antika halılar 97.06’da yer alamaz.<br/>III. 71.01 ila 71.03 pozisyonlarındaki inci ve kıymetli taşlar, eskiliklerine bakılmaksızın 97.06 dışında kalır.<br/>IV. 97.06, eskiliği 100 yılı aşan ve 97.01 ila 97.05 pozisyonlarında yer almayan antika eşyayı kapsar.",
      "I, III ve IV", ["I ve II", "II ve III", "I, II ve IV", "II, III ve IV"], "D", CC,
      "97.06 Açıklama Notu, orijinal vasfını koruyan tamir edilmiş antikaları ve yeni ağaç üzerine duvar örtüsü olarak monte edilmiş antika halı ve kilimleri bu pozisyona alır; bu yüzden II yanlıştır. İnci ve kıymetli taşlar eskiliklerine bakılmaksızın hariçtir; pozisyon 97.01–97.05’e girmeyen, 100 yılı aşan antikaları kapsar.",
      "97.06 pozisyon metni ve Açıklama Notu; Fasıl 97 Not 1(c), 5(B)."),
    # 24 SN
    S("Bir heykeltıraş, kilden yaptığı asıl modelden alçı model ve döküm kalıbı hazırlamış; her dökümde bizzat düzeltmeler yaparak bronzdan yalnızca altı nüsha elde etmiş, nüshaların patina tonları birbirinden farklı olmuştur. Bu nüshalardan biri Tarife Cetveline göre hangi pozisyonda sınıflandırılır?",
      "97.03", ["83.06", "74.19", "97.06", "69.13"], "B", SN,
      "97.03 Açıklama Notu, heykeltıraşın kil modelinden kalıp yoluyla, kendisinin veya başka bir sanatçının müdahalesiyle elde edilen ve birbirinin tamamen aynı olmayan sınırlı sayıdaki nüshaları orijinal eser sayar; bu nüshalar nadir haller dışında bir düzineyi geçmez. Ticari karakterli seri üretim metal heykelcikler 83.06’ya gider; eser antika olmadığından 97.06 da söz konusu değildir.",
      "97.03 Açıklama Notu; Fasıl 97 Not 4."),
    # 25 SN
    S("Bir sanatçının tasarladığı modelden fabrikada binlerce adet dökülen ve turistik hediyelik eşya dükkanlarında satılan pirinçten küçük at heykelcikleri Tarife Cetveline göre hangi pozisyonda sınıflandırılır?",
      "83.06", ["97.03", "97.06", "74.19", "71.17"], "C", SN,
      "Not 4’e göre ticari karakterde seri halde üretilen kopyalar veya eserler, sanatçılar tarafından tasarlanmış olsalar bile 97.03 dışında kalır; 97.03 Açıklama Notu bunların maddesine göre, metalden olanların 83.06’da sınıflandırılacağını belirtir. Eser antika olmadığından 97.06, taklit mücevher olmadığından 71.17 de söz konusu değildir.",
      "Fasıl 97 Not 4; 97.03 Açıklama Notu, hariç tutmalar."),
]

obj = {
    "tur": "fasil",
    "fasil": 97,
    "baslik": "Sanat eserleri, kolleksiyon eşyası ve antikalar",
    "bolum": "XXI",
    "oz": {
        "vurgu": "Fasıl 97 üç soruyla çözülür: Eşya gerçekten sanat eseri, pul veya koleksiyon eşyası mı (97.01–97.05)? Değilse eskiliği 100 yılı aşan bir antika mı (97.06)? İkisi de değilse ya da Not 1–4’teki şartları taşımıyorsa, eşya maddesine veya işlevine göre diğer fasıllarda sınıflandırılır. Bir kez Fasıl 97’ye giren eşya başka fasla gitmez (Not 5(A)).",
        "maddeler": [
            "Bölüm XXI yalnızca Fasıl 97’den oluşur; kurallar fasıl notlarındadır.",
            "Sanat eseri olmanın ölçütü “tamamen elle” ve “ticari seri üretim olmama”dır: elle yapılmış resim ve kopyası 97.01, elle hazırlanmış levhadan doğrudan baskı 97.02, orijinal heykel 97.03.",
            "Yaş, sanat eserini antikaya çevirmez: 97.01–97.05 eşyası 100 yaşını aşsa da yerinde kalır; 97.06 artık pozisyondur (Not 5(B)).",
            "Fasıl dışı: itibari değeri tanınan kullanılmamış pullar (49.07), tiyatro dekoru tuvalleri (59.07), inci ve kıymetli taşlar (71.01–71.03, yaşına bakılmaksızın).",
        ],
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı yeri verir.",
        "satirlar": [
            ["1", "Tabii-kültür incisi veya kıymetli-yarı kıymetli taş mı?", "71.01–71.03 (yaşı önemsiz, Not 1(c))"],
            ["2", "İtibari değeri tanınan, tedavüldeki veya tedavüle çıkacak kullanılmamış pul ya da damgalı kağıt mı?", "<b>49.07</b> (Not 1(a))"],
            ["3", "Tamamen elle yapılmış yağlıboya, karakalem, pastel resim; kolaj; ticari olmayan el yapımı mozaik mi?", "<b>97.01</b>"],
            ["4", "Sanatçının elle hazırladığı levhadan mekanik-fotomekanik usul olmadan doğrudan baskı mı?", "<b>97.02</b>"],
            ["5", "Heykel veya yontu sanatının orijinal eseri mi (ticari seri üretim değil)?", "<b>97.03</b>"],
            ["6", "Kullanılmış veya 49.07 dışı pul, ilk gün zarfı, pullu maksimum kart mı?", "<b>97.04</b>"],
            ["7", "Zoolojik, botanik, mineralojik, anatomik; tarihi, arkeolojik, paleontolojik, etnografik veya nümizmatik koleksiyon eşyası mı?", "<b>97.05</b>"],
            ["8", "Yukarıdakilerin hiçbiri değil ve eskiliği 100 yılı aşıyor mu?*", "<b>97.06</b>"],
            ["9", "Hiçbiri değilse (seri üretim heykel, elle dekore fabrikasyon ürün, plan, tiyatro dekoru)", "Maddesine veya işlevine göre (44.20, 69.13, 83.06, 49.06, 59.07)"],
        ],
        "dipnot": "* Not 5(B): 97.06, 97.01–97.05 eşyasına uygulanmaz; 100 yaşını aşan orijinal tablo 97.01’de, orijinal heykel 97.03’te kalır. Çerçeve, mahiyet ve kıymeti uygunsa eserle birlikte sınıflandırılır (Not 6).",
    },
    "pozisyon_haritasi": [
        ["97.01", "Tamamen elle yapılmış resimler; kolajlar, mozaikler, dekoratif plakalar",
         "Tamamen el yapımı; 49.06 çizimleri ve elle dekore fabrikasyon ürün hariç", "Yağlıboya tablo, elle kopya, karakalem, kolaj"],
        ["97.02", "Orijinal gravürler, estamplar, litografyalar",
         "Elle yapılmış levhadan doğrudan baskı; fotomekanik hariç", "Bakır gravür, orijinal litografya"],
        ["97.03", "Heykel veya yontu sanatının orijinal eserleri",
         "Madde önemsiz; ticari seri üretim hariç", "Mermer heykel, sınırlı bronz döküm"],
        ["97.04", "Posta pulları, damga pulları, pullu zarflar ve benzerleri",
         "Kullanılmış olsun olmasın; 49.07 hariç", "Pul koleksiyonu, ilk gün zarfı"],
        ["97.05", "Zoolojik, botanik, mineralojik, anatomik, tarihi, arkeolojik, paleontolojik, etnografik, nümizmatik koleksiyonlar",
         "Değerini nadirlik ve sunuş şeklinden alır", "Fosil, herbaryum, sikke koleksiyonu"],
        ["97.06", "Eskiliği 100 yılı aşan antikalar",
         "97.01–97.05’e girmeyenler; inci-kıymetli taş hariç", "Antika mobilya, halı, saat, avize"],
    ],
    "notlar": [
        ["Bölüm XXI",
         "Bölüm XXI yalnızca Fasıl 97’den oluşur; metinde ayrı bir bölüm notu yoktur. Bütün sınıflandırma kuralları aşağıdaki fasıl notlarındadır."],
        ["Fasıl 97 Not 1",
         "Fasıl dışı: (a) 49.07’deki kullanılmamış posta veya damga ve harç pulları, damgalı kağıt ve benzerleri; (b) tiyatro dekorları, atölye fonları veya benzeri işler için boyanmış tuvaller (59.07), 97.06’ya girebilecekler hariç; (c) tabii veya kültür incileri, kıymetli veya yarı kıymetli taşlar (71.01–71.03)."],
        ["Fasıl 97 Not 2",
         "97.01, sanatçılar tarafından tasarlanmış veya yaratılmış olsalar bile ticari nitelikteki geleneksel zanaatkarlığın seri üretim reprodüksiyonları, kalıpları veya eserleri olan mozaiklere uygulanmaz."],
        ["Fasıl 97 Not 3",
         "97.02 anlamında “orijinal gravürler, estamplar ve litograflar”: kullanılan usul ve madde ne olursa olsun, <b>mekanik veya fotomekanik usuller hariç</b>, sanatkar tarafından tamamen elle yapılmış bir veya daha fazla levhadan doğrudan elde edilen renkli veya siyah-beyaz baskılar."],
        ["Fasıl 97 Not 4",
         "Ticari karakterde seri halde üretilen kopyalar veya eserler, sanatçılar tarafından tasarlanmış, dizayn edilmiş veya yaratılmış olsalar bile 97.03 dışında kalır."],
        ["Fasıl 97 Not 5",
         "(A) Not 1–4 saklı kalmak şartıyla, bu fasılda yer alan eşya tarifenin başka herhangi bir faslında değil bu fasılda sınıflandırılır. (B) 97.06, bu fasılın daha önceki pozisyonlarında yer alan eşyaya uygulanmaz."],
        ["Fasıl 97 Not 6",
         "Yağlıboya, karakalem ve pastel resimlerin, kolajların veya benzeri dekoratif panoların, gravür, estamp ve litografların çerçeveleri, <b>mahiyet ve kıymet</b> itibarıyla eserin değerine uygunsa onunla birlikte sınıflandırılır; uygun değilse ayrı sınıflandırılır."],
        ["Genel Açıklamalar",
         "97.01–97.05’teki eşya 100 yıldan daha eski olsa bile bu pozisyonlarda kalır. Pozisyon veya not şartlarını taşımayan eşya tarifenin diğer fasıllarında sınıflandırılır."],
        ["97.01 Açıklama Notu",
         "Resim her maddeye yapılmış olabilir ama <b>tamamen elle</b> yapılmış olmalıdır. Hariç: fotomekanik usulle yapılan yağlıboyalar, basılı çizgiler üzerine elle yapılanlar, delikli kalıplarla elde edilen “hakiki kopyalar”; mimari ve mühendislik planları ile model, mücevher, duvar kağıdı, mensucat, mobilya desenleri (49.06); elle dekore fabrikasyon ürünler (seramik vazo, hatıra eşyası). Orijinalin elle yapılmış kopyası 97.01’de kalır. Tek parçalık süs eşyası “benzeri dekoratif pano” sayılmaz (44.20, 83.06 vb.)."],
        ["97.02 ve 97.03 Açıklama Notları",
         "97.02: transfer tekniğiyle elde edilen ve rötuşlu orijinaller dahil; baskı levhaları (klişeler) 84.42. 97.03: herhangi bir maddeden orijinal heykel; heykeltıraşın modelinden sınırlı sayıda alınan nüshalar (nadir haller dışında bir düzineyi geçmez) dahil. Hariç: ticari süs heykelleri, zanaatkar işleri, seri üretim heykeller; bunlar maddesine göre (ahşap 44.20, taş 68.02 / 68.15, seramik 69.13, metal 83.06), süs eşyası olarak 71.16 / 71.17’ye girenler hariç."],
        ["97.04 Açıklama Notu",
         "Kullanılmış olsun olmasın posta ve damga pulları, pullu ilk gün zarfları ve maksimum kartlar, damgalı kağıtlar; koleksiyon için mutat değerdeki albümler koleksiyonla birlikte. Hariç: pulsuz ilk gün ve maksimum kartları (48.17 veya Fasıl 49), itibari değeri tanınan kullanılmamış pullar (49.07), tasarruf pulları ve tenzilat kuponları (49.11)."],
        ["97.05 Açıklama Notu",
         "Doldurulmuş hayvanlar, kutu içinde böcekler, herbaryumlar, mineral (Fasıl 71 taşları hariç) ve fosil numuneleri, iskeletler; arkeolojik, etnografik, tarihi eserler. Nümizmatik: tedavülde olmayan paralar ve madalyalar; tek parça halinde gelenler her neviden birkaç adedi geçmemeli ve koleksiyon amacı açık olmalı. Hariç: aynı cins büyük miktar paralar (Fasıl 71), yasal para birimi olan paralar (71.18, hediye kutusunda bile), mücevher olarak monte edilen paralar (Fasıl 71 veya 97.06), koleksiyon eşyası sayılmayan tedavülden kalkmış kağıt paralar (49.07); ticari amaçla üretilen hatıra eşyası, sonradan nadirlik veya yaş değeri kazanmadıkça."],
        ["97.06 Açıklama Notu",
         "Eskiliği 100 yılı aşan, 97.01–97.05’e girmeyen antikalar: mobilya, çerçeve, eski basma kitaplar, haritalar, vazolar, halılar, mücevherat, kuyumcu eşyası, vitraylar, avizeler, müzik aletleri, saatler, kabartmalar, mühürler. Orijinal vasfını koruyan tamir edilmiş antikalar ve yeni ağaca monte edilmiş antika halılar dahil; 71.01–71.03 inci ve taşları eskiliklerine bakılmaksızın hariç."],
    ],
    "sinir_komsulari": [
        ["İtibari değeri tanınan, kullanılmamış posta pulu", "49.07", "Not 1(a); kullanılmış pul 97.04"],
        ["Posta pulu taşımayan ilk gün kartı, maksimum kart", "48.17 / Fasıl 49", "97.04 hariç tutması"],
        ["Tasarruf pulu, pul şeklinde tenzilat kuponu", "49.11", "97.04 hariç tutması"],
        ["Elle çizilmiş mimari plan; mobilya, mensucat deseni", "49.06", "97.01 hariç tutması"],
        ["Tiyatro dekoru, atölye fonu için boyanmış tuval", "59.07", "Not 1(b); 97.06’ya girebilecekler hariç"],
        ["Elle boyanmış seramik tabak, vazo; hatıra eşyası", "Kendi pozisyonu (ör. Fasıl 69)", "Elle dekore fabrikasyon ürün"],
        ["Seri üretim ahşap, taş, seramik, metal heykelcik", "44.20 / 68.02 / 69.13 / 83.06", "Not 4; ticari karakter"],
        ["Gravür ve litografya baskı levhası (klişe)", "84.42", "97.02 hariç tutması"],
        ["Fona yapıştırılmış tek parçalık süs eşyası", "44.20 / 83.06", "97.01 “benzeri dekoratif pano” sayılmaz"],
        ["Yasal para birimi olan madeni para (hediye kutusunda)", "71.18", "97.05 hariç tutması"],
        ["Aynı cinsten büyük miktarda madeni para; mücevher olarak monte para", "Fasıl 71 (monte para 97.06 olabilir)", "Koleksiyon niteliği yok"],
        ["Koleksiyon eşyası sayılmayan tedavülden kalkmış kağıt para", "49.07", "97.05 hariç tutması"],
        ["Antika inci ve kıymetli taş", "71.01–71.03", "Not 1(c); yaşı önemsiz"],
        ["Esere uygun olmayan tablo çerçevesi", "Maddesine göre (ör. 44.14)", "Not 6"],
        ["100 yaşını aşmış orijinal tablo veya heykel", "97.01 / 97.03", "Not 5(B); 97.06 değil"],
    ],
    "tuzaklar": [
        "<b>Yaş, sanat eserini antikaya çevirmez.</b> 100 yaşını geçmiş orijinal heykel 97.03’te, eski yağlıboya tablo 97.01’de kalır (Not 5(B)); 97.06 artık pozisyondur.",
        "<b>Elle kopya sanat eseridir, baskı kopya değildir.</b> Orijinalin tamamen elle yapılmış kopyası 97.01; fotomekanik yağlıboya, basılı çizgi üzerine boyama ve delikli kalıp kopyaları hariç.",
        "<b>Sanatçı imzası seri üretimi kurtarmaz.</b> Ticari nitelikte seri üretilen mozaik ve heykeller sanatçı tasarlasa da 97.01 / 97.03 dışıdır (Not 2, Not 4).",
        "<b>Kullanılmamış pul her zaman 97.04 değildir.</b> İtibari değeri tanınan, tedavüldeki veya tedavüle çıkacak pul 49.07; kullanılmış pul ve pullu ilk gün zarfı 97.04.",
        "<b>Antika inci antika değildir.</b> 71.01–71.03’teki inci ve kıymetli taşlar eskiliklerine bakılmaksızın Fasıl 71’dedir; ama 100 yaşını aşmış mücevherat 97.06’dır.",
        "<b>Çerçeve, değeri uygunsa tabloyla gider.</b> Mahiyet ve kıymet uygun değilse ayrı, maddesine göre sınıflandırılır (Not 6).",
        "<b>Gravürün levhası 97.02 değildir.</b> Baskı levhaları ve klişeler 84.42’dedir.",
        "<b>Hediye kutusundaki geçerli para koleksiyon eşyası değildir.</b> Yasal para birimi olan paralar 71.18; aynı cinsten büyük miktarda para Fasıl 71; ezilmiş paralar hurda.",
        "<b>Tamir edilmiş antika yine antikadır.</b> Orijinal vasfını korudukça modern tamir parçası içeren antika mobilya 97.06’da kalır.",
        "<b>Elle çizilmiş mimari plan resim değildir.</b> 49.06’ya gider; tiyatro dekoru tuvali de 59.07’dir.",
    ],
    "hafiza": {
        "kanca": "RE – BA – HEY – PUL – KOL – ANT",
        "aciklama": "<b>RE</b>sim 97.01 · <b>BA</b>skı (gravür, litografya) 97.02 · <b>HEY</b>kel 97.03 · <b>PUL</b> 97.04 · <b>KOL</b>eksiyon 97.05 · <b>ANT</b>ika 97.06. Bir müzeyi gezdiğinizi düşünün: önce resim salonu, sonra baskı galerisi, heykel avlusu, pul vitrini, doğa tarihi salonu; en sonda “yüz yaşındaki diğer her şey”in durduğu antika deposu. Depoya yalnızca ilk beş salona girmeyen eşya konur.",
    },
    "sinav_odagi": [
        "Bu fasıl çıkmış sorularda az sayıda yer almıştır; doğrudan sorulan konu Not 5(B)’dir: eskiliği 100 yılı aşan orijinal antika heykelin GYK 1 ile 97.03’te kaldığı, 97.06 ve GYK 3 seçeneklerinin çeldirici olduğu “gerekçe + pozisyon” kalıbı.",
        "Fasıl 97 eşyası (orijinal heykel, zooloji koleksiyonu) “hangisi aynı fasılda yer alır” sorularında Fasıl 95 eşyasıyla (gezici hayvan sergisi, üç tekerlekli bisiklet) karıştırılmak üzere çeldirici olarak kullanılmıştır; tiyatro dekoru (59.07) da aynı soruda yer almıştır.",
        "Plastikten küçük heykel ve süs eşyasının 39.26’da sınıflandırıldığı sorular: ticari karakterli seri üretim heykellerin maddesine göre sınıflandırılması (Not 4).",
        "“Mamul olduğu maddeye göre sınıflandırılır mı?” kalıbında antika biblonun maddeden bağımsız olarak Fasıl 97’de yer aldığı.",
    ],
    "cikmis_ornekler": [
        {
            "soru": "Tarife Cetveline göre eskiliği 100 yılı aşan orijinal antika heykel hangi gerekçe ile hangi tarife pozisyonunda sınıflandırılır?",
            "secenekler": ["Genel Yorum Kuralı 1, 97.03", "Genel Yorum Kuralı 1, 97.06", "Genel Yorum Kuralı 3-A, 97.03",
                           "Genel Yorum Kuralı 3-A, 97.06", "Genel Yorum Kuralı 3-C, 97.06"],
            "cevap": "A",
            "aciklama": "Not 5(B), 97.06’nın fasılın önceki pozisyonlarındaki eşyaya uygulanmayacağını öngörür; Genel Açıklamalar da 97.01–97.05 eşyasının 100 yıldan eski olsa bile bu pozisyonlarda kalacağını belirtir. Sonuç doğrudan not hükmünden çıktığı için GYK 1 uygulanır.",
        },
        {
            "soru": "Türk Gümrük Tarife Cetveli’ne göre aşağıdaki eşyalardan hangisi “gezici hayvan sergileri” ile aynı fasılda sınıflandırılır?",
            "secenekler": ["Kamp çadırı", "Heykel ve yontu sanatının orijinal bir eseri", "Çocuklar için üç tekerlekli bisiklet",
                           "Tiyatro dekoru", "Zooloji bilim dalına ait bir koleksiyon eşyası"],
            "cevap": "C",
            "aciklama": "Gezici hayvan sergileri 95.08’de, üç tekerlekli bisikletler 95.03’te, yani ikisi de Fasıl 95’tedir. Orijinal heykel 97.03’te, zooloji koleksiyonu 97.05’te; tiyatro dekoru tuvali Not 1(b) uyarınca 59.07’de (97.06’ya girebilecekler hariç) yer alır.",
        },
    ],
    "ozet": [
        "Fasıl 97 eşyası başka fasla gitmez (Not 5(A)); ama Not 1–4 şartlarını taşımayan eşya diğer fasıllarda sınıflandırılır.",
        "97.01 tamamen elle yapılmış resim, kolaj, mozaik; elle dekore fabrikasyon ürün ve 49.06 planları hariç.",
        "97.02 elle hazırlanmış levhadan doğrudan baskı; fotomekanik baskı ve levha (84.42) hariç.",
        "97.03 orijinal heykel, madde önemsiz; ticari seri üretim heykel maddesine göre (44.20, 68.02, 69.13, 83.06).",
        "97.04 pullar (49.07 hariç), 97.05 koleksiyon eşyası, 97.06 100 yılı aşan diğer antikalar.",
        "97.01–97.05 eşyası 100 yaşını aşsa da yerinde kalır; inci ve kıymetli taşlar yaşına bakılmaksızın Fasıl 71.",
        "Çerçeve, mahiyet ve kıymeti esere uygunsa eserle birlikte sınıflandırılır (Not 6).",
    ],
    "sorular": sorular,
}

if __name__ == "__main__":
    out = os.path.join(KITAP, "data", "fasil_97.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    print("yazıldı:", out)
