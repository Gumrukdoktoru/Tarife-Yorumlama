import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yardim_04_08 import q, yaz, T_E, T_O, T_F, T_N, T_G, T_B, T_C, T_S  # noqa: E402

obj = {
 "tur": "fasil",
 "fasil": 4,
 "baslik": "Süt ürünleri; kuş ve kümes hayvanlarının yumurtaları; tabii bal; Tarifenin başka yerinde belirtilmeyen veya yer almayan yenilebilir hayvansal menşeli ürünler",
 "bolum": "I",
 "oz": {
  "vurgu": "Fasıl 4 dört grubu toplar: süt ürünleri (04.01–04.06), kuş ve kümes hayvanı yumurtaları (04.07–04.08), tabii bal (04.09) ve yenilebilir böceklerle başka yerde yer almayan yenilebilir hayvansal ürünler (04.10). Süt ürünlerinde iki soru belirleyicidir: Ürün yalnızca tabii süt bileşenlerinden mi oluşuyor ve notlardaki yağ, kuru madde, laktoz eşikleri sağlanıyor mu?",
  "maddeler": [
   "Süt ürünleri işlem derecesine göre ayrılır: sade süt ve krema 04.01, konsantre veya tatlandırılmış 04.02, fermente veya asitliği artırılmış 04.03, peyniraltı suyu 04.04, süt yağları 04.05, peynir 04.06.",
   "Bir tabii bileşeni (ör. süt yağı) başka bir maddeyle (ör. bitkisel yağ) değiştirilmiş süt ürünü Fasıl 4 dışıdır → 19.01 veya 21.06.",
   "Yumurtada ölçüt kabuktur: kabuklu yumurta pişmiş olsa bile 04.07, kabuksuz yumurta ve yumurta sarısı 04.08; yumurta beyazı (albümin) 35.02.",
   "Bal ancak şeker veya başka bir madde katılmamışsa 04.09’dadır; suni bal ve tabii balla karışımları 17.02.",
   "İnsan tüketimine uygun cansız böcekler ve unları 04.10; uygun olmayanlar 05.11."
  ]
 },
 "karar_tablosu": {
  "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
  "satirlar": [
   ["1", "Bir tabii süt bileşeni başka bir maddeyle değiştirilmiş mi? (süt yağı yerine bitkisel yağ) ya da süt ürünlerinden hazırlanmış gıda müstahzarı mı?", "<b>19.01</b> / <b>21.06</b>"],
   ["2", "Dondurma veya kakao vb. ile aromalandırılmış sütten içecek mi?", "Dondurma <b>21.05</b> · içecek <b>22.02</b>"],
   ["3", "Peynir veya lor mu? (Not 4 şartlarını taşıyan peyniraltı suyu peyniri dahil)", "<b>04.06</b>"],
   ["4", "Tereyağı, diğer süt yağı (butteroil, ghee) veya sürülerek yenilen süt ürünü mü?", "<b>04.05</b>"],
   ["5", "Yoğurt, kefir, yayıkaltı, pıhtılaştırılmış ya da fermente veya asitliği artırılmış süt-krema mı?", "<b>04.03</b> (şekerli, aromalı, meyveli olsa da)"],
   ["6", "Peyniraltı suyu veya tabii süt bileşenlerinden oluşan başka ürün mü?", "<b>04.04</b> (laktoz %95’ten fazla <b>17.02</b>; albümin <b>35.02</b>)"],
   ["7", "Süt veya krema konsantre edilmiş ya da tatlandırılmış mı? (süt tozu dahil)", "<b>04.02</b>"],
   ["8", "Sade süt veya krema mı?", "<b>04.01</b>"],
   ["9", "Kuş veya kümes hayvanı yumurtası mı?", "Kabuklu <b>04.07</b> · kabuksuz veya sarı <b>04.08</b>"],
   ["10", "Bal mı?", "Katkısız <b>04.09</b> · suni bal veya karışım <b>17.02</b>"],
   ["11", "Yenilebilir böcek, kaplumbağa yumurtası, salangan yuvası mı?", "<b>04.10</b> (yenmeyen böcek <b>05.11</b>)"]
  ],
  "dipnot": "* Vitamin veya mineral tuzlarıyla zenginleştirme, az miktarda stabilize edici, çok az antioksidan veya vitamin, işleme için az miktarda kimyasal madde ve toz ürünlerde topaklanmayı önleyici madde katılması süt ürününü fasıl dışına çıkarmaz (Genel Açıklamalar)."
 },
 "pozisyon_haritasi": [
  ["04.01", "Süt ve krema (konsantre edilmemiş, tatlandırılmamış)", "Pastörize, sterilize, homojenize olabilir; dondurulmuş olabilir; rekonstitüe süt dahil", "Pastörize inek sütü, sterilize süt, krema"],
  ["04.02", "Süt ve krema (konsantre veya tatlandırılmış)", "Sıvı, hamur, blok, toz, granül; süt tozunda %5’e kadar nişasta", "Süt tozu, şekerli koyulaştırılmış süt"],
  ["04.03", "Yoğurt, yayıkaltı, kefir, fermente/asitliği artırılmış süt ve krema", "Şeker, aroma, meyve, sert kabuklu meyve, kakao içerebilir", "Meyveli yoğurt, kefir, pıhtılaştırılmış krema"],
  ["04.04", "Peyniraltı suyu; tabii süt bileşenlerinden ürünler", "Konsantre veya toz olabilir; başka yerde yer almama şartı", "Peyniraltı suyu tozu, proteince zenginleştirilmiş süt"],
  ["04.05", "Tereyağı, diğer süt yağları; sürülerek yenilen süt ürünleri", "Tereyağı süt yağı %80–95; sürülebilir %39–%80’den az", "Tereyağı, butteroil, ghee, keçi sütü tereyağı"],
  ["04.06", "Peynir ve pıhtılaştırılmış ürünler (lor)", "Her cins peynir; peynir karakteri korunmalı", "Mozzarella, krem peynir, rendelenmiş peynir, eritme peynir"],
  ["04.07", "Kuş ve kümes hayvanı yumurtaları (kabuklu)", "Taze, kuluçkalık, dayanıklı hale getirilmiş veya pişirilmiş", "Kuluçkalık tavuk yumurtası, haşlanmış kabuklu yumurta"],
  ["04.08", "Kabuksuz yumurtalar ve yumurta sarıları", "Kurutulmuş, pişirilmiş, kalıplanmış, dondurulmuş; şekerli olabilir", "Yumurta tozu, dondurulmuş yumurta sarısı, “uzun yumurta”"],
  ["04.09", "Tabii bal", "Şeker veya başka madde katılmamış; petekli olabilir", "Santrifüj edilmiş bal, petek bal"],
  ["04.10", "Böcekler; başka yerde yer almayan yenilebilir hayvansal ürünler", "İnsan tüketimine uygunluk; böcekte Not 6 işlemleri", "Kurutulmuş çekirge, böcek unu, kaplumbağa yumurtası, salangan yuvası"]
 ],
 "notlar": [
  ["Fasıl 4 Not 1", "“Süt”: tam yağlı, yarı yağlı veya tamamen yağsız süt."],
  ["Fasıl 4 Not 2", "04.03 anlamında yoğurt; konsantre edilmiş veya aromalandırılmış olabilir; ilave şeker veya diğer tatlandırıcı, meyve, sert kabuklu meyve, kakao, çikolata, baharat, kahve veya kahve hülasası, bitki, bitki kısımları, hububat ve ekmekçi mamulleri içerebilir. Şart: eklenen madde süt içeriğini tamamen veya kısmen ikame etme amaçlı olmamalı ve ürün yoğurdun esas karakterini korumalıdır."],
  ["Fasıl 4 Not 3(a)", "“Tereyağı”: sadece sütten elde edilen; süt yağı ağırlıkça <b>%80 veya daha fazla, %95’i geçmeyen</b>; yağsız katı madde en fazla <b>%2</b>; su en fazla <b>%16</b>. Tabii, peyniraltı suyu ve rekombine tereyağı (taze, tuzlanmış, acımış, kutulanmış) dahil. İlave emülsifiye edici içermez; sodyum klorür, gıda boyaları, nötralizasyon tuzları ve zararsız laktik asit üreten bakteri kültürleri içerebilir."],
  ["Fasıl 4 Not 3(b)", "“Sürülerek yenilen süt ürünleri”: içinde katı yağ olarak sadece süt yağı bulunan, süt yağı ağırlıkça <b>%39 veya daha fazla fakat %80’den az</b> olan, yağlı-sulu tipte (yağ içinde su) sürülebilen emülsiyonlar."],
  ["Fasıl 4 Not 4", "Peyniraltı suyu konsantrasyonu ve süt veya süt yağı ilavesiyle elde edilen ürünler üç şartla 04.06’da peynirdir: (a) süt yağı kuru madde üzerinden ağırlıkça <b>%5 veya daha fazla</b>; (b) kuru madde ağırlıkça <b>en az %70, en fazla %85</b>; (c) kalıplanmış veya kalıp haline getirilmeye müsait."],
  ["Fasıl 4 Not 5", "Fasıl dışı: (a) insan tüketimine uygun olmayan cansız böcekler (05.11); (b) peyniraltı suyundan elde edilen, kuru madde üzerinden ağırlıkça <b>%95’ten fazla laktoz</b> (susuz laktoz) içeren ürünler (17.02); (c) bir veya daha çok tabii bileşeni (ör. bütirik yağ) alınıp yerine başka madde (ör. oleik yağ) katılan süt ürünleri (19.01 veya 21.06); (d) albüminler (kuru madde üzerinden ağırlıkça <b>%80’den fazla</b> peyniraltı suyu proteini içeren, iki veya daha fazla peyniraltı suyu proteini konsantreleri dahil) (35.02) ve globulinler (35.04)."],
  ["Fasıl 4 Not 6", "04.10 anlamında “böcek”: bütün veya parça halinde; taze, soğutulmuş, dondurulmuş, kurutulmuş, tütsülenmiş, tuzlanmış veya salamura edilmiş, insan tüketimine uygun cansız böcekler ile böceklerin insan tüketimine uygun un ve kaba unları. Başka şekillerde hazırlanmış veya konserve edilmiş yenilen böcekleri kapsamaz (genellikle Bölüm IV)."],
  ["Genel Açıklamalar", "Süt ürünleri; vitamin veya mineral tuzlarıyla zenginleştirilmiş olabilir; sıvı naklinde doğal yapıyı koruyan az miktarda stabilize edici (disodyum fosfat, trisodyum sitrat, kalsiyum klorür), çok az antioksidan veya vitamin, işleme için az miktarda kimyasal (sodyum bikarbonat) ve toz ürünlerde kalıplaşmayı önleyici madde (fosfolipidler, amorf silikon dioksit) içerebilir."],
  ["Genel Açıklamalar", "“Bütirik yağlar” süt yağlarını, “oleik yağlar” süt yağları dışındaki yağları (özellikle bitkisel yağlar, zeytinyağı) ifade eder. Laktoz yüzdesinde “kuru madde” ifadesi serbest su ve kristalizasyon suyunu hariç tutmak için kullanılır."],
  ["Genel Açıklamalar", "Fasıl dışı: süt ürünlerinden hazırlanmış gıda müstahzarları (özellikle 19.01); dondurma ve diğer yenilebilir buzlar (21.05); Fasıl 30’daki ilaçlar; kazein (35.01), süt albümini (35.02), sertleştirilmiş kazein (39.13)."],
  ["04.02 Açıklama Notu", "Süt tozu, normal fiziki halini korumak için ağırlıkça <b>%5’i aşmayan</b> nişasta içerebilir. Kakao veya diğer maddelerle aromalandırılmış sütten mamul meşrubat 22.02’dedir."],
  ["04.03 Açıklama Notu", "Fermente süt 04.02’deki süt tozundan yapılabilir; az miktarda ilave laktik maya içerebilir. Asitliği artırılmış süt, limon suyu dahil az miktarda kristal asit içerebilir."],
  ["04.05 Açıklama Notu", "Keçi veya koyun sütünden tereyağı, susuz süt yağı (butteroil), suyu alınmış tereyağı, ghee ve karakteri değişmemek şartıyla az miktarda baharat, sarımsak vb. karıştırılmış tereyağı buradadır. Süt yağı dışında yağ içeren veya ağırlıkça %39’dan az süt yağı içeren sürülerek yenilen yağlar genellikle 15.17 veya 21.06’dadır."],
  ["04.06 Açıklama Notu", "Peynir karakteri korunduğu sürece et, balık, kabuklu hayvan, ot, baharat, sebze, meyve, sert kabuklu meyve, vitamin, yağsız süt tozu içermesi sınıflandırmayı etkilemez. Sulu hamur veya ekmek kırıntısıyla kaplanmış peynir, önceden pişirilmiş olsun olmasın, bu fasılda kalır."],
  ["04.07 / 04.08 Açıklama Notu", "Kabuklu yumurtalar (kuluçkalık, taze, dayanıklı hale getirilmiş, pişirilmiş) 04.07’de; kabuksuz yumurta ve yumurta sarısı gıda veya sanayi (ör. debagat) amaçlı olsun 04.08’de. 04.08 hariç: yumurta sarısı yağı (15.06), baharat, çeşni veya diğer katkı içeren yumurta ürünleri (21.06), lesitin (29.23), yumurta beyazı (35.02)."],
  ["04.09 Açıklama Notu", "Arıların (Apis mellifera) veya diğer böceklerin ürettiği, santrifüj edilmiş, petekte veya petek parçaları içeren bal; şeker veya başka madde katılmamış olmalı. Suni bal ve tabii bal ile suni bal karışımları 17.02’dedir."],
  ["04.10 Açıklama Notu", "Kaplumbağa yumurtaları (taze, kurutulmuş veya dayanıklı hale getirilmiş; yağı 15.06) ve salangan yuvaları (“kuş yuvası”) buradadır. Yenilen veya yenilmeyen, sıvı veya kurutulmuş hayvan kanı 05.11 veya 30.02’dedir."]
 ],
 "sinir_komsulari": [
  ["Süt yağı yerine bitkisel yağ konmuş süt ürünü; süt esaslı gıda müstahzarı", "19.01 / 21.06", "Tabii bileşen değiştirilmiş (Not 5(c)); Genel Açıklamalar"],
  ["Dondurma ve diğer yenilebilir buzlar", "21.05", "Genel Açıklamalar hariç tutması"],
  ["Kakao ile aromalandırılmış sütten içecek", "22.02", "04.02 hariç tutması"],
  ["Kuru maddede %95’ten fazla laktoz içeren peyniraltı suyu ürünü", "17.02", "Fasıl 4 Not 5(b)"],
  ["Suni bal; tabii bal ile suni bal karışımı", "17.02", "04.09 hariç tutması"],
  ["Kazein; sertleştirilmiş kazein", "35.01 / 39.13", "Genel Açıklamalar"],
  ["Yumurta beyazı; %80’den fazla peyniraltı suyu proteinli konsantre", "35.02", "04.08 hariç tutması; Not 5(d)"],
  ["Yumurta sarısı yağı; kaplumbağa yumurtası yağı", "15.06", "04.08 ve 04.10 hariç tutmaları"],
  ["Baharat veya çeşni katılmış yumurta ürünü", "21.06", "04.08 hariç tutması"],
  ["Lesitin", "29.23", "04.08 hariç tutması"],
  ["Süt dışı yağ içeren veya %39’dan az süt yağlı sürülebilir yağ", "15.17 / 21.06", "04.05 hariç tutması"],
  ["İnsan tüketimine uygun olmayan cansız böcek", "05.11", "Fasıl 4 Not 5(a)"],
  ["Hayvan kanı (yenilsin yenilmesin)", "05.11 / 30.02", "04.10 hariç tutması"],
  ["Yenilebilir balık yumurtası", "Fasıl 3", "Fasıl 4 yalnız kuş ve kümes hayvanı yumurtasını kapsar; 05.11 Açıklama Notu"]
 ],
 "tuzaklar": [
  "<b>Tereyağı eşiği iki uçludur.</b> Süt yağı %80 veya daha fazla olup %95’i geçmemeli; %39 ile %80’in altı arası sürülerek yenilen süt ürünüdür. %39’un altı veya süt dışı yağ içeren sürülebilir yağ 04.05 dışıdır (genellikle 15.17 veya 21.06).",
  "<b>Şekerli yoğurt 04.02’ye gitmez.</b> 04.03 konsantre, tatlandırılmış, aromalı, meyveli veya kakaolu fermente ürünleri kendisi kapsar; 04.02 ise fermente süt ve kremayı hariç tutar.",
  "<b>Peyniraltı suyundan peynir 04.04 değil 04.06.</b> Not 4’ün üç şartı (kuru maddede süt yağı %5 veya fazla, kuru madde %70–85, kalıp) sağlanırsa ürün peynirdir.",
  "<b>Laktoz %95 sınırı “fazla” ile çalışır.</b> Peyniraltı suyundan elde edilip kuru maddede %95’ten fazla laktoz içeren ürün 17.02’ye gider; bu eşiği aşmayan ürün 17.02’ye gönderilemez.",
  "<b>Yumurtada kabuk, pişirmeden önemlidir.</b> Haşlanmış kabuklu yumurta 04.07’de; kabuksuz pişirilmiş yumurta 04.08’de; yumurta beyazı (albümin) 35.02’de.",
  "<b>Bala bir damla suni bal katılırsa 04.09 biter.</b> Tabii bal ile suni bal karışımı 17.02’dedir.",
  "<b>Böcekte iki ölçüt: yenilebilirlik ve işlem.</b> İnsan tüketimine uygun, kurutulmuş, tuzlanmış, tütsülenmiş veya dondurulmuş böcek ve böcek unu 04.10; yenmeyen 05.11; başka şekilde hazırlanmış yenilebilir böcek genellikle Bölüm IV.",
  "<b>Kaplanmış peynir hâlâ peynirdir.</b> Sulu hamur veya ekmek kırıntısıyla kaplanmış, önceden pişirilmiş peynir, peynir karakterini koruyorsa 04.06’da kalır.",
  "<b>Kan Fasıl 4’te değildir.</b> Yenilebilir olsa bile sıvı veya kurutulmuş hayvan kanı 05.11’de (tedavi amacıyla hazırlanmışsa 30.02).",
  "<b>Kazein ve süt albümini süt ürünü pozisyonuna girmez.</b> Kazein 35.01, süt albümini 35.02, sertleştirilmiş kazein 39.13."
 ],
 "hafiza": {
  "kanca": "Kova → Kazan → Maya → Süzgeç → Yayık → Kalıp  |  Sepet → Kâse → Kovan → Raf",
  "aciklama": "Mandırayı dolaşın: sağım <b>kova</b>sı sade süt 04.01, koyulaştırma <b>kazan</b>ı 04.02, <b>maya</b> küpü yoğurt-kefir 04.03, peynir <b>süzgec</b>inden akan peyniraltı suyu 04.04, <b>yayık</b> tereyağı 04.05, <b>kalıp</b> peynir 04.06. Kümeste kabuklu yumurta <b>sepet</b>i 04.07, kırılmış yumurta <b>kâse</b>si 04.08, arı <b>kovan</b>ı 04.09; en sondaki “başka yerde yok” <b>raf</b>ında böcek, kaplumbağa yumurtası ve kuş yuvası 04.10."
 },
 "sinav_odagi": [
  "Yenilebilirlik ölçütü: insan tüketimine uygun, kurutulmuş ve tuzlanmış çekirgenin 04.10’da; insan tüketimine uygun olmayan cansız böceklerin 05.11’de sınıflandırıldığı.",
  "“Hangisi 4. fasılda yer almaz?” kalıbında kuş yumurtalarının balık yumurtası, kaplumbağa yumurtası (04.10) ve yenilebilir böceklerle birlikte seçeneklere konması.",
  "Suni balın (tabii balla karıştırılmış olsun olmasın) 04.09 yerine 17.02’de yer aldığı.",
  "Ürün–pozisyon eşleştirmelerinde yumurta sarısının 04.08’de olduğu; diğer fasıllardaki gıdalarla birlikte “yanlış eşleştirme hangisi” kalıbı.",
  "GYK 3(b) takım sorularında rendelenmiş peynirin (04.06) makarna takımının bir unsuru olarak yer alması; takımın esas niteliği veren eşyaya göre sınıflandırılması."
 ],
 "cikmis_ornekler": [
  {
   "soru": "Tarife Cetveline göre insan tüketimine uygun kurutulmuş ve tuzlanmış çekirge hangi tarife pozisyonundadır?",
   "secenekler": ["04.09", "04.10", "05.09", "05.11", "16.02"],
   "cevap": "B",
   "aciklama": "Fasıl 4 Not 6’ya göre insan tüketimine uygun, kurutulmuş, tuzlanmış veya salamura edilmiş cansız böcekler 04.10’dadır. İnsan tüketimine uygun olmayanlar 05.11’e gider; 04.09 tabii baldır."
  },
  {
   "soru": "İnsan tüketimine uygun olmayan cansız böcekler aşağıdaki seçeneklerde yer verilen hangi tarife pozisyonunda sınıflandırılmaktadır?",
   "secenekler": ["04.09", "04.10", "05.08", "05.10", "05.11"],
   "cevap": "E",
   "aciklama": "Fasıl 4 Not 5(a) insan tüketimine uygun olmayan cansız böcekleri fasıl dışında bırakarak 05.11’e gönderir; 04.10 yalnızca insan tüketimine uygun böcekleri kapsar."
  }
 ],
 "ozet": [
  "Süt ürünü sırası: sade 04.01 → konsantre/tatlı 04.02 → fermente 04.03 → peyniraltı suyu 04.04 → süt yağı 04.05 → peynir 04.06.",
  "Tabii bileşeni değiştirilmiş süt ürünü 19.01 / 21.06; dondurma 21.05; kakaolu sütten içecek 22.02; kazein 35.01.",
  "Eşikler: tereyağı süt yağı %80–95; sürülerek yenilen %39–%80’den az; peyniraltı suyu peyniri kuru madde %70–85 ve kuru maddede süt yağı %5+; laktoz %95’ten fazla → 17.02; peyniraltı suyu proteini %80’den fazla → 35.02.",
  "Yumurta: kabuklu 04.07, kabuksuz ve sarı 04.08, beyazı 35.02, baharatlı yumurta ürünü 21.06.",
  "Bal katkısızsa 04.09; suni bal ve karışımı 17.02.",
  "Yenilebilir böcek, kaplumbağa yumurtası, kuş yuvası 04.10; yenmeyen böcek ve hayvan kanı 05.11."
 ],
 "sorular": []
}

S = obj["sorular"]

# 1 — C
S.append(q(
 "Tarife Cetveline göre, şekerle tatlandırılmış, kakao ve fındık parçaları ilave edilmiş ve yoğurdun esas karakterini koruyan yoğurt hangi tarife pozisyonunda sınıflandırılır?",
 ["04.02", "19.01", "*04.03", "21.06", "04.04"],
 T_E,
 "04.03 pozisyon metni yoğurdu, ilave şeker veya tatlandırıcı katılmış olsun olmasın, aroma, meyve, sert kabuklu meyve veya kakao içersin içermesin kapsar; Not 2 de bu katkıları sayar. 04.02 fermente sütü hariç tutar. Katkılar süt bileşeninin yerini almadığından ürün 19.01 veya 21.06’ya da gitmez.",
 "Fasıl 4 Not 2; 04.03 pozisyon metni ve Açıklama Notu."
))
# 2 — A
S.append(q(
 "Tarife Cetveline göre, haşlanmış ancak kabuğu soyulmamış bıldırcın yumurtası hangi tarife pozisyonunda sınıflandırılır?",
 ["*04.07", "04.08", "04.10", "21.06", "16.02"],
 T_E,
 "04.07 bütün kuşların ve kümes hayvanlarının kabuklu yumurtalarını kapsar; pozisyon metni pişirilmiş kabuklu yumurtayı açıkça içine alır. 04.08 kabuksuz yumurta ve yumurta sarısı içindir. 04.10 kaplumbağa yumurtası gibi başka yerde yer almayan ürünleri kapsar. Tuzak, “pişmiş” kelimesini fasıl dışı sanmaktır.",
 "04.07 pozisyon metni ve Açıklama Notu."
))
# 3 — D
S.append(q(
 "Tarife Cetveline göre, tereyağı veya kremadan su ve yağ dışı maddelerin ayrılmasıyla elde edilen susuz süt yağı (butteroil) hangi tarife pozisyonunda sınıflandırılır?",
 ["04.01", "04.04", "15.17", "*04.05", "21.06"],
 T_E,
 "04.05 “sütten elde edilen diğer katı ve sıvı yağlar” grubunda süt yağı, süt kaymağı ve susuz süt yağını (butteroil) sayar. 04.01 süt ve kremayı, 04.04 peyniraltı suyunu kapsar. 15.17 ve 21.06, süt yağı dışında yağ içeren sürülebilir ürünler için anılır.",
 "04.05 Açıklama Notu."
))
# 4 — B
S.append(q(
 "Tarife Cetveline göre, kuşların salgıladığı ve hava ile temas edince sertleşen bir maddeden oluşan, tüy ve kirlerden temizlenmiş salangan yuvaları (“kuş yuvası”) hangi tarife pozisyonunda sınıflandırılır?",
 ["05.05", "*04.10", "05.11", "04.08", "21.06"],
 T_E,
 "04.10 Açıklama Notu salangan yuvalarını, tarifenin başka yerinde yer almayan yenilebilir hayvansal ürünler arasında açıkça sayar; tüketime uygun hale getirmek için temizlenmeleri pozisyonu değiştirmez. 05.05 kuş derileri ve tüyleri, 05.11 yenmeyen hayvansal ürünler içindir.",
 "04.10 Açıklama Notu (2)."
))
# 5 — E
S.append(q(
 "Tarife Cetveline göre, normal fiziki halini muhafaza edebilmesi için ağırlıkça %3 oranında nişasta ilave edilmiş yağsız süt tozu hangi tarife pozisyonunda sınıflandırılır?",
 ["04.01", "04.04", "11.08", "19.01", "*04.02"],
 T_E,
 "Not 1’e göre yağsız süt de “süt”tür; toz haline getirilmiş süt konsantre edilmiş süt olarak 04.02’dedir. 04.02 Açıklama Notu, süt tozunun fiziki halini korumak için ağırlıkça %5’i aşmayan nişasta içerebileceğini belirtir; %3 bu sınırın içindedir. 04.01 konsantre edilmemiş süt, 04.04 peyniraltı suyu içindir.",
 "Fasıl 4 Not 1; 04.02 Açıklama Notu."
))
# 6 — E
S.append(q(
 "Aşağıdakilerden hangisi Tarife Cetvelinin 4. faslında <b>sınıflandırılmaz</b>?",
 ["Keçi sütünden elde edilmiş tereyağı",
  "Ekmek kırıntısıyla kaplanıp önceden pişirilmiş, peynir karakterini koruyan peynir",
  "Kurutulmuş yumurta sarısı",
  "Vitamin ve mineral tuzlarıyla zenginleştirilmiş süt",
  "*Süt ürünlerinden yapılmış dondurma"],
 T_O,
 "Fasıl 4 Genel Açıklamaları dondurma ve diğer yenilebilir buzları fasıl dışında bırakır (21.05). Keçi sütü tereyağı 04.05’te, kaplanmış ve önceden pişirilmiş peynir peynir karakterini koruduğu için 04.06’da, kurutulmuş yumurta sarısı 04.08’de, vitaminle zenginleştirilmiş süt ise Fasıl 4’te kalır.",
 "Fasıl 4 Genel Açıklamalar; 04.05 ve 04.06 Açıklama Notları."
))
# 7 — D
S.append(q(
 "Aşağıdakilerden hangisi 04.04 pozisyonunda <b>sınıflandırılmaz</b>?",
 ["Toz halindeki peyniraltı suyu",
  "İlave şeker içeren konsantre peyniraltı suyu",
  "Proteince zengin ürün elde etmek için tabii süt bileşenleri ilave edilmiş süt",
  "*Tabii sütle aynı nitel ve nicel bileşime sahip rekonstitüe yağsız süt",
  "Hayvan yemi katkısı olarak kullanılacak, az miktarda laktik maya içeren toz peyniraltı suyu"],
 T_O,
 "04.04 Açıklama Notu, tabii sütle aynı nitel ve nicel bileşime sahip yağsız süt ve rekonstitüe sütü hariç tutar; bunlar 04.01 veya 04.02’dedir. Toz veya konsantre peyniraltı suyu, şekerli peyniraltı suyu, tabii süt bileşeni ilave edilmiş süt ve laktik mayalı toz peyniraltı suyu ise 04.04 kapsamındadır.",
 "04.04 Açıklama Notu."
))
# 8 — B
S.append(q(
 "Aşağıdakilerden hangisi 04.08 pozisyonunda <b>yer almaz</b>?",
 ["Silindir şeklinde kalıplanmış “uzun yumurta”",
  "*Yumurta sarısı yağı",
  "Şeker ilave edilmiş dondurulmuş yumurta sarısı",
  "Debagatta kullanılmak üzere kurutulmuş kabuksuz yumurta",
  "Buharda pişirilmiş kabuksuz yumurta"],
 T_O,
 "04.08 Açıklama Notu yumurta sarısı yağını hariç tutar ve 15.06’ya gönderir. Kalıplanmış, şekerli, dondurulmuş, buharda pişirilmiş kabuksuz yumurtalar ve sarılar 04.08’dedir; sanayide (ör. debagatta) kullanılmaları da pozisyonu değiştirmez.",
 "04.08 pozisyon metni ve Açıklama Notu."
))
# 9 — C
S.append(q(
 "Aşağıdakilerden hangisi tabii bal olarak 04.09 pozisyonunda <b>sınıflandırılmaz</b>?",
 ["Petek parçaları içeren bal",
  "Santrifüj edilmiş, çiçek kaynağına göre adlandırılan bal",
  "*Tabii bal ile suni bal karışımı",
  "Apis mellifera dışındaki böceklerin ürettiği katkısız bal",
  "Rengine göre tanımlanan, hiçbir madde katılmamış bal"],
 T_O,
 "04.09 yalnızca şeker veya başka bir madde katılmamış balı kapsar; suni bal ve tabii bal ile suni bal karışımları 17.02’dedir. Petekli veya santrifüj edilmiş bal, diğer böceklerin ürettiği bal ve çiçek kaynağı ya da rengine göre adlandırılan bal 04.09’da kalır.",
 "04.09 Açıklama Notu."
))
# 10 — A
S.append(q(
 "Tarife Cetveline göre aşağıdakilerden hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır?",
 ["*Şeker ilave edilmiş koyulaştırılmış süt", "Kefir", "Yayıkaltı", "Pıhtılaştırılmış krema", "Meyveli yoğurt"],
 T_F,
 "Kefir, yayıkaltı, pıhtılaştırılmış krema ve meyveli yoğurt fermente veya pıhtılaştırılmış ürünler olarak 04.03’tedir. Şeker ilave edilmiş koyulaştırılmış süt fermente olmadığından konsantre ve tatlandırılmış süt olarak 04.02’de yer alır. Tuzak, “şekerli” ifadesinin tek başına 04.02’ye götürdüğünü sanmaktır; şekerli yoğurt yine 04.03’tür.",
 "04.02 ve 04.03 pozisyon metinleri."
))
# 11 — D
S.append(q(
 "Tarife Cetveline göre aşağıdakilerden hangisi diğerlerinden farklı bir fasılda sınıflandırılır?",
 ["Pastörize krema", "Ghee", "Krem peynir", "*Kazein", "Kalıplanmış “uzun yumurta”"],
 T_F,
 "Fasıl 4 Genel Açıklamaları kazeini fasıl dışında bırakır (35.01). Pastörize krema 04.01’de, ghee 04.05’te, krem peynir taze peynir olarak 04.06’da, kalıplanmış “uzun yumurta” 04.08’de, yani hepsi Fasıl 4’tedir.",
 "Fasıl 4 Genel Açıklamalar (e); 04.05, 04.06, 04.08 Açıklama Notları."
))
# 12 — B
S.append(q(
 "Tarife Cetveline göre aşağıdaki eşya çiftlerinden hangisinde her iki eşya <b>aynı</b> pozisyonda sınıflandırılır? (Ürünlere belirtilenler dışında işlem uygulanmamış ve madde katılmamıştır.)",
 ["Haşlanmış kabuklu yumurta – haşlanmış kabuksuz yumurta",
  "*Pastörize krema – homojenize edilmiş yağsız süt",
  "Peyniraltı suyu – peyniraltı suyundan yapılmış peynir",
  "Tabii bal – suni bal",
  "Kefir – yağsız süt tozu"],
 T_F,
 "Not 1’e göre yağsız süt de süttür; konsantre edilmemiş ve tatlandırılmamış süt ve krema, pastörize veya homojenize olsun, 04.01’dedir. Kabuklu yumurta 04.07 iken kabuksuz yumurta 04.08; peyniraltı suyu 04.04 iken ondan yapılan peynir 04.06; tabii bal 04.09 iken suni bal 17.02; kefir 04.03 iken süt tozu 04.02’dedir.",
 "Fasıl 4 Not 1; 04.01 Açıklama Notu."
))
# 13 — E
S.append(q(
 "Aşağıdaki süt ürünlerinden hangisi Tarife Cetvelinde diğerlerinden farklı bir pozisyonda yer alır?",
 ["Peyniraltı suyundan yapılmış taze peynir", "Rendelenmiş parmesan", "Eritme peynir", "Mavi küflü peynir", "*Toz halindeki peyniraltı suyu"],
 T_F,
 "04.06 her cins peyniri kapsar: peyniraltı suyundan yapılmış peynirler dahil taze peynir, rendelenmiş peynir, eritme (işlenmiş) peynir ve mavi küflü peynir. Toz halindeki peyniraltı suyu ise peynir değil, 04.04’teki peyniraltı suyudur. Tuzak, “peyniraltı suyu” ifadesi geçen her ürünü aynı pozisyona koymaktır.",
 "04.04 ve 04.06 Açıklama Notları."
))
# 14 — A
S.append(q(
 "Tarife Cetvelinin 4. Fasıl notlarına göre “tereyağı” ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
 ["*Süt yağı oranı ağırlıkça %80 veya daha fazla olup %95’i geçmez; su oranı en fazla %16’dır.",
  "Süt yağı oranı ağırlıkça %39 veya daha fazla olup %80’den az olan emülsiyondur.",
  "İlave emülsifiye edici madde içerebilir; ancak gıda boyası içeremez.",
  "Yağsız katı madde oranı ağırlıkça en fazla %5 olabilir.",
  "Peyniraltı suyundan elde edilen tereyağı bu tanımın dışında kalır."],
 T_N,
 "Not 3(a)’ya göre tereyağının süt yağı ağırlıkça %80 veya daha fazla olup %95’i geçmez, yağsız katı madde en fazla %2, su en fazla %16’dır. %39–%80’den az aralığı sürülerek yenilen süt ürünlerine aittir. Tereyağı ilave emülsifiye edici içermez ama gıda boyası içerebilir; peyniraltı suyu tereyağı da tanıma dahildir.",
 "Fasıl 4 Not 3(a) ve 3(b)."
))
# 15 — D
S.append(q(
 "Fasıl 4 Not 6’ya göre, 04.10 pozisyonu anlamında “böcek” tabiri ile ilgili aşağıdakilerden hangisi <b>yanlıştır</b>?",
 ["Bütün veya parça halinde olabilir.",
  "Tütsülenmiş, tuzlanmış veya salamura edilmiş olabilir.",
  "Böceklerin insan tüketimine uygun un ve kaba unlarını da kapsar.",
  "*Başka şekillerde hazırlanmış veya konserve edilmiş yenilen böcekleri de kapsar.",
  "İnsan tüketimine uygun olmayan cansız böcekleri kapsamaz."],
 T_N,
 "Not 6, 04.10’daki böcekleri bütün veya parça halinde; taze, soğutulmuş, dondurulmuş, kurutulmuş, tütsülenmiş, tuzlanmış veya salamura edilmiş, insan tüketimine uygun cansız böcekler ile bunların un ve kaba unları olarak tanımlar. Başka şekillerde hazırlanmış veya konserve edilmiş yenilen böcekler kapsam dışıdır (genellikle Bölüm IV).",
 "Fasıl 4 Not 6."
))
# 16 — C
S.append(q(
 "Fasıl 4 notları ve açıklama notlarına göre aşağıdaki eşik–sonuç ilişkilerinden hangisi <b>yanlıştır</b>?",
 ["Kuru maddede %80’den fazla peyniraltı suyu proteini içeren, iki veya daha fazla peyniraltı suyu proteini konsantresi → 35.02",
  "Katı yağ olarak yalnız süt yağı içeren, süt yağı ağırlıkça %50 olan yağ içinde su tipi sürülebilir emülsiyon → 04.05",
  "*Kuru madde üzerinden ağırlıkça %90 laktoz içeren peyniraltı suyu ürünü → 17.02",
  "Süt yağı dışında yağ içeren sürülerek yenilen yağ → genellikle 15.17 veya 21.06",
  "Fiziki halini korumak için ağırlıkça %5’i aşmayan nişasta içeren süt tozu → 04.02"],
 T_N,
 "Not 5(b) yalnızca kuru madde üzerinden ağırlıkça %95’ten fazla laktoz içeren peyniraltı suyu ürünlerini 17.02’ye gönderir; %90 laktozlu ürün bu eşiği aşmaz. Diğer ilişkiler Not 5(d), Not 3(b), 04.05 ve 04.02 Açıklama Notlarıyla uyumludur.",
 "Fasıl 4 Not 3(b), Not 5(b) ve 5(d); 04.02 ve 04.05 Açıklama Notları."
))
# 17 — B
S.append(q(
 "Fasıl 4 açıklama notlarına göre, tabii bileşeni değiştirilmiş süt ürünleriyle ilgili hükümde geçen “bütirik yağlar” ve “oleik yağlar” ifadeleri için aşağıdakilerden hangisi <b>doğrudur</b>?",
 ["Bütirik yağlar bitkisel yağları, oleik yağlar süt yağlarını ifade eder; bu ürünler 04.05’te kalır.",
  "*Bütirik yağlar süt yağlarını, oleik yağlar süt yağı dışındaki yağları ifade eder; bu ürünler 19.01 veya 21.06’dadır.",
  "Her iki ifade de süt yağlarının çeşitlerini ifade eder; bu ürünler 04.04’te sınıflandırılır.",
  "Bütirik yağlar süt yağlarını, oleik yağlar yalnız hayvansal yağları ifade eder; bu ürünler 04.03’tedir.",
  "Bütirik yağlar süt yağlarını, oleik yağlar süt yağı dışındaki yağları ifade eder; bu ürünler 04.01’de kalır."],
 T_N,
 "Genel Açıklamalara göre “bütirik yağlar” süt yağlarını, “oleik yağlar” süt yağları dışındaki yağları (özellikle bitkisel yağlar, zeytinyağı) ifade eder. Not 5(c) uyarınca süt yağı alınıp yerine bu tür yağ konulan süt ürünleri Fasıl 4 dışında, 19.01 veya 21.06’dadır. Son seçenekte tanım doğru, sonuç yanlıştır.",
 "Fasıl 4 Not 5(c); Fasıl 4 Genel Açıklamalar."
))
# 18 — A
S.append(q(
 "Fasıl 4 başlığında “yenilebilir hayvansal menşeli ürünler” ifadesi yer almasına rağmen, yenilebilir nitelikteki kurutulmuş hayvan kanının Fasıl 4’te değil 05.11 pozisyonunda sınıflandırılması hangi Genel Yorum Kuralının gereğidir?",
 ["*GYK 1", "GYK 2(b)", "GYK 3(a)", "GYK 4", "GYK 6"],
 T_G,
 "GYK 1’e göre fasıl başlıkları yalnızca gösterici niteliktedir; sınıflandırma pozisyon metinlerine ve bölüm-fasıl notlarına göre yapılır. 04.10 Açıklama Notu hayvan kanını hariç tutar; Fasıl 5 Not 1(a) yenilebilir ürünleri dışlarken kanı istisna tutar ve 05.11 kanı, yenilsin yenilmesin, kapsar. Diğer kurallara başvurmaya gerek kalmaz.",
 "GYK 1; 04.10 Açıklama Notu; Fasıl 5 Not 1(a)."
))
# 19 — E
S.append(q(
 "Bir karton kutuda perakende satışa sunulan; pişirilmemiş bir paket spagetti, küçük bir poşet rendelenmiş peynir ve küçük bir teneke domates sosundan oluşan, spagetti yemeği hazırlamada birlikte kullanılması amaçlanan takımın sınıflandırılmasıyla ilgili aşağıdakilerden hangisi doğrudur?",
 ["GYK 3(b) uyarınca takım olarak, peynirin yer aldığı 04.06’da sınıflandırılır.",
  "GYK 3(c) uyarınca numara sırasına göre sonuncu olan 21.03’te sınıflandırılır.",
  "Takım sayılmaz; her ürün GYK 1 uyarınca ayrı ayrı sınıflandırılır.",
  "GYK 2(b) uyarınca karışım sayılarak 04.06’da sınıflandırılır.",
  "*GYK 3(b) uyarınca takım olarak, spagettinin yer aldığı 19.02’de sınıflandırılır."],
 T_G,
 "GYK 3(b) Açıklama Notu bu takımı perakende satış takımı örneği olarak verir ve 19.02’de sınıflandırır; esas niteliği spagetti verir. Takımdaki rendelenmiş peynir (04.06) ve domates sosu (21.03) ayrı ayrı sınıflandırılmaz. GYK 3(c) ancak 3(b) ile sonuca ulaşılamazsa uygulanır.",
 "GYK 3(b) Açıklama Notu (X)."
))
# 20 — C
S.append(q(
 "Tarife Cetveline göre; kabuklu kuş yumurtaları ……, kabuksuz yumurtalar ve yumurta sarıları ……, yumurta beyazı (yumurta albümini) ise …… pozisyonunda sınıflandırılır. Boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?",
 ["04.08 – 04.07 – 35.02", "04.07 – 04.08 – 04.10", "*04.07 – 04.08 – 35.02", "04.07 – 21.06 – 35.02", "04.10 – 04.08 – 15.06"],
 T_B,
 "Kabuklu yumurtalar (taze, dayanıklı hale getirilmiş veya pişirilmiş) 04.07’de, kabuksuz yumurtalar ve yumurta sarıları 04.08’dedir. 04.08 Açıklama Notu yumurta beyazını (yumurta albümini) hariç tutarak 35.02’ye gönderir. 15.06 yumurta sarısı yağı, 21.06 baharatlı yumurta ürünleri içindir.",
 "04.07 ve 04.08 pozisyon metinleri; 04.08 Açıklama Notu."
))
# 21 — D
S.append(q(
 "Tarife Cetveline göre aşağıdaki eşya–pozisyon eşleştirmelerinden hangisi <b>doğrudur</b>?",
 ["Kefir – 04.01", "Kakao ile aromalandırılmış sütten içecek – 04.02", "Lesitin – 04.08", "*Rendelenmiş peynir – 04.06", "Suni bal – 04.09"],
 T_B,
 "04.06 rendelenmiş veya toz haline getirilmiş peynirleri de kapsar. Kefir fermente süt olarak 04.03’te; kakaolu sütten içecek 22.02’de; lesitin 29.23’te; suni bal 17.02’dedir.",
 "04.06 Açıklama Notu; 04.02, 04.08, 04.09 Açıklama Notları."
))
# 22 — B
S.append(q(
 "Fasıl 4 Not 2’ye göre aşağıdakilerden hangileri, 04.03 anlamındaki yoğurdun içerebileceği maddeler arasında sayılmıştır?  I. Kahve hülasası  II. Hububat ve ekmekçi mamulleri  III. Süt yağının yerini kısmen alan bitkisel yağ  IV. Çikolata",
 ["I ve II", "*I, II ve IV", "II ve III", "III ve IV", "I, II, III ve IV"],
 T_C,
 "Not 2 yoğurdun şeker, meyve, sert kabuklu meyve, kakao, çikolata, baharat, kahve veya kahve hülasası, bitki, hububat ve ekmekçi mamulleri içerebileceğini sayar. Ancak eklenen madde süt içeriğini tamamen veya kısmen ikame etme amaçlı olmamalıdır; süt yağının yerini alan bitkisel yağ bu nedenle yoğurt tanımını bozar.",
 "Fasıl 4 Not 2; 04.03 Açıklama Notu."
))
# 23 — A
S.append(q(
 "Tarife Cetveline göre aşağıdaki ifadelerden hangileri <b>doğrudur</b>?  I. Vitamin veya mineral tuzlarıyla zenginleştirilmiş süt Fasıl 4’te kalır.  II. 04.02’deki süt tozundan yapılan fermente süt 04.02’de sınıflandırılır.  III. Sterilize veya homojenize edilmiş, konsantre edilmemiş ve tatlandırılmamış süt 04.01’dedir.  IV. Bir veya daha fazla tabii süt bileşenini içermeyen, başka yerde yer almayan süt bileşeni ürünleri 04.01’dedir.",
 ["*I ve III", "I, II ve III", "II ve IV", "III ve IV", "I ve IV"],
 T_C,
 "Genel Açıklamalara göre vitamin veya mineral tuzlarıyla zenginleştirme ürünü fasıl dışına çıkarmaz (I doğru); sterilize veya homojenize süt 04.01’dedir (III doğru). 04.03 Açıklama Notuna göre süt tozundan yapılan fermente süt 04.03’tedir (II yanlış). Tabii bileşenlerinden bir veya daha fazlasını içermeyen süt ürünleri 04.04’tedir (IV yanlış).",
 "Fasıl 4 Genel Açıklamalar; 04.01, 04.03, 04.04 Açıklama Notları."
))
# 24 — C
S.append(q(
 "Bir firma, peyniraltı suyunu konsantre edip süt yağı ilave ederek bir ürün elde etmiştir. Ürünün kuru madde oranı ağırlıkça %78, süt yağı oranı kuru madde üzerinden %12’dir ve ürün kalıplar halinde sunulmaktadır. Tarife Cetveline göre bu ürün hangi pozisyonda sınıflandırılır?",
 ["04.04", "04.05", "*04.06", "17.02", "19.01"],
 T_S,
 "Not 4’e göre peyniraltı suyu konsantrasyonu ve süt veya süt yağı ilavesiyle elde edilen ürün; kuru maddede süt yağı %5 veya daha fazla, kuru madde %70–85 arasında ve kalıplanmış ise 04.06’da peynirdir. Üç şart da sağlandığından ürün 04.04’te kalmaz. Laktoz eşiği (17.02) veya bileşen ikamesi (19.01) söz konusu değildir.",
 "Fasıl 4 Not 4; 04.06 Açıklama Notu."
))
# 25 — E
S.append(q(
 "Kabukları kırılarak çırpılmış tavuk yumurtalarına karabiber ve diğer baharatlar katılmış, ürün dondurularak plastik kaplarda gıda sanayiine sunulmaktadır. Tarife Cetveline göre bu ürün hangi pozisyonda sınıflandırılır?",
 ["04.08", "04.07", "04.10", "16.02", "*21.06"],
 T_S,
 "Kabuksuz ve dondurulmuş yumurta normalde 04.08’dedir; ancak 04.08 Açıklama Notu baharat, çeşni verici veya diğer katkı maddelerini içeren yumurta ürünlerini hariç tutarak 21.06’ya gönderir. Dondurulması ve sanayide kullanılması değil, baharat katılması belirleyicidir. Kabuk olmadığından 04.07 de söz konusu değildir.",
 "04.08 Açıklama Notu, hariç tutmalar (b)."
))

yaz(4, obj)
