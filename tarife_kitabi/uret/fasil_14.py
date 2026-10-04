from yardim_14_18 import q, yaz

T_E = "Eşya → 4’lü pozisyon"
T_O = "Olumsuz teşhis"
T_F = "Farklı/aynı pozisyon veya fasıl"
T_N = "Fasıl notu · Tanım/Eşik"
T_G = "Genel Yorum Kuralı"
T_B = "Eşleştirme / Boşluk doldurma"
T_C = "Çoktan-çoğa (I–IV)"
T_S = "Senaryo"

sorular = [
    # 1
    q("Tarife Cetveline göre, uzunlamasına yarılmış, beyazlatılmış ve yanmaz hale getirilmiş bambu çubukları hangi pozisyonda sınıflandırılır?",
      "14.01", ["44.04", "46.01", "14.04", "46.02"], "C", T_E,
      "Fasıl 14 Not 2’ye göre 14.01; bambuları yarılmış, uzunlamasına biçilmiş, uçları yuvarlaklaştırılmış, beyazlatılmış, yanmaz hale getirilmiş, parlatılmış veya boyanmış olsun olmasın kapsar. 44.04 yonga ve ahşap çubuklar, 46.01 örgüler, 46.02 sepetçi eşyası içindir. 14.04 kalıntı pozisyondur; bambu ise 14.01’de ismen sayılmıştır.",
      "Fasıl 14 Not 2; 14.01 Açıklama Notu."),
    # 2
    q("Aşağıdakilerden hangisi Tarife Cetvelinin 14. faslında <b>sınıflandırılmaz</b>?",
      "Agar-agar", ["Lif kabağı (bitkisel sünger)", "Japon pirinç kağıdı", "Tanbul yaprakları", "Quillaia (sabun ağacı) kabuğu"], "A", T_O,
      "14.04 Açıklama Notu agar-agar, deniz kadayıfı (karragenan) ve bitkisel maddelerden çıkarılan diğer yapışkan ve kıvam verici maddeleri hariç tutar; bunlar 13.02’dedir. Lif kabağı, ağaç özünden dilimlenen Japon pirinç kağıdı, tanbul yaprakları ve quillaia kabuğu ise “diğer bitkisel ürünler” olarak 14.04’te sayılmıştır.",
      "14.04 Açıklama Notu (diğer bitkisel ürünler ve hariç tutmalar)."),
    # 3
    q("Tarife Cetvelinin 14. Fasıl notlarına göre, nasıl hazırlanmış olursa olsun esas itibariyle mensucat imalinde kullanılan bitkisel maddeler ve bitkisel madde lifleri nerede yer alır?",
      "Bölüm XI’de", ["14.01 pozisyonunda", "14.04 pozisyonunda", "Fasıl 46’da", "Fasıl 12’de"], "E", T_N,
      "Fasıl 14 Not 1’e göre esas itibariyle mensucat imalinde kullanılan bitkisel maddeler ve lifler ile yalnızca mensucat imalinde kullanılabilecek hale getirilmiş diğer bitkisel maddeler bu fasla dahil olmayıp XI. Bölümde yer alır. 14.01 ve 14.04 bu maddeleri kapsamaz; Fasıl 46 örgü ve sepetçi eşyası içindir.",
      "Fasıl 14 Not 1; Fasıl 14 Genel Açıklamalar."),
    # 4
    q("Tarife Cetveline göre, pamuk tohumlarının çırçırlanmasından sonra tohum üzerinde kalan, uzunluğu genellikle 5 mm’den az olan beyazlatılmış kısa lifler (pamuk linterleri) hangi pozisyonda yer alır?",
      "14.04", ["52.01", "56.01", "30.05", "14.01"], "B", T_E,
      "14.04 Açıklama Notuna göre pamuk linterleri; kullanım amaçları ve ham, temiz, beyazlatılmış, boyanmış veya absorbe edici hale getirilmiş olup olmamaları dikkate alınmaksızın 14.04’te sınıflandırılır. Pamuk (52.01) değildir. Tampon haline getirilmiş olanlar tıbbi ise 30.05’e, diğerleri 56.01’e gider; burada tampon söz konusu değildir.",
      "14.04 Açıklama Notu (pamuk linterleri)."),
    # 5
    q("Tarife Cetveline göre aşağıdakilerden hangisi diğerlerinden farklı bir tarife pozisyonunda yer alır?",
      "Kapok", ["Bambu", "Hint kamışı", "Rafya", "Sepetçi söğüdü"], "D", T_F,
      "Bambu, Hint kamışı, rafya ve sepetçi söğüdü özellikle örgü için kullanılan bitkisel maddeler olarak 14.01’dedir. Kapok ise esas olarak dolgu veya vatka olarak kullanılan bitkisel madde olduğundan 14.04’te yer alır. Tuzak, hepsinin ham bitkisel madde olması nedeniyle aynı pozisyonda sanılmasıdır.",
      "14.01 pozisyon metni; 14.04 Açıklama Notu (dolgu maddeleri)."),
    # 6
    q("Tarife Cetvelinin 14. faslı ile ilgili aşağıdaki ifadelerden hangileri doğrudur?  I. Bambular boyanmış veya yanmaz hale getirilmiş olsalar da 14.01 pozisyonunda yer alır.  II. Yonga 14.01 pozisyonunun kapsamındadır.  III. Odun yünü 14.04 pozisyonunda sınıflandırılır.  IV. Esas itibariyle mensucat imalinde kullanılan bitkisel lifler XI. Bölümde yer alır.",
      "I ve IV", ["I ve II", "II ve III", "I, III ve IV", "Yalnız IV"], "A", T_C,
      "I, Fasıl 14 Not 2 ile; IV, Fasıl 14 Not 1 ile doğrudur. II yanlıştır: yonga 14.01’e dahil değildir (44.04). III yanlıştır: odun yünü 14.04’e dahil değildir (44.05, Not 3). Bu nedenle doğru ifadeler yalnız I ve IV’tür.",
      "Fasıl 14 Not 1, Not 2 ve Not 3."),
    # 7
    q("Tarife Cetveline göre, debagatte kullanılmak üzere öğütülerek toz haline getirilmiş mazı yumruları hangi pozisyonda sınıflandırılır?",
      "14.04", ["32.01", "32.03", "12.11", "09.10"], "C", T_E,
      "Esas olarak boyacılıkta veya debagatte kullanılan bitkisel hammaddeler (mazı yumruları dahil) işlem görmemiş, temizlenmiş, kurutulmuş, öğütülmüş veya toz haline getirilmiş olarak 14.04’tedir. 32.01 debagat hülasaları ve tanenleri (su ile çıkarılmış mazı yumrusu taneni dahil), 32.03 boya hülasalarını kapsar; toz haline getirmek hülasa elde etmek değildir.",
      "14.04 Açıklama Notu (boyacılık ve debagat hammaddeleri, mazı yumruları)."),
    # 8
    q("Aşağıdakilerden hangisi Tarife Cetvelinin 14.01 pozisyonunda <b>sınıflandırılmaz</b>?",
      "İnce şeritler halindeki ağaç malzeme (yonga)", ["Rafya", "Ihlamur ağacının iç kabuğu", "Yarılmış sepetçi söğüdü", "Hint kamışı içinden kesilmiş uzun şeritler"], "E", T_O,
      "Fasıl 14 Not 2’ye göre yonga 14.01’e dahil değildir; 44.04 pozisyonunda yer alır. Rafya, ıhlamur iç kabuğu, yarılmış sepetçi söğüdü ve Hint kamışının içinden veya dışından boydan boya kesilen şeritler 14.01 Açıklama Notunda açıkça sayılmıştır.",
      "Fasıl 14 Not 2; 14.01 Açıklama Notu."),
    # 9
    q("Açıklama notlarına göre pamuk linterleri ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
      "Genellikle 5 mm’den kısa liflerdir; absorbe edici olsalar da 14.04’te kalırlar.",
      ["Uzunluğu 15 ila 30 mm olan, elastik ve su geçirmez liflerdir.",
       "Yalnız ham ve temizlenmemiş olanları 14.04 pozisyonunda yer alır.",
       "Beyazlatılmış veya boyanmış olanları Fasıl 52’de sınıflandırılır.",
       "Tabaka veya dilim şeklinde preslenmiş olanları 56.01’de yer alır."], "D", T_N,
      "Linterler çırçırlamadan sonra tohumda kalan, genellikle 5 mm’den kısa liflerdir; ham, temiz, beyazlatılmış, boyanmış veya absorbe edici hale getirilmiş olsun olmasın ve dökme ya da tabaka veya dilim şeklinde preslenmiş olarak 14.04’tedir. 15–30 mm uzunluk kapoka ait bir özelliktir (tuzak).",
      "14.04 Açıklama Notu (pamuk linterleri, kapok)."),
    # 10
    q("Tarifenin Yorumuna İlişkin Genel Kuralların açıklama notlarına göre, aşağıdaki kurallardan hangisi I ila VI. Bölümlere giren eşyaya (dolayısıyla Fasıl 14 ürünlerine) normal olarak uygulanmaz?",
      "2(a)", ["1", "3(a)", "3(c)", "6"], "B", T_G,
      "GYK 2(a) açıklama notu, eksik veya bitirilmemiş eşya ile birleştirilmemiş veya demonte eşyaya ilişkin hükümlerin I ila VI. Bölümlere ait pozisyonlarda normal olarak bu bölümlere giren eşyaya uygulanmadığını belirtir. Fasıl 14 Bölüm II’dedir. GYK 1, 3 ve 6 ise her bölümde uygulanabilir.",
      "GYK 2(a) Açıklama Notu (III) ve (IX)."),
    # 11
    q("Tarife Cetveline göre aşağıdakilerden hangisi diğerlerinden farklı bir fasılda yer alır?",
      "Hindistan cevizi lifi (coir)", ["Piassava", "Korozo (bitkisel fildişi) dilimleri", "Lif kabağı", "Pamuk linterleri"], "B", T_F,
      "Piassava (fırça-süpürge maddesi), dilimlenmiş korozo (oymacılık tohumu), lif kabağı ve pamuk linterleri 14.04’tedir. Hindistan cevizi lifi ise dolgu olarak kullanılsa bile tarifenin başka yerinde belirtildiğinden 53.05’te (Fasıl 53) sınıflandırılır.",
      "14.04 Açıklama Notu (dolgu maddeleri hariç tutması)."),
    # 12
    q("Tarife Cetveline göre, işlenmemiş haldeki hububat sapları …… pozisyonunda; temizlenmiş, beyazlatılmış veya boyanmış hububat sapları ise …… pozisyonunda sınıflandırılır. Boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?",
      "12.13 – 14.01", ["14.01 – 12.13", "12.13 – 14.04", "12.14 – 14.01", "14.04 – 46.01"], "E", T_B,
      "14.01 pozisyon metni “temizlenmiş, beyazlatılmış veya boyanmış hububat saplarını” sayar; açıklama notu işlenmemiş haldeki hububat saplarını hariç tutarak 12.13’e gönderir. 12.14 yem bitkileri, 46.01 örgüler içindir; 14.04 kalıntı pozisyon olduğundan ismen sayılan saplara uygulanmaz.",
      "14.01 pozisyon metni ve Açıklama Notu."),
    # 13
    q("Bir firma, bazı tropik palm ağacı yapraklarından elde edilmiş sert lifleri ithal etmektedir. Lifler belirli boyda kesilmiş, boyanmış ve demetler halinde bağlanmıştır; eğirme işlemi görmemiştir. Alıcı bunları süpürge imalatında kullanacaktır; ancak lifler henüz süpürge veya fırçaya takılmaya hazır saçak veya püskül haline getirilmemiştir. Tarife Cetveline göre bu eşya hangi pozisyonda sınıflandırılır?",
      "14.04", ["96.03", "53.05", "14.01", "46.01"], "A", T_S,
      "Tarif edilen ürün piassavadır. 14.04 Açıklama Notuna göre fırça ve süpürge imalinde kullanılan bitkisel maddeler kesilmiş, beyazlatılmış, boyanmış veya taranmış (eğirme için olanlar hariç), bağ veya demet halinde olsun olmasın 14.04’tedir. 96.03 yalnız yapıma hazır saçak ve püskülleri kapsar; 53.05 eğirme için hazırlanmış lifler içindir.",
      "14.04 Açıklama Notu (fırça ve süpürge maddeleri); Fasıl 14 Not 3."),
    # 14
    q("Tarife Cetveline göre, süpürge yapımına hazır hale getirilmiş (yapımda yalnızca çok küçük işlemler gerektiren) süpürge darısı saçak ve püskülleri hangi pozisyonda yer alır?",
      "96.03", ["14.04", "14.01", "12.13", "46.02"], "C", T_E,
      "Fasıl 14 Not 3 hazır fırça başlarını 14.04’ün dışında tutar. 14.04 Açıklama Notu da süpürge veya fırça yapımına hazır (veya yalnızca çok küçük işlemler gerektiren) lif saçak ve püsküllerinin 96.03’te sınıflandırıldığını belirtir. Ham süpürge darısı başakları ise 14.04’te kalırdı.",
      "Fasıl 14 Not 3; 14.04 Açıklama Notu."),
    # 15
    q("Aşağıdakilerden hangisi Tarife Cetvelinin 14.04 pozisyonunda <b>sınıflandırılmaz</b>?",
      "Ağaç (odun) yünü", ["Kapok", "Dilimlenmiş korozo cevizi", "Piassava", "Zostera (deniz) otu"], "D", T_O,
      "Fasıl 14 Not 3’e göre odun yünü 14.04’e dahil değildir; 44.05 pozisyonunda yer alır. Kapok ve zostera otu dolgu maddesi, dilimlenmiş korozo oymacılık tohumu, piassava fırça-süpürge maddesi olarak 14.04’te sınıflandırılır.",
      "Fasıl 14 Not 3; 14.04 Açıklama Notu."),
    # 16
    q("Tarife Cetvelinin 14. Fasıl notlarına göre aşağıdaki ürün çiftlerinden hangisi 14.04 pozisyonuna dahil değildir?",
      "Odun yünü ve süpürge-fırça yapımına hazır fırça başları",
      ["Kapok ve bitkisel tüy gibi dolgu maddeleri", "Piassava ve istle gibi fırça-süpürge maddeleri", "Korozo ve doum palmiyesi cevizi gibi oyma tohumları", "Pamuk linterleri ve lif kabağı gibi diğer ürünler"], "E", T_N,
      "Fasıl 14 Not 3 açıkça odun yününü (44.05) ve fırça veya süpürge yapımında kullanılan hazır fırça başlarını (96.03) 14.04’ün dışında bırakır. Diğer çiftlerin hepsi 14.04 Açıklama Notunda dolgu, fırça-süpürge, oymacılık veya diğer bitkisel ürün olarak sayılmıştır.",
      "Fasıl 14 Not 3."),
    # 17
    q("Tarife Cetveline göre aşağıdaki eşya çiftlerinden hangisinde her iki eşya da aynı tarife pozisyonunda yer alır?",
      "Piassava – pamuk linterleri",
      ["İşlenmemiş hububat sapı – boyanmış hububat sapı", "Bambu – yonga", "Mazı yumrusu – mazı yumrusu taneni", "Kapok – ağaç yünü"], "A", T_F,
      "Piassava ve pamuk linterleri 14.04’tedir. İşlenmemiş sap 12.13, boyanmış sap 14.01; bambu 14.01, yonga 44.04; mazı yumrusu 14.04, su ile çıkarılmış taneni 32.01; kapok 14.04, ağaç yünü 44.05’tir.",
      "Fasıl 14 Not 2 ve Not 3; 14.01 ve 14.04 Açıklama Notları."),
    # 18
    q("Tarife Cetveline göre aşağıdakilerden hangileri 14.04 pozisyonunda sınıflandırılır?  I. Bütün veya dilimlenmiş korozo (bitkisel fildişi)  II. Korozodan yapılmış düğme taslakları  III. Lif kabağı (bitkisel sünger)  IV. Safran stigmaları",
      "I ve III", ["I ve II", "II ve IV", "I, II ve III", "III ve IV"], "D", T_C,
      "Oymacılıkta kullanılan tohumlar bütün veya dilimlenmiş olup başka türlü işlem görmemişse 14.04’tedir (I); daha ileri işlenmişleri genellikle 96.02 veya 96.06’ya gider, düğme taslakları 96.06’dadır (II). Lif kabağı 14.04’tedir (III). Safran stigmaları ise boya bitkisi sayılmaz, 09.10’da yer alır (IV).",
      "14.04 Açıklama Notu (oymacılık tohumları, boya bitkileri, diğer bitkisel ürünler)."),
    # 19
    q("Ham, uzunlamasına yarılmış ve boyanmış bambuların 14.01 pozisyonunda sınıflandırılmasında, bu durum pozisyon metni ve Fasıl 14 Not 2’de açıkça belirtildiğinden aşağıdaki Genel Yorum Kurallarından hangisi esas alınır?",
      "GYK 1", ["GYK 2(a)", "GYK 3(a)", "GYK 3(b)", "GYK 4"], "B", T_G,
      "GYK 1’e göre eşyanın tarifedeki yeri pozisyon metinlerine ve bölüm veya fasıl notlarına göre saptanır. Bambu 14.01 metninde ismen yer alır ve Not 2 yarılmış, boyanmış halleri açıkça kapsar; başka kurala başvurmaya gerek kalmaz. 2(a) bitirilmemiş eşya, 3(a)–3(b) birden fazla pozisyona girebilen eşya, 4 ise hiçbir pozisyona sokulamayan eşya içindir.",
      "GYK 1; Fasıl 14 Not 2."),
    # 20
    q("Tarife Cetveline göre, temizlenmiş ve boyanmış, içme çubuğu imali için uzunluğuna kesilmiş hububat sapları hangi pozisyonda sınıflandırılır?",
      "14.01", ["12.13", "14.04", "46.01", "12.14"], "C", T_E,
      "14.01 Açıklama Notu, bu pozisyondaki maddelerin uzunluğuna kesilmiş veya uçları yuvarlatılmış (örneğin içme çubuğu imali için hububat sapları) olabileceğini belirtir; temizlenmiş, beyazlatılmış veya boyanmış hububat sapları zaten pozisyon metninde sayılmıştır. 12.13 yalnız işlenmemiş sapları kapsar; 46.01 örgüler içindir.",
      "14.01 pozisyon metni ve Açıklama Notu."),
    # 21
    q("Aşağıdakilerden hangisi Tarife Cetvelinin 14.04 pozisyonunda <b>yer almaz</b>?",
      "Boya ağacı hülasası", ["Kurutulmuş kök boya kökleri", "Kurutulmuş kına fidanı yaprakları", "Valonya", "Toz haline getirilmiş mazı yumrusu"], "A", T_O,
      "Boyacılık ve debagat hammaddeleri (kök boya, kına fidanı yaprakları, valonya, mazı yumrusu) işlem görmemiş, kurutulmuş, öğütülmüş veya toz halinde 14.04’tedir. Boya ağacı hülasaları ve diğer bitkisel boya hülasaları ise açıklama notunda hariç tutulmuş olup 32.03’te yer alır.",
      "14.04 Açıklama Notu (boyacılık ve debagat hammaddeleri ve hariç tutmalar)."),
    # 22
    q("Açıklama notlarına göre, esas olarak boyacılıkta veya debagatte kullanılan türdeki odunlar hangi halde iseler 14.04 pozisyonunda sınıflandırılır?",
      "Yalnızca yonga, talaş, kıymık veya toz halinde iseler",
      ["Yalnızca kütük halinde iseler", "Kabuğu soyulmuş tomruk halinde iseler", "Boyutları ve şekilleri ne olursa olsun her halde", "Yalnızca su ile hülasaları çıkarıldıktan sonra"], "D", T_N,
      "14.04 Açıklama Notu, boyacılık veya debagatte kullanılan türdeki odunların yalnızca yonga, talaş, kıymık veya toz şeklinde iseler burada sınıflandırıldığını, diğer şekillerde olanların Fasıl 44’e girdiğini belirtir. Hülasaları ise 32.01 veya 32.03’tedir.",
      "14.04 Açıklama Notu (boyacılık ve debagat odunları)."),
    # 23
    q("Tarife Cetveline göre aşağıdaki bitkisel kökenli ürünlerden hangisi diğerlerinden farklı bir fasılda yer alır?",
      "Un veya nişasta hamurundan yapılmış pirinç kağıdı",
      ["Ağaç özünün dilimlenmesiyle elde edilen Japon pirinç kağıdı", "Tanbul yaprakları", "Korozo unu", "Quillaia (sabun ağacı) kabuğu"], "E", T_F,
      "Ağaç özünden dilimlenen Japon pirinç kağıdı, tanbul yaprakları, korozo unları ve quillaia kabuğu 14.04’te sayılmıştır. Un veya nişasta hamurundan pişirilip kurutularak yapılan yenilebilir pirinç kağıdı ise 19.05’tedir; iki ürün aynı adla anıldığı için karıştırılmamalıdır.",
      "14.04 Açıklama Notu; 19.05 Açıklama Notu."),
    # 24
    q("Tarife Cetveline göre aşağıdaki eşya – pozisyon eşleştirmelerinden hangisi <b>yanlıştır</b>?",
      "Hindistan cevizi lifi – 14.04",
      ["Pamuk linterleri – 14.04", "Ağaç yünü – 44.05", "Debagat hülasası – 32.01", "Hazır fırça başı – 96.03"], "C", T_B,
      "Hindistan cevizi lifi (coir) dolgu veya fırça yapımında kullanılsa bile tarifenin başka yerinde belirtildiğinden 53.05’tedir; 14.04 Açıklama Notu onu açıkça hariç tutar. Linter 14.04, ağaç yünü 44.05, debagat hülasası 32.01, hazır fırça başı 96.03 eşleştirmeleri doğrudur.",
      "14.04 Açıklama Notu; Fasıl 14 Not 3."),
    # 25
    q("Kağıt hamuru imalinde, ip ve sepet örgüsünde kullanılan halfa otu (Stipa tenacissima) sap ve yaprak halinde ithal edilmiştir. Ürün yalnızca beyazlatılmıştır; dokumaya elverişli lif olarak haddeleme, ezme veya tarama işlemi görmemiştir. Tarife Cetveline göre bu eşya hangi pozisyonda sınıflandırılır?",
      "14.04", ["53.05", "53.03", "46.01", "12.14"], "B", T_S,
      "14.04 Açıklama Notuna göre halfa yalnızca sap ve yaprak şeklinde, ham, beyazlatılmış veya boyanmış durumda ise 14.04’te sınıflandırılır. Dokumaya elverişli lif olarak haddelenmiş, ezilmiş veya taranmış halfa 53.05’e gider. 53.03 jüt ve süpürge çalısı lifleri, 46.01 örgüler içindir.",
      "14.04 Açıklama Notu (halfa); Fasıl 14 Not 1."),
]

obj = {
    "tur": "fasil",
    "fasil": 14,
    "baslik": "Örülmeye elverişli bitkisel maddeler; tarifenin başka yerinde belirtilmeyen veya yer almayan bitkisel ürünler",
    "bolum": "II",
    "oz": {
        "vurgu": "Fasıl 14 yalnız iki pozisyondan oluşur: 14.01 örgü için kullanılan ham bitkisel maddeleri, 14.04 ise tarifenin başka yerinde yer almayan bitkisel ürünleri toplar. Belirleyici soru şudur: Madde esas olarak dokumacılıkta mı kullanılıyor (Bölüm XI), yoksa ham veya basitçe işlenmiş olarak örgü, fırça-süpürge, dolgu, boyacılık-debagat veya oymacılık hammaddesi mi?",
        "maddeler": [
            "Esas itibariyle mensucat imalinde kullanılan bitkisel maddeler ve lifler, nasıl hazırlanmış olursa olsun Fasıl 14’e girmez; XI. Bölümde yer alır (Not 1).",
            "14.01: bambu, Hint kamışı, kamış, saz, sepetçi söğüdü, rafya, temizlenmiş-beyazlatılmış-boyanmış hububat sapları, ıhlamur iç kabuğu; yarılmış, cilalanmış, boyanmış veya yanmaz hale getirilmiş olabilir.",
            "14.04: pamuk linterleri; boyacılık ve debagat hammaddeleri; oymacılık tohum ve kabukları (korozo); dolgu maddeleri (kapok); fırça-süpürge maddeleri (piassava); diğerleri (lif kabağı, Japon pirinç kağıdı, tanbul yaprağı).",
            "İşlem ilerledikçe ürün fasıldan çıkar: örgü haline getirilen 46.01, eğirme için hazırlanan 53.03 / 53.05, hazır fırça başı 96.03, işlenmiş bitkisel fildişi 96.02 / 96.06.",
        ],
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Esas olarak mensucat imalinde kullanılan bitkisel madde veya lif mi; ya da eğirme için haddelenmiş, ezilmiş, taranmış mı?", "Bölüm XI (ör. <b>53.03</b> / <b>53.05</b>)"],
            ["2", "Bükülerek birleştirilmiş, örgü yerine kullanılabilir hale getirilmiş veya örgü/dokuma haline gelmiş mi?", "<b>46.01</b> (sepet ise <b>46.02</b>)"],
            ["3", "İşlenmemiş hububat sapı mı?", "<b>12.13</b>"],
            ["4", "Yonga mı, odun yünü mü?", "<b>44.04</b> / <b>44.05</b>"],
            ["5", "Örgü için kullanılan türde ham veya basitçe işlenmiş bitkisel madde mi? (bambu, Hint kamışı, kamış, saz, söğüt, rafya, ıhlamur kabuğu, temizlenmiş-beyazlatılmış-boyanmış hububat sapı)", "<b>14.01</b>"],
            ["6", "Bitkisel hammaddeden elde edilmiş hülasa mı? (debagat hülasası, tanen, boya hülasası)", "<b>32.01</b> / <b>32.03</b>"],
            ["7", "Süpürge veya fırça yapımına hazır saçak ve püskül mü?", "<b>96.03</b>"],
            ["8", "Oymacılık tohumu veya kabuğu bütün veya dilimlenmiş halin ötesinde işlenmiş mi?", "Genellikle <b>96.02</b> / <b>96.06</b>"],
            ["9", "Başka yerde yer almayan bitkisel ürün mü? (linter, boya-debagat hammaddesi*, oymacılık tohumu, dolgu, fırça-süpürge maddesi, lif kabağı vb.)", "<b>14.04</b>"],
        ],
        "dipnot": "* Boyacılık veya debagatte kullanılan odunlar yalnız yonga, talaş, kıymık veya toz halinde 14.04’tedir; diğer şekillerdeki bu odunlar Fasıl 44’e gider.",
    },
    "pozisyon_haritasi": [
        ["14.01", "Örgü için kullanılan bitkisel maddeler", "Ham veya basitçe işlenmiş; yarılmış, boyanmış, cilalı, yanmaz olabilir", "Bambu, Hint kamışı, rafya, sepetçi söğüdü, boyanmış saman"],
        ["14.02", "Kaldırılmış pozisyon", "Cetvelde boş bırakılmıştır", "—"],
        ["14.03", "Kaldırılmış pozisyon", "Cetvelde boş bırakılmıştır", "—"],
        ["14.04", "Başka yerde yer almayan bitkisel ürünler", "Kalıntı pozisyon: linter, boya-debagat, oyma, dolgu, fırça maddeleri", "Pamuk linteri, kapok, piassava, korozo, lif kabağı"],
    ],
    "notlar": [
        ["Fasıl 14 Not 1", "Nasıl hazırlanmış olursa olsun esas itibariyle mensucat imalinde kullanılan bitkisel maddeler ve bitkisel madde lifleri ile sadece mensucat imalinde kullanılabilecek hale getirilmiş diğer bitkisel maddeler bu fasla dahil değildir; XI. Bölümde yer alır."],
        ["Fasıl 14 Not 2", "14.01; bambuları (yarılmış, uzunlamasına biçilmiş veya kesilmiş, uçları yuvarlaklaştırılmış, beyazlatılmış, yanmaz hale getirilmiş, parlatılmış veya boyanmış olsun olmasın), yarılmış sepetçi söğüdünü, kamış ve benzerlerini, Hint kamışı içini ve bunun dilimlenmişlerini de kapsar. Yonga bu pozisyona dahil değildir (44.04)."],
        ["Fasıl 14 Not 3", "Odun yünü (44.05) ve fırça veya süpürge yapımında kullanılan hazır fırça başları (96.03) 14.04’e dahil değildir."],
        ["14.01 Açıklama Notu", "Örgü maddeleri yıkanmış, şeritlere ayrılmış, soyulmuş, parlatılmış, beyazlatılmış, boyanmış, verniklenmiş veya yanmaz hale getirilmiş; uzunluğuna kesilmiş veya uçları yuvarlatılmış; demet halinde olabilir. İşlenmemiş hububat sapları 12.13’tedir. Bükülerek birleştirilip örgü yerine kullanılabilir hale getirilenler 46.01’e; eğirme için haddelenen, ezilen, taranan maddeler 53.03 / 53.05’e gider. Bükülmemiş rafyadan dokumalar 46.01’dedir."],
        ["14.04 Açıklama Notu", "Pamuk linterleri: çırçırlamadan sonra tohumda kalan, genellikle 5 mm’den kısa lifler; kullanım amacına ve ham, temiz, beyazlatılmış, boyanmış veya absorbe edici olmasına bakılmaksızın 14.04. Tıbbi tamponlar 30.05, diğer tamponlar 56.01."],
        ["14.04 Açıklama Notu", "Boyacılık ve debagat hammaddeleri (odun, kabuk, kök, meyve, mazı yumrusu, yaprak, liken) işlem görmemiş, kurutulmuş, öğütülmüş veya toz halinde 14.04’tedir; odunlar yalnız yonga, talaş, kıymık veya toz halinde (diğerleri Fasıl 44). Safran 09.10; debagat hülasaları ve tanenler 32.01; boya hülasaları 32.03."],
        ["14.04 Açıklama Notu", "Oymacılıkta kullanılan tohum, çekirdek ve kabuklar (korozo, doum cevizi, hurma çekirdeği, Hindistan cevizi kabuğu) bütün veya dilimlenmiş halde 14.04’te; başka türlü işlem görmüşleri genellikle 96.02 veya 96.06’da."],
        ["14.04 Açıklama Notu", "Dolgu maddeleri (kapok – lifleri 15–30 mm –, bitkisel tüy, zostera otu) mesnet üzerine veya iki tabaka arasına tutturulmuş olsalar da 14.04’tedir. Ağaç yünü 44.05, mantar yünü 45.01, Hindistan cevizi lifi 53.05."],
        ["14.04 Açıklama Notu", "Fırça-süpürge maddeleri (süpürge darısı, piassava, sedir otu kökü, istle) kesilmiş, beyazlatılmış, boyanmış, taranmış (eğirme için olanlar hariç), demet halinde olsun olmasın 14.04’te. Yapıma hazır saçak ve püsküller 96.03. Vetiver ve tıbbi sedir otu 12.11."],
        ["14.04 Açıklama Notu", "Diğer bitkisel ürünler: halfa (sap ve yaprak halinde; eğirme için hazırlanmışı 53.05), lif kabağı, korozo unları, Japon pirinç kağıdı, tanbul yaprakları, quillaia kabuğu, Hint sabun ağacı meyveleri. Hayvansal süngerler 05.11; agar-agar ve karragenan 13.02; deniz yosunları 12.12."],
    ],
    "sinir_komsulari": [
        ["Yonga (ince şeritler halinde ağaç)", "44.04", "Fasıl 14 Not 2: 14.01’e dahil değildir"],
        ["Ağaç (odun) yünü", "44.05", "Fasıl 14 Not 3"],
        ["Süpürge-fırça yapımına hazır saçak ve püskül", "96.03", "Fasıl 14 Not 3; hazır fırça başı"],
        ["İşlenmemiş hububat sapı", "12.13", "14.01 yalnız temizlenmiş, beyazlatılmış veya boyanmış sapları kapsar"],
        ["Örülmeye elverişli maddelerden örgüler; bükülmemiş rafyadan dokumalar", "46.01", "Hammadde değil, örgü"],
        ["Bambudan veya söğütten sepet; lif kabağından kese eldiveni", "46.02", "Sepetçi eşyası ve luffadan eşya"],
        ["Eğirme için hazırlanmış bitkisel lifler; Hindistan cevizi lifi", "53.03 / 53.05", "Fasıl 14 Not 1: mensucat maddesi"],
        ["Debagat hülasaları, tanenler; boya hülasaları", "32.01 / 32.03", "Hammadde değil, hülasa"],
        ["Safran stigmaları", "09.10", "Boya bitkisi sayılmaz"],
        ["Hayvansal menşeli sünger", "05.11", "Bitkisel sünger (lif kabağı) ise 14.04"],
        ["Agar-agar, karragenan", "13.02", "Bitkisel kıvam verici maddeler"],
        ["Vetiver kökü, tıbbi sedir otu", "12.11", "Fırça yapımında kullanılan sedir otu kökü ise 14.04"],
        ["Linterden tıbbi tampon / diğer tampon", "30.05 / 56.01", "Tampon haline gelince 14.04’ten çıkar"],
        ["Korozodan düğme veya düğme taslağı", "96.06", "Bütün veya dilimlenmiş halin ötesine geçmiş"],
        ["Un veya nişastadan yapılan yenilebilir pirinç kağıdı", "19.05", "Ağaç özünden dilimlenen Japon pirinç kağıdı ise 14.04"],
    ],
    "tuzaklar": [
        "<b>Bambu eşya olana kadar 14.01’de kalır.</b> Yarılmış, uzunlamasına biçilmiş, uçları yuvarlatılmış, beyazlatılmış, yanmaz hale getirilmiş, cilalanmış veya boyanmış bambu 14.01’dedir (Not 2). Örgü haline getirilirse 46.01, sepet olursa 46.02.",
        "<b>Hububat sapı iki yere ayrılır.</b> İşlenmemiş sap 12.13; temizlenmiş, beyazlatılmış veya boyanmış sap 14.01.",
        "<b>Yonga örgü maddesi sayılmaz.</b> İnce şeritler halindeki ağaç malzeme 14.01’e girmez; 44.04’tedir.",
        "<b>Mensucat maddesi Fasıl 14’e girmez.</b> Esas olarak dokumacılıkta kullanılan bitkisel lifler XI. Bölümdedir. Halfa sap ve yaprak halinde 14.04’te; eğirme için taranırsa 53.05.",
        "<b>Pamuk linteri pamuk değildir.</b> Kısa lifler (genellikle 5 mm’den az) beyazlatılmış veya absorbe edici hale getirilmiş olsa da 14.04’tedir; tampon olunca 30.05 veya 56.01.",
        "<b>Boya odunu yalnız ufalanmış halde 14.04’tedir.</b> Yonga, talaş, kıymık veya toz halindeki boya-debagat odunları 14.04’te; diğer şekilleri Fasıl 44.",
        "<b>Hammadde ile hülasa ayrımı.</b> Mazı yumrusu, valonya, kök boya 14.04; bunlardan çıkarılan tanen 32.01, boya hülasası 32.03.",
        "<b>Demet halindeki piassava ≠ hazır fırça başı.</b> Kesilmiş, boyanmış, demetlenmiş piassava 14.04’te; yapıma hazır saçak ve püskül 96.03.",
        "<b>“Pirinç kağıdı” iki ayrı eşyadır.</b> Ağaç özünden dilimlenen Japon pirinç kağıdı 14.04; un veya nişasta hamurundan yapılan yenilebilir pirinç kağıdı 19.05.",
    ],
    "hafiza": {
        "kanca": "14.01 = ÖR · 14.04 = LİBO-DOF",
        "aciklama": "<b>ÖR</b>: örgülük bambu, kamış, saz, söğüt, rafya → 14.01. 14.04’ün çekmeceleri: <b>Lİ</b>nter · <b>BO</b>ya-debagat · <b>D</b>olgu (kapok) · <b>O</b>yma (korozo) · <b>F</b>ırça-süpürge (piassava) ve en altta “diğerleri” (lif kabağı, Japon pirinç kağıdı). 14.02 ve 14.03 boş çekmecelerdir.",
    },
    "sinav_odagi": [
        "Bu fasıl çıkmış sorularda doğrudan sorulmamış; daha çok bölüm düzeyindeki sorularda ve örülmeye elverişli maddelerden yapılmış eşya sorularında arka plan olarak yer almıştır.",
        "Bölüm II’nin kapsamı: Fasıl 6–14 bitkisel ürünlerdir; “yenilen çeşitli gıda müstahzarları” (Fasıl 21) ise Bölüm IV’tedir. Bölüm–fasıl eşleştirmesi sık kullanılan bir kalıptır.",
        "Bambu gibi örülmeye elverişli maddelerden yapılmış mobilya veya sepet sorularında hammadde (14.01) ile mamul eşyanın (Fasıl 46, 94) ayrımı ve GYK 3 kurallarının birlikte kullanılması.",
        "Sepetçi ve hasırcı eşyasının hangi bölümde yer aldığı: hammadde Bölüm II’de (14.01), eşya Bölüm IX’da (46.02).",
    ],
    "cikmis_ornekler": [
        {
            "soru": "Aşağıdakilerden hangisi Tarife Cetveli’nin 2. Bölümünde bulunan “Bitkisel Ürünler” içerisinde yer almaz?",
            "secenekler": [
                "Yenilen sebzeler ve bazı kök ve yumrular",
                "Yenilen çeşitli gıda müstahzarları",
                "Hububat",
                "Lak; sakız, reçine ve diğer bitkisel özsu ve hülasalar",
            ],
            "cevap": "B",
            "aciklama": "Bölüm II Fasıl 6–14’ten oluşur (Fasıl 7 sebzeler, Fasıl 10 hububat, Fasıl 13 lak ve sakızlar; Fasıl 14 bölümün son faslıdır). Yenilen çeşitli gıda müstahzarları Fasıl 21 olup Bölüm IV’te yer alır.",
        }
    ],
    "ozet": [
        "Fasıl 14’te yalnız iki pozisyon vardır: 14.01 ve 14.04 (14.02 ve 14.03 boş).",
        "Esas itibariyle dokumacılıkta kullanılan bitkisel madde ve lifler XI. Bölümdedir.",
        "14.01: örgülük ham maddeler; yarılmış, boyanmış, cilalanmış, yanmaz olabilir; yonga 44.04.",
        "14.04: linter, boya-debagat hammaddesi, oymacılık tohumu, dolgu, fırça-süpürge maddesi ve diğer bitkisel ürünler.",
        "Fasıl dışı komşular: hülasa 32.01 / 32.03, hazır fırça başı 96.03, ağaç yünü 44.05, örgü 46.01, işlenmemiş sap 12.13.",
        "İşlem ilerledikçe ürün fasıldan çıkar: örgü, eğirmeye hazırlama, tampon, düğme.",
    ],
    "sorular": sorular,
}

yaz(14, obj)
