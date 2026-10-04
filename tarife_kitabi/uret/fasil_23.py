import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yardim_19_23 import S, kaydet  # noqa: E402

obj = {
    "tur": "fasil",
    "fasil": 23,
    "baslik": "Gıda sanayisinin kalıntı ve döküntüleri; hayvanlar için hazırlanmış kaba yemler",
    "bolum": "IV",
    "oz": {
        "vurgu": "Fasıl 23, gıda sanayiinden arta kalan bitkisel ve bazı hayvansal kalıntılarla hayvan yemi müstahzarlarını kapsar. Önce kalıntının kaynağı sorulur (hayvansal un, değirmencilik, nişasta-şeker-bira, yağ küspesi, şarap tortusu, diğer bitkisel artık); karıştırılmış, tatlandırılmış veya orijinal özelliğini kaybedecek kadar işlenmiş yem ise 23.09’dur.",
        "maddeler": [
            "İnsan tüketimine elverişsiz et, sakatat, balık ve su omurgasızı unları, kaba unları, pelletleri ile kıkırdaklar 23.01.",
            "Hububat ve baklagillerin kepek, kavuz ve diğer kalıntıları 23.02; nişastacılık, şeker, biracılık ve damıtık içki artıkları 23.03.",
            "Yağ ekstraksiyonundan kalan küspeler: soya 23.04, yer fıstığı 23.05, diğer bitkisel veya mikrobiyal yağlar 23.06; şarap tortusu ve ham tartar 23.07.",
            "Hayvan yemi olarak kullanılan, başka yerde yer almayan bitkisel madde ve artıklar 23.08; kedi-köpek maması, köpek bisküvisi, tam ve tamamlayıcı yemler, premiksler 23.09."
        ]
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "İnsan tüketimine elverişsiz et, sakatat, balık veya su omurgasızı unu, kaba unu, pelleti ya da kıkırdak mı?", "<b>23.01</b> (böcek unu <b>05.11</b>)"],
            ["2", "Hububat veya baklagillerin öğütülmesi, elenmesi, işlenmesinden kalan kepek, kavuz, kalıntı mı?", "<b>23.02</b> (harman kapçığı <b>12.13</b>)"],
            ["3", "Nişastacılık, şeker pancarı veya kamışı, biracılık ya da damıtık içki artığı mı?", "<b>23.03</b> (melas <b>17.03</b>)"],
            ["4", "Bitkisel veya mikrobiyal yağ ekstraksiyonundan kalan küspe mi?", "Soya <b>23.04</b> · yer fıstığı <b>23.05</b> · diğer <b>23.06</b> (yağ tortusu <b>15.22</b>)"],
            ["5", "Şarap tortusu veya ham tartar mı?", "<b>23.07</b> (krem tartar <b>29.18</b>)"],
            ["6", "Hayvan yemi olarak kullanılan, başka yerde yer almayan bitkisel madde, döküntü veya yan ürün mü?", "<b>23.08</b>"],
            ["7", "Hayvan beslemek için hazırlanmış müstahzar mı? (tatlandırılmış yem, tam veya tamamlayıcı yem, premiks, mama, köpek bisküvisi)", "<b>23.09</b>*"]
        ],
        "dipnot": "* Tek bir maddeden veya tek bir pozisyondaki maddelerin karışımından, ağırlıkça %3’ü geçmeyen bağlayıcıyla yapılan pelletler 23.09’a değil, maddenin kendi pozisyonuna (07.14, 12.14, 23.01 vb.) girer. Hem insan hem hayvan beslemesine uygun müstahzarlar 19.01 veya 21.06’dadır."
    },
    "pozisyon_haritasi": [
        ["23.01", "İnsana elverişsiz et, sakatat, balık, su omurgasızı unları ve pelletleri; kıkırdaklar", "Yenmezlik; kıkırdak yenilebilir olsa da burada", "Yem amaçlı balık unu, et unu, kıkırdak"],
        ["23.02", "Hububat ve baklagillerin kepek, kavuz ve kalıntıları", "Fasıl 11 Not 2(A) nişasta-kül şartını sağlamayanlar", "Buğday kepeği, pirinç perikarpı, silo temizleme artığı"],
        ["23.03", "Nişastacılık, şeker, biracılık ve damıtık içki artıkları", "Yaş veya kuru; pellet olabilir; melas hariç", "Şeker pancarı küspesi, bagas, bira posası, malt filizi"],
        ["23.04", "Soya yağı ekstraksiyonu küspesi ve katı artıkları", "İnsana uygun yağsız soya unu dahil; tekstüre hariç", "Soya küspesi, yağsız soya unu"],
        ["23.05", "Yer fıstığı yağı ekstraksiyonu küspesi ve katı artıkları", "23.04 notu kıyasen uygulanır", "Yer fıstığı küspesi"],
        ["23.06", "Diğer bitkisel veya mikrobiyal yağ küspeleri", "Yağlı tohum, meyve, hububat rüşeymi; yağı alınmış pirinç kepeği", "Ayçiçeği, pamuk tohumu, keten tohumu, kopra küspesi"],
        ["23.07", "Şarap tortusu; ham tartar", "Yıkanmış ham tartar dahil; krem tartar hariç", "Kurutulmuş şarap tortusu, ham tartar"],
        ["23.08", "Hayvan yemi olarak kullanılan bitkisel maddeler ve artıklar (başka yerde yer almayan)", "Başka yerde daha özel yer almamak", "Meşe palamudu, at kestanesi, mısır koçanı, meyve posası"],
        ["23.09", "Hayvan gıdası olarak kullanılan müstahzarlar", "Karışım, tatlandırma veya özellik kaybettiren işlem", "Kedi-köpek maması, köpek bisküvisi, premiks, melaslı yem"]
    ],
    "notlar": [
        ["Bölüm IV Notu", "Bu bölümde “pellet”: doğrudan sıkıştırma suretiyle veya ağırlığının <b>%3’ünü</b> geçmeyecek oranda bağlayıcı ilavesiyle küçük topaklar halinde bir araya getirilen ürünler."],
        ["Fasıl 23 Not 1", "Bitki döküntüleri, bitki kalıntıları ve bu işlemlerin yan ürünleri dışında; bitkisel veya hayvansal maddelerin ana maddenin <b>esas özelliklerini kaybettirecek</b> derecede işlenmesiyle elde edilen, başka yerde yer almayan ve hayvan gıdası olarak kullanılmaya elverişli ürünler 23.09’dadır."],
        ["Genel Açıklamalar", "Ürünlerin bazıları insan tüketimine uygun olsa da esas kullanımları hayvan beslenmesidir; şarap tortusu, ham tartar ve yağlı tohum küspeleri sanayide de kullanılır. Fasıldaki “pellet”: doğrudan sıkıştırma veya ağırlıkça <b>%3’ten fazla olmamak</b> şartıyla bağlayıcı (melas, nişastalı madde vb.) ilavesiyle aglomere edilen ürünler."],
        ["23.01 Açıklama Notu", "Kemik, boynuz, kabuk gibi uzuvlar hariç olmak üzere bütün hayvanların (kümes hayvanları, deniz memelileri, balıklar, su omurgasızları) veya et, sakatat gibi ürünlerin işlenmesiyle elde edilen, insana elverişsiz un ve kaba unlar ve bunların pelletleri; gübre olarak da kullanılabilir. Kıkırdaklar (domuz veya diğer hayvan yağlarının eritilmesinden kalan zarsı dokular) insan gıdasına elverişli olsalar da buradadır. İnsana elverişsiz böcek unları 05.11."],
        ["23.02 Açıklama Notu", "Kepek, kavuz ve diğer kalıntılar; Fasıl 11 Not 2(A)’daki kül ve nişasta şartlarına uymayan öğütme yan ürünleridir. Eleme kalıntıları, silo ve gemi temizleme artıkları, pirinç perikarpı, kabuk soyma ve dilimleme kalıntıları, şartlara uymayan öğütülmüş mısır koçanı ve baklagil kalıntıları dahildir. Harmanın dövülmesinden çıkan kapçıklar 12.13; yağ küspeleri 23.04–23.06."],
        ["23.03 Açıklama Notu", "Nişasta artıkları, yaş veya kuru şeker pancarı küspesi, şeker kamışı bagası, tasfiye köpükleri, bira posası, malt filizleri, şerbetçi otu döküntüleri, damıtık içki posaları ve pancar tortusu. Melas katılarak veya başka şekilde hayvan gıdası olarak hazırlanmış pancar küspesi 23.09. Hariç: melas (17.03), cansız mayalar (21.02), ham potasyum tuzları (26.21), bagas hamuru (47.06)."],
        ["23.04 Açıklama Notu", "Soya yağının presleme, çözücü veya santrifüjle ekstraksiyonundan kalan küspe ve katı artıklar; kalıp, kaba un veya pellet halinde olabilir. İnsan tüketimine uygun, yapısı değişmemiş yağsız soya unu da buradadır. Hariç: yağ tortuları (15.22); soya protein konsantresi ve tekstüre soya unu (21.06). 23.05 için bu not kıyasen uygulanır."],
        ["23.06 Açıklama Notu", "Soya ve yer fıstığı dışındaki yağlı tohum, yağlı meyve, hububat rüşeymi ve mikrobiyal yağ küspeleri; yağı ayrıştırılmış pirinç kepeği ve insana uygun yağsız unlar dahil. Kastor küspesi yem olarak değil gübre olarak, acı badem ve hardal küspesi uçucu yağ üretiminde kullanılır. Yağ tortuları 15.22."],
        ["23.07 Açıklama Notu", "Şarap tortusu: fermentasyon ve olgunlaşma sırasında kaplarda biriken çamur kıvamındaki artık (preslenmiş, kurutulmuş). Ham tartar: teknelerde veya fıçılarda katılaşan madde; yıkanmış ham tartar dahil. Krem tartar 29.18; kalsiyum tartarat 29.18 veya 38.24."],
        ["23.08 Açıklama Notu", "Meşe palamudu, at kestanesi; tanesi alınmış mısır koçanı, mısır sapları ve yaprakları; pancar ve havuç başları; sebze kabukları; meyve artıkları ve pektin çıkarmada kullanılsa da meyve posası; hardal tohumu ezme kalıntıları; kahve ikamesi hazırlama artıkları; “turunçgil melası”; hidrolize mısır koçanı kalıntıları."],
        ["23.09 Açıklama Notu", "Tatlandırılmış yemler (melas genellikle ağırlıkça <b>%10’dan fazla</b>), tam yemler, tamamlayıcı yemler ve premiksler; işlemin bitkinin hücresel yapısını mikroskopta tanınamaz hale getirdiği ürünler. Dahil: bir öğünlük konserve kedi-köpek maması, köpek bisküvisi, köpekler için kakaolu olsun olmasın tatlı müstahzarlar, kuş ve balık yemleri, genellikle %8–16 antibiyotik içeren kurutulmuş fermentasyon ürünleri."],
        ["23.09 Açıklama Notu", "Hariç: tek maddeden %3’e kadar bağlayıcılı pelletler (07.14, 12.14, 23.01 vb.); hububat tanelerinin (Fasıl 10) veya unlarının (Fasıl 11) basit karışımları; hem hayvan hem insan beslenmesine uygun müstahzarlar (19.01, 21.06); 23.08 artıkları; vitaminler (29.36); ilaçlar; Fasıl 35 proteinleri; antimikrobiyal dezenfektanlar (38.08); genellikle %70’i geçmeyen antibiyotikli ara ürünler (38.24)."]
    ],
    "sinir_komsulari": [
        ["İnsan tüketimine uygun et unu / balık unu", "02.10 / 03.09", "23.01 yalnız elverişsiz olanları alır"],
        ["İnsan tüketimine elverişsiz böcek unları", "05.11", "23.01 hariç tutması"],
        ["Harmanın dövülmesinden çıkan hububat kapçıkları", "12.13", "23.02 hariç tutması"],
        ["Tek başına kuş yemi tanesi; hububat tanelerinin basit karışımı", "10.08 / Fasıl 10", "Kuşlar için hazırlanmış karışık yem 23.09"],
        ["Tek maddeden %3’e kadar bağlayıcılı yonca pelleti", "12.14", "23.09 hariç tutması"],
        ["Şeker ekstraksiyonu veya rafinajından melas", "17.03", "23.03 hariç tutması"],
        ["Cansız (aktif olmayan) mayalar", "21.02", "23.03 hariç tutması"],
        ["Pancar melası tortusundan ham potasyum tuzları; bagas hamuru", "26.21 / 47.06", "23.03 hariç tutmaları"],
        ["Sıvı yağ tortuları (degra)", "15.22", "23.04–23.06 hariç tutması"],
        ["Soya protein konsantresi, tekstüre soya unu", "21.06", "23.04 hariç tutması"],
        ["Krem tartar; kalsiyum tartarat", "29.18 / 38.24", "23.07 hariç tutması"],
        ["Hem insan hem hayvan beslemesine uygun müstahzarlar", "19.01 / 21.06", "23.09 hariç tutması"],
        ["Vitaminler (stabilize edilmiş olsa da)", "29.36", "23.09 hariç tutması"],
        ["Antimikrobiyal dezenfektan; %70’e kadar antibiyotikli ara ürün", "38.08 / 38.24", "23.09 hariç tutmaları"],
        ["İnsan için bisküvi (köpek bisküvisi değil)", "19.05", "Fasıl 19 Not 1(b)"]
    ],
    "tuzaklar": [
        "<b>Yenilebilirlik 23.01’in anahtarıdır.</b> İnsan tüketimine uygun et unu 02.10’da, balık unu 03.09’da; elverişsiz olanlar 23.01’de. Kıkırdaklar ise insan gıdasına elverişli olsalar da 23.01’dedir.",
        "<b>Böcek unu 23.01’de değildir.</b> İnsan tüketimine elverişsiz böcek unları ve kaba unları 05.11’dedir.",
        "<b>Kepek ile un arasındaki çizgiyi nişasta ve kül çizer.</b> Fasıl 11 Not 2(A)’daki nişasta ve kül şartlarını sağlamayan öğütme ürünleri 23.02’dedir; elek oranları ise yalnız Fasıl 11 içindeki pozisyonları ayırır. Harmandan çıkan kapçıklar 12.13.",
        "<b>Şeker pancarı küspesi melaslanınca 23.09’a geçer.</b> Yaş veya kuru küspe 23.03; hayvan gıdası olarak hazırlanmak için melas katılmışsa 23.09. Melasın kendisi 17.03.",
        "<b>Küspe ile yağ tortusu farklıdır.</b> Ekstraksiyondan kalan katı küspe 23.04–23.06; sıvı yağ tortuları (degra) 15.22.",
        "<b>Soya üç pozisyona dağılır.</b> Yağsız soya unu (insana uygun olsa da) 23.04; protein konsantresi ve tekstüre soya unu 21.06; protein izolatları 35.04.",
        "<b>Kedi-köpek maması et içse de Fasıl 16 değildir.</b> Hayvan beslemek için hazırlanmış et esaslı müstahzarlar 23.09’dadır; köpekler için kakaolu tatlı müstahzarlar da 23.09.",
        "<b>%3 bağlayıcı kuralı.</b> Tek maddeden (veya tek pozisyondaki maddelerden) en çok %3 bağlayıcıyla yapılan pelletler 23.09 değil, maddenin kendi pozisyonundadır (07.14, 12.14, 23.01 vb.).",
        "<b>Antibiyotikli üründe oran belirleyicidir.</b> Fermentasyon fıçısı içeriğinin kurutulmasıyla elde edilen, genellikle %8–16 antibiyotikli premiks esası 23.09; antibiyotik üretiminin ara ürünü olan, genellikle %70’i geçmeyen antibiyotikli ürünler 38.24.",
        "<b>Meyve posası pektin için kullanılsa da 23.08’dir.</b> Üzüm, elma, armut ve turunçgillerin preslenmesinden kalan posa ve kabuklar 23.08’de kalır."
    ],
    "hafiza": {
        "kanca": "ET – KEPEK – POSA – SOYA – FISTIK – KÜSPE – TORTU – BİTKİ – MAMA",
        "aciklama": "<b>Et</b>-balık unu 23.01 · <b>Kepek</b> 23.02 · nişasta-şeker-bira <b>posa</b>sı 23.03 · <b>Soya</b> küspesi 23.04 · yer <b>fıstığı</b> küspesi 23.05 · diğer <b>küspe</b>ler 23.06 · şarap <b>tortu</b>su 23.07 · <b>bitki</b>sel artıklar 23.08 · <b>mama</b> ve yem müstahzarları 23.09. Görsel: bir fabrika turunda mezbahadan değirmene, şeker fabrikasından yağ fabrikasına, şaraphaneden bahçeye geçip yem karma tesisinde bitirin."
    },
    "sinav_odagi": [
        "Bu fasıl çıkmış sorularda daha çok seçeneklerde ve çeldirici olarak yer almıştır.",
        "Kayak merkezinde kullanılacak tabii kar sorusunda 23.03 (nişastacılık, şeker ve biracılık artıkları) çeldirici seçenek olarak verilmiştir; doğru cevap 22.01’dir.",
        "Bölüm kapsamı sorularında şarap tortusunun (23.07) Bölüm IV eşyası olarak şekerleme ve tütünle birlikte sayılması.",
        "Adı “yem” çağrıştıran ürünlerin yeri: tek başına kuş yemi tanesi hububat faslında (10.08), kuşlar için hazırlanmış karışık yemler ise 23.09’dadır; yem bitkileri (fiğ, yonca) 12.14’tedir."
    ],
    "cikmis_ornekler": [
        {
            "soru": "Tarife Cetveline göre kayak merkezinde kullanılmak için ithal edilen tabii kar hangi tarife pozisyonundadır?",
            "secenekler": ["22.01", "25.01", "95.06", "23.03"],
            "cevap": "A",
            "aciklama": "22.01 Açıklama Notuna göre “buz ve kar” tabii kar ve buz ile suni dondurulmuş suyu kapsar; kullanım yeri sonucu değiştirmez. Çeldirici 23.03 ise nişastacılık, şeker pancarı, biracılık ve damıtık içki artıklarının pozisyonudur ve kar ile ilgisi yoktur."
        }
    ],
    "ozet": [
        "İnsana elverişsiz hayvansal unlar, pelletler ve kıkırdaklar 23.01; böcek unu 05.11.",
        "Kepek ve değirmencilik kalıntıları 23.02; nişasta, şeker, bira ve damıtık içki artıkları 23.03.",
        "Küspeler: soya 23.04, yer fıstığı 23.05, diğerleri 23.06; yağ tortusu 15.22.",
        "Şarap tortusu ve ham tartar 23.07; krem tartar 29.18.",
        "Yem olarak kullanılan bitkisel artıklar 23.08; hazırlanmış yemler, mamalar ve premiksler 23.09.",
        "Pellet: doğrudan sıkıştırma veya en çok %3 bağlayıcı; tek maddeden pellet kendi pozisyonunda kalır."
    ],
    "sorular": []
}

Q = obj["sorular"]

# 1
Q.append(S("E4",
    "Tarife Cetveline göre, şeker pancarının yapısındaki şekerin ekstraksiyonundan sonra kalan, herhangi bir katkı içermeyen kurutulmuş şeker pancarı küspesi hangi pozisyonda sınıflandırılır?",
    ["23.03", "23.09", "17.03", "12.12", "23.08"], "A",
    "23.03 Açıklama Notuna göre şeker pancarı küspesi, şeker ekstraksiyonundan sonra kalan artıktır ve yaş veya kuru olsun bu pozisyondadır. Hayvan gıdası olarak hazırlanmak için melas katılmış olsaydı 23.09’a girerdi; melasın kendisi 17.03, şeker pancarının kendisi 12.12’dedir.",
    "23.03 Açıklama Notu."))
# 2
Q.append(S("OT",
    "Aşağıdakilerden hangisi Tarife Cetvelinin 23.09 pozisyonunda <b>sınıflandırılmaz</b>?",
    ["Hava geçirmez kutuda, et ve sakatattan bir öğünlük kedi maması",
     "Un ve don yağı karışımından yapılmış köpek bisküvisi",
     "Yalnız köpeklerin yemesi için hazırlanmış kakaolu tatlı müstahzar",
     "Melasla tatlandırılmış saman ve buğday kepeği karışımı",
     "Yalnız yoncadan, ağırlıkça %2 melas bağlayıcıyla yapılmış pellet"], "E",
    "23.09 Açıklama Notu, tek bir maddeden yapılmış ve ağırlıkça %3’ü geçmeyen bağlayıcı ilave edilmiş pelletleri hariç tutar; yonca pelleti 12.14’te kalır. Konserve kedi maması, köpek bisküvisi, köpekler için kakaolu tatlı müstahzarlar ve melasla tatlandırılmış yemler 23.09’da sayılmıştır.",
    "23.09 Açıklama Notu; Bölüm IV Notu."))
# 3
Q.append(S("TN",
    "Tarife Cetvelinin 23. Fasıl Genel Açıklamalarına göre, bu fasıldaki “pellet” tabiri için aşağıdakilerden hangisi <b>doğrudur</b>?",
    ["Bağlayıcı oranı ağırlıkça %10’u geçmeyen topaklardır.",
     "Yalnızca bağlayıcı ilavesiyle elde edilen topaklar pellet sayılır.",
     "Doğrudan sıkıştırma veya en çok %3 bağlayıcıyla aglomere edilen ürünlerdir.",
     "Bağlayıcı olarak yalnızca melas kullanılabilir, nişastalı madde kullanılamaz.",
     "Az miktarda bağlayıcı içeren topaklardır; bağlayıcı için oran verilmemiştir."], "C",
    "Fasıl 23 Genel Açıklamalarına ve Bölüm IV Notuna göre pellet, doğrudan sıkıştırma ile veya ağırlıkça %3’ü geçmeyen bir bağlayıcı (melas, nişastalı maddeler vb.) ilavesiyle aglomere edilen üründür. Oran vermeyen “az miktarda bağlayıcı” tanımı Fasıl 3 notuna aittir (E’deki tuzak).",
    "Bölüm IV Notu; Fasıl 23 Genel Açıklamalar."))
# 4
Q.append(S("FA",
    "Aşağıdakilerden hangisi diğerlerinden farklı bir tarife pozisyonunda sınıflandırılır?",
    ["Bira üretiminde etkisini yitirmiş malttan oluşan hububat posası",
     "Elma ve armudun preslenmesinden kalan meyve posası",
     "Çimlendirilmiş hububatın fırınlanması sırasında ayrılan malt filizleri",
     "Etkisini yitirmiş şerbetçi otu döküntüleri",
     "Pancar melasının damıtılmasından arta kalan pancar tortusu"], "B",
    "Elma, armut, üzüm, turunçgil gibi meyvelerin preslenmesinden elde edilen posa 23.08 Açıklama Notunda sayılmıştır. Hububat posası, malt filizleri, şerbetçi otu döküntüleri ve pancar tortusu biracılık ve damıtık içki sanayii artıkları olarak 23.03’tedir.",
    "23.03 ve 23.08 Açıklama Notları."))
# 5
Q.append(S("E4",
    "Tarife Cetveline göre, soya fasulyesi yağının çözücü ile ekstraksiyonundan sonra arta kalan ve pellet haline getirilmiş küspe hangi pozisyonda sınıflandırılır?",
    ["12.01", "23.06", "15.22", "23.04", "21.06"], "D",
    "23.04, soya fasulyesi yağının presleme, çözücü veya santrifüjle ekstraksiyonundan kalan küspe ve katı artıkları kapsar; bunlar kalıp, kaba un veya pellet halinde olabilir. 23.06 soya ve yer fıstığı dışındaki küspeler içindir; sıvı yağ tortuları 15.22’de, tekstüre soya unu 21.06’dadır.",
    "23.04 Açıklama Notu; Fasıl 23 Genel Açıklamalar (pellet)."))
# 6
Q.append(S("SN",
    "Bir ürün; tahıllar, yağlı tohum küspeleri, kalsiyum ve fosfor gibi mineraller, vitaminler ve iz elementler içermekte olup ineklere rasyonel ve dengeli bir günlük diyet sağlamak amacıyla formüle edilmiş ve pellet halinde sunulmaktadır. Bu ürün hangi pozisyonda sınıflandırılır?",
    ["23.06", "23.08", "23.09", "10.08", "29.36"], "C",
    "23.09 Açıklama Notu, hayvana rasyonel ve dengeli bir günlük diyet sağlayan, enerji veren, vücudu onarıcı (protein ve mineral) ve fonksiyonel (vitamin, iz element) besin maddelerini birlikte içeren “tam gıdaları” bu pozisyona alır. Bileşenlerden biri küspe veya vitamin olsa da karışım hazırlanmış yemdir.",
    "23.09 Açıklama Notu (tam gıdalar)."))
# 7
Q.append(S("OT",
    "Aşağıdakilerden hangisi Tarife Cetvelinin 23.08 pozisyonunda <b>yer almaz</b>?",
    ["Meşe palamudu ve at kestanesi",
     "Tanesi çıkarıldıktan sonra arta kalan mısır koçanı",
     "Pancar ve havuç başları (toprak üstünde kalan kısımlar)",
     "Bezelye ve bakla gibi sebzelerin tohum zarfları",
     "Harmanın dövülmesinden elde edilen hububat kapçıkları"], "E",
    "23.02 Açıklama Notu, harmanın dövülmesinden elde edilen hububat dış kabuklarının (kapçıklar) 12.13’te yer aldığını belirtir. Meşe palamudu, at kestanesi, tanesi alınmış mısır koçanı, pancar ve havuç başları ile sebze kabukları 23.08 Açıklama Notunda sayılmıştır.",
    "23.02 ve 23.08 Açıklama Notları."))
# 8
Q.append(S("TN",
    "Tarife Cetvelinin 23. Fasıl notuna göre, aşağıdakilerden hangisi 23.09 pozisyonunda yer alır?",
    ["Esas özelliğini kaybedecek ölçüde işlenmiş, başka yerde yer almayan yem ürünleri",
     "Hayvan gıdası olarak kullanılan bütün bitkisel döküntü, kalıntı ve yan ürünler",
     "İnsan tüketimine elverişsiz et, balık ve su omurgasızı unları ile kıkırdaklar",
     "Yağlı tohumların yağ ekstraksiyonundan arta kalan küspe ve diğer katı artıklar",
     "Hem insan hem hayvan beslenmesinde kullanılabilen bütün gıda müstahzarları"], "A",
    "Fasıl 23 Not 1’e göre bitki döküntüleri, kalıntıları ve yan ürünler dışında; bitkisel veya hayvansal maddelerin ana maddenin esas özelliklerini kaybettirecek derecede işlenmesiyle elde edilen, başka yerde yer almayan ve hayvan gıdası olarak kullanılan ürünler 23.09’dadır. Bitkisel döküntüler 23.08’de, hayvansal unlar 23.01’de, küspeler 23.04–23.06’da, her iki amaca uygun müstahzarlar 19.01 veya 21.06’dadır.",
    "Fasıl 23 Not 1; 23.09 Açıklama Notu."))
# 9
Q.append(S("FA",
    "Aşağıdaki seçeneklerin hangisinde sayılan eşyanın <b>tamamı</b> 23.06 pozisyonunda yer alır?",
    ["Ayçiçeği küspesi – soya küspesi – keten tohumu küspesi",
     "Pamuk tohumu küspesi – yer fıstığı küspesi – kopra küspesi",
     "Hardal küspesi – sıvı yağ tortusu (degra) – susam küspesi",
     "Yağı alınmış pirinç kepeği – kastor küspesi – ayçiçeği küspesi",
     "Keten tohumu küspesi – buğday kepeği – palm çekirdeği küspesi"], "D",
    "23.06 Açıklama Notu, yağı ayrıştırılmış pirinç kepeğini ve gübre olarak kullanılan kastor küspesini açıkça sayar; ayçiçeği küspesi de bu pozisyondadır. Soya küspesi 23.04’te, yer fıstığı küspesi 23.05’te, yağ tortusu 15.22’de, buğday kepeği 23.02’dedir.",
    "23.02, 23.04, 23.05, 23.06 Açıklama Notları."))
# 10
Q.append(S("E4",
    "Tarife Cetveline göre, domuz yağının eritilmesi sonucunda arta kalan ve insan gıdası olarak kullanılmaya elverişli olan zarsı dokular (kıkırdaklar) hangi pozisyonda sınıflandırılır?",
    ["02.09", "23.01", "16.02", "05.11", "15.01"], "B",
    "23.01 Açıklama Notu, domuz yağının veya diğer hayvan katı yağlarının eritilmesinden kalan zarsı dokuları (kıkırdakları) insan gıdası olarak kullanılmaya elverişli olsalar dahi bu pozisyona alır. Eritilmemiş domuz yağı 02.09’da, eritilmiş domuz yağı 15.01’dedir.",
    "23.01 Açıklama Notu (Kıkırdaklar)."))
# 11
Q.append(S("GYK",
    "Avustralya papağanları için tam yem olarak kullanılan; darı, kuş yemi, kabuklu yulaf ve keten tohumundan oluşan perakende ambalajlı müstahzar için hangi kural–pozisyon ikilisi doğrudur?",
    ["GYK 3(b) – 10.08", "GYK 3(c) – 12.04", "GYK 2(b) – 10.04", "GYK 1 – 23.09", "GYK 4 – 10.08"], "D",
    "23.09 pozisyon metni hayvan gıdası olarak kullanılan müstahzarları kapsar ve Açıklama Notu, Avustralya papağanları için esas veya tam yem olarak kullanılan darı, kuş yemi, kabuklu yulaf ve keten tohumundan oluşan müstahzarları açıkça sayar. Sonuç pozisyon metninden çıktığı için GYK 1 uygulanır; karışımın tohumlara göre 3(b) veya 3(c) ile ayrıştırılması gerekmez.",
    "GYK 1; 23.09 Açıklama Notu."))
# 12
Q.append(S("CC",
    "Tarife Cetveline göre aşağıdaki ifadelerden hangileri <b>doğrudur</b>? I. Şeker pancarı küspesi yaş veya kuru olsun 23.03 pozisyonunda yer alır. II. Hayvan gıdası olarak hazırlanmak maksadıyla melas katılmış şeker pancarı küspesi 23.09 pozisyonunda yer alır. III. Şekerin ekstraksiyonundan veya rafinajından arta kalan melas 23.03 pozisyonunda yer alır. IV. Şeker kamışı bagası hamuru (pulpu) 23.03 pozisyonunda yer alır.",
    ["I ve III", "I ve II", "II ve IV", "I, II ve III", "II, III ve IV"], "B",
    "23.03 Açıklama Notuna göre şeker pancarı küspesi yaş veya kuru olsun 23.03’tedir (I); melas katılmış veya başka şekilde hayvan gıdası olarak hazırlanmışsa 23.09’a girer (II). Aynı not melası 17.03’e (III yanlış), şeker kamışı bagası hamurunu 47.06’ya (IV yanlış) gönderir.",
    "23.03 Açıklama Notu."))
# 13
Q.append(S("ES",
    "Tarife Cetveline göre aşağıdaki eşya – pozisyon eşleştirmelerinden hangisi <b>yanlıştır</b>?",
    ["Ham tartar – 23.07", "Yer fıstığı küspesi – 23.05", "Malt filizleri – 23.03", "Meşe palamudu – 23.08", "Krem tartar – 23.07"], "E",
    "23.07 Açıklama Notu, ham tartar ve şarap tortusundan üretilen krem tartarı (potasyum bitartarat) bu pozisyondan hariç tutar ve 29.18’e gönderir. Ham tartar 23.07’de, yer fıstığı küspesi 23.05’te, malt filizleri 23.03’te, meşe palamudu 23.08’dedir.",
    "23.07 Açıklama Notu."))
# 14
Q.append(S("OT",
    "Aşağıdakilerden hangisi Tarife Cetvelinin 23.03 pozisyonunda <b>yer almaz</b>?",
    ["Mısırdan nişasta imalinden arta kalan lifli ve proteinli artıklar",
     "Şeker kamışının özsuyu çıkarıldıktan sonra kalan bagas",
     "Aktif olmayan, faaliyeti bitmiş cansız mayalar",
     "Şeker tasfiyesi sırasında ortaya çıkan köpükler",
     "Alkollü içki üretiminde damıtmadan arta kalan hububat posaları"], "C",
    "23.03 Açıklama Notu, aktif olmayan veya faaliyeti bitmiş cansız mayaları hariç tutar ve 21.02’ye gönderir. Nişasta artıkları, şeker kamışı bagası, şeker tasfiye köpükleri ve damıtık içki posaları 23.03’te sayılmıştır.",
    "23.03 Açıklama Notu; 21.02 Açıklama Notu."))
# 15
Q.append(S("TN",
    "Tarife Cetvelinin 23.02 pozisyonu Açıklama Notuna göre, hububatın öğütülmesinden elde edilen bir ürünün 11. Fasıl yerine 23.02 pozisyonunda sınıflandırılmasında hangi ölçütler esas alınır?",
    ["11. Fasıl 2(A) Notundaki nişasta ve kül içeriği şartları",
     "Ürünün protein ve yağ içeriği oranları",
     "Ürünün eleklerden geçme oranı ve tane büyüklüğü",
     "Ürünün hayvan yemi olarak kullanılıp kullanılmadığı",
     "Ürünün pellet halinde sunulup sunulmadığı"], "A",
    "23.02 Açıklama Notuna göre bu pozisyondaki kepek ve kalıntılar, kül ve nişasta içerikleri bakımından Fasıl 11 Not 2(A)’daki şartlara uymayan öğütme yan ürünleridir. Elekten geçme oranları (Not 2(B)) yalnız Fasıl 11 içindeki 11.01–11.02 ile 11.03–11.04 ayrımında kullanılır; pellet hali de pozisyonu değiştirmez.",
    "23.02 Açıklama Notu; Fasıl 11 Not 2(A)."))
# 16
Q.append(S("FA",
    "Aşağıdakilerden hangisi diğerlerinden farklı bir fasılda yer alır?",
    ["Yem amaçlı, insan tüketimine elverişsiz balık unu",
     "Kurutulmuş şarap tortusu",
     "Ayçiçeği tohumu küspesi",
     "İnsan tüketimine elverişsiz böceklerin unları",
     "Buğday öğütülmesinden elde edilen kepek"], "D",
    "23.01 Açıklama Notu, insan tüketimine uygun olmayan böceklerin unlarını ve kaba unlarını hariç tutar ve 05.11’e (Fasıl 5) gönderir. Yem amaçlı balık unu 23.01’de, şarap tortusu 23.07’de, ayçiçeği küspesi 23.06’da, buğday kepeği 23.02’de, yani Fasıl 23’tedir.",
    "23.01 Açıklama Notu."))
# 17
Q.append(S("E4",
    "Tarife Cetveline göre, şarabın fermentasyonu ve olgunlaşması sırasında kaplarda biriken çamur kıvamındaki artığın preslenip kurutulmasıyla elde edilen şarap tortusu hangi pozisyonda sınıflandırılır?",
    ["22.04", "29.18", "23.07", "23.08", "38.24"], "C",
    "23.07 Açıklama Notu şarap tortusunu, şarabın fermentasyonu ve olgunlaşması sırasında kaplarda biriken, preslenip filtreden geçirilerek katı hale getirilen ve kurutulmuş halde toz, granül veya parçacık şeklinde bulunan artık olarak tanımlar. Krem tartar 29.18’de, kalsiyum tartarat 29.18 veya 38.24’tedir.",
    "23.07 Açıklama Notu."))
# 18
Q.append(S("OT",
    "Aşağıdakilerden hangisi Tarife Cetvelinin 23. Faslında <b>sınıflandırılmaz</b>?",
    ["Antioksidanla stabil hale getirilmiş, yem katkısı olarak kullanılan vitamin",
     "Turunçgil suyu imalatındaki artık suların konsantre edilmesiyle elde edilen “turunçgil melası”",
     "Yoncadan ısı uygulanarak elde edilen yeşil konsantre protein yaprağı",
     "İnsan tüketimine uygun, yapısı değiştirilmemiş yağsız soya unu",
     "Fermentasyon fıçısı içeriğinin kurutulmasıyla elde edilen, %10 antibiyotikli premiks esası"], "A",
    "23.09 Açıklama Notu, antioksidan vb. ile stabil hale getirilmiş olsalar da (katkı miktarı muhafaza ve taşıma için gerekenden fazla değilse) vitaminleri hariç tutar ve 29.36’ya gönderir. Turunçgil melası 23.08’de, yoncadan protein konsantresi ve antibiyotikli premiks esası 23.09’da, yağsız soya unu 23.04’tedir.",
    "23.04, 23.08, 23.09 Açıklama Notları."))
# 19
Q.append(S("FA",
    "Aşağıdakilerden hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır?",
    ["Hava geçirmez kutuda bir öğünlük köpek maması",
     "Akvaryum balıkları için besleyici müstahzar",
     "Melasla tatlandırılmış sığır yemi",
     "Vitamin, amino asit ve taşıyıcı maddeden oluşan premiks",
     "Elma kabukları ve çekirdeklerinden oluşan meyve artığı"], "E",
    "Elma ve armut kabuk ve çekirdekleri gibi meyve artıkları 23.08 Açıklama Notunda bitkisel döküntü olarak sayılmıştır. Köpek maması, balık yemi, melaslı tatlandırılmış yem ve premiksler hayvan gıdası müstahzarı olarak 23.09’dadır.",
    "23.08 ve 23.09 Açıklama Notları."))
# 20
Q.append(S("GYK",
    "Hayvan gıdası olarak hazırlanmak maksadıyla melas katılmış şeker pancarı küspesi için aşağıdakilerden hangisi doğrudur?",
    ["GYK 2(b) uyarınca küspenin karışımı sayılarak 23.03’te kalır.",
     "GYK 1 ve 23.03 Açıklama Notu gereği 23.09’dadır.",
     "GYK 3(b) uyarınca asli niteliği melas verdiğinden 17.03’tedir.",
     "GYK 3(c) uyarınca numara sırasına göre son olan 23.09’dadır.",
     "GYK 4 uyarınca en çok benzediği şeker pancarı gibi 12.12’dedir."], "B",
    "23.03 Açıklama Notu, melas katılmış veya başka şekilde hayvan gıdası olarak hazırlanmış şeker pancarı küspesinin 23.09’a dahil olduğunu açıkça belirtir; sınıflandırma pozisyon metinleri ve notlarla (GYK 1) yapılır. GYK 2(b), katılan madde eşyanın asli karakterini değiştiriyorsa ve aksine hüküm varsa uygulanmaz; 3(c) ile aynı pozisyona ulaşmak ise yanlış gerekçedir.",
    "GYK 1; GYK 2(b) Açıklama Notu (X)–(XII); 23.03 Açıklama Notu."))
# 21
Q.append(S("TN",
    "Tarife Cetvelinin 23.09 pozisyonu Açıklama Notuna göre “tatlandırılmış hayvan gıdaları”nda melas veya benzeri tatlandırıcı maddelerin oranı genellikle ağırlıkça ne kadardır?",
    ["%3’ten fazla", "%10’dan fazla", "%20’den fazla", "%50’den fazla", "%5’ten az"], "B",
    "23.09 Açıklama Notu, tatlandırılmış hayvan gıdalarını melasın veya benzeri tatlandırıcı maddelerin (genellikle ağırlık olarak %10’dan fazla oranda) bir veya daha fazla besleyici maddeyle karışımı olarak tanımlar. %3 ise pellet tanımındaki bağlayıcı sınırıdır.",
    "23.09 Açıklama Notu (Tatlandırılmış hayvan gıdaları)."))
# 22
Q.append(S("CC",
    "Tarife Cetveline göre aşağıdakilerden hangileri 23.09 pozisyonu <b>dışında</b> kalır? I. Hububat tanelerinin basit karışımları II. Hem hayvan beslemede hem insan gıdası olarak kullanılabilen ve ambalaj ibareleri bakımından insan gıdasına da uygun müstahzarlar III. Kedi ve köpekler için et, sakatat ve katkı maddelerinden oluşan bir öğünlük konserve mama IV. Antibiyotik üretiminde filtrasyon ve ilk ekstraksiyon sırasında elde edilen, %70’i geçmeyen antibiyotikli ara ürünler",
    ["I ve III", "II ve III", "III ve IV", "I, II ve IV", "II, III ve IV"], "D",
    "23.09 Açıklama Notu; hububat tanelerinin basit karışımlarını Fasıl 10’a (I), hem hayvan hem insan beslenmesine uygun müstahzarları 19.01 veya 21.06’ya (II), %70’i geçmeyen antibiyotikli ara ürünleri 38.24’e (IV) gönderir. Bir öğünlük konserve kedi-köpek maması ise 23.09’da açıkça sayılmıştır (III).",
    "23.09 Açıklama Notu."))
# 23
Q.append(S("ES",
    "Tarife Cetveline göre; soya fasulyesi yağı ekstraksiyonundan kalan küspe (I), yer fıstığı yağı ekstraksiyonundan kalan küspe (II), ayçiçeği tohumu küspesi (III), sıvı yağ tortuları (degra) ise (IV) pozisyonunda sınıflandırılır. Boşlukları sırasıyla dolduran seçenek hangisidir?",
    ["23.04 / 23.06 / 23.06 / 15.22",
     "23.06 / 23.05 / 23.06 / 23.06",
     "23.04 / 23.05 / 23.06 / 15.22",
     "23.04 / 23.05 / 23.05 / 15.22",
     "23.04 / 23.05 / 23.06 / 23.08"], "C",
    "Soya küspesi 23.04’te, yer fıstığı küspesi 23.05’te, diğer bitkisel yağ küspeleri (ayçiçeği dahil) 23.06’dadır. 23.04–23.06 Açıklama Notları sıvı yağ tortularını (degra) hariç tutar ve 15.22’ye gönderir.",
    "23.04, 23.05, 23.06 Açıklama Notları."))
# 24
Q.append(S("SN",
    "Bir ürün; mısırdan nişasta üretimi sırasında mısırın ıslatılıp demlendirilmesiyle elde edilen likörlerin kalıntısıdır. Büyük ölçüde lifli ve proteinli unsurlardan oluşmakta, pellet halinde sunulmakta ve hayvan yemi olarak veya bazı antibiyotiklerin üretiminde kültür ortamı olarak kullanılmaktadır. Başka bir maddeyle karıştırılmamıştır. Bu ürün hangi pozisyonda sınıflandırılır?",
    ["23.09", "11.08", "38.24", "23.08", "23.03"], "E",
    "23.03 Açıklama Notu, mısır, pirinç, patates vb.den nişasta imalinden kalan, büyük ölçüde lifli ve proteinli artıkları ve mısırın ıslatılıp demlendirilmesiyle yapılan likörlerin kalıntılarını bu pozisyona alır; bunlar pellet halinde olabilir. Karıştırılmamış bir sanayi artığı olduğundan yem müstahzarı (23.09) sayılmaz; nişastanın kendisi 11.08’dedir.",
    "23.03 Açıklama Notu; Fasıl 23 Genel Açıklamalar."))
# 25
Q.append(S("E4",
    "Tarife Cetveline göre, pirinç tanesinin beyazlatılması ve parlatılması sırasında taneden ayrılan meyve kabuğu (perikarp) hangi pozisyonda sınıflandırılır?",
    ["23.02", "10.06", "12.13", "23.06", "23.08"], "A",
    "23.02 Açıklama Notu, pirinç tanesinin beyazlatılması ve parlatılması sırasında taneden ayrılan perikarpı hububat kalıntıları arasında sayar. Yağı ayrıştırılmış pirinç kepeği ise 23.06’dadır (yağ ekstraksiyonu artığı); harman kapçıkları 12.13’tedir.",
    "23.02 ve 23.06 Açıklama Notları."))

kaydet(obj, 23)
