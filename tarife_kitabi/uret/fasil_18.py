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
    q("Tarife Cetveline göre, fermente edilmiş, kavrulmuş ve kırılarak kabuklarından ayrılmış kakao dane parçaları hangi pozisyonda sınıflandırılır?",
      "18.01", ["18.02", "18.03", "18.05", "09.01"], "A", T_E,
      "18.01 kakao danelerini ve kırıklarını ham veya kavrulmuş, bütün veya kırık halde kapsar; açıklama notu kabuklarından ayrılmış olsun olmasın kırık daneleri (kakao parçaları) açıkça sayar. Kabuklar 18.02’ye, hamur kıvamında öğütülmüş daneler 18.03’e gider. 09.01 kahve içindir.",
      "18.01 pozisyon metni ve Açıklama Notu."),
    # 2
    q("Aşağıdakilerden hangisi Tarife Cetvelinin 18. faslında <b>sınıflandırılmaz</b>?",
      "Çikolatalı dondurma", ["Kakao yağı", "Kakao hamuru", "Tatlandırılmış kakao tozu", "Sürülebilen çikolata"], "D", T_O,
      "Fasıl 18 Not 1(b) 21.05’teki müstahzarları fasıl dışında bırakır; genel açıklamalara göre herhangi bir oranda kakao içeren dondurma ve diğer yenilebilir buzlar 21.05’tedir. Kakao yağı 18.04, kakao hamuru 18.03, tatlandırılmış kakao tozu ve sürülebilen çikolata 18.06’dadır.",
      "Fasıl 18 Not 1(b); Fasıl 18 Genel Açıklamalar."),
    # 3
    q("Tarife Cetvelinin 18. Fasıl notlarına göre, ağırlık itibariyle hangi oranın üzerinde sosis, et, sakatat, kan, böcek, balık veya su omurgasızı (ya da bunların bileşimini) içeren gıda müstahzarları kakao içerse bile bu fasla dahil değildir?",
      "%20", ["%5", "%6", "%15", "%40"], "B", T_N,
      "Fasıl 18 Not 1(a), ağırlık itibariyle %20’den fazla bu ürünleri içeren gıda müstahzarlarını Fasıl 16’ya gönderir. %5, %6 ve %40, Fasıl 19 ile sınırı belirleyen kakao oranlarıdır; %15 ise Fasıl 15’teki süt yağı eşiğidir (tuzak).",
      "Fasıl 18 Not 1(a); Fasıl 16 Not 2."),
    # 4
    q("Tarife Cetveline göre, kavrulmuş kakao danelerinin ezilmesiyle elde edilen, yağı kısmen alınmış ve şeker katılmamış kakao hamuru (kakao küspesi) hangi pozisyonda yer alır?",
      "18.03", ["18.02", "18.05", "18.04", "23.06"], "C", T_E,
      "18.03 kakao hamurunu yağı alınmış olsun olmasın kapsar; açıklama notu tamamen veya kısmen yağı alınmış kakao hamurunu (kakao küspesi) da sayar. 18.02 kabuk ve zar içeren artıklar, 18.05 öğütülmüş şekersiz toz, 18.04 kakao yağı içindir. 23.06 diğer bitkisel yağ küspeleridir.",
      "18.03 pozisyon metni ve Açıklama Notu."),
    # 5
    q("Tarife Cetveline göre, çözünürlüğünü artırmak için potasyum karbonat gibi alkali maddelerle işlem görmüş, ilave şeker veya tatlandırıcı içermeyen kakao tozu hangi pozisyonda sınıflandırılır?",
      "18.05", ["18.06", "18.03", "21.06", "21.01"], "E", T_E,
      "18.05 yalnız ilave şeker veya tatlandırıcı içermeyen kakao tozunu kapsar; açıklama notu, alkali maddelerle (sodyum veya potasyum karbonat) işlenmiş çözünür kakaoyu da bu pozisyona alır. Şeker, süt tozu veya pepton katılsaydı 18.06’ya giderdi. 21.01 kahve ve çay hülasaları içindir.",
      "18.05 pozisyon metni ve Açıklama Notu."),
    # 6
    q("Tarife Cetveline göre aşağıdakilerden hangisi diğerlerinden farklı bir tarife pozisyonunda yer alır?",
      "Şekersiz kakao tozu", ["Sütlü tablet çikolata", "Fındıklı çikolatalı nuga", "Şeker katılmış kakao tozu", "Sürülebilen çikolata"], "D", T_F,
      "Tablet çikolata, çikolatalı nuga, şekerli kakao tozu ve sürülebilen çikolata 18.06’dadır. Tatlandırıcı içermeyen kakao tozu ise 18.05’tedir. Aynı ürünün (kakao tozu) şeker katılınca pozisyon değiştirmesi tipik bir tuzaktır.",
      "18.05 ve 18.06 pozisyon metinleri ve Açıklama Notları."),
    # 7
    q("Tarife Cetveline göre, vitaminlerle zenginleştirilmiş sütlü tablet çikolata hangi pozisyonda sınıflandırılır?",
      "18.06", ["30.04", "21.06", "17.04", "19.01"], "B", T_E,
      "18.06 açıklama notu vitaminlerle zenginleştirilmiş çikolatanın da bu pozisyonda yer aldığını açıkça belirtir. Vitamin eklenmesi ürünü ilaç (30.04) yapmaz. 17.04 yalnız beyaz çikolata ve kakaosuz şekerlemeler içindir; 19.01 un veya süt esaslı, düşük kakaolu müstahzarları kapsar.",
      "18.06 Açıklama Notu; Fasıl 18 Not 2."),
    # 8
    q("Aşağıdakilerden hangisi Tarife Cetvelinin 18.06 pozisyonunda <b>sınıflandırılmaz</b>?",
      "Çikolata ile kaplanmış bisküvi", ["Çikolatalı nuga", "Çikolata tozu", "Kakaolu şekerleme", "Şeker katılmış kakao hamuru"], "A", T_O,
      "18.06 açıklama notu, çikolata ile kaplı bisküvileri ve diğer fırıncılık ürünlerini hariç tutar; bunlar 19.05’tedir (Not 1(b)). Çikolatalı nuga, çikolata tozu ve kakaolu şekerlemeler 18.06’da sayılmıştır; şeker katılmış kakao hamuru da 18.03 açıklama notu gereği 18.06’ya gider.",
      "18.06 Açıklama Notu; 18.03 Açıklama Notu; Fasıl 18 Not 1(b)."),
    # 9
    q("Tarife Cetveline göre aşağıdakilerden hangisi diğerlerinden farklı bir fasılda yer alır?",
      "Kakaodan elde edilen teobromin", ["Preslenerek elde edilen kakao yağı", "Kavrulmuş kakaonun kabuğu", "Yağı alınmamış kakao hamuru", "Fermente edilmiş kakao danesi"], "E", T_F,
      "Fasıl 18 genel açıklamalarına göre kakaodan çıkarılan teobromin alkaloidi bu fasıl haricindedir ve 29.39’da (Fasıl 29) yer alır. Kakao yağı 18.04, kabuğu 18.02, hamuru 18.03, danesi 18.01 ile Fasıl 18’dedir.",
      "Fasıl 18 Genel Açıklamalar."),
    # 10
    q("Tarife Cetveline göre, kakao danelerinin kavrulması ve kırılması sırasında ayrılan iç ve dış kabuklar ile zarlar hangi pozisyonda yer alır?",
      "18.02", ["18.01", "23.08", "18.03", "18.04"], "C", T_E,
      "18.02 kakao kabuklarını, iç kabuklarını, zarlarını ve diğer kakao döküntülerini kapsar; açıklama notu bunların danelerin kavrulması ve kırılması işlemleri sırasında ayrıldığını belirtir. Hayvan yemlerine katılabilmeleri 23.08’e götürmez; ismen 18.02’de belirtilmiştir.",
      "18.02 pozisyon metni ve Açıklama Notu."),
    # 11
    q("Aşağıdakilerden hangisi Tarife Cetvelinin 18.02 pozisyonunda <b>sınıflandırılmaz</b>?",
      "Kabuk-zar içermeyen kakao hamurundan yağ alındıktan sonra kalan küspe",
      ["Kavurma sırasında ayrılan kakao kabukları", "Danelerden ayrılan kakao zarları", "Özel makinelerle ayrılan kakao rüşeymleri", "Kabuk ve zarlardan kakao yağı çıkarıldıktan sonra kalan küspe"], "E", T_O,
      "18.02 açıklama notu, kakao hamurundan yağ ekstraksiyonundan sonra arta kalan ve iç-dış kabuklar ile zarları içermeyen küspeleri hariç tutarak 18.03’e gönderir. Kabuklar, zarlar, rüşeymler ve kabuk-zar içeren küspeler ise 18.02’de sayılmıştır. Ayrımı küspenin kabuk ve zar içerip içermemesi belirler.",
      "18.02 Açıklama Notu; 18.03 pozisyon metni."),
    # 12
    q("Tarife Cetveline göre aşağıdaki eşya çiftlerinden hangisinde her iki eşya da aynı pozisyonda yer alır?",
      "Çikolatalı nuga – vitaminli çikolata",
      ["Beyaz çikolata – sütlü çikolata", "Şekersiz kakao tozu – şekerli kakao tozu", "Kakao hamuru – şeker katılmış kakao hamuru", "Kakao danesi – kakao kabuğu"], "C", T_F,
      "Çikolatalı nuga ve vitaminli çikolata 18.06’da birlikte yer alır. Beyaz çikolata 17.04 – sütlü çikolata 18.06; şekersiz kakao tozu 18.05 – şekerli 18.06; kakao hamuru 18.03 – şekerli hamur 18.06; kakao danesi 18.01 – kabuğu 18.02’dir.",
      "18.01–18.06 Açıklama Notları; 17.04 pozisyon metni."),
    # 13
    q("Aşağıdaki kakao içeren ürünlerden hangisi Tarife Cetvelinin 18. faslında <b>yer almaz</b>?",
      "İçmeye hazır kakaolu alkolsüz içecek",
      ["Kakao içeren, ekmeğe sürülen krema", "Vitaminlerle zenginleştirilmiş çikolata", "Şeker katılmış kakao tozu", "Kakao içeren şeker mamulü"], "D", T_O,
      "Fasıl 18 Not 1(b) 22.02 ve 22.08’deki müstahzarları hariç tutar; genel açıklamalara göre kakao içeren ve tüketime hazır alkollü veya alkolsüz içecekler Fasıl 22’dedir. Sürülebilir krema, vitaminli çikolata, şekerli kakao tozu ve kakaolu şekerleme 18.06’dadır.",
      "Fasıl 18 Not 1(b); Fasıl 18 Genel Açıklamalar."),
    # 14
    q("Fasıl 18 Not 1(b)’de, kakao içerse bile bu fasla dahil olmayan müstahzarların yer aldığı pozisyonlar sayılmıştır. Aşağıdakilerden hangisi bu pozisyonlardan biridir?",
      "21.05", ["17.04", "21.06", "20.07", "21.03"], "B", T_N,
      "Not 1(b)’de sayılan pozisyonlar 04.03, 19.01, 19.02, 19.04, 19.05, 21.05, 22.02, 22.08, 30.03 ve 30.04’tür. Seçeneklerden yalnız 21.05 (dondurma ve yenilen diğer buzlar) bu listede yer alır. Listede olmayan pozisyonlara ait olabilecek kakaolu müstahzarlar Not 2 gereği 18.06’ya yönelir.",
      "Fasıl 18 Not 1(b) ve Not 2."),
    # 15
    q("Şeker katılmış kakao tozunun 18.05 pozisyonunda sınıflandırılamamasının nedeni aşağıdakilerden hangisidir?",
      "18.05 metni karışımı dışladığından 2(b) uygulanmaz; eşya GYK 1 ile 18.06’dadır.",
      ["GYK 3(b) uyarınca esas niteliği şeker verdiğinden eşya 17.01’de yer alır.",
       "GYK 3(c) uyarınca numara sırasına göre sonuncu olan 18.06’da yer alır.",
       "GYK 2(a) uyarınca bitirilmemiş çikolata sayılarak 18.06’da yer alır.",
       "GYK 4 uyarınca en çok benzediği eşya olan çikolata ile 18.06’dadır."], "A", T_G,
      "GYK 2(b) bir maddeye yapılan atfın karışımlarını da kapsadığını söyler; ancak açıklama notuna göre pozisyon metni aksini öngörüyorsa uygulanmaz. 18.05 metni “ilave şeker veya diğer tatlandırıcı maddeler içermeyenler” ile sınırlıdır; 18.06 ise tatlandırılmış kakao tozunu açıkça kapsar. Bu nedenle sınıflandırma doğrudan GYK 1 ile 18.06’da yapılır.",
      "GYK 1; GYK 2(b) Açıklama Notu (X); 18.05 ve 18.06 Açıklama Notları."),
    # 16
    q("Tarife Cetveline göre aşağıdaki kakaolu hububat ürünlerinden hangisi diğerlerinden farklı bir fasılda yer alır?",
      "Tamamen çikolata ile kaplanmış mısır gevreği",
      ["Kakaolu kek", "Çikolata ile kaplanmış bisküvi", "Yağsız baz üzerinden %4 kakao içeren kavrulmuş hububat gevreği", "Un esaslı, yağsız baz üzerinden %30 kakao içeren gıda müstahzarı"], "C", T_F,
      "Fasıl 19 Not 3’e göre 19.04, tamamen çikolata ile kaplanmış müstahzarları kapsamaz; bunlar 18.06’dadır (Fasıl 18). Kakaolu kek ve çikolata kaplı bisküvi 19.05’te, %6’yı geçmeyen kakaolu kavrulmuş gevrek 19.04’te, %40’tan az kakaolu un esaslı müstahzar 19.01’de, yani Fasıl 19’dadır.",
      "Fasıl 19 Not 3; Fasıl 18 Genel Açıklamalar."),
    # 17
    q("Fasıl 18 genel açıklamalarına göre, şişirilmiş veya kavrulmuş hububat (19.04) tamamen yağsız baz üzerinden hesaplanan ağırlık itibariyle ne kadar kakao içerdiğinde Fasıl 18 dışında kalır?",
      "%6’dan fazla olmayan", ["%5’ten az olan", "%10’dan fazla olmayan", "%20’den fazla olmayan", "%40’tan az olan"], "B", T_N,
      "Genel açıklamalar, tamamen yağsız baz üzerinden %6’dan daha fazla olmayan oranda kakao içeren şişirilmiş veya kavrulmuş hububatı 19.04’e bırakır; Fasıl 19 Not 3 de %6’dan fazla kakaolu olanları 18.06’ya gönderir. %40 un-malt esaslı, %5 süt esaslı müstahzarlar için geçerli eşiklerdir (tuzak).",
      "Fasıl 18 Genel Açıklamalar; Fasıl 19 Not 3."),
    # 18
    q("Fındık ezmesi, şeker, bitkisel yağ, yağsız süt tozu ve kakao tozundan oluşan, ekmeğe sürülerek tüketilen bir krem kavanozlarda perakende satılmaktadır. Ürün un veya nişasta içermez; yağsız baz üzerinden ağırlıkça %7 kakao içerir. Tarife Cetveline göre bu eşya hangi pozisyonda sınıflandırılır?",
      "18.06", ["20.08", "21.06", "19.01", "17.04"], "E", T_S,
      "Fasıl 18 Not 2’ye göre kakao içeren gıda müstahzarları, Not 1 istisnaları dışında 18.06’dadır; açıklama notu sürülebilen çikolatayı açıkça sayar. Ürün un-malt esaslı değildir ve süt esaslı olsa bile %5 eşiğini aştığından 19.01’e girmez. Kakao içerdiği için 17.04 (kakaosuz şeker mamulleri) de değildir.",
      "Fasıl 18 Not 2; 18.06 Açıklama Notu; Fasıl 18 Genel Açıklamalar."),
    # 19
    q("Fasıl 18 genel açıklamalarına göre; esası un, kaba un, nişasta veya malt hülasası olan gıda müstahzarları tamamen yağsız baz üzerinden ağırlıkça %…’tan az kakao, esası 04.01 ila 04.04 ürünleri olan gıda müstahzarları ise %…’ten az kakao içeriyorsa 19.01’de kalır. Boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?",
      "40 – 5", ["5 – 40", "40 – 6", "20 – 5", "6 – 40"], "A", T_B,
      "Genel açıklamalar 19.01’deki iki eşiği verir: un, kaba un, nişasta veya malt hülasası esaslı müstahzarlarda %40’tan az, 04.01–04.04 (süt ürünleri) esaslı müstahzarlarda %5’ten az kakao. %6, şişirilmiş veya kavrulmuş hububatın (19.04) eşiğidir; %20 ise et-balık oranıdır.",
      "Fasıl 18 Genel Açıklamalar; 19.01 pozisyon metni."),
    # 20
    q("Tarife Cetvelinin 18. Fasıl notlarına göre, içinde kakao bulunan şeker mamulleri nerede sınıflandırılır?",
      "18.06 pozisyonunda",
      ["17.04 pozisyonunda", "Kakao oranı %5’ten azsa 17.04, fazlaysa 18.06 pozisyonunda", "18.05 pozisyonunda", "Kakao yağı içeriyorsa 18.04 pozisyonunda"], "D", T_N,
      "Fasıl 18 Not 2 açıktır: içinde kakao bulunan şeker mamulleri 18.06’dadır. Fasıl 17 Not 1(a) de kakao içeren şeker mamullerini 18.06’ya gönderir; kakao oranı için bir alt sınır yoktur. Kakao yağı ise kakao sayılmaz; bu yüzden beyaz çikolata 17.04’tedir.",
      "Fasıl 18 Not 2; Fasıl 17 Not 1(a)."),
    # 21
    q("Tarife Cetveline göre aşağıdakilerden hangileri 18.06 pozisyonunda sınıflandırılır?  I. Süt tozu katılmış kakao tozu  II. Tamamen çikolata ile kaplanmış mısır gevreği  III. Kakaolu dondurma  IV. Esası süt tozu olan, yağsız baz üzerinden %3 kakao içeren gıda müstahzarı",
      "I ve II", ["I, II ve III", "II ve IV", "I ve III", "III ve IV"], "B", T_C,
      "Süt tozu katılmış kakao tozu 18.05 açıklama notu gereği 18.06’dadır (I); tamamen çikolata kaplı gevrek Fasıl 19 Not 3 gereği 18.06’dadır (II). Kakaolu dondurma 21.05’tedir (III). Süt ürünü esaslı ve %5’ten az kakaolu müstahzar 19.01’dedir (IV).",
      "18.05 Açıklama Notu; Fasıl 19 Not 3; Fasıl 18 Not 1(b) ve Genel Açıklamalar."),
    # 22
    q("Tarife Cetveline göre aşağıdaki eşya – pozisyon eşleştirmelerinden hangisi <b>yanlıştır</b>?",
      "Şeker katılmış kakao hamuru – 18.03",
      ["Kakao danesi – 18.01", "Kakao kabuğu – 18.02", "Kakao yağı – 18.04", "Beyaz çikolata – 17.04"], "D", T_B,
      "18.03 açıklama notu, içine ilave şeker veya diğer tatlandırıcı katılmış kakao hamurunu hariç tutarak 18.06’ya gönderir. Kakao danesi 18.01, kabuğu 18.02, kakao yağı 18.04, beyaz çikolata 17.04 eşleştirmeleri doğrudur.",
      "18.03 Açıklama Notu; 17.04 pozisyon metni."),
    # 23
    q("Tek bir hediye kutusunda birlikte perakende satışa sunulan, aynı tür ve ağırlıkta altı adet sütlü tablet çikolatanın sınıflandırılmasında aşağıdakilerden hangisi doğrudur?",
      "Farklı pozisyonlara girebilen en az iki farklı eşya olmadığından takım yoktur; GYK 1 ile 18.06.",
      ["GYK 3(b) uyarınca perakende satılacak takım sayılarak 18.06’da sınıflandırılır.",
       "GYK 5(b) uyarınca kutu esas alınarak kutunun ait olduğu pozisyonda sınıflandırılır.",
       "GYK 3(c) uyarınca geçerli pozisyonlardan numara sırasına göre sonuncusunda sınıflandırılır.",
       "GYK 2(a) uyarınca demonte veya birleştirilmemiş eşya sayılarak sınıflandırılır."], "A", T_G,
      "GYK 3(b) açıklama notuna göre takım, ilk bakışta farklı pozisyonlarda sınıflandırılabilen en az iki farklı eşyadan oluşmalıdır; altı adet fondü çatalı örneği takım sayılmaz. Aynı tür altı çikolata da takım değildir; her biri 18.06’dadır. Normal ambalaj kutusu GYK 5(b) gereği içindeki eşya ile birlikte sınıflandırılır, kutunun pozisyonu esas alınmaz.",
      "GYK 3(b) Açıklama Notu (X); GYK 5(b); 18.06 pozisyon metni."),
    # 24
    q("Tarife Cetvelinin 18. faslı ile ilgili aşağıdaki ifadelerden hangileri doğrudur?  I. Kakaodan çıkarılan teobromin 18.02’de yer alır.  II. Kakao danelerinin bütün veya kırık, çiğ veya kavrulmuş olması 18.01’i değiştirmez.  III. Kakao yağı Fasıl 15’te yer alır.  IV. Kakao içeren ve tüketime hazır alkollü içecekler Fasıl 22’de yer alır.",
      "II ve IV", ["I ve II", "I ve III", "II, III ve IV", "Yalnız II"], "E", T_C,
      "18.01 dane ve kırıkları ham veya kavrulmuş, bütün veya kırık halde kapsar (II doğru). Kakaolu, tüketime hazır içecekler Fasıl 22’dedir (IV doğru). Teobromin 29.39’dadır (I yanlış). Kakao yağı Fasıl 15 Not 1(b) gereği 18.04’tedir (III yanlış).",
      "18.01 pozisyon metni; Fasıl 18 Genel Açıklamalar; Fasıl 15 Not 1(b)."),
    # 25
    q("Malt hülasası esaslı, içine süt tozu, şeker ve kakao katılmış, sıcak süt veya su ile karıştırılarak içecek hazırlanan bir toz perakende satılmaktadır. Ürün yağı tamamen alınmış baz üzerinden ağırlıkça %25 kakao içerir. Tarife Cetveline göre bu eşya hangi pozisyonda sınıflandırılır?",
      "19.01", ["18.06", "22.02", "21.01", "18.05"], "C", T_S,
      "Fasıl 18 Not 1(b) 19.01’deki müstahzarları hariç tutar; genel açıklamalara göre esası malt hülasası olan ve yağsız baz üzerinden %40’tan az kakao içeren gıda müstahzarları 19.01’dedir. %25 bu eşiğin altında olduğundan ürün 18.06’ya gitmez. Ürün içmeye hazır olmadığından 22.02 değildir.",
      "Fasıl 18 Not 1(b) ve Genel Açıklamalar; 19.01 pozisyon metni."),
]

obj = {
    "tur": "fasil",
    "fasil": 18,
    "baslik": "Kakao ve kakao müstahzarları",
    "bolum": "IV",
    "oz": {
        "vurgu": "Fasıl 18’in pozisyon sırası kakaonun üretim sırasıdır: dane 18.01, kabuk ve döküntü 18.02, hamur 18.03, yağ 18.04, şekersiz toz 18.05; şeker veya başka madde katılıp gıda müstahzarı haline geldiğinde 18.06. Temel kural: kakao içeren gıda müstahzarları 18.06’dadır; Not 1’de sayılan pozisyonlar (Fasıl 16, 04.03, 19.01, 19.02, 19.04, 19.05, 21.05, Fasıl 22, Fasıl 30) bu kuralın istisnasıdır.",
        "maddeler": [
            "Kakao yağı kakao sayılmaz: beyaz çikolata 17.04’te, kakao yağının kendisi 18.04’tedir (Fasıl 15’e girmez).",
            "Şeker veya tatlandırıcı katılan hamur ve toz 18.06’ya geçer; süt tozu veya pepton katılan kakao tozu da 18.06’dır.",
            "Fasıl 19 ile sınır yağsız baz üzerinden hesaplanan kakao oranıyla çizilir: un-malt esaslı %40, süt esaslı %5, kavrulmuş-şişirilmiş hububat %6.",
            "Kakao oranı ne olursa olsun fasıl dışı: dondurma 21.05, bisküvi-kek 19.05, yoğurt 04.03, tüketime hazır içecekler Fasıl 22, ilaçlar 30.03 / 30.04.",
        ],
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Ağırlıkça %20’den fazla et, sakatat, kan, böcek, balık veya su omurgasızı içeriyor mu?", "Fasıl 16"],
            ["2", "Dondurma, fırıncılık ürünü, yoğurt, doldurulmuş makarna, tüketime hazır içecek veya ilaç mı?", "<b>21.05</b> / <b>19.05</b> / <b>04.03</b> / <b>19.02</b> / <b>22.02</b> / <b>22.08</b> / <b>30.03</b> / <b>30.04</b>"],
            ["3", "Un-malt esaslı ve %40’tan az ya da süt esaslı ve %5’ten az kakaolu müstahzar mı? Kakaosu %6’yı geçmeyen kavrulmuş-şişirilmiş hububat mı?*", "<b>19.01</b> / <b>19.04</b>"],
            ["4", "Beyaz çikolata mı? (kakao yağı, şeker, süt tozu; eser miktardan fazla kakao yok)", "<b>17.04</b>"],
            ["5", "Kakao danesi veya kırığı mı? (ham veya kavrulmuş)", "<b>18.01</b>"],
            ["6", "Kabuk, zar, rüşeym veya kabuk-zar içeren küspe mi?", "<b>18.02</b>"],
            ["7", "Şeker katılmamış kakao hamuru mu? (yağı alınmış olsun olmasın)", "<b>18.03</b>"],
            ["8", "Kakao yağı mı?", "<b>18.04</b>"],
            ["9", "İlave şeker, tatlandırıcı, süt tozu veya pepton içermeyen kakao tozu mu?", "<b>18.05</b>"],
            ["10", "Kakao içeren diğer gıda müstahzarı mı? (çikolata, kakaolu şekerleme, şekerli kakao tozu, sürülebilir çikolata)", "<b>18.06</b>"],
        ],
        "dipnot": "* Kakao oranları yağı tamamen alınmış baz üzerinden hesaplanır. Tamamen çikolata ile kaplanmış hububat gevreği oran ne olursa olsun 18.06’dadır (Fasıl 19 Not 3).",
    },
    "pozisyon_haritasi": [
        ["18.01", "Kakao dane ve kırıkları", "Ham veya kavrulmuş, bütün veya kırık", "Fermente kakao danesi, kakao parçaları"],
        ["18.02", "Kakao kabukları, zarları ve diğer döküntüler", "Kavurma-kırma artıkları; kabuklu küspe", "Kakao kabuğu, kakao rüşeymi"],
        ["18.03", "Kakao hamuru", "Yağı alınmış olsun olmasın; şekersiz", "Kalıp halinde kakao hamuru, kakao küspesi"],
        ["18.04", "Kakao yağı (katı ve sıvı)", "Fasıl 15’e değil buraya girer", "Tabaka halinde kakao yağı"],
        ["18.05", "Kakao tozu (şekersiz)", "Tatlandırıcı yok; alkali işlemli dahil", "Çözünür kakao, şekersiz kakao tozu"],
        ["18.06", "Çikolata ve kakao içeren diğer gıda müstahzarları", "Kakao hangi oranda olursa olsun (Not 1 hariç)", "Tablet çikolata, çikolatalı nuga, sürülebilir çikolata"],
    ],
    "notlar": [
        ["Fasıl 18 Not 1", "Fasıl 18’e dahil değildir: (a) ağırlık itibariyle <b>%20’den fazla</b> sosis, et, sakatat, kan, böcek, balık, kabuklu hayvan, yumuşakça veya diğer su omurgasızı ya da bunların bileşimini içeren gıda müstahzarları (Fasıl 16); (b) 04.03, 19.01, 19.02, 19.04, 19.05, 21.05, 22.02, 22.08, 30.03 ve 30.04 pozisyonlarında yer alan müstahzarlar."],
        ["Fasıl 18 Not 2", "İçinde kakao bulunan şeker mamulleri ve Not 1 hükmü saklı kalmak şartıyla kakao içeren diğer gıda müstahzarları 18.06’da yer alır."],
        ["Genel Açıklamalar", "Fasıl; kakaonun bütün şekillerini (daneler dahil), katı ve sıvı kakao yağını ve nispeti ne olursa olsun kakao içeren gıda müstahzarlarını kapsar. Hariç: beyaz çikolata (17.04); yağsız baz üzerinden <b>%40’tan az</b> kakao içeren un, kaba un, nişasta veya malt hülasası esaslı müstahzarlar ile <b>%5’ten az</b> kakao içeren 04.01–04.04 esaslı müstahzarlar (19.01); <b>%6’dan fazla olmayan</b> kakao içeren şişirilmiş veya kavrulmuş hububat (19.04); kakaolu pasta, kek, bisküvi (19.05); herhangi oranda kakao içeren dondurma (21.05); tüketime hazır kakaolu içecekler (Fasıl 22); ilaçlar (30.03 / 30.04); teobromin (29.39)."],
        ["Fasıl 19 Not 3", "19.04, yağsız baz üzerinden %6’dan fazla kakao içeren veya tamamen çikolata ile kaplanmış müstahzarları ve 18.06’daki kakao içeren diğer gıda müstahzarlarını kapsamaz (18.06)."],
        ["18.01 / 18.02 Açıklama Notları", "Kakao daneleri fermente edilir veya buharla işlenip kurutulur, kavrulur ve kırılır; bütün veya kırık, çiğ veya kavrulmuş daneler 18.01’dedir. Kabuklar, zarlar, rüşeymler ve kabuk-zar içeren küspeler 18.02’dedir; kabuk ve zar içermeyen kakao hamurundan yağ çıkarıldıktan sonra kalan küspe 18.03’tedir."],
        ["18.03 / 18.04 Açıklama Notları", "Kakao hamuru kavrulmuş ve temizlenmiş danelerin ezilmesiyle elde edilir; tamamen veya kısmen yağı alınmış hamur (kakao küspesi) dahil. Şeker veya tatlandırıcı katılmış hamur 18.06. Kakao yağı genellikle hamurun sıcak preslenmesiyle elde edilir; çikolata, şekercilik, kozmetik ve eczacılıkta kullanılsa da 18.04’tedir."],
        ["18.05 Açıklama Notu", "Yalnız ilave şeker veya tatlandırıcı içermeyen kakao tozu; çözünürlüğü artırmak için alkali maddelerle (sodyum veya potasyum karbonat) işlenmiş toz dahil. Şekerli, süt tozu veya pepton katılmış kakao tozu 18.06; destek madde olarak az miktarda kakao tozu içeren ilaçlar 30.03 / 30.04."],
        ["18.06 Açıklama Notu", "Çikolata esas olarak kakao hamuru ile şeker veya başka tatlandırıcıdan oluşur; blok, tablet, çubuk, pastil, granül, toz veya krema, meyve, likör vb. ile doldurulmuş halde olabilir. Kakaolu tüm şeker mamulleri (çikolatalı nuga dahil), tatlandırılmış kakao tozu, çikolata tozu, sürülebilen çikolata ve vitaminlerle zenginleştirilmiş çikolata buradadır. Hariç: beyaz çikolata 17.04; çikolata kaplı bisküviler 19.05."],
    ],
    "sinir_komsulari": [
        ["Beyaz çikolata", "17.04", "Kakao yağı kakao sayılmaz"],
        ["Kakaolu veya çikolatalı yoğurt", "04.03", "Fasıl 18 Not 1(b)"],
        ["Un, nişasta veya malt hülasası esaslı, %40’tan az kakaolu müstahzar", "19.01", "Not 1(b); Genel Açıklamalar"],
        ["Süt ürünü esaslı, %5’ten az kakaolu müstahzar", "19.01", "Not 1(b); Genel Açıklamalar"],
        ["Kakaosu %6’yı geçmeyen kavrulmuş veya şişirilmiş hububat", "19.04", "Tamamen çikolata kaplıysa 18.06"],
        ["Kakaolu kek, pasta; çikolata kaplı bisküvi", "19.05", "Fırıncılık ürünü"],
        ["Kakaolu veya çikolatalı dondurma", "21.05", "Kakao oranı ne olursa olsun"],
        ["İçmeye hazır kakaolu alkolsüz içecek", "22.02", "Fasıl 18 Not 1(b)"],
        ["Kakaolu likör", "22.08", "Fasıl 18 Not 1(b)"],
        ["Destek madde olarak kakao içeren ilaçlar", "30.03 / 30.04", "Fasıl 18 Not 1(b)"],
        ["Kakaodan çıkarılan teobromin", "29.39", "Alkaloid"],
        ["%20’den fazla et veya balık içeren kakaolu müstahzar", "Fasıl 16", "Fasıl 18 Not 1(a)"],
        ["Kahve", "09.01", "Bölüm II; kakao ise Bölüm IV"],
        ["Diğer bitkisel katı yağlar (ör. palm çekirdeği yağı)", "15.13", "Kakao yağı ise Fasıl 15 Not 1(b) gereği 18.04"],
    ],
    "tuzaklar": [
        "<b>Kakao yağı kakao sayılmaz.</b> Bu yüzden beyaz çikolata 17.04’tedir; eser miktardan fazla kakao içeren çikolata ise 18.06.",
        "<b>Kakao yağı Fasıl 15’e gitmez.</b> Bitkisel bir yağ olmasına rağmen Fasıl 15 Not 1(b) gereği 18.04’tedir.",
        "<b>Tatlandırma pozisyon değiştirir.</b> Şekersiz kakao hamuru 18.03, şekerlisi 18.06; şekersiz kakao tozu 18.05, şekerli veya süt tozu katılmışı 18.06.",
        "<b>Alkali işlem 18.05’i bozmaz.</b> Sodyum veya potasyum karbonatla işlenmiş çözünür kakao tozu 18.05’te kalır.",
        "<b>Kabuklu küspe ≠ kabuksuz küspe.</b> Kabuk ve zar içeren küspeler 18.02; kabuk ve zar içermeyen hamurdan yağ çıkarıldıktan sonra kalan küspe 18.03.",
        "<b>“Herhangi oranda kakao” kuralının istisnaları.</b> Kakaolu dondurma 21.05, bisküvi-kek 19.05, yoğurt 04.03, içecekler Fasıl 22; kakao oranı ne olursa olsun.",
        "<b>Eşikleri karıştırmayın.</b> Un-malt esaslı %40, süt esaslı %5, kavrulmuş hububat %6 (yağsız baz). Eşiğin altı Fasıl 19, üstü 18.06.",
        "<b>Kaplama gevreği taşır, bisküviyi taşımaz.</b> Tamamen çikolata ile kaplanmış mısır gevreği 18.06; çikolata kaplı bisküvi ise 19.05’te kalır.",
        "<b>Vitamin eklemek ilaç yapmaz.</b> Vitaminlerle zenginleştirilmiş çikolata 18.06’dadır; destek madde olarak az kakao içeren ilaçlar 30.03 / 30.04.",
        "<b>Teobromin kakaodan çıkarılsa da Fasıl 18 değildir.</b> Alkaloid olarak 29.39’dadır.",
    ],
    "hafiza": {
        "kanca": "Kakao fabrikası: DANE → KABUK → HAMUR → YAĞ → TOZ → ÇİKOLATA  (eşikler 40 – 5 – 6)",
        "aciklama": "Fabrikaya <b>dane</b> girer (18.01); kavrulup kırılırken <b>kabuk</b> ayrılır (18.02); öz ezilip <b>hamur</b> olur (18.03); hamur preslenince <b>yağ</b> (18.04), kalan küspe öğütülünce şekersiz <b>toz</b> (18.05) çıkar; şeker girdiği anda ürün <b>çikolata</b> ve müstahzar olur (18.06). Fabrikanın kapısında Fasıl 19 bekler: un-malt <b>40</b>, süt <b>5</b>, gevrek <b>6</b>.",
    },
    "sinav_odagi": [
        "Bu fasıl çıkmış sorularda doğrudan az sorulmuştur; daha çok Bölüm IV kapsamı ve GYK 3(b) takım sorularında seçenek olarak yer almıştır.",
        "Bir kutu çikolatanın kalem ve kol saati gibi ilgisiz eşyayla birlikte paketlenmesinin takım oluşturmadığı; takım için ortak bir ihtiyaç veya işlev şartının arandığı.",
        "Kakao ile kahvenin bölüm ayrımı: kakao Bölüm IV’te (Fasıl 18), kahve Bölüm II’de (Fasıl 9) yer alır; bölüm kapsamı sorularında çeldirici çiftlerdir.",
        "Dondurmanın kakao içersin içermesin Fasıl 21’de yer aldığı; “aynı fasılda yer alan eşya” sorularında dondurmanın ketçap, maya ve çay hülasası gibi Fasıl 21 ürünleriyle gruplanması.",
    ],
    "cikmis_ornekler": [
        {
            "soru": "Aşağıdakilerden hangisi perakende satılacak şekilde birlikte paketlenmiş olarak gümrüğe sunulduğunda set olarak değerlendirilebilir?",
            "secenekler": [
                "2 adet not defteri, 1 şişe parfüm",
                "1 kalem, 1 kol saati, 1 kutu çikolata",
                "1 kurşun kalem, 1 kalem pil, 1 kontrol kalemi",
                "1 resim fırçası, 1 kutu suluboya, 1 resim defteri",
            ],
            "cevap": "D",
            "aciklama": "GYK 3(b) takımı, özel bir gereksinmeyi karşılamak veya belirli bir işlevi yerine getirmek üzere bir araya getirilmiş eşya ister; resim fırçası, suluboya ve resim defteri resim yapma amacına hizmet eder. Kalem, kol saati ve bir kutu çikolata ortak bir işleve yönelmediğinden takım sayılmaz; çikolata tek başına 18.06’da sınıflandırılır.",
        }
    ],
    "ozet": [
        "Pozisyon sırası = üretim sırası: dane 18.01, kabuk 18.02, hamur 18.03, yağ 18.04, şekersiz toz 18.05, çikolata ve müstahzarlar 18.06.",
        "Şeker veya tatlandırıcı katılan hamur ve toz 18.06’ya geçer; süt tozu veya pepton katılan toz da 18.06.",
        "Kakao içeren gıda müstahzarları kural olarak 18.06’dadır (Not 2); istisnalar Not 1’de sayılmıştır.",
        "Not 1 istisnaları: %20’den fazla et-balık (Fasıl 16), 04.03, 19.01 (%40 / %5), 19.02, 19.04 (%6), 19.05, 21.05, 22.02, 22.08, 30.03, 30.04.",
        "Beyaz çikolata 17.04; kakao yağı 18.04 (Fasıl 15 değil); teobromin 29.39.",
        "Kakao Bölüm IV’tedir; kahve Bölüm II’dedir.",
    ],
    "sorular": sorular,
}

yaz(18, obj)
