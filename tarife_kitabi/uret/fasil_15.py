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
    q("Tarife Cetveline göre, zeytinyağı çıkarıldıktan sonra kalan zeytin katılarından (prina) çözücü ekstraksiyonu ile elde edilen ham yağ hangi pozisyonda sınıflandırılır?",
      "15.10", ["15.09", "15.15", "15.18", "15.22"], "B", T_E,
      "Fasıl 15 Not 2’ye göre zeytinden çözücüler yardımıyla elde edilen sıvı yağlar 15.09’a dahil değildir, 15.10’da yer alır; 15.10 açıklama notu ham prina yağını açıkça sayar. 15.09 yalnız mekanik veya fiziksel yollarla elde edilen yağlar içindir. 15.22 yağ artıklarını kapsar; prina yağı artık değil, yağın kendisidir.",
      "Fasıl 15 Not 2; 15.10 Açıklama Notu."),
    # 2
    q("Aşağıdakilerden hangisi Tarife Cetvelinin 15. faslında <b>sınıflandırılmaz</b>?",
      "Kakao yağı", ["Lanolin", "İspermeçet", "Balık stearini", "Ham gliserin"], "D", T_O,
      "Fasıl 15 Not 1(b) kakao yağını (katı veya sıvı) fasıl dışında bırakır; 18.04’te yer alır. Lanolin 15.05, ispermeçet 15.21, balık stearini 15.04, ham gliserin 15.20 pozisyonundadır. Tuzak, kakao yağının bitkisel bir yağ olması nedeniyle Fasıl 15’te sanılmasıdır.",
      "Fasıl 15 Not 1(b)."),
    # 3
    q("Tarife Cetvelinin 15. Fasıl notlarına göre, ağırlık itibariyle hangi oranın üzerinde 04.05 pozisyonundaki ürünleri (tereyağı ve diğer süt yağları) içeren yenilen müstahzarlar bu fasla dahil değildir?",
      "%15", ["%10", "%20", "%25", "%50"], "A", T_N,
      "Fasıl 15 Not 1(c), ağırlık itibariyle %15’ten fazla 04.05 ürünü içeren yenilen müstahzarları fasıl dışında bırakır (genellikle Fasıl 21). 15.17 açıklama notu da %15’ten fazla tereyağı veya süt yağı içeren müstahzarları hariç tutar. %20 Fasıl 16’nın et-balık eşiğidir (tuzak).",
      "Fasıl 15 Not 1(c); 15.17 Açıklama Notu."),
    # 4
    q("Tarife Cetveline göre, margarin (sıvı margarin hariç, yağda su tipi emülsiyon) hangi pozisyonda sınıflandırılır?",
      "15.17", ["15.16", "04.05", "15.18", "21.06"], "E", T_E,
      "15.17 pozisyon metni margarini ismen sayar; açıklama notu margarini hayvansal veya bitkisel yağlardan elde edilen, tereyağına benzeyen yağda su tipi emülsiyon olarak tanımlar. 04.05 sütten elde edilen yağlar, 15.16 daha ileri işlem görmemiş hidrojene yağlar, 15.18 yenilemeyen karışımlar içindir.",
      "15.17 pozisyon metni ve Açıklama Notu."),
    # 5
    q("Tarife Cetveline göre aşağıdakilerden hangisi diğerlerinden farklı bir tarife pozisyonunda yer alır?",
      "Susam yağı", ["Ayçiçeği tohumu yağı", "Aspir yağı", "Pamuk tohumu yağı", "Gossypol’u alınmış ham pamuk tohumu yağı"], "C", T_F,
      "Ayçiçeği, aspir ve pamuk tohumu yağları (gossypol’u alınmış olsun olmasın) 15.12’de birlikte yer alır. Susam yağı ise ayrı bir pozisyonda sayılmadığından diğer bitkisel sabit yağlar olarak 15.15’tedir.",
      "15.12 ve 15.15 pozisyon metinleri ve Açıklama Notları."),
    # 6
    q("Tarife Cetveline göre aşağıdakilerden hangileri 15.17 pozisyonunda sınıflandırılır?  I. Margarin (sıvı margarin hariç)  II. Taklit lard  III. Yalnızca rafine edilmiş, perakende satış ambalajında soya yağı  IV. Ağırlık itibariyle %25 tereyağı içeren yenilen yağ karışımı",
      "I ve II", ["I, II ve III", "I ve IV", "II, III ve IV", "Yalnız I"], "C", T_C,
      "Margarin ve taklit lard 15.17’dedir (I, II). Basitçe rafine edilmiş fakat daha ileri işlem görmemiş yağlar perakende satışa hazır olsalar da kendi pozisyonlarında kalır; soya yağı 15.07’dir (III). %15’ten fazla tereyağı içeren yenilen müstahzarlar Not 1(c) gereği fasıl dışıdır, genellikle Fasıl 21 (IV).",
      "15.17 Açıklama Notu; Fasıl 15 Not 1(c)."),
    # 7
    q("Tarife Cetveline göre, kuruma özelliğini iyileştirmek için ısı uygulanarak içine hava üflenmiş, kısmen oksitlenmiş ve polimerize olmuş keten tohumu yağı hangi pozisyonda yer alır?",
      "15.18", ["15.15", "15.16", "15.17", "34.03"], "A", T_E,
      "Kaynatılmış, oksitlenmiş, suyu alınmış, kükürtlenmiş, üflenmiş veya ısıyla polimerize edilmiş yağlar 15.18’dedir; açıklama notu “üflenmiş sıvı yağları” açıkça sayar. Saf keten tohumu yağı 15.15’te kalırdı; 15.16 hidrojenizasyon ve esterleme işlemleri, 15.17 yenilen karışımlar içindir.",
      "15.18 pozisyon metni ve Açıklama Notu."),
    # 8
    q("Aşağıdakilerden hangisi Tarife Cetvelinin 15.21 pozisyonunda <b>sınıflandırılmaz</b>?",
      "Japon mumu", ["Karnauba mumu", "Kandelila mumu", "Balmumu", "Çin (böcek) mumu"], "D", T_O,
      "Ticarette Japon mumu ve mersin ağacı mumu olarak bilinen ürünler gerçekte bitkisel yağdır; 15.21 açıklama notu bunları hariç tutar ve 15.15’e gönderir. Karnauba ve kandelila bitkisel mum, balmumu ve Çin mumu böcek mumu olarak 15.21’dedir.",
      "15.21 Açıklama Notu; 15.15 Açıklama Notu."),
    # 9
    q("Tarife Cetvelinin 15. Fasıl notlarına göre, zeytinden çözücüler yardımıyla elde edilen sıvı yağlar için aşağıdakilerden hangisi <b>doğrudur</b>?",
      "15.09’a dahil olmayıp 15.10’da yer alır.",
      ["Rafine edilmişlerse 15.09’da yer alır.", "Kimyasal işlem gördükleri kabul edildiğinden 15.18’de yer alır.", "Diğer bitkisel sabit yağlar olarak 15.15’te yer alır.", "Saf zeytinyağı ile karıştırılmışlarsa 15.09’da yer alır."], "B", T_N,
      "Fasıl 15 Not 2 açıktır: 15.09’a çözücüler yardımıyla zeytinden elde edilen sıvı yağlar dahil değildir, 15.10’da yer alır. 15.10 ayrıca bu yağların 15.09’daki yağlarla karışımlarını da kapsar; bu nedenle karışım 15.09’a dönmez. Rafine etmek gliserid yapısını değiştirmediğinden 15.18’e de gitmez.",
      "Fasıl 15 Not 2; 15.10 pozisyon metni."),
    # 10
    q("Tarife Cetveline göre, kuru ürün ağırlığı üzerinden %90 saflıkta olan ve sabun yapımındaki artıklardan elde edilen ham gliserin hangi pozisyonda sınıflandırılır?",
      "15.20", ["29.05", "15.22", "38.23", "15.18"], "E", T_E,
      "15.20 açıklama notuna göre ham gliserin kuru ürün ağırlığı üzerinden %95’ten az saflıktaki üründür; sabun artıklarından elde edilmesi fark etmez. %95 veya daha saf gliserin 29.05’e gider. 15.22 degra ve yağ işleme artıklarını, 38.23 sınai yağ asitleri ve yağ alkollerini kapsar.",
      "15.20 Açıklama Notu."),
    # 11
    q("Tarife Cetveline göre aşağıdakilerden hangisi diğerlerinden farklı bir fasılda yer alır?",
      "Eritilmemiş, etli kısım içermeyen taze domuz yağı",
      ["Eritilerek elde edilmiş domuz yağı (lard)", "Eritilmiş sığır don yağı", "Don yağının preslenmesiyle elde edilen oleo yağı", "Yağlı yapağıdan çıkarılan yapağı yağı"], "D", T_F,
      "Fasıl 15 Not 1(a) uyarınca 02.09’daki domuz ve kümes hayvanı yağı (eritilmemiş veya başka şekilde çıkarılmamış) Fasıl 2’dedir. Lard 15.01, don yağı 15.02, oleo yağı 15.03, yapağı yağı 15.05 ile Fasıl 15’tedir. Ayrım, yağın eritilip eritilmemesidir.",
      "Fasıl 15 Not 1(a); 15.01 Açıklama Notu."),
    # 12
    q("Tarife Cetveline göre, palm meyvesinin etli kısmından elde edilen yağ …… pozisyonunda; aynı ağacın meyve çekirdeği içindeki yenilebilir kısımdan elde edilen yağ ise …… pozisyonunda yer alır. Boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?",
      "15.11 – 15.13", ["15.13 – 15.11", "15.11 – 15.15", "15.15 – 15.13", "15.11 – 15.12"], "A", T_B,
      "15.11 açıklama notu palm yağını palm meyvelerinin etli kısımlarından elde edilen yağ olarak tanımlar ve palm çekirdeği yağı ile babassu yağını hariç tutarak 15.13’e gönderir. 15.13 Hindistan cevizi (kopra), palm çekirdeği ve babassu yağlarını kapsar.",
      "15.11 ve 15.13 Açıklama Notları."),
    # 13
    q("Aşağıdakilerden hangisi Tarife Cetvelinin 15.22 pozisyonunda <b>sınıflandırılmaz</b>?",
      "Domuz yağı eritilmesinden kalan kıkırdaklar", ["Sıvı yağ rafinasyonundan çıkan nötralizasyon patları", "Yağ asitlerinin damıtılmasından kalan stearin zifti", "Gliserolün damıtılmasından kalan gliserol zifti", "Güderi dabaklamasından kalan tabii degra"], "C", T_O,
      "Fasıl 15 Not 4’e göre sabun hammaddeleri, yağ tortuları, stearin zifti, gliserol zifti ve yapağı yağı artığı 15.22’dedir; degralar da burada yer alır. Domuz yağı ve diğer hayvansal yağların eritilmesinden kalan kıkırdaklar (donyağı tortusu) ise Not 1(d) gereği 23.01’dedir.",
      "Fasıl 15 Not 1(d) ve Not 4; 15.22 Açıklama Notu."),
    # 14
    q("Tarife Cetveline göre aşağıdaki eşya çiftlerinden hangisinde her iki eşya da aynı pozisyonda yer alır?",
      "Jojoba yağı – Japon mumu",
      ["Palm yağı – palm çekirdeği yağı", "Zeytinyağı – prina yağı", "Lard – lard stearini", "Ham gliserin – %98 saflıkta gliserin"], "E", T_F,
      "Jojoba yağı (sıvı mum olarak tanımlansa da) ve Japon mumu (gerçekte bitkisel yağ) 15.15’te birlikte yer alır. Palm yağı 15.11 – palm çekirdeği yağı 15.13; zeytinyağı 15.09 – prina yağı 15.10; lard 15.01 – lard stearini 15.03; ham gliserin 15.20 – %95 ve üzeri saflıkta gliserin 29.05’tir.",
      "15.15, 15.21 ve 15.20 Açıklama Notları; 15.01 Açıklama Notu."),
    # 15
    q("Tarife Cetvelinin 15. Fasıl notlarına göre, sadece denatüre edilmiş katı veya sıvı yağlar ve bunların fraksiyonları nerede sınıflandırılır?",
      "Denatüre edilmemiş hallerinin ait olduğu pozisyonda",
      ["Kimyasal olarak değiştirilmiş yağlar olarak 15.18’de", "Yağ işleme artıkları olarak 15.22’de", "Kimyasal ürün olarak 38.24’te", "Yağ müstahzarı olarak 15.17’de"], "B", T_N,
      "Fasıl 15 Not 3’e göre 15.18 sadece denatüre edilmiş yağları ve fraksiyonlarını kapsamaz; bunlar denatüre edilmemiş halinin yer aldığı pozisyonda sınıflandırılır. Genel açıklamalara göre bu hüküm denatüre edilmiş karışım veya müstahzarlara uygulanmaz; onlar 15.18’e gider (tuzak).",
      "Fasıl 15 Not 3; Fasıl 15 Genel Açıklamalar."),
    # 16
    q("15.03 pozisyon metni ürünlerin “emülsiyon haline getirilmemiş, karıştırılmamış veya başka şekilde hazırlanmamış” olmasını şart koşar; bu nedenle lard stearininin başka bir yağla karışımı 15.03’te sınıflandırılamaz. Genel Yorum Kurallarının açıklama notlarında bu pozisyon, pozisyon metni aksini öngördüğünde hangi kuralın uygulanamayacağına örnek olarak gösterilmiştir?",
      "GYK 2(b)", ["GYK 2(a)", "GYK 3(a)", "GYK 3(c)", "GYK 5(b)"], "A", T_G,
      "GYK 2(b), bir maddeye yapılan atfın o maddenin karışımlarını da kapsadığını söyler; ancak açıklama notuna göre bu kural ancak pozisyon veya notlarda aksine hüküm yoksa uygulanır ve örnek olarak “15.03 pozisyonu – domuz yağı karıştırılmamış” verilir. 2(a) bitirilmemiş eşya, 3(a) ve 3(c) birden fazla pozisyona girebilen eşya, 5(b) ambalaj içindir.",
      "GYK 2(b) Açıklama Notu (X); 15.03 pozisyon metni."),
    # 17
    q("Tarife Cetveline göre, sığır ayak ve incik kemiklerinin kaynatılmasıyla elde edilen yağın soğuk preslenmesiyle üretilen, saat ve dikiş makinesi gibi nazik mekanizmaların yağlanmasında kullanılan paça yağı hangi pozisyonda yer alır?",
      "15.06", ["15.02", "15.03", "15.04", "34.03"], "E", T_E,
      "15.06 açıklama notu paça yağını ve benzeri sıvı yağları açıkça sayar; 15.02 açıklama notu da hayvansal menşeli sıvı yağları (sığır paçası yağı gibi) hariç tutarak 15.06’ya gönderir. Sığırdan elde edilmesi 15.02’yi, yağlamada kullanılması 34.03’ü gerektirmez; karışım veya müstahzar değildir.",
      "15.02 ve 15.06 Açıklama Notları."),
    # 18
    q("Tarife Cetveline göre aşağıdaki işlem görmüş yağlardan hangisi diğerlerinden farklı bir tarife pozisyonunda yer alır?",
      "Hidrojene edilmiş Hint yağı (opal mumu)",
      ["Kaynatılmış keten tohumu yağı", "Suyu alınmış (dehidre edilmiş) Hint yağı", "Kükürtlenmiş sıvı yağ", "Epokside soya yağı"], "B", T_F,
      "Kaynatılmış, dehidre edilmiş, kükürtlenmiş ve epokside edilmiş yağlar kimyasal olarak değiştirilmiş yağlar olarak 15.18’dedir. Hidrojene edilmiş Hint yağı (opal mumu) ise 15.16 açıklama notunda açıkça sayılmıştır. Tuzak, iki seçenekte de Hint yağının geçmesidir.",
      "15.16 ve 15.18 Açıklama Notları."),
    # 19
    q("Aşağıdakilerden hangisi Tarife Cetvelinin 15.04 pozisyonunda <b>sınıflandırılmaz</b>?",
      "Kısmen hidrojene edilmiş balık yağı",
      ["Morina karaciğeri yağı", "Yunus yağı", "Balık stearini", "İspermeçetten ayrılarak rafine edilmiş sperm yağı"], "D", T_O,
      "15.04, balık ve deniz memelisi yağlarını rafine edilmiş olsun olmasın, kimyasal olarak değiştirilmemiş halde kapsar; balık stearini ve sperm yağı da buradadır. Kısmen veya tamamen hidrojene edilmiş, ara-esterlenmiş veya elaidik asitleşmiş olanlar 15.16’ya gider.",
      "15.04 Açıklama Notu; 15.21 Açıklama Notu (sperm yağı)."),
    # 20
    q("Tarife Cetvelinin 15. faslı ile ilgili aşağıdaki ifadelerden hangileri doğrudur?  I. Yağlar sabun, vernik veya boya imalinde kullanılacak olsalar da bu fasılda sınıflandırılır.  II. Fraksiyonlara ayırma yağın kimyasal yapısını değiştirdiğinden fraksiyonlar 15.18’e gider.  III. Rafinasyon sırasında ham soya yağından elde edilen soya lesitini 15.07’de yer alır.  IV. Rafinasyondan elde edilen asit yağları 38.23’te yer alır.",
      "I ve IV", ["I ve II", "II ve III", "I, III ve IV", "III ve IV"], "C", T_C,
      "Genel açıklamalara göre yağlar gıda veya teknik-sınai amaçla kullanılsın Fasıl 15’tedir (I doğru). Fraksiyonlara ayırma kimyasal yapıda değişiklik yapmaz; fraksiyonlar kendi pozisyonundadır (II yanlış). Soya lesitini 29.23’tedir (III yanlış). Rafinasyondan elde edilen asit yağları 38.23’tedir (IV doğru).",
      "Fasıl 15 Genel Açıklamalar; 15.07 Açıklama Notu."),
    # 21
    q("Restoranlarda derin kızartma yağı olarak kullanılmış; rep yağı, soya yağı ve az miktarda hayvansal katı yağ içeren bir yağ toplanarak hayvan yemi hazırlanmasında kullanılmak üzere satılmaktadır. Ürün henüz yem müstahzarı haline getirilmemiştir. Tarife Cetveline göre bu eşya hangi pozisyonda sınıflandırılır?",
      "15.18", ["15.17", "23.09", "15.22", "15.14"], "E", T_S,
      "15.18 açıklama notu, rap yağı, soya yağı ve az miktarda hayvansal katı yağ içeren ve hayvan yemi hazırlanmasında kullanılan kullanılmış derin kızartma yağını yenilemeyen karışım olarak açıkça kapsar. 15.17 yalnız yenilen karışımlar içindir; 23.09 hazırlanmış yem müstahzarlarını kapsar; 15.14 tek ve saf rep yağı içindir.",
      "15.18 Açıklama Notu."),
    # 22
    q("Tarife Cetveline göre aşağıdaki eşya – pozisyon eşleştirmelerinden hangisi <b>yanlıştır</b>?",
      "Balmumu ile parafin karışımı – 15.21",
      ["Saflaştırılmış yapağı yağı (lanolin) – 15.05", "Ham soya yağından elde edilen lesitin – 29.23", "Katı veya sıvı kakao yağı – 18.04", "Sütten elde edilen tereyağı – 04.05"], "C", T_B,
      "15.21 yalnız karıştırılmamış bitkisel mumları, balmumu ve diğer böcek mumlarını, ispermeçeti kapsar; böcek mumlarının bitkisel, mineral veya suni mumlarla karışımları genellikle Fasıl 34’te (34.04 veya 34.05) yer alır. Lanolin 15.05, soya lesitini 29.23, kakao yağı 18.04, tereyağı 04.05 eşleştirmeleri doğrudur.",
      "15.21 Açıklama Notu; Fasıl 15 Not 1(b); 15.07 Açıklama Notu."),
    # 23
    q("Bir litrelik plastik şişelerde perakende satışa sunulan, yalnızca rafine edilmiş ayçiçeği yağı 15.12’de sınıflandırılır; tek kullanımlık plastik şişe ayrıca sınıflandırılmaz. Ambalajın içindeki eşya ile birlikte sınıflandırılması hangi Genel Yorum Kuralına dayanır?",
      "GYK 5(b)", ["GYK 5(a)", "GYK 3(b)", "GYK 2(b)", "GYK 4"], "B", T_G,
      "GYK 5(b)’ye göre içindeki eşya ile birlikte sunulan ve bu eşyanın ambalajında normal olarak kullanılan türden ambalaj maddeleri eşya ile birlikte sınıflandırılır (sürekli kullanıma elverişli olmamak şartıyla). 5(a) belirli bir eşyaya göre yapılmış uzun ömürlü mahfazalar içindir; 3(b) karışım ve setler, 2(b) karışımlar, 4 benzerlik içindir.",
      "GYK 5(b); 15.17 Açıklama Notu (basitçe rafine edilmiş yağlar)."),
    # 24
    q("Yapağının yıkandığı sabunlu sulardan çıkarılan yağın saflaştırılmasıyla elde edilen, merhem kıvamında, suda çözünmeyen ancak çok miktarda su absorbe edebilen sarımsı beyaz bir ürün ithal edilmiştir. Ürüne ilaç veya parfüm katılmamış, kimyasal yapısı değiştirilmemiştir. Tarife Cetveline göre bu eşya hangi pozisyonda sınıflandırılır?",
      "15.05", ["15.06", "15.21", "15.22", "34.04"], "A", T_S,
      "Tarif edilen ürün lanolindir: yapağı yağının saflaştırılmasıyla elde edilir ve 15.05’te sınıflandırılır. İlaç veya parfüm katılmış lanolin Fasıl 30 veya 33’e, suda çözünecek kadar etoksile edilmiş lanolin genellikle 34.02’ye gider. Yapağı yağı artıkları 15.22’dedir; 15.21 bitkisel ve böcek mumlarını kapsar.",
      "15.05 Açıklama Notu; Fasıl 15 Not 4."),
    # 25
    q("Aşağıdakilerden hangisi Tarife Cetvelinin 15.20 pozisyonundaki ham gliserin için açıklama notlarında yapılan tanıma uygundur?",
      "Kuru ürün ağırlığı üzerinden %95’ten daha az saflıktaki gliserindir.",
      ["Kuru ürün ağırlığı üzerinden %95 veya daha fazla saflıktaki gliserindir.",
       "Yalnızca propilenden sentetik olarak elde edilen gliserindir.",
       "Kokulandırılmış veya içine kozmetik madde katılmış gliserindir.",
       "Yalnızca sabun üretiminin yan ürünü olan gliserinli lesivlerdir."], "D", T_N,
      "15.20 açıklama notu ham gliserini kuru ürün ağırlığı üzerinden %95’ten az saflıktaki ürün olarak tanımlar; katı veya sıvı yağların parçalanmasından ya da propilenden elde edilebilir. %95 ve üzeri saf gliserin 29.05’te, kokulandırılmış veya kozmetik katılmış gliserin Fasıl 33’te yer alır. Pozisyon gliserinli suları ve lesivleri de kapsar.",
      "15.20 Açıklama Notu."),
]

obj = {
    "tur": "fasil",
    "fasil": 15,
    "baslik": "Hayvansal, bitkisel veya mikrobiyal katı ve sıvı yağlar ve bunların parçalanma ürünleri; hazır yemeklik katı yağlar; hayvansal veya bitkisel mumlar",
    "bolum": "III",
    "oz": {
        "vurgu": "Fasıl 15 yağları önce kaynağına, sonra gördüğü işleme göre ayırır: hayvansal 15.01–15.06, bitkisel ve mikrobiyal 15.07–15.15; hidrojenizasyon ve esterleme 15.16, yenilen karışım ve margarin 15.17, kimyasal değişiklik ve yenilemeyen karışım 15.18. Gıda ya da sanayi amacı fark etmez; Fasıl 15 Not 1’deki istisnalar dışında yağ, yağdır.",
        "maddeler": [
            "Saf (başka yağla karışmamış) ve kimyasal olarak değişmemiş bitkisel yağlar kendi pozisyonunda kalır; rafine edilmek, fraksiyonlara ayrılmak veya perakende ambalaja konulmak pozisyonu değiştirmez.",
            "Karışım yenilebilirse 15.17 (margarin, taklit lard, shortening), yenilemezse 15.18.",
            "Yan ürünler: ham gliserin (saflık %95’ten az) 15.20; bitkisel mumlar, balmumu, ispermeçet 15.21; degra ve yağ artıkları 15.22. 15.19 boştur.",
            "Fasıl dışı: eritilmemiş domuz-kümes yağı 02.09, tereyağı 04.05, kakao yağı 18.04, yağ asitleri ve yağ alkolleri 38.23, sabun ve kozmetik Bölüm VI.",
        ],
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Fasıl 15 Not 1 istisnası mı? (eritilmemiş domuz-kümes yağı, kakao yağı, %15’ten fazla süt yağı içeren yenilen müstahzar, yağ asidi, sabun, kozmetik, taklit kauçuk)", "<b>02.09</b> / <b>18.04</b> / Fasıl 21 / Bölüm VI / <b>40.02</b>"],
            ["2", "Yağ veya mum işleme artığı mı? (degra, nötralizasyon patı, yağ tortusu, stearin zifti, gliserol zifti, yapağı yağı artığı)", "<b>15.22</b> (donyağı tortusu <b>23.01</b>, küspeler Fasıl 23)"],
            ["3", "Ham gliserin, gliserinli su veya gliserinli lesiv mi?", "<b>15.20</b> (saflık %95 ve üzeri ise <b>29.05</b>)"],
            ["4", "Karıştırılmamış bitkisel mum, balmumu, böcek mumu veya ispermeçet mi?", "<b>15.21</b> (karışımlar genellikle Fasıl 34)"],
            ["5", "Hidrojene, ara-esterlenmiş, tekrar esterlenmiş veya elaidik asitleşmiş ve daha ileri işlem görmemiş mi?", "<b>15.16</b>"],
            ["6", "Yenilen karışım veya müstahzar mı? (margarin, taklit lard, shortening, tekstüre edilmiş yağ)", "<b>15.17</b>"],
            ["7", "Kaynatılmış, oksitlenmiş, dehidre, kükürtlenmiş, üflenmiş, polimerize edilmiş ya da yenilemeyen karışım mı?*", "<b>15.18</b>"],
            ["8", "Hayvansal yağ mı?", "Domuz-kümes <b>15.01</b> · sığır-koyun-keçi <b>15.02</b> · lard stearini, oleo yağı <b>15.03</b> · balık-deniz memelisi <b>15.04</b> · yapağı yağı <b>15.05</b> · diğer <b>15.06</b>"],
            ["9", "Bitkisel veya mikrobiyal sabit yağ mı?", "Soya <b>15.07</b> · yer fıstığı <b>15.08</b> · zeytin <b>15.09</b> / <b>15.10</b> · palm <b>15.11</b> · ayçiçeği-aspir-pamuk <b>15.12</b> · kopra-palm çekirdeği-babassu <b>15.13</b> · rep-kolza-hardal <b>15.14</b> · diğer <b>15.15</b>"],
        ],
        "dipnot": "* Sadece denatüre edilmiş yağlar 15.18’e gitmez; denatüre edilmemiş hallerinin pozisyonunda kalır (Not 3). Denatüre edilmiş karışım ve müstahzarlar ise 15.18’dedir.",
    },
    "pozisyon_haritasi": [
        ["15.01", "Domuz yağı (lard dahil), kümes hayvanı yağı", "Eritilmiş veya çıkarılmış; eritilmemişi 02.09", "Lard, kemik yağı, kaz yağı"],
        ["15.02", "Sığır, koyun, keçi yağları", "Don yağı; 15.03 ürünleri hariç", "Don yağı, premier jus"],
        ["15.03", "Lard stearini, sıvı lard, oleostearin, oleo yağı, sıvı don yağı", "Presleme ürünü; karıştırılmamış, hazırlanmamış", "Oleo yağı, sıvı don yağı"],
        ["15.04", "Balık ve deniz memelisi yağları", "Rafine olabilir; hidrojene ise 15.16", "Morina karaciğeri yağı, balık stearini"],
        ["15.05", "Yapağı yağı ve türevleri", "Kimyasal olarak mum; lanolin dahil", "Lanolin, yapağı yağı oleini"],
        ["15.06", "Diğer hayvansal yağlar", "Kalıntı hayvansal pozisyon", "Paça yağı, at yağı, yumurta sarısı yağı"],
        ["15.07", "Soya yağı", "Ham veya rafine; lesitin 29.23", "Ham soya yağı"],
        ["15.08", "Yer fıstığı yağı", "Ham veya rafine", "Rafine fıstık yağı"],
        ["15.09", "Zeytinyağı", "Yalnız mekanik veya fiziksel yollarla", "Sızma zeytinyağı, rafine zeytinyağı"],
        ["15.10", "Zeytinden elde edilen diğer yağlar", "Prina yağı ve 15.09 ile karışımları", "Ham prina yağı"],
        ["15.11", "Palm yağı", "Meyvenin etli kısmından", "Ham palm yağı"],
        ["15.12", "Ayçiçeği, aspir, pamuk tohumu yağları", "Fraksiyonları dahil", "Rafine ayçiçeği yağı"],
        ["15.13", "Kopra, palm çekirdeği, babassu yağları", "Çekirdekten elde edilir", "Hindistan cevizi yağı"],
        ["15.14", "Rep, kolza, hardal yağları", "Düşük erusik asitli olanlar dahil", "Kanola yağı"],
        ["15.15", "Diğer bitkisel ve mikrobiyal sabit yağlar", "Jojoba dahil; kalıntı bitkisel pozisyon", "Keten, mısır, Hint, susam, tung yağı"],
        ["15.16", "Hidrojene, esterlenmiş, elaidik asitleşmiş yağlar", "Daha ileri işlem görmemiş", "Hidrojene soya yağı, opal mumu"],
        ["15.17", "Margarin; yenilen karışım ve müstahzarlar", "Yenilebilir; süt yağı en fazla %15", "Margarin, taklit lard, shortening"],
        ["15.18", "Kimyasal değiştirilmiş yağlar; yenilemeyen karışımlar", "Kaynatılmış, üflenmiş, kükürtlenmiş, polimerize", "Linoksin, epokside soya yağı"],
        ["15.19", "Kaldırılmış pozisyon", "Cetvelde boş bırakılmıştır", "—"],
        ["15.20", "Ham gliserin; gliserinli sular ve lesivler", "Saflık %95’ten az (kuru madde)", "Sabun lesivinden ham gliserin"],
        ["15.21", "Bitkisel mumlar, balmumu, böcek mumları, ispermeçet", "Karıştırılmamış; rafine veya boyanmış olabilir", "Karnauba mumu, balmumu"],
        ["15.22", "Degra; yağ ve mum işleme artıkları", "Yağ tortuları, patlar, ziftler", "Soap stock, stearin zifti"],
    ],
    "notlar": [
        ["Bölüm III", "Bölüm III’ün bölüm notu yoktur. Bölüm yalnız Fasıl 15’ten oluşur ve bölüm başlığı fasıl başlığıyla aynıdır."],
        ["Fasıl 15 Not 1", "Fasıl dışı: (a) 02.09’daki domuz ve kümes hayvanı yağı; (b) kakao yağı (18.04); (c) ağırlık itibariyle <b>%15’ten fazla</b> 04.05 ürünü içeren yenilen müstahzarlar (genellikle Fasıl 21); (d) donyağı tortusu (23.01) ve 23.04–23.06 artıkları; (e) yağ asitleri, müstahzar mumlar, ilaçlar, boyalar, vernikler, sabun, parfümeri, kozmetik veya tuvalet müstahzarları, sülfonatlı yağlar ve VI. Bölümdeki diğer ürünler; (f) sıvı yağlardan elde edilen taklit kauçuk (40.02)."],
        ["Fasıl 15 Not 2", "15.09’a çözücüler yardımıyla zeytinden elde edilen sıvı yağlar dahil değildir (15.10)."],
        ["Fasıl 15 Not 3", "15.18, sadece denatüre edilmiş katı veya sıvı yağları ve fraksiyonlarını kapsamaz; bunlar denatüre edilmemiş hallerinin uygun pozisyonunda sınıflandırılır."],
        ["Fasıl 15 Not 4", "Sabun hammaddeleri, yağ tortuları ve posaları, stearin zifti, gliserol zifti ve yapağı yağı artığı 15.22’de yer alır."],
        ["Genel Açıklamalar", "Not 1 istisnaları saklı kalmak üzere yağlar gıda olarak da teknik veya sınai amaçla (sabun, mum, yağlayıcı, vernik, boya imali) da kullanılsa Fasıl 15’tedir. 15.07–15.15 rafine edilmiş olsun olmasın, kimyasal olarak değişmemiş, saf (başka yağla karışmamış) yağları ve fraksiyonlarını kapsar; fraksiyonlara ayırma kimyasal yapıyı değiştirmez."],
        ["Genel Açıklamalar", "“Sadece denatüre edilmiş” yağlar: genellikle %1’den az denatürant (balık yağı, fenoller, terebantin yağı, toluen vb.) katılarak yenilemez hale getirilmiş yağlardır. Not 3 denatüre edilmiş karışım veya müstahzarlara uygulanmaz (15.18)."],
        ["15.09 Açıklama Notu", "Saf zeytinyağı yalnızca mekanik veya diğer fiziksel yollarla elde edilir; yıkama, süzme, santrifüj ve filtrasyon dışında işlem görmez. Serbest asitlik (oleik asit, 100 g’da): ekstra sızma en fazla 0,8 g, saf (natürel) zeytinyağı en fazla 2,0 g, rafine zeytinyağı en fazla 0,3 g. Prina yağı 15.10, tekrar esterleşmiş zeytin yağı 15.16."],
        ["15.16 Açıklama Notu", "Hidrojene, ara-esterlenmiş, tekrar esterlenmiş veya elaidik asitleşmiş yağlar koku giderme gibi iyileştirmeden geçmiş olsa da 15.16’dadır; gıda amacıyla tekstürasyon gibi daha ileri işlem görmüşleri 15.17’ye gider. Hidrojene Hint yağı (opal mumu) 15.16."],
        ["15.17 Açıklama Notu", "Margarin yağda su tipi emülsiyondur. Basitçe rafine edilmiş yağlar perakende satışa hazır olsalar da kendi pozisyonlarında kalır. %15’ten fazla tereyağı veya süt yağı içeren müstahzarlar genellikle Fasıl 21."],
        ["15.18 Açıklama Notu", "Kaynatılmış, oksitlenmiş, üflenmiş, dehidre (Hint yağı), kükürtlenmiş, ısıyla polimerize edilmiş, maleik, epokside, bromlu yağlar ile yenilemeyen karışımlar (ör. hayvan yemi hazırlanmasında kullanılan kullanılmış kızartma yağı). Sülfonlanmış yağlar 34.02; yem müstahzarları 23.09."],
        ["15.20 Açıklama Notu", "Ham gliserin kuru ürün ağırlığı üzerinden <b>%95’ten az</b> saflıktadır; gliserinli sular ve lesivler de buradadır. %95 veya daha saf gliserin 29.05; ilaç halindeki 30.03 / 30.04; kokulandırılmış veya kozmetik katılmış Fasıl 33."],
        ["15.21 Açıklama Notu", "Karıştırılmamış bitkisel mumlar, balmumu ve diğer böcek mumları, ispermeçet. Mum karışımları ve mumların başka maddelerle karışımları genellikle Fasıl 34; kovan için petek haline getirilmiş mum 96.02; jojoba yağı, mersin ağacı mumu ve Japon mumu 15.15; sperm yağı 15.04."],
        ["15.04 / 15.05 Açıklama Notları", "Balık karaciğeri yağları vitamin muhtevası artırılmış olsa da 15.04’tedir; ilaç olarak veya tedavi amacıyla madde katılırsa Fasıl 30. Yapağı yağı gliserol esteri olmadığından kimyasal olarak mum sayılır; lanolin 15.05, ilaçlı veya parfümlü lanolin Fasıl 30 veya 33."],
    ],
    "sinir_komsulari": [
        ["Eritilmemiş domuz ve kümes hayvanı yağı", "02.09", "Fasıl 15 Not 1(a)"],
        ["Tereyağı ve sütten elde edilen diğer yağlar", "04.05", "Süt ürünü"],
        ["Kakao yağı", "18.04", "Fasıl 15 Not 1(b)"],
        ["%15’ten fazla süt yağı içeren yenilen müstahzar", "Fasıl 21 (genellikle)", "Fasıl 15 Not 1(c)"],
        ["Kıkırdaklar (donyağı tortusu); yağlı küspeler", "23.01 / 23.04–23.06", "Fasıl 15 Not 1(d)"],
        ["Sınai yağ asitleri, rafinaj asit yağları, sınai yağ alkolleri", "38.23", "Not 1(e); VI. Bölüm ürünü"],
        ["%95 veya daha saf gliserin", "29.05", "15.20 yalnız ham gliserin"],
        ["Soya lesitini", "29.23", "15.07 Açıklama Notu"],
        ["Sabun; sülfonlanmış yağlar", "34.01 / 34.02", "Fasıl 15 Not 1(e)"],
        ["Mum karışımları, müstahzar mumlar", "34.04", "15.21 yalnız karıştırılmamış mumlar"],
        ["Işık temini için fitilli mumlar", "34.06", "Wax değil, aydınlatma mumu"],
        ["Parafin ve diğer mineral mumlar", "27.12", "Mineral menşeli"],
        ["Sıvı yağlardan elde edilen taklit kauçuk", "40.02", "Fasıl 15 Not 1(f)"],
        ["Hayvan yemi müstahzarları", "23.09", "15.18 hariç tutması"],
        ["Kovan için petek haline getirilmiş mum", "96.02", "15.21 hariç tutması"],
    ],
    "tuzaklar": [
        "<b>Eritilmemiş domuz yağı Fasıl 2’dedir.</b> Etli kısım içermeyen, eritilmemiş veya başka şekilde çıkarılmamış domuz ve kümes hayvanı yağı 02.09; eritilmiş lard 15.01.",
        "<b>Sığırdan gelen her yağ 15.02 değildir.</b> Don yağının preslenmesiyle elde edilen oleo yağı, sıvı don yağı, oleostearin 15.03; sığır paçası yağı gibi hayvansal sıvı yağlar 15.06.",
        "<b>Palm yağı ≠ palm çekirdeği yağı.</b> Meyvenin etli kısmından 15.11; çekirdekten 15.13 (kopra ve babassu ile birlikte).",
        "<b>Zeytinde elde etme yöntemi belirleyicidir.</b> Mekanik-fiziksel yolla 15.09; çözücüyle elde edilen prina yağı ve bunun zeytinyağı ile karışımı 15.10; tekrar esterleşmiş zeytin yağı 15.16.",
        "<b>Rafine etmek ve şişelemek pozisyon değiştirmez.</b> Sadece rafine edilmiş ayçiçeği yağı perakende şişede de 15.12’dedir; 15.17 karışım veya müstahzar ister.",
        "<b>Hint yağı üç ayrı yerde.</b> Saf Hint yağı 15.15; hidrojene Hint yağı (opal mumu) 15.16; suyu alınmış (dehidre) Hint yağı 15.18.",
        "<b>Adında “mum” geçen her şey 15.21 değildir.</b> Japon mumu ve mersin ağacı mumu gerçekte bitkisel yağdır (15.15); jojoba yağı sıvı mum olsa da 15.15; mum karışımları 34.04; fitilli mum 34.06; parafin 27.12.",
        "<b>Gliserinde eşik %95.</b> Kuru madde üzerinden %95’ten az saflıkta ham gliserin 15.20; %95 ve üzeri 29.05.",
        "<b>Sadece denatüre edilmiş yağ 15.18’e gitmez.</b> Denatüre edilmemiş halinin pozisyonunda kalır (Not 3); denatüre edilmiş karışım ise 15.18.",
        "<b>Yağ asidi ve yağ alkolü Fasıl 15 değildir.</b> Sınai yağ asitleri, rafinaj asit yağları ve sınai yağ alkolleri 38.23; nötralizasyon patları ise 15.22.",
    ],
    "hafiza": {
        "kanca": "“Soyadı Yerli Zeytinci Prens Palmiye, Ayçiçeğini Koparıp Repçe Dikti”",
        "aciklama": "Bitkisel sıra 15.07–15.15: <b>So</b>ya · <b>Yer</b> fıstığı · <b>Zeytin</b> · <b>Pr</b>ina · <b>Palm</b> · <b>Ay</b>çiçeği · <b>Ko</b>pra · <b>Rep</b> · <b>Di</b>ğer. Hayvansal sıra 15.01–15.06: domuz, sığır, stearin, balık, yapağı, diğer. Ardından üç işlem basamağı: <b>hidro</b> 15.16 → <b>yenir karışım</b> 15.17 → <b>kimya / yenmez</b> 15.18; en sonda gliserin 15.20, mum 15.21, artık 15.22.",
    },
    "sinav_odagi": [
        "Bu fasıl çıkmış sorularda az sayıda ve çoğunlukla “hangi pozisyonda yer alır” kalıbıyla, Fasıl 15 ile Bölüm VI (Fasıl 29, 34, 38) arasındaki sınır üzerinden sorulmuştur.",
        "Sınai yağ alkollerinin Fasıl 15’te değil 38.23’te yer aldığı; seçeneklerde 15.18, 15.20 ve Fasıl 29, 38 pozisyonlarının çeldirici olarak kullanılması.",
        "Ham gliserinin (gliserinli sular ve lesivler dahil) 15.20’de yer aldığı; saf gliserin, kozmetik ve ilaç seçenekleriyle karıştırılması.",
        "“Mum” kelimesinin iki anlamı: ışık temini için fitilli mum 34.06’dadır ve aydınlatma cihazı aksamı sayılmaz; bitkisel mumlar ve balmumu ise 15.21’dedir.",
        "GYK 3(b) set sorularında bir şişe sıvı yağın (Fasıl 15) diğer gıdalarla birlikte bir koliye konulmasının, ortak bir ihtiyaca yönelmediği sürece set oluşturmadığı.",
    ],
    "cikmis_ornekler": [
        {
            "soru": "Tarife Cetveline göre sınai yağ alkolleri aşağıdaki tarife pozisyonlarından hangisinde yer alır?",
            "secenekler": ["15.18", "15.20", "29.34", "38.23", "38.24"],
            "cevap": "D",
            "aciklama": "Fasıl 15 Not 1 ve Genel Açıklamalar, yağ asitlerini, yağ alkollerini ve VI. Bölümdeki diğer ürünleri fasıl dışında bırakır. Sınai yağ alkolleri; sınai monokarboksilik yağ asitleri ve rafinaj asit yağlarıyla birlikte 38.23’te yer alır.",
        }
    ],
    "ozet": [
        "Kaynak + işlem derecesi = pozisyon: hayvansal 15.01–15.06, bitkisel ve mikrobiyal 15.07–15.15.",
        "Hidrojene vb. 15.16; yenilen karışım ve margarin 15.17; kimyasal değişmiş veya yenilemeyen karışım 15.18.",
        "Yan ürünler: ham gliserin 15.20, mumlar 15.21, degra ve artıklar 15.22; 15.19 boştur.",
        "Not 1 dışı: 02.09, 18.04, %15 süt yağı eşiği (Fasıl 21), 23.01 / 23.04–23.06, VI. Bölüm, 40.02.",
        "Gıda veya sanayi amacı fark etmez; rafine etmek, fraksiyonlamak ve şişelemek pozisyonu değiştirmez.",
        "Bölüm III’ün bölüm notu yoktur; bölüm yalnız Fasıl 15’ten ibarettir.",
    ],
    "sorular": sorular,
}

yaz(15, obj)
