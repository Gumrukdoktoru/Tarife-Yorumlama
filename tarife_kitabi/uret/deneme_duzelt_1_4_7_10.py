#!/usr/bin/env python3
"""Deneme 1, 4, 7, 10'da son_kontrol.py'nin işaretlediği soruları yenileriyle değiştirir."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")

YENI = {
 1: {
  12: {
   "soru": "Elektrikle ısıtma esasına göre çalışan aşağıdaki cihazlardan hangisi 85.16 pozisyonunda <b>sınıflandırılmaz</b>?",
   "secenekler": [
    "Yüz derisi bakımı için suyu buharlaştıran, yüz maskeli yüz saunası",
    "Banyoda kullanılan, ısıtmalı havlu askısı",
    "Haşarat öldürücü müstahzarları ısıtarak yayan elektrikli buhurdan",
    "Bitkilerin büyümesini hızlandırmak için toprağa gömülen ısıtıcı",
    "Taşıt ön camına uygun çerçevede takılı rezistans telli buğu önleyici"
   ],
   "cevap": "E",
   "gerekce": "85.16 Açıklama Notu, ön cama uygun bir çerçevede takılı rezistans telinden oluşan buzlanma ve buğulanma önleyici cihazları bu pozisyon dışında bırakır; bunlar pozisyon metninde ismen sayıldıkları 85.12’de yer alır. Yüz saunaları, ısıtmalı havlu asacakları ve elektrikli buhurdanlar ev işlerinde kullanılan elektrotermik cihazlar olarak, toprağı ısıtan cihazlar ise toprak ve benzeri yerlerin ısıtılmasına mahsus cihazlar olarak 85.16’dadır. Tuzak, ısıtıcı rezistans içeren her cihazı doğrudan 85.16’ya yerleştirmektir.",
   "dayanak": "85.16 Açıklama Notu (B), (E) ve (F); 85.12 pozisyon metni."
  },
  17: {
   "soru": "Aşağıdaki kurutulmuş bitkisel ürünlerden hangisi diğerlerinden <b>farklı</b> bir fasılda sınıflandırılır?",
   "secenekler": [
    "Defne yaprakları",
    "Şerbetçi otu kozalakları",
    "Çemen otu tohumu",
    "Ardıç meyveleri",
    "Kakule"
   ],
   "cevap": "B",
   "gerekce": "Fasıl 9 Genel Açıklamaları şerbetçi otunu bu fasıl dışında bırakarak 12.10’a gönderir. Defne yaprakları ve çemen otu tohumu 09.10’da, ardıç meyveleri 09.09’da, kakule 09.08’de yer alır. Ardıç meyvelerinin de şerbetçi otu gibi alkollü içkilere tat vermede kullanılması tuzaktır; ardıç meyveleri 09.09 pozisyon metninde ismen sayılmıştır.",
   "dayanak": "Fasıl 9 Genel Açıklamalar (hariç tutulanlar); 09.08, 09.09 ve 09.10 Açıklama Notları; 12.10 pozisyon metni."
  },
  30: {
   "soru": "Sığır ve at türü hayvanlara ait aşağıdaki deri ve köselelerden hangisi diğerlerinden <b>farklı</b> bir fasılda sınıflandırılır?",
   "secenekler": [
    "Kılları alınmamış, tuzlanarak muhafaza edilmiş ham at derisi",
    "Bölmeyi kolaylaştırmak için geri alınabilir ön dabaklama yapılmış, kılları alınmış sığır derisi",
    "Kılları alınmış, dabaklanıp ara kurutulmuş (crust) manda derisi",
    "Kılları alınmamış, kromla dabaklanmış dana derisi",
    "Silindirden geçirilerek sertleştirilmiş, bütün halde sığır taban köselesi"
   ],
   "cevap": "D",
   "gerekce": "Fasıl 41 Not 1(c) uyarınca sığır ve atların kılları alınmamış derileri yalnızca ham haldeyken Fasıl 41’de kalır; 41.04 Açıklama Notu kılı alınmadan dabaklanmış veya ara kurutulmuş sığır ve at derilerini Fasıl 43’e gönderir, Fasıl 43 Not 1 de bunları “kürk” sayar. Kılı alınmamış ham at derisi ile geri alınabilir ön dabaklama görmüş sığır derisi 41.01’de, crust manda derisi 41.04’te, taban köselesi 41.07’de, yani hepsi Fasıl 41’dedir. Tuzak, “kılı alınmamış” ibaresini her durumda Fasıl 41 için yeterli saymaktır.",
   "dayanak": "Fasıl 41 Not 1(c) ve Not 2(A); 41.04 ve 41.07 Açıklama Notları; Fasıl 43 Not 1."
  },
  35: {
   "soru": "91.02 Açıklama Notuna göre “zaman ölçen sayaçları” kronograflardan ayıran özellik aşağıdakilerden hangisidir?",
   "secenekler": [
    "Saniyenin beşte, onda, yüzde veya binde birini gösterebilmeleri",
    "Düğmeye basılarak işletilip durdurulabilen merkezi saniye ibresine sahip olmaları",
    "Mutad akrep, yelkovan ve saniye ibreleri olmayıp yalnız merkezi saniye ve dakika kaydeden ibrelere sahip olmaları",
    "Bir koşucunun veya taşıtın süratini hesaplamasız gösteren düzeneklerle donatılabilmeleri",
    "Çeşitli vaziyetlerde ve değişik sıcaklıklarda denenmiş yüksek doğruluğa sahip olmaları"
   ],
   "cevap": "C",
   "gerekce": "91.02 Açıklama Notuna göre kronograflar günün saatini gösteren mutad akrep, yelkovan ve saniye ibrelerine ek olarak kısa zaman aralıklarını ölçen hususi ibrelere sahiptir; zaman ölçen sayaçlar ise mutad ibreleri taşımaz, yalnızca merkezi saniye ibresi ve dakika kaydeden ibrelere sahiptir. Merkezi saniye ibresi, saniyenin küçük kesirlerini gösterebilme ve sürat gibi değerleri hesaplamasız veren düzenekler her ikisinde de bulunabildiğinden ayırt edici değildir. Çeşitli vaziyet ve sıcaklıklarda denenmiş yüksek doğruluk ise kronometrenin tanımıdır.",
   "dayanak": "91.02 Açıklama Notu."
  },
 },
 4: {
  2: {
   "soru": "Tarife Cetveline göre, kalıptan çekilerek elde edilmiş, pencere çerçevelerinin kapatılmasında kullanılan yapışkan yüzeyli, sertleştirilmemiş vulkanize kauçuktan profiller hangi pozisyonda sınıflandırılır?",
   "secenekler": [
    "40.08",
    "40.16",
    "40.06",
    "40.17",
    "40.07"
   ],
   "cevap": "A",
   "gerekce": "40.08 Açıklama Notu, kalıptan çekme gibi tek bir işlemle elde edilen ve boydan boya sabit veya tekrarlamalı enine kesite sahip profilleri pozisyona alır ve pencere çerçevelerinin kapatılmasında kullanılan yapışkan yüzeyli profilleri ismen sayar. Kullanım amacına bakarak eşyayı 40.16’daki diğer vulkanize kauçuk eşya arasında görmek tuzaktır. Vulkanize edilmemiş kauçuktan profiller 40.06’da, sertleştirilmiş kauçuktan olanlar 40.17’de, enine kesiti 5 mm’yi geçmeyen iplikler ise 40.07’de yer alır.",
   "dayanak": "Fasıl 40 Not 7 ve Not 9; 40.08 Açıklama Notu."
  },
  15: {
   "soru": "Uçucu yağlarla ilgili aşağıdaki ürünlerden hangisi Fasıl 33’te <b>yer almaz</b>?",
   "secenekler": [
    "Terpeni alınmış lavanta uçucu yağı",
    "Kağıt imalinden arta kalan sülfatlı terebantin esansı",
    "Uçucu yağların terpeninin alınmasından arta kalan terpenli yan ürünler",
    "Karabiberden organik çözücülerle elde edilen çeşni verici yağ reçinesi",
    "Çiçeklerden katı yağla emdirme (enfleurage) yoluyla elde edilen çiçek pomatı"
   ],
   "cevap": "B",
   "gerekce": "Fasıl 33 Not 1, 38.05 pozisyonunda yer alan terebantin esansını, çam ağacı esansını ve kağıt imalinden arta kalan sülfatlı esansı bu fasıl dışında bırakır. Terpeni alınmış uçucu yağlar, terpen alınmasından arta kalan terpenli yan ürünler, ekstraksiyonla elde edilen yağ reçineleri ve “çiçek pomatı” olarak bilinen, katı yağlardaki uçucu yağ konsantreleri 33.01’de sayılmıştır. Tuzak, terebantin esansının da uçucu ve kokulu bir ürün olması nedeniyle 33.01’e yöneltmesidir.",
   "dayanak": "Fasıl 33 Not 1; 33.01 pozisyon metni ve Açıklama Notu."
  },
  18: {
   "soru": "88.01 Açıklama Notuna göre, meteorolojide bulut yüksekliğini anlamak için kullanılan balonların türü ve normal ağırlığı hangi seçenekte doğru verilmiştir?",
   "secenekler": [
    "Sinyal balonları – 350 ila 1.500 gram",
    "Pilot balonları – 50 ila 100 gram",
    "İrtifa balonları – 50 ila 100 gram",
    "Sinyal balonları – 4 ila 30 gram",
    "İrtifa balonları – 4 ila 30 gram"
   ],
   "cevap": "E",
   "gerekce": "88.01 Açıklama Notu meteorolojide kullanılan balonları üçe ayırır: radyo verici cihazlarını yükseğe taşıyan sinyal balonları (normal ağırlığı 350–1.500 gram), rüzgârın yön ve hızını tayin eden pilot balonları (50–100 gram) ve bulut yüksekliğini anlamaya yarayan, diğerlerinden küçük irtifa balonları (4–30 gram). Diğer seçenekler balon türlerini veya ağırlık aralıklarını yer değiştirmiştir. Bu balonların tümü 88.01’dedir; daha aşağı kalitede kauçuktan, kısa şişirme emzikli ve baskılı oyuncak balonlar ise 95.03’te yer alır.",
   "dayanak": "88.01 Açıklama Notu (I)."
  },
 },
 7: {
  27: {
   "soru": "Tarife Cetveline göre, sürtünmeyle ateş alan ve kibrit şeklinde bulunan Bengal kibritleri hangi pozisyonda sınıflandırılır?",
   "secenekler": [
    "36.05",
    "36.03",
    "36.06",
    "36.01",
    "36.04"
   ],
   "cevap": "E",
   "gerekce": "36.05 pozisyon metni 36.04’teki pirotekni eşyasını kibritler dışında tutar; Açıklama Notu da Bengal kibritlerini ve benzeri bazı pirotekni ürünlerini, sürtünmeyle ateş almalarına ve kibrit şeklinde olmalarına rağmen 36.04’e gönderir. 36.04 ışık, ses, gaz veya duman oluşturan pirotekni eşyayı kapsar. 36.03 fitil ve ateşleyicilere, 36.06 piroforik alaşımlar ile ateş alıcı maddelerden eşyaya, 36.01 silah barutuna aittir.",
   "dayanak": "36.05 pozisyon metni ve Açıklama Notu; 36.04 Açıklama Notu."
  },
 },
 10: {
  4: {
   "soru": "Adında “biber” geçen aşağıdaki baharatlardan hangisi Tarife Cetvelinde diğerlerinden <b>farklı</b> bir pozisyonda sınıflandırılır?",
   "secenekler": [
    "Uzun biber (Piper longum)",
    "Beyaz biber",
    "Pimenta cinsinden kurutulmuş yenibahar",
    "Kurutulmuş, öğütülmemiş paprika (acısı az kırmızı biber)",
    "Malageta biberi (cennet tanesi, Aframomum melegueta)"
   ],
   "cevap": "E",
   "gerekce": "Malageta biberi veya “cennet tanesi” (Aframomum melegueta), adında biber geçmesine ve biber gibi acı, yakıcı bir tada sahip olmasına rağmen 09.08 Açıklama Notunda kakuleler arasında sayılmıştır. Uzun biber ve beyaz biber Piper cinsi biber olarak, yenibahar Pimenta cinsi, paprika ise Capsicum cinsi meyve olarak 09.04’te yer alır. Tuzak, ticari adı esas alıp bitkinin cinsini gözden kaçırmaktır.",
   "dayanak": "09.04 ve 09.08 Açıklama Notları."
  },
  36: {
   "soru": "GYK 1 ve açıklama notuna göre aşağıdaki ifadelerden hangisi <b>doğrudur</b>?",
   "secenekler": [
    "Bölüm, fasıl ve tali fasıl başlıkları eşyanın Tarifedeki yerinin saptanmasında yasal dayanak oluşturur.",
    "Önce 2 ila 5 numaralı kurallar uygulanır; pozisyon metinleri ve notlara ancak bunlar sonuç vermezse başvurulur.",
    "Birçok eşya diğer kurallara başvurulmadan sınıflandırılabilir; Fasıl 30 Not 4’teki eczacılık eşyasının 30.06’da yer alması buna örnektir.",
    "Fasıl notları, 2(b) kuralı uyarınca bir pozisyona girebilecek eşyanın o pozisyon dışında tutulmasını sağlayamaz.",
    "Kural 1’deki 2 numaralı kurala atıf, demonte sunulan bir bisikletin parçalar halinde ayrı ayrı sınıflandırılacağını ifade eder."
   ],
   "cevap": "C",
   "gerekce": "Açıklama notu (III)(a), birçok eşyanın diğer kurallara gerek kalmaksızın doğrudan pozisyon metinleri ve notlarla sınıflandırılabileceğini belirtir ve canlı atlar (01.01) ile Fasıl 30 Not 4 uyarınca 30.06’daki eczacılık müstahzarlarını örnek verir. Başlıklar yalnızca gösterici niteliktedir ve yasal dayanak oluşturmaz; 2–5 numaralı kurallar ise ancak lüzumu halinde ve pozisyon ve notlarda aksine hüküm bulunmadıkça uygulanır. Açıklama notu, Fasıl 31 notlarının 2(b) yoluyla bazı pozisyonlara girebilecek eşyayı engellediğini örnekler; demonte bisiklet ise 2(a) şartları sağlanırsa bitmiş bisiklet olarak sınıflandırılır.",
   "dayanak": "GYK 1 ve Açıklama Notu (I)–(III)."
  },
  47: {
   "soru": "Fasıl 85 Not 7’ye göre 85.24 pozisyonu anlamında “düz panel gösterge modülleri” ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
   "secenekler": [
    "Yalnızca düz ekranları kapsar; kavisli, esnek veya katlanabilir ekranlar tanımın dışındadır.",
    "Ölçekleyici veya kod çözücü entegre devre gibi video sinyali dönüştüren bileşenleri olanlar da 85.24’te kalır.",
    "Başka ürünlere dahil edilmesi amaçlanmayan, doğrudan kullanıma hazır monitörleri ifade eder.",
    "Video sinyallerini almak ve piksellere tahsis etmek için gereken unsurları içerenler tanımın dışında kalır.",
    "Bu notta tanımlanan modüllerin sınıflandırılmasında 85.24 pozisyonu Tarifedeki diğer pozisyonlara göre önceliklidir."
   ],
   "cevap": "E",
   "gerekce": "Not 7, düz panel gösterge modüllerini kullanımdan önce diğer pozisyonlardaki ürünlere dahil edilmek üzere tasarlanmış, asgari olarak bir görüntüleme ekranıyla donatılmış cihazlar olarak tanımlar ve bu modüllerin sınıflandırılmasında 85.24’ün diğer pozisyonlara göre öncelikli olduğunu belirtir. Ekranlar düz, kavisli, esnek, katlanabilir veya gerilebilir olabilir; video sinyallerini almak ve piksellere tahsis etmek için gereken unsurları içermeleri tanıma engel değildir. Buna karşılık ölçekleyici IC, kod çözücü IC veya uygulama işlemcisi gibi video sinyali dönüştürücü bileşenlerle donatılmış modüller 85.24’e girmez.",
   "dayanak": "Fasıl 85 Not 7."
  },
  48: {
   "soru": "GYK 3 açıklama notuna göre, kuraldaki üç yöntemin uygulanma sırası ve koşulu ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
   "secenekler": [
    "Önce eşyaya esas niteliğini veren madde aranır; bu saptanamazsa en özel tanımı veren pozisyon seçilir.",
    "Üç yöntem arasında öncelik sırası yoktur; eşyaya en uygun sonucu veren yöntem seçilebilir.",
    "Önce özel tanımlamaya, o yetersiz kalırsa esas niteliğe, o da yetersiz kalırsa geçerli pozisyonlardan numara sırasına göre sonuncusuna bakılır.",
    "Bölüm veya fasıl notlarında aksine bir hüküm bulunsa dahi 3 numaralı kural notlardan önce uygulanır.",
    "3(c) uyarınca eşya, geçerli olabilecek pozisyonlardan numara sırasına göre ilkinde sınıflandırılır."
   ],
   "cevap": "C",
   "gerekce": "Açıklama notu (I), kuraldaki yöntemlerin belirtilen sırayla uygulanacağını, 3(b)’nin yalnızca 3(a) yetersiz kaldığında, 3(c)’nin ise 3(a) ve 3(b) yetersiz kaldığında devreye gireceğini belirtir; öncelik sırası özel tanımlama, asli karakter ve numara sırasına göre son pozisyondur. Açıklama notu (II)’ye göre kural ancak bölüm veya fasıl notlarında ya da pozisyon metinlerinde aksine hüküm bulunmadığında uygulanabilir. 3(c) geçerli pozisyonlardan ilkini değil sonuncusunu işaret eder.",
   "dayanak": "GYK 3; Açıklama Notu (I), (II) ve (XII)."
  },
 },
}

for no, degisim in YENI.items():
    yol = os.path.join(DATA, f"deneme_{no:02d}.json")
    d = json.load(open(yol, encoding="utf-8"))
    for sira, yeni in degisim.items():
        eski = d["sorular"][sira - 1]
        assert yeni["cevap"] == eski["cevap"], (no, sira)
        q = {"soru": yeni["soru"], "secenekler": yeni["secenekler"], "cevap": yeni["cevap"],
             "tip": eski["tip"], "gerekce": yeni["gerekce"], "dayanak": yeni["dayanak"], "fasil": eski["fasil"]}
        d["sorular"][sira - 1] = q
    with open(yol, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
    print("yazıldı:", yol)
