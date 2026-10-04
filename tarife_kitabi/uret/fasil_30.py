#!/usr/bin/env python3
"""Fasıl 30 (Eczacılık ürünleri) modülünü üretir."""
import json
import os
from collections import Counter

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CIKTI = os.path.join(KITAP, "data", "fasil_30.json")

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
    # 1 — Eşya → pozisyon
    Q(T_ESYA,
      "Tarife Cetveline göre, son kullanma tarihi geçtiği için tasarlandığı amaçla kullanılamayan ve imha edilmek üzere toplanmış ampul halindeki antibiyotikler hangi pozisyonda sınıflandırılır?",
      "30.06", ["30.04", "30.03", "38.25", "30.02"], "B",
      "Fasıl 30 Not 4(k), raf ömrünün bitmesi gibi nedenlerle tasarlandığı amaç için kullanılamayan eczacılık ürünlerini 30.06’ya verir. Ürün dozlandırılmış olduğu için 30.04 akla gelir; ancak miadı dolmuş ilaç artık ilaç pozisyonunda değil, Not 4 listesindedir. 30.03 dökme karışık ilaçlar, 30.02 aşı ve serumlar içindir.",
      "Fasıl 30 Not 4(k); 30.06 Açıklama Notu (11)."),
    # 2
    Q(T_ESYA,
      "Tek dozluk flakonlarda, perakende satış ambalajında sunulan kızamık aşısı Tarife Cetvelinde hangi pozisyonda yer alır?",
      "30.02", ["30.04", "30.03", "30.06", "29.37"], "D",
      "Aşılar 30.02 pozisyonunda ismen sayılmıştır; bu pozisyondaki ürünler ölçülü dozlarda, perakende ambalajda veya dökme olsun olmasın burada kalır. “Dozlandırılmış veya perakende” ölçütü yalnız 30.03 ile 30.04 arasındaki ayrımda işler ve 30.04 metni 30.02 eşyasını açıkça hariç tutar. 29.37 hormonlar içindir.",
      "30.02 pozisyon metni ve Açıklama Notu; 30.04 pozisyon metni."),
    # 3
    Q(T_ESYA,
      "İç organların radyografik muayenesinde kullanılmak üzere ağızdan alınacak şekilde granül halde hazırlanmış, X ışınlarını geçirmeyen baryum sülfat esaslı müstahzar hangi pozisyonda sınıflandırılır?",
      "30.06", ["28.33", "25.11", "30.04", "38.22"], "E",
      "Radyografi muayeneleri için X ışınlarını geçirmeyen müstahzarlar Fasıl 30 Not 4(d) uyarınca 30.06’dadır; açıklama notu granül halde baryumu örnek verir. Baryum sülfatın kimyasal (28.33) veya tabii (25.11) hali müstahzar haline geldiğinde bu pozisyonlarda kalmaz. 38.22 hastaya uygulanmayan laboratuvar reaktifleri içindir.",
      "Fasıl 30 Not 4(d); 30.06 Açıklama Notu (5)."),
    # 4
    Q(T_ESYA,
      "İyot emdirilmiş, doğrudan kullanıcılara satılmak üzere perakende ambalajlanmış pamuk hangi pozisyonda sınıflandırılır?",
      "30.05", ["30.04", "30.06", "56.01", "33.07"], "A",
      "30.05; eczacılık maddeleri emdirilmiş veya kaplanmış ya da tıbbi amaçla perakende hazırlanmış pamukları, gazlı bezleri ve bandajları kapsar; açıklama notu iyot emdirilmiş pamuğu ismen sayar. 56.01 dokumaya elverişli vatkalar içindir; 30.04 ilaçlar, 30.06 Not 4 listesi, 33.07 kozmetik emdirilmiş vatka içindir.",
      "30.05 pozisyon metni ve Açıklama Notu."),
    # 5
    Q(T_ESYA,
      "Memeli hayvan dokularından elde edilen ve kan pıhtılaşmasını önleyici olarak kullanılan, dökme halde heparin sodyum tuzu hangi pozisyonda yer alır?",
      "30.01", ["30.02", "30.03", "35.07", "29.37"], "C",
      "Heparin ve tuzları 30.01 pozisyon metninde ismen sayılmıştır ve tesir dereceleri ne olursa olsun burada sınıflandırılır. Kandan elde edilmediği için 30.02’ye, enzim olmadığı için 35.07’ye, hormon olmadığı için 29.37’ye girmez; tek madde olduğundan 30.03 karışım şartı da yoktur.",
      "30.01 pozisyon metni ve Açıklama Notu (3)."),
    # 6 — Olumsuz teşhis
    Q(T_OLUMSUZ,
      "Aşağıdakilerden hangisi Tarife Cetvelinin 30. faslında <b>sınıflandırılmaz</b>?",
      "Tıbbi madde katılmış el sabunu",
      ["Cerrahide kullanılan steril emilebilir hemostatik jelatin sünger",
       "Damar yoluyla verilen beslenme müstahzarı",
       "Ultrason muayenesinde beden ile cihaz arasında kullanılan jel",
       "Ostomi kullanımına mahsus şekil verilerek kesilmiş kolostomi torbası"], "B",
      "Fasıl 30 Not 1, 34.01’de yer alan tıbbi madde içeren sabunları fasıl dışında bırakır. Hemostatik sünger, ultrason jeli ve ostomi torbası Not 4 uyarınca 30.06’dadır. Damar yoluyla beslenme müstahzarı, gıda istisnasının tek ayrığıdır ve Fasıl 30’da kalır.",
      "Fasıl 30 Not 1 ve Not 4; 30.03 Açıklama Notu."),
    # 7
    Q(T_OLUMSUZ,
      "Aşağıdakilerden hangisi 30.04 pozisyonunda <b>sınıflandırılmaz</b>?",
      "Tıbbi amaçla küçük şişelerde hazırlanmış kolloidal gümüş",
      ["Perakende ambalajlı, dozlandırılmış antibiyotik kapsül",
       "Nikotin içermeyen, ağrı kesici etken maddeli transdermal bant",
       "Kullanım bilgisi bulunan perakende paketlerdeki tıbbi sodyum bikarbonat",
       "Ölçülü dozlarda ilaç haline getirilmiş yılan zehri"], "D",
      "30.04 açıklama notuna göre 28.43 ila 28.46 ve 28.52 pozisyonlarındaki karışık olmayan ürünler dozlandırılmış veya ilaç olarak hazırlanmış olsalar da 30.04’e girmez; kolloidal gümüş 28.43’tedir. Transdermal bantlar 30.04 metninde sayılır, yılan zehri ilaç haline getirilince 30.01’den 30.04’e geçer.",
      "30.04 Açıklama Notu; 30.01 Açıklama Notu; Bölüm VI Not 1."),
    # 8
    Q(T_OLUMSUZ,
      "Aşağıdakilerden hangisi 30.02 pozisyonunda <b>yer almaz</b>?",
      "Mikrobik menşeli streptokinaz enzimi",
      ["Mühürlü ampullerde insan kanı",
       "Tedavi amacıyla hazırlanmış insan albümini",
       "Monoklonal antikorlar",
       "Sirke yapımında kullanılan asetik ferment kültürü"], "E",
      "30.02 açıklama notu, mikrobik menşeli olsalar bile streptokinaz ve streptodornaz gibi enzimleri hariç tutar ve 35.07’ye gönderir. İnsan kanı, tedavi amaçlı albümin, monoklonal antikorlar ve asetik ferment gibi mikroorganizma kültürleri 30.02’nin kapsamındadır.",
      "30.02 Açıklama Notu."),
    # 9
    Q(T_OLUMSUZ,
      "Aşağıdakilerden hangisi 30.06 pozisyonunda <b>sınıflandırılmaz</b>?",
      "Dişçilikte kullanılmak üzere kalsine edilmiş alçı",
      ["Steril cerrahi katgüt",
       "Diş kökü kanallarını doldurmaya mahsus guta-perka uçlar",
       "Esası hormon olan kimyasal gebelik önleyici müstahzar",
       "Tanınmış klinik deneyde kullanılacak ölçülü dozlarda plasebo"], "D",
      "Dişçilikte kullanılmak üzere özellikle kalsine edilmiş veya iyice öğütülmüş alçılar Fasıl 30 Not 1 uyarınca 25.20’dedir; alçı esaslı dişçilik müstahzarları ise 34.07’dedir. Diğer seçenekler Not 4’te sayılmıştır: steril katgüt (a), diş dolgu maddeleri (f), hormon esaslı gebelik önleyiciler (h), plasebolar (e).",
      "Fasıl 30 Not 1 ve Not 4; 30.06 Açıklama Notu (6)."),
    # 10 — Farklı / aynı
    Q(T_FARKLI,
      "Aşağıdakilerden hangisi diğerlerinden farklı bir tarife pozisyonunda sınıflandırılır?",
      "Eczacılık maddesi emdirilmiş yapışkan flaster",
      ["Az miktarda ilaç, sargı ve basit alet içeren ilk yardım kutusu",
       "Diş doldurmaya mahsus metal alaşımlı dolgu maddesi",
       "Cerrahide genişletici olarak kullanılan steril laminarya fitili",
       "X ışınlarını geçirmeyen kontrast müstahzarı"], "A",
      "İlaçlı yapışkan flasterler 30.05’te sayılan sargı ve benzeri maddelerdendir. İlk yardım kutusu, diş dolgu maddesi, steril laminarya fitili ve kontrast müstahzarı Fasıl 30 Not 4 listesinde yer aldığından 30.06’dadır.",
      "Fasıl 30 Not 4; 30.05 Açıklama Notu."),
    # 11
    Q(T_FARKLI,
      "Aşağıdakilerden hangisi diğerlerinden farklı bir fasılda yer alır?",
      "Tedavi edici doz içermeyen, şifalı olduğu iddia edilen bitkisel çay",
      ["Tek dozluk flakonlarda, perakende ambalajlı kızamık aşısı",
       "Mühürlü ampullerde sunulan insan kanı plazması",
       "Memeli hayvan dokularından elde edilmiş heparin",
       "Tıbbi amaçla kullanılan köpüren sağlık tuzu karışımı"], "E",
      "30.03 ve 30.04 açıklama notları, belirli bir hastalığa özgü aktif bileşenin tedavi edici dozunu içermeyen bitkisel infüzyon ve çayları 21.06’ya gönderir. Aşı ve plazma 30.02’de, heparin 30.01’de, sağlık tuzları 30.03’te (perakende ise 30.04) sayılır.",
      "30.03 ve 30.04 Açıklama Notları; Fasıl 30 Not 1."),
    # 12
    Q(T_FARKLI,
      "Aşağıdaki eşya çiftlerinden hangisinde her iki eşya da aynı tarife pozisyonunda yer alır?",
      "Tetanoz aşısı – Difteri antiserumu",
      ["Steril katgüt – Steril olmayan katgüt",
       "Dişçilikte kullanılan alçı – Dişçi çimentosu",
       "İlaçlı yara bandı – Transdermal ilaç bandı",
       "Dökme karışık ilaç – Aynı ilacın perakende tabletleri"], "A",
      "Aşılar ve antiserumlar birlikte 30.02’dedir. Steril katgüt 30.06, steril olmayanı 42.06; dişçilik alçısı 25.20, dişçi çimentosu 30.06; ilaçlı yara bandı 30.05, transdermal bant 30.04; dökme karışık ilaç 30.03, aynı ilacın dozlandırılmış hali 30.04’tür.",
      "30.02, 30.05, 30.06 Açıklama Notları; Fasıl 30 Not 1 ve Not 4."),
    # 13
    Q(T_FARKLI,
      "Aşağıdakilerden hangisi diğerlerinden farklı bir fasılda sınıflandırılır?",
      "Parfümlü banyo tuzu",
      ["Tıbbi banyolar için hazırlanmış iyotlu karışık tuzlar",
       "Kâfurlu yağ",
       "Anti-astmatik kağıtlar",
       "Veterinerlik cerrahisinde kullanılan anestezikler"], "C",
      "Parfümlü banyo tuzları 33.07’de yer alır. Tıbbi banyolar için hazırlanmış karışık tuzlar, kâfurlu yağ, anti-astmatik kağıtlar ve anestezikler 30.03 açıklama notunda sayılan ilaçlardır; dozlandırılmış veya perakende iseler 30.04’e geçer, ama her durumda Fasıl 30’dadır. Tuzak, “banyo tuzu” kelimesini tek başına yeterli görmektir.",
      "30.03 Açıklama Notu; Fasıl 30 Not 1; 33.07 pozisyon metni."),
    # 14 — Not / tanım
    Q(T_NOT,
      "Fasıl 30 Not 3’e göre, 30.03 ve 30.04 pozisyonlarının uygulanmasında aşağıdakilerden hangisi “karışım halinde bulunan ürün” sayılır?",
      "Tabii mineral suların buharlaştırılmasından elde edilen tuzlar",
      ["Karışım halinde olmayan bir ürünün sulu çözeltisi",
       "Fasıl 29’da yer alan bir organik bileşik",
       "13.02’de yer alan, sadece standardize edilmiş basit bitkisel hülasa",
       "Fasıl 28’de yer alan bir inorganik bileşik"], "E",
      "Not 3(b), kolloidal çözeltileri (kolloidal kükürt hariç), bitki karışımlarının işlenmesinden elde edilen hülasaları ve tabii mineral suların buharlaştırılmasından elde edilen tuzları karışım sayar. Not 3(a) ise sulu çözeltileri, Fasıl 28 ve 29 ürünlerini ve sadece standardize edilmiş 13.02 basit hülasalarını karışım olmayan ürün kabul eder.",
      "Fasıl 30 Not 3."),
    # 15
    Q(T_NOT,
      "Fasıl 30 Not 2’ye göre, 30.02 pozisyonu anlamında “bağışıklık sağlayan ürünler” tabiri ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
      "Bağışıklık süreçlerini doğrudan düzenleyen peptit ve proteinleri (29.37 hariç) kapsar.",
      ["Yalnızca biyoteknolojik yöntemle elde edilmiş veya modifiye edilmiş ürünleri kapsar.",
       "Monoklonal antikorları kapsar; interferonları ve interlökinleri kapsamaz.",
       "29.37 pozisyonundaki hormonları ve bunların türevlerini de kapsar.",
       "Dozlandırılmış veya perakende ambalajlı olanlar 30.04’te sınıflandırılır."], "A",
      "Not 2, monoklonal antikorlar, antikor parçaları, interlökinler, interferonlar, TNF, büyüme faktörleri ve CSF gibi bağışıklık süreçlerinin düzenlenmesine doğrudan katılan peptit ve proteinleri sayar ve 29.37’dekileri hariç tutar. Pozisyon metni “biyoteknolojik işlemle elde edilmiş olsun olmasın” der; açıklama notu ölçülü doz veya perakende ambalajın sınıflandırmayı değiştirmediğini belirtir.",
      "Fasıl 30 Not 2; 30.02 pozisyon metni ve Açıklama Notu."),
    # 16
    Q(T_NOT,
      "30.04 Açıklama Notuna göre, enjekte edilebilen tıbbi solüsyonların hazırlanmasında çözücü olarak kullanılan tekrar distile edilmiş su, hangi hacimdeki ampullerde bulunduğunda dozlandırılmış ilaç sayılır?",
      "1,25 ila 10 cm3",
      ["0,5 ila 5 cm3", "10 ila 50 cm3", "2,5 ila 12,5 cm3", "5 ila 25 cm3"], "C",
      "30.04 açıklama notu, dozlandırılmış ilaç örnekleri arasında enjekte edilebilen solüsyonların hazırlanmasında çözücü olarak kullanılan 1,25 ila 10 cm3’lük ampullerdeki tekrar distile edilmiş suyu sayar. Diğer hacim aralıkları notta geçmez; eşik değerin sınırları ezberlenmelidir.",
      "30.04 Açıklama Notu (a)."),
    # 17
    Q(T_NOT,
      "30.04 Açıklama Notuna göre boğaz pastilleri ve öksürük şekerleri ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
      "Esası şeker ve tat-koku verici olan pastiller, mentol içerse de 17.04’tedir.",
      ["Tüm boğaz pastilleri dozlandırılmış sayıldığından her durumda 30.04’tedir.",
       "Mentol içeren her pastil karışım sayıldığı için dökme halde 30.03’tedir.",
       "Tıbbi madde içeren pastiller ambalajına bakılmaksızın 21.06’dadır.",
       "Esası şeker olan pastiller Fasıl 30 Not 4 uyarınca 30.06’dadır."], "B",
      "Açıklama notu, esası şeker olan ve tat-koku verici maddelerden (mentol, ökaliptol, tolu balzamı gibi tıbbi özellikli olanlar dahil) oluşan boğaz pastillerini 17.04’e verir. Tat ve koku vericiler dışında tıbbi madde içeren pastiller ise, her pastildeki oran tedavi veya korunmaya yetiyor ve ürün dozlandırılmış ya da perakende ambalajlıysa 30.04’tedir.",
      "30.04 Açıklama Notu."),
    # 18 — GYK
    Q(T_GYK,
      "Kutu içinde sunulan; az miktarda oksijenli su ve tentürdiyot, birkaç sargı bezi ve flaster ile bir makas ve pensten oluşan ilk yardım seti hangi Genel Yorum Kurallarına göre sınıflandırılır?",
      "GYK 1 ve 6 (Fasıl 30 Not 4 uyarınca 30.06)",
      ["GYK 3(b) ve 6 (esas karakteri veren ilaçlara göre 30.04)",
       "GYK 3(c) ve 6 (numara sırasına göre en son pozisyon)",
       "GYK 2(a) ve 6 (tamamlanmamış eşya olarak 30.05)",
       "GYK 4 ve 6 (en çok benzeyen eşyanın pozisyonu)"], "A",
      "İlk yardım kutuları ve setleri Fasıl 30 Not 4(g) ile 30.06’da ismen sayıldığından sınıflandırma doğrudan pozisyon metni ve fasıl notuyla, yani GYK 1 ile yapılır; alt pozisyon için GYK 6 uygulanır. GYK 1 açıklama notu da 30. Faslın 4 nolu notuna göre sınıflandırılan eczacılık eşyasını örnek verir. Set görünümü 3(b)’yi çağrıştırsa da notun açık hükmü önce gelir.",
      "GYK 1 Açıklama Notu; Fasıl 30 Not 4(g)."),
    # 19
    Q(T_GYK,
      "Ayrı kaplarda toz ve sıvıdan oluşan, kullanım anında birbirine karıştırılarak diş dolgusu elde edilecek şekilde aynı ambalajda birlikte sunulan ve birbirini tamamlayan ürünler nasıl sınıflandırılır?",
      "Bölüm VI Not 3 ile diş dolgusu olarak 30.06’da (GYK 1 ve 6)",
      ["Her bileşen ayrı ayrı kendi pozisyonunda (GYK 1 ve 6)",
       "GYK 3(b) uyarınca esas karakteri veren toza göre Fasıl 28’de",
       "GYK 3(c) uyarınca numara sırasına göre en son pozisyonda",
       "GYK 2(b) uyarınca karışık ilaç olarak dökme halde 30.03’te"], "C",
      "Bölüm VI Not 3, birlikte karıştırılması tasarlanan, birlikte sunulan ve birbirini tamamlayan bileşenlerden oluşan setleri elde edilecek ürünün pozisyonunda sınıflandırır; bölüm açıklama notu 30.06’daki dişçilik dolgularını örnek verir. Bölüm notu GYK 1 kapsamında uygulandığından 3(b) veya 3(c)’ye geçilmez; bileşenler de ayrı ayrı sınıflandırılmaz.",
      "Bölüm VI Not 3; Fasıl 30 Not 4(f); 30.06 Açıklama Notu (6)."),
    # 20 — Eşleştirme / boşluk
    Q(T_ESL,
      "Tedavide veya korunmada kullanılmak üzere birbirleriyle karıştırılmış iki veya daha fazla unsurdan oluşan ilaçlar dozlandırılmamış ve perakende ambalajlanmamış ise ……… pozisyonunda; dozlandırılmış veya perakende satış ambalajında ise ……… pozisyonunda sınıflandırılır. Boşluklara sırasıyla hangisi gelmelidir?",
      "30.03 – 30.04",
      ["30.04 – 30.03", "30.03 – 30.06", "30.02 – 30.04", "30.04 – 30.05"], "B",
      "30.03 karışık ve dökme ilaçları, 30.04 ise karışık olsun olmasın dozlandırılmış veya perakende ambalajlı ilaçları kapsar. Ters sıralama (30.04 – 30.03) en sık yapılan hatadır. 30.02, 30.05 ve 30.06’daki eşya her iki pozisyonun metninde hariç tutulmuştur.",
      "30.03 ve 30.04 pozisyon metinleri ve Açıklama Notları."),
    # 21
    Q(T_ESL,
      "Aşağıdaki eşya – pozisyon eşleştirmelerinden hangisi <b>yanlıştır</b>?",
      "Sigarayı bırakmaya yardımcı nikotinli ciklet – 30.04",
      ["Hijyenik havlular (pedler) ve tamponlar – 96.19",
       "Tıbbi madde katılmış kalıp halinde sabun – 34.01",
       "Perakende ambalajlı kontak lens solüsyonu – 33.07",
       "Steril olmayan laminarya çubukları – 12.12"], "C",
      "Fasıl 30 Not 1, nikotin içeren ve sigarayı bırakmaya yardımcı tablet, ciklet ve bantları (transdermal sistemler) 24.04’e gönderir; dozlandırılmış olmaları sonucu değiştirmez. Hijyenik pedler 96.19, tıbbi sabun 34.01, kontak lens solüsyonu 33.07, steril olmayan laminarya 12.12’dedir.",
      "Fasıl 30 Not 1; 30.04, 30.05 ve 30.06 Açıklama Notları."),
    # 22 — Çoktan-çoğa
    Q(T_COK,
      "Aşağıdakilerden hangileri 30.06 pozisyonunda sınıflandırılır? I. Prostetik implantı mevcut kemiğe bağlamakta kullanılan, sertleştirici ve aktifleştirici içeren kemik çimentosu II. Steril olmayan cerrahi dikiş ipliği III. Ultrason taramasında beden ile cihaz arasında birleştirme vasıtası olarak kullanılan jel IV. Doktorların kullandığı türden teferruatlı tıbbi takım çantası",
      "I ve III",
      ["I ve II", "II ve IV", "I, III ve IV", "III ve IV"], "D",
      "Kemiklerin tedavisinde kullanılan çimentolar Not 4(f), birleştirme vasıtası jeller Not 4(ij) ile 30.06’dadır. Steril olmayan dikiş malzemeleri tabiatlarına göre (katgüt 42.06, iplikler Bölüm XI) sınıflandırılır. Açıklama notu, doktorların kullandığı daha teferruatlı tıbbi takım çantalarını ilk yardım kutusu kapsamından çıkarır.",
      "Fasıl 30 Not 4; 30.06 Açıklama Notu."),
    # 23
    Q(T_COK,
      "Fasıl 30 ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Pegile ürünler, pegile edilmemiş şekilleriyle aynı pozisyonda sınıflandırılır. II. Damar yoluyla verilen beslenme müstahzarları gıda sayıldığından Bölüm IV’tedir. III. 30.02’deki ürünler dozlandırılmış veya perakende ambalajlı olsalar da 30.02’de kalır. IV. Belirli bir hastalığa özgü aktif bileşenin tedavi edici dozunu içermeyen bitkisel çay karışımları 21.06’dadır.",
      "I, III ve IV",
      ["I ve II", "II ve IV", "I, II ve III", "II, III ve IV"], "E",
      "Genel açıklamalar pegile ürünlerin pegile edilmemiş halleriyle aynı pozisyonda olduğunu (I), 30.02 açıklama notu doz ve ambalajın önemsiz olduğunu (III), 30.04 açıklama notu bu tür bitkisel çayların 21.06’da olduğunu (IV) belirtir. Not 1(a) ise damardan alınan beslenme müstahzarlarını gıda istisnasının dışında tutar; bunlar Fasıl 30’dadır (II yanlış).",
      "Fasıl 30 Genel Açıklamalar; Not 1(a); 30.02 ve 30.04 Açıklama Notları."),
    # 24 — Senaryo
    Q(T_SEN,
      "Bir firma büyük varillerde dökme olarak; sodyum hidrojenkarbonat, tartarik asit, magnezyum sülfat ve şekerden oluşan, tıbbi amaçla kullanılan köpüren sağlık tuzu karışımı ithal etmektedir. Ürün dozlandırılmamış ve perakende satış ambalajına konulmamıştır. Eşya hangi pozisyonda sınıflandırılır?",
      "30.03",
      ["28.36", "30.04", "21.06", "25.01"], "B",
      "30.03 açıklama notu sağlık tuzlarını (sodyum hidrojenkarbonat, tartarik asit, magnezyum sülfat ve şeker karışımı) ve benzeri köpüren tuz karışımlarını ismen sayar. Ürün karışım olduğundan tek kimyasal bileşik pozisyonuna (28.36) girmez; dozlandırılmamış ve perakende olmadığından 30.04 de uygulanmaz. Tıbbi amaç onu gıda müstahzarından (21.06) ayırır.",
      "30.03 pozisyon metni ve Açıklama Notu."),
    # 25
    Q(T_SEN,
      "Domuz derisi dokusundan dondurularak kurutulmuş (liyofilize) şeritler halinde hazırlanan, açık yaralarda ve deri kaybı olan alanlarda geçici biyolojik kapatma olarak kullanılan, kullanım bilgilerini içeren etiketli steril kaplarda perakende ambalajlanmış deri sargıları hangi pozisyonda sınıflandırılır?",
      "30.05",
      ["30.01", "30.06", "30.04", "05.11"], "D",
      "30.05 açıklama notu, hayvan deri dokusundan (çoğunlukla domuz derisinden) dondurulmuş veya liyofilize şeritler halinde hazırlanan ve steril perakende kaplarda sunulan deri sargılarını bu pozisyona dahil eder. 30.01’deki hayvansal dokular daimi yerleştirme veya implantasyon içindir; ürün ilaç olmadığından 30.04’e, Not 4 listesinde olmadığından 30.06’ya girmez.",
      "30.05 Açıklama Notu; 30.01 Açıklama Notu."),
]

modul = {
    "tur": "fasil",
    "fasil": 30,
    "baslik": "Eczacılık ürünleri",
    "bolum": "VI",
    "oz": {
        "vurgu": "Fasıl 30 önce eşyanın tedavi, korunma veya (bazı ürünlerde) teşhis için hazırlanıp hazırlanmadığını sorar. Ardından özel pozisyonlara bakılır: kan, serum ve aşılar 30.02, sargılar 30.05, Not 4 listesi 30.06. Kalan ilaçlarda tek soru vardır: karışık ve dökme ise 30.03, dozlandırılmış veya perakende ambalajlı ise 30.04.",
        "maddeler": [
            "Gıdalar, gıda takviyeleri, tonik içecekler ve maden suları Fasıl 30 dışındadır (Bölüm IV); tek istisna damardan alınan beslenme müstahzarlarıdır.",
            "33.03–33.07 müstahzarları, tıbbi sabunlar (34.01), nikotinli sigara bırakma ürünleri (24.04) ve 38.22 teşhis reaktifleri tedavi edici özellikleri olsa da bu fasla girmez.",
            "30.02’deki ürünler ve 30.06’daki Not 4 eşyası, doz ve ambalaj ne olursa olsun kendi pozisyonlarında kalır.",
            "Karışım olmayan dökme madde (Fasıl 28–29 ürünleri, standardize 13.02 hülasaları) ilaç pozisyonuna ancak dozlandırılınca veya perakende ambalajlanınca (30.04) girer.",
        ],
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Gıda, gıda takviyesi, tonik içecek veya maden suyu mu? (damardan beslenme hariç)", "Bölüm IV (çoğunlukla <b>21.06</b> veya Fasıl 22)"],
            ["2", "Kozmetik, tıbbi sabun, nikotinli sigara bırakma ürünü veya hastaya uygulanmayan teşhis reaktifi mi?", "<b>33.03–33.07</b> · <b>34.01</b> · <b>24.04</b> · <b>38.22</b>"],
            ["3", "Not 4 listesinde mi? (steril katgüt, kontrast madde, diş dolgusu, ilk yardım kutusu, gebelik önleyici, tıbbi jel, miadı dolmuş ilaç, ostomi aleti, plasebo)", "<b>30.06</b>"],
            ["4", "İnsan kanı, tedavi/teşhis amaçlı hayvan kanı, antiserum, bağışıklık ürünü, aşı, toksin, mikroorganizma veya hücre kültürü mü?", "<b>30.02</b> (doz ve ambalaj önemsiz)"],
            ["5", "Eczacılık maddesi emdirilmiş veya tıbbi amaçla perakende hazırlanmış pamuk, gazlı bez, bandaj, plaster mi?", "<b>30.05</b>"],
            ["6", "Tedavide kullanılan kurutulmuş gudde/organ, organ hülasası, heparin, ilaç haline getirilmemiş zehir mi?", "<b>30.01</b>"],
            ["7", "İlaç dozlandırılmış veya perakende ambalajlı mı? (transdermal sistemler dahil)", "<b>30.04</b>"],
            ["8", "İlaç karışık ve dökme mi?", "<b>30.03</b>"],
            ["9", "Karışım olmayan dökme madde mi?*", "Kendi faslı (28, 29, 13.02 vb.)"],
        ],
        "dipnot": "* Not 3: Fasıl 28–29 ürünleri, karışım olmayan ürünlerin sulu çözeltileri ve sadece standardize edilmiş veya çözücüde çözülmüş 13.02 basit hülasaları “karışım olmayan” sayılır. 28.43–28.46 ve 28.52 ürünleri (ör. kolloidal gümüş) dozlandırılmış olsa bile 30.04’e girmez.",
    },
    "pozisyon_haritasi": [
        ["30.01", "Kurutulmuş gudde ve organlar; hülasaları; heparin; diğer insan/hayvan menşeli maddeler", "Tedavi amacı; kurutulmuş (taze, dondurulmuş Fasıl 2 veya 5)", "Pankreas tozu, safra hülasası, heparin, arı zehri, implant için steril kemik"],
        ["30.02", "İnsan kanı; antiserum, kan fraksiyonları, bağışıklık ürünleri; aşılar, toksinler, kültürler", "Doz ve ambalaj önemsiz; mayalar hariç", "Kızamık aşısı, plazma, monoklonal antikor, laktik ferment kültürü"],
        ["30.03", "Karışık ilaçlar (dozlandırılmamış, perakende değil)", "İki veya daha fazla unsur; dökme", "Varilde merhem, dökme sağlık tuzu, kâfurlu yağ"],
        ["30.04", "İlaçlar (karışık olsun olmasın), dozlandırılmış veya perakende", "Tablet, kapsül, ampul, transdermal bant; kullanım bilgisi", "Antibiyotik kapsül, ağrı kesici bant, perakende tıbbi sodyum bikarbonat"],
        ["30.05", "İlaç emdirilmiş veya tıbbi perakende pamuk, gazlı bez, bandaj, plaster", "Emdirme/kaplama veya tıbbi perakende ambalaj", "İyotlu pamuk, ilaçlı flaster, hardal yakısı, sprey sıvı sargı"],
        ["30.06", "Not 4’te sayılan eczacılık eşyası", "Kapalı liste", "Steril katgüt, baryumlu kontrast, diş dolgusu, ilk yardım kutusu, miadı dolmuş ilaç"],
    ],
    "notlar": [
        ["Fasıl 30 Not 1", "Fasıl dışı: (a) gıdalar ve içecekler (dietetik, diabetik, zenginleştirilmiş gıdalar, gıda takviyeleri, tonikler, maden suları; Bölüm IV) – damardan alınan beslenme müstahzarları hariç; (b) nikotin içeren, sigarayı bırakmaya yardımcı tablet, ciklet, bant (24.04); (c) dişçilik için kalsine edilmiş veya iyice öğütülmüş alçılar (25.20); (d) tıpta kullanılan uçucu yağların sulu distilat ve çözeltileri (33.01); (e) 33.03–33.07 müstahzarları (tedavi edici özellikleri olsa bile); (f) tıbbi madde içeren sabunlar (34.01); (g) alçı esaslı dişçilik müstahzarları (34.07); (h) tedavi için hazırlanmamış kan albümini (35.02); (ij) 38.22 teşhis reaktifleri."],
        ["Fasıl 30 Not 2", "30.02’deki “bağışıklık sağlayan ürünler”: bağışıklık süreçlerinin düzenlenmesine doğrudan katılan peptit ve proteinler (29.37’dekiler hariç) – monoklonal antikorlar, antikor parçaları, konjugatlar, interlökinler, interferonlar, kemokinler, TNF, büyüme faktörleri, hematopoietinler, CSF."],
        ["Fasıl 30 Not 3", "30.03, 30.04 ve Not 4(d) için <b>karışım olmayan</b>: karışım olmayan ürünlerin sulu çözeltileri, Fasıl 28 ve 29 ürünleri, sadece standardize edilmiş veya çözücüde çözülmüş 13.02 basit bitkisel hülasaları. <b>Karışım</b>: kolloidal çözelti ve süspansiyonlar (kolloidal kükürt hariç), bitki karışımlarından elde edilen hülasalar, tabii mineral suların buharlaştırılmasından elde edilen tuz ve konsantreler."],
        ["Fasıl 30 Not 4", "30.06 <b>sadece</b> şunları kapsar: (a) steril katgüt, steril dikiş malzemeleri, steril doku yapıştırıcıları; (b) steril laminarya ve fitilleri; (c) steril emilebilir hemostatikler, steril yapışmayı önleyiciler; (d) X ışını kontrast müstahzarları ve hastaya uygulanan teşhis reaktifleri; (e) tanınmış klinik deneyler için ölçülü dozlarda plasebolar ve kör klinik deney kitleri; (f) dişçi çimentoları, diş dolguları, kemik çimentoları; (g) ilk yardım kutuları ve setleri; (h) hormon, 29.37 ürünü veya spermisit esaslı gebelik önleyiciler; (ij) yağlayıcı veya birleştirme vasıtası tıbbi jeller; (k) raf ömrü bitmiş vb. eczacılık ürünleri; (l) ostomi kullanımına mahsus torba ve aletler."],
        ["Bölüm VI Not 2", "Ölçülü dozlarda veya perakende satış için hazırlanmış olmaları nedeniyle 30.04, 30.05 veya 30.06’ya giren ürünler, başka bir pozisyona da girebilseler bu pozisyonlarda kalır (Bölüm VI Not 1 saklıdır: 28.43–28.46, 28.52 önceliklidir)."],
        ["Genel Açıklamalar", "Pegile ürünler (PEG polimerlerine bağlanmış eczacılık ürünleri) pegile edilmemiş halleriyle aynı pozisyonda sınıflandırılır (ör. peginterferon 30.02)."],
        ["30.02 Açıklama Notu", "Tedavi, korunma veya teşhis için hazırlanmamış hayvan kanı 05.11; tedavi için hazırlanmamış kan albümini 35.02, globulinler 35.04; enzimler (mikrobik menşeli olsa da) 35.07; canlı olmayan tek hücreli mikroorganizmalar (aşılar hariç) 21.02. Bu pozisyondaki ürünler doz ve ambalajdan bağımsız olarak burada kalır."],
        ["30.03 Açıklama Notu", "Tek ecza maddesi + dolgu, tatlandırıcı, destekleyici madde karışımları da ilaçtır. Kolloidal kükürt dozlandırılmış/perakende ise 30.04, diğer hallerde 28.02; sade kolloidal kıymetli metaller her durumda 28.43. Sivilce müstahzarları yeterli aktif madde içermiyorsa 33.04."],
        ["30.04 Açıklama Notu", "Perakende ambalaj, kullanım bilgisi (hastalık, kullanma yöntemi, doz) ile belli olur; yalnız saflık bilgisi yetmez. Gıda takviyeleri 21.06 veya Fasıl 22; esası şeker olan boğaz pastilleri 17.04. Gıda yalnız taşıyıcı veya tatlandırıcı ise ürün ilaç kalır."],
        ["30.05 Açıklama Notu", "İlaç emdirilmemiş pamuk ve gazlı bez de tıbbi amaçla perakende hazırlanmışsa buradadır. Perakende hazırlanmamış alçılı kırık bandajları, transdermal ilaçlar (30.04), Not 4 eşyası (30.06) ve hijyenik ped/tamponlar (96.19) hariçtir."],
        ["30.06 Açıklama Notu", "Steril olmayan katgüt 42.06, steril olmayan laminarya 12.12; hastaya uygulanmayan teşhis reaktifleri yapıldıkları maddeye göre (Fasıl 28, 29, 30.02 veya 38.22). İlk yardım kutusu kapsamı doktorların kullandığı teferruatlı takım çantalarını içermez."],
    ],
    "sinir_komsulari": [
        ["Tedavi amacıyla hazırlanmamış hayvan kanı; safra", "05.11 / 05.10", "Fasıl 5 ham hayvansal ürünleri"],
        ["Vitamin-mineral gıda takviyesi; şifalı olduğu iddia edilen bitkisel çay", "21.06", "Fasıl 30 Not 1(a); 30.04 Açıklama Notu"],
        ["Esası şeker olan mentollü boğaz pastili", "17.04", "Tat-koku verici esaslı şekerleme"],
        ["Nikotinli sigara bırakma bandı veya cikleti", "24.04", "Fasıl 30 Not 1(b)"],
        ["Dişçilik alçısı; alçı esaslı dişçilik müstahzarı", "25.20 / 34.07", "Fasıl 30 Not 1(c), (g)"],
        ["Kolloidal gümüş (dozlandırılmış olsa da)", "28.43", "Bölüm VI Not 1; 30.04 Açıklama Notu"],
        ["Dökme vitamin; izole hormon", "29.36 / 29.37", "Karışım olmayan Fasıl 29 ürünü"],
        ["Uçucu yağların sulu çözeltileri ve damıtık suları", "33.01", "Fasıl 30 Not 1(d)"],
        ["Yeterli aktif madde içermeyen sivilce müstahzarı; kontak lens solüsyonu", "33.04 / 33.07", "Fasıl 30 Not 1(e)"],
        ["Tıbbi sabun", "34.01", "Fasıl 30 Not 1(f)"],
        ["Tedavi için hazırlanmamış kan albümini; enzimler", "35.02 / 35.07", "Not 1(h); 30.02 Açıklama Notu"],
        ["Hastaya uygulanmayan laboratuvar teşhis reaktifi", "38.22", "Fasıl 30 Not 1(ij)"],
        ["İlaç olarak hazırlanmamış dezenfektan, haşere öldürücü", "38.08", "30.03 ve 30.04 Açıklama Notları"],
        ["Steril olmayan katgüt; steril olmayan laminarya", "42.06 / 12.12", "Steril olma şartı (Not 4)"],
        ["Hijyenik ped, tampon, bebek bezi", "96.19", "30.05 Açıklama Notu"],
    ],
    "tuzaklar": [
        "<b>Doz ve perakende ambalaj 30.03’ü 30.04’e çevirir, 30.02’yi çevirmez.</b> Aşılar, serumlar ve antikorlar ambalajları ne olursa olsun 30.02’de kalır.",
        "<b>Karışım olmayan dökme madde ilaç pozisyonuna girmez.</b> Fasıl 28–29 ürünleri ve standardize 13.02 hülasaları dökme haldeyken kendi fasıllarında, dozlandırılınca 30.04’te sınıflandırılır.",
        "<b>Tedavi edici özellik kozmetiği ilaç yapmaz.</b> 33.03–33.07 müstahzarları ve tıbbi sabunlar (34.01) Fasıl 30 dışıdır; yeterli aktif madde içermeyen sivilce müstahzarı 33.04’tedir.",
        "<b>Üç bant, üç pozisyon.</b> Nikotinli sigara bırakma bandı 24.04; diğer transdermal ilaç bantları 30.04; ilaçlı yapışkan flaster 30.05.",
        "<b>Gıda takviyesi ilaç değildir.</b> Vitamin-mineral takviyeleri 21.06 veya Fasıl 22’dedir; gıda yalnız taşıyıcı veya tatlandırıcı ise ürün ilaç olarak kalır. Damardan beslenme müstahzarı ise Fasıl 30’dadır.",
        "<b>Miadı dolmuş ilaç 30.06’dır.</b> Raf ömrü bittiği için kullanılamayan eczacılık ürünleri artık 30.04’te değil, Not 4(k) ile 30.06’dadır.",
        "<b>Teşhis reaktifinde ölçüt hastaya uygulanmasıdır.</b> Ağızdan veya enjeksiyonla hastaya verilen reaktif ve kontrast madde 30.06; numune üzerinde kullanılan laboratuvar reaktifi 38.22 (veya Fasıl 28, 29, 30.02).",
        "<b>Steril olmayan Fasıl 30’a girmez.</b> Steril olmayan katgüt 42.06, steril olmayan laminarya 12.12’dedir.",
        "<b>Kan albümini amaca bakar.</b> Tedavi veya korunma için hazırlanmışsa 30.02, değilse 35.02. Hayvan kanı da tedavi veya teşhis için hazırlanmamışsa 05.11’dedir.",
        "<b>Kolloidal gümüş ilaç ambalajında da 28.43’tür.</b> Bölüm VI Not 1 ile 28.43–28.46 ve 28.52 ürünleri bölümün diğer pozisyonlarına göre önceliklidir.",
    ],
    "hafiza": {
        "kanca": "ORGAN – KAN – VARİL – KUTU – SARGI – LİSTE",
        "aciklama": "<b>ORGAN</b> 30.01 · <b>KAN</b> ve aşı 30.02 · <b>VARİL</b>deki karışık dökme ilaç 30.03 · <b>KUTU</b>daki dozlu/perakende ilaç 30.04 · <b>SARGI</b> 30.05 · Not 4 <b>LİSTE</b>si 30.06. Görsel benzetme: hastanede koridor boyunca yürüyün; önce organ laboratuvarı, sonra kan ve aşı dolabı, ecza deposunda varil ve kutular, pansuman odasında sargılar, kapıda acil çantası ve imha kutusu.",
    },
    "sinav_odagi": [
        "“Hangisi 30. fasılda yer almaz?” kalıbında Not 1 hariç tutmaları: sigarayı bırakmaya yardımcı nikotinli bant, tedavi amacıyla hazırlanmamış kan albümini, tıbbi madde içeren sabun, akne azaltan yüz bakım müstahzarı, dökme vitamin.",
        "Fasılda yer alan eşyanın çeldiriciler arasından tanınması: insan kanı, kızamık aşısı, serum, gaz bezi, perakende hazırlanmış alçılı sargı bezi.",
        "Not 4 listesinin (30.06) doğrudan sorulması: ilk yardım kutusu, kullanım süresi bitmiş hazır ilaçlar; 30.04 ve 38.25 çeldiricileri.",
        "İlk yardım kutusunun hangi GYK ile sınıflandırıldığı: fasıl notunda ismen sayıldığı için GYK 1 ve 6; 3(b) ve 3(c) çeldirici.",
        "Dişçilikte kullanılan alçının 25.20’de olduğu; 30.06, 68.09 ve 90.21 çeldirici olarak kullanılmıştır.",
        "“Aynı fasıl” sorularında mikroorganizma kültürü, ilk yardım çantası ve steril dikiş malzemesinin birlikte Fasıl 30’da olduğu.",
    ],
    "cikmis_ornekler": [
        {
            "soru": "Tarife Cetveline göre aşağıdakilerden hangisi 30. Fasılda <b>yer almaz</b>?",
            "secenekler": ["İnsan kanı", "Gaz bezi", "Sigara bırakmaya yardımcı bant", "Kızamık aşısı"],
            "cevap": "C",
            "aciklama": "Fasıl 30 Not 1 uyarınca nikotin içeren, sigarayı bırakmaya yardımcı tablet, ciklet ve bantlar 24.04’te yer alır. İnsan kanı ve kızamık aşısı 30.02’de, tıbbi amaçla hazırlanmış gaz bezi 30.05’tedir.",
        },
        {
            "soru": "Kullanım süresi bitmiş hazır ilaçların sınıflandırıldığı tarife pozisyonu nedir?",
            "secenekler": ["30.04", "30.06", "38.25", "39.15"],
            "cevap": "B",
            "aciklama": "Fasıl 30 Not 4(k), raf ömrünün bitmesi gibi nedenlerle tasarlandığı amaçla kullanılamayan eczacılık ürünlerini 30.06’ya verir; bu ürünler artık 30.04’teki ilaç sayılmaz.",
        },
    ],
    "ozet": [
        "Önce dışarı: gıda ve takviyeler Bölüm IV, nikotinli ürün 24.04, kozmetik 33.03–33.07, tıbbi sabun 34.01, teşhis reaktifi 38.22.",
        "Kan, serum, aşı, bağışıklık ürünleri, toksinler ve kültürler her halükarda 30.02.",
        "Not 4 listesi kapalıdır: sayılmayan 30.06’ya giremez; sayılan (miadı dolmuş ilaç dahil) başka yere gitmez.",
        "İlaç: karışık ve dökme 30.03; dozlandırılmış veya perakende 30.04; karışım olmayan dökme madde kendi faslında.",
        "Pamuk, gazlı bez, bandaj: ilaç emdirilmiş veya tıbbi perakende ise 30.05.",
        "Kurutulmuş organ, organ hülasası, heparin ve ilaç haline gelmemiş zehirler 30.01.",
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
