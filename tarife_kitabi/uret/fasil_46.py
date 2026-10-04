from yardim_44_47 import q, yaz, T_E, T_O, T_F, T_N, T_G, T_B, T_C, T_S

sorular = [
    # 1
    q("Tarife Cetveline göre, buğday sapından örülmüş, yan yana konulup dikilerek daha geniş şerit haline getirilmiş ve kadın şapkası imalinde kullanılacak örgüler hangi pozisyonda sınıflandırılır?",
      "46.01", ["65.02", "46.02", "14.01", "65.04"], "D", T_E,
      "46.01 metni örgüleri ve örülmeye elverişli maddelerden benzeri ürünleri, şeritler halinde birleştirilmiş olsun olmasın kapsar; Açıklama Notu bunların yan yana dikilerek genişletilebileceğini ve çoğunlukla kadın şapkacılığında kullanıldığını belirtir. Henüz şapka veya şapka taslağı şekli verilmediği için Fasıl 65’e girmez. Örülmemiş ham sap 14.01’de, sepet gibi şekil verilmiş eşya 46.02’de olurdu.",
      "46.01 pozisyon metni ve Açıklama Notu (A)(1)."),
    # 2
    q("Fasıl 46 Not 1’e göre aşağıdakilerden hangisi “örülmeye elverişli madde” <b>sayılır</b>?",
      "Kağıttan şeritler", ["Terkip yoluyla elde edilen deriden şeritler", "At kılı", "İnsan saçı", "Keçeden şeritler"], "B", T_N,
      "Not 1’e göre örülmeye elverişli madde tabiri kağıttan şeritleri de kapsar. Deri veya terkip yoluyla elde edilen deri, keçe veya dokunmamış mensucattan şeritler, insan saçı, at kılı, dokumaya elverişli fitil ve iplikler ile Fasıl 54 monofilament ve şeritleri bu tabirin dışındadır. Bu maddelerden örülen eşya Fasıl 46’ya girmez.",
      "Fasıl 46 Not 1."),
    # 3
    q("Aşağıdakilerden hangisi Tarife Cetvelinin 46. faslında <b>sınıflandırılmaz</b>?",
      "Hint kamışından (rattan) örülmüş koltuk",
      ["Söğüt dallarından örülmüş, kulplu meyve sepeti", "Hint kamışından örülmüş kuş kafesi",
       "Lufadan yapılmış banyo eldiveni", "Sazdan örülmüş arı kovanı"], "E", T_O,
      "Fasıl 46 Not 2, Fasıl 94’teki eşyayı (mobilya, lamba vb.) fasıl dışında bırakır; rattan koltuk oturmaya mahsus mobilya olarak Fasıl 94’tedir. Meyve sepeti, kuş kafesi, arı kovanı ve lufadan eşya 46.02 Açıklama Notunda açıkça sayılmıştır.",
      "Fasıl 46 Not 2; 46.02 Açıklama Notu."),
    # 4
    q("Aşağıdakilerden hangisi diğerlerinden farklı bir fasılda yer alır?",
      "Sisal lifinden örülmüş sicim",
      ["Rafyadan örülmüş el çantası", "Saman örgüsünden yapılmış hasır",
       "Bambu şeritlerinden yapılmış paravan",
       "Görünür genişliği 8 mm olan plastik şeritlerden örülmüş alışveriş sepeti"], "A", T_F,
      "Sicim, kordon, ip ve halatlar örülmüş olsun olmasın 56.07’dedir (Fasıl 46 Not 2). Rafya çanta ve plastik şerit sepet 46.02’de, hasır ve paravan 46.01’dedir. 5 mm’yi aşan plastik şeritler Fasıl 54 şeridi sayılmadığından örülmeye elverişli maddedir.",
      "Fasıl 46 Not 1 ve Not 2; Fasıl 46 Genel Açıklamalar."),
    # 5
    q("Saman saplarının birbirine paralel dizilip sicimle birleştirilmesiyle yapılmış, bahçecilikte kullanılan kaba hasır hangi pozisyonda yer alır?",
      "46.01", ["46.02", "14.01", "56.07", "57.02"], "C", T_E,
      "46.01, düz dokunmuş veya birbirine paralel hale getirilmiş örülmeye elverişli maddelerden hasır, paspas ve paravanları kapsar; Açıklama Notu bahçecilikte kullanılan saman hasırı gibi kaba hasırları açıkça sayar. Bağlayıcının sicim olması pozisyonu değiştirmez (Not 3). Sepet gibi şekil verilmiş eşya olmadığından 46.02’ye girmez; ham sap ise 14.01’de kalırdı.",
      "Fasıl 46 Not 3; 46.01 Açıklama Notu (B)."),
    # 6
    q("Fasıl 46 Not 2’ye göre aşağıdakilerden hangileri, örülmeye elverişli maddelerden yapılmış olsa bile bu fasıl kapsamı dışındadır? I. 48.14 pozisyonundaki duvar kaplamaları II. Sepetçi eşyasından taşıt karoseri gövdeleri III. Kuş kafesleri IV. Lambalar ve aydınlatma cihazları",
      "I, II ve IV", ["I ve III", "II ve III", "II, III ve IV", "I, III ve IV"], "B", T_C,
      "Not 2; 48.14’teki duvar kaplamalarını, sicim ve halatları, ayakkabı ve başlıkları, sepetçi eşyasından nakil vasıtaları ve karoseri gövdelerini (Fasıl 87) ve Fasıl 94 eşyasını (mobilya, lamba, aydınlatma cihazları) hariç tutar. Kuş kafesleri ise 46.02 Açıklama Notunda sepetçi eşyası olarak sayılmıştır (III yanlış).",
      "Fasıl 46 Not 2; 46.02 Açıklama Notu."),
    # 7
    q("Aşağıdakilerden hangisi 46.02 pozisyonunda <b>yer almaz</b>?",
      "Birbirine geçirilmemiş yonga odundan yapılmış talaş sepeti",
      ["Yonga odunun birbirine geçirilmesiyle yapılmış sepet",
       "Buğday sapından yapılmış koni biçimli şişe mahfazası",
       "Kadın şapkacılığına mahsus örgü motifler (67.02’dekiler hariç)",
       "Hasırdan yapılmış halı dövücüsü"], "D", T_O,
      "46.02 Açıklama Notu, yonga odunun birbirine geçirilmesiyle yapılan sepetleri kapsar; birbirine geçirilmemiş yonga odundan talaş sepetlerini ise 44.15’e gönderir. Buğday sapından şişe mahfazaları, şapkacılık motifleri ve halı dövücüleri 46.02’de açıkça sayılmıştır.",
      "46.02 Açıklama Notu; 44.15 Açıklama Notu."),
    # 8
    q("Fasıl 46 Genel Açıklamalarına göre aşağıdaki plastik ürünlerden hangisi örülmeye elverişli madde <b>sayılmaz</b> ve bundan yapılan eşya Bölüm XI’de değerlendirilir?",
      "Enine kesiti 1 mm’yi geçmeyen monofilament",
      ["Enine kesiti 2 mm olan monofilament", "Görünür genişliği 6 mm olan plastik şerit",
       "Görünür genişliği 8 mm olan plastik şerit",
       "Dokumaya elverişli özü kalınca bir plastik tabakayla kaplanmış ve lif karakterini kaybetmiş şerit"], "A", T_N,
      "Genel Açıklamalara göre enine kesiti 1 mm’yi geçmeyen monofilamentler ile genişliği 5 mm’yi aşmayan şerit ve yassılaştırılmış tüpler dokuma maddesi olup Bölüm XI’e aittir. Daha kalın monofilamentler ve 5 mm’yi aşan şeritler örülmeye elverişli maddedir. Plastikle kaplanarak lif karakterini kaybetmiş tekstil özlü maddeler de örülmeye elverişli sayılır.",
      "Fasıl 46 Not 1; Fasıl 46 Genel Açıklamalar."),
    # 9
    q("Lufadan (lif kabağı) yapılmış, iç kısmı bezle astarlanmış masaj eldiveni hangi pozisyonda sınıflandırılır?",
      "46.02", ["14.04", "61.16", "63.07", "96.03"], "E", T_E,
      "46.02 metni lufadan yapılmış eşyayı açıkça kapsar; Açıklama Notu eldiven ve tamponları astarlanmış olsun olmasın bu pozisyonda sayar. Astar bezinin varlığı eşyayı mensucat eşyası (61.16, 63.07) yapmaz. Süpürge ve fırçalar 96.03’tedir.",
      "46.02 pozisyon metni ve Açıklama Notu (iii)."),
    # 10
    q("Söğüt çubuklarından örülmüş bir sepetin gövdesi, kapağı ve kulpları ayrı ayrı örülmüş olup monte edilmemiş halde aynı ambalajda birlikte sunulmaktadır. Eşyanın bitmiş sepet olarak 46.02 pozisyonunda sınıflandırılmasını sağlayan kural hangisidir?",
      "GYK 2(a)", ["GYK 3(a)", "GYK 2(b)", "GYK 3(c)", "GYK 5(b)"], "C", T_G,
      "GYK 2(a), bir eşyaya yapılan atfın o eşyanın monte edilmeden veya sökülerek getirilmiş olanlarını da kapsadığını hükme bağlar; parçaları birlikte sunulan sepet bitmiş sepet gibi 46.02’de sınıflandırılır. 2(b) madde karışımları, 3(a) ve 3(c) birden çok pozisyona girebilen eşya, 5(b) ambalaj içindir.",
      "GYK 2(a); 46.02 pozisyon metni."),
    # 11
    q("Tarife Cetveline göre aşağıdaki hint kamışı (rattan) eşyasından hangisi diğerlerinden farklı bir pozisyonda yer alır?",
      "Rattan şeritlerinden düz dokunmuş paspas",
      ["Rattandan örülmüş servis tepsisi", "Rattandan örülmüş şişe tutacağı",
       "Rattandan örülmüş, astarlı kapaklı el çantası", "Rattandan örülmüş, halkalı kapaklı balık sepeti"], "A", T_F,
      "Düz dokunmuş veya paralel birleştirilmiş örülmeye elverişli maddelerden hasır, paspas ve paravan gibi levha halindeki eşya 46.01’dedir. Tepsi, şişe tutacağı, el çantası ve balık sepeti şekil verilmiş sepetçi eşyası olarak 46.02’dedir.",
      "46.01 ve 46.02 pozisyon metinleri ve Açıklama Notları."),
    # 12
    q("Buğday sapları birbirine paralel dizilip metal tellerle düzenli aralıklarla birleştirilerek sıkıştırılmış; ürünün bütün yüzeyleri ve kenarları kraft kartonu ile kaplanmıştır. Ürün inşaatta bölme panosu olarak kullanılacaktır. Tarife Cetveline göre bu ürün hangi pozisyonda sınıflandırılır?",
      "46.01", ["68.08", "44.10", "46.02", "48.14"], "D", T_S,
      "46.01 Açıklama Notu; paralel dizilip metal tellerle düzenli aralıklarla birleştirilmiş, sıkıştırılmış buğday sapı, kamış vb. maddelerden inşaat panolarını sayar ve bütün yüzey ve kenarlarının kraft kartonla kaplanabileceğini belirtir. Mineral bağlayıcı olmadığından 68.08’e, ağaç yongası olmadığından 44.10’a girmez; levha karakteri taşıdığından 46.02 değildir.",
      "46.01 Açıklama Notu (B)."),
    # 13
    q("Aşağıdaki eşya – pozisyon veya fasıl eşleştirmelerinden hangisi <b>yanlıştır</b>?",
      "Sepetçi eşyasından atık kağıt sepeti – Fasıl 94",
      ["Hasırdan örülmüş şapka – Fasıl 65", "Tabanı hasırdan örülmüş espadril – Fasıl 64",
       "Örülmeye elverişli maddeden yapılmış kamçı – 66.02", "Örülmeye elverişli maddeden yapma çiçek – 67.02"], "B", T_B,
      "Sepetçi eşyasından atık kağıt sepetleri mobilya değildir; Fasıl 94 açıklamaları bunları 46.02’ye gönderir. Hasır şapka Fasıl 65’te, espadril Fasıl 64’te, kamçı 66.02’de, yapma çiçek 67.02’dedir; bunların hepsi Fasıl 46 notları ve Genel Açıklamaları ile fasıl dışında bırakılmıştır.",
      "Fasıl 46 Not 2 ve Genel Açıklamalar; Fasıl 94 Genel Açıklamalar."),
    # 14
    q("Aşağıdakilerden hangisi 46.01 pozisyonunda <b>sınıflandırılmaz</b>?",
      "Dokunmuş mensucattan tabanı olan, hindistan cevizi lifinden kapı paspası",
      ["Döşemecilikte kullanılan, şerit halindeki rafya örgüsü",
       "Ezilmemiş bitkisel maddelerin basitçe bükülmesiyle elde edilen “Çin ipi” türü ürün",
       "Bambu şeritlerinden düz dokunmuş paravan",
       "Hasır şeritlerinin paralel dizilip sicimle birleştirilmesiyle yapılmış yer hasırı"], "E", T_O,
      "46.01 Açıklama Notu, iplerden veya dokunmuş mensucattan bir tabana sahip hindistan cevizi veya sisal lifinden hasır ve paspasları hariç tutar ve Fasıl 57’ye gönderir. Rafya örgüsü, Çin ipi türü ürünler, düz dokunmuş paravan ve paralel birleştirilmiş hasır 46.01 kapsamındadır.",
      "46.01 Açıklama Notu (A), (B) ve hariç tutma."),
    # 15
    q("Fasıl 46 Not 3’e göre 46.01 pozisyonundaki “birbirine paralel şekilde birleştirilmiş örülmeye elverişli maddeler” tabiri ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
      "Paralel teller halinde levha şeklinde birleştirilmiş maddelerdir; bağlayıcının iplik olması önemli değildir.",
      ["Bağlayıcı madde iplik haline getirilmiş dokumaya elverişli maddeden ise eşya 46.01’de değil 46.02’de yer alır.",
       "Yalnızca birbirine dik açıyla dokunmuş örgü maddelerini kapsar.",
       "Sadece tamamlanmış hasır ve paspasları kapsar; tamamlanmamış levhalar 14.01’e girer.",
       "Levha halinde birleştirilen maddeler sepetçi eşyası sayılarak 46.02’ye girer."], "C", T_N,
      "Not 3’e göre bu tabir, yan yana getirilmiş ve birbirine paralel teller halinde birleştirilmiş levha halindeki örülmeye elverişli maddeleri, örgüleri ve benzeri eşyayı ifade eder; bağlayıcı maddelerin iplik haline getirilmiş dokumaya elverişli maddelerden olup olmaması önemli değildir. 46.01 metni de eşyanın tamamlanmış olup olmamasını aramaz.",
      "Fasıl 46 Not 3; 46.01 pozisyon metni."),
    # 16
    q("Henüz örülmemiş, yalnızca boyuna yarılmış ve parlatılmış, örgü işlerinde kullanılmak üzere demetler halinde sunulan bambu kamışları hangi pozisyonda yer alır?",
      "14.01", ["46.01", "44.04", "46.02", "44.21"], "B", T_E,
      "Örgüye mahsus bitkisel maddeler işlenmemiş veya yarılmış, parlatılmış, boyanmış halde 14.01’dedir; Fasıl 44 Not 1 işlenmemiş bambuyu Fasıl 44’ten çıkarır. Fasıl 46’ya girmesi için örülmüş, birbirine geçirilmiş veya birleştirilmiş olması gerekir. 44.04 ahşap çember ve sırıklar içindir.",
      "Fasıl 46 Genel Açıklamalar; Fasıl 44 Not 1; 14.01 pozisyon metni."),
    # 17
    q("Aşağıdaki bambu veya bitkisel madde ürünlerinden hangisi diğerlerinden farklı bir fasılda yer alır?",
      "Bambu katlarından yapılmış kontrplak",
      ["Sazdan örülmüş paspas", "Bambu şeritlerinden örülmüş sepet",
       "Rafyadan örülmüş alışveriş çantası", "Söğüt sürgünlerinden örülmüş kuş kafesi"], "E", T_F,
      "Fasıl 46 Genel Açıklamaları Fasıl 44’teki bambudan eşyayı hariç tutar; Fasıl 44 Not 6 gereği bambu kontrplak 44.12’dedir. Saz paspas 46.01’de; bambu sepet, rafya çanta ve söğüt kuş kafesi 46.02’de yer alır.",
      "Fasıl 46 Genel Açıklamalar; Fasıl 44 Not 6."),
    # 18
    q("Aşağıdaki ifadelerden hangileri doğrudur? I. İplik haline getirilmemiş dokumaya elverişli tabii lifler örülmeye elverişli madde sayılır. II. Dokumaya elverişli fitiller, tamamen plastikle kaplanmadıkça örülmeye elverişli madde sayılmaz. III. Örülmüş halde olan sicim, kordon ve halatlar Fasıl 46’da yer alır. IV. Örülmeye elverişli maddeler, örülmeyi kolaylaştırmak için yarma, soyma veya mum ya da gliserin emdirme gibi hazırlayıcı işlemlere tabi tutulabilir.",
      "I, II ve IV", ["I ve III", "II ve III", "I, III ve IV", "II, III ve IV"], "C", T_C,
      "Not 1 iplik haline getirilmemiş tabii lifleri kapsar (I). Genel Açıklamalar dokumaya elverişli fitilleri, tamamen plastikle kaplı oldukları durum hariç, örülmeye elverişli madde saymaz (II). Hazırlayıcı işlemler (yarma, çekme, soyma, mum veya gliserin emdirme) mümkündür (IV). Sicim ve halatlar örülmüş olsalar da 56.07’dedir (III yanlış).",
      "Fasıl 46 Not 1 ve Not 2; Fasıl 46 Genel Açıklamalar."),
    # 19
    q("Örülmeye elverişli maddelerden yapılmış olsa bile aşağıdakilerden hangisi Fasıl 46’da <b>yer almaz</b>?",
      "Süpürge",
      ["Şişe tutacağı", "Tepsi", "Istakoz kabı", "Balık sepeti"], "A", T_O,
      "Fasıl 46 Genel Açıklamaları süpürge ve fırçaları hariç tutar; bunlar 96.03’tedir. Şişe tutacağı, tepsi, ıstakoz kabı ve balık sepeti 46.02 Açıklama Notunda sepetçi eşyası olarak sayılmıştır.",
      "Fasıl 46 Genel Açıklamalar; 46.02 Açıklama Notu."),
    # 20
    q("Rafya şeritlerinden örülmüş, astarlanmış ve şerit ile donatılmış yazlık şapka hangi pozisyonda sınıflandırılır?",
      "65.04", ["46.02", "46.01", "14.01", "65.07"], "D", T_E,
      "Fasıl 46 Not 2 Fasıl 65’teki başlıkları hariç tutar; 65.04 her nevi maddeden şeritlerin birleştirilmesi veya örülmesi suretiyle yapılmış şapkaları, astarlanmış veya donatılmış olsun olmasın kapsar. 65.07 yalnız başlıkların iç şerit, astar, siperlik gibi aksamı içindir. Rafya örgüsünün kendisi 46.01’de kalırdı.",
      "Fasıl 46 Not 2; 65.04 pozisyon metni."),
    # 21
    q("“Örülmeye elverişli maddelerden örgüler ve hasır, paspas, paravan gibi levha halindeki eşya ……… pozisyonunda; örülmeye elverişli maddelerden doğrudan şekil verilerek veya bu eşyadan yapılmış sepetçi eşyası ile ……… eşya 46.02 pozisyonunda sınıflandırılır.” Cümlesindeki boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?",
      "46.01 – lufadan yapılmış",
      ["14.01 – rafyadan yapılmış", "46.02 – lufadan yapılmış",
       "46.01 – deri şeritten yapılmış", "44.21 – mantardan yapılmış"], "C", T_B,
      "46.01 örgüleri ve düz dokunmuş veya paralel birleştirilmiş levha halindeki eşyayı (hasır, paspas, paravan) kapsar. 46.02 ise sepetçi eşyası ile lufadan yapılmış eşyayı içerir. Deri şeritler örülmeye elverişli madde sayılmaz; mantar eşyası Fasıl 45’tedir.",
      "46.01 ve 46.02 pozisyon metinleri; Fasıl 46 Not 1."),
    # 22
    q("Hint kamışından örülmüş sandalye, örülmeye elverişli maddeden olmasına rağmen Fasıl 46 yerine 94.01 pozisyonunda sınıflandırılır. Bu sonuca götüren dayanak aşağıdakilerden hangisidir?",
      "GYK 1 – pozisyon metinleri ve Fasıl 46 Not 2",
      ["GYK 3(b) – eşyaya esas niteliğini veren madde", "GYK 3(c) – numara sırasına göre son pozisyon",
       "GYK 2(b) – karışım ve bileşik maddeler", "GYK 4 – en çok benzeyen eşya"], "E", T_G,
      "GYK 1’e göre sınıflandırma pozisyon metinleri ile bölüm ve fasıl notlarına göre yapılır. Fasıl 46 Not 2, Fasıl 94’teki mobilyayı fasıl dışında bıraktığından ve 94.01 oturmaya mahsus mobilyayı her maddeden kapsadığından sandalye 94.01’e girer. Not ile çözülen durumda 3. ve 4. kurallara başvurulmaz.",
      "GYK 1; Fasıl 46 Not 2; Fasıl 94 Genel Açıklamalar."),
    # 23
    q("Aşağıdaki eşya çiftlerinden hangisinde her iki eşya da aynı pozisyonda yer alır?",
      "Söğütten örülmüş küfe – Rafyadan örülmüş çanta",
      ["İşlenmemiş rattan – Rattan sepet", "Saman örgüsü – Saman örgüsünden sepet",
       "Bambu hasır – Bambu kontrplak", "Hasırdan örülmüş şapka – Hasırdan örülmüş sepet"], "D", T_F,
      "Küfe ve el çantası şekil verilmiş sepetçi eşyası olarak 46.02’dedir. İşlenmemiş rattan 14.01, rattan sepet 46.02; saman örgüsü 46.01, ondan sepet 46.02; bambu hasır 46.01, bambu kontrplak 44.12; hasır şapka Fasıl 65, hasır sepet 46.02’dedir.",
      "46.01 ve 46.02 Açıklama Notları; Fasıl 46 Not 2 ve Genel Açıklamalar."),
    # 24
    q("Fasıl 46 Genel Açıklamalarına göre aşağıdakilerden hangisi <b>yanlıştır</b>?",
      "Bambudan mamul eşyanın tamamı, sepetçi eşyası olsun olmasın, Fasıl 46’da sınıflandırılır.",
      ["Saraciye ve koşum takımları bu fasılda yer almaz.",
       "Atkısı olmayan, yapıştırıcıyla birleştirilmiş çözgüden oluşan dar mensucat (boldük) 58.06’da yer alır.",
       "Terzi mankenleri bu fasıl kapsamı dışındadır.",
       "Dokumaya elverişli özü plastik şeritlerle sarılarak lif karakterini kaybetmiş maddeler örülmeye elverişli madde sayılır."], "A", T_N,
      "Genel Açıklamalar Fasıl 44’te yer alan bambudan eşyayı açıkça hariç tutar; bambu yalnız örülmeye elverişli madde olarak kullanıldığında Fasıl 46’ya girer. Saraciye (42.01), boldük (58.06) ve terzi mankenleri (96.18) fasıl dışındadır; plastikle kaplanarak lif karakterini kaybetmiş tekstil özlü maddeler ise örülmeye elverişli madde sayılır.",
      "Fasıl 46 Genel Açıklamalar."),
    # 25
    q("Muz yapraklarından kesilmiş şeritler, tekstil ipliğinden bir atkı ile düz dokunarak levha haline getirilmiştir; tekstil ipliğinin renk etkisi dışında tek işlevi şeritleri birleştirmektir. Kenarları tamamlanmış ürün, yere serilen dikdörtgen bir hasırdır. Bu ürün hangi pozisyonda sınıflandırılır?",
      "46.01", ["46.02", "57.02", "14.01", "63.04"], "B", T_S,
      "46.01 Açıklama Notuna göre örülmüş eşya, örgü maddelerinden bir çözgü ve tekstil ipliğinden bir atkıdan oluşabilir; yeter ki tekstil ipliğinin renk dışındaki tek işlevi örgü maddelerini birleştirmek olsun. Muz veya palmiye yapraklarından kesilmiş şeritler Genel Açıklamalarda örülmeye elverişli madde olarak sayılmıştır. Ürün levha karakterli hasır olduğundan 46.02’ye değil 46.01’e girer; tekstil ipliği onu dokunmuş halı (57.02) yapmaz.",
      "Fasıl 46 Not 1 ve Not 3; 46.01 Açıklama Notu (B)."),
]

obj = {
    "tur": "fasil",
    "fasil": 46,
    "baslik": "Hasırdan, sazdan veya örülmeye elverişli diğer maddelerden mamuller; sepetçi ve hasırcı eşyası",
    "bolum": "IX",
    "oz": {
        "vurgu": "Fasıl 46’nın anahtarı “örülmeye elverişli madde” tanımıdır (Not 1). Bu maddelerden örgüler ve düz dokunmuş ya da paralel birleştirilmiş levha halindeki hasır, paspas, paravan 46.01’de; doğrudan şekil verilerek veya 46.01 eşyasından yapılan sepetçi eşyası ile lufadan eşya 46.02’dedir. Mobilya, ayakkabı, şapka, sicim-halat, oyuncak ve süpürge örgüden yapılsa da başka fasıllara gider.",
        "maddeler": [
            "Örülmeye elverişli madde: hasır, söğüt ve sepetçi söğüdü, bambu, hint kamışı, saz, kamış, ağaç şeritleri, bitkisel şeritler (rafya, dar yapraklar, geniş yapraklardan kesilmiş şeritler), iplik haline getirilmemiş tabii lifler, plastik monofilament ve şeritler, kağıt şeritler.",
            "Sayılmayanlar: deri, terkip deri, keçe ve dokunmamış mensucat şeritleri, insan saçı, at kılı, dokumaya elverişli fitil ve iplikler, Fasıl 54 monofilament ve şeritleri (enine kesiti 1 mm’yi geçmeyen monofilament; genişliği 5 mm’yi aşmayan şerit).",
            "Ham, örülmemiş bitkisel örgü maddeleri 14.01’dedir; Fasıl 46 için örülmüş, birbirine geçirilmiş veya birleştirilmiş olmaları gerekir.",
            "Örgüyü birleştiren bağlayıcının tekstil ipliği olması 46.01’i bozmaz; ipliğin renk dışındaki tek işlevi birleştirmek olmalıdır (Not 3)."
        ]
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Malzeme Not 1 anlamında örülmeye elverişli madde değil mi? (deri şerit, keçe, at kılı, insan saçı, iplik, fitil, Fasıl 54 monofilament ve şeridi)", "Fasıl 46 dışı (genellikle Bölüm XI veya Fasıl 41–42)"],
            ["2", "Henüz örülmemiş, birleştirilmemiş ham bitkisel örgü maddesi mi?", "<b>14.01</b>"],
            ["3", "Mobilya, lamba, ayakkabı, başlık, taşıt gövdesi, oyuncak, süpürge, kamçı, yapma çiçek mi?", "Fasıl 94 / 64 / 65 / 87 / 95 · <b>96.03</b> · <b>66.02</b> · <b>67.02</b>"],
            ["4", "Sicim, kordon, ip, halat (örülmüş olsun olmasın) ya da 48.14’teki duvar kaplaması mı?", "<b>56.07</b> / <b>48.14</b>"],
            ["5", "İplik veya dokunmuş mensucat tabanlı hindistan cevizi ya da sisal lifinden paspas mı?", "Fasıl 57"],
            ["6", "Bambudan Fasıl 44 ürünü mü? (kontrplak, yonga levha, odun kömürü)", "Fasıl 44"],
            ["7", "Örgü, örgüye benzer ürün ya da levha halinde hasır, paspas, paravan, inşaat panosu mu?", "<b>46.01</b>"],
            ["8", "Sepet, küfe, çanta, kafes, tepsi gibi şekil verilmiş eşya ya da lufadan eşya mı?", "<b>46.02</b>"]
        ],
        "dipnot": ""
    },
    "pozisyon_haritasi": [
        ["46.01", "Örgüler; levha halinde hasır, paspas, paravan", "Düz dokunmuş veya paralel birleştirilmiş; tamamlanmış olsun olmasın", "Saman örgüsü, Çin ipi, bahçe hasırı, saz paspas"],
        ["46.02", "Sepetçi eşyası; lufadan eşya", "Doğrudan şekil verilmiş veya 46.01 eşyasından yapılmış", "Sepet, küfe, örgü çanta, kuş kafesi, lufa eldiven"]
    ],
    "notlar": [
        ["Fasıl 46 Not 1", "“Örülmeye elverişli madde”: örülmeye, birbirine geçirmeye ve benzeri işlemlere uygun durum veya şekildeki maddeler; hasır, söğüt veya sepetçi söğüdü sürgünleri, bambu, benekli hint kamışı, saz sapları, kamışlar, ağaç şeritleri, bitkisel şeritler (ağaç kabuğu şeritleri, dar yapraklar, rafya, yayvan yapraklardan şeritler), iplik haline getirilmemiş tabii dokuma lifleri, plastikten monofilament ve şeritler, kağıttan şeritler. Kapsamaz: deri, terkip deri, keçe veya dokunmamış mensucattan şeritler, insan saçı, at kılı, dokumaya elverişli fitil veya iplikler, Fasıl 54’teki monofilament ve şeritler."],
        ["Fasıl 46 Not 2", "Fasıl dışı: 48.14’teki duvar kaplamaları; sicim, kordon, ip ve halatlar (örülmüş olsun olmasın) (56.07); Fasıl 64 veya 65’teki ayakkabı ve başlıklar ile aksamı; sepetçi eşyasından nakil vasıtaları ve karoseri gövdeleri (Fasıl 87); Fasıl 94 eşyası (mobilya, lamba, aydınlatma cihazları)."],
        ["Fasıl 46 Not 3", "46.01 anlamında “birbirine paralel şekilde birleştirilmiş örülmeye elverişli maddeler, örgüler ve benzeri eşya”: yan yana getirilip paralel teller halinde levha şeklinde birleştirilmiş örülmeye elverişli maddeler ve örgüler; bağlayıcı maddeler iplik haline getirilmiş dokumaya elverişli maddeden olsun olmasın."],
        ["Genel Açıklamalar", "Plastik monofilament ve şeritler örülmeye elverişlidir; ancak enine kesiti <b>1 mm’yi geçmeyen</b> monofilamentler ile genişliği <b>5 mm’yi aşmayan</b> şerit ve yassılaştırılmış tüpler (suni saman dahil) dokuma maddesidir (Bölüm XI). Tekstil özü plastikle kaplanıp lif karakterini kaybetmiş maddeler örülmeye elverişli sayılır."],
        ["Genel Açıklamalar", "Örülmeye elverişli maddeler örmeyi kolaylaştırmak için yarma, çekme, soyma veya mum, gliserin vb. emdirme gibi hazırlayıcı işlemlere tabi tutulabilir."],
        ["Genel Açıklamalar", "Ayrıca fasıl dışı: saraciye ve koşum takımları (42.01); Fasıl 44’teki bambudan eşya; boldük (58.06); kamçılar (66.02); yapma çiçekler (67.02); Fasıl 95 eşyası; süpürge ve fırçalar (96.03); terzi mankenleri (96.18)."],
        ["46.01 Açıklama Notu", "(A) Örgüler: çözgü ve atkı olmadan birbirine geçirilerek uzunlamasına devam eden şeritler; yan yana dikilerek genişletilebilir. Örgüye benzer ürünler: iki veya daha çok telin bükülmesiyle veya ezilmemiş bitkisel maddelerin basitçe bükülmesiyle (“Çin ipi”) elde edilenler. (B) Levha halinde eşya: hasırlar, paspaslar, paravanlar, bahçe hasırları, kraft kartonla kaplanabilen inşaat panoları."],
        ["46.01 Açıklama Notu", "Örülmüş eşya örgü maddesi çözgü ve tekstil ipliği atkıdan (veya tersinden) oluşabilir; yeter ki tekstil ipliğinin renk dışındaki tek işlevi örgü maddelerini birleştirmek olsun. İplerden veya dokunmuş mensucattan tabanı olan hindistan cevizi veya sisal lifinden hasır ve paspaslar Fasıl 57’dedir."],
        ["46.02 Açıklama Notu", "Doğrudan örgü maddelerinden veya 46.01 ürünlerinden yapılan eşya ile lufadan eşya (astarlanmış olsun olmasın): sepet, küfe, balık ve meyve sepeti, seyahat ve el çantaları, ıstakoz kapları, kuş kafesleri, arı kovanları, tepsiler, şişe tutacakları, halı dövücüleri, şapkacılık motifleri, şişe mahfazaları. Birbirine geçirilmemiş yonga odundan talaş sepetleri 44.15’tedir; 46.01’in levha halindeki tamamlanmış eşyası 46.02’ye girmez."]
    ],
    "sinir_komsulari": [
        ["İşlenmemiş veya yarılmış bambu, rattan, saz, söğüt dalı", "14.01", "Henüz örülmemiş örgü maddesi"],
        ["Bambu kontrplak, bambu yonga levha, bambu odun kömürü", "44.12 / 44.10 / 44.02", "Fasıl 44 Not 6; Fasıl 46 Genel Açıklamalar"],
        ["Birbirine geçirilmemiş yonga odundan talaş sepeti", "44.15", "46.02 hariç tutması"],
        ["Deri şeritlerden örülmüş eşya", "Fasıl 42", "Deri şerit örülmeye elverişli madde değildir"],
        ["Saraciye ve koşum takımı", "42.01", "Genel Açıklamalar"],
        ["Örgü maddesinden duvar kaplaması", "48.14", "Not 2"],
        ["Örülmüş sicim, kordon, halat", "56.07", "Not 2"],
        ["Dokunmuş tabanlı hindistan cevizi lifi paspası", "Fasıl 57", "46.01 hariç tutması"],
        ["Hasır tabanlı espadril; hasır şapka", "Fasıl 64 / 65.04", "Not 2"],
        ["Kamçı; yapma çiçek", "66.02 / 67.02", "Genel Açıklamalar"],
        ["Sepetçi eşyasından taşıt gövdesi", "Fasıl 87", "Not 2"],
        ["Rattan koltuk, hasır sandalye, bambu sehpa", "94.01 / 94.03", "Not 2; Fasıl 94 her maddeden mobilyayı kapsar"],
        ["Hasır oyuncak", "Fasıl 95", "Genel Açıklamalar"],
        ["Hasır sazından veya bambudan süpürge", "96.03", "Genel Açıklamalar"],
        ["Hasır kaplı terzi mankeni", "96.18", "Genel Açıklamalar"]
    ],
    "tuzaklar": [
        "<b>Ham bambu 14.01, örülmüş bambu Fasıl 46, levha veya kömür bambu Fasıl 44.</b> Örülmemiş yarılmış, parlatılmış bambu 14.01’dedir; bambu kontrplak 44.12’ye gider.",
        "<b>Örgü mobilya Fasıl 94’tür.</b> Rattan koltuk, hasır sandalye, bambu sehpa örgü maddesinden olsa da Not 2 gereği mobilyadır.",
        "<b>Deri şerit örgü maddesi değildir.</b> Deri, terkip deri, keçe, dokunmamış mensucat şeritleri, at kılı ve insan saçından örülen eşya Fasıl 46’ya girmez.",
        "<b>Plastik şeritte 5 mm, monofilamentte 1 mm.</b> Genişliği 5 mm’yi aşmayan şerit ve enine kesiti 1 mm’yi geçmeyen monofilament dokuma maddesidir (Bölüm XI); daha kalın ve geniş olanlar örülmeye elverişlidir.",
        "<b>Örülmüş sicim 56.07’dir.</b> Sicim, kordon, ip ve halat örülmüş olsalar da Not 2 ile Fasıl 46 dışına çıkar.",
        "<b>Levha mı, şekil mi?</b> Hasır, paspas, paravan gibi levha halindeki eşya tamamlanmış olsa da 46.01; sepet, çanta, kafes gibi şekil verilmiş eşya 46.02. Ancak uzun örgülerin kare veya daire halinde sicimle birleştirilmesiyle yapılan hasırlar 46.02 Açıklama Notunda sayılmıştır.",
        "<b>Tekstil ipliği yalnız birleştiriyorsa 46.01 bozulmaz.</b> Örgü maddesi çözgü, tekstil ipliği atkı olabilir; ipliğin tek işlevi birleştirmek olmalıdır.",
        "<b>Hindistan cevizi lifi paspası tabana bakar.</b> İplik veya dokunmuş mensucat tabanı varsa Fasıl 57; yoksa örgü maddesinden paspas olarak 46.01.",
        "<b>Lufa 46.02’dedir.</b> Lufadan eldiven ve tamponlar astarlı olsa da sepetçi eşyası ile birlikte 46.02’de yer alır.",
        "<b>Yonga odunu: geçirilmiş mi?</b> Birbirine geçirilerek yapılan sepet 46.02; geçirilmemiş yonga odundan talaş sepeti 44.15."
    ],
    "hafiza": {
        "kanca": "SERİLİR – DOLDURULUR",
        "aciklama": "<b>46.01 serilir</b>: örgü şeridi, hasır, paspas, paravan; yere, duvara, şapka atölyesine düz giden levhalar. <b>46.02 doldurulur</b>: sepet, küfe, çanta, kafes, kovan; içine bir şey konan şekilli eşya, yanında da lufa. Ham sap 14.01’de bekler; üstüne oturulursa 94’e, başa giyilirse 65’e, ayağa giyilirse 64’e gider."
    },
    "sinav_odagi": [
        "Bu fasıl çıkmış sorularda daha çok seçeneklerde ve çeldirici olarak yer almıştır; doğrudan pozisyon sorusu azdır.",
        "Bölüm bilgisi: sepetçi ve hasırcı eşyasının Bölüm X’da değil Bölüm IX’da (44–46. fasıllar) yer aldığı, sepetçi eşyası pozisyonuna ait bir kodla “hangisi söylenemez?” kalıbında sorulmuştur.",
        "Bölüm–fasıl eşleştirmesi: dokumaya elverişli maddeler sorusunda “Dokuzuncu bölüm, 44–46. fasıllar” çeldirici seçenek olarak kullanılmıştır.",
        "Örgü veya bambu yüzeyli, metal ayaklı sehpa: örgü maddesinden olsa da mobilya olduğu için Fasıl 94’te sınıflandırıldığı, GYK seçimiyle birlikte sorulmuştur."
    ],
    "cikmis_ornekler": [
        {
            "soru": "Dokumaya elverişli maddeler ve bunlardan mamul eşya Türk Gümrük Tarife Cetvelinin hangi bölüm ve hangi fasıllarında yer almaktadır?",
            "secenekler": ["Dördüncü bölüm, 16-24 fasıl", "Yedinci bölüm, 39-40 fasıl", "Dokuzuncu bölüm, 44-46 fasıl", "On birinci bölüm, 50-63 fasıl"],
            "cevap": "D",
            "aciklama": "Dokumaya elverişli maddeler Bölüm XI’dedir (Fasıl 50–63). Bölüm IX (Fasıl 44–46) ağaç, mantar ve hasır ile sepetçi eşyasını kapsar; iplik haline getirilmemiş tabii lifler ancak örülmeye elverişli madde olarak kullanıldığında Fasıl 46 eşyası olabilir."
        }
    ],
    "ozet": [
        "Önce malzemeye bak: Not 1’deki örülmeye elverişli maddelerden mi? Deri şerit, keçe, at kılı, insan saçı, iplik ve ince plastik (1 mm / 5 mm) değil.",
        "Ham örgü maddesi 14.01; örgü ve levha halindeki hasır, paspas, paravan 46.01; şekil verilmiş sepetçi eşyası ve lufa 46.02.",
        "Bağlayıcının tekstil ipliği olması 46.01’i bozmaz; tek işlevi birleştirmek olmalıdır.",
        "Mobilya 94, ayakkabı 64, şapka 65, sicim-halat 56.07, duvar kaplaması 48.14, süpürge 96.03, oyuncak 95.",
        "Bambudan Fasıl 44 ürünleri (kontrplak, levha, kömür) Fasıl 46 dışındadır."
    ],
    "sorular": sorular,
}

yaz(46, obj)
