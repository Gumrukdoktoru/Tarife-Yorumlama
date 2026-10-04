#!/usr/bin/env python3
"""Deneme sınavı 6 üreticisi → data/deneme_06.json"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "deneme_06.json")

LET = "ABCDE"
SORULAR = []


def q(fasil, tip, harf, soru, dogru, yanlis, gerekce, dayanak):
    """Doğru seçeneği istenen harfe yerleştirir, çeldiricileri sırayla dağıtır."""
    assert len(yanlis) == 4, soru
    secenekler = list(yanlis)
    secenekler.insert(LET.index(harf), dogru)
    SORULAR.append({
        "soru": soru,
        "secenekler": secenekler,
        "cevap": harf,
        "tip": tip,
        "gerekce": gerekce,
        "dayanak": dayanak,
        "fasil": fasil,
    })


ES = "Eşya → 4’lü pozisyon"
OL = "Olumsuz teşhis"
FA = "Farklı/aynı pozisyon veya fasıl"
FN = "Fasıl notu · Tanım/Eşik"
GY = "Genel Yorum Kuralı"
EB = "Eşleştirme / Boşluk doldurma"
CC = "Çoktan-çoğa (I–IV)"
SE = "Senaryo"

# 1
q(1, ES, "C",
  "Tarife Cetveline göre, Poephagus cinsine giren canlı Tibet sığırı (yak, Bos grunniens) hangi pozisyonda sınıflandırılır?",
  "01.02", ["01.06", "01.04", "01.01", "95.08"],
  "01.02 Açıklama Notu, sığırlar kategorisinde Bos cinsinin Poephagus alt grubunu sayar ve Tibet sığırlarını (Bos grunniens) açıkça örnek verir. "
  "Yabani veya egzotik görünüşü nedeniyle 01.06’daki “diğer canlı hayvanlar”ı seçmek tipik tuzaktır; 01.06 yalnızca 01.01–01.05 dışında kalan hayvanları kapsar. "
  "01.04 koyun ve keçileri, 01.01 at türlerini kapsar; 95.08 ise yalnızca sirk ve gezici hayvan gösterilerindeki hayvanlar içindir.",
  "Fasıl 1 Notu; 01.02 Açıklama Notu.")

# 2
q(44, FA, "E",
  "Aşağıdaki eşyadan hangisi Tarife Cetvelinde diğerlerinden <b>farklı</b> bir pozisyonda sınıflandırılır?",
  "Ahşap çerçeveli cam ayna",
  ["Kakmalı ahşap resim çerçevesi", "Lif levhadan yapılmış fotoğraf çerçevesi",
   "Arkası kaplanmış ve camı takılmış, içi boş ahşap fotoğraf çerçevesi", "Yonga levhadan yapılmış, aynası takılmamış ayna çerçevesi"],
  "44.14 Açıklama Notu; resim, fotoğraf, ayna ve benzerleri için ahşap çerçeveleri, kakmalı olanları, arkası kaplanmış ve cam takılmış olanları ve yonga levha veya lif levhadan yapılanları bu pozisyonda sayar. "
  "Aynı not çerçevelenmiş cam aynaları açıkça 44.14 dışında bırakır; bunlar 70.09’da yer alır, çünkü eşyaya esas niteliğini ayna verir. "
  "Tuzak, çerçevenin ahşap olmasına bakarak aynayı da 44.14’e koymaktır.",
  "44.14 Açıklama Notu.")

# 3
q(10, ES, "A",
  "Tarife Cetveline göre, değirmencilik işlemleri sırasında kırılan ve başka bir işleme tabi tutulmamış kırık pirinç taneleri hangi pozisyonda sınıflandırılır?",
  "10.06", ["11.03", "11.02", "11.04", "23.02"],
  "Fasıl 10 Not 1(B), kavuzundan çıkarılmış veya başkaca işlenmiş hububat tanelerini fasıl dışında bırakmakla birlikte kavuzu çıkarılmış, değirmenden geçirilmiş, parlatılmış, yarım kaynatılmış veya kırık pirinçleri 10.06’da tutar; 10.06 Açıklama Notu da kırık pirinci ayrıca sayar. "
  "Diğer hububatta olduğu gibi işlenmiş tane sayıp ürünü Fasıl 11’e (11.03 veya 11.04) götürmek tuzaktır; pirinç için notta açık istisna vardır. "
  "11.02 hububat unlarını, 23.02 ise kepek ve benzeri kalıntıları kapsar.",
  "Fasıl 10 Not 1(B); 10.06 Açıklama Notu.")

# 4
q(33, FA, "D",
  "Aşağıdaki eşya çiftlerinden hangisinde her iki eşya da Tarife Cetvelinde <b>aynı</b> pozisyonda sınıflandırılır?",
  "Takma dişleri ağızda sabit tutmaya mahsus toz – Ağız parfümü",
  ["Bireysel ambalajda perakende satılan diş ipi – Diş fırçası", "Ağız suyu – Tıraş sonrası losyonu",
   "Diş macunu – Saç şampuanı",
   "Bireysel ambalajda perakende satılan diş ipi – Büyük makaralar halinde dökme diş ipliği"],
  "33.06 pozisyonu ağız ve diş sağlığını korumaya mahsus müstahzarları kapsar; açıklama notu ağız sularını, ağız parfümlerini ve takma dişleri ağızda sabit tutmaya mahsus pat, toz ve tabletleri birlikte sayar. "
  "Diş ipi ancak bireysel kullanıma mahsus ambalajda perakende satılacak hale getirilmişse 33.06’dadır; dökme diş ipliği bu pozisyona girmez. "
  "Diş fırçası 96.03’te, tıraş sonrası losyonu 33.07’de, şampuan 33.05’te yer aldığından diğer çiftler ayrışır.",
  "33.06 pozisyon metni ve Açıklama Notu.")

# 5
q("GYK", GY, "B",
  "GYK 2(a) açıklama notuna göre, bu kuralın birleştirilmemiş veya demonte şekilde sunulan eşyaya ilişkin hükümlerinin aktarıldığı Bölüm ve Fasıl Genel Açıklama Notları arasında aşağıdakilerden hangisi <b>yer almaz</b>?",
  "Fasıl 62", ["Bölüm XVI", "Fasıl 44", "Fasıl 87", "Fasıl 89"],
  "GYK 2(a) Açıklama Notu (VIII), kuralın birleştirilmemiş veya demonte eşyaya ilişkin hususlarının Bölüm XVI ile Fasıl 44, 86, 87 ve 89’un Genel Açıklama Notlarına aktarıldığını belirtir. "
  "Fasıl 62 ise aynı notun (IV) numaralı paragrafında, kuralın tamamlanmamış veya bitirilmemiş eşyaya ilişkin kısmı için sayılan Bölüm XVI ile Fasıl 61, 62, 86, 87 ve 90 arasında yer alır. "
  "Tuzak, kuralın iki kısmı için verilen listeleri birbirine karıştırmaktır.",
  "GYK 2(a) Açıklama Notu (IV) ve (VIII).")

# 6
q(66, ES, "E",
  "Tarife Cetveline göre, tutamağı açılıp kapanarak oturma yeri oluşturan iskemle bastonlarda kullanılmak üzere ayrı olarak sunulan oturma tablası hangi pozisyonda sınıflandırılır?",
  "66.03", ["66.02", "94.01", "94.03", "90.21"],
  "66.03 pozisyonu 66.01 ve 66.02’deki eşyanın aksam, süs ve teferruatını kapsar; açıklama notu bu aksam arasında baston için sivri uçlu demirler ile iskemle bastonlara mahsus oturma tablalarını açıkça sayar. "
  "Ayrı sunulan tabla bastonun kendisi olmadığından 66.02’ye girmez; oturmaya yaradığı için 94. Fasıldaki oturmaya mahsus eşya veya mobilya olarak düşünmek tuzaktır. "
  "90.21 ise destekler ve koltuk değnekleri gibi ortopedik eşyayı kapsar.",
  "66.03 Açıklama Notu; 66.02 Açıklama Notu.")

# 7
q(16, OL, "A",
  "Aşağıdakilerden hangisi Tarife Cetvelinin 16. faslında <b>sınıflandırılmaz</b>?",
  "Esası et ve balık olan, kediler için hazırlanmış konserve mama",
  ["Pişirilerek konserve edilmiş kara salyangozu", "Hazırlanmış deniz hıyarı konservesi",
   "Konserve edilmiş deniz anası", "Hava geçirmez kutuda yağ içinde konserve edilmiş yılan balığı"],
  "Fasıl 16 Genel Açıklamaları, hayvan beslemek için kullanılan ve esası et, sakatat, balık vb. olan müstahzarları fasıl dışında bırakarak 23.09’a gönderir; kedi maması bu nedenle Fasıl 16’ya girmez. "
  "16.05 Açıklama Notu hazırlanmış veya konserve edilmiş salyangozları, deniz hıyarlarını ve deniz analarını bu pozisyonda sayar; yağ içinde konserve edilmiş yılan balığı ise hazırlanmış balık olarak 16.04’tedir. "
  "Tuzak, ürünün etten ve balıktan yapılmış olmasını tek başına yeterli saymaktır; kullanım amacı (hayvan yemi) belirleyicidir.",
  "Fasıl 16 Genel Açıklamaları; 16.04 ve 16.05 Açıklama Notları.")

# 8
q(9, FA, "C",
  "Kurutulmuş halde sunulan aşağıdaki bitkisel ürünlerden hangisi Tarife Cetvelinde diğerlerinden <b>farklı</b> bir fasılda sınıflandırılır?",
  "Biberiye yaprakları", ["Kekik", "Defne yaprakları", "Safran", "Köri"],
  "09.10 pozisyonu zencefil, safran, zerdeçal, kekik, defne yaprakları, köri ve diğer baharatı kapsar; kekik ve defne yaprakları kurutulmuş olsun olmasın bu pozisyondadır. "
  "Fasıl 9 Genel Açıklamaları ise baharat olarak kullanılabilmekle beraber daha çok parfümeri veya ilaç yapımında kullanılan biberiye, fesleğen, adaçayı ve bütün nane türleri gibi bitki parçalarını 12.11’e gönderir. "
  "Mutfakta baharat gibi kullanılması biberiyeyi Fasıl 9’a sokmaz.",
  "Fasıl 9 Genel Açıklamaları; 09.10 pozisyon metni ve Açıklama Notu.")

# 9
q(81, ES, "B",
  "Stibnit cevherinin zenginleştirilmesiyle elde edilen ve “ham antimon” denilen ham sülfürün ergitilmesi sonucu üretilen, “regulus” adı verilen saf olmayan antimon Tarife Cetvelinde hangi pozisyonda sınıflandırılır?",
  "81.10", ["26.17", "26.20", "81.12", "78.01"],
  "81.10 Açıklama Notu antimonun stibnitten elde edilişini anlatırken yalnızca “ham antimon” denilen ham sülfürü 26.17’ye bırakır; bunun ergitilmesiyle elde edilen saf olmayan regulus artık metal antimondur ve işlenmemiş antimon olarak 81.10’da yer alır. "
  "Tuzak, “ham” nitelemesi veya saf olmayışı nedeniyle ürünü cevher (26.17) ya da cüruf ve kalıntı (26.20) saymaktır. "
  "Antimon 81.12’de sayılan metaller arasında değildir; 78.01 ise işlenmemiş kurşuna aittir.",
  "81.10 Açıklama Notu; 26.17 Açıklama Notu.")

# 10
q(56, FN, "D",
  "Tarife Cetveline göre, özellikle kadifelerin yüzlerinin tıraş edilmesi gibi finisaj işlemlerinden elde edilen dokumaya elverişli lif kırpıntılarının 56.01 pozisyonunda yer alabilmesi için liflerin uzunluğu en fazla ne kadar olmalıdır?",
  "5 mm", ["1 mm", "2 mm", "10 mm", "25 mm"],
  "56.01 pozisyon metni ve açıklama notu, uzunluğu 5 mm’yi geçmeyen dokumaya elverişli lifleri (kırpıntılar) ve dokumaya elverişli maddelerin toz ve tarazlarını bu pozisyonda toplar; bu kırpıntılar finisaj işlemlerinden veya lif demetlerinin kesilmesinden elde edilir. "
  "Parfümlü kırpıntı ve tozlar 33.07’ye gider; yatak ve yastık doldurmada kullanılan paçavra kırpıntıları ise döküntü olarak 50–55. Fasıllarda kalır.",
  "56.01 pozisyon metni ve Açıklama Notu (B).")

# 11
q(2, ES, "A",
  "Tarife Cetveline göre, pişirildikten sonra kurutulup öğütülmüş, insan tüketimine uygun sığır eti unu hangi pozisyonda sınıflandırılır?",
  "02.10", ["16.02", "23.01", "02.02", "11.06"],
  "02.10 pozisyon metni etlerin ve sakatatın yenilen un ve kaba unlarını kapsar; Fasıl 2 Genel Açıklamaları da insan tüketimine uygun un veya kaba un halindeki et ve sakatatın pişirilmiş olsun olmasın bu fasılda kaldığını belirtir. "
  "Pişirilmiş olması ürünü 16.02’ye götürmez; Fasıl 16 Genel Açıklamaları yenilebilir et unlarını açıkça 02.10’a bırakır. "
  "İnsan tüketimine elverişli olmayan et ve sakatat unları ise 23.01’de yer alır; 11.06 sebze ve meyve unları içindir.",
  "Fasıl 2 Genel Açıklamaları; 02.10 pozisyon metni; Fasıl 16 Genel Açıklamaları.")

# 12
q(89, OL, "D",
  "Aşağıdakilerden hangisi 89.03 pozisyonunda <b>sınıflandırılmaz</b>?",
  "Eğlence parkındaki su kanalı gezintisinde kullanılan küçük sandal",
  ["Sert karinalı, şişirilebilir gezinti botu", "Eskimo kayığı",
   "Balık avı sporu için kullanılan motorbot", "Yardımcı motoru bulunan yelkenli yat"],
  "89.03 pozisyonu yatları ve spor ve eğlence amaçlı tüm deniz taşıtlarını; şişirilen, monte edilebilen veya katlanan botları, eskimo kayıklarını ve balıkçılık sporunda kullanılan taşıtları kapsar. "
  "Fasıl 89 Genel Açıklamaları ise eğlence parkı gezintileri, su parkı eğlenceleri ve diğer fuar eğlencelerinde kullanılan küçük sandalları fasıl dışında bırakarak 95.08’e gönderir. "
  "Tuzak, “eğlence amaçlı tekne” ifadesine bakıp bu sandalı da 89.03’e koymaktır.",
  "Fasıl 89 Genel Açıklamaları; 89.03 Açıklama Notu.")

# 13
q(57, FA, "E",
  "Aşağıdaki halı ve yer kaplamalarından hangisi Tarife Cetvelinde diğerlerinden <b>farklı</b> bir pozisyonda sınıflandırılır?",
  "Havları yapıştırıcı veya ısıl işlemle zemin tabakasına tutturulmuş yapıştırılmış havlı halı",
  ["Tel çubuklar yardımıyla bukle oluşturularak dokunan Wilton halısı",
   "Çift katlı mensucattan oluşan Kidderminster tipi (Belçika) halı",
   "Çözgüsü jüt iplik, atkısı mensucat döküntüsü şeritlerinden dokunmuş paçavra halısı",
   "Havlu mensucattan banyo paspası"],
  "57.02 Açıklama Notu dokunmuş halılar arasında Wilton ve benzeri halıları, Kidderminster tipi (Belçika) halıları, paçavra halılarını ve havlu mensucattan banyo paspaslarını sayar. "
  "Havları yapıştırıcı, ısı veya ultrasonik kaynakla zemin tabakaya ya da doğrudan yapıştırıcıya tutturulan yapıştırılmış havlı halılar ise dokuma işlemiyle elde edilmediğinden 57.05 Açıklama Notunda “diğer halılar” arasında sayılır. "
  "Havlı görünümü nedeniyle bu halıyı Wilton gibi dokunmuş halı sanmak tuzaktır.",
  "57.02 ve 57.05 Açıklama Notları.")

# 14
q(32, ES, "B",
  "Tarife Cetveline göre, çinko sülfür ile baryum sülfatın değişik oranlardaki karışımından oluşan, litopon adıyla bilinen beyaz pigment hangi pozisyonda sınıflandırılır?",
  "32.06", ["28.30", "32.04", "32.12", "28.33"],
  "32.06 Açıklama Notu, esası çinko sülfür olan pigmentler arasında litoponu, yani çinko sülfür ve baryum sülfatın değişik oranlardaki karışımlarından oluşan beyaz pigmentleri açıkça sayar. "
  "Ürün iki bileşiğin karışımı olduğundan kimyasal olarak belirli yapıda izole bir bileşik değildir; bu nedenle sülfürler veya sülfatlar olarak Fasıl 28’e giremez. "
  "32.04 sentetik organik boyayıcı maddeleri, 32.12 ise boya imalinde kullanılan, susuz ortamda dağılan sıvı veya hamur haldeki pigmentleri kapsar.",
  "32.06 Açıklama Notu.")

# 15
q("GYK", GY, "C",
  "Bir pozisyonun alt pozisyonlarında sınıflandırma yapılırken GYK 6 açıklama notuna göre aşağıdaki ifadelerden hangisi doğrudur?",
  "İki tireli bir alt pozisyonun kapsamı ait olduğu tek tireli alt pozisyonun, tek tireli alt pozisyonun kapsamı da ait olduğu pozisyonun kapsamı dışına çıkamaz.",
  ["Farklı seviyelerdeki alt pozisyonlar, yani tek tireli ve iki tireli alt pozisyonlar, eşyaya göre birbiriyle doğrudan karşılaştırılabilir.",
   "Alt pozisyon düzeyinde yalnızca GYK 6 uygulanır; 1 ila 5 numaralı kurallar bu düzeyde hiç uygulanmaz.",
   "İki tireli bir alt pozisyon, ait olduğu tek tireli alt pozisyonun metninde yer almayan eşyayı da kapsayabilir.",
   "Tek tireli alt pozisyonlar karşılaştırılırken bunların altındaki iki tireli alt pozisyonların metinleri de her durumda birlikte dikkate alınır."],
  "GYK 6 Açıklama Notu, 1 ila 5 numaralı kuralların gerekli değişikliklerle alt pozisyonlarda da uygulandığını ve yalnızca aynı seviyedeki (tek tireli veya iki tireli) alt pozisyonların karşılaştırılacağını belirtir; iki tireli alt pozisyonların içeriği ancak eşyayı en özel niteleyen tek tireli alt pozisyon seçildikten sonra dikkate alınır. "
  "Notun son paragrafı, iki tireli alt pozisyon kapsamının ait olduğu tek tireli alt pozisyon kapsamının, tek tireli alt pozisyon kapsamının da pozisyon kapsamının dışına çıkamayacağını hükme bağlar. "
  "Diğer seçenekler bu hükümlerle çelişir.",
  "GYK 6 Açıklama Notu (I) ve (II).")

# 16
q(18, OL, "E",
  "Aşağıdakilerden hangisi 18.06 pozisyonunda <b>sınıflandırılmaz</b>?",
  "Kakao danelerinden özel makinelerde ayrılan, pratikte yağ içermeyen kakao rüşeymleri",
  ["Pepton katılmış kakao tozu", "Ekmeğe sürülebilen çikolata",
   "İçi likörle doldurulmuş çikolata pralinler", "Toz halindeki çikolata"],
  "18.02 pozisyonu kakao kabukları, zarları ve diğer kakao döküntülerini kapsar; açıklama notu kakao danelerinden özel makinelerle ayrılan ve pratikte yağ içermeyen kakao rüşeymlerini bu pozisyonda sayar. "
  "18.05 ve 18.06 Açıklama Notları ise süt tozu veya pepton katılmış kakao tozunu, çikolata tozunu, sürülebilen çikolatayı ve krema, likör vb. ile doldurulmuş çikolata ürünlerini 18.06’ya dahil eder. "
  "Tuzak, pepton katkısını önemsiz sayıp ürünü 18.05’e götürmek veya rüşeymi kakao danesi gibi düşünmektir.",
  "18.02, 18.05 ve 18.06 Açıklama Notları.")

# 17
q(65, FA, "A",
  "Aşağıdaki başlıklardan hangisi Tarife Cetvelinde diğerlerinden <b>farklı</b> bir fasılda sınıflandırılır?",
  "Fazlaca kullanıldığını gösteren izler taşıyan, balyalar halinde sunulan başlıklar",
  ["Mensucattan yapılmış aşçı başlığı", "Örme ve keçeleştirme yoluyla elde edilmiş fes",
   "Silindir şapka", "Yağ emdirilmiş mensucattan geniş kenarlı gemici başlığı"],
  "Fasıl 65 Not 1(a) ve Genel Açıklamalar, fazlaca kullanıldığını gösteren izler taşıyan ve dağınık halde veya balya, çuval ve benzeri ambalajlarda sunulan başlıkları fasıl dışında bırakarak 63.09’a gönderir. "
  "Aşçı başlıkları, fesler, silindir şapkalar ve yağ emdirilmiş mensucattan gemici başlıkları 65.05 Açıklama Notunda dokumaya elverişli maddelerden başlıklar arasında sayılır. "
  "Tuzak, bütün seçeneklerin başlık olmasına bakıp eşyanın kullanılmış ve balyalanmış halini gözden kaçırmaktır.",
  "Fasıl 65 Not 1(a); Fasıl 65 Genel Açıklamaları; 65.05 Açıklama Notu.")

# 18
q(11, ES, "B",
  "Tarife Cetveline göre; koruma kalitesini artırmak amacıyla yağı kısmen alınmış ve ısıl işlem görmüş, işleme sırasındaki kayıpları telafi etmek için vitamin eklenerek öğütülmüş buğday embriyonu hangi pozisyonda sınıflandırılır?",
  "11.04", ["23.06", "23.02", "11.01", "21.06"],
  "Fasıl 11 Not 2(A), bütün halde, yuvarlatılmış, flokon halinde veya öğütülmüş hububat embriyonlarının daima 11.04’te sınıflandırılacağını belirtir; 11.04 Açıklama Notu da embriyonun koruma amacıyla yağının kısmen alınabileceğini, ısıl işleme tabi tutulabileceğini, öğütülebileceğini ve kayıpları telafi için vitamin eklenebileceğini açıkça kabul eder. "
  "Aynı nota göre 23.06’ya giden, embriyonlardan yağ çıkarılması sonucu kalan artıklardır; kısmen yağı alınmış embriyon bu kapsamda değildir. "
  "Vitamin katkısı ürünü 21.06’daki gıda müstahzarlarına götürmez; 23.02 kepek ve benzeri kalıntılar, 11.01 buğday unu içindir.",
  "Fasıl 11 Not 2(A); 11.04 Açıklama Notu.")

# 19
q(80, FN, "D",
  "Tarife Cetveline göre kalay granülleri 80.01’de kalırken kalay tozları 80.07’de sınıflandırılır. Bölüm XV notlarına göre bir ürünün “toz” sayılabilmesi için aşağıdaki ölçütlerden hangisini karşılaması gerekir?",
  "Göz açıklığı 1 mm olan elekten ağırlık itibariyle %90 veya daha fazlasının geçmesi",
  ["Göz açıklığı 1 mm olan elekten ağırlık itibariyle %50’sinden fazlasının geçmesi",
   "Göz açıklığı 0,5 mm olan elekten ağırlık itibariyle %90 veya daha fazlasının geçmesi",
   "Göz açıklığı 2 mm olan elekten ağırlık itibariyle %95 veya daha fazlasının geçmesi",
   "Tanelerin tamamının 1 mm’den küçük ve aynı boyutta olması"],
  "Bölüm XV Not 8(b), bu bölümde “tozlar” tabirinden göz açıklığı 1 mm olan elekten ağırlık itibariyle %90 veya daha fazlası geçen ürünleri anlar. "
  "80.01 Açıklama Notu kalay kırıntı ve granüllerini işlenmemiş kalay sayarken kalay tozları ve pullarını 80.07’ye gönderdiğinden bu tanım iki pozisyonu birbirinden ayırır. "
  "Diğer seçeneklerdeki elek ölçüleri ve oranlar notta yer almaz.",
  "Bölüm XV Not 8(b); 80.01 Açıklama Notu.")

# 20
q(3, OL, "C",
  "Aşağıdakilerden hangisi 03.07 pozisyonunda <b>sınıflandırılmaz</b>?",
  "Tuzlanmış deniz anası",
  ["Yetiştiricilik amacına yönelik, insan gıdası olarak kullanılmaya elverişli istiridye yumurtası",
   "Kurutulmuş mürekkep balığı", "Salamura edilmiş deniz kulağı", "Dondurulmuş kara salyangozu"],
  "03.07 Açıklama Notu yumuşakçalar arasında istiridyeleri, mürekkep balıklarını, salyangozları ve deniz kulağını sayar ve yetiştiricilik amacına yönelik, insan gıdası olarak kullanılmaya elverişli istiridye yumurtasını da bu pozisyona dahil eder. "
  "Deniz anası ise kabuklu hayvan veya yumuşakça olmayan bir su omurgasızıdır; 03.08 Açıklama Notu deniz kestanesi ve deniz hıyarıyla birlikte deniz anasını bu pozisyonda sayar. "
  "Tuzak, bütün deniz canlılarını yumuşakça saymaktır.",
  "03.07 ve 03.08 Açıklama Notları.")

# 21
q(46, ES, "E",
  "Tarife Cetveline göre, saman saplarından doğrudan doğruya örülerek şekil verilmiş arı kovanı hangi pozisyonda sınıflandırılır?",
  "46.02", ["46.01", "44.21", "84.36", "14.01"],
  "46.02 pozisyonu örülmeye elverişli maddelerden doğrudan şekil verilerek elde edilmiş sepetçi eşyasını kapsar; açıklama notu bu eşyaya örnek olarak istakoz kaplarını, kuş kafeslerini ve arı kovanlarını açıkça sayar. "
  "46.01 örgüler ile hasır, paspas, paravan gibi levha halindeki eşyayı kapsadığından şekil verilmiş kovan için uygun değildir. "
  "44.21 ahşap eşya, 84.36 arıcılığa mahsus makine ve cihazlar, 14.01 ise örücülükte kullanılan işlenmemiş bitkisel maddeler içindir.",
  "Fasıl 46 Not 1; 46.02 Açıklama Notu.")

# 22
q(15, FA, "A",
  "Aşağıdaki ham bitkisel yağ çiftlerinden hangisinde her iki yağ da Tarife Cetvelinde <b>aynı</b> pozisyonda sınıflandırılır?",
  "Aspir yağı – Pamuk tohumu yağı",
  ["Hardal yağı – Susam yağı", "Palm yağı – Palm çekirdeği yağı",
   "Yer fıstığı yağı – Soya yağı", "Hindistan cevizi (kopra) yağı – Kolza yağı"],
  "15.12 pozisyonu ayçiçeği tohumu, aspir ve pamuk tohumu yağlarını ve fraksiyonlarını birlikte kapsar. "
  "Hardal yağı rep ve kolza yağıyla birlikte 15.14’te, susam yağı ise 15.15’teki diğer bitkisel sabit yağlar arasındadır; Hindistan cevizi yağı palm çekirdeği ve babassu yağlarıyla 15.13’te yer alır. "
  "Palm yağı 15.11’de, yer fıstığı yağı 15.08’de, soya yağı 15.07’dedir; aynı ağaçtan gelse de palm meyvesi ile çekirdeğinin yağları ayrı pozisyonlardadır.",
  "15.07, 15.08 ve 15.11–15.15 pozisyon metinleri.")

# 23
q(83, OL, "C",
  "Adi metalden yapılmış, elektrikli olmayan aşağıdaki zil, çan ve bunların aksamından hangisi 83.06 pozisyonunda <b>sınıflandırılmaz</b>?",
  "Duvar saatlerine mahsus zil ve gonglar",
  ["Okullar ve ibadet yerleri için çanlar", "Sığırlara takılan çanlar",
   "Bisikletlere takılan ziller", "Elektrikli olmayan masa zillerine mahsus metal düğmeler"],
  "83.06 Açıklama Notu, adi metalden elektrikli olmayan zil ve çanlar arasında ibadet yerleri, okullar ve umuma açık binalar için çanları, hayvanlara takılan çanları, bisikletlere takılan zilleri ve elektrikli olmayan masa ve kapı zillerine mahsus metal düğmeleri sayar. "
  "Aynı not saat zillerini ve gonglarını pozisyon dışında bırakarak 91.14’e gönderir; elektrikli ziller 85.31’de, müzik aleti niteliğindeki çan takımları ise 92. Fasılda yer alır. "
  "Tuzak, zilin elektriksiz ve adi metalden olmasını yeterli saymaktır.",
  "83.06 Açıklama Notu (A).")

# 24
q(17, ES, "B",
  "Tarife Cetveline göre; şeker rafinasyonu sırasında veya sakkarozun kısmi inversiyonuyla elde edilen, sakkaroz ve invert şeker içeren, ilave aroma veya renk verici madde katılmamış sofralık “golden şurup” hangi pozisyonda sınıflandırılır?",
  "17.02", ["17.03", "21.06", "17.01", "17.04"],
  "17.02 Açıklama Notunun şeker şurupları kısmı, ilave aroma ve renk verici madde içermemek şartıyla bütün şeker şuruplarını kapsar ve sakkaroz ile invert şeker içeren sofralık veya yemeklik golden şurubu ismen sayar. "
  "Aroma veya renk katılmış şeker şurupları 21.06’ya gider; 17.03 yalnızca şekerin çıkarılması veya rafinasyonundan elde edilen, kolayca kristalleşmeyen şeker içeren melasları kapsar. "
  "17.01 ise yalnızca katı haldeki kamış ve pancar şekeri içindir.",
  "17.01, 17.02 ve 17.03 Açıklama Notları.")

# 25
q(39, FN, "D",
  "Bölüm VII Not 1’e göre, tamamen veya kısmen bu bölümde yer alan birbirinden farklı maddelerden oluşan takım halindeki eşyanın, bu maddelerin karıştırılmasıyla elde edilecek ürünün pozisyonunda sınıflandırılabilmesi için aranan şartlar arasında aşağıdakilerden hangisi <b>yer almaz</b>?",
  "Perakende satış için hazırlanmış ambalajlarda sunulmaları",
  ["Karıştırıldıktan sonra VI. veya VII. Bölümün bir ürününü oluşturabilmeleri",
   "Oluşturdukları şekle göre, tekrar bir araya getirmeye gerek duyulmadan bir arada kullanılmaya mahsus oldukları açıkça belli olmaları",
   "Birlikte ithal edilmeleri",
   "Nitelikleri veya miktarları itibarıyla birbirinin tamamlayıcısı olarak kabul edilebilmeleri"],
  "Bölüm VII Not 1, karıştırıldıktan sonra VI. veya VII. Bölümün bir ürününü oluşturabilen takım halindeki maddelerin; tekrar bir araya getirmeye gerek duyulmadan bir arada kullanılmaya mahsus oldukları açıkça belli olması, birlikte ithal edilmeleri ve nitelik veya miktar itibarıyla birbirinin tamamlayıcısı olmaları şartıyla o ürünün pozisyonunda sınıflandırılacağını belirtir. "
  "Notta perakende ambalaj şartı yoktur; perakende satışa sunulmuş olup önceden karıştırılmaksızın birbiri ardına kullanılacak takımlar ise not kapsamı dışında kalır ve genellikle GYK 3(b) ile sınıflandırılır.",
  "Bölüm VII Not 1 ve Genel Açıklamaları.")

# 26
q("GYK", GY, "E",
  "Tüm parçaları aynı kolide, sökülmüş halde gümrüğe sunulan bir bisikletin dış ve iç lastikleri, tek başlarına sunulduklarında kendi pozisyonlarında sınıflandırılabilecek niteliktedir. Genel Yorum Kurallarının açıklama notlarına göre bu eşyanın sınıflandırılmasıyla ilgili aşağıdakilerden hangisi doğrudur?",
  "GYK 2(a) uyarınca lastikler dahil bütün parçalar, imalatı bitirilmiş bir bisiklet olarak birlikte sınıflandırılır.",
  ["Dış ve iç lastikler ayrılarak kendi pozisyonlarında, kalan parçalar bisiklet aksamı olarak sınıflandırılır.",
   "GYK 2(a) yalnızca eksik eşyaya uygulandığından sökülmüş eşyanın her parçası ayrı ayrı sınıflandırılır.",
   "GYK 3(b) uyarınca esas niteliği veren kadronun pozisyonunda aksam olarak sınıflandırılır.",
   "Montajı cıvata ve somunla yapılacağından GYK 2(b) uyarınca birden fazla maddeden oluşan eşya olarak değerlendirilir."],
  "GYK 1 Açıklama Notu (III), 2 numaralı kurala yapılan atfın, parçaları kendi başlarına (lastikler, iç lastikler) sınıflandırılabilecek olsa bile birleştirilmemiş veya sökülmüş olarak sunulan eşyanın (tüm parçaları bir arada sunulan bisiklet örneği) imalatı bitirilmiş bütün eşya olarak sınıflandırılması anlamına geldiğini açıkça belirtir. "
  "GYK 2(a)’nın ikinci kısmı, sökülmüş veya monte edilmemiş eşyayı monte edilmiş eşya ile aynı pozisyonda tutar ve hem eksik hem demonte eşyaya uygulanır. "
  "2(b) maddelerin karışım ve bileşimleriyle ilgilidir; 3(b) ise ancak eşya ilk bakışta birden fazla pozisyona girebildiğinde gündeme gelir.",
  "GYK 1 Açıklama Notu (III)(b); GYK 2(a) Açıklama Notu (V)–(VII).")

# 27
q(45, ES, "B",
  "Tarife Cetveline göre, döşemecilikte doldurma maddesi olarak kullanılan, “mantar yünü” şeklindeki tabii mantar döküntüleri hangi pozisyonda sınıflandırılır?",
  "45.01", ["45.04", "45.03", "14.04", "53.05"],
  "45.01 Açıklama Notu, tabii veya aglomere mantarın döküntülerini bu pozisyonda sayar ve “mantar yünü” şeklinde olan ve bazen döşemecilikte doldurma maddesi olarak kullanılan mantar döküntülerinin de bu gruba dahil olduğunu belirtir. "
  "“Yün” adı nedeniyle ürünü dokumaya elverişli bitkisel lif (Fasıl 53) veya bitkisel doldurma maddesi (14.04) saymak tuzaktır. "
  "Ürün aglomere edilmediği için 45.04’e, mamul eşya olmadığı için de 45.03’e girmez.",
  "45.01 Açıklama Notu.")

# 28
q(35, ES, "A",
  "Tarife Cetveline göre, proteinlerin hidrolize edilmesiyle veya pepsin, papain gibi enzimlerin etkisiyle elde edilen, nem çekici, beyaz veya sarımsı toz halindeki peptonlar hangi pozisyonda sınıflandırılır?",
  "35.04", ["35.07", "35.02", "16.03", "35.01"],
  "35.04 pozisyonu peptonları ve bunların türevlerini kapsar; açıklama notu peptonları proteinlerin hidrolizi veya pepsin, papain, pankreatin gibi enzimlerin etkisiyle elde edilen eriyebilir, higroskopik tozlar olarak tanımlar. "
  "Elde edilişinde enzim kullanılması ürünü 35.07’deki enzimlere götürmez. "
  "16.03 Açıklama Notu da peptonları et ve balık hülasalarından ayırarak 35.04’e gönderir; 35.02 albüminleri, 35.01 ise kazeinleri kapsar.",
  "35.04 Açıklama Notu; 16.03 Açıklama Notu.")

# 29
q(40, OL, "D",
  "Aşağıdakilerden hangisi 40.17 pozisyonunda <b>sınıflandırılmaz</b>?",
  "Sertleştirilmiş kauçuktan tüfek dipçik levhası",
  ["Sertleştirilmiş kauçuktan su tenekesi", "Sertleştirilmiş kauçuktan fıçı",
   "Sertleştirilmiş kauçuktan boru malzemesi", "Gözenekli yapıdaki sertleştirilmiş kauçuk levha"],
  "40.17 Açıklama Notu, gözenekli çeşitleri ve döküntüleri dahil her haldeki sertleştirilmiş kauçuğu ve başka fasıllarda yer almayan sertleştirilmiş kauçuktan eşyayı kapsar; fıçılar, su tenekeleri ve boru malzemeleri bu eşyaya örnek olarak sayılır. "
  "Aynı not dipçik levhaları ve diğer silah parçalarını pozisyon dışında bırakarak 93. Fasla gönderir; XVI. Bölüm, 90, 92, 94, 95 ve 96. Fasıllara giren eşya da hariçtir. "
  "Tuzak, ebonit gibi tek bir maddeden yapılmış her eşyayı 40.17’ye koymaktır.",
  "40.17 Açıklama Notu.")

# 30
q(26, EB, "C",
  "Aşağıdaki metal cevherleri sınıflandırıldıkları pozisyonlarla eşleştirildiğinde hangi seçenek doğru olur?<br/>"
  "I. Scheelite (kalsiyum tungstat)<br/>II. Arjantit (gümüş sülfür)<br/>III. Sinnabar (cıva sülfür)<br/>IV. Pentlandit (nikel ve demir sülfürü)<br/>"
  "a) 26.04 · b) 26.11 · c) 26.16 · d) 26.17",
  "I-b, II-c, III-d, IV-a",
  ["I-b, II-d, III-c, IV-a", "I-d, II-c, III-b, IV-a", "I-a, II-c, III-d, IV-b", "I-b, II-c, III-a, IV-d"],
  "26.11 Açıklama Notu kalsiyum tungstat olan scheelite’i tungsten cevherleri arasında, 26.16 Açıklama Notu gümüş sülfür olan arjantiti kıymetli metal cevherleri arasında sayar. "
  "Cıva için ayrı bir cevher pozisyonu bulunmadığından sinnabar 26.17 Açıklama Notunda diğer metal cevherleri arasında yer alır. "
  "Nikel ve demir sülfürü olan pentlandit ise 26.04 Açıklama Notunda nikel cevherleri arasında açıkça sayılır; demir içermesi onu demir cevherlerine götürmez.",
  "26.04, 26.11, 26.16 ve 26.17 Açıklama Notları.")

# 31
q(58, ES, "E",
  "Tarife Cetveline göre, bir desen veya mesnet üzerine konulmaksızın doğrudan bir tığ ile elde yapılan, parça halindeki İrlanda işi tığ danteli hangi pozisyonda sınıflandırılır?",
  "58.04", ["60.06", "58.10", "58.08", "63.04"],
  "58.04 Açıklama Notu, elde yapılan danteller arasında iğne işi ve bobino dantellerin yanında bir tığ ile doğrudan doğruya yapılan tığ işi dantelleri (İrlanda işi danteller gibi) açıkça sayar. "
  "Dantelin ayırt edici özelliği desenlerin mevcut bir zemin üzerinde yapılmamasıdır; bu nedenle zemin üzerine iplikle desen işlenen 58.10’daki işlemelerden ayrılır. "
  "Tığ kullanılması dantelleri 60. Fasla götürmez; Fasıl 60’a giden, ilmek yapısından tanınan ajurlu örme eşyadır.",
  "58.04 pozisyon metni ve Açıklama Notu (II).")

# 32
q(8, FA, "D",
  "Aşağıdaki dondurulmuş ürünlerden hangisi Tarife Cetvelinde diğerlerinden <b>farklı</b> bir fasılda sınıflandırılır?",
  "Fırında pişirildikten sonra dondurulmuş elma dilimleri",
  ["Buharda pişirildikten sonra dondurulmuş böğürtlen", "Suda kaynatıldıktan sonra dondurulmuş kestane",
   "Pişirilmeden dondurulmuş vişne", "Az miktarda tuz katılarak dondurulmuş kayısı"],
  "08.11 pozisyonu pişirilmemiş veya buharda ya da suda kaynatılarak pişirilmiş dondurulmuş meyve ve sert kabuklu meyveleri kapsar; açıklama notuna göre bu ürünler ilave şeker veya tuz da içerebilir. "
  "Aynı not, dondurulmadan önce buhar veya kaynatma dışındaki yöntemlerle pişirilen meyveleri pozisyon dışında bırakarak Fasıl 20’ye gönderir. "
  "Bu nedenle belirleyici olan pişirme yöntemidir; fırında pişirilmiş elma Fasıl 20’dedir.",
  "08.11 Açıklama Notu; Fasıl 8 Genel Açıklamaları.")

# 33
q(27, FN, "A",
  "Fasıl 27 Genel Açıklamalarına göre, Fasıl 27 Not 2’de ve 27.07 pozisyonunda geçen “aromatik unsurlar” tabiri neyi ifade eder?",
  "Yan zincirlerinin uzunluğu ve sayısı ne olursa olsun aromatik kısım içeren moleküllerin tamamını",
  ["Moleküllerin yalnızca aromatik halka kısımlarını, yan zincirler hariç",
   "Yalnızca yan zinciri bulunmayan benzen, toluen ve ksileni",
   "Yalnızca taşkömürü katranının yüksek sıcaklıkta damıtılmasıyla elde edilen bileşikleri",
   "Doymamış hidrokarbon karışımlarını oluşturan bütün unsurları"],
  "Fasıl 27 Genel Açıklamaları, Not 2’de ve 27.07’de geçen “aromatik unsurlar” tabirinin moleküllerin yalnızca aromatik kısımlarını değil, yan zincirin uzunluğuna ve sayısına bağlı olmaksızın aromatik kısımlı bütün molekülleri ifade ettiğini belirtir. "
  "Bu tanım, 27.07’de aromatik unsurların ağırlığının aromatik olmayanlardan fazla olması, 27.10 anlamındaki benzeri yağlarda ise bunun tersinin aranması karşılaştırmasında esas alınır. "
  "Tuzak, yalnızca halka kısmının hesaba katılacağını düşünmektir.",
  "Fasıl 27 Not 2; Fasıl 27 Genel Açıklamaları; 27.07 pozisyon metni.")

# 34
q(43, OL, "B",
  "Aşağıdakilerden hangisi 43.04 pozisyonunda <b>sınıflandırılmaz</b>?",
  "Birkaç hakiki kuyruğun veya hakiki kürk parçalarının bir mesnet üzerine dikilmesiyle elde edilmiş fabrikasyon kuyruk",
  ["Deriden bir mesnet üzerine yün ve kıllar yapıştırılarak elde edilmiş taklit kuyruk",
   "Pamuklu dokuma bir mensucat üzerine yün lifleri dikilerek kürkü taklit edecek şekilde elde edilmiş ürün",
   "Deri üzerine tırtıl iplik şeklindeki liflerin dikilmesiyle elde edilmiş taklit kürk",
   "Taklit kürkten yapılmış manto"],
  "43.04 Açıklama Notu taklit kürkü, kürkü taklit edecek şekilde deri, dokunmuş mensucat veya başka maddeler üzerine yün, kıl veya diğer liflerin (tırtıl iplik şeklindeki lifler dahil) yapıştırılması veya dikilmesiyle elde edilen eşya olarak tanımlar; taklit kürkten giysiler ve deri veya ip mesnet üzerine yün ve kıl yapıştırılmış taklit kuyruklar da bu pozisyondadır. "
  "Aynı not, birkaç hakiki kuyruktan oluşan fabrikasyon kuyrukları veya hakiki kürk parçalarının bir mesnet üzerine dikilmesiyle elde edilen kuyrukları 43.04 dışında bırakarak 43.03’e gönderir. "
  "Tuzak, “fabrikasyon” nitelemesini taklit sanmaktır; belirleyici olan kullanılan maddenin hakiki kürk olmasıdır.",
  "Fasıl 43 Not 5; 43.04 Açıklama Notu.")

# 35
q(40, ES, "C",
  "Tarife Cetveline göre; sertleştirilmemiş vulkanize kauçuk levhadan yalnızca kare şeklinde kesilmiş, yüzeyi kabartma desenle işlenmiş, başka bir işleme tabi tutulmamış ve yer döşemesi olarak kullanılacak karolar hangi pozisyonda sınıflandırılır?",
  "40.08", ["40.16", "59.04", "39.18", "40.17"],
  "Fasıl 40 Not 9, 40.08’deki “levhalar, yapraklar ve şeritler” tabirinin kesilmemiş veya dikdörtgen (kare dahil) şeklinde basitçe kesilmiş, kullanıma hazır eşya karakterinde olsun olmasın, baskılı veya başka surette yüzey işçiliğine tabi tutulmuş ürünleri kapsadığını belirtir. "
  "40.16 Açıklama Notu da yer kaplamalarını yalnızca yüzey işçiliği ötesinde işlem görmemiş ve dikdörtgen kesilmiş 40.08’deki döşemeler dışında kalanlar için bu pozisyona alır; başka şekillerde kesilmiş veya ileri işlem görmüş döşemeler 40.16’ya gider. "
  "Ürün plastik veya tekstil mesnetli olmadığından 39.18 ve 59.04, sertleştirilmiş kauçuk olmadığından 40.17 söz konusu değildir.",
  "Fasıl 40 Not 9; 40.08 ve 40.16 Açıklama Notları.")

# 36
q(31, CC, "E",
  "Aşağıdakilerden hangileri 31.05 pozisyonunda sınıflandırılır?<br/>"
  "I. Brüt ağırlığı 25 kg olan torbalarda sunulan, tablet şeklindeki üre<br/>"
  "II. Brüt ağırlığı 50 kg olan torbalarda sunulan, toz halindeki amonyum sülfat<br/>"
  "III. Bitki besin maddelerinden azot ve fosforun ikisini birlikte içeren, dökme halde sunulan mineral gübre<br/>"
  "IV. Brüt ağırlığı 12 kg olan torbalarda sunulan, toz halindeki kalsiyum siyanamit",
  "I ve III", ["I ve II", "II ve IV", "I, III ve IV", "Yalnız III"],
  "31.05 pozisyon metni, azot, fosfor ve potasyumun ikisini veya üçünü içeren mineral veya kimyasal gübreleri ve bu fasıldaki ürünlerin tablet veya benzeri şekillerde ya da brüt ağırlığı 10 kg’ı geçmeyen ambalajlarda olanlarını kapsar; tablet şekli ambalaj ağırlığından bağımsız olarak ürünü 31.05’e götürür. "
  "Toz halindeki amonyum sülfat ile kalsiyum siyanamit 10 kg’ı aşan ambalajlarda sunulduğundan Fasıl 31 Not 2 uyarınca 31.02’de kalır. "
  "Tuzak, yalnızca ambalaj ağırlığına bakıp tablet şeklini gözden kaçırmaktır.",
  "Fasıl 31 Not 2; 31.05 pozisyon metni ve Açıklama Notu.")

# 37
q("GYK", GY, "A",
  "Bir elektrikli tıraş makinesi ile bu makineye göre şekil verilmiş, uzun süre kullanılmaya elverişli ve normal olarak makineyle birlikte satılan türden mahfazası aynı sevkiyatta gümrüğe sunulmuştur; ancak nakliye kolaylığı için makine ve mahfaza ayrı kolilerde paketlenmiştir. Genel Yorum Kurallarına göre mahfazanın sınıflandırılmasıyla ilgili aşağıdakilerden hangisi doğrudur?",
  "GYK 5(a) uygulanır; mahfaza ait olduğu tıraş makinesiyle birlikte 85.10’da sınıflandırılır.",
  ["Ayrı kolide paketlendiği için ayrı sunulmuş sayılır ve kendi pozisyonunda (örneğin 42.02) sınıflandırılır.",
   "Uzun süre kullanılmaya elverişli olduğundan GYK 5(b) uygulanmaz ve mahfaza kendi pozisyonunda ayrıca sınıflandırılır.",
   "GYK 3(b) uyarınca makine ile mahfaza perakende takım oluşturur ve esas niteliği veren makinenin pozisyonunda sınıflandırılır.",
   "GYK 2(a) uyarınca mahfaza, tıraş makinesinin eksik aksamı sayılarak 85.10’da sınıflandırılır."],
  "GYK 5(a) Açıklama Notu (I)(3), kuralın muhafaza ettikleri eşya ile birlikte sunulan kaplara, nakliye amacıyla eşya ayrı ayrı paketlenmiş olsun olmasın uygulandığını; yalnızca ayrı olarak sunulan kutuların kendi pozisyonlarında sınıflandırılacağını belirtir. "
  "Açıklama notu (II), elektrikli tıraş makinesi mahfazasını (85.10) ait olduğu eşya ile birlikte sınıflandırılan mahfazalara örnek olarak sayar. "
  "5(b) ambalaj maddeleri içindir ve 5(a) saklıdır; sonuç takım (3(b)) veya eksik eşya (2(a)) kuralına değil 5(a)’ya dayanır.",
  "GYK 5(a) Açıklama Notu (I) ve (II).")

# 38
q(82, EB, "D",
  "Adi metalden aşağıdaki el aletleri sınıflandırıldıkları pozisyonlarla eşleştirildiğinde hangi seçenek doğru olur?<br/>"
  "I. Cımbız<br/>II. Değişebilir sıkıştırma soketi (sapsız)<br/>III. Mengene<br/>IV. Dişsiz testere ağzı<br/>"
  "a) 82.04 · b) 82.02 · c) 82.05 · d) 82.03",
  "I-d, II-a, III-c, IV-b",
  ["I-c, II-a, III-d, IV-b", "I-d, II-c, III-a, IV-b", "I-d, II-a, III-b, IV-c", "I-b, II-a, III-c, IV-d"],
  "82.03 pozisyon metni eğeler, törpüler, pensler ve kerpetenlerle birlikte cımbızları; 82.04 ise elle kullanılan sıkıştırma anahtarlarıyla birlikte değişebilir sıkıştırma soketlerini (saplı olsun olmasın) sayar. "
  "Mengeneler ve vida mengeneleri 82.05’te, freze testereler ve dişsiz testere ağızları dahil her tür testere ağzı 82.02’dedir. "
  "Sapsız soketi 82.07’deki değişebilen aletlerle karıştırmamak gerekir; 82.04 metni bunları ismen kapsar.",
  "82.02–82.05 pozisyon metinleri.")

# 39
q(34, OL, "B",
  "Aşağıdakilerden hangisi 34.06 pozisyonunda <b>sınıflandırılmaz</b>?",
  "Sapları mumla kaplı fitilden yapılmış mumlu kibrit",
  ["Su üstünde yüzebilecek şekilde yapılmış gece kandili", "Boyanmış ve süslenmiş stearin mum",
   "Top veya halka şeklindeki ince mum", "Parafinden yapılmış, parfümlenmiş fitilli mum"],
  "34.06 Açıklama Notu, ışık temini için kullanılan her türlü mumu (top veya halka şeklindeki ince mumlar dahil) boyanmış, parfümlenmiş veya süslenmiş olsun olmasın bu pozisyonda sayar; su üstünde yüzebilecek gece kandilleri de buraya dahildir. "
  "Aynı not, mumlu kibrit denilen ve sapları mumla kaplı fitilden mamul kibritleri pozisyon dışında bırakarak 36.05’e gönderir; astım için fitilli mumlar 30.04’e, kükürtle muamele edilmiş fitil ve mumlar 38.08’e gider. "
  "Tuzak, ürünün mum içermesini tek başına yeterli saymaktır.",
  "34.06 Açıklama Notu.")

# 40
q(84, FN, "C",
  "Fasıl 84 Not 6’ya göre aşağıdaki birimlerden hangisi, Not 6(C)’nin (ii) ve (iii) bentlerinde belirtilen şartları yerine getirmesi halinde ayrı olarak sunulduğunda her durumda 84.71 pozisyonunda sınıflandırılır?",
  "Klavyeler",
  ["Yazıcılar", "Hoparlörler", "Televizyon yayınlarını alıcı tertibatı bulunmayan monitörler",
   "Kablolu veya kablosuz ağlarda veri alışverişi sağlayan cihazlar"],
  "Fasıl 84 Not 6(C)’nin son paragrafı, klavyelerin, X-Y koordinatlı giriş tertibatının ve (ii) ile (iii) bentlerindeki şartları yerine getiren diskli hafıza birimlerinin birim olarak daima 84.71’de sınıflandırılacağını belirtir. "
  "Not 6(D) ise yazıcıları, ağlarda ses, görüntü veya veri alışverişi sağlayan cihazları, hoparlör ve mikrofonları ve televizyon yayını alıcı tertibatı olmayan monitörleri, 6(C) şartlarını sağlasalar bile 84.71 dışında bırakır. "
  "Bilgisayara bağlanabilmek tek başına yeterli değildir.",
  "Fasıl 84 Not 6(C) ve 6(D).")

# 41
q(59, SE, "E",
  "Bir yapı malzemesi firması şu ürünü ithal etmektedir: jütten dokunmuş bir zemin mensucatın bir yüzü; okside edilmiş keten tohumu (bezir) yağı, reçine ve dolgu maddesi olarak mantar tozundan oluşan, boyayıcı pigment katılmamış bir hamur tabakasıyla tamamen kaplanmıştır. Ürün rulolar halindedir ve yer kaplaması olarak kullanılmaktadır. Tarife Cetveline göre bu ürün hangi pozisyonda sınıflandırılır?",
  "59.04", ["45.04", "59.03", "57.05", "59.07"],
  "59.04 Açıklama Notu linoleumu, okside edilmiş bezir yağı, reçine ve zamklarla dolgu maddelerinden (genellikle mantar tozu) oluşan bir hamur tabakasıyla kaplı, genellikle jütten bir zemin dokuması olarak tanımlar; pigment katılmamış ve mantar tozuyla yapılan türüne “mantarlı halı” denir ve not bunun 45.04’teki mensucat mesnetli aglomere mantar eşyasıyla karıştırılmaması gerektiğini vurgular. "
  "Kaplama maddesi plastik değil linoleum hamuru olduğundan ürün 59.03’e, tekstil yüzeyli bir halı olmadığından 57.05’e girmez; 59.07 ise başka yerde belirtilmeyen emdirilmiş veya kaplanmış mensucat içindir.",
  "59.04 Açıklama Notu; 45.04 Açıklama Notu.")

# 42
q(67, CC, "A",
  "Aşağıdakilerden hangileri 67.02 pozisyonunda sınıflandırılır?<br/>"
  "I. Ayrı olarak sunulan, kumaştan yapma çiçek taç yaprakları, çanak yaprakları ve sapları<br/>"
  "II. Üzeri kağıtla kaplanmış, yapma çiçeklerde sap olarak kullanılmak üzere yalnızca belirli boylarda kesilmiş teller<br/>"
  "III. Mercan gibi suda yaşayan hayvanların yumuşak gövde artıklarından özel olarak hazırlanıp boyanmış yapma yaprak ve dallar<br/>"
  "IV. Çocuklar için oyuncak olduğu açıkça belli olan yapma çiçekler",
  "I ve III", ["I ve II", "II ve IV", "I, III ve IV", "Yalnız III"],
  "67.02 Açıklama Notu, yapma çiçek, yapraklı dal ve meyvelerin aksamını (taç yaprakları, çanaklar, yapraklar, sap veya gövdeler) ve bryozoa veya hydrozoa (deniz anası, mercan gibi) cinsi hayvanların yumuşak gövde artıklarından özel olarak hazırlanıp boyanmış yapma yaprak ve dalları bu pozisyonda sayar. "
  "Aynı not, üzeri dokumaya elverişli madde veya kağıtla kaplanmış olup yalnızca belirli boylarda kesilmiş sap tellerini Bölüm XV’e, oyuncak veya karnaval eşyası olduğu açıkça belli olanları ise Fasıl 95’e gönderir.",
  "Fasıl 67 Not 1(e); 67.02 Açıklama Notu.")

# 43
q(92, GY, "C",
  "Gövdesinde ses kutusu bulunan; sapı, perdeleri ve akort mekanizması takılmış, ancak telleri ve köprüsü henüz takılmamış bir akustik gitar gümrüğe sunulmuştur. Eşyanın bu haliyle tamamlanmış gitarın ayırt edici niteliğine sahip olduğu tespit edilmiştir. Bu eşya hangi pozisyonda ve hangi Genel Yorum Kuralları uyarınca sınıflandırılır?",
  "92.02 – GYK 1 ve 2(a)",
  ["92.09 – GYK 1; tamamlanmamış alet, aksam sayılır", "92.07 – GYK 3(a); en özel tanım olarak",
   "92.09 – GYK 3(b); esas niteliği veren gövde nedeniyle", "44.20 – GYK 4; en çok benzeyen ahşap eşya olarak"],
  "GYK 2(a), bir eşyaya yapılan atfın, gümrüğe sunulduğunda tamamlanmış eşyanın ayırt edici niteliğine sahip olmak şartıyla aksamı tamamlanmamış halini de kapsadığını belirtir; eksik gitar bu nedenle telli müzik aletlerini kapsayan 92.02’de, pozisyon metni (GYK 1) ile birlikte uygulanan 2(a) uyarınca sınıflandırılır. "
  "92.09 ayrı sunulan aksam ve parçalar içindir; esas niteliği taşıyan eksik alet aksam sayılmaz. "
  "92.07 sesin elektrikle üretildiği veya yükseltildiği aletleri kapsar; ses kutusu bulunan akustik gitar bu kapsamda değildir.",
  "GYK 1; GYK 2(a) Açıklama Notu (I); 92.02 ve 92.09 pozisyon metinleri.")

# 44
q(85, EB, "D",
  "Aşağıdaki elektrikli eşya sınıflandırıldıkları pozisyonlarla eşleştirildiğinde hangi seçenek doğru olur?<br/>"
  "I. Kitap veya dergiye klipsle tutturulan, pille çalışan okuma lambası<br/>"
  "II. Bisiklete monte edilmek üzere düzenlenmiş, pille çalışan ön lamba<br/>"
  "III. Laboratuvarlarda kullanılan, rezistansla ısıtılan elektrikli fırın<br/>"
  "IV. Tabanca şeklinde saplı, fanlı saç kurutucu<br/>"
  "a) 85.16 · b) 85.13 · c) 85.12 · d) 85.14",
  "I-b, II-c, III-d, IV-a",
  ["I-c, II-b, III-d, IV-a", "I-b, II-c, III-a, IV-d", "I-d, II-c, III-b, IV-a", "I-b, II-d, III-c, IV-a"],
  "85.13 Açıklama Notu, kendi enerji kaynaklarıyla işleyen portatif lambalar arasında kitap veya dergiye klipsle tutturulan okuma lambalarını sayar; ancak 85.13 metni 85.12’deki aydınlatma cihazlarını hariç tutar ve 85.12 Açıklama Notu bisikletlere monte edilmek üzere düzenlenmiş pille çalışan lambaları da kapsar. "
  "Sanayi veya laboratuvarlarda kullanılan rezistansla ısıtılan fırınlar 85.14’te, tabanca şeklinde fanlı saç kurutucular ise berber işleri için elektrotermik cihazlar olarak 85.16’dadır. "
  "Tuzak, “pilli lamba” ortak özelliğine bakıp bisiklet lambasını da 85.13’e koymaktır.",
  "85.12, 85.13, 85.14 ve 85.16 pozisyon metinleri ve Açıklama Notları.")

# 45
q("GYK", GY, "B",
  "GYK 2(a) açıklama notuna göre aşağıdakilerden hangisi “son şeklini almamış eşya” sayılarak bitmiş eşya veya aksam ile aynı pozisyonda <b>değerlendirilmez</b>?",
  "Herhangi bir eşyanın yapımında kullanılabilecek, bitmiş eşyanın esas şeklini henüz almamış genel amaçlı metal çubuklar ve borular",
  ["Bir ucu kapalı, vida ağzı açılmış ve istenilen şekil ve boyutta şişeye genişletilebilecek tüp biçimli plastik şişe taslağı",
   "Bitmiş anahtarın yaklaşık şekli verilmiş, dişleri henüz açılmamış ve yalnızca anahtara dönüştürülebilecek anahtar taslağı",
   "Kenarları yuvarlatılmış ve tıpa olarak kullanılacağı ayırt edilebilen tabii mantar tıpa taslağı",
   "Bitmiş aksamın yaklaşık şekline sahip, doğrudan kullanıma hazır olmayan ve istisnai haller dışında yalnızca o aksamın tamamlanmasında kullanılabilen parça"],
  "GYK 2(a) Açıklama Notu (II), “son şeklini almamış eşya” tabirini doğrudan kullanıma hazır olmayan, bitirilmiş eşya veya aksamın yaklaşık şekil veya taslağına sahip ve istisnai haller dışında yalnızca onun tamamlanması için kullanılabilecek eşya olarak tanımlar ve vida ağzı açılmış plastik şişe taslaklarını örnek verir. "
  "Aynı not, bitirilmiş eşyanın esas şeklini henüz almamış çubuk, disk, boru gibi yarı mamullerin son şeklini almamış eşya olarak mütalaa edilmeyeceğini açıkça belirtir. "
  "Anahtar ve yuvarlak kenarlı mantar tıpa taslakları ise bitmiş eşyanın yaklaşık şekline sahip olduğundan ilgili pozisyonlarda (83.01, 45.03) yer alır.",
  "GYK 2(a) Açıklama Notu (II).")

# 46
q(85, FN, "E",
  "Fasıl 85 Not 12’ye göre “hibrit entegre devreler” aşağıdakilerden hangisidir?",
  "Pasif elemanları ince veya kalın film tekniğiyle, aktif elemanları yarı iletken tekniğiyle elde edilip yalıtkan yekpare bir zemin üzerinde ayrılmayacak şekilde birleştirilmiş devreler",
  ["Bütün devre elemanları yarı iletken bir maddenin kütlesi içinde ve yüzeyinde ayrılmaz bir bütün olarak meydana getirilmiş devreler",
   "Başka bir aktif veya pasif eleman içermeksizin iki veya daha fazla monolitik entegre devrenin bir araya getirilmesinden oluşan devreler",
   "Yalıtıcı bir zemin üzerinde baskı işlemiyle elde edilmiş bağlantı elemanları ve pasif elemanlardan oluşan devreler",
   "Silikon temelli sensör veya aktüatörlerle monolitik devrelerin tek bir gövdede birleştirildiği, devre kartına monte edilecek bileşenler"],
  "Fasıl 85 Not 12, hibrit entegre devreleri pasif elemanları (dirençler, kapasitörler, ara bağlantılar vb.) ince veya kalın film tekniğiyle, aktif elemanları (diyot, transistör, monolitik entegre devre vb.) yarı iletken tekniğiyle elde edilip yalıtkan yekpare bir zemin (cam, seramik vb.) üzerinde ayrılmayacak şekilde birleştirilmiş devreler olarak tanımlar. "
  "Elemanların tamamının yarı iletken kütlede oluşturulduğu tanım monolitik devrelere, birden çok monolitik devrenin birleşimi çoklu çiplere, sensör veya aktüatör içeren tek gövdeli bileşenler ise çok komponentli entegre devrelere aittir. "
  "Yalnızca baskı işlemiyle elde edilen devreler Not 8 uyarınca 85.34’teki baskılı devrelerdir.",
  "Fasıl 85 Not 8 ve Not 12.")

# 47
q(84, SE, "B",
  "Bir matbaa şu makineyi ithal etmektedir: ciltlenecek kitapların formalarını iplikle diken; formaları dikiş kısmına veren besleyici bir tertibat ile dikişin üzerine mensucattan bir takviye maddesi geçiren tertibatı bulunan makine. Tarife Cetveline göre bu makine hangi pozisyonda sınıflandırılır?",
  "84.40", ["84.52", "84.41", "84.43", "84.79"],
  "84.40 pozisyonu cilt makinalarını ve kitap formalarını dikmeye mahsus makinaları kapsar; açıklama notu ciltçiliğe mahsus dikiş makinalarını ve formaları dikiş kısmına veren besleyici tertibat ile dikişin üzerine mensucattan takviye maddesi geçiren tertibatı bulunan komplike makinaları bu pozisyonda sayar. "
  "84.52 pozisyon metni dikiş makinalarını kapsamakla birlikte 84.40’taki kitap dikme makinalarını açıkça hariç tutar. "
  "84.41 kağıt hamuru, kağıt veya karton işleyen diğer makineler, 84.43 baskı makineleri içindir; özel pozisyon bulunduğundan 84.79 da uygulanmaz.",
  "84.40 pozisyon metni ve Açıklama Notu; 84.52 pozisyon metni.")

# 48
q(93, CC, "A",
  "Aşağıdakilerden hangileri 93.03 pozisyonunda sınıflandırılır?<br/>"
  "I. Gemi bordasında veya cankurtaran merkezlerinde bulunan, can kurtarma ve iletişim amacıyla kullanılan palamar atan tüfek<br/>"
  "II. Bulutları yağmura çevirmek için kullanılan, sac levhadan kesik koni şeklindeki “yağmur topu”<br/>"
  "III. Kuşlara ve zararlı böceklere atış yapmak için tasarlanmış sapan<br/>"
  "IV. Herhangi bir fişeği atamayan, ağızdan kara barutla doldurulan tüfek",
  "I, II ve IV", ["I ve II", "II ve III", "I, III ve IV", "III ve IV"],
  "93.03 pozisyonu bir patlayıcının itiş gücüyle çalışan diğer ateşli silahları ve benzeri cihazları kapsar; açıklama notu bu pozisyonda palamar atan tüfekleri, bulutların yağmura çevrilmesinde kullanılan yağmur toplarını ve herhangi bir fişeği atamayan ağızdan doldurulan (kara barutlu) ateşli silahları açıkça sayar. "
  "Sapanlar ise patlayıcı ile çalışmadığından 93.04 Açıklama Notunda diğer silahlar arasında yer alır; oyuncak sapanlar da 95.03’e gider.",
  "93.03 ve 93.04 Açıklama Notları.")

# 49
q(85, SE, "D",
  "Bir elektronik kart üreticisi şu makineyi ithal etmektedir: ısıyı elektrik kaynağı kullanarak endüksiyon yoluyla üreten, lehim telini otomatik olarak besleyen bir sistemle donatılmış ve bu özel tertibatı nedeniyle yalnızca ve esas olarak lehim işinde kullanılacağı anlaşılan bir makine. Tarife Cetveline göre bu makine hangi pozisyonda sınıflandırılır?",
  "85.15", ["85.14", "84.68", "84.79", "85.43"],
  "85.15 Açıklama Notu, lehim makina ve cihazlarında ısının elektrik kaynağı kullanılarak endüksiyon veya kondüksiyon yoluyla üretildiğini belirtir ve bu gruba yalnızca kendi özel tertibatları (örneğin lehim teli için besleyici bir sistem) nedeniyle yalnızca ve esas olarak lehim için kullanılacağı anlaşılan makineleri dahil eder. "
  "Bu özelliği taşımayan benzeri makineler 85.14 anlamında ocak, fırın veya ısıtma cihazı sayılır; 84.68 ise 85.15’tekiler hariç lehim ve kaynak makinelerini kapsadığından burada uygulanmaz. "
  "Bu nedenle lehim teli besleme sistemi belirleyici unsurdur.",
  "85.15 Açıklama Notu; 84.68 pozisyon metni.")

# 50
q(88, SE, "C",
  "Bir reklam ajansı şu taşıtı ithal etmektedir: helyumla doldurulmuş, havadan hafif; elektrik motorlu pervanelerle hareket eden, içinde pilot bulunmayan ve yerden uzaktan kumanda edilen, gövdesinde reklam panoları taşıyan bir hava gemisi (zeplin). Tarife Cetveline göre bu taşıt hangi pozisyonda sınıflandırılır?",
  "88.01", ["88.06", "88.02", "88.07", "95.03"],
  "88.01 pozisyon metni balonları ve hava gemilerini ismen sayar; açıklama notu bu grubun reklam dahil çeşitli amaçlarla kullanılan havadan hafif taşıtları ve motorla işleyen hava gemilerini kapsadığını belirtir. "
  "Fasıl 88 Not 1, “insansız hava taşıtı” tabirini 88.01 pozisyonunda yer alanlar dışındaki pilotsuz hava araçları olarak tanımladığından taşıtın pilotsuz olması onu 88.06’ya götürmez. "
  "Motorlu olması da 88.02’yi gerektirmez; 88.02’ye giden motorlu planörlerle karıştırılmamalıdır.",
  "Fasıl 88 Not 1; 88.01 pozisyon metni ve Açıklama Notu.")


if __name__ == "__main__":
    assert len(SORULAR) == 50, len(SORULAR)
    json.dump({"tur": "deneme", "no": 6, "sorular": SORULAR},
              open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    from collections import Counter
    print("yazıldı:", OUT, Counter(s["cevap"] for s in SORULAR), Counter(s["tip"] for s in SORULAR))
