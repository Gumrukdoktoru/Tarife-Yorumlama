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
    q("Tarife Cetveline göre, kılıf içinde tütsülenmiş, dilimlenerek hava geçirmez kutulara konulmuş salam hangi pozisyonda sınıflandırılır?",
      "16.01", ["16.02", "02.10", "16.03", "21.06"], "D", T_E,
      "16.01 açıklama notuna göre sosis ve benzeri ürünler çiğ veya pişmiş, tütsülenmiş veya tütsülenmemiş olabilir; dilimlenmiş olmaları ya da hava geçirmez kaplara konulmaları sınıflandırmayı değiştirmez. Tütsüleme Fasıl 2 işlemi olsa da kıyılmış etin kılıfa doldurulmasıyla elde edilen salam 02.10’da kalmaz; 16.02 sosis dışındaki et müstahzarları içindir.",
      "16.01 Açıklama Notu; Fasıl 2 Genel Açıklamalar."),
    # 2
    q("Aşağıdakilerden hangisi Tarife Cetvelinin 16. faslında <b>sınıflandırılmaz</b>?",
      "Kabuğu içinde suda haşlanmış, dondurulmuş karides",
      ["Ton balığı konservesi", "Sirke ve baharatla hazırlanmış hamsi (marinade)", "Havyar", "Ekmek kırıntısıyla kaplanmış karides"], "B", T_O,
      "Kabukları içinde buharda veya suda pişirilmiş kabuklu hayvanlar 03.06’da kalır; 16.05 açıklama notu bunları açıkça hariç tutar. Ton konservesi, sirkede hamsi ve havyar 16.04’te; yalnızca ekmek kırıntısıyla kaplanmış karides ise Fasıl 3’te sayılmayan bir işlem gördüğünden 16.05’tedir.",
      "Fasıl 16 Not 1; 16.05 Açıklama Notu; Fasıl 16 Genel Açıklamalar."),
    # 3
    q("Tarife Cetvelinin 16. Fasıl notlarına göre, gıda müstahzarlarının bu fasılda yer alabilmesi için ağırlık itibariyle ne kadar sosis, et, sakatat, kan, böcek, balık veya su omurgasızı (ya da bunların bileşimini) içermesi gerekir?",
      "%20’den fazla", ["%10’dan fazla", "%15’ten fazla", "%20 veya daha az", "%50’den fazla"], "E", T_N,
      "Fasıl 16 Not 2’ye göre gıda müstahzarları ağırlık itibariyle %20’den fazla bu ürünleri veya bunların herhangi bir bileşimini içermeleri şartıyla Fasıl 16’da yer alır. %15, Fasıl 15’teki süt yağı eşiğidir (tuzak); oranın tek bir bileşen için değil toplam için arandığına dikkat edilmelidir.",
      "Fasıl 16 Not 2."),
    # 4
    q("Tarife Cetveline göre, yalnızca ekmek kırıntısı ile kaplanmış, pişirilmemiş, dondurulmuş morina balığı filetoları hangi pozisyonda sınıflandırılır?",
      "16.04", ["03.04", "03.03", "16.05", "03.05"], "A", T_E,
      "16.04 açıklama notu, 03.02 ila 03.05’te belirtilen yöntemlerden başka şekilde hazırlanan balıkları, örneğin sadece pasta hamuru veya ekmek kırıntısı ile kaplanmış balık filetolarını kapsar. Kaplama Fasıl 3 işlemi olmadığından fileto pişmemiş ve dondurulmuş olsa da 03.04’te kalmaz. 16.05 kabuklu ve yumuşakçalar içindir.",
      "16.04 Açıklama Notu; Fasıl 16 Not 1."),
    # 5
    q("Tarife Cetveline göre aşağıdakilerden hangisi diğerlerinden farklı bir tarife pozisyonunda yer alır?",
      "Konserve yengeç", ["Ton balığı konservesi", "Hamsi ezmesi", "Havyar", "Balık sosisi"], "C", T_F,
      "Ton konservesi, hamsi ezmesi, havyar ve balık sosisi 16.04’tedir; balık sosisi, et sosisleri gibi 16.01’e değil, açıklama notunda sayıldığı üzere 16.04’e girer (tuzak). Yengeç kabuklu hayvan olduğundan hazırlanmış veya konserve edilmiş hali 16.05’tedir.",
      "16.04 ve 16.05 Açıklama Notları."),
    # 6
    q("Plastik tabakta dondurulmuş bir hazır yemek; pişmiş pirinç, sebze ve sos ile birlikte ızgara tavuk parçalarından oluşmaktadır. Satışa sunulduğu haliyle ürünün ağırlıkça %28’i tavuk etidir (üretimde kullanılan çiğ tavuk oranı %35’tir); başka et veya balık içermez. Tarife Cetveline göre bu eşya hangi pozisyonda sınıflandırılır?",
      "16.02", ["19.04", "21.06", "16.01", "21.04"], "E", T_S,
      "Fasıl 16 Not 2’ye göre %20’den fazla et içeren gıda müstahzarları (“hazır öğünler” dahil) Fasıl 16’dadır; ağırlık satışa sunulduğu andaki et ağırlığıdır. %28 tavuk eti eşiği aşar ve tek hayvansal bileşen et olduğundan pozisyon 16.02’dir. Ürün sosis olmadığından 16.01, çorba olmadığından 21.04 değildir.",
      "Fasıl 16 Not 2; Fasıl 16 Genel Açıklamalar; 16.02 Açıklama Notu."),
    # 7
    q("Tarife Cetveline göre, kabukları çıkarılmış, sirke ve baharatla hazırlanarak cam kavanozlara konulmuş midyeler hangi pozisyonda sınıflandırılır?",
      "16.05", ["03.07", "16.04", "16.03", "21.04"], "B", T_E,
      "Sirke içinde hazırlama Fasıl 3’te sayılan işlemlerden değildir. 16.05 açıklama notu, 16.04 için belirtilen hazırlama şekillerinin (sirke, sıvı yağ vb. içinde hazırlama) gerekli değişikliklerle kabuklu, yumuşakça ve diğer su omurgasızlarına uygulanacağını belirtir; midye bu pozisyonda sayılmıştır. 16.04 balıklar içindir.",
      "16.05 Açıklama Notu; 16.04 Açıklama Notu."),
    # 8
    q("Aşağıdakilerden hangisi Tarife Cetvelinin 16.01 pozisyonunda <b>sınıflandırılmaz</b>?",
      "Pişirilmiş ve hafif kemikli rulo hindi eti",
      ["Kümes hayvanı karaciğerinden yapılmış karaciğer sosisi", "Kanlı sucuk (black pudding)", "Kılıfsız, sosisin karakteristik şeklinde preslenmiş et ürünü", "Sosis kılıfına konulmuş pate"], "D", T_O,
      "16.01 açıklama notu, pişirilmiş ve hafif kemikli kümes hayvanlarını (rulo hindi eti gibi) hariç tutarak 16.02’ye gönderir. Karaciğer sosisleri, kanlı sucuk, kılıfsız fakat sosis şeklinde preslenmiş ürünler ve sosis kılıfına konulmuş pateler 16.01’de açıkça sayılmıştır.",
      "16.01 Açıklama Notu."),
    # 9
    q("Fasıl 16 genel açıklamalarına göre, bir gıda müstahzarındaki et, balık vb. oranının (%20 eşiği) hesaplanmasında hangi ağırlık dikkate alınır?",
      "Satışa sunulduğu andaki müstahzarda bulunan et, balık vb. ağırlığı",
      ["Üretimden önce kullanılan çiğ et, balık vb. hammaddelerin ağırlığı", "Ambalaj dahil müstahzarın toplam brüt ağırlığı", "Müstahzardaki et, balık vb.nin yalnızca kuru madde ağırlığı", "Kemik ve kılçıkları ayrılmış çiğ hammaddenin net ağırlığı"], "A", T_N,
      "Genel açıklamalar açıktır: tüm durumlarda dikkate alınması gereken ağırlık, satışa sunulduğu zaman müstahzardaki et, balık vb. ağırlığıdır; yapımından önce kullanılan maddelerin ağırlığı değildir. Pişirmede ağırlık kaybı olsa bile hesap nihai ürün üzerinden yapılır.",
      "Fasıl 16 Genel Açıklamalar; Fasıl 16 Not 2."),
    # 10
    q("Tarife Cetveline göre, basınç altında suda haşlanan sığır etinden alınan sıvının yağı ayrıldıktan sonra konsantre edilmesiyle elde edilen macun kıvamındaki et hülasası hangi pozisyonda yer alır?",
      "16.03", ["21.04", "16.02", "02.10", "21.03"], "C", T_E,
      "16.03 açıklama notu et hülasalarını; basınç altında suda haşlama veya buharlama ile etten alınan sıvının yağı ayrıldıktan sonra konsantre edilmesiyle elde edilen ürünler olarak tanımlar. 21.04 çorbaları ve et sularını (tablet, küp dahil), 21.03 sosları kapsar; 16.02 hülasaları hariç tutar.",
      "16.03 Açıklama Notu."),
    # 11
    q("Tarife Cetveline göre aşağıdakilerden hangisi diğerlerinden farklı bir fasılda yer alır?",
      "Tuzlanmış ve tütsülenmiş çiğ domuz eti",
      ["Kılıf içinde pişirilmiş sosis", "Konserve kutusunda pişirilmiş jambon", "Konsantre edilmiş sığır eti hülasası", "Zeytinyağlı ton balığı konservesi"], "A", T_F,
      "Tuzlama ve tütsüleme Fasıl 2’de sayılan işlemlerdir; pişirilmemiş tuzlu-tütsülü et 02.10’dadır (Fasıl 2). Sosis 16.01, pişirilmiş jambon 16.02, et hülasası 16.03, ton konservesi 16.04 ile Fasıl 16’dadır. Tuzak, tütsülemenin “hazırlama” sanılmasıdır.",
      "Fasıl 16 Not 1; Fasıl 2 Genel Açıklamalar."),
    # 12
    q("Aşağıdakilerden hangisi Tarife Cetvelinin 16.03 pozisyonunda <b>sınıflandırılmaz</b>?",
      "Tablet halinde et suyu (bulyon)",
      ["Sığır eti hülasası", "Çiğ etin preslenmesiyle elde edilen et suyu", "Balık kaba unundan elde edilen balık hülasası", "Çiğ yumuşakçaların preslenmesiyle elde edilen su"], "D", T_O,
      "16.03 açıklama notu; tablet veya küp şeklindekiler dahil çorbaları, et sularını ve bunların müstahzarlarını hariç tutarak 21.04’e gönderir. Et hülasası, çiğ etin preslenmesiyle elde edilen et suyu, balık hülasası ve çiğ su omurgasızlarından preslenerek elde edilen sular 16.03’tedir.",
      "16.03 Açıklama Notu."),
    # 13
    q("Bölüm IV notuna göre “pellet” tabiri aşağıdakilerden hangisini ifade eder?",
      "Doğrudan sıkıştırma veya ağırlığının %3’ünü geçmeyen bağlayıcı ilavesiyle küçük topaklar halinde birleştirilen ürünler",
      ["Ağırlığının %5’ini geçmeyen oranda bağlayıcı ilavesiyle küçük topaklar halinde bir araya getirilen ürünler",
       "Yalnızca bağlayıcı kullanılmadan, doğrudan doğruya sıkıştırma suretiyle küçük topaklar haline getirilen ürünler",
       "Ağırlığının %20’sini geçmeyecek oranda et veya balık içeren, sıkıştırılarak topak haline getirilen ürünler",
       "Bağlayıcı oranına bakılmaksızın yalnızca hayvan yemi olarak kullanılan sıkıştırılmış küçük topaklar"], "B", T_N,
      "Bölüm IV notu pelleti, doğrudan doğruya sıkıştırma suretiyle veya ağırlığının %3’ünü geçmeyecek oranda bir bağlayıcı ilavesiyle küçük topaklar halinde bir araya getirilen ürünler olarak tanımlar. Bağlayıcı kullanımı serbesttir ama sınırlıdır; tanım kullanım amacına bağlı değildir.",
      "Bölüm IV Not 1."),
    # 14
    q("Tarife Cetveline göre, kızartılarak pişirilmiş, baharatlanmış ve plastik kaplarda dondurularak satışa sunulan yenilebilir çekirgeler hangi pozisyonda sınıflandırılır?",
      "16.02", ["04.10", "05.11", "16.01", "21.06"], "E", T_E,
      "Fasıl 4 Not 6’ya göre 04.10 yalnız taze, soğutulmuş, dondurulmuş, kurutulmuş, tütsülenmiş, tuzlanmış veya salamura edilmiş yenilebilir böcekleri kapsar; başka şekilde hazırlananlar Bölüm IV’e gider. Fasıl 16 başlığı ve 16.02 metni böcekleri içerir; kızartma Fasıl 4 işlemi değildir. 05.11 yenmeyen böcekler içindir.",
      "Fasıl 4 Not 6; Fasıl 16 Not 1; 16.02 pozisyon metni."),
    # 15
    q("Tarife Cetveline göre aşağıdaki eşya çiftlerinden hangisinde her iki eşya da aynı pozisyonda yer alır?",
      "Balık sosisi – sirkede ringa balığı",
      ["Havyar – hazırlanmamış taze balık yumurtası", "Kabuğunda buharda pişirilmiş karides – kabuğu çıkarılıp haşlanmış karides", "Et hülasası – et suyu tableti", "Kanlı sucuk – sucuk şeklinde olmayan kan müstahzarı"], "C", T_F,
      "Balık sosisleri ve sirkede hazırlanmış balıklar 16.04’te birlikte yer alır. Havyar 16.04 – taze balık yumurtası Fasıl 3; kabuğunda pişen karides 03.06 – kabuğu çıkarılıp haşlanan 16.05; et hülasası 16.03 – et suyu tableti 21.04; kanlı sucuk 16.01 – diğer kan müstahzarları 16.02’dir.",
      "16.01, 16.02, 16.03, 16.04 ve 16.05 Açıklama Notları."),
    # 16
    q("Fasıl 16 Not 2’ye göre, ağırlık itibariyle %12 tavuk eti ve %15 karides içeren (başka et, balık vb. içermeyen) bir gıda müstahzarı hangi pozisyonda sınıflandırılır?",
      "16.05", ["16.02", "16.04", "16.01", "21.06"], "B", T_N,
      "Not 2’deki %20 eşiği bileşenlerin toplamına uygulanır: %12 + %15 = %27 olduğundan müstahzar Fasıl 16’dadır. İki veya daha fazla bileşen varsa ağırlıkça fazla olan bileşenin pozisyonu esas alınır; karides (%15) tavuktan (%12) fazla olduğundan 16.05. Tek tek hiçbirinin %20’yi aşmaması müstahzarı fasıl dışına çıkarmaz (tuzak).",
      "Fasıl 16 Not 2."),
    # 17
    q("Aşağıdakilerden hangisi Tarife Cetvelinin 16. faslında <b>yer almaz</b>?",
      "İnsan tüketimine uygun balık unu",
      ["Ciğer ezmesi (pate)", "Kan müstahzarı", "Morina balığı yumurtasından hazırlanmış havyar benzeri", "İyice homojenize edilmiş et müstahzarı"], "D", T_O,
      "Fasıl 16 genel açıklamaları insan gıdası olarak elverişli et ve sakatat unlarını (02.10), balık unlarını (03.09) ve böcek unlarını (04.10) fasıl dışında bırakır. Pate, kan müstahzarı ve homojenize et müstahzarı 16.02’de; havyar benzerleri 16.04’tedir.",
      "Fasıl 16 Genel Açıklamalar; Fasıl 3 Not 3."),
    # 18
    q("Karton bir kutuda birlikte perakende satışa sunulan; çörek içinde sığır etinden oluşan bir sandviç (peynirli olsun olmasın) ile patates kızartmasından oluşan takımın sınıflandırılmasında aşağıdakilerden hangisi doğrudur?",
      "GYK 3(b) uygulanır; takım 16.02 pozisyonunda sınıflandırılır.",
      ["GYK 3(b) uygulanır; takım 20.04 pozisyonunda sınıflandırılır.",
       "GYK 3(c) uygulanır; takım numara sırasına göre sonuncu olan 20.04 pozisyonunda sınıflandırılır.",
       "GYK 1 uygulanır; takım ekmekçilik ürünü olarak 19.05 pozisyonunda sınıflandırılır.",
       "GYK 3(a) uygulanır; takım sosis benzeri ürün olarak 16.01 pozisyonunda sınıflandırılır."], "A", T_G,
      "GYK 3(b) açıklama notu bu takımı “perakende satılacak hale getirilmiş takım” örneği olarak verir: 16.02’deki çörek içinde sığır eti sandviçi ile 20.04’teki patates kızartması birlikte paketlendiğinde takım 16.02’de sınıflandırılır. Esas niteliği sandviç verdiğinden 3(c)’ye geçilmez.",
      "GYK 3(b) Açıklama Notu (X)."),
    # 19
    q("Tarife Cetveline göre aşağıdaki eşya – pozisyon eşleştirmelerinden hangisi <b>doğrudur</b>?",
      "Kanlı sucuk (black pudding) – 16.01",
      ["Balık sosisi – 16.01", "Pişirilmiş rulo hindi eti – 16.01", "Et suyu tableti – 16.03", "Kabuğu içinde haşlanmış ıstakoz – 16.05"], "E", T_B,
      "Kanlı sucuk 16.01 açıklama notunda açıkça sayılmıştır. Balık sosisleri 16.04’te, pişirilmiş rulo hindi eti 16.02’de, et suyu tabletleri 21.04’te, kabuğu içinde haşlanmış kabuklular ise 03.06’da yer alır.",
      "16.01, 16.03, 16.04 ve 16.05 Açıklama Notları."),
    # 20
    q("Tarife Cetveline göre aşağıdaki hazır gıdalardan hangisi diğerlerinden farklı bir fasılda yer alır?",
      "Ağırlıkça %30 et içeren ravioli (doldurulmuş makarna)",
      ["Ağırlıkça %30 tavuk eti içeren pilavlı hazır yemek", "Ağırlıkça %25 ton balığı içeren makarnalı salata", "Ağırlıkça %40 sığır eti içeren sebzeli konserve yemek", "Ağırlıkça %22 karides içeren pilav"], "C", T_F,
      "Fasıl 16 Not 2’deki %20 kuralı 19.02’deki doldurulmuş ürünlere uygulanmaz; ravioli et oranı ne olursa olsun 19.02’dedir (Fasıl 19). Diğer hazır yemekler %20’den fazla et, balık veya kabuklu içerdiğinden Fasıl 16’dadır (16.02, 16.04, 16.02, 16.05).",
      "Fasıl 16 Not 2; 16.02 Açıklama Notu (hariç tutmalar)."),
    # 21
    q("Tarife Cetveline göre aşağıdakilerden hangileri 16.02 pozisyonunda sınıflandırılır?  I. Tuz ve biberle baharatlanmış çiğ sığır eti  II. Pişirilmiş işkembe  III. Proteolitik enzimle (papain) yumuşatılmış çiğ dana eti  IV. Sosis şeklinde olmayan ciğer ezmesi",
      "I, II ve IV", ["Yalnız IV", "II ve IV", "I ve III", "III ve IV"], "D", T_C,
      "Fasıl 2 genel açıklamalarına göre biber ve tuz gibi baharatlarla işlem görmüş et (I) ve sosis niteliği taşımayan ciğer ezmeleri (IV) 16.02’dedir; 05.04 açıklama notuna göre pişirilmiş işkembe Fasıl 16’ya gider (II). Proteolitik enzimle yumuşatılmış çiğ et ise Fasıl 2’de kalır (III).",
      "Fasıl 2 Genel Açıklamalar; 05.04 Açıklama Notu; 16.02 Açıklama Notu."),
    # 22
    q("Fasıl 16 Not 2’ye göre, ağırlık itibariyle %20’den fazla et veya balık içerse bile …… pozisyonundaki doldurulmuş ürünler ile …… ve 21.04 pozisyonlarındaki müstahzarlar bu fasılda sınıflandırılmaz. Boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?",
      "19.02 – 21.03", ["19.05 – 21.03", "19.02 – 21.06", "19.04 – 21.05", "19.01 – 21.06"], "A", T_B,
      "Not 2’nin son cümlesi, %20 kuralının 19.02 pozisyonundaki doldurulmuş ürünlere (ravioli, mantı) ve 21.03 (soslar, çeşniler) ile 21.04 (çorbalar, et suları, homojenize bileşik müstahzarlar) pozisyonlarındaki müstahzarlara uygulanmayacağını belirtir. 21.06 kalıntı pozisyondur ve istisna olarak sayılmamıştır.",
      "Fasıl 16 Not 2."),
    # 23
    q("Morina balığının yumurtaları yıkanmış, yapışık oldukları zarlardan temizlenmiş, tuzlanıp hafifçe preslenmiş, baharat ilave edilerek siyaha boyanmış ve küçük cam kavanozlara konulmuştur. Ürün ekmek üzerine sürülerek tüketilmek üzere perakende satılmaktadır. Tarife Cetveline göre bu eşya hangi pozisyonda sınıflandırılır?",
      "16.04", ["03.05", "16.05", "04.10", "16.03"], "C", T_S,
      "16.04 açıklama notuna göre havyar benzerleri, mersin balığı dışındaki balıkların (morina dahil) yumurtalarından yıkama, temizleme, tuzlama ve bazen presleme ile hazırlanan, baharat ilave edilmiş ve boyanmış olabilen müstahzarlardır. Fasıl 3 Not 1 havyar ve havyar benzerlerini 16.04’e gönderir. Balık yumurtası Fasıl 4’e (04.10) girmez.",
      "16.04 Açıklama Notu; Fasıl 3 Not 1."),
    # 24
    q("Tarife Cetvelinin 16. faslı ile ilgili aşağıdaki ifadelerden hangileri doğrudur?  I. Fasıl 16, Bölüm IV’ün ilk faslıdır.  II. Kabukları içinde buharda pişirilmiş kabuklu hayvanlar 16.05’te yer alır.  III. Esası et olan hayvan yemi müstahzarları 16.02’de yer alır.  IV. Havyar benzerleri mersin balığı dışındaki balıkların yumurtalarından hazırlanır.",
      "I ve IV", ["I ve II", "II ve III", "I, II ve IV", "III ve IV"], "E", T_C,
      "Bölüm IV Fasıl 16 ile başlar (I doğru). Kabukları içinde buharda veya suda pişirilmiş kabuklular 03.06’dadır (II yanlış). Esası et, sakatat, balık vb. olan hayvan yemi müstahzarları 23.09’dadır (III yanlış). Havyar benzerleri mersin dışındaki balıkların yumurtalarından yapılır (IV doğru).",
      "Fasıl 16 Genel Açıklamalar; 16.04 ve 16.05 Açıklama Notları."),
    # 25
    q("Aynı karton kutuda birlikte sunulan bir kutu karides konservesi, bir kutu ciğer ezmesi, bir kutu peynir ve bir kutu dilimlenmiş domuz pastırmasının sınıflandırılmasında aşağıdakilerden hangisi doğrudur?",
      "Takım sayılmaz; her ürün kendi uygun pozisyonunda ayrı ayrı sınıflandırılır.",
      ["GYK 3(b) uyarınca takım olarak karides konservesinin pozisyonunda (16.05) sınıflandırılır.",
       "GYK 3(c) uyarınca numara sırasına göre sonuncu pozisyon olan 16.05’te sınıflandırılır.",
       "Tamamı et ve balık ürünü sayılarak Fasıl 16 Not 2 gereği 16.02’de sınıflandırılır.",
       "GYK 5(b) uyarınca karton kutu ile birlikte kutunun pozisyonunda sınıflandırılır."], "B", T_G,
      "GYK 3(b) açıklama notu bu bileşimi açıkça “takım oluşturmayan” örnek olarak verir: ürünler özel bir gereksinmeyi karşılamak veya belirli bir işlevi yerine getirmek üzere bir araya getirilmemiştir. Bu nedenle karides konservesi 16.05, ciğer ezmesi ve domuz pastırması 16.02, peynir 04.06’da ayrı ayrı sınıflandırılır.",
      "GYK 3(b) Açıklama Notu (X)."),
]

obj = {
    "tur": "fasil",
    "fasil": 16,
    "baslik": "Et, balık, kabuklu hayvanlar, yumuşakçalar veya diğer su omurgasızlarının veya böceklerin müstahzarları",
    "bolum": "IV",
    "oz": {
        "vurgu": "Fasıl 16’ya iki kapıdan girilir: (1) et, sakatat, kan, böcek, balık veya su omurgasızı Fasıl 2–3’te, Fasıl 4 Not 6’da veya 05.04’te sayılmayan bir işlem (pişirme, kaplama, baharatlama, sirke-yağda hazırlama, konserve, homojenize etme) görmüşse; (2) bir gıda müstahzarı ağırlıkça %20’den fazla bu ürünleri içeriyorsa. Pozisyonu ağırlıkça hakim hayvansal bileşen belirler.",
        "maddeler": [
            "%20 kuralının istisnaları: 19.02’deki doldurulmuş makarnalar, 21.03 soslar, 21.04 çorbalar-et suları ve homojenize bileşik gıda müstahzarları; et oranı ne olursa olsun kendi pozisyonlarında kalır.",
            "Ağırlık, satışa sunulduğu andaki et, balık vb. ağırlığıdır; üretimde kullanılan hammadde ağırlığı değildir.",
            "Pozisyonlar: sosis ve benzerleri 16.01; diğer et-sakatat-kan-böcek müstahzarları 16.02; hülasa ve sular 16.03; balık, havyar ve benzerleri 16.04; kabuklu, yumuşakça ve diğer su omurgasızları 16.05.",
            "Yenilebilir unlar Fasıl 16’da değildir: et 02.10, balık 03.09, böcek 04.10; yenmeyenler 05.11 / 23.01; yem müstahzarları 23.09.",
        ],
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Yalnız Fasıl 2–3 işlemlerini mi görmüş? (taze, soğutulmuş, dondurulmuş, tuzlanmış, salamura, kurutulmuş, tütsülenmiş*; böcekte Fasıl 4 Not 6; bağırsak-mide 05.04)", "Fasıl 2 / Fasıl 3 / <b>04.10</b> / <b>05.04</b>"],
            ["2", "Yenilebilir un veya kaba un mu?", "Et <b>02.10</b> · balık <b>03.09</b> · böcek <b>04.10</b>"],
            ["3", "Doldurulmuş makarna, sos ya da çorba, et suyu veya homojenize bileşik müstahzar mı?", "<b>19.02</b> / <b>21.03</b> / <b>21.04</b> (et oranı ne olursa olsun)"],
            ["4", "Gıda müstahzarında et, sakatat, kan, böcek, balık, su omurgasızı toplamı ağırlıkça %20 veya daha az mı?", "Fasıl 16 dışı (genellikle Fasıl 19–21)"],
            ["5", "Sosis, salam, sucuk veya benzeri ürün ya da esası bunlar olan müstahzar mı?", "<b>16.01</b>"],
            ["6", "Hülasa veya çiğden preslenmiş su mu?", "<b>16.03</b>"],
            ["7", "Ağırlıkça hakim bileşen et, sakatat, kan veya böcek mi?", "<b>16.02</b>"],
            ["8", "Ağırlıkça hakim bileşen balık mı; ya da havyar veya havyar benzeri mi?", "<b>16.04</b>"],
            ["9", "Ağırlıkça hakim bileşen kabuklu, yumuşakça veya diğer su omurgasızı mı?", "<b>16.05</b>"],
        ],
        "dipnot": "* Fasıl 3’te kalan pişmiş ürünler: tütsüleme öncesinde veya sırasında pişen tütsülü balık (03.05), kabuğu içinde buharda veya suda pişirilmiş kabuklu (03.06), kabuğunu açmak için ısı şoku görmüş yumuşakça (03.07).",
    },
    "pozisyon_haritasi": [
        ["16.01", "Sosisler ve benzerleri; esası bunlar olan müstahzarlar", "Kılıflı veya sosis şeklinde preslenmiş; çiğ, pişmiş, tütsülü", "Salam, sucuk, sosis, kanlı sucuk"],
        ["16.02", "Diğer hazırlanmış veya konserve et, sakatat, kan, böcek", "Pişmiş, kaplanmış, baharatlanmış, homojenize; hazır yemek", "Konserve kavurma, jambon, ciğer ezmesi, pişmiş böcek"],
        ["16.03", "Et, balık ve su omurgasızlarının hülasa ve suları", "Konsantre hülasa veya çiğden pres suyu", "Et hülasası, balık hülasası"],
        ["16.04", "Hazırlanmış veya konserve balıklar; havyar ve benzerleri", "Pişmiş, sirke-yağda, kaplanmış, ezme, sosis", "Ton konservesi, hamsi ezmesi, havyar"],
        ["16.05", "Hazırlanmış veya konserve kabuklu, yumuşakça, su omurgasızı", "Kabuk dışında pişirme, kaplama, sirke, konserve", "Karides konservesi, sirkede midye, pişmiş ahtapot"],
    ],
    "notlar": [
        ["Bölüm IV Not 1", "Bu bölümde “pellet” tabirinden, doğrudan doğruya sıkıştırma suretiyle veya ağırlığının <b>%3</b>’ünü geçmeyecek oranda bir bağlayıcı ilavesiyle küçük topaklar halinde bir araya getirilen ürünler anlaşılır."],
        ["Fasıl 16 Not 1", "Fasıl 2 veya 3’te, Fasıl 4 Not 6’da veya 05.04’te yazılı usullerle hazırlanmış veya konserve edilmiş et, sakatat, balık, kabuklu hayvanlar, yumuşakçalar, diğer su omurgasızları ve böcekler bu fasla girmez."],
        ["Fasıl 16 Not 2", "Gıda müstahzarları ağırlık itibariyle <b>%20’den fazla</b> sosis, et, sakatat, kan, böcek, balık, kabuklu hayvan, yumuşakça veya diğer su omurgasızı ya da bunların bileşimini içeriyorsa Fasıl 16’dadır. İki veya daha fazlasını içerenler ağırlıkça fazla olan bileşenin Fasıl 16’daki pozisyonunda sınıflandırılır. Bu hükümler 19.02’deki doldurulmuş ürünlere ve 21.03 veya 21.04 müstahzarlarına uygulanmaz."],
        ["Genel Açıklamalar", "Dikkate alınacak ağırlık, satışa sunulduğu andaki et, balık vb. ağırlığıdır; yapımdan önce kullanılan maddelerin ağırlığı değildir. Sebze, spagetti, sos vb. ile birlikte hazırlanan “hazır öğünler” de %20 şartıyla Fasıl 16’dadır."],
        ["Genel Açıklamalar", "Fasıl dışı: insan gıdası olarak elverişli et-sakatat unları (02.10), balık unları (03.09), böcek unları (04.10); yenmeyen unlar, kaba unlar ve pelletler (böcek 05.11; et, balık, su omurgasızı 23.01); hayvan yemi müstahzarları (23.09); ilaçlar (Fasıl 30)."],
        ["Fasıl 2 Genel Açıklamalar", "Fasıl 2’de kalan et: taze, soğutulmuş, dondurulmuş, tuzlanmış, salamura, kurutulmuş, tütsülenmiş; pişirilmemek şartıyla haşlanmış; enzimle yumuşatılmış, kıyılmış, hafifçe şeker serpilmiş. Pişirilmiş, hamur veya ekmek kırıntısıyla kaplanmış, biber ve tuzla baharatlanmış et ile ciğer ezmeleri 16.02’dedir."],
        ["Fasıl 4 Not 6", "04.10’daki böcekler: bütün veya parça halinde taze, soğutulmuş, dondurulmuş, kurutulmuş, tütsülenmiş, tuzlanmış veya salamura edilmiş yenilebilir cansız böcekler ile böceklerin yenilebilir un ve kaba unları. Başka şekilde hazırlananlar genellikle Bölüm IV’tedir."],
        ["16.01 Açıklama Notu", "Sosisler kılıf içinde ya da kılıfsız sosis şeklinde preslenmiş; çiğ veya pişmiş, tütsülenmiş, dilimlenmiş veya hava geçirmez kapta olabilir. Hariç: kıyılmadan kılıfa konmuş et (rulo jambon) genellikle 02.10 veya 16.02; katkısız kılıflı çiğ kıyma Fasıl 2; pişmiş rulo hindi eti 16.02."],
        ["16.03 Açıklama Notu", "Et hülasası: basınç altında haşlama veya buharlamayla alınan sıvının yağı ayrılıp konsantre edilmesiyle; et suyu çiğ etin preslenmesiyle elde edilir. Çorbalar, et suları ve müstahzarları (tablet veya küp dahil) 21.04; balık eriyikleri 23.09; peptonlar 35.04."],
        ["16.04 Açıklama Notu", "Havyar mersin balığı yumurtasından (2–4 mm), havyar benzerleri diğer balıkların yumurtalarından hazırlanır. Balık sosisleri, ezmeleri, marinadlar, pastörize veya sterilize balık buradadır. Tütsüleme sırasında pişmiş tütsülü balık 03.05; balıklı doldurulmuş makarna 19.02."],
        ["16.05 Açıklama Notu", "16.04’teki hazırlama şekilleri gerekli değişikliklerle uygulanır. Kabukları içinde buharda veya suda pişirilmiş kabuklular (03.06) ve kabuğunu açmak veya dengede tutmak için ısı şokuna maruz kalan yumuşakçalar (03.07) bu pozisyona girmez."],
    ],
    "sinir_komsulari": [
        ["Tuzlanmış, kurutulmuş veya tütsülenmiş (pişmemiş) et", "02.10", "Fasıl 2 işlemi"],
        ["Katkısız çiğ kıyma (kılıfa konmuş olsa da)", "Fasıl 2", "16.01 hariç tutması"],
        ["Kurutulmuş veya tuzlanmış yenilebilir böcek; böcek unu", "04.10", "Fasıl 4 Not 6"],
        ["Yenilebilir et unu; yenilebilir balık unu", "02.10 / 03.09", "Fasıl 16 Genel Açıklamalar"],
        ["Tütsüleme sırasında pişmiş balık", "03.05", "Fasıl 3 işlemi sayılır"],
        ["Kabuğu içinde buharda pişirilmiş karides", "03.06", "16.05 hariç tutması"],
        ["Isı şokuyla kabuğu açılmış midye", "03.07", "16.05 hariç tutması"],
        ["Pişmemiş işkembe, temizlenmiş bağırsak", "05.04", "Pişirilmiş işkembe ise Fasıl 16"],
        ["Etli veya karidesli doldurulmuş makarna (ravioli, mantı)", "19.02", "Fasıl 16 Not 2 istisnası"],
        ["Et veya balık içeren soslar ve çeşniler", "21.03", "Fasıl 16 Not 2 istisnası"],
        ["Çorbalar, et suları (tablet, küp); homojenize bileşik müstahzar", "21.04", "Fasıl 16 Not 2 istisnası"],
        ["Esası et veya balık olan yem müstahzarları; balık eriyikleri", "23.09", "Hayvan beslemek için"],
        ["Yenmeyen et-balık unları ve pelletler", "23.01", "İnsan tüketimine elverişsiz"],
        ["Peptonlar", "35.04", "16.03 hariç tutması"],
    ],
    "tuzaklar": [
        "<b>%20 eşiği satış anındaki ağırlıkla ölçülür.</b> Pişirme sonrası müstahzarda kalan et ağırlığı esastır; reçetedeki çiğ et ağırlığı değil.",
        "<b>%20’yi aşsa da Fasıl 16’ya girmeyenler.</b> Doldurulmuş makarna (19.02), soslar (21.03), çorbalar ve homojenize bileşik müstahzarlar (21.04).",
        "<b>Eşik toplam için aranır, pozisyonu çoğunluk belirler.</b> %12 tavuk + %15 karides = %27: Fasıl 16’dır ve karides ağır bastığı için 16.05’e gider.",
        "<b>Pişmişlik her zaman Fasıl 16 demek değildir.</b> Tütsülenirken pişen balık 03.05, kabuğunda haşlanan kabuklu 03.06, ısı şoku görmüş yumuşakça 03.07’de kalır.",
        "<b>Kaplamak veya tuz-biber eklemek yeter.</b> Ekmek kırıntısıyla kaplanmış çiğ balık filetosu 16.04; biber ve tuzla baharatlanmış çiğ et 16.02. Enzimle yumuşatma ise Fasıl 2’de bırakır.",
        "<b>Kılıf tek başına sosis yapmaz.</b> Kıyılmadan kılıfa konmuş et (rulo jambon) 02.10 veya 16.02; katkısız çiğ kıyma kılıfta da Fasıl 2. Kılıfsız ama sosis şeklinde preslenmiş ürün 16.01 olabilir.",
        "<b>Balık sosisi 16.01 değildir.</b> 16.01 et, sakatat, kan veya böcek sosisleri içindir; balık sosisleri 16.04’te sayılmıştır.",
        "<b>“Et suyu” iki farklı eşyadır.</b> Çiğ etin preslenmesiyle elde edilen et suyu 16.03; çorba niteliğindeki et suları (tablet, küp) 21.04.",
        "<b>Böcekte Fasıl 4 sınırı.</b> Kurutulmuş, tütsülenmiş, tuzlanmış böcek ve böcek unu 04.10; pişirilmiş veya başka şekilde hazırlanmış böcek 16.02; yenmeyen böcek 05.11.",
    ],
    "hafiza": {
        "kanca": "SOsis – ET – SUyu – BAlık – KAbuklu  (kapıda %20)",
        "aciklama": "16.01 <b>SO</b>sis · 16.02 <b>ET</b> (sakatat, kan, böcek dahil) · 16.03 <b>SU</b> ve hülasa · 16.04 <b>BA</b>lık ve havyar · 16.05 <b>KA</b>buklu, yumuşakça, su omurgasızı. Kapıdaki bekçi %20’dir; bekçinin üç “misafiri” her zaman dışarıda kalır: mantı (19.02), sos (21.03), çorba (21.04).",
    },
    "sinav_odagi": [
        "Fasıl 16 çoğunlukla Bölüm IV kapsamı, %20 kuralı ve GYK takım (set) sorularıyla birlikte sorulmuştur.",
        "Karidesli mantı (wonton) ile çorba tozundan oluşan dondurulmuş set: karides oranı %20’yi aşsa da doldurulmuş makarna 19.02’de kalır; karides müstahzarı ve çorba seçenekleri çeldiricidir; GYK 1, 2(b), 3(b) ve 6 birlikte uygulanır.",
        "Yenilebilir kurutulmuş ve tuzlanmış böceklerin (çekirge) 04.10’da kaldığı; 16.02 ve 05.11 seçeneklerinin çeldirici olarak kullanılması.",
        "Bölüm–fasıl–pozisyon numaralandırma mantığı: Bölüm IV’ün Fasıl 16 ile başladığı ve 16. fasılda beşinci pozisyonun kabuklu ve yumuşakça müstahzarlarına ayrıldığı.",
        "Et pozisyonları arasındaki geçişler (02.08, 02.10, 16.02) ile et suyunun 16.03 ve 21.04 arasındaki ayrımı.",
    ],
    "cikmis_ornekler": [
        {
            "soru": "Tarife Cetveline göre insan tüketimine uygun kurutulmuş ve tuzlanmış çekirge hangi tarife pozisyonundadır?",
            "secenekler": ["04.09", "04.10", "05.09", "05.11", "16.02"],
            "cevap": "B",
            "aciklama": "Fasıl 4 Not 6’ya göre kurutulmuş, tütsülenmiş, tuzlanmış veya salamura edilmiş yenilebilir cansız böcekler 04.10’dadır; Fasıl 16 Not 1 de bu usullerle hazırlanmış böcekleri fasıl dışında bırakır. Pişirilmiş veya başka şekilde hazırlanmış olsaydı 16.02’de yer alırdı.",
        },
        {
            "soru": "Tarife Cetveline göre ürün ve sınıflandırıldığı tarife pozisyonu ile ilgili aşağıdaki eşleştirmelerden hangisi yanlıştır?",
            "secenekler": ["Yumurta sarısı 04.08", "Buğday unu 11.01", "Kuskus 19.02", "Reçel 20.08", "Et suyu 21.04"],
            "cevap": "D",
            "aciklama": "Reçel 20.07’dedir. Çorba niteliğindeki et suları 21.04’te yer alır; Fasıl 16’daki 16.03 ise yalnız hülasaları ve çiğ etin preslenmesiyle elde edilen et suyunu kapsar.",
        },
    ],
    "ozet": [
        "İki kapı: Fasıl 2–3 dışı işlem veya müstahzarda %20’den fazla et, balık vb.",
        "%20 satış anındaki ağırlıkla, bileşenlerin toplamı üzerinden hesaplanır; pozisyonu ağırlıkça hakim bileşen belirler.",
        "İstisnalar: 19.02 doldurulmuş makarna, 21.03 sos, 21.04 çorba-et suyu-homojenize bileşik müstahzar.",
        "16.01 sosis · 16.02 et-sakatat-kan-böcek · 16.03 hülasa ve su · 16.04 balık-havyar · 16.05 kabuklu-yumuşakça.",
        "Fasıl 3’te kalan pişmişler: tütsüleme sırasında pişen balık, kabuğunda haşlanan kabuklu, ısı şoku görmüş yumuşakça.",
        "Yenilebilir unlar 02.10 / 03.09 / 04.10; yem müstahzarları 23.09. Bölüm IV notu: pellette bağlayıcı en fazla %3.",
    ],
    "sorular": sorular,
}

yaz(16, obj)
