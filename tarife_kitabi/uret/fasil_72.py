"""Fasıl 72 – Demir ve çelik modülü (Bölüm XV notları dahil)."""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yardim_70_72 import (ESYA, OLUMSUZ, FARKLI, TANIM, GYK, ESLES, COKLU, SENARYO,  # noqa: E402
                          soru, kaydet)

obj = {
    "tur": "fasil",
    "fasil": 72,
    "baslik": "Demir ve çelik",
    "bolum": "XV",
    "oz": {
        "vurgu": "Fasıl 72, demir ve çeliği ilk maddelerden (pik, ferro-alyaj, sünger demir, hurda, toz) başlayıp külçe, yarı mamul, yassı hadde, filmaşin, çubuk, profil ve tel aşamasına kadar kapsar; borular, kaynaklı profiller ve şekil verilmiş eşya Fasıl 73’tedir. Sınıflandırma üç eksende yapılır: çelik türü (alaşımsız, paslanmaz, diğer alaşımlı), ürünün şekli (Not 1 tanımları) ve yassı ürünlerde genişlik ile hadde-kaplama durumu.",
        "maddeler": [
            "Bölüm XV notları bütün adi metal fasıllarını yönetir: dışlamalar (Not 1), genel kullanıma mahsus aksam (Not 2), adi metal listesi (Not 3), alaşım (Not 5) ve karma eşya (Not 7) kuralları.",
            "Eşikler: pik demir %2’den fazla karbon; çelik %2 veya daha az karbon; paslanmaz çelik en çok %1,2 karbon ve en az %10,5 krom; diğer alaşımlı çelik Not 1(f)’deki eşiklerden birini aşan çelik.",
            "Pozisyon blokları: ilk maddeler 72.01–72.05; demir ve alaşımsız çelik 72.06–72.17; paslanmaz çelik 72.18–72.23; diğer alaşımlı çelik 72.24–72.29.",
            "Şekil tanımları: filmaşin sıcak haddelenmiş düzensiz kangal; tel soğuk elde edilmiş kangal; diğer çubuk kangal olmayan düz boy; yassı ürün dikdörtgen kesitli ve genişlik/kalınlık oranı tanımlı.",
            "Yassı ürünlerde 600 mm sınırı: 600 mm veya fazla sıcak 72.08, soğuk 72.09, kaplanmış 72.10; 600 mm’den az kaplanmamış 72.11, kaplanmış 72.12.",
        ],
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Bölüm XV Not 1 dışlaması mı? (makine XVI, taşıt XVII, mobilya 94, oyuncak 95, Fasıl 71 eşyası, ferro-seryum 36.06)", "İlgili fasıl"],
            ["2", "Demir cevheri veya konsantresi mi?", "<b>26.01</b>"],
            ["3", "%2’den fazla karbonlu, dövülemeyen pik demir ya da %6–30 manganezli aynalı demir mi?", "<b>72.01</b>"],
            ["4", "En az %4 demir içeren ve Not 1(c) eşiklerini aşan ferro-alyaj mı?", "<b>72.02</b>"],
            ["5", "Sünger demir veya en az %99,94 saflıkta demir (parça, pellet) mi?", "<b>72.03</b>"],
            ["6", "Döküntü, hurda veya hurdadan yeniden ergitilmiş külçe mi?", "<b>72.04</b>"],
            ["7", "Granül veya toz mu?", "<b>72.05</b> (ferro-alyaj tozu <b>72.02</b>)"],
            ["8", "Çelik türü hangisi?", "Alaşımsız <b>72.06</b>–<b>72.17</b> · paslanmaz <b>72.18</b>–<b>72.23</b> · diğer alaşımlı <b>72.24</b>–<b>72.29</b>"],
            ["9", "Külçe, ilk şekil veya yarı mamul mü?", "<b>72.06</b> / <b>72.07</b> (paslanmaz <b>72.18</b>, alaşımlı <b>72.24</b>)"],
            ["10", "Yassı hadde mamulü mü?", "600 mm veya fazla: sıcak <b>72.08</b>, soğuk <b>72.09</b>, kaplı <b>72.10</b> · 600 mm’den az: kaplamasız <b>72.11</b>, kaplı <b>72.12</b>"],
            ["11", "Filmaşin, çubuk, profil veya tel mi?", "<b>72.13</b> · sıcak çubuk <b>72.14</b> · diğer çubuk <b>72.15</b> · profil <b>72.16</b> · tel <b>72.17</b>"],
            ["12", "Boru, kaynaklı profil, palplanş, ray veya şekil verilmiş eşya mı?", "<b>Fasıl 73</b>*"],
        ],
        "dipnot": "* Fasıl 72 yalnız ham ve yarı işlenmiş ürünleri alır; döküm eşya, kaynakla birleştirilmiş profiller, demiryolu malzemesi, borular ve inşaat aksamı Fasıl 73’tedir. Satır 8–11 paslanmaz ve diğer alaşımlı çelik için aynı sırayla uygulanır.",
    },
    "pozisyon_haritasi": [
        ["72.01", "Dökme (pik) demir ve aynalı demir", "%2’den fazla karbon; dövülemez; ilk şekiller", "Pik külçe, aynalı demir"],
        ["72.02", "Ferro-alyajlar", "En az %4 demir; Not 1(c) eşikleri", "Ferro-krom, ferro-manganez, ferro-silisyum"],
        ["72.03", "Sünger demir; çok saf demir", "Doğrudan indirgeme; saflık en az %99,94", "Sünger demir pelleti"],
        ["72.04", "Döküntü ve hurdalar; hurda külçesi", "Kesinlikle kullanılmaz hale gelmiş", "Talaş, balyalanmış hurda"],
        ["72.05", "Granül ve tozlar", "Granül 1/5 mm elek ölçütü; toz 1 mm", "Çelik bilye kumu, demir tozu"],
        ["72.06", "Külçe ve ilk şekiller (alaşımsız)", "Kalıba dökülmüş; 72.03 demiri hariç", "Çelik külçe, pudla demir bloğu"],
        ["72.07", "Yarı mamuller (alaşımsız)", "Blum, kütük, kalın levha; sürekli döküm ürünleri", "Kütük, kaba dövme taslak"],
        ["72.08", "Yassı, 600 mm ve fazla, sıcak hadde", "Kaplanmamış; dekapaj ve kaba kaplama serbest", "Sıcak haddelenmiş rulo saç"],
        ["72.09", "Yassı, 600 mm ve fazla, soğuk hadde", "Kaplanmamış", "Soğuk haddelenmiş saç"],
        ["72.10", "Yassı, 600 mm ve fazla, kaplanmış", "Metal veya metal olmayan kaplama, plakaj", "Galvanizli saç, teneke, boyalı saç"],
        ["72.11", "Yassı, 600 mm’den az, kaplanmamış", "Sıcak veya soğuk; şerit ve çember", "Dar şerit, çember"],
        ["72.12", "Yassı, 600 mm’den az, kaplanmış", "Kalay, çinko, boya, plastik, plakaj", "Kalaylı dar şerit"],
        ["72.13", "Filmaşin (alaşımsız)", "Sıcak hadde; düzensiz kangal", "Kangal inşaat demiri, tel çubuk"],
        ["72.14", "Diğer çubuklar – sıcak (alaşımsız)", "Sadece dövme, sıcak hadde veya sıcak çekme", "Düz boy nervürlü inşaat demiri"],
        ["72.15", "Diğer çubuklar (alaşımsız)", "Soğuk işlenmiş veya daha ileri işlem görmüş", "Soğuk çekilmiş parlak çubuk"],
        ["72.16", "Profiller (alaşımsız)", "U, I, H, L, T vb.; kaynaklı profil hariç", "I profil, köşebent"],
        ["72.17", "Teller (alaşımsız)", "Soğuk elde edilmiş; kangal", "Galvanizli tel, bağ teli"],
        ["72.18", "Paslanmaz: külçe ve yarı mamul", "En az %10,5 krom, en çok %1,2 karbon", "Paslanmaz kütük, kalın levha"],
        ["72.19", "Paslanmaz yassı, 600 mm ve fazla", "Sıcak, soğuk veya kaplanmış", "Paslanmaz saç rulo"],
        ["72.20", "Paslanmaz yassı, 600 mm’den az", "Sıcak, soğuk veya diğer", "Paslanmaz şerit"],
        ["72.21", "Paslanmaz filmaşin", "Sıcak hadde; düzensiz kangal", "Paslanmaz tel çubuk"],
        ["72.22", "Paslanmaz çubuk ve profiller", "Kangal olmayan çubuk; profil", "Paslanmaz yuvarlak çubuk, köşebent"],
        ["72.23", "Paslanmaz teller", "Soğuk elde edilmiş; kangal", "Paslanmaz tel"],
        ["72.24", "Diğer alaşımlı: külçe ve yarı mamul", "Not 1(f) eşikleri", "Alaşımlı çelik kütük"],
        ["72.25", "Diğer alaşımlı yassı, 600 mm ve fazla", "Silisyumlu manyetik saç dahil", "Elektrik (silisli) saç"],
        ["72.26", "Diğer alaşımlı yassı, 600 mm’den az", "Yüksek hız çeliği şerit dahil", "Alaşımlı dar şerit"],
        ["72.27", "Diğer alaşımlı filmaşin", "Sıcak hadde; düzensiz kangal", "Alaşımlı tel çubuk"],
        ["72.28", "Diğer alaşımlı çubuk, profil; sondaj çubuğu", "İçi boş sondaj çubuğu alaşımsızda da burada", "Alaşımlı çubuk, sondaj çeliği"],
        ["72.29", "Diğer alaşımlı teller", "Soğuk elde edilmiş; kangal", "Siliko-manganez çelik tel"],
    ],
    "notlar": [
        ["Bölüm XV Not 1", "Bölüm dışı: esası metal toz veya pul olan müstahzar boya, mürekkep vb. (32.07–32.10, 32.12, 32.13, 32.15); ferro-seryum ve diğer piroforik alaşımlar (36.06); 65.06 veya 65.07 başlıkları ve parçaları; 66.03 şemsiye iskeletleri; Fasıl 71 eşyası (kıymetli metal alaşımları, kıymetli metal kaplama adi metaller, taklit mücevher); XVI. Bölüm (makine, mekanik ve elektrikli cihaz); birleştirilmiş demiryolu hatları (86.08) ve XVII. Bölüm taşıtları; XVIII. Bölüm alet ve cihazları (saat zemberekleri dahil); mühimmat olarak hazırlanmış kurşun saçma (93.06) ve XIX. Bölüm; Fasıl 94 (mobilya, lamba, prefabrik yapı); Fasıl 95 (oyuncak, spor); Fasıl 96 (el elekleri, düğmeler, kalemler, tripodlar vb.); Fasıl 97 (sanat eserleri)."],
        ["Bölüm XV Not 2", "“Genel kullanıma mahsus aksam ve parça” (tarifenin her yerinde): 73.07, 73.12, 73.15, 73.17, 73.18 eşyası ve diğer adi metallerden benzerleri (implant için özel tasarlanmış tıbbi ürünler hariç, 90.21); adi metal yaylar ve yay yaprakları (saat zemberekleri hariç, 91.14); 83.01, 83.02, 83.08, 83.10 eşyası ile 83.06’daki adi metal çerçeve ve aynalar. 73–76 ve 78–82. fasıllarda (73.15 hariç) eşyanın “aksam ve parçalarına” yapılan atıflar bunları kapsamaz. 83. Fasıl Not 1 saklı kalmak üzere, 82 veya 83. fasıla giren eşya 72–76 ve 78–81. fasıllara verilmez."],
        ["Bölüm XV Not 3", "“Adi metaller”: demir ve çelik, bakır, nikel, alüminyum, kurşun, çinko, kalay, tungsten (volfram), molibden, tantal, magnezyum, kobalt, bizmut, kadmiyum, titan, zirkonyum, antimon, manganez, berilyum, krom, germanyum, vanadyum, galyum, hafniyum, indiyum, niyobyum (kolombiyum), renyum ve talyum. Kıymetli metaller (gümüş, altın ve platin grubu) bu listede yoktur."],
        ["Bölüm XV Not 4", "“Sermet”: metal ve seramik terkiplerin mikroskopik heterojen bileşimi; metalle sinterlenmiş metal karbürleri (sert metaller) de kapsar."],
        ["Bölüm XV Not 5", "Alaşımlar (72 ve 74. fasıllardaki ferro-alyajlar ve ön alaşımlar hariç): (a) adi metal alaşımları, ağırlıkça diğer metallere üstün gelen metalin alaşımıdır; (b) bölümdeki adi metallerle bölüm dışı elementlerin alaşımı, adi metallerin toplam ağırlığı diğer elementlerin toplam ağırlığına <b>eşit veya fazlaysa</b> bu bölümün adi metal alaşımıdır (aksi halde genellikle 38.24); (c) sinterlenmiş metal tozu karışımları, ergitmeyle elde edilen heterojen karışımlar (sermetler hariç) ve intermetalik bileşimler de alaşımdır."],
        ["Bölüm XV Not 6", "Aksine hüküm yoksa tarifede bir adi metale yapılan atıf, Not 5’e göre o metalin alaşımı sayılan alaşımları da kapsar."],
        ["Bölüm XV Not 7", "Karma eşya: pozisyon metninde aksine hüküm yoksa iki veya daha fazla adi metal içeren eşya, ağırlıkça diğer metallerin <b>her birinden</b> üstün olan metalden sayılır. Demir ve çeliğin tüm türleri tek metaldir; alaşım, sınıflandırıldığı metalden ibaret sayılır (pirinç parça bakır sayılır); 81.13’teki sermet tek bir adi metaldir. Pozisyon metni önceliklidir: bakır başlıklı çelik gövdeli çivi 74.15’tedir."],
        ["Bölüm XV Not 8", "(a) Döküntü ve hurda: tamamen metal döküntü ve hurdalar ile kırılma, kesilme, eskime vb. nedenlerle <b>kesinlikle kullanılmaz</b> halde olan metal eşya. (b) Toz: göz açıklığı <b>1 mm</b> olan elekten ağırlıkça <b>%90 veya fazlası</b> geçen ürün."],
        ["Bölüm XV Not 9", "74–76 ve 78–81. fasıllar için: çubuk = rulo halinde olmayan içi dolu ürün; tel = rulo halinde içi dolu ürün (kesit şekilleri aynı tanımlanır; dikdörtgen kesitlilerde kalınlık genişliğin onda birini geçer); profil = çubuk, tel, levha veya boru tanımına uymayan sabit kesitli ürün; levha, sac, şerit, yaprak = kalınlığı genişliğin onda birini geçmeyen yassı ürün; boru = tek kapalı boşluklu, sabit kesitli içi boş ürün. Fasıl 72’nin kendi tanımları vardır (Fasıl 72 Not 1)."],
        ["Fasıl 72 Not 1(a)–(c)", "(a) Dökme (pik) demir: ağırlıkça <b>%2’den fazla</b> karbon; krom en çok %10, manganez en çok %6, fosfor en çok %3, silisyum en çok %8, diğer elementler toplamı en çok %10; dövülmeye elverişsiz demir-karbon alaşımı. (b) Aynalı demir: <b>%6’dan fazla, %30’u geçmeyen</b> manganez; diğer özellikleri (a)’ya uygun. (c) Ferro-alyaj: ilk şekillerde, sürekli dökümle veya granül-toz halinde, katkı, deoksidan veya desülfüran olarak kullanılan, genellikle dövülemeyen, ağırlıkça <b>%4 veya fazla demir</b> ile kromu %10’dan, manganezi %30’dan, fosforu %3’ten, silisyumu %8’den fazla ya da diğer elementleri toplam %10’dan fazla (karbon hariç; bakır en çok %10) içeren alaşım."],
        ["Fasıl 72 Not 1(d)–(f)", "(d) Çelik: genellikle dövülerek işlenebilen, ağırlıkça <b>%2 veya daha az</b> karbon içeren demirli maddeler (72.03 ürünleri ayrı tutulur); kromlu çelikler daha fazla karbon içerebilir. (e) Paslanmaz çelik: <b>%1,2 veya daha az karbon</b> ve <b>%10,5 veya daha fazla krom</b>. (f) Diğer alaşımlı çelik: paslanmaz olmayan ve ağırlıkça şunlardan en az birini içeren çelik: alüminyum %0,3; bor %0,0008; krom %0,3; kobalt %0,3; bakır %0,4; kurşun %0,4; manganez %1,65; molibden %0,08; nikel %0,3; niyobyum %0,06; silisyum %0,6; titanyum %0,05; tungsten %0,3; vanadyum %0,1; zirkonyum %0,05; diğer elementler ayrı ayrı %0,1 (kükürt, fosfor, karbon ve azot hariç). (d), (e), (f) tanımları tarifenin her yerinde geçerlidir."],
        ["Fasıl 72 Not 1(g)–(ij)", "(g) Hurdadan ergitilmiş külçe: kabaca dökülmüş, besleme başı olmayan, yüzey hataları belirgin, pik, aynalı demir veya ferro-alyaj bileşimine uymayan ürünler. (h) Granül: göz açıklığı <b>1 mm</b> elekten ağırlıkça <b>%90’dan azı</b>, <b>5 mm</b> elekten <b>%90 veya fazlası</b> geçen ürün. (ij) Yarı mamul: sürekli dökümle elde edilen içi dolu ürünler ve yalnız ilk sıcak haddeleme veya dövme ile kabaca şekil verilmiş içi dolu ürünler; rulo halinde bulunmazlar."],
        ["Fasıl 72 Not 1(k)", "Yassı hadde mamulü: kesiti dikdörtgen (kare hariç), içi dolu; ya üst üste sarılmış rulo halinde ya da rulo değilse kalınlık <b>4,75 mm’den azsa</b> genişlik kalınlığın <b>en az 10 katı</b>, kalınlık <b>4,75 mm veya fazlaysa</b> genişlik <b>150 mm’yi geçen</b> ve kalınlığın <b>en az 2 katı</b>. Haddeden gelen kabartmalar ile başka eşya karakteri kazandırmayan delme, oluklama ve parlatma serbesttir. Kare veya dikdörtgen dışındaki yassı ürünler, boyutu ne olursa olsun <b>600 mm veya fazla</b> genişlikte sayılır."],
        ["Fasıl 72 Not 1(l)–(p)", "(l) Filmaşin: sıcak haddelenmiş, <b>düzensiz sarılmış kangal</b> halinde içi dolu ürün (hadde nervürlü olabilir). (m) Diğer çubuklar: (ij), (k), (l) ve tel tanımına uymayan, sabit kesitli içi dolu ürün; hadde nervürlü veya haddeden sonra burulmuş olabilir. (n) Profiller: bu tanımlara uymayan sabit kesitli içi dolu ürünler; 73.01 ve 73.02 ürünleri Fasıl 72’ye dahil değildir. (o) Tel: yassı tanımına uymayan, <b>soğuk usulle</b> elde edilmiş, rulo (kangal) halinde içi dolu ürün. (p) Sondaj için içi boş çubuk: dış kesitinin en geniş boyutu <b>15 mm’yi geçen, 52 mm’yi geçmeyen</b> sondaja elverişli içi boş çubuk; tanıma uymayan içi boş çubuklar 73.04’tedir."],
        ["Fasıl 72 Not 2 – Not 3", "Not 2: farklı nitelikte bir demirli metalle kaplanmış demirli metaller, ağırlıkça üstün olan demirli metalin ürünü sayılır (ör. paslanmaz çelik kaplı alaşımsız çelik çubukta alaşımsız çelik üstünse Tali Fasıl II). Not 3: elektrolitik depozisyon, basınçlı döküm veya sinterleme ile elde edilen demir ve çelik ürünleri; şekil, bileşim ve görünüşlerine göre benzeri sıcak hadde ürünlerinin pozisyonunda sınıflandırılır."],
        ["Bölüm XV Genel Açıklamalar", "Genel kullanıma mahsus aksam, ait olduğu eşyanın parçası sayılmaz: merkezi ısıtma radyatörüne özel cıvata 73.22 yerine 73.18’de, motorlu taşıt yayı 87.08 yerine 73.20’de. %2’den az kıymetli metal içeren alaşım adi metal alaşımıdır. Sinterlenmemiş metal tozu karışımları Not 7’ye göre sınıflandırılır. Bölüm dışı ayrıca: adi metal amalgamları (28.53), metalize iplik (56.05), metal paralar (71.18), kullanılmış pil ve akümülatörler (85.48), metal tel fırçalar (96.03)."],
        ["Fasıl 72 Genel Açıklamalar", "Döküm eşya, kaynakla birleştirilmiş profiller, demiryolu malzemesi, borular ve daha ileri işlenmiş eşya Fasıl 73’tedir. Tavlama, temperleme, dekapaj, pas önleyici kaba kaplama (yağ, pas önleyici boya), parlatma, yapay oksidasyon ve kimyasal yüzey işlemleri (fosfatlama, kromlama) pozisyon metinlerinde aksi belirtilmedikçe pozisyonu değiştirmez. Hafif soğuk haddeleme (skin pass) sıcak hadde karakterini bozmaz. Demir olmayan metalle kaplı demir ürünleri, demir-çelik ağırlıkça üstünse Fasıl 72’de kalır."],
        ["72.01 – 72.05 Açıklama Notları", "Ağırlıkça %2’den fazla karbon içeren kromlu çelikler pik değil, Tali Fasıl IV’tedir. Aynalı demir dökme demirle aynı pozisyondadır (72.01). Ferro-alyaj gibi kullanılan fakat %4’ten az demir içeren kimyasallar Fasıl 28’de; ferro-uranyum 28.44; ferro-seryum 36.06. Sünger demir %80’den fazla metalik demir içerir; çelik yünü 73.23. Tamirle veya yeniden haddelemeyle kullanılabilecek eşya (eski ray, bilenebilir eğe) hurda değildir; cüruf ve tufal 26.19; pik kırıkları 72.01; radyoaktif hurda 28.44. Ferro-alyaj granül ve tozu 72.02’de; aşındırıcı bilyalar 73.26."],
        ["72.06 – 72.07 Açıklama Notları", "Hurdadan ergitilmiş külçe 72.04’te, sürekli döküm ürünleri 72.07’de. Yarı mamuller: blum, kütük, yuvarlak, kalın levha, levha çubuğu, dövmeyle kabaca şekil verilmiş parça, profil taslağı. Sonradan önemli şekil verme gerektiren kaba dövme taslak (gemi krank mili için zikzak parça) 72.07’dedir; krank mili halini almış olanlar ile kalıpta dövülmüş taslaklar hariçtir."],
        ["72.08 – 72.12 Açıklama Notları", "“Kaplanmış”: metalle kaplama (galvaniz, kalay, elektrolitik çinko vb.), boya, emaye, vernik, plastik gibi metal olmayan kaplama veya plakaj. Kıymetli metalle kaplananlar Fasıl 71’de; genleşmiş metal 73.14’te; Fasıl 82 eşya taslakları hariçtir. “Geniş yassı ürün”: genişliği 600–1.250 mm, kalınlığı en az 4 mm, dört yüzü haddelenmiş, rulo olmayan ürün. Oluklu yassı ürünlerde kenar genişliği esas alınır; köşeli profilli “kenarlı levhalar” genellikle 72.16’dadır."],
        ["72.13 – 72.17 Açıklama Notları", "Beton için nervürlü çubuk: kangal halinde 72.13, düz boyda 72.14. Soğuk çekilmiş, taşlanmış veya kaplanmış çubuk 72.15; düz boyda satılan soğuk çubuk daima kangal halindeki telden (72.17) ayrılır. Hariç: iki veya daha fazla çubuğun birlikte burulmasıyla oluşan ürün 73.08; uzunluğu kesitinden kısa parça ve konik çubuk 73.26; kaynaklı profil ve palplanş 73.01; demiryolu malzemesi 73.02; dikenli tel 73.13; demetlenmiş tel ve halat 73.12; kaplanmış kaynak elektrodu 83.11; izole tel 85.44; müzik teli 92.09."],
        ["72.18 – 72.29 Açıklama Notları", "Paslanmaz ve diğer alaşımlı çelik pozisyonlarına alaşımsız çeliğin (72.06–72.17) açıklama notları gerekli değişikliklerle uygulanır. Cerrahi dikiş için steril paslanmaz tel 30.06’dadır. 72.28 alaşımlı veya alaşımsız çelikten sondaj için içi boş çubukları da kapsar."],
    ],
    "sinir_komsulari": [
        ["Demir cevheri ve konsantre pelletler", "26.01", "Cevherdir; sünger demir (72.03) parlak kesit yüzeyiyle ayrılır"],
        ["Cüruf, yüksek fırın cürufu, tufal", "26.19", "72.04 hariç tutması"],
        ["Ferro-seryum, piroforik alaşım", "36.06", "Bölüm XV Not 1"],
        ["%4’ten az demirli silisyum karbür, molibden oksit (katkı)", "Fasıl 28", "72.02 hariç tutması"],
        ["Çelik yünü (“çelik sünger”)", "73.23", "72.03 hariç tutması"],
        ["Kaynaklı profil, palplanş", "73.01", "72.16 hariç tutması"],
        ["Demiryolu ve tramvay hattı malzemesi", "73.02", "Fasıl 72 Not 1(n)"],
        ["Birlikte burulmuş çubuklar; inşaat için hazırlanmış eşya", "73.08", "72.14 ve 72.16 hariç tutmaları"],
        ["Ölçü dışı içi boş çubuklar", "73.04", "Fasıl 72 Not 1(p)"],
        ["Dikenli tel; demetlenmiş tel ve halat", "73.13 / 73.12", "72.17 hariç tutması"],
        ["Genleşmiş metal (depluvayye)", "73.14", "72.08 hariç tutması"],
        ["Konik çubuk; aşındırıcı bilya", "73.26", "72.15 ve 72.05 hariç tutmaları"],
        ["Kaplanmış kaynak elektrodu", "83.11", "72.17 hariç tutması"],
        ["Taşıt yayı; radyatör cıvatası", "73.20 / 73.18", "Bölüm XV Not 2: genel kullanıma mahsus aksam"],
        ["Kıymetli metalle kaplanmış yassı ürün", "Fasıl 71", "Bölüm XV Not 1; 72.08 ve 72.10 hariç tutmaları"],
    ],
    "tuzaklar": [
        "<b>Fasıl 72’de tel soğuk elde edilir.</b> Sıcak haddelenmiş düzensiz kangal filmaşindir (72.13); soğuk elde edilmiş kangal teldir (72.17); düz boyda soğuk çekilmiş ürün çubuktur (72.15). Bölüm XV Not 9’daki “rulo mu değil mi” ölçütü 74–76 ve 78–81. fasıllar içindir.",
        "<b>Kaplama ile kaba kaplama aynı değildir.</b> Yağlama ve pas önleyici kaba boya 72.08–72.09’u bozmaz; galvaniz, kalay, plastik, emaye veya vernik kaplama ürünü 72.10 veya 72.12’ye götürür.",
        "<b>Skin pass soğuk hadde sayılmaz.</b> Kalınlığı belirgin şekilde azaltmayan hafif soğuk geçiş sıcak hadde ürünü karakterini değiştirmez (72.08).",
        "<b>Paslanmaz için iki şart birlikte aranır.</b> En az %10,5 krom ve en çok %1,2 karbon. %12 krom ve %2 karbonlu alet çeliği paslanmaz değil, diğer alaşımlı çeliktir (Tali Fasıl IV).",
        "<b>Aynalı demir ferro-alyaj değildir.</b> Manganez %6–30 arasındaysa 72.01; %30’u aşarsa (ve en az %4 demir varsa) ferro-manganez 72.02.",
        "<b>Pik kırığı hurda değildir.</b> Dökme demir ve aynalı demir kırıkları 72.01’dedir; tamirle veya yeniden haddelemeyle kullanılabilecek eski raylar ve eğeler de 72.04’e girmez.",
        "<b>Karma eşyada demir-çelik tek metaldir.</b> Ağırlıkça üstünlük her bir metalle ayrı ayrı karşılaştırılır; pirinç bakır sayılır. Pozisyon metni önceliklidir: bakır başlıklı çelik çivi 74.15’tedir.",
        "<b>Genel kullanıma mahsus aksam kendi pozisyonunda kalır.</b> Taşıt yayı 87.08’de değil 73.20’de, radyatör cıvatası 73.22’de değil 73.18’de; saat zembereği ise 91.14’tedir.",
        "<b>Kare veya dikdörtgen olmayan yassı ürün</b>, ölçüsü ne olursa olsun 600 mm veya fazla genişlikte sayılır (Not 1(k)).",
        "<b>Adi metal listesinde kıymetli metal yoktur.</b> Paladyum, rodyum gibi platin grubu metaller Fasıl 71’dedir; berilyum, kadmiyum, galyum, hafniyum ise adi metaldir (Bölüm XV Not 3).",
    ],
    "hafiza": {
        "kanca": "PİK – FERRO – SÜNGER – HURDA – TOZ, sonra KÜ – YA – YAS – FİL – ÇU – PRO – TEL",
        "aciklama": "01–05 ilk maddeler: <b>PİK</b> 01, <b>FERRO</b> 02, <b>SÜNGER</b> 03, <b>HURDA</b> 04, <b>TOZ</b> 05. Sonra her çelik ailesi aynı merdiveni iner: <b>KÜ</b>lçe → <b>YA</b>rı mamul → <b>YAS</b>sı → <b>FİL</b>maşin → <b>ÇU</b>buk → <b>PRO</b>fil → <b>TEL</b>. Alaşımsız 06–17 (yassı 08–12 beş pozisyon), paslanmaz 18–23, diğer alaşımlı 24–29. Hadde fabrikasında erimiş metal soldan girer, en sağdan kangal tel olarak çıkar.",
    },
    "sinav_odagi": [
        "Bu fasıl çıkmış sorularda daha çok Bölüm XV notları üzerinden yer almıştır: “XV. Bölüm notlarına göre çubuk ile tel arasındaki fark” (rulo halinde olup olmama) gibi tanım soruları.",
        "Adi metallerin bölüm içindeki dağılımı: hangi adi metal için ayrı fasıl açıldığı (kalay Fasıl 80; magnezyum, titanyum, krom Fasıl 81).",
        "72.08’deki yassı ürünlerin genişlik (600 mm), kalınlık, rulo olup olmama, kabartmalı motif, dekapaj ve karbon oranı gibi ölçütlerle birlikte değerlendirildiği uzun öncüllü sorular (alt pozisyon düzeyine kadar inen).",
        "Çelik taslaklarının GYK 2(a) ile bitmiş eşya gibi sınıflandırılması (anahtar taslakları) ve set sorularında alaşımsız çelik taslakların çeldirici olarak kullanılması.",
        "Fasıl 72–73–83 sınırı: boru bağlantı parçaları, yaylar, zımba teli, konteyner gibi demir-çelik eşyanın hangi fasılda yer aldığına ilişkin “hangisi 73. fasılda yer almaz” kalıbı.",
    ],
    "cikmis_ornekler": [
        {
            "soru": "Türk Gümrük Tarife Cetveli’nin XV. Bölüm Notlarına göre “çubuk” ve “tel” arasındaki farklılık nedir?",
            "secenekler": ["Enine kesitleri", "Üretim yöntemleri", "İçlerinin dolu-boş olması", "Rulo halde olup olmaması", "Mamul oldukları madde"],
            "cevap": "D",
            "aciklama": "Bölüm XV Not 9’a göre çubuk rulo halinde olmayan, tel ise rulo halinde içi dolu üründür; enine kesit şekilleri her iki tanımda aynıdır ve ikisi de içi doludur.",
        },
        {
            "soru": "Aşağıdaki adi metallerden hangisi için Armonize Sistem Nomanklatüründe özel olarak açılmış bir fasıl bulunmaktadır?",
            "secenekler": ["Magnezyum", "Titanyum", "Krom", "Kalay"],
            "cevap": "D",
            "aciklama": "Kalay için ayrı bir fasıl (Fasıl 80) vardır. Magnezyum, titanyum ve krom Bölüm XV Not 3’te sayılan adi metaller olmakla birlikte Fasıl 81’de “diğer adi metaller” arasında yer alır.",
        },
    ],
    "ozet": [
        "Bölüm XV notları bütün adi metal fasıllarını yönetir: dışlamalar, genel kullanıma mahsus aksam, adi metal listesi, alaşım ve karma eşya kuralları.",
        "Pik %2’den fazla karbon; çelik %2 veya az; paslanmaz en az %10,5 krom ve en çok %1,2 karbon; diğer alaşımlı Not 1(f) eşikleri.",
        "İlk maddeler 72.01–72.05; alaşımsız 72.06–72.17; paslanmaz 72.18–72.23; diğer alaşımlı 72.24–72.29.",
        "Yassı ürünlerde 600 mm sınırı ve sıcak/soğuk/kaplanmış ayrımı: 72.08–72.09–72.10 ve 72.11–72.12.",
        "Filmaşin sıcak ve düzensiz kangal; tel soğuk ve kangal; çubuk düz boy.",
        "Borular, kaynaklı profiller, demiryolu malzemesi ve şekil verilmiş eşya Fasıl 73’tedir.",
    ],
}

S = []

# ---------- Eşya → 4’lü pozisyon (5) ----------
S.append(soru(ESYA,
    "Tarife Cetveline göre, demir veya alaşımsız çelikten, genişliği 1.000 mm, kalınlığı 2 mm, rulo halinde, sıcak daldırma yoluyla çinko ile kaplanmış (galvanizli) yassı hadde ürünü hangi pozisyonda sınıflandırılır?",
    "72.10", ["72.08", "72.09", "72.12", "72.25"], "E",
    "Genişliği 600 mm veya daha fazla olan demir veya alaşımsız çelikten yassı hadde ürünleri kaplanmış ise 72.10’dadır; sıcak daldırma ile çinko kaplama metalle kaplama işlemidir. 72.08 ve 72.09 yalnız kaplanmamış ürünleri, 72.12 genişliği 600 mm’den az kaplanmış ürünleri, 72.25 diğer alaşımlı çeliği kapsar.",
    "72.10 pozisyon metni ve Açıklama Notu; Fasıl 72 Not 1(k); Fasıl 72 Genel Açıklamalar."))

S.append(soru(ESYA,
    "Tarife Cetveline göre, alaşımsız çelikten, betonla daha iyi kaynaşması için haddeleme sırasında üzerinde çıkıntı ve kertikler oluşturulmuş, kangal halinde değil düz boylar halinde sunulan, sadece sıcak haddelenmiş inşaat çubuğu hangi pozisyonda yer alır?",
    "72.14", ["72.13", "72.15", "72.16", "73.08"], "C",
    "Haddeleme sırasında oluşan çentik ve nervürler Not 1(m) gereği çubuk tanımını bozmaz; sadece sıcak haddelenmiş düz boy çubuklar 72.14’tedir. Aynı ürün düzensiz kangal halinde olsaydı filmaşin olarak 72.13’e girerdi. 72.15 soğuk işlenmiş veya daha ileri işlem görmüş çubukları, 73.08 inşaat için hazırlanmış eşyayı kapsar.",
    "Fasıl 72 Not 1(l) ve 1(m); 72.13 ve 72.14 Açıklama Notları."))

S.append(soru(ESYA,
    "Tarife Cetveline göre, ağırlıkça %0,08 karbon, %18 krom ve %8 nikel içeren çelikten, genişliği 1.250 mm, rulo halinde, sadece soğuk haddelenmiş yassı ürün hangi pozisyonda sınıflandırılır?",
    "72.19", ["72.09", "72.25", "72.20", "72.26"], "A",
    "Karbon %1,2’yi geçmediği ve krom %10,5 veya daha fazla olduğu için çelik Not 1(e) anlamında paslanmaz çeliktir. Paslanmaz çelikten genişliği 600 mm veya daha fazla yassı hadde ürünleri 72.19’dadır; 600 mm’den az olsaydı 72.20’ye girerdi. 72.09 alaşımsız, 72.25 ve 72.26 diğer alaşımlı çelik içindir.",
    "Fasıl 72 Not 1(e) ve 1(k); 72.19 pozisyon metni."))

S.append(soru(ESYA,
    "Tarife Cetveline göre, ağırlıkça %70 manganez, %20 demir ve %7 karbon içeren, çelik üretiminde katkı maddesi olarak kullanılan, kütle halindeki alaşım hangi pozisyonda yer alır?",
    "72.02", ["72.01", "81.11", "72.24", "26.02"], "D",
    "Ağırlıkça %4 veya daha fazla demir ve %30’dan fazla manganez içeren, katkı maddesi olarak kullanılan bu alaşım Not 1(c) anlamında ferro-alyajdır (ferro-manganez) ve 72.02’dedir. Aynalı demir (72.01) en çok %30 manganez içerebilir. Bölüm XV Not 5 ferro-alyajları ağırlıkça üstün metal kuralının dışında tuttuğundan, manganez ağır bassa da ürün 81.11’e gitmez.",
    "Fasıl 72 Not 1(b) ve 1(c); Bölüm XV Not 5; 72.02 Açıklama Notu."))

S.append(soru(ESYA,
    "Tarife Cetveline göre, ağırlıkça %3,5 karbon, %2 silisyum ve %0,6 manganez içeren, dövülmeye elverişli olmayan, külçe halindeki demir-karbon alaşımı hangi pozisyonda sınıflandırılır?",
    "72.01", ["72.02", "72.06", "72.04", "73.25"], "B",
    "Ağırlıkça %2’den fazla karbon içeren, silisyumu %8’i ve manganezi %6’yı aşmayan, dövülmeye elverişli olmayan demir-karbon alaşımı Not 1(a) anlamında dökme (pik) demirdir ve ilk şekillerde 72.01’dedir. Ferro-alyaj için silisyumun %8’den veya manganezin %30’dan fazla olması gerekir; 72.06 çelik külçeleri, 73.25 döküm eşyayı kapsar.",
    "Fasıl 72 Not 1(a), (c) ve (d); 72.01 Açıklama Notu."))

# ---------- Olumsuz teşhis (4) ----------
S.append(soru(OLUMSUZ,
    "Aşağıdakilerden hangisi Tarife Cetvelinin 72. faslında <b>sınıflandırılmaz</b>?",
    "“Çelik sünger” olarak da bilinen çelik yünü",
    ["Demir cevherinin doğrudan indirgenmesiyle elde edilen sünger demir pelleti", "Paket halinde torna talaşları",
     "Hurdaların yeniden ergitilmesiyle elde edilen külçe", "Ferro-silisyum granülleri"], "C",
    "Çelik yünleri 72.03 açıklama notu gereği 73.23’tedir. Sünger demir 72.03’te; torna talaşları ve hurdadan ergitilmiş külçeler 72.04’te; ferro-alyajların granül ve toz halleri de 72.02’de kalır (72.05’e girmez).",
    "72.02, 72.03, 72.04 ve 72.05 Açıklama Notları."))

S.append(soru(OLUMSUZ,
    "Aşağıdaki tellerden hangisi 72.17 pozisyonunda <b>yer almaz</b>?",
    "Çit yapımında kullanılan demir veya çelikten dikenli tel",
    ["Çinko ile kaplanmış alaşımsız çelik tel",
     "Şapka iskeleti için üzeri dokumaya elverişli maddeyle kaplanmış çelik tel",
     "Bakırla kaplanmış, ağırlıkça çeliğin üstün olduğu alaşımsız çelik tel",
     "Kangal halinde, cilalanmış alaşımsız çelik tel"], "E",
    "Dikenli teller 72.17 açıklama notunda hariç tutulmuş ve 73.13’e verilmiştir. Çinko veya bakır gibi adi metallerle kaplanmış ya da cilalanmış teller 72.17’de kalır; tel esas unsur olduğu sürece üzeri dokumaya elverişli maddeyle kaplanmış şapkacı telleri de bu pozisyondadır.",
    "Fasıl 72 Not 1(o); 72.17 Açıklama Notu; Bölüm XV Not 7."))

S.append(soru(OLUMSUZ,
    "XV. Bölüm Not 1 uyarınca aşağıdakilerden hangisi bu bölümde <b>sınıflandırılmaz</b>?",
    "Ferro-seryum",
    ["Ferro-krom", "Adi metalden kapı menteşesi", "Demir veya çelikten cıvata", "Alüminyumdan folyo"], "A",
    "Ferro-seryum ve diğer piroforik alaşımlar Bölüm XV Not 1 gereği 36.06’dadır. Ferro-krom ferro-alyaj olarak 72.02’de, menteşe 83.02’de, cıvata 73.18’de, alüminyum folyo 76.07’de olmak üzere diğerleri Bölüm XV içindedir.",
    "Bölüm XV Not 1; 72.02 Açıklama Notu, hariç tutma (c)."))

S.append(soru(OLUMSUZ,
    "Aşağıdakilerden hangisi 72.04 pozisyonunda döküntü ve hurda olarak <b>sınıflandırılmaz</b>?",
    "Dökme (pik) demirin kırılmış parçaları",
    ["Kırılma nedeniyle kesinlikle kullanılmaz hale gelmiş çelik eşya",
     "Motorlu taşıt gövdelerinin parçalanıp manyetik olarak ayrılmasıyla elde edilen çelik hurda",
     "Hidrolik presle balya yapılmış hafif çelik döküntüleri", "Kalaylı çelik saç kırpıntıları"], "D",
    "72.04 açıklama notu dökme demir ve aynalı demirin kırılmış parçalarını hariç tutar; bunlar 72.01’dedir. Bölüm XV Not 8(a)’ya göre kesinlikle kullanılmaz hale gelmiş metal eşya hurdadır; parçalama, balyalama ve manyetik ayırma gibi hazırlık işlemleri görmüş hurdalar ile kalaylı saç kırpıntıları 72.04’te kalır.",
    "Bölüm XV Not 8(a); 72.04 Açıklama Notu."))

# ---------- Farklı/aynı pozisyon veya fasıl (4) ----------
S.append(soru(FARKLI,
    "Aşağıdakilerden hangisi diğerlerinden <b>farklı</b> bir fasılda yer alır?",
    "Kaynakla birleştirilmiş çelik profil",
    ["Alaşımsız çelikten blum", "Alaşımsız çelikten sıcak haddelenmiş U profil", "Paslanmaz çelikten tel",
     "Not 1(p) tanımına uyan, alaşımlı çelikten sondaj için içi boş çubuk"], "B",
    "Kaynaklı profiller 72.16 açıklama notunda hariç tutulmuş ve 73.01’e verilmiştir; Fasıl 72 Genel Açıklamalarına göre kaynakla birleştirilmiş profiller Fasıl 73’tedir. Blum 72.07’de, sıcak haddelenmiş U profil 72.16’da, paslanmaz tel 72.23’te, sondaj için içi boş çubuk 72.28’dedir.",
    "72.16 Açıklama Notu; Fasıl 72 Genel Açıklamalar; Fasıl 72 Not 1(p)."))

S.append(soru(FARKLI,
    "Genişliği 600 mm veya daha fazla olan, demir veya alaşımsız çelikten aşağıdaki sıcak haddelenmiş yassı ürünlerden hangisi diğerlerinden <b>farklı</b> bir pozisyonda yer alır?",
    "Plastik maddeyle kaplanmış levha",
    ["Dekapaj (asitle pul temizleme) işlemi görmüş rulo",
     "Yalnızca taşıma sırasında paslanmayı önlemek için yağlanmış levha",
     "Üzerinde haddeden gelen baklava desenli kabartma bulunan levha",
     "Kalınlığı belirgin azaltmayan hafif soğuk haddeleme (skin pass) uygulanmış rulo"], "E",
    "Plastikle kaplama metal olmayan maddeyle kaplamadır ve ürünü 72.10’a götürür. Dekapaj, yağlama gibi kaba koruyucu kaplama ve haddeden gelen kabartmalar 72.08’i bozmaz; hafif soğuk geçiş (skin pass) da sıcak hadde karakterini değiştirmez.",
    "72.08 ve 72.10 Açıklama Notları; Fasıl 72 Genel Açıklamalar (IV)."))

S.append(soru(FARKLI,
    "Aşağıdaki eşya çiftlerinden hangisinde her iki eşya da <b>aynı</b> pozisyonda yer alır?",
    "Alaşımsız çelikten blum – alaşımsız çelikten sürekli dökümle elde edilmiş kütük",
    ["Sıcak haddelenmiş, düzensiz kangal halinde alaşımsız çelik çubuk – soğuk çekilmiş, kangal halinde alaşımsız çelik tel",
     "Soğuk çekilmiş düz boy alaşımsız çelik çubuk – sadece sıcak haddelenmiş düz boy alaşımsız çelik çubuk",
     "Motorlu taşıt için çelik yaprak yay – adi metalden kapı menteşesi",
     "Alaşımsız çelikten külçe – hurdaların yeniden ergitilmesiyle elde edilen külçe"], "D",
    "Blumlar ve sürekli dökümle elde edilen tüm yarı mamuller 72.07’dedir. Filmaşin 72.13’te, tel 72.17’de; soğuk çekilmiş çubuk 72.15’te, sıcak haddelenmiş çubuk 72.14’te; yay 73.20’de, menteşe 83.02’de; çelik külçe 72.06’da, hurdadan ergitilmiş külçe 72.04’tedir.",
    "72.04, 72.06, 72.07 ve 72.13–72.17 Açıklama Notları; Bölüm XV Not 2."))

S.append(soru(FARKLI,
    "Aşağıdaki yaylardan hangisi diğerlerinden <b>farklı</b> bir pozisyonda yer alır?",
    "Duvar saati için çelik zemberek",
    ["Motorlu taşıt süspansiyonu için çelik helezon yay", "Kamyon için çelik yay yaprağı",
     "Çamaşır makinesi için çelik yay", "Koltuk için çelik helezon yay"], "A",
    "Bölüm XV Not 2’ye göre adi metal yaylar ve yay yaprakları genel kullanıma mahsus aksamdır ve ait oldukları eşyanın parçası olarak değil kendi pozisyonunda (demir veya çelikten olanlar 73.20) sınıflandırılır. Saat zemberekleri bu tanımdan açıkça hariç tutulmuş olup 91.14’tedir.",
    "Bölüm XV Not 1 ve Not 2; Bölüm XV Genel Açıklamalar (C)."))

# ---------- Fasıl notu · Tanım/Eşik (4) ----------
S.append(soru(TANIM,
    "Fasıl 72 Not 1(e)’ye göre “paslanmaz çelik” aşağıdakilerden hangisidir?",
    "Ağırlıkça %1,2 veya daha az karbon ve %10,5 veya daha fazla krom içeren çelik alaşımları",
    ["Ağırlıkça %2 veya daha az karbon ve %10 veya daha fazla krom içeren çelik alaşımları",
     "Ağırlıkça %1,2 veya daha az karbon ve %12 veya daha fazla nikel içeren çelik alaşımları",
     "Ağırlıkça %0,3 veya daha fazla krom içeren bütün çelikler",
     "Ağırlıkça %1,2’den fazla karbon ve %10,5’ten az krom içeren çelik alaşımları"], "B",
    "Not 1(e) paslanmaz çeliği, diğer elementlerle birlikte olsun olmasın, ağırlıkça %1,2 veya daha az karbon ve %10,5 veya daha fazla krom içeren çelik alaşımı olarak tanımlar. %0,3 krom eşiği Not 1(f)’deki “diğer alaşımlı çelik” tanımına aittir; %2 karbon ise çelik ile pik demir arasındaki sınırdır.",
    "Fasıl 72 Not 1(d), (e) ve (f)."))

S.append(soru(TANIM,
    "Fasıl 72 Not 1(k)’ye göre rulo halinde olmayan, enine kesiti dikdörtgen bir ürünün “yassı hadde mamulü” sayılabilmesi için; kalınlığı 4,75 mm’den az ise genişliği kalınlığının en az ..... katı, kalınlığı 4,75 mm veya daha fazla ise genişliği ..... mm’yi geçmeli ve kalınlığının en az iki katı olmalıdır. Boşluklara sırasıyla hangisi gelmelidir?",
    "10 – 150", ["10 – 600", "2 – 150", "5 – 150", "10 – 300"], "C",
    "Not 1(k)’ye göre rulo halinde olmayan ürünlerde kalınlık 4,75 mm’den azsa genişlik kalınlığın en az 10 katı; kalınlık 4,75 mm veya fazlaysa genişlik 150 mm’yi geçmeli ve kalınlığın en az iki katı olmalıdır. 600 mm, yassı ürünlerin pozisyonlar arası ayrımında (72.08–72.10 ile 72.11–72.12) kullanılan genişlik sınırıdır, tanım eşiği değildir.",
    "Fasıl 72 Not 1(k)."))

S.append(soru(TANIM,
    "XV. Bölüm Not 7’ye göre iki veya daha fazla adi metal içeren eşyanın sınıflandırılmasıyla ilgili aşağıdakilerden hangisi <b>yanlıştır</b>?",
    "Ağırlıkça üstünlük, metallerin eşyadaki kıymetlerine göre belirlenir.",
    ["Pozisyon metninde aksine hüküm yoksa eşya, ağırlıkça diğer metallerin her birinden üstün olan metalden sayılır.",
     "Demir ve çelik ile bunların değişik türleri tek ve aynı metal sayılır.",
     "Pirinçten bir parça, hesaplamada tamamen bakırdan imiş gibi değerlendirilir.",
     "81.13 pozisyonundaki sermet tek bir adi metal sayılır."], "E",
    "Not 7 karşılaştırmayı ağırlık üzerinden yapar; kıymet esas alınmaz. Demir ve çeliğin tüm türleri tek metal sayılır, alaşım (pirinç gibi) sınıflandırıldığı metalden ibaret kabul edilir ve sermet tek bir adi metaldir. Pozisyon metni önceliklidir: bakır başlıklı çelik çivi 74.15’te kalır.",
    "Bölüm XV Not 7; Bölüm XV Genel Açıklamalar (B)."))

S.append(soru(TANIM,
    "Tarife Cetveline göre demir veya çelikten “granül” aşağıdakilerden hangisidir?",
    "Göz açıklığı 1 mm olan elekten ağırlıkça %90’dan azı, göz açıklığı 5 mm olan elekten ağırlıkça %90 veya daha fazlası geçen ürünler",
    ["Göz açıklığı 1 mm olan elekten ağırlıkça %90 veya daha fazlası geçen ürünler",
     "Göz açıklığı 0,5 mm olan elekten ağırlıkça %90 veya daha fazlası geçen ürünler",
     "Göz açıklığı 5 mm olan elekten ağırlıkça %50’den azı geçen ürünler",
     "Göz açıklığı 2 mm olan elekten ağırlıkça %90 veya daha fazlası geçen ürünler"], "A",
    "Fasıl 72 Not 1(h) granülü, 1 mm elekten %90’dan azı ve 5 mm elekten %90 veya fazlası geçen ürün olarak tanımlar. 1 mm elekten %90 veya fazlası geçen ürün ise Bölüm XV Not 8(b) anlamında tozdur. Her ikisi de 72.05’te yer alır; ancak ferro-alyajların granül ve tozları 72.02’de kalır.",
    "Fasıl 72 Not 1(h); Bölüm XV Not 8(b); 72.05 Açıklama Notu."))

# ---------- Genel Yorum Kuralı (2) ----------
S.append(soru(GYK,
    "Gemi krank mili imali için dövülerek kabaca zikzak şeklinde yassılaştırılmış, ancak sonradan dövme, presleme veya tornalama ile önemli bir şekillendirme işlemi gerektiren alaşımsız çelik parça nasıl sınıflandırılır?",
    "72.07’de yarı mamul olarak; GYK 1 ile",
    ["84.83’te bitirilmemiş krank mili olarak; GYK 2(a) ile", "73.26’da demir veya çelikten diğer eşya olarak; GYK 4 ile",
     "72.14’te dövülmüş çubuk olarak; GYK 3(a) ile", "72.04’te döküntü olarak; GYK 1 ile"], "B",
    "72.07 açıklama notu, sonradan önemli şekil verme işlemi gerektiren kaba dövme taslakları (gemi krank mili için zikzak parça) yarı mamul olarak bu pozisyonda sayar; sınıflandırma pozisyon metni ve notlarla, yani GYK 1 ile yapılır. Parça bitmiş krank milinin asli niteliğini taşımadığından GYK 2(a) uygulanmaz; krank mili halini alıp yalnız bitirme işlemi eksik olanlar ise 72.07 dışında kalır.",
    "GYK 1; GYK 2(a) Açıklama Notu (II); 72.07 Açıklama Notu (B)."))

S.append(soru(GYK,
    "Paslanmaz çelikle plakaj yapılmış (kaplanmış), ağırlıkça alaşımsız çelik kısmın üstün olduğu, düz boy halindeki bir çubuğun sınıflandırılmasıyla ilgili hangisi doğrudur?",
    "Alaşımsız çelik çubuk olarak 72.15’te; Fasıl 72 Not 2’ye dayanarak GYK 1 ile",
    ["Paslanmaz çelik çubuk olarak 72.22’de; asli niteliği kaplama verdiği için GYK 3(b) ile",
     "Alaşımsız çelik çubuk olarak 72.14’te; GYK 3(a) ile",
     "Paslanmaz çelik çubuk olarak 72.22’de; numara sırasına göre son pozisyon olduğu için GYK 3(c) ile",
     "Diğer alaşımlı çelik çubuk olarak 72.28’de; GYK 4 ile"], "D",
    "Fasıl 72 Not 2’ye göre farklı nitelikte demirli metalle kaplanmış demirli metal, ağırlıkça üstün olan metalin ürünü sayılır; Genel Açıklamalar paslanmaz çelik kaplı alaşımsız çubuğu bu durumda Tali Fasıl II’ye yerleştirir. Kaplama, 72.14’te izin verilen işlemlerin ötesinde bir yüzey işlemi olduğundan çubuk 72.15’tedir. Not hükmü bulunduğundan GYK 3 kurallarına başvurulmaz.",
    "GYK 1; Fasıl 72 Not 2; Fasıl 72 Genel Açıklamalar (IV)(C); 72.15 Açıklama Notu."))

# ---------- Eşleştirme / Boşluk doldurma (2) ----------
S.append(soru(ESLES,
    "Fasıl 72 Not 1’deki tanımlara göre aşağıdaki ürünler ile eşikleri hangi seçenekte doğru eşleştirilmiştir? I. Dökme (pik) demir – karbon · II. Aynalı demir – manganez · III. Paslanmaz çelik – krom · IV. Ferro-alyaj – demir — a) %2’den fazla · b) %6’dan fazla, %30’u geçmeyen · c) %10,5 veya daha fazla · d) %4 veya daha fazla",
    "I-a, II-b, III-c, IV-d",
    ["I-b, II-a, III-c, IV-d", "I-a, II-b, III-d, IV-c", "I-d, II-b, III-c, IV-a", "I-a, II-c, III-b, IV-d"], "C",
    "Pik demir ağırlıkça %2’den fazla karbon, aynalı demir %6’dan fazla fakat %30’u geçmeyen manganez, paslanmaz çelik %10,5 veya daha fazla krom (ve en çok %1,2 karbon), ferro-alyaj ise %4 veya daha fazla demir içerir. Ferro-alyajdaki %4 demir şartı ile paslanmazdaki krom eşiğinin karıştırılması sık yapılan hatadır.",
    "Fasıl 72 Not 1(a), (b), (c) ve (e)."))

S.append(soru(ESLES,
    "Demir veya alaşımsız çelikten genişliği 600 mm veya daha fazla yassı hadde mamulleri; sıcak haddelenmiş ve kaplanmamış ise ....., soğuk haddelenmiş ve kaplanmamış ise ....., kaplanmış ise ..... pozisyonunda yer alır. Boşluklara sırasıyla hangisi gelmelidir?",
    "72.08 – 72.09 – 72.10",
    ["72.08 – 72.10 – 72.09", "72.09 – 72.08 – 72.10", "72.11 – 72.09 – 72.12", "72.08 – 72.09 – 72.12"], "A",
    "600 mm ve fazla genişlikte sıcak haddelenmiş kaplanmamış ürünler 72.08’de, soğuk haddelenmiş kaplanmamışlar 72.09’da, kaplanmışlar 72.10’dadır. 600 mm’den dar ürünlerde kaplanmamışlar 72.11’e, kaplanmışlar 72.12’ye gider.",
    "72.08–72.12 pozisyon metinleri."))

# ---------- Çoktan-çoğa (I–IV) (2) ----------
S.append(soru(COKLU,
    "XV. Bölüm Not 2’ye göre aşağıdakilerden hangileri “genel kullanıma mahsus aksam ve parça” sayılır? I. 73.18 pozisyonundaki demir veya çelikten cıvata ve somunlar · II. Adi metallerden yaylar ve yay yaprakları (saat zemberekleri hariç) · III. 83.01 pozisyonundaki adi metal kilitler · IV. Bilyalı rulmanlar",
    "I, II ve III", ["I ve II", "II, III ve IV", "I ve IV", "III ve IV"], "B",
    "Not 2; 73.07, 73.12, 73.15, 73.17 ve 73.18 eşyası ile diğer adi metallerden benzerlerini, saat zemberekleri dışındaki yayları ve 83.01, 83.02, 83.08, 83.10 eşyası ile 83.06’daki çerçeve ve aynaları sayar. Rulmanlar bu listede yoktur; XVI. Bölüm eşyası olarak Bölüm XV dışındadır.",
    "Bölüm XV Not 1 ve Not 2."))

S.append(soru(COKLU,
    "Fasıl 72 ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Ağırlıkça %2’den fazla karbon içeren kromlu çelikler Tali Fasıl IV’te diğer alaşımlı çeliklerle birlikte sınıflandırılır. · II. Elektrolitik depozisyon veya sinterleme ile elde edilen demir-çelik ürünleri benzeri sıcak hadde ürünlerinin pozisyonunda sınıflandırılır. · III. 73.01 veya 73.02 pozisyonuna giren ürünler 72.16’da profil olarak yer alır. · IV. Kare veya dikdörtgen dışındaki şekillerde kesilmiş yassı ürünler, boyutlarına bakılmaksızın genişliği 600 mm’den az ürün sayılır.",
    "I ve II", ["II ve III", "I, II ve IV", "III ve IV", "I ve IV"], "E",
    "72.01 açıklama notu %2’den fazla karbonlu kromlu çelikleri Tali Fasıl IV’e verir (I doğru); Not 3 elektrolitik depozisyon, basınçlı döküm ve sinterleme ürünlerini benzeri sıcak hadde ürünleriyle sınıflandırır (II doğru). Not 1(n) 73.01 ve 73.02 ürünlerini Fasıl 72 dışında bırakır (III yanlış); Not 1(k) kare veya dikdörtgen olmayan yassı ürünleri 600 mm veya fazla genişlikte sayar (IV yanlış).",
    "Fasıl 72 Not 1(d), (k), (n) ve Not 3; 72.01 Açıklama Notu."))

# ---------- Senaryo (2) ----------
S.append(soru(SENARYO,
    "Bir ithalatçı; ağırlıkça %0,45 karbon, %1 krom ve %0,2 molibden içeren çelikten, sıcak haddelenmiş, düzensiz sarılmış kangal halinde, enine kesiti daire ve çapı 12 mm olan bir ürün ithal etmektedir. Tarife Cetveline göre bu ürün hangi pozisyonda sınıflandırılır?",
    "72.27", ["72.13", "72.21", "72.28", "72.29"], "C",
    "Krom %0,3’ü ve molibden %0,08’i aştığından çelik Not 1(f) anlamında diğer alaşımlı çeliktir; krom %10,5’in altında olduğu için paslanmaz değildir. Sıcak haddelenmiş, düzensiz sarılmış kangal halindeki ürün filmaşindir; diğer alaşımlı çelikten filmaşin 72.27’dedir. 72.13 alaşımsız, 72.21 paslanmaz filmaşin içindir; 72.28 çubuk ve profilleri, 72.29 soğuk elde edilmiş telleri kapsar.",
    "Fasıl 72 Not 1(e), (f) ve (l); 72.27 pozisyon metni."))

S.append(soru(SENARYO,
    "Bir firma; demir veya alaşımsız çelikten, genişliği 300 mm, kalınlığı 2 mm, rulo halinde, soğuk haddelendikten sonra elektrolitik yolla kalayla kaplanmış şerit ithal etmektedir. Tarife Cetveline göre bu ürün hangi pozisyonda sınıflandırılır?",
    "72.12", ["72.10", "72.11", "72.09", "72.26"], "D",
    "Genişliği 600 mm’den az olan demir veya alaşımsız çelikten yassı hadde ürünleri kaplanmış ise 72.12’dedir; kalayla elektrolitik kaplama metalle kaplamadır. 72.10 genişliği 600 mm veya fazla kaplanmış ürünleri, 72.11 dar ve kaplanmamış ürünleri alır; 72.26 diğer alaşımlı çelik içindir.",
    "72.11 ve 72.12 pozisyon metinleri ve Açıklama Notları; Fasıl 72 Not 1(k)."))

obj["sorular"] = S

if __name__ == "__main__":
    kaydet(obj, 72)
