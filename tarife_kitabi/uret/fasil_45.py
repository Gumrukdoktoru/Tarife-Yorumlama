from yardim_44_47 import q, yaz, T_E, T_O, T_F, T_N, T_G, T_B, T_C, T_S

sorular = [
    # 1
    q("Tarife Cetveline göre, tabii mantardan kesilmiş, kenarları yuvarlatılmış ve tıpa olarak kullanılacağı ayırt edilebilen tıpa taslakları hangi pozisyonda sınıflandırılır?",
      "45.03", ["45.02", "45.01", "45.04", "44.21"], "B", T_E,
      "45.03 Açıklama Notu, yuvarlak kenarlı tıpa taslakları dahil tabii mantardan her türlü tıpa ve tıkacı kapsar. Keskin kenarlı küpler veya kare dilimler halindeki taslaklar ise 45.02’de kalır. Aglomere mantardan olsaydı 45.04’e girerdi; mantar eşyası ahşap eşya (44.21) sayılmaz.",
      "45.02 ve 45.03 Açıklama Notları."),
    # 2
    q("Aşağıdakilerden hangisi Tarife Cetvelinin 45. faslında <b>sınıflandırılmaz</b>?",
      "Tabii mantardan balık oltası mantarı",
      ["Tabii mantardan şişe tıpası", "Granül halinde mantar",
       "Aglomere mantardan yer karosu", "Tabii mantardan balıkçı ağı yüzdürücüsü"], "D", T_O,
      "45.03 Açıklama Notu balık oltalarına mahsus mantarları oyun ve spor malzemesi olarak Fasıl 95’e gönderir; Fasıl 45 Not 1 de Fasıl 95 eşyasını hariç tutar. Balıkçı ağı yüzdürücüleri ise 45.03’te açıkça sayılmıştır. Tıpa 45.03’te, granül 45.01’de, aglomere karo 45.04’tedir.",
      "Fasıl 45 Not 1; 45.03 Açıklama Notu."),
    # 3
    q("Fasıl 45 Not 1’e göre aşağıdakilerden hangisi mantardan yapılmış olsa bile bu fasıl kapsamı <b>dışındadır</b>?",
      "65. Fasıldaki başlıklar ve bunların aksamı",
      ["Şişe ve kavanoz kapaklarında kullanılan contalar", "Can kurtaran simitleri",
       "Isı yalıtımında kullanılan aglomere mantar levhalar", "Tabii mantardan masa altlıkları"], "A", T_N,
      "Fasıl 45 Not 1; Fasıl 64’teki ayakkabı ve aksamını, Fasıl 65’teki başlık ve aksamını ve Fasıl 95’teki oyuncak, oyun ve spor malzemesini fasıl dışında bırakır. Conta, can simidi ve masa altlığı 45.03’te, aglomere mantar levha 45.04’te yer alır.",
      "Fasıl 45 Not 1; 45.03 ve 45.04 Açıklama Notları."),
    # 4
    q("Aşağıdakilerden hangisi diğerlerinden farklı bir pozisyonda yer alır?",
      "Kare kesilmiş, keskin kenarlı tabii mantar levha",
      ["Plastik başlıklı tabii mantar şişe tıpası", "Tabii mantardan banyo paspası",
       "Daire şeklinde kesilmiş tabii mantar masa altlığı", "Tabii mantardan can kurtaran simidi"], "E", T_F,
      "Dikdörtgen (kare dahil) şeklinde kesilmiş tabii mantar blok, levha, yaprak ve şeritler 45.02’dedir. Tıpa, banyo paspası, daire şeklindeki altlık ve can simidi tabii mantardan eşya olarak 45.03’tedir. Dikdörtgen dışı şekilde kesilen parçaların 45.03’e geçtiği unutulmamalıdır.",
      "45.02 ve 45.03 Açıklama Notları."),
    # 5
    q("Kırılmış mantar granüllerinin ilave bir yapıştırma maddesi kullanılmadan yüksek sıcaklıkta basınç altında sıkıştırılmasıyla elde edilen ısı yalıtım levhası hangi pozisyonda sınıflandırılır?",
      "45.04", ["45.01", "45.02", "45.03", "44.11"], "C", T_E,
      "45.04 Açıklama Notuna göre aglomere mantar, granül veya toz mantarın bir yapıştırıcı ile ya da yapıştırıcı olmadan yaklaşık 300 °C’de sıkıştırılmasıyla elde edilir; ikinci halde mantarın tabii zamkı bağlayıcı görevi görür. Granülün kendisi 45.01’de kalırdı. Lif levha (44.11) ağaç liflerinden yapılır.",
      "45.04 Açıklama Notu; 45.01 Açıklama Notu."),
    # 6
    q("Metal başlık takılmış tabii mantar şişe tıpası 45.03 pozisyonunda sınıflandırılır. Bir maddeden mamul eşyaya yapılan atfın, kısmen o maddeden mamul eşyayı da kapsamasını sağlayan ve açıklama notunda 45.03 pozisyonu örnek olarak verilen Genel Yorum Kuralı hangisidir?",
      "GYK 2(b)", ["GYK 1", "GYK 2(a)", "GYK 3(c)", "GYK 5(b)"], "C", T_G,
      "GYK 2(b)’ye göre belirli bir maddeden mamul eşyaya yapılan atıf, tamamen veya kısmen bu maddeden mamul eşyayı da içine alır; kuralın açıklama notu örnek olarak 45.03’ü (tabii mantardan mamul eşya) verir. 45.03 Açıklama Notu da tıpaların metal veya plastik başlıklı olabileceğini belirtir. 2(a) tamamlanmamış veya demonte eşya, 5(b) ambalaj, 3(c) son pozisyon kuralıdır.",
      "GYK 2(b) ve Açıklama Notu; 45.03 Açıklama Notu."),
    # 7
    q("Aşağıdakilerden hangisi 45.01 pozisyonunda <b>yer almaz</b>?",
      "Mantar granüllerinin tutkalla bağlanmasıyla elde edilen blok",
      ["Ağaçtan soyulduğu gibi kıvrılmış kalın dilimler halindeki işlenmemiş mantar",
       "Fungisitle işlem görmüş tabii mantar",
       "Döşemecilikte doldurma maddesi olarak kullanılan mantar yünü",
       "Isı işlemiyle genleştirilmiş mantar granülü"], "E", T_O,
      "Bir bağlayıcıyla sıkıştırılmış mantar aglomere mantar olup 45.04’tedir; 45.01 Açıklama Notu aglomere mantarı açıkça hariç tutar. İşlenmemiş kabuk, fungisitle işlenmiş mantar, mantar yünü (döküntü) ve boyanmış, emprenye edilmiş, fırınlanmış veya genleştirilmiş granül 45.01’de kalır.",
      "45.01 Açıklama Notu (1), (2), (3)."),
    # 8
    q("Aşağıdaki eşya – pozisyon eşleştirmelerinden hangisi <b>doğrudur</b>?",
      "Kağıtla sağlamlaştırılmış ince tabii mantar şeridi – 45.02",
      ["Tıpa diski ile kaplanmış adi metal şişe kapsülü – 45.03",
       "Ayakkabı içine konulan değiştirilebilir mantar tabanlık – 45.03",
       "Ezilmiş tabii mantar – 45.04",
       "Fişek tapa mantarı – 45.03"], "A", T_B,
      "45.02 Açıklama Notu, sigara uçlarında kullanılan rulo halindeki çok ince şeritler dahil kağıt veya bezle sağlamlaştırılmış mantar levhaları kapsar. Tıpa diskli adi metal kapsüller 83.09’a, değiştirilebilir tabanlıklar Fasıl 64’e, fişek tapa mantarı 93.06’ya gider; ezilmiş mantar ise 45.01’dedir.",
      "45.02 ve 45.03 Açıklama Notları; 45.01 pozisyon metni."),
    # 9
    q("Fasıl 45 Genel Açıklamalarına göre mantarla ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Mantar, mantar meşesinin (Quercus suber) dış kabuklarından elde edilir. II. İlk ürün olarak soyulan kabuğa “dişi mantar” denir ve ticari bakımdan en değerli mantardır. III. Mantar ısı ve sesi iyi iletmez. IV. Mantar ağır, sert ve su emici bir maddedir.",
      "I ve III", ["I ve II", "II ve IV", "I, II ve III", "I, III ve IV"], "B", T_C,
      "Mantar, mantar meşesinin dış kabuğundan elde edilir (I) ve ısı ile sesi iyi iletmez (III). İlk soyulan “dişi mantar” sert, gevrek, düşük kalite ve değerdedir; ticari bakımdan önemli olan sonraki ürünlerdir (II yanlış). Mantar hafif, esnek, sıkıştırılabilir ve su geçirmezdir (IV yanlış).",
      "Fasıl 45 Genel Açıklamalar."),
    # 10
    q("Dış (kabuk) ve iç (ağaç) yüzeyleri birbirine neredeyse paralel olacak şekilde biçilmiş, yani kabaca kare haline getirilmiş tabii mantar dilimleri hangi pozisyonda yer alır?",
      "45.02", ["45.01", "45.03", "45.04", "44.03"], "D", T_E,
      "45.02 Açıklama Notu, dış kabuğunun tamamı çıkarılmış veya iki yüzeyi neredeyse paralel hale getirilecek şekilde kesilmiş (kabaca kare haline getirilmiş) tabii mantar dilimlerini kapsar. 45.01 yalnız işlenmemiş veya basitçe hazırlanmış mantar içindir. Kabaca kare yontulmuş ağaç gövdesi 44.03’te olsa da mantar Fasıl 45’in konusudur.",
      "45.02 pozisyon metni ve Açıklama Notu; 45.01 Açıklama Notu."),
    # 11
    q("45.04 pozisyonu Açıklama Notuna göre, ilave bir yapıştırma maddesi kullanılmadan aglomere mantar elde edilirken mantar yaklaşık hangi sıcaklıkta sıkıştırılır ve bağlayıcı görevini ne üstlenir?",
      "Yaklaşık 300 °C; mantardaki tabii zamk",
      ["Yaklaşık 100 °C; ilave edilen jelatin", "Yaklaşık 150 °C; vulkanize edilmemiş kauçuk",
       "Yaklaşık 200 °C; katran", "Yaklaşık 500 °C; plastik reçine"], "E", T_N,
      "Açıklama Notuna göre yapıştırıcısız aglomere mantar yaklaşık 300 °C sıcaklıkta sıkıştırılır ve mantardaki tabii zamk yapıştırma maddesi görevi yapar. Jelatin, vulkanize edilmemiş kauçuk, katran ve plastik ise ilave yapıştırıcı olarak kullanılan maddelerdir.",
      "45.04 Açıklama Notu."),
    # 12
    q("Aşağıdakilerden hangisi tabii mantardan yapılmış olmasına rağmen diğerlerinden farklı bir fasılda yer alır?",
      "Şapka siperliği",
      ["Bıçak sapı tutacağı", "Şişe boynunun iç kısmında kullanılan astar",
       "Daktilo altlığı", "Rondela"], "A", T_F,
      "Başlıkların aksamı Fasıl 45 Not 1 gereği Fasıl 65’tedir; şapka siperliği bu nedenle mantardan olsa da Fasıl 45 dışındadır. Sap tutacakları, şişe boynu astarları, daktilo altlıkları ve rondelalar 45.03 Açıklama Notunda tabii mantardan eşya olarak sayılmıştır.",
      "Fasıl 45 Not 1; 45.03 Açıklama Notu."),
    # 13
    q("Bir işletme, mantar meşesinden soyduğu kabukları kaynar suyla muamele ettikten sonra presle düzleştirmekte ve çatlaklı dış tabakalarda kalan kullanılamaz kenarları kırparak balyalamaktadır. Kabukların dış kabuğu çıkarılmamış, dikdörtgen veya kare şekil verilmemiştir. Bu ürün hangi pozisyonda sınıflandırılır?",
      "45.01", ["45.02", "45.03", "45.04", "44.01"], "D", T_S,
      "45.01 Açıklama Notuna göre basitçe hazırlanmış tabii mantar; kullanıma elverişsiz kısımları atmak için kenarları temizlenmiş, kaynar su veya buharla muamele edildikten sonra presle düzleştirilmiş mantarı da kapsar. Dış kabuğu alınmış veya kabaca kare yapılmış olsaydı 45.02’ye geçerdi. Mantar artığı yakacak odun artığı (44.01) değildir.",
      "45.01 Açıklama Notu (1); 45.02 Açıklama Notu."),
    # 14
    q("Aşağıdakilerden hangisi 45.03 pozisyonunda <b>sınıflandırılmaz</b>?",
      "84.84’teki türden takım halindeki contalar (mantar contalı)",
      ["Metal başlıklı tabii mantar şişe tıpası ve tıkacı", "Şişe boynunun iç kısmında kullanılan tabii mantar astar",
       "Dikdörtgen dışında, oval şekilde kesilmiş tabii mantar levha", "Tabii mantar levhalardan yapılmış can kurtaran simidi"], "B", T_O,
      "45.03 Açıklama Notu mantardan rondela ve contaları kapsar; ancak 84.84 pozisyonunda yer alan takım halindeki contaları hariç tutar. Başlıklı tıpa, şişe boynu astarı, dikdörtgen dışı (oval) kesilmiş levha ve can simidi 45.03’tedir.",
      "45.03 Açıklama Notu (1)–(4)."),
    # 15
    q("Tabii mantar döküntülerinin öğütülmesiyle elde edilen, boyanmış ve fırınlanmış, aglomere edilmemiş mantar tozu hangi pozisyonda sınıflandırılır?",
      "45.01", ["45.04", "45.02", "14.04", "45.03"], "C", T_E,
      "Ezilmiş, granül veya toz haline getirilmiş mantar, boyanmış, emprenye edilmiş, fırınlanmış veya ısıyla genleştirilmiş olsa da 45.01’de yer alır. Ancak bir araya getirilip aglomere edilirse 45.04’e geçer. Bitkisel ürün olması onu 14.04’e götürmez; mantar Fasıl 45’te özel olarak düzenlenmiştir.",
      "45.01 pozisyon metni ve Açıklama Notu (3)."),
    # 16
    q("Fasıl 45 Açıklama Notlarına göre aşağıdakilerden hangisi <b>doğrudur</b>?",
      "Dikdörtgenden (kare dahil) başka şekillerde kesilmiş tabii mantar blok ve levhalar mantar eşyası kabul edilir.",
      ["Aglomere mantar, tıpa imalinde tabii mantardan daha fazla kullanılır.",
       "Linoleum karakterini taşıyan aglomere mantar ürünleri 45.04’te kalır.",
       "Birbiri üzerine tutkalla yapıştırılmış tabii mantar tabakalarından oluşan dikdörtgen levhalar aglomere mantar sayılır.",
       "Mantarın yalnızca yardımcı bir kısım olduğu süzme ve ölçü tıpaları 45.03’te yer alır."], "A", T_N,
      "45.02 Açıklama Notuna göre dikdörtgenden başka şekiller halinde kesilmiş blok, levha, yaprak ve şeritler mantar eşyası sayılır ve 45.03’e girer. Aglomere mantar tıpa imalinde nadiren kullanılır; linoleum karakterindeki ürünler 59.04’tedir. Tutkalla yapıştırılmış tabii mantar tabakaları 45.02’de kalır; süzme ve ölçü tıpaları esas karakteri veren maddeye göre sınıflandırılır.",
      "45.02, 45.03 ve 45.04 Açıklama Notları."),
    # 17
    q("Tarife Cetveline göre aşağıdaki mantar ürünlerinden hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır?",
      "Aglomere mantardan şişe kapağı diski",
      ["Tabii mantar talaşları", "Aglomere mantar kırpıntıları",
       "Granül halinde mantar", "Yüzeyi ateşe tutularak temizlenmiş tabii mantar"], "D", T_F,
      "Aglomere mantardan eşya 45.04’tedir; Açıklama Notu aglomere mantarın şişe kapağı disklerinde yaygın olarak kullanıldığını belirtir. Tabii veya aglomere mantarın döküntüleri (talaş, kırpıntı), granül mantar ve yüzeyi kazınmış ya da ateşe tutularak temizlenmiş mantar 45.01’dedir. Tuzak, aglomere mantar kırpıntısını 45.04 sanmaktır.",
      "45.01 Açıklama Notu (1), (2); 45.04 Açıklama Notu."),
    # 18
    q("Mantardan yapılmış, ayakkabı içine konulan değiştirilebilir tabanlığın Fasıl 45 yerine Fasıl 64’te sınıflandırılmasının dayanağı aşağıdakilerden hangisidir?",
      "GYK 1 – pozisyon metinleri ile Fasıl 45 Not 1",
      ["GYK 2(b) – kısmen mantardan eşya", "GYK 3(a) – en özel tanım",
       "GYK 3(c) – numara sırasına göre en son pozisyon", "GYK 4 – en çok benzeyen eşya"], "E", T_G,
      "GYK 1’e göre sınıflandırma pozisyon metinlerine ve bölüm veya fasıl notlarına göre yapılır. Fasıl 45 Not 1, Fasıl 64’teki ayakkabı ve aksamını hariç tuttuğundan, 45.03 Açıklama Notunun da belirttiği gibi değiştirilebilir tabanlık Fasıl 64’e gider. Notla çözülen bir durumda 3. veya 4. kurallara başvurulmaz.",
      "GYK 1; Fasıl 45 Not 1; 45.03 Açıklama Notu."),
    # 19
    q("“Keskin kenarlı küpler veya kare şeklinde kalınca dilimler halindeki tıpa taslakları ……… pozisyonunda, kenarları yuvarlatılmış benzer taslaklar ise ……… pozisyonunda sınıflandırılır.” Cümlesindeki boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?",
      "45.02 – 45.03", ["45.01 – 45.02", "45.03 – 45.02", "45.02 – 45.04", "45.04 – 45.03"], "B", T_B,
      "45.02 Açıklama Notu keskin kenarlı küp veya kare dilim halindeki tıpa taslaklarını kapsar, kenarları yuvarlatılmış benzerlerini 45.03’e gönderir. 45.03 Açıklama Notu da yuvarlak kenarlı taslakları tıpalarla birlikte sayar. 45.01 ham mantar, 45.04 aglomere mantar pozisyonudur.",
      "45.02 ve 45.03 Açıklama Notları."),
    # 20
    q("Aşağıdakilerden hangileri 45.04 pozisyonunda sınıflandırılır? I. Vulkanize edilmemiş kauçukla bağlanmış mantar granüllerinden kalıplanmış boru yalıtım kabukları II. Yağ ile emprenye edilmiş, kağıtla takviye edilmiş, linoleum karakteri taşımayan aglomere mantar levha III. Isı işlemiyle genleştirilmiş, aglomere edilmemiş mantar granülü IV. Aglomere mantardan şişe kapağı diskleri",
      "I, II ve IV", ["I ve III", "II ve III", "I, III ve IV", "II, III ve IV"], "C", T_C,
      "Bağlayıcılı aglomere mantar ve ondan kalıplanmış yalıtım şekilleri (I), emprenye edilmiş veya kağıtla takviye edilmiş, linoleum karakteri taşımayan aglomere mantar (II) ve aglomere mantardan kapak diskleri (IV) 45.04’tedir. Aglomere edilmemiş granül genleştirilmiş olsa da 45.01’de kalır (III).",
      "45.04 Açıklama Notu; 45.01 Açıklama Notu (3)."),
    # 21
    q("Tabii veya aglomere mantardan yapılmış olsa bile aşağıdakilerden hangisi Fasıl 45’te <b>sınıflandırılmaz</b>?",
      "Oyuncak olarak üretilmiş mantar yapı blokları",
      ["Tabii mantardan tıpa ve tıkaçlar", "Aglomere mantardan yer karoları", "Tabii mantardan balıkçı ağı yüzdürücüleri",
       "Şişe kapaklarında kullanılan mantar conta ve pullar"], "E", T_O,
      "Fasıl 45 Not 1, Fasıl 95’teki oyuncak, oyun ve spor malzemesini fasıl dışında bırakır. Tıpa ve tıkaçlar ile conta ve pullar 45.03’te, aglomere mantardan karolar 45.04’te, balıkçı ağı yüzdürücüleri 45.03’tedir.",
      "Fasıl 45 Not 1; 45.03 ve 45.04 Açıklama Notları."),
    # 22
    q("İki yüzü kontrplak olan, iç kısmında aralıklı ahşap lataları bulunan ve boşlukları ses yalıtımı için mantarla doldurulmuş, inşaat bölmelerinde kullanılan hücreli panel hangi pozisyonda yer alır?",
      "44.18", ["45.04", "44.12", "45.03", "94.06"], "B", T_E,
      "44.18 Açıklama Notuna göre hücreli ağaç panoların iç boşlukları mantar, cam elyaf vb. ses veya ısı yalıtıcı maddelerle donatılmış olabilir; bunlar inşaat bölmelerinde kullanılır. Mantar dolgu yalnız yardımcı işlev görür, paneli Fasıl 45’e götürmez. Göbekli kontrplaktan (44.12) farkı, göbeğin aralıklı lata veya kafesten oluşmasıdır.",
      "44.18 Açıklama Notu; 44.12 Açıklama Notu (hariç tutmalar)."),
    # 23
    q("Aşağıdaki eşya çiftlerinden hangisinde her iki eşya da aynı pozisyonda yer alır?",
      "Tabii mantar döküntüsü – Ezilmiş mantar",
      ["Tabii mantardan tıpa – Aglomere mantardan tıpa",
       "Keskin kenarlı tıpa taslağı – Kenarı yuvarlatılmış tıpa taslağı",
       "Mantar granülü – Aglomere mantardan karo",
       "Dış kabuğu alınmış mantar levha – Tabii mantardan can simidi"], "A", T_F,
      "Mantar döküntüleri ile ezilmiş, granül veya toz mantar 45.01 metninde birlikte sayılmıştır. Tabii mantar tıpa 45.03’te, aglomere tıpa 45.04’te; keskin kenarlı taslak 45.02’de, yuvarlak kenarlı taslak 45.03’te; granül 45.01’de, aglomere karo 45.04’te; kabuğu alınmış levha 45.02’de, can simidi 45.03’tedir.",
      "45.01–45.04 pozisyon metinleri ve Açıklama Notları."),
    # 24
    q("45.02 pozisyonu Açıklama Notuna göre “kağıt mantar” tabiri bazen hangi ürün için kullanılır?",
      "Arkası kağıtsız olsa da çok ince mantar tabaka veya şeridi için",
      ["Kağıt hamuruna mantar tozu katılarak üretilen kağıt ve karton için",
       "Yüzeyi mantar granülleriyle kaplanmış kağıt için",
       "Aglomere mantardan dilimlenmiş levhalar için",
       "Kağıda sarılmış halde satılan mantar tıpalar için"], "D", T_N,
      "45.02 Açıklama Notu, “kağıt mantar” tabirinin bazen arkası kağıtla kaplı olmasa dahi çok ince mantar tabakası veya şeridi için kullanıldığını belirtir. Kağıtla sağlamlaştırılmış ince mantar levhalar da 45.02’de yer alır. Diğer seçenekler notta geçmeyen ürünlerdir.",
      "45.02 Açıklama Notu."),
    # 25
    q("Tabii mantar levhalardan daire şeklinde kesilmiş, kenarları zımparalanmış ve sıcak tencere altlığı olarak kullanılan eşya hangi pozisyonda sınıflandırılır?",
      "45.03", ["45.02", "45.04", "44.19", "46.02"], "C", T_S,
      "Dikdörtgen dışında kesilmiş tabii mantar parçaları ve masa ile diğer eşya altlıkları 45.03 Açıklama Notunda tabii mantardan eşya olarak sayılmıştır. Dikdörtgen kesilmiş olsaydı levha olarak 45.02’de kalabilirdi. Ahşap tencere altlıkları 44.19’dadır; mantardan olanlar Fasıl 45’in konusudur.",
      "45.02 ve 45.03 Açıklama Notları; 44.19 Açıklama Notu."),
]

obj = {
    "tur": "fasil",
    "fasil": 45,
    "baslik": "Mantar ve mantardan eşya",
    "bolum": "IX",
    "oz": {
        "vurgu": "Fasıl 45’teki “mantar”, mantar meşesinin (Quercus suber) dış kabuğudur; yenilen mantarla ilgisi yoktur. Tabii ve aglomere mantar işlenme derecesine göre dört pozisyona ayrılır: ham, döküntü ve granül (45.01) → kabuğu alınmış veya dikdörtgen kesilmiş (45.02) → tabii mantardan eşya (45.03) → aglomere mantar ve eşyası (45.04). Ayakkabı, başlık ve oyuncak-spor eşyası mantardan olsa da Fasıl 45 dışındadır.",
        "maddeler": [
            "45.01: işlenmemiş veya basitçe hazırlanmış tabii mantar (kazınmış, kenarları temizlenmiş, fungisitle işlenmiş, kaynar suyla düzleştirilmiş); tabii veya aglomere mantar döküntüleri; ezilmiş, granül, toz mantar (boyanmış, fırınlanmış, genleştirilmiş olsa da).",
            "45.02: dış kabuğu alınmış veya kabaca kare yapılmış mantar; dikdörtgen (kare dahil) blok, levha, yaprak, şerit; kağıt veya bezle sağlamlaştırılmış levhalar; keskin kenarlı tıpa taslakları.",
            "45.03: tabii mantardan eşya; tıpa ve tıkaç (yuvarlak kenarlı taslaklar dahil), conta, rondela, can simidi, ağ yüzdürücüsü, banyo paspası, altlıklar ve dikdörtgen dışı kesilmiş parçalar.",
            "45.04: granül mantarın bağlayıcıyla veya bağlayıcısız yaklaşık 300 °C’de sıkıştırılmasıyla elde edilen aglomere mantar ve ondan eşya (karo, yalıtım levhası, kapak diski)."
        ]
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Ayakkabı veya aksamı mı? (değiştirilebilir tabanlık dahil)", "Fasıl 64"],
            ["2", "Başlık veya aksamı mı? (siperlik, iç şerit)", "Fasıl 65"],
            ["3", "Oyuncak, oyun veya spor malzemesi mi? (olta mantarı dahil)", "Fasıl 95"],
            ["4", "Tıpa diskiyle kaplanmış adi metal şişe kapsülü, fişek tapa mantarı ya da 84.84 türü takım conta mı?", "<b>83.09</b> / <b>93.06</b> / <b>84.84</b>"],
            ["5", "Aglomere mantar ya da aglomere mantardan eşya mı?", "<b>45.04</b> (linoleum karakterindeyse <b>59.04</b>)"],
            ["6", "Tabii mantardan bitmiş eşya, dikdörtgen dışı kesilmiş parça veya yuvarlak kenarlı tıpa taslağı mı?", "<b>45.03</b>"],
            ["7", "Dış kabuğu alınmış, kabaca kare, dikdörtgen blok, levha, şerit veya keskin kenarlı tıpa taslağı mı?", "<b>45.02</b>"],
            ["8", "Hiçbiri değilse: ham, basitçe hazırlanmış, döküntü, ezilmiş, granül veya toz", "<b>45.01</b>"]
        ],
        "dipnot": ""
    },
    "pozisyon_haritasi": [
        ["45.01", "Tabii mantar (ham), döküntü, granül, toz", "İşlenmemiş veya basit hazırlık; aglomere değil", "Soyulmuş kabuk, mantar yünü, granül"],
        ["45.02", "Kabuğu alınmış veya kare; dikdörtgen blok, levha, şerit", "Dik açılı kesim; keskin kenarlı tıpa taslağı", "Mantar levha, sigara ucu şeridi"],
        ["45.03", "Tabii mantardan eşya", "Dikdörtgen dışı şekil, yuvarlak kenar", "Şişe tıpası, conta, can simidi"],
        ["45.04", "Aglomere mantar ve eşyası", "Granülün ısı ve basınçla sıkıştırılması", "Mantar karo, yalıtım levhası, kapak diski"]
    ],
    "notlar": [
        ["Fasıl 45 Not 1", "Fasıl dışı: (a) Fasıl 64’teki ayakkabılar veya aksamı; (b) Fasıl 65’teki başlıklar veya aksamı; (c) Fasıl 95’teki eşya (oyuncak, oyun, spor malzemesi)."],
        ["Genel Açıklamalar", "Mantar, mantar meşesinin (Quercus suber) dış kabuğundan elde edilir. İlk soyulan kabuk “dişi mantar”dır: sert, gevrek, esnek olmayan, düşük kalite ve değerde. Sonraki soyumlar sıkı, homojen ve ticari bakımdan daha önemlidir."],
        ["Genel Açıklamalar", "Mantar hafif, esnek, sıkıştırılabilir, bükülebilir, su geçirmez, çürümez; ısı ve sesi iyi iletmez. Fasıl, 45.03 Açıklama Notunun son kısmındaki hariç tutmalar dışında tabii veya aglomere mantarın her tür ve şeklini ve bunlardan eşyayı kapsar."],
        ["45.01 Açıklama Notu", "Basit hazırlık: dış yüzeyi kazınmış veya ateşe tutularak temizlenmiş, kullanılamaz kenarları kırpılmış, fungisitle işlenmiş, kaynar su veya buharla muamele edilip presle düzleştirilmiş mantar. Dış kabuğu alınmış veya kabaca dört köşe yapılmış mantar 45.02’ye; aglomere mantar 45.04’e gider."],
        ["45.01 Açıklama Notu", "Döküntüler tabii veya aglomere mantardan olabilir (talaş, kırpıntı, “mantar yünü”). Ezilmiş, granül veya toz mantar boyanmış, emprenye edilmiş, fırınlanmış veya ısıyla genleştirilmiş olsa da 45.01’dedir."],
        ["45.02 Açıklama Notu", "Dikdörtgen (kare dahil) blok, levha, yaprak ve şeritler, tutkalla yapıştırılmış tabakalardan olsa da 45.02’dedir; dikdörtgen dışı şekiller 45.03’e girer. Kağıt veya bezle sağlamlaştırılmış levhalar (sigara ucu şeritleri dahil) 45.02’dedir. Keskin kenarlı tıpa taslakları 45.02, kenarları yuvarlatılmışlar 45.03."],
        ["45.03 Açıklama Notu", "Tabii mantardan tıpa ve tıkaçlar (metal, plastik başlıklı olabilir), conta, rondela, şişe boynu astarı, can simidi, ağ yüzdürücüsü, banyo paspası, altlıklar, sap tutacakları. Süzme veya ölçü tıpası gibi mantarın yardımcı kısım olduğu eşya kendi pozisyonuna gider."],
        ["45.03 Açıklama Notu", "Hariç: Fasıl 64 ayakkabı ve aksamı (değiştirilebilir tabanlık dahil); Fasıl 65 başlıklar; tıpa diskiyle kaplanmış adi metal kapsüller (83.09); fişek tapa mantarı (93.06); oyuncak, oyun ve spor malzemesi (olta mantarları dahil) (Fasıl 95); takım halindeki contalar (84.84)."],
        ["45.04 Açıklama Notu", "Aglomere mantar; granül veya toz mantarın ısı ve basınç altında, ya ilave yapıştırıcıyla (vulkanize edilmemiş kauçuk, tutkal, plastik, katran, jelatin) ya da yapıştırıcısız <b>yaklaşık 300 °C</b>’de (tabii zamk bağlayıcı) sıkıştırılmasıyla elde edilir. Emprenye edilmiş veya kağıt ya da mensucatla takviyeli olabilir; linoleum karakteri taşırsa 59.04."],
        ["45.04 Açıklama Notu", "Aglomere mantar tıpa imalinde nadiren, şişe kapağı disklerinde ise tabii mantardan çok daha fazla kullanılır; panel, blok, karo, boru yalıtımı, genleşme derzleri ve filtre imalinde yaygındır."]
    ],
    "sinir_komsulari": [
        ["Yenilen (kültür) mantarı; konserve mantar", "07.09 / 07.12 / 20.03", "Aynı kelime, farklı eşya: sebze veya müstahzar"],
        ["Mantardan değiştirilebilir ayakkabı tabanlığı, ayakkabı topuğu", "Fasıl 64", "Fasıl 45 Not 1"],
        ["Mantardan şapka siperliği veya başlık", "Fasıl 65", "Fasıl 45 Not 1"],
        ["Olta mantarı (şamandıra), mantar oyuncak, dart hedef tahtası", "Fasıl 95", "Fasıl 45 Not 1; 45.03 hariç tutması"],
        ["Tıpa diskiyle kaplanmış adi metal şişe kapsülü", "83.09", "45.03 hariç tutması"],
        ["Fişek tapa mantarı", "93.06", "45.03 hariç tutması"],
        ["Mantar conta da içeren takım halindeki contalar", "84.84", "45.03 hariç tutması"],
        ["Linoleum karakterindeki mantar kaplama", "59.04", "45.04 Açıklama Notu"],
        ["Boşlukları mantarla doldurulmuş hücreli ahşap panel", "44.18", "Mantar yalnız yalıtım dolgusu"],
        ["Ahşap tencere altlığı", "44.19", "Ahşap mutfak eşyası; mantardan olan 45.03"],
        ["Mantarın yardımcı kısım olduğu süzme veya ölçü tıpası", "Esas maddesine göre", "45.03 Açıklama Notu"]
    ],
    "tuzaklar": [
        "<b>Mantar = mantar meşesinin kabuğu.</b> Fasıl 45’te “mantar” yenilen mantar değildir; yenilen mantarlar sebze (Fasıl 7) veya müstahzar (20.03) olarak sınıflandırılır.",
        "<b>Kenar keskin mi, yuvarlak mı?</b> Keskin kenarlı küp veya kare dilim tıpa taslağı 45.02; kenarları yuvarlatılmış taslak 45.03.",
        "<b>Dikdörtgen sınırı.</b> Dikdörtgen (kare dahil) blok, levha, şerit 45.02; dikdörtgenden başka şekilde kesilen parça mantar eşyası sayılır → 45.03.",
        "<b>Granül işlem görse de 45.01’dir.</b> Boyanmış, emprenye edilmiş, fırınlanmış veya genleştirilmiş granül 45.01; sıkıştırılıp aglomere edilirse 45.04.",
        "<b>Aglomere mantar kırpıntısı 45.04 değildir.</b> Tabii veya aglomere mantarın döküntüleri 45.01’de toplanır.",
        "<b>45.03 yalnız tabii mantardan eşyadır.</b> Aglomere mantardan tıpa, karo, kapak diski 45.04’tedir.",
        "<b>Ağ yüzdürücüsü ≠ olta mantarı.</b> Balıkçı ağı yüzdürücüleri 45.03; balık oltalarına mahsus mantarlar spor malzemesi olarak Fasıl 95.",
        "<b>Başlıklı tıpa yine 45.03’tür.</b> Metal veya plastik başlıklı tabii mantar tıpa 45.03; tıpa diskiyle kaplanmış adi metal kapsül 83.09; mantarın yardımcı olduğu süzme tıpası kendi maddesine göre.",
        "<b>Takviye pozisyonu bozmaz.</b> Kağıt veya bezle sağlamlaştırılmış mantar levha 45.02; kağıt veya mensucatla takviyeli aglomere mantar linoleum karakteri taşımadıkça 45.04."
    ],
    "hafiza": {
        "kanca": "KABUK – KARE – TIPA – PRES",
        "aciklama": "<b>KABUK</b> 45.01: ağaçtan soyulan ham kabuk, kırıntı ve granül · <b>KARE</b> 45.02: kabuğu alınmış, dik açıyla kesilmiş levha ve keskin kenarlı taslak · <b>TIPA</b> 45.03: tabii mantardan eşya, simgesi şişe tıpası · <b>PRES</b> 45.04: granülün preslenmesiyle oluşan aglomere mantar. Bir şarap şişesini düşünün: kabuk ağaçtan soyulur, levha kesilir, tıpa yuvarlatılır, kapağın içindeki disk preslenmiş granüldür."
    },
    "sinav_odagi": [
        "Bu fasıl çıkmış sorularda az yer almıştır; doğrudan sorulduğu kalıp “mantardan yapılmış eşyadan hangisi 45. fasılda sınıflandırılır?” şeklindedir.",
        "Çeldiriciler Fasıl 45 Not 1’in hariç tuttuğu eşyadan seçilmiştir: ayakkabı topuğu (Fasıl 64), şapka siperliği (Fasıl 65), dart oyunu tablası (Fasıl 95); doğru cevap şişe tıpasıdır (45.03).",
        "Soru, eşyanın yapıldığı maddeden çok türüne bakılması gerektiğini ölçer: mantardan yapılmış olmak tek başına Fasıl 45 için yeterli değildir.",
        "Bölüm–fasıl eşleştirme sorularında Bölüm IX’un fasılları (44–46) çeldirici seçenek olarak kullanılmıştır."
    ],
    "cikmis_ornekler": [
        {
            "soru": "Aşağıdaki mantardan yapılmış eşyadan hangisi tarife cetvelinde 45’inci fasılda sınıflandırılır?",
            "secenekler": ["Ayakkabı topuğu", "Şapka siperliği", "Dart oyunu tablası", "Şişe tıpası"],
            "cevap": "D",
            "aciklama": "Fasıl 45 Not 1; Fasıl 64 ayakkabı aksamını, Fasıl 65 başlık aksamını ve Fasıl 95 oyun eşyasını fasıl dışında bırakır. Tabii mantardan şişe tıpası 45.03’te yer alır."
        }
    ],
    "ozet": [
        "Fasıl 45’teki mantar, mantar meşesi kabuğudur; yenilen mantar değildir.",
        "Ham, basitçe hazırlanmış, döküntü, granül ve toz 45.01; işlem (boyama, fırınlama, genleştirme) granülü 45.01’den çıkarmaz.",
        "Kabuğu alınmış veya dikdörtgen kesilmiş mantar ve keskin kenarlı taslak 45.02; dikdörtgen dışı parça ve yuvarlak kenarlı taslak 45.03.",
        "Tabii mantardan eşya 45.03; aglomere mantar ve eşyası 45.04 (yapıştırıcısız ise yaklaşık 300 °C).",
        "Ayakkabı (64), başlık (65), oyuncak-spor (95) mantardan olsa da Fasıl 45 dışıdır."
    ],
    "sorular": sorular,
}

yaz(45, obj)
