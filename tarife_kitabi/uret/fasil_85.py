#!/usr/bin/env python3
# Fasıl 85 modülü üreticisi
import json, os

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

E4 = "Eşya → 4’lü pozisyon"
OT = "Olumsuz teşhis"
FA = "Farklı/aynı pozisyon veya fasıl"
FN = "Fasıl notu · Tanım/Eşik"
GY = "Genel Yorum Kuralı"
ES = "Eşleştirme / Boşluk doldurma"
CC = "Çoktan-çoğa (I–IV)"
SN = "Senaryo"

d = {
 "tur": "fasil",
 "fasil": 85,
 "baslik": "Elektrikli makina ve cihazlar ve bunların aksam ve parçaları; ses kaydetmeye ve kaydedilen sesi tekrar vermeye mahsus cihazlar, televizyon görüntü ve seslerinin kaydedilmesine ve kaydedilen görüntü ve sesin tekrar verilmesine mahsus cihazlar ve bunların aksam, parça ve aksesuarı",
 "bolum": "XVI",
 "oz": {
  "vurgu": "Fasıl 85 elektrikli makine ve cihazların faslıdır; ancak “elektrikli olmak” tek başına yetmez. Önce Bölüm XVI Not 1 ve Fasıl 85 Not 1 dışlamalarına, sonra eşyanın 84. Fasılda tanımlı bir makine olup olmadığına bakılır (84’teki makineler elektrikli olsa da orada kalır). Ardından notlarda tanımlanan eşya (akıllı telefon, akıllı kart, düz panel modülü, baskılı devre, LED, yarı iletken, entegre devre), isimle geçen pozisyonlar, parçalar için Bölüm XVI Not 2 ve en sonda artık pozisyon 85.43 gelir.",
  "maddeler": [
   "<b>Enerji grubu (85.01–85.07):</b> motor-jeneratör 85.01, elektrojen grubu 85.02, transformatör-statik konvertör (şarj cihazı, UPS) 85.04, mıknatıslar 85.05, şarj edilemeyen pil 85.06, şarj edilebilir akümülatör 85.07.",
   "<b>Ev, taşıt ve atölye cihazları (85.08–85.16):</b> süpürge 85.08, bünyesinde motoru olan ev cihazı 85.09 (Not 4: 20 kg), traş-kırkma 85.10, motor ateşleme-marş 85.11, taşıt aydınlatma-silecek 85.12, portatif lamba 85.13, sanayi fırını 85.14, kaynak 85.15, ısıyla çalışan ev cihazları 85.16.",
   "<b>İletişim ve ses-görüntü (85.17–85.29):</b> telefon-ağ 85.17, mikrofon-hoparlör 85.18, ses kaydı 85.19, video 85.21 (parçaları 85.22), kayıt mesnetleri 85.23, düz panel modülü 85.24, kamera 85.25, radar-GPS-telsiz kumanda 85.26, radyo 85.27, monitör-TV 85.28 (parçaları 85.29).",
   "<b>İşaret ve devre elemanları (85.30–85.42):</b> trafik işaretleri 85.30, alarm-zil 85.31, kondansatör 85.32, rezistans 85.33, baskılı devre 85.34, anahtar-sigortada 1000 V eşiği (85.35 / 85.36), pano 85.37, ampul 85.39, tüp 85.40; 85.41 ve 85.42 Not 12 ile önceliklidir (85.23 hariç).",
   "<b>Artıklar ve tamamlayıcılar (85.43–85.49):</b> kendine has fonksiyonlu cihaz 85.43, izole kablo 85.44, elektrik kömürleri 85.45, izolatör 85.46, izole edici parçalar 85.47, başka yerde olmayan elektrikli aksam 85.48, e-atık 85.49 (Bölüm XVI Not 6)."
  ]
 },
 "karar_tablosu": {
  "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
  "satirlar": [
   ["1", "Bölüm XVI Not 1 veya Fasıl 85 Not 1 dışlamasına giriyor mu? (elektrikle ısıtılan battaniye-giysi, 70.11 cam zarf, 84.86 makinesi, tıbbi vakum cihazı, ısıtmalı mobilya; Fasıl 90, 91, 95 eşyası; tripod)", "İlgili fasıl / pozisyon (ör. <b>70.11</b>, <b>84.86</b>, <b>90.18</b>, <b>96.20</b>)"],
   ["2", "Orijinal amacı için kullanılamaz hale gelmiş, dökme sevk edilen elektrikli-elektronik hurda veya atık mı?", "<b>85.49</b> (Bölüm XVI Not 6)"],
   ["3", "84. Fasılda tanımlı bir makine mi? (çamaşır, bulaşık makinesi, buzdolabı, klima, fan, bilgisayar, yazıcı-faks)", "Fasıl <b>84</b> (elektrikli olsa da)"],
   ["4", "Not 7 tanımına uyan, ayrı sunulmuş düz panel gösterge modülü mü?", "<b>85.24</b> (diğer pozisyonlara göre öncelikli)"],
   ["5", "Not 12’deki yarı iletken cihaz, LED veya elektronik entegre devre mi?", "<b>85.41</b> / <b>85.42</b> (akıllı kart, flash bellek ise <b>85.23</b>)"],
   ["6", "Fasıl 85’in bir pozisyonunda isim veya tanımla geçiyor mu? (85.09 için Not 4 ağırlık şartı)", "O pozisyon"],
   ["7", "Belirli bir cihaza ait aksam mı?", "Kendi pozisyonu varsa orada; yoksa <b>85.03</b>, <b>85.22</b>, <b>85.29</b>, <b>85.38</b> veya cihazın pozisyonu (Bölüm XVI Not 2)"],
   ["8", "Belirli bir cihaza ait olduğu anlaşılmayan elektrikli aksam mı?", "<b>85.48</b> (elektriksizse <b>84.87</b>)"],
   ["9", "Hiçbiri değilse: kendine has fonksiyonu olan elektrikli cihaz", "<b>85.43</b>"]
  ],
  "dipnot": "* 85.20 pozisyonu boştur (metinde yalnızca köşeli parantez içinde yer alır); bu nedenle pozisyon haritasında gösterilmemiştir."
 },
 "pozisyon_haritasi": [
  ["85.01", "Elektrik motorları ve jeneratörler", "Elektrojen grubu hariç", "Servomotor, dıştan takma bot motoru"],
  ["85.02", "Elektrojen grupları; rotatif konvertörler", "Jeneratör + mekanik hareket ettirici", "Dizel jeneratör seti"],
  ["85.03", "85.01–85.02 makinalarının parçaları", "Sadece veya esas itibarıyla bunlar için", "Stator, rotor, fırça mesnedi"],
  ["85.04", "Transformatör, statik konvertör, endüktör", "Hareketli kısmı olmayan dönüştürücü", "Akü şarj cihazı, UPS, balast"],
  ["85.05", "Mıknatıslar; elektromanyetik kaplin, fren, vinç başı", "Ayrı gelen daimi mıknatıs, kullanım yeri önemsiz", "Oyuncak mıknatıs, manyetik ayna"],
  ["85.06", "Primer (şarj edilemeyen) piller", "Tekrar şarj edilemez", "Alkali kalem pil, düğme pil"],
  ["85.07", "Elektrik akümülatörleri", "Şarj edilebilir; batarya grubu dahil", "Araç aküsü, telefon bataryası"],
  ["85.08", "Vakumlu süpürgeler", "Kuru-ıslak, her tip", "Ev süpürgesi, hayvan tımar vakumu"],
  ["85.09", "Motorlu ev tipi elektromekanik cihazlar", "Motor bünyede; Not 4 (20 kg)", "Mikser, meyve presi, diş fırçası"],
  ["85.10", "Traş, saç kesme, kırkma, epilasyon", "Kendinden elektrik motorlu", "Traş makinesi, epilatör"],
  ["85.11", "Motor ateşleme ve marş tertibatı", "İçten yanmalı motorla çalışır", "Buji, ateşleme bobini, marş motoru"],
  ["85.12", "Taşıt-bisiklet aydınlatma, işaret, silecek", "85.39 ampulleri hariç", "Far, korna, cam silici"],
  ["85.13", "Kendi enerjili portatif lambalar", "Elde veya üstte taşınır", "El feneri, madenci lambası"],
  ["85.14", "Sanayi-laboratuvar elektrik fırınları", "Ev tipi değil", "Ark ocağı, endüstriyel mikrodalga"],
  ["85.15", "Elektrikli lehim ve kaynak makinaları", "Kesebilse de burada", "Ark kaynağı, lehim havyası"],
  ["85.16", "Isıtıcılar, saç kurutucu, ütü, ev elektrotermik", "Isıyla çalışır; rezistanslar dahil", "Fön, kettle, tost makinesi"],
  ["85.17", "Telefonlar ve ağ iletişim cihazları", "Ses-görüntü-veri alır/verir", "Akıllı telefon, modem, router"],
  ["85.18", "Mikrofon, hoparlör, kulaklık, amplifikatör", "Ayrı gelen; kullanım yeri önemsiz", "Kulaklık, kablosuz mikrofon seti"],
  ["85.19", "Ses kayıt ve tekrar verme cihazları", "Yalnız ses", "Pikap, MP3 çalar, telesekreter"],
  ["85.21", "Video kayıt veya gösterme cihazları", "Görüntü ve ses", "DVD oynatıcı, dijital video kaydedici"],
  ["85.22", "85.19 ve 85.21 aksam-aksesuarı", "Kafalar, okuyucular", "Lazer okuyucu, pikap iğnesi safiri"],
  ["85.23", "Kayıt mesnetleri", "Kayıtlı olsun olmasın", "USB bellek, DVD, akıllı kart"],
  ["85.24", "Düz panel gösterge modülleri", "Not 7; video dönüştürücü yok", "LCD/OLED dokunmatik modül"],
  ["85.25", "Yayın vericileri; TV, dijital, video kameralar", "Görüntüyü elektronik veriye çevirir", "Dijital fotoğraf makinesi, webcam"],
  ["85.26", "Radar, telsiz seyrüsefer, telsiz kumanda", "Radyo dalgası esaslı", "GPS alıcısı, model uçak kumandası"],
  ["85.27", "Radyo yayını alıcıları", "Kayıt veya saat olsun olmasın", "Oto radyosu, saatli radyo"],
  ["85.28", "Monitör, projektör, TV alıcısı", "Tuner varsa TV alıcısı", "Bilgisayar monitörü, uydu alıcısı"],
  ["85.29", "85.24–85.28 aksam ve parçaları", "Anten, kabin, şasi", "Çanak anten, TV kasası"],
  ["85.30", "Trafik kontrol ve işaret cihazları", "Yol, demiryolu, liman, havaalanı", "Trafik ışığı, demiryolu sinyali"],
  ["85.31", "Sesli veya görüntülü işaret cihazları", "85.12 ve 85.30 dışı", "Kapı zili, siren, yangın alarmı"],
  ["85.32", "Elektrik kondansatörleri", "Sabit, değişken, ayarlanabilir", "Elektrolitik kondansatör"],
  ["85.33", "Rezistanslar (ısıtıcı hariç)", "Reosta, potansiyometre dahil", "Termistör, varistör"],
  ["85.34", "Baskılı devreler", "Not 8; yalnız baskıyla elde", "Boş baskılı devre kartı"],
  ["85.35", "Anahtarlama-koruma teçhizatı (1000 V üstü)", "Yüksek gerilim", "Yük ayırıcı, paratoner"],
  ["85.36", "Anahtarlama-koruma (1000 V’a kadar); optik lif konnektörü", "Alçak gerilim", "Anahtar, röle, fiş, priz, duy"],
  ["85.37", "Kontrol-dağıtım panoları; sayısal kontrol", "85.35/85.36 cihazından en az iki", "Elektrik panosu, PLC"],
  ["85.38", "85.35–85.37 aksam ve parçaları", "Boş pano dahil", "Cihazsız pano"],
  ["85.39", "Ampuller, ark lambaları, LED ışık kaynakları", "Not 11: modül veya ampul", "Halojen ampul, floresan, LED ampul"],
  ["85.40", "Termiyonik, soğuk ve foto katotlu tüpler", "Elektron yayımı esaslı", "Katot ışınlı tüp, magnetron"],
  ["85.41", "Yarı iletkenler, LED, FV hücre, piezo kristal", "Not 12(a); öncelikli", "Diyot, transistör, güneş pili"],
  ["85.42", "Elektronik entegre devreler", "Not 12(b); öncelikli", "İşlemci, bellek çipi, MCO"],
  ["85.43", "Kendine has fonksiyonlu elektrikli cihazlar", "Fasılın artık pozisyonu", "E-sigara, IR kumanda, metal dedektörü"],
  ["85.44", "İzole tel ve kablolar; fiber optik kablo", "İzolasyon şart; fişli dahil", "Uzatma kablosu, koaksiyel kablo"],
  ["85.45", "Elektrik işlerinde kömür-grafit eşya", "Elektrot, fırça, pil kömürü", "Kömür fırça, ark ocağı elektrodu"],
  ["85.46", "Elektrik izolatörleri", "Her türlü maddeden", "Porselen veya cam izolatör"],
  ["85.47", "İzole edici bağlantı parçaları; izoleli boru", "Tamamen izole edici madde", "Bobin göbeği, duy iç gövdesi"],
  ["85.48", "Başka yerde olmayan elektrikli aksam", "Belirli makineye ait değil", "Ortak kullanımlı elektrikli parça"],
  ["85.49", "Elektrikli ve elektronik hurda-atık", "Bölüm XVI Not 6", "Hurda devre kartı, bitmiş akü"]
 ],
 "notlar": [
  ["Bölüm XVI Not 1", "Bölüm dışı (Fasıl 85 bakımından önemlileri): 40.10 ve 40.16’daki kauçuk eşya; 42.05 deri, 43.03 kürk eşya; her maddeden masura, makara, bobin ve benzeri mesnetler; genel kullanıma elverişli adi metal (Bölüm XV) veya plastik (Fasıl 39) aksam; Fasıl 82 ve 83 eşyası; Bölüm XVII, Fasıl 90, Fasıl 91 ve Fasıl 95 eşyası; makine parçası fırçalar (96.03); daktilo şeritleri (96.12); monopod, bipod, tripod (96.20). Kıymetli taşlar da hariçtir, ancak pikap iğneleri için işlenmiş fakat monte edilmemiş safir ve elmaslar 85.22’dedir."],
  ["Bölüm XVI Not 2", "Aksam-parça (84.84, 85.44, 85.45, 85.46, 85.47 eşyasının parçaları hariç): (a) Kendisi 84 veya 85. Fasılda bir pozisyona giren parça, hangi makineye ait olursa olsun o pozisyonda kalır (84.09, 84.31, 84.48, 84.66, 84.73, 84.87, 85.03, 85.22, 85.29, 85.38, 85.48 hariç). (b) Sadece veya esas itibarıyla belli bir makinede kullanılan parça o makinenin pozisyonunda veya hale göre 85.03, 85.22, 85.29, 85.38’de; 85.17 ile 85.25–85.28 eşyasında aynı derecede kullanılanlar 85.17’de; esas itibarıyla 85.24 eşyası ile kullanılanlar 85.29’da. (c) Diğerleri bu parça pozisyonlarında, bu da mümkün değilse 84.87 veya 85.48’de."],
  ["Bölüm XVI Not 3", "Bir bütün oluşturmak üzere birlikte monte edilmiş karma makineler ile tamamlayıcı veya değişik işlemler yapan makineler, metinde aksi belirtilmedikçe, esas fonksiyonuna göre tek makine gibi sınıflandırılır."],
  ["Bölüm XVI Not 4", "Açıkça belirlenmiş tek bir fonksiyonu birlikte yerine getiren ayrı elemanlardan (boru, kablo vb. ile bağlı olsun olmasın) oluşan makine, bir bütün olarak bu fonksiyona uygun pozisyonda sınıflandırılır (fonksiyonel birim)."],
  ["Bölüm XVI Not 5", "Bu notlar anlamında “makina”: 84 veya 85. Fasıllara giren her türlü makine, cihaz, tertibat, alet ve malzeme."],
  ["Bölüm XVI Not 6", "“Elektrikli ve elektronik hurda ve atık”: kırılma, kesilme vb. ile orijinal amacı için kullanılamaz hale gelmiş veya tamiri ekonomik olmayan ve taşıma-yükleme sırasında tek tek korunacak şekilde paketlenmemiş elektrikli-elektronik montajlar, baskılı devre kartları ve eşya. Bunların diğer hurda ve atıklarla karışık sevkiyatı 85.49’dadır. Fasıl 38 Not 4’teki şehir atıkları bu bölüm dışıdır."],
  ["Bölüm XVI Genel Açıklamalar (VII)", "Fasıl 85’teki fonksiyonel birim örnekleri: jeneratör veya transformatör ile kaynak başlarından oluşan kaynak teçhizatı (85.15); portatif telsiz telefon ve el mikrofonu (85.17); yardımcı güç istasyonlu radar (85.26); anten çanağı, LNB ve kumandalı uydu TV alıcı sistemi (85.28); kızılötesi lamba ve zilli hırsız alarmı (85.31). Kapalı devre video gözetleme sistemleri ise fonksiyonel birim sayılmaz; her eleman kendi pozisyonunda."],
  ["Fasıl 85 Not 1", "Fasıl dışı: (a) elektrikle ısıtılan battaniye, yatak örtüsü, yastık, ayak ısıtıcısı ve benzerleri; elektrikle ısıtılan giyim eşyası, ayakkabı, kulak koruyucusu ve üstte taşınan diğer eşya; (b) 70.11 cam eşya; (c) 84.86 makine ve cihazları; (d) tıp, cerrahi, dişçilik ve veterinerlikte kullanılan vakum cihazları (90.18); (e) Fasıl 94’teki elektrikle ısıtılan mobilyalar."],
  ["Fasıl 85 Not 2", "85.01–85.04’e 85.11, 85.12, 85.40, 85.41 veya 85.42’de tarif edilen eşya girmez. Ancak metal tanklı cıva buharlı redresörler 85.04’te kalır."],
  ["Fasıl 85 Not 3", "85.07’deki akümülatörler; enerji depolama ve sunma fonksiyonunu destekleyen veya akümülatörü hasardan koruyan yardımcı bileşenlerle (elektrik konektörü, termistör gibi ısı kontrol cihazı, devre koruyucu) sunulanları da kapsar; koruyucu bir gövde içerebilir."],
  ["Fasıl 85 Not 4", "85.09 yalnız ev işlerinde kullanılan türden şu elektromekanik cihazları kapsar: (a) ağırlığı ne olursa olsun yer cilalama makinaları, gıda öğütücü ve karıştırıcıları, meyve ve sebze presleri; (b) ağırlığı <b>20 kg</b>’ı geçmeyen diğer cihazlar. Hariç: fan ve aspiratörlü davlumbaz (84.14), santrifüjlü çamaşır kurutucu (84.21), bulaşık makinesi (84.22), ev tipi çamaşır makinesi (84.50), ütü makinaları (84.20 veya 84.51), dikiş makinesi (84.52), elektrikli makas (84.67), elektrotermik cihazlar (85.16)."],
  ["Fasıl 85 Not 5", "85.17 anlamında “akıllı telefon”: mobil işletim sistemi bulunan, üçüncü taraf uygulamalar dahil birden fazla uygulamayı aynı anda indirip çalıştırma gibi otomatik bilgi işlem makinesi işlevlerini yerine getiren, dijital kamera ve seyrüsefer yardımı gibi özelliklerle entegre olabilen hücresel ağ telefonları."],
  ["Fasıl 85 Not 6(a)", "85.23 anlamında “katı halde kalıcı (uçucu olmayan) bellek cihazları”: bağlantı soketi bulunan, baskılı devre kartına monte entegre devre şeklinde bir veya daha fazla flash belleği aynı kabin içinde içeren bellek cihazları; kontrol entegre devresi ile kapasitör ve direnç gibi küçük münferit pasif elemanlar içerebilir."],
  ["Fasıl 85 Not 6(b)", "“Akıllı kart”: içine çip şeklinde bir veya daha fazla elektronik entegre devre (mikroişlemci, RAM veya ROM) yerleştirilmiş kart. Kontak, manyetik şerit veya yerleştirilmiş anten içerebilir; bunlardan başka <b>aktif veya pasif devre elemanı içermez</b>."],
  ["Fasıl 85 Not 7", "85.24 anlamında “düz panel gösterge modülleri”: kullanımdan önce başka pozisyonlardaki ürünlere dahil edilmek üzere tasarlanmış, asgari olarak bir görüntüleme ekranı ile donatılmış, bilgi görüntülemeye mahsus cihazlar. Ekran düz, kavisli, esnek, katlanabilir veya gerilebilir olabilir; video sinyallerini alma ve piksellere tahsis için gerekli unsurları içerebilir. Video sinyallerini dönüştüren bileşenlerle (ölçekleyici IC, kod çözücü IC, uygulama işlemcisi) donatılmış veya başka pozisyondaki eşyanın karakterini taşıyan modüller hariçtir. Bu tanıma uyan modüller için 85.24 diğer pozisyonlara göre <b>önceliklidir</b>."],
  ["Fasıl 85 Not 8", "85.34 anlamında “baskılı devreler”: yalıtıcı zemin üzerinde baskı işlemiyle (kakma, elektriksel kaplama, asitle yedirme) veya film tekniğiyle elde edilen bağlantı elemanları, kontaklar veya diğer baskılı elemanların (endüktans, direnç, kapasitör) önceden hazırlanmış şemaya göre düzenlenmesiyle oluşan devreler; sinyal üreten, doğrultan, modüle eden veya büyülten elemanlar (yarı iletkenler) hariç. Baskı işlemi dışında elde edilen elemanlarla birleştirilmiş devreler ile tek, ayrık direnç, kapasitör ve endüktanslar baskılı devre değildir; baskılı olmayan bağlantı elemanları takılabilir. Aynı teknik işlemle elde edilmiş aktif ve pasif elemanları içeren ince veya kalın film devreleri 85.42’dedir."],
  ["Fasıl 85 Not 9", "85.36’daki “optik lif, optik lif demeti veya kablosu için konnektörler”: dijital telekomünikasyon sisteminde optik lifleri uç uca yalnızca mekanik olarak hizalayan elemanlar; sinyali yükseltme, yeniden üretme veya düzeltme gibi başka işlevleri yoktur."],
  ["Fasıl 85 Not 10", "85.37, televizyon uzaktan kumandaları için kordonsuz kızılötesi cihazları ve başka elektrik teçhizatını kapsamaz (85.43)."],
  ["Fasıl 85 Not 11", "85.39’daki “LED ışık kaynakları”: (a) LED modüller: elektrik devresi şeklinde düzenlenmiş, elektriksel, mekanik, termal ve optik elemanlar ile güç kaynağı veya güç kontrolü için 85.36 veya 85.42 eşyası içerebilen modüller; (b) LED ampuller: bir veya daha fazla LED modül içeren ampuller. Fark: LED ampul, aydınlatma cihazına kolay takılıp değiştirilmesini ve elektriksel veya mekanik teması sağlayan bir <b>kapağa (tabana)</b> sahiptir; modülde bu kapak yoktur."],
  ["Fasıl 85 Not 12(a)", "“Yarı iletken cihazlar”: çalışması bir elektrik alanının uygulanmasıyla direnç değişikliğine bağlı olan cihazlar ile yarı iletken tabanlı dönüştürücüler (sensör, aktüatör, rezonatör, osilatör). “LED”: elektrik enerjisini görünür, kızılötesi veya morötesi ışınlara dönüştüren yarı iletken cihazlar; 85.41’deki LED’ler güç kaynağı veya güç kontrolü elemanı içermez."],
  ["Fasıl 85 Not 12(b)", "“Elektronik entegre devreler”: monolitik, hibrit (pasif elemanlar film tekniğiyle, aktif elemanlar yarı iletken tekniğiyle, yalıtkan yekpare zeminde ayrılmaz biçimde), çoklu çip (başka aktif veya pasif eleman içermeyen) ve çok komponentli entegre devreler (MCO). Bu notta tarif edilen eşya için 85.41 ve 85.42, <b>85.23 hariç</b>, fonksiyonları dolayısıyla girebilecekleri diğer bütün pozisyonlara göre öncelik alır."],
  ["Genel Açıklamalar", "Fasıl 85; 84. Fasıla dahil makineler (elektrikli olsalar dahi) ve Bölüm XVI dışında bırakılan eşya hariç bütün elektrikli makine ve cihazları kapsar. Bu fasıldaki eşya seramik veya camdan yapılmış olsa da (70.11 cam zarflar hariç) bu fasılda kalır."],
  ["Genel Açıklamalar", "Elektrikli ısıtma cihazlarının çoğu başka fasıllardadır: elektrikli buhar kazanı 84.02, klima 84.15, 84.19 cihazları, kalender 84.20, kuluçka makinesi 84.36, kızgın demirle markalama 84.79, tıbbi cihaz 90.18. Fasıl 85’te elektrotermik cihazların yalnız bazı tipleri yer alır: başlıca 85.14 (sanayi-laboratuvar fırınları) ve 85.16 (mahal ısıtıcıları, ev tipi elektrotermik cihazlar)."],
  ["Genel Açıklamalar", "85.23’e girmeyen bellek modülleri (SIMM, DIMM) ve 85.42’deki MCO’lar Bölüm XVI Not 2’ye göre: yalnız veya esas olarak otomatik bilgi işlem makinesiyle kullanılanlar 84.73; başka belirli makine için olanlar o makinenin parçası; esas kullanım belirlenemiyorsa 85.48."],
  ["Genel Açıklamalar", "Elektriksiz aksam: pompa ve fan (84.13, 84.14), musluk-vana (84.81), rulman (84.82), mil-dişli (84.83) kendi pozisyonlarında; belli bir cihaza özgü olanlar cihazın pozisyonunda veya 85.03, 85.22, 85.29, 85.38’de; diğerleri 84.87’de."],
  ["Fasıl 84 Not 6(D)", "84.71, şartları taşısalar bile şunları kapsamaz: yazıcı, fotokopi ve faks makineleri (84.43); kablolu veya kablosuz ağlarda ses, görüntü veya veri alışverişi sağlayan cihazlar (85.17); hoparlör ve mikrofonlar (85.18); TV kameraları, dijital fotoğraf makineleri ve video kamera kaydediciler (85.25); TV alıcı tertibatı olmayan monitör ve projektörler (85.28)."],
  ["85.09 Açıklama Notu", "“Ev işlerinde kullanılan” cihaz, ev ihtiyaçlarının üzerinde bir seviyede çalışmayan cihazdır. Bünyesi dışındaki ayrı bir motorla (esnek mil, kayış) çalışanlar ve açıkça sanayi tipi olanlar hariçtir (genellikle 82.10 veya Fasıl 84). 20 kg sınırının hesabında ekstra değiştirilebilir parçalar ve yardımcı tertibat dikkate alınmaz."],
  ["85.24 Açıklama Notu", "Başka cihaza entegre edilmeden ayrı sunulan düz panel modülü, bitmiş ürünün pozisyonunda değil 85.24’te; cihaza entegre edilmiş modül ise cihazla birlikte sınıflandırılır. Modülün aksam-parçaları 85.29’dadır."],
  ["85.28 Açıklama Notu", "Monitör veya projektör bir televizyon ayarlayıcısı (tuner) içeriyorsa televizyon alıcısı kabul edilir. 84.71 makineleri için monitörler: kanal seçici ve video tuneri yok, bilgisayar konektörleri (VGA, DVI, HDMI, DP), görüntü boyutu genellikle 76 cm’i aşmaz, nokta aralığı genellikle 0,3 mm’den küçük. Yalnızca yüksek frekanslı TV sinyalini ayıran basit ayarlayıcılar 85.29’dadır."],
  ["85.35 / 85.36 Açıklama Notları", "Anahtar, sigorta, devre kesici, dalga bastırıcı, fiş-priz ve bağlantı kutuları: gerilimi <b>1000 voltu geçen</b> devreler için 85.35, <b>geçmeyenler</b> için 85.36. Bunlardan birleştirilmiş halde olanlar (basit anahtar takımları hariç) 85.37; kablo ucuna takılı fiş-priz 85.44; varistör 85.33; otomatik voltaj regülatörü 90.32."],
  ["85.43 Açıklama Notu", "Fasıl 85’in başka pozisyonunda yer almayan, kendine has fonksiyonu olan elektrikli cihazlar: tanecik hızlandırıcıları, sinyal jeneratörleri, elektroliz-elektrokaplama cihazları, e-sigaralar, metal dedektörleri, ses karıştırma cihazları, yüksek-orta frekans amplifikatörleri, kızılötesi uzaktan kumandalar, uçuş veri kaydedicileri (kara kutu), elektrikli çit enerji sistemleri. Tek kullanımlık e-sigara ve sıvı kartuşları 24.04’tedir."],
  ["85.49 Açıklama Notu", "Sadece kullanılmış olmak e-atık sayılmaya yetmez; eşya yalnız geri kazanım, geri dönüşüm veya bertarafa uygun olmalıdır. Genellikle dökme sevk edilir ve ağırlıkla alınıp satılır; tek tek koruyucu ambalaja sarılıp kutulanmış televizyon, telefon veya piller e-atık sayılmaz. Atık, hurda veya bitmiş primer pil ve akümülatörler de e-atıktır. Radyoaktif atık 28.44, tasnif edilmemiş şehir atığı 38.25."]
 ],
 "sinir_komsulari": [
  ["Ev tipi bulaşık ve çamaşır makinesi, buzdolabı, vantilatör, aspiratörlü davlumbaz", "84.22 / 84.50 / 84.18 / 84.14", "Fasıl 85 Not 4 ve 85.09 hariç tutmaları; elektrikli olsa da Fasıl 84"],
  ["Faks makinesi, yazıcı", "84.43", "85.17 hariç tutması; Fasıl 84 Not 6(D)"],
  ["Bilgisayar bellek modülü (DIMM, SIMM)", "84.73", "85.23’e girmez; Bölüm XVI Not 2(b)"],
  ["Elektrikle ısıtılan battaniye, giysi, ayakkabı; ısıtmalı mobilya", "Kendi pozisyonu / Fasıl 94", "Fasıl 85 Not 1(a) ve (e)"],
  ["Tıbbi vakum cihazı; göz cerrahisi elektromıknatısı; boğaz-kulak muayene lambası", "90.18", "Fasıl 85 Not 1(d); 85.05 ve 85.13 hariç tutmaları"],
  ["Tek kullanımlık e-sigara; e-sigara sıvı kartuşu", "24.04", "85.43 hariç tutması"],
  ["Motorlu taşıt ampulü, monoblok far ünitesi", "85.39", "85.12 metnindeki “85.39 eşyası hariç” kaydı"],
  ["Otomobil cam silicisi, korna, park sensörü", "85.12", "Bölüm XVII Not 2(f): Fasıl 85 eşyası 87.08 parçası sayılmaz"],
  ["Termistör, varistör (voltaja bağlı direnç)", "85.33", "85.41 hariç tutması; varistör diyot ise 85.41"],
  ["Diyotlarla donatılmış, gücü doğrudan motora veren güneş paneli", "85.01", "Elemansız modül-panel 85.41’de kalır"],
  ["Ampul ve tüpler için cam zarf; katot ışınlı tüp cam konisi", "70.11", "Fasıl 85 Not 1(b)"],
  ["X ışını tüpü; radyoaktif duman dedektörlü yangın alarmı", "90.22", "85.40 ve 85.31 hariç tutmaları"],
  ["Otomatik voltaj regülatörü", "90.32", "85.04, 85.35 ve 85.36 hariç tutmaları"],
  ["İşitme cihazı; havacı başlığı (kulaklıklı)", "90.21 / 65.06", "85.18 hariç tutmaları"],
  ["Monopod, bipod, tripod", "96.20", "Bölüm XVI Not 1(r)"]
 ],
 "tuzaklar": [
  "<b>Elektrikli olmak Fasıl 85 demek değildir.</b> 84. Fasılda tanımlı makineler elektrikli olsalar da orada kalır: bulaşık makinesi 84.22, çamaşır makinesi 84.50, buzdolabı 84.18, klima 84.15, bilgisayar 84.71, faks 84.43.",
  "<b>85.09’da 20 kg sınırının üç istisnası vardır.</b> Yer cilalama makinası, gıda öğütücü-karıştırıcı ve meyve-sebze presi ağırlıktan bağımsız 85.09’dadır; diğer ev cihazları 20 kg’a kadar. Isıyla çalışan ev cihazı (fön, tost makinesi, kettle) 85.16’ya gider.",
  "<b>Uzaktan kumanda: radyo dalgası mı, kızılötesi mi?</b> Telsiz (radyo) ile uzaktan kontrol 85.26; televizyon ve video kaydedicilerin kordonsuz kızılötesi kumandası 85.43 (Not 10: 85.37 değil).",
  "<b>LED: diyot mu, ışık kaynağı mı?</b> Tek LED, LED paketi veya güç kontrol devresi olmayan LED grubu 85.41; güç kontrollü LED modül ve taban-kapaklı LED ampul 85.39 (Not 11). Lazer diyotu da 85.41’dedir; lazer diyotlu lazer ibresi ise 90.13.",
  "<b>Akıllı kart ve flash bellek çip içerse de 85.42 değildir.</b> Not 12 önceliği 85.23 karşısında işlemez; ikisi de 85.23’tedir. Akıllı karta kapasitör-direnç eklenemez, flash belleğe eklenebilir. Bellek modülü (DIMM) ise 84.73’tür.",
  "<b>Pil ≠ akümülatör.</b> Şarj edilemeyen pil 85.06; kalem pil görünümlü şarjlı pil ve batarya grubu 85.07. Cep telefonu aküsü 85.29 değil 85.07’dir. Bitmiş veya hurda pil ve akümülatörler 85.49.",
  "<b>Kendi pozisyonu olan parça, makine parçası olarak sınıflandırılmaz.</b> Motora ait kömür fırça 85.45, motor içindeki kondansatör 85.32, vincin elektromanyetik başı 85.05 (Bölüm XVI Not 2(a)). Fırça mesnedi ise 85.03’tür.",
  "<b>Düz panel modülü ayrı gelirse 85.24’tür.</b> Buzdolabı, telefon veya bilgisayar için tasarlanmış olsa da Not 7 önceliği nedeniyle 85.24; video dönüştürücü bileşen (ölçekleyici, kod çözücü, uygulama işlemcisi) içeriyorsa 85.24 dışına çıkar.",
  "<b>1000 volt eşiği.</b> Anahtar, sigorta, fiş-priz 1000 V’a kadar 85.36, üstünde 85.35; iki veya daha fazla cihazla donatılmış pano 85.37, cihazsız boş pano 85.38; kablo ucuna takılı fiş 85.44.",
  "<b>Tek kullanımlık e-sigara Fasıl 24’tedir.</b> Şarj edilebilir veya yeniden doldurulabilir cihaz 85.43; atılan tek kullanımlık cihaz ile sıvı kartuşu veya tankı 24.04."
 ],
 "hafiza": {
  "kanca": "ENERJİ → EV → İLETİŞİM → İŞARET → DEVRE → ARTIK → KABLO-ATIK",
  "aciklama": "<b>ENERJİ</b> 85.01–85.07 (motor, trafo, mıknatıs, pil, akü) · <b>EV</b> ve taşıt 85.08–85.16 (süpürge, mikser, traş, buji, far, fener, fırın, kaynak, ısıtıcı) · <b>İLETİŞİM</b> 85.17–85.29 (telefon, mikrofon, kayıt, mesnet, ekran modülü, kamera, radar, radyo, TV) · <b>İŞARET</b> 85.30–85.31 (trafik ışığı, alarm) · <b>DEVRE</b> 85.32–85.42 (kondansatör, rezistans, baskılı devre, anahtar, pano, ampul, tüp, yarı iletken, çip) · <b>ARTIK</b> 85.43 · <b>KABLO-ATIK</b> 85.44–85.49 (kablo, kömür, izolatör, izole parça, elektrikli aksam, e-atık). Görsel benzetme: bir binaya elektrik gelir (enerji), evdeki cihazlar çalışır, odada telefon ve TV vardır, kapıda zil çalar, duvarın içinde devreler ve panolar, en altta kablolar ve çöp kutusu."
 },
 "sinav_odagi": [
  "Tek bir eşyanın 4’lü pozisyonu: elektromanyetik frenler (85.05), pil kömürleri (85.45), elektromanyetik dalgalarla çalışan uzaktan kumanda (85.26), otomobil cam silicisi (85.12); çeldiriciler 84, 87 ve 90. Fasıllardan seçilmiştir.",
  "“Hangisi 85.28’de sınıflandırılmaz?” kalıbı: bilgisayar monitörü, video monitörü ve TV alıcısı 85.28’de; katot ışınlı TV görüntü tüpü ise 85.40’tadır.",
  "Fasıl notu tanımları: 85.24 düz panel gösterge modülünün özellikleri (esnek olabilir, başka eşyaya monte edilmek üzere tasarlanır, video dönüştürücü bileşen içermez) ve notlarda açıklaması bulunan eşya (akıllı kart, baskılı devre, LED ampul, hibrit entegre devre); dizüstü bilgisayar için LCD ekran modülü gibi modül-parça ayrımı (bugünkü Not 7’ye göre 85.24).",
  "Fasıl 84 ile sınır: 84.68 makinesinin elektriklisinin 85.15’te olması; “fırın”ın 73.21, 84.17, 85.14 ve 85.16’da bulunup 85.09’da bulunmaması.",
  "Boşluk doldurma ve sıralama: e-sigara 85.43 / kartuşu 24.04 / sigara 24.02; pozisyon numarasına göre sıralama (transformatör – pilli el feneri – baskılı devre – kullanılmış pil; cep radyosu, MP3 çalar, DVD oynatıcı, video monitör).",
  "Fasıl dışına itilen elektronik eşya: kameralı uzaktan kumandalı drone (Fasıl 88), piyano ile birlikte gelen hafıza kartı (piyano aksesuarı, Fasıl 92), elektrikli çelenk (94.05).",
  "Aynı fasıl / bölüm soruları: mikrofon, boş CD ve LED ampul (Fasıl 85) ile buhar türbininin (Fasıl 84) aynı fasılda olmaması; GYK 6 ile alt pozisyon karşılaştırmasında Fasıl 85 eşyasının kullanılması."
 ],
 "cikmis_ornekler": [
  {
   "soru": "Aşağıdakilerden hangisi Tarife Cetvelinde 85.28 tarife pozisyonunda <b>sınıflandırılmaz</b>?",
   "secenekler": ["Bilgisayar monitörü", "Video monitörü", "TV alıcı cihazları", "Katot ışınlı TV görüntü tüpü"],
   "cevap": "D",
   "aciklama": "Katot ışınlı tüpler 85.40’tadır; 85.29 Açıklama Notu da bunları ve parçalarını 85.40’a gönderir. Bilgisayar ve video monitörleri ile TV alıcıları 85.28’in kapsamındadır."
  },
  {
   "soru": "Tarife Cetveline göre 85.24 tarife pozisyonunda yer alan eşya için aşağıdaki ifadelerden hangisi <b>yanlıştır</b>?",
   "secenekler": ["Esnek olabilir", "Başka eşyalara monte edilmek üzere tasarlanmışlardır", "Bir görüntüleme ekranı içerir", "Likit kristal olabilir", "Video sinyallerini dönüştürmek için bileşenler içerir"],
   "cevap": "E",
   "aciklama": "Fasıl 85 Not 7’ye göre ölçekleyici IC, kod çözücü IC veya uygulama işlemcisi gibi video sinyallerini dönüştüren bileşenlerle donatılmış modüller 85.24’e girmez. Esnek ekran, başka ürüne dahil edilme amacı, görüntüleme ekranı ve LCD teknolojisi tanımın parçasıdır."
  }
 ],
 "ozet": [
  "Elektrikli makine önce 84. Fasılda aranır; orada tanımlıysa (bulaşık, çamaşır, buzdolabı, klima, bilgisayar, yazıcı) elektrikli olsa da 84’tedir.",
  "85.09: motor bünyede ve ev tipi; yer cilalama, gıda öğütücü-karıştırıcı, meyve-sebze presi ağırlıksız, diğerleri 20 kg’a kadar. Isıyla çalışan ev cihazı 85.16.",
  "Not 7 ve Not 12 öncelik verir: ayrı gelen düz panel modülü 85.24; yarı iletken ve entegre devre 85.41 / 85.42; fakat akıllı kart ve flash bellek 85.23.",
  "Parça kuralı (Bölüm XVI Not 2): kendi pozisyonu olan parça orada; belli cihaza özgü parça cihazın pozisyonunda veya 85.03, 85.22, 85.29, 85.38’de; ortak elektrikli parça 85.48.",
  "Uzaktan kumanda: telsiz 85.26, kızılötesi 85.43. Pil: şarjsız 85.06, şarjlı 85.07. Anahtar: 1000 V’a kadar 85.36, üstü 85.35; pano 85.37.",
  "LED: tek diyot 85.41; güç kontrollü modül veya kapaklı ampul 85.39. Baskılı devre yalnız pasif ve baskıyla elde edilmiş elemanlarla 85.34.",
  "E-atık 85.49; tek kullanımlık e-sigara 24.04, yeniden doldurulabilir cihaz 85.43; artık pozisyon 85.43."
 ],
 "sorular": [
  # 1 E4 – D
  {
   "soru": "Tarife Cetveline göre, vinçlerde demir hurda ve artıklarını kaldırmak için kullanılan, esas itibarıyla yuvarlak bir elektromıknatıstan oluşan elektromanyetik vinç başı ayrı olarak getirildiğinde hangi tarife pozisyonunda sınıflandırılır?",
   "secenekler": ["84.26", "84.31", "85.43", "85.05", "85.48"],
   "cevap": "D",
   "tip": E4,
   "gerekce": "85.05 pozisyon metni “elektromanyetik vinç başları”nı ismen sayar. Bölüm XVI Not 2(a) uyarınca kendisi 84 veya 85. Fasılda bir pozisyona giren parça, hangi makineye ait olursa olsun o pozisyonda kalır; bu nedenle vinç parçası olarak 84.31’e gitmez. 84.26 vincin kendisidir; 85.43 ve 85.48 artık pozisyonlardır.",
   "dayanak": "85.05 pozisyon metni ve Açıklama Notu (6); Bölüm XVI Not 2(a)."
  },
  # 2 OT – B
  {
   "soru": "Tarife Cetveline göre, ev işlerinde kullanılan türden, kendinden elektrik motorlu ve ağırlığı 20 kg’ı geçmeyen aşağıdaki cihazlardan hangisi 85.09 pozisyonunda <b>sınıflandırılmaz</b>?",
   "secenekler": ["Elektrikli diş fırçası", "Ev tipi bulaşık yıkama makinesi", "Mutfak evyesine monte edilen artık öğütücü", "Hava nemlendirici", "Ev tipi meyve ve sebze presi"],
   "cevap": "B",
   "tip": OT,
   "gerekce": "Fasıl 85 Not 4, bulaşık yıkama makinelerini açıkça 85.09 dışında bırakır; bunlar 84.22’dedir. Elektrikli diş fırçası, mutfak artığı öğütücü ve hava nemlendirici 85.09 Açıklama Notunda 20 kg’ı geçmeyen cihazlar arasında sayılır; meyve ve sebze presi ise ağırlığı ne olursa olsun 85.09’dadır. Tuzak, “ev tipi ve motorlu” olmayı yeterli sanmaktır.",
   "dayanak": "Fasıl 85 Not 4; 85.09 Açıklama Notu."
  },
  # 3 FN – A
  {
   "soru": "Fasıl 85 Not 4’e göre, ev işlerinde kullanılan türden aşağıdaki elektromekanik cihazlardan hangisi ağırlığı 20 kg’ı geçse dahi 85.09 pozisyonunda kalır?",
   "secenekler": ["Yer cilalama makinası", "Ev tipi nem giderici", "Mutfak artıklarını öğüterek yok eden cihaz", "Ekmek ve peynir dilimleme cihazı", "Yer fırçalama ve kirli suyu emme cihazı"],
   "cevap": "A",
   "tip": FN,
   "gerekce": "Not 4(a), yer cilalama makinaları, gıda maddelerini öğütücü ve karıştırıcılar ile meyve-sebze preslerini ağırlıklarına bakılmaksızın 85.09’a alır. Nem giderici, mutfak artığı öğütücü, dilimleme cihazı ve yer fırçalama-emme cihazı Açıklama Notunda (B) grubunda, yani ancak 20 kg’ı geçmezse 85.09’da yer alan cihazlar arasındadır. Tuzak, mutfak artığı öğütücüyü “gıda öğütücüsü” sanmaktır.",
   "dayanak": "Fasıl 85 Not 4(a) ve (b); 85.09 Açıklama Notu (A) ve (B)."
  },
  # 4 FA – E
  {
   "soru": "Tarife Cetveline göre aşağıdaki elektrikli cihazlardan hangisi diğerlerinden farklı bir tarife pozisyonunda sınıflandırılır?",
   "secenekler": ["Televizyon alıcıları için kordonsuz kızılötesi uzaktan kumanda", "Bilinen dalga boyunda elektrik sinyali üreten sinyal jeneratörü", "Gıda maddelerinde yabancı metal arayan maden dedektörü", "Ses kaydında mikrofon seslerini birleştiren ses karıştırma cihazı", "Model uçakların telsiz ile uzaktan kontrolüne mahsus cihaz"],
   "cevap": "E",
   "tip": FA,
   "gerekce": "Model uçak, gemi, oyuncak ve pilotsuz uçakların radyo (telsiz) ile uzaktan kontrolüne mahsus cihazlar 85.26’dadır. Kızılötesi TV kumandası (Not 10), sinyal jeneratörü, maden dedektörü ve ses karıştırma cihazı 85.43 Açıklama Notunda sayılır. Tuzak, “uzaktan kumanda” ortak adına bakmaktır; belirleyici olan radyo dalgası ile kızılötesi ayrımıdır.",
   "dayanak": "85.26 Açıklama Notu (11); Fasıl 85 Not 10; 85.43 Açıklama Notu."
  },
  # 5 E4 – C
  {
   "soru": "Tarife Cetveline göre, otomatik bilgi işlem makinesine takılarak yerel alan ağına (LAN) bağlantı sağlayan Ethernet arabirim kartı (ağ kartı) hangi tarife pozisyonunda sınıflandırılır?",
   "secenekler": ["84.71", "84.73", "85.17", "85.42", "85.43"],
   "cevap": "C",
   "tip": E4,
   "gerekce": "85.17 Açıklama Notu, kablolu veya kablosuz ağlarda iletişim cihazları arasında arabirim ağ kartlarını (Ethernet arabirim kartları) ismen sayar. Fasıl 84 Not 6(D) bu cihazları, şartları taşısalar bile 84.71 dışında bırakır; kendi pozisyonu olduğundan Bölüm XVI Not 2(a) gereği 84.73’e de gitmez. Kart, entegre devrelerin baskılı devreye monte edildiği bir bütün olduğu için 85.42 de değildir.",
   "dayanak": "85.17 Açıklama Notu (G); Fasıl 84 Not 6(D)(ii); Bölüm XVI Not 2(a)."
  },
  # 6 SN – B
  {
   "soru": "Bir firma şu eşyayı ithal etmektedir: Gövdesinde elektrik motoru bulunan, evlerde kullanılan türden, ağırlığı 12 kg olan; halıya sıvı temizleme çözeltisi püskürtüp ardından bu çözeltiyi emerek çeken, kuru ve ıslak vakumlu temizlemeyi birlikte yapma özelliği bulunmayan halı temizleme cihazı. Tarife Cetveline göre bu eşya hangi pozisyonda sınıflandırılır?",
   "secenekler": ["85.08", "85.09", "84.51", "84.24", "84.79"],
   "cevap": "B",
   "tip": SN,
   "gerekce": "85.08 Açıklama Notu, çözelti püskürtüp emen ve kuru-ıslak vakum kombinasyonu olmayan halı temizleme cihazlarını vakumlu süpürge saymaz ve 84.51 veya 85.09’a yönlendirir. 85.09’un hariç tutmalarına göre otel, hastane, büro gibi tesisler için tasarlananlar 84.51’dedir; ev tipi olup 20 kg’ı geçmeyen bu cihaz Not 4(b) ile 85.09’da kalır. Tuzak, “emme” işlevine bakıp 85.08’i seçmektir.",
   "dayanak": "Fasıl 85 Not 4(b); 85.08 ve 85.09 Açıklama Notları."
  },
  # 7 CC – D
  {
   "soru": "Tarife Cetveline göre aşağıdaki ifadelerden hangileri doğrudur? I. Fasıl 85 Not 12’de tarif edilen eşyanın sınıflandırılmasında 85.41 ve 85.42 pozisyonları, 85.23 hariç, fonksiyonları dolayısıyla girebilecekleri diğer pozisyonlara göre öncelik alır. II. Yalnızca pasif elemanlardan oluşan ince veya kalın film devreleri 85.42 pozisyonunda sınıflandırılır. III. 85.41 pozisyonundaki ışık yayan diyotlar (LED), güç kaynağı veya güç kontrolü sağlamak amacıyla eleman içermez. IV. Akımın yönünü kontrol eden diyotlar gibi elemanlarla donatılmamış, modül halinde birleştirilmiş güneş pilleri 85.01 pozisyonunda sınıflandırılır.",
   "secenekler": ["I ve II", "II ve IV", "I, III ve IV", "I ve III", "III ve IV"],
   "cevap": "D",
   "tip": CC,
   "gerekce": "I, Not 12’nin son cümlesidir; III, Not 12(a)(ii)’deki LED tanımıdır. II yanlıştır: yalnız pasif elemanlı film devreleri 85.34’tedir; 85.42 için aktif ve pasif elemanların aynı işlemle elde edilmesi gerekir. IV yanlıştır: elemansız modül ve paneller 85.41’dedir; diyot gibi elemanlarla donatılıp gücü doğrudan veren paneller 85.01’e gider.",
   "dayanak": "Fasıl 85 Not 8 ve Not 12; 85.41 ve 85.01 Açıklama Notları."
  },
  # 8 OT – A
  {
   "soru": "Tarife Cetveline göre aşağıdakilerden hangisi 85. Fasılda <b>sınıflandırılmaz</b>?",
   "secenekler": ["Elektrikle ısıtılan battaniye", "Elektrikli buharlı ütü", "Elektrikli depolu su ısıtıcı", "Elektrikli kapı zili", "Motorlu taşıtlar için elektrikli cam silici"],
   "cevap": "A",
   "tip": OT,
   "gerekce": "Fasıl 85 Not 1(a), elektrikle ısıtılan battaniye, yatak örtüsü ve giyim eşyasını fasıl dışında bırakır; bunlar kendi uygun pozisyonlarında sınıflandırılır. Elektrikli ütü ve depolu su ısıtıcı 85.16’da, kapı zili 85.31’de, motorlu taşıt cam silicisi 85.12’dedir. Tuzak, ısıtma işlevi nedeniyle battaniyeyi 85.16’ya koymaktır.",
   "dayanak": "Fasıl 85 Not 1(a); 85.16 Açıklama Notu, hariç tutmalar; 85.12 ve 85.31 Açıklama Notları."
  },
  # 9 GY – C
  {
   "soru": "Nakliye kolaylığı için ayrı ayrı ambalajlanarak aynı sevkiyatta getirilen ve birleştirildiğinde ortak bir kaide üzerinde çalışacak olan dizel motor ile alternatörden oluşan elektrik enerjisi üretim (elektrojen) grubu, 85.02 pozisyonunda hangi Genel Yorum Kuralları uygulanarak sınıflandırılır?",
   "secenekler": ["GYK 1 ve 3(b)", "GYK 1 ve 3(c)", "GYK 1 ve 2(a)", "GYK 1 ve 2(b)", "GYK 1 ve 4"],
   "cevap": "C",
   "tip": GY,
   "gerekce": "GYK 2(a), monte edilmemiş veya sökülmüş halde sunulan eşyayı bütün eşya gibi sınıflandırır; Bölüm XVI Genel Açıklamalarının (V) kısmı da demonte makinelerin parça pozisyonlarına değil makine pozisyonuna gittiğini belirtir. 85.02 Açıklama Notu, jeneratör ve hareket ettiricinin nakil kolaylığı için ayrı ambalajlansa dahi birlikte getirilmesi şartıyla 85.02’de yer aldığını söyler. 2(b) madde karışımları, 3(b) takımlar, GYK 4 en çok benzeyen eşya içindir.",
   "dayanak": "GYK 1 ve 2(a); 85.02 Açıklama Notu (I); Bölüm XVI Genel Açıklamalar (V)."
  },
  # 10 FN – E
  {
   "soru": "Fasıl 85 Not 6(b)’ye göre “akıllı kart” ile ilgili aşağıdaki ifadelerden hangisi doğrudur?",
   "secenekler": ["Kart üzerinde mutlaka manyetik bir şerit bulunması gerekir.", "İçine anten yerleştirilmiş kartlar akıllı kart sayılmaz, 85.17’de yer alır.", "Entegre devre içerdiği için 85.42 pozisyonunda sınıflandırılır.", "Çipin yanında kapasitör ve direnç gibi pasif devre elemanları da içerebilir.", "İçine çip şeklinde en az bir elektronik entegre devre yerleştirilmiş karttır."],
   "cevap": "E",
   "tip": FN,
   "gerekce": "Not 6(b)’ye göre akıllı kart, içine çip şeklinde bir veya daha fazla elektronik entegre devre (mikroişlemci, RAM, ROM) yerleştirilmiş karttır; kontak, manyetik şerit veya anten içerebilir ama başka aktif veya pasif eleman içermez. D şıkkındaki pasif eleman serbestliği Not 6(a)’daki flash bellek cihazlarına aittir (tuzak). Not 12 önceliği 85.23’ü kapsamadığından akıllı kart 85.42’ye değil 85.23’e gider.",
   "dayanak": "Fasıl 85 Not 6(a), 6(b) ve Not 12; 85.23 Açıklama Notu."
  },
  # 11 ES – A
  {
   "soru": "Tarife Cetveline göre aşağıdaki cümlede boşlukları doğru tamamlayan seçenek hangisidir? “Gerilimi 1000 voltu geçmeyen elektrik devreleri için anahtarlar ……… pozisyonunda, gerilimi 1000 voltu geçen devreler için yük ayırıcılar ……… pozisyonunda, bu cihazlardan iki veya daha fazlasıyla donatılmış elektrik dağıtım panoları ……… pozisyonunda, cihazları takılmamış boş panolar ise ……… pozisyonunda sınıflandırılır.”",
   "secenekler": ["85.36 / 85.35 / 85.37 / 85.38", "85.35 / 85.36 / 85.37 / 85.38", "85.36 / 85.35 / 85.38 / 85.37", "85.36 / 85.37 / 85.35 / 85.48", "85.35 / 85.36 / 85.38 / 85.48"],
   "cevap": "A",
   "tip": ES,
   "gerekce": "85.36 gerilimi 1000 voltu geçmeyen, 85.35 geçen devrelerin anahtarlama ve koruma teçhizatını kapsar. 85.35 veya 85.36 cihazlarından iki veya daha fazlasıyla donatılmış panolar 85.37’de; cihazları bulunmayan boş panolar, kumanda tablosu parçası oldukları açıkça anlaşılmak kaydıyla 85.38’dedir. B şıkkı eşiği tersine çevirir; 85.48 belirli cihaza ait olmayan aksam içindir.",
   "dayanak": "85.35, 85.36, 85.37 ve 85.38 pozisyon metinleri ve Açıklama Notları."
  },
  # 12 FA – D
  {
   "soru": "Tarife Cetveline göre aşağıdakilerden hangisi diğerlerinden farklı bir tarife pozisyonunda sınıflandırılır?",
   "secenekler": ["Pistonlu motorlar için kurşun-asitli starter aküsü", "Şarj edilebilir nikel-metal hidrürlü kalem pil", "Elektrolit maddesi konulmamış halde getirilen akümülatör", "Manganez dioksitli, şarj edilemeyen alkali kalem pil", "Bir el aletine özgü, koruyucu devreli lityum iyon batarya grubu"],
   "cevap": "D",
   "tip": FA,
   "gerekce": "Şarj edilemeyen primer piller 85.06’dadır. Diğerleri 85.07’dedir: kurşun-asitli akü ve elektrolitsiz akümülatör Açıklama Notunda, şarjlı kalem pil “tekrar şarj edilebilen piller 85.07’dedir” hükmüyle, belirli alete özgü koruyucu devreli batarya grubu Not 3 ve Açıklama Notu ile. Tuzak, kalem pil görünümüne bakıp şarjlı pili 85.06’ya koymaktır.",
   "dayanak": "Fasıl 85 Not 3; 85.06 ve 85.07 Açıklama Notları."
  },
  # 13 E4 – B
  {
   "soru": "Tarife Cetveline göre, floresan lamba ve tüplerin ateşlenmesinde kullanılan ve “starter” olarak bilinen otomatik termo-elektrik anahtar hangi tarife pozisyonunda sınıflandırılır?",
   "secenekler": ["85.39", "85.36", "85.04", "85.40", "94.05"],
   "cevap": "B",
   "tip": E4,
   "gerekce": "85.36 Açıklama Notu, floresan lamba ve tüpler için kullanılan “starter” denilen otomatik termo-elektrik anahtarları bu pozisyonda sayar; 85.39 Açıklama Notu da bunları hariç tutar. 85.04 deşarj ampulleri için balastları, 85.40 termiyonik tüpleri, 94.05 aydınlatma cihazlarını kapsar. Tuzak, floresan ile birlikte kullanıldığı için 85.39’u seçmektir.",
   "dayanak": "85.36 Açıklama Notu (I)(A); 85.39 Açıklama Notu, hariç tutmalar."
  },
  # 14 SN – C
  {
   "soru": "Bir üretici şu eşyayı ayrı olarak ithal etmektedir: Buzdolabı kapağına takılmak üzere tasarlanmış; sıvı kristal (LCD) hücre, sürücü entegre devresi, bunu bağlayan baskılı devre kartı ve arka ışık ünitesinden oluşan, dokunmaya duyarlı ekranı bulunan, ancak ölçekleyici IC, kod çözücü IC veya uygulama işlemcisi gibi video sinyallerini dönüştüren bileşen içermeyen gösterge modülü. Tarife Cetveline göre bu eşya hangi pozisyonda sınıflandırılır?",
   "secenekler": ["84.18", "85.28", "85.24", "85.29", "85.31"],
   "cevap": "C",
   "tip": SN,
   "gerekce": "Eşya Not 7’deki düz panel gösterge modülü tanımına uyar: başka ürüne dahil edilmek üzere tasarlanmış, ekranlı, video sinyalini piksellere tahsis eden sürücüsü var, video dönüştürücü bileşeni yok; dokunmatik ekran pozisyon metninde serbesttir. Not 7 son cümlesiyle 85.24 diğer pozisyonlara göre önceliklidir ve ayrı sunulan modül bitmiş ürünün pozisyonunda (84.18) değil 85.24’te sınıflandırılır. 85.29 modülün parçaları içindir.",
   "dayanak": "Fasıl 85 Not 7; 85.24 pozisyon metni ve Açıklama Notu."
  },
  # 15 OT – E
  {
   "soru": "Tarife Cetveline göre aşağıdakilerden hangisi 85.43 pozisyonunda <b>yer almaz</b>?",
   "secenekler": ["Yüklü taneciklere yüksek kinetik enerji veren tanecik hızlandırıcısı", "Şarj edilebilir ve yeniden doldurulabilir elektronik sigara", "Elektrikli çit enerji sağlayıcı sistem", "Uçuş verilerini kaydeden, darbe ve yangına dayanıklı kara kutu", "Pil veya sıvı bitince atılan tek kullanımlık elektronik sigara"],
   "cevap": "E",
   "tip": OT,
   "gerekce": "85.43 Açıklama Notu, şarj edilmek veya yeniden doldurulmak üzere tasarlanmamış tek kullanımlık e-sigaraları ve sıvı kartuşlarını hariç tutar; bunlar 24.04’tedir. Tanecik hızlandırıcıları, yeniden doldurulabilir e-sigaralar, elektrikli çit enerji sistemleri ve uçuş veri kaydedicileri (kara kutu) 85.43’te ismen sayılır.",
   "dayanak": "85.43 Açıklama Notu ve hariç tutmaları."
  },
  # 16 FN – D
  {
   "soru": "Fasıl 85 Not 11’e göre “LED modül”ü “LED ampul”den ayıran temel özellik aşağıdakilerden hangisidir?",
   "secenekler": ["LED modülün güç kaynağı veya güç kontrolü sağlayan hiçbir eleman bulundurmaması", "LED ampulün yalnızca tek bir ışık yayan diyottan oluşması", "LED modülün baskılı devre şeklinde düzenlenmemiş olması", "LED ampulün kolay takılıp değiştirilmesini sağlayan bir kapağa sahip olması", "LED modülün yalnızca 85.41 pozisyonundaki LED paketlerinden oluşması"],
   "cevap": "D",
   "tip": FN,
   "gerekce": "Not 11(b)’ye göre LED ampuller, aydınlatma cihazına kolay kurulum veya değiştirmeye izin veren ve elektriksel veya mekanik teması sağlayan bir kapağa (tabana) sahiptir; LED modüllerde bu kapak yoktur. Modüller elektrik devresi şeklinde düzenlenir ve güç kaynağı veya güç kontrolü için 85.36 ya da 85.42 eşyası içerebilir (A ve C yanlış); ampul bir veya daha fazla LED modül içerir (B yanlış).",
   "dayanak": "Fasıl 85 Not 11(a) ve (b); 85.39 Açıklama Notu (F) ve (G)."
  },
  # 17 FA – A
  {
   "soru": "Tarife Cetveline göre aşağıdaki eşya çiftlerinden hangisinde her iki eşya da aynı tarife pozisyonunda sınıflandırılır?",
   "secenekler": ["Metal tanklı cıva buharlı redresör – Akümülatör şarj cihazı", "LED ampul – Tek bir ışık yayan diyot (LED)", "Floresan tüp – Floresan lamba starteri", "Elektrik motoru – Bu motora ait kömür fırça", "Televizyon alıcısı – Katot ışınlı televizyon görüntü tüpü"],
   "cevap": "A",
   "tip": FA,
   "gerekce": "Not 2, metal tanklı cıva buharlı redresörleri 85.04’te bırakır; akümülatör şarj cihazları da statik konvertör olarak 85.04’tedir. Diğer çiftler ayrışır: LED ampul 85.39 – LED 85.41; floresan tüp 85.39 – starter 85.36; motor 85.01 – kömür fırça 85.45; TV alıcısı 85.28 – katot ışınlı tüp 85.40.",
   "dayanak": "Fasıl 85 Not 2; 85.04 Açıklama Notu (II); 85.36, 85.39, 85.40, 85.45 Açıklama Notları."
  },
  # 18 E4 – B
  {
   "soru": "Tarife Cetveline göre, bir elektrik motorunda kayan kontak olarak kullanılmak üzere ölçüsüne göre işlenmiş, terminal ve yay ile donatılmış kömür fırça (bale) ayrı olarak getirildiğinde hangi tarife pozisyonunda sınıflandırılır?",
   "secenekler": ["85.03", "85.45", "38.01", "96.03", "85.48"],
   "cevap": "B",
   "tip": E4,
   "gerekce": "85.45, elektrik işlerinde kullanılan kömür fırçaları ismen kapsar; tutucu, kablo, terminal veya yay ile donatılmış olmaları bunu değiştirmez. Bölüm XVI Not 2(a) ve Genel Açıklamalardaki listeye göre elektrik kömürleri belirli bir makine için yapılmış olsa da kendi pozisyonunda kalır; bu yüzden motor parçası olarak 85.03’e gitmez (fırça mesnedi ise 85.03’tür). 38.01, fırçaların kesildiği kömür blok ve levhaları içindir; 96.03 ise Bölüm XVI Not 1’de anılan, makine parçası olarak kullanılan diğer fırçaları kapsar.",
   "dayanak": "85.45 Açıklama Notu (D); Bölüm XVI Not 2(a); Bölüm XVI Genel Açıklamalar, Aksam ve Parçalar."
  },
  # 19 GY – E
  {
   "soru": "Aynı kabin içinde bir saat ile birleştirilmiş radyo yayını alıcı cihazının (saatli radyo) 85.27 pozisyonunda sınıflandırılması hangi Genel Yorum Kuralına dayanır?",
   "secenekler": ["GYK 3(a)", "GYK 3(b)", "GYK 3(c)", "GYK 2(a)", "GYK 1"],
   "cevap": "E",
   "tip": GY,
   "gerekce": "85.27 pozisyon metni “aynı kabin içinde ses kayıt veya kaydedilen sesi tekrar vermeye mahsus cihaz veya saatle birlikte olsun olmasın” ifadesini içerir. Kombinasyon pozisyon metninde açıkça karşılandığından sınıflandırma GYK 1 ile yapılır; GYK 3’ün alt bentlerine başvurmaya gerek kalmaz. GYK 2(a) eksik veya demonte eşya içindir.",
   "dayanak": "GYK 1; 85.27 pozisyon metni ve Açıklama Notu."
  },
  # 20 CC – C
  {
   "soru": "Tarife Cetveline göre aşağıdaki ifadelerden hangileri doğrudur? I. Restoranlarda kullanılmak üzere tasarlanmış mikrodalga fırınlar 85.16 pozisyonunda sınıflandırılır. II. Elektrikli merkezi ısıtma kazanları 84.03 pozisyonunda sınıflandırılır. III. Kömürden mamul ısıtıcı rezistanslar 85.45 pozisyonunda sınıflandırılır. IV. Elektrikle ısıtılan giyim eşyası 85.16 pozisyonunda sınıflandırılır.",
   "secenekler": ["I ve II", "I ve IV", "II ve III", "I, II ve III", "II, III ve IV"],
   "cevap": "C",
   "tip": CC,
   "gerekce": "II, 85.16 Açıklama Notunda (elektrikli merkezi ısıtma kazanları 84.03); III, 85.16 metnindeki “85.45 pozisyonundakiler hariç” kaydı ve Açıklama Notu (F) ile doğrudur. I yanlıştır: restoran tipi mikrodalga fırınlar sanayi mikrodalga cihazı olarak 85.14’tedir. IV yanlıştır: elektrikle ısıtılan giyim eşyası Not 1(a) ile Fasıl 85 dışındadır.",
   "dayanak": "Fasıl 85 Not 1(a); 85.14 ve 85.16 Açıklama Notları."
  },
  # 21 ES – A
  {
   "soru": "Tarife Cetveline göre aşağıdaki cihaz gruplarının aksam ve parçalarının sınıflandırıldığı pozisyonlar hangi seçenekte doğru eşleştirilmiştir? I. 85.01 ve 85.02 pozisyonlarındaki makinalar II. 85.19 ve 85.21 pozisyonlarındaki cihazlar III. 85.24 ila 85.28 pozisyonlarındaki eşya IV. 85.35, 85.36 ve 85.37 pozisyonlarındaki cihazlar",
   "secenekler": ["I–85.03, II–85.22, III–85.29, IV–85.38", "I–85.03, II–85.29, III–85.22, IV–85.38", "I–85.48, II–85.22, III–85.29, IV–85.38", "I–85.03, II–85.22, III–85.38, IV–85.29", "I–85.04, II–85.22, III–85.29, IV–85.48"],
   "cevap": "A",
   "tip": ES,
   "gerekce": "Fasıl 85’te dört ayrı parça pozisyonu vardır: 85.01–85.02 makinaları için 85.03, 85.19 ve 85.21 cihazları için 85.22, 85.24–85.28 eşyası için 85.29, 85.35–85.37 cihazları için 85.38. 85.48 yalnız belirli bir cihaza ait olmayan elektrikli aksam içindir; 85.04 ise kendi parçalarını kendi bünyesinde toplar.",
   "dayanak": "Bölüm XVI Not 2(b); 85.03, 85.22, 85.29 ve 85.38 pozisyon metinleri."
  },
  # 22 OT – D
  {
   "soru": "Tarife Cetveline göre aşağıdakilerden hangisi 85.17 pozisyonunda <b>sınıflandırılmaz</b>?",
   "secenekler": ["Modem", "Hücresel ağ baz istasyonu", "Bina girişine monte edilen giriş-telefon sistemi", "Faks makinesi", "Router (yönlendirici)"],
   "cevap": "D",
   "tip": OT,
   "gerekce": "85.17 Açıklama Notu faks makinelerini hariç tutar ve 84.43’e gönderir; Fasıl 84 Not 6(D) de faksı 84.71 dışında 84.43’e bırakır. Modem, router, baz istasyonu ve giriş-telefon (diafon) sistemleri 85.17 Açıklama Notunda ismen sayılır. Tuzak, faksın telefon hattıyla veri iletmesine bakıp 85.17’yi seçmektir.",
   "dayanak": "85.17 Açıklama Notu ve hariç tutmaları; Fasıl 84 Not 6(D)(i)."
  },
  # 23 FA – C
  {
   "soru": "Tarife Cetveline göre aşağıdakilerden hangisi diğerlerinden farklı bir fasılda sınıflandırılır?",
   "secenekler": ["Berberlerin kullandığı, kendinden elektrik motorlu saç kesme makinesi", "Elektrikli vibratörle donatılmış, kendinden motorlu traş makinesi", "Ayrı bir motora esnek mille bağlanarak çalışan hayvan kırkma makinesi", "Kılları kökünden çıkaran, kendinden motorlu epilasyon cihazı", "Ev tipi, şarj edilebilir ve kendinden motorlu elektrikli diş fırçası"],
   "cevap": "C",
   "tip": FA,
   "gerekce": "85.10 Açıklama Notuna göre ayrı haldeki bir elektrik motoruna eğilip bükülebilen mil ile bağlanarak işletilen saç kesme ve hayvan kırkma makineleri 82.14’tedir (Fasıl 82), motorları ise 85.01’dedir. Saç kesme, traş ve epilasyon cihazları kendinden motorlu oldukları için 85.10’da, elektrikli diş fırçası 85.09’dadır; bunların hepsi Fasıl 85’tir.",
   "dayanak": "85.10 Açıklama Notu; 85.09 Açıklama Notu (B)."
  },
  # 24 FN – E
  {
   "soru": "Fasıl 85 Not 8’e göre “baskılı devreler” ile ilgili aşağıdaki ifadelerden hangisi doğrudur?",
   "secenekler": ["Baskı işlemi sırasında elde edilmeyen elemanlarla birleştirilmiş devreler de baskılı devre sayılır.", "Baskı yoluyla elde edilen tek, ayrık bir direnç baskılı devre olarak 85.34’te yer alır.", "Diyot ve transistör gibi sinyal üreten veya büyülten elemanlar da baskılı devre elemanıdır.", "Baskılı olmayan bağlantı elemanları takılan devre, baskılı devre niteliğini kaybeder.", "Aynı teknik işlemle elde edilmiş aktif ve pasif elemanlı film devreleri 85.42’dedir."],
   "cevap": "E",
   "tip": FN,
   "gerekce": "Not 8’in son paragrafına göre aynı teknik işlem sırasında elde edilen aktif ve pasif elemanları içeren ince veya kalın film devreleri 85.42’de sınıflandırılır. Not 8, baskı dışında elde edilen elemanlarla birleştirilmiş devreleri ve tek, ayrık direnç-kapasitör-endüktansları kapsam dışı tutar (A, B yanlış); sinyal üreten veya büyülten yarı iletkenleri hariç tutar (C yanlış); baskılı olmayan bağlantı elemanlarının takılmasına izin verir (D yanlış).",
   "dayanak": "Fasıl 85 Not 8; 85.34 Açıklama Notu."
  },
  # 25 E4 – B
  {
   "soru": "Tarife Cetveline göre, aynı muhafaza içinde baskılı devre kartına monte edilmiş flash bellek entegre devreleri ile bir mikro denetleyiciden oluşan, bilgisayarın USB girişine takılan ve batarya gerektirmeyen taşınabilir veri depolama aygıtı (USB bellek) hangi tarife pozisyonunda sınıflandırılır?",
   "secenekler": ["84.71", "85.23", "85.42", "84.73", "85.48"],
   "cevap": "B",
   "tip": E4,
   "gerekce": "Eşya Not 6(a)’daki katı halde kalıcı bellek cihazı tanımına uyar; 85.23 Açıklama Notu USB sürücüyü örnek olarak sayar. Not 12’nin 85.41 ve 85.42’ye verdiği öncelik 85.23’ü kapsamaz; 85.42 Açıklama Notu da katı hal depolama aygıtlarını hariç tutar. Kendi pozisyonu olduğu için Bölüm XVI Not 2(a) gereği bilgisayar parçası (84.73) veya genel elektrikli aksam (85.48) da değildir.",
   "dayanak": "Fasıl 85 Not 6(a) ve Not 12; 85.23 ve 85.42 Açıklama Notları; Bölüm XVI Not 2(a)."
  }
 ]
}

out = os.path.join(KITAP, "data", "fasil_85.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=1)
print("yazıldı:", out)
