import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yardim_04_08 import q, yaz, harf_ata, T_E, T_O, T_F, T_N, T_G, T_B, T_C, T_S  # noqa: E402

obj = {
 "tur": "fasil",
 "fasil": 8,
 "baslik": "Yenilen meyveler ve yenilen sert kabuklu meyveler; turunçgillerin ve kavun ve karpuzların kabukları",
 "bolum": "II",
 "oz": {
  "vurgu": "Fasıl 8 yenilen meyve ve sert kabuklu meyveleri taze, soğutulmuş, dondurulmuş, geçici korunmuş veya kurutulmuş halde kapsar. Yapı “6 + 4 + 4”tür: 08.01–08.06 adı geçen meyveleri taze ve kuru halde, 08.07–08.10 yalnız taze meyveleri, 08.11–08.14 ise halleri (dondurulmuş, geçici korunmuş, kurutulmuş, kabuk) toplar. Fasılda öngörülmeyen bir hazırlık görmüş meyve Fasıl 20’ye gider.",
  "maddeler": [
   "Yenilmeyen meyveler ve sert kabuklu meyveler fasıl dışıdır (Not 1); soğutulmuş meyve tazesiyle aynı pozisyondadır (Not 2).",
   "Kurutulmuş meyve, karakterini korumak şartıyla kısmen rehidre edilebilir; kükürtleme, sorbik asit veya potasyum sorbat, bitkisel yağ veya az miktarda glikoz şurubu ilavesi faslı değiştirmez (Not 3).",
   "Sebze sayılan meyveler (zeytin, domates, biber, kabak, patlıcan) Fasıl 7; yer fıstığı ve diğer yağlı meyveler Fasıl 12; kahve, vanilya, ardıç Fasıl 9; kakao 18.01.",
   "Kaju, Hindistan cevizi ve Brezilya cevizi 08.01’de adıyla; fındık, badem, ceviz, kestane, Antep fıstığı ve diğerleri 08.02’de.",
   "Ozmotik dehidrasyonla şeker şurubunda suyu alınan meyve 20.08; şekerli meyve kabuğu 20.06; meyve unu ve tozu 11.06."
  ]
 },
 "karar_tablosu": {
  "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
  "satirlar": [
   ["1", "Yenilmeyen bir meyve mi?", "Fasıl 8 dışı (ör. at kestanesi <b>23.08</b>; “orange peas” <b>12.11</b>)"],
   ["2", "Tarifede sebze sayılan meyve mi? (zeytin, domates, hıyar, kabak, patlıcan, Capsicum, Pimenta)", "Fasıl <b>7</b>"],
   ["3", "Yer fıstığı, yağlı meyve, keçiboynuzu, meyve çekirdeği; kahve, vanilya, ardıç; kakao tanesi mi?", "Fasıl <b>12</b> · Fasıl <b>9</b> · <b>18.01</b>"],
   ["4", "Fasılda öngörülmeyen bir hazırlık görmüş mü? (buhar veya kaynatma dışında pişirme, ozmotik dehidrasyon, şekerleme, kavurma, öğütme)", "Fasıl <b>20</b> · kahve yerine kavrulmuş <b>21.01</b> · un-toz <b>11.06</b>"],
   ["5", "Turunçgil veya kavun-karpuz kabuğu mu?", "<b>08.14</b> (toz kabuk <b>11.06</b>, şekerli kabuk <b>20.06</b>)"],
   ["6", "Geçici olarak korunmuş ve bu haliyle hemen yenmeye elverişsiz mi?", "<b>08.12</b>"],
   ["7", "Dondurulmuş mu? (önce buharda veya suda pişirilmiş, şekerli olabilir)", "<b>08.11</b>"],
   ["8", "Bu fasıldaki sert kabuklu meyvelerin veya kurutulmuş meyvelerin birbiriyle karışımı mı?", "<b>08.13</b>"],
   ["9", "Adı 08.01–08.06’da geçen tek bir meyve mi? (taze veya kurutulmuş)", "<b>08.01</b>–<b>08.06</b>"],
   ["10", "Diğer bir kurutulmuş meyve mi?", "<b>08.13</b>"],
   ["11", "Taze (soğutulmuş dahil) diğer meyve mi?", "Kavun-papaya <b>08.07</b> · elma-armut-ayva <b>08.08</b> · kayısı-kiraz-şeftali-erik <b>08.09</b> · diğerleri <b>08.10</b>"]
  ],
  "dipnot": "* Soğutulmuş meyve tazesiyle aynı pozisyondadır (Not 2). Hava almayacak şekilde paketlenmiş (teneke kutuda kuru erik, fındık) veya MAP ile paketlenmiş (taze çilek) meyveler, fasılda belirtilmeyen bir işlem görmedikçe Fasıl 8’de kalır."
 },
 "pozisyon_haritasi": [
  ["08.01", "Hindistan cevizi, Brezilya cevizi, kaju cevizi", "Taze veya kurutulmuş; kabuklu veya kabuksuz", "Rendelenmiş kuru Hindistan cevizi, kaju içi"],
  ["08.02", "Diğer sert kabuklu meyveler", "Taze veya kurutulmuş; kabuklu veya kabuksuz", "Fındık, badem, ceviz, kestane, Antep fıstığı, kola, arek"],
  ["08.03", "Muz (plantain dahil)", "Musa cinsi; taze veya kurutulmuş", "Muz, plantain, kuru muz"],
  ["08.04", "Hurma, incir, ananas, avokado, guava, mango, mangost", "Taze veya kurutulmuş; incir yalnız Ficus carica", "Kuru incir, hurma, ananas"],
  ["08.05", "Turunçgiller", "Taze veya kurutulmuş; kabukları hariç", "Portakal, mandarin, limon, greyfurt, bergamot"],
  ["08.06", "Üzümler", "Taze veya kurutulmuş; sofralık veya şaraplık", "Sultani kuru üzüm, şaraplık üzüm"],
  ["08.07", "Kavunlar (karpuz dahil) ve papaya", "Yalnız taze", "Karpuz, kavun, Carica papaya"],
  ["08.08", "Elma, armut ve ayva", "Yalnız taze; kullanım amacı önemsiz", "Sofralık veya şıralık elma, ayva"],
  ["08.09", "Kayısı, kiraz, şeftali, erik, çakal eriği", "Yalnız taze; vişne ve nektarin dahil", "Vişne, nektarin, mürdüm eriği"],
  ["08.10", "Diğer meyveler (taze)", "Önceki pozisyonlarda ve diğer fasıllarda olmayan yenilen meyveler", "Çilek, kivi, nar, kuşburnu, Trabzon hurması, Frenk inciri"],
  ["08.11", "Dondurulmuş meyveler ve sert kabuklu meyveler", "Çiğ veya buharda-suda pişirilmiş; şeker veya tuz eklenebilir", "Dondurulmuş çilek, ahududu"],
  ["08.12", "Geçici olarak konserve edilmiş meyveler", "Kükürt dioksit, salamura; hemen yenmeye elverişsiz", "Varilde kükürtlü suda kiraz"],
  ["08.13", "Kurutulmuş meyveler (08.01–08.06 hariç); karışımlar", "Kuru meyve ve sert kabuklu meyve karışımları dahil", "Kuru kayısı, kuru erik, karışık kuruyemiş"],
  ["08.14", "Turunçgil ve kavun-karpuz kabukları", "Taze, dondurulmuş, kurutulmuş veya geçici korunmuş", "Kurutulmuş portakal kabuğu"]
 ],
 "notlar": [
  ["Fasıl 8 Not 1", "Yenilmeyen meyveler ve sert kabuklu meyveler bu fasla dahil değildir."],
  ["Fasıl 8 Not 2", "Soğutulmuş meyveler ve sert kabuklu meyveler, tazeleri ile aynı pozisyonda sınıflandırılır."],
  ["Fasıl 8 Not 3", "Kurutulmuş meyve veya kurutulmuş sert kabuklu meyve karakterini korumak şartıyla bu fasıldaki kurutulmuş meyveler kısmen rehidre edilebilir veya (a) korunmalarını ya da dayanıklılıklarını artırmak (düşük ısı işlemi, kükürtleme, sorbik asit veya potasyum sorbat ilavesi) ya da (b) görünümlerini iyileştirmek veya korumak (bitkisel yağ veya az miktarda glikoz şurubu ilavesi) amacıyla işlem görmüş olabilir."],
  ["Fasıl 8 Not 4", "08.12, kullanımdan önce taşınma veya depolama sırasında esas olarak geçici koruma sağlamak üzere işlem görmüş (kükürt dioksit gazı, salamura, kükürtlü su veya diğer koruyucu eriyikler) fakat bu halleriyle derhal yenilmeye elverişli olmayan meyve ve sert kabuklu meyvelere uygulanır."],
  ["Genel Açıklamalar", "Meyveler taze (soğutulmuş dahil), dondurulmuş (önceden buharda veya kaynar suda pişirilmiş ya da tatlandırıcı katılmış olsun olmasın), kurutulmuş (suyu alınmış, buharlaştırılmış, dondurularak kurutulmuş) veya hemen tüketilmeye uygun olmamak şartıyla geçici olarak konserve edilmiş olabilir; bütün, dilimlenmiş, çekirdeği çıkarılmış, lapa haline getirilmiş, rendelenmiş veya kabuğu soyulmuş olabilir."],
  ["Genel Açıklamalar", "“Soğutulmuş”: dondurmadan sıcaklığın genellikle <b>0 °C</b> civarına düşürülmesi; kavun, karpuz ve bazı turunçgillerde <b>+10 °C</b>’ye düşürülüp bu derecede tutulma da soğutma sayılabilir. “Dondurulmuş”: tamamen donuncaya kadar donma noktasının altına soğutma."],
  ["Genel Açıklamalar", "Tek başına homojenizasyon Fasıl 20’ye götürmez. Az miktarda şeker ilavesi sınıflandırmayı etkilemez; dış yüzeyi kendi doğal şekeriyle kaplanmış kuru hurma ve erik bu fasıldadır. Ozmotik dehidrasyon (meyve parçalarının uzun süre konsantre şeker şurubunda bekletilerek su ve doğal şekerinin şuruptaki şekerle yer değiştirmesi) ile konserve edilen meyveler 20.08’dedir."],
  ["Genel Açıklamalar", "Fasıl dışı: zeytin, domates, hıyar, kornişon, sakız kabağı, bal kabağı, patlıcan, Capsicum ve Pimenta (Fasıl 7); kahve, vanilya, ardıç meyvesi ve diğer Fasıl 9 ürünleri; yer fıstığı ve diğer yağlı meyveler, eczacılık ve parfümeri meyveleri, keçiboynuzu, kayısı vb. çekirdekleri (Fasıl 12); kakao taneleri (18.01); meyve unu, ezmesi ve tozu (11.06); başka şekilde hazırlanmış meyveler (Fasıl 20); kahve yerine kullanılan kavrulmuş meyveler (21.01)."],
  ["Genel Açıklamalar", "Hava almayacak şekilde paketlenmiş (teneke kutuda kuru erik, fındık) veya MAP ile paketlenmiş (taze çilek) meyveler bu fasılda kalır; ancak pozisyonlarda belirtilenden başka usulle hazırlanmışsa Fasıl 20’ye gider."],
  ["08.01 / 08.02 Açıklama Notları", "Rendelenmiş ve kurutulmuş Hindistan cevizi 08.01’de; yağ üretiminde kullanılan, insan tüketimine uygun olmayan kopra 12.03’tedir. 08.02 hariç: Çin su kestanesi (07.14), ceviz ve bademin boş dış kabukları (14.04), yer fıstığı (12.02), kavrulmuş yer fıstığı ve yer fıstığı ezmesi (20.08), at kestanesi (23.08)."],
  ["08.04 / 08.07 Açıklama Notları", "08.04’teki “incir” yalnız Ficus carica türüdür; kaktüs inciri (Frenk inciri) 08.10’dadır. 08.07 Carica papaya’yı kapsar; Asimina triloba türü (pawpaw) 08.10’dadır."],
  ["08.05 Açıklama Notu", "Portakal (tatlı ve acı), mandarin (tanjerin, satsuma), klementin, vilking ve benzeri melezler, greyfurt, pomelo, limon, tatlı limon, ağaç kavunu, kumkat, bergamot; konservecilikte kullanılan yeşil küçük portakal ve limonlar. Hariç: turunçgil kabukları (08.14); “orange peas” veya “orangettes” (12.11)."],
  ["08.11 Açıklama Notu", "Dondurmadan önce buharla veya kaynatılarak pişirilmiş, şeker veya tatlandırıcı katılmış ya da tuz içeren dondurulmuş meyveler buradadır; diğer metotlarla pişirilip dondurulanlar Fasıl 20’dedir."],
  ["08.13 / 08.14 Açıklama Notları", "08.13, 08.07–08.10 meyvelerinin kurutulmuşlarını, demirhindi kabuk ve etini, bu fasıldaki sert kabuklu ve kurutulmuş meyvelerin karışımlarını (bitki çayı için paketlenmiş olanlar dahil) kapsar; başka fasıllardaki bitki parçaları veya bitki ekstraktlarıyla karışımları genellikle 21.06’dadır. Toz haline getirilmiş kabuklar 11.06, şekerli meyve kabukları 20.06’dadır."]
 ],
 "sinir_komsulari": [
  ["Yer fıstığı", "12.02", "08.02 hariç tutması"],
  ["Kavrulmuş yer fıstığı; yer fıstığı ezmesi", "20.08", "08.02 hariç tutması"],
  ["Kopra (yağ üretimi için kurutulmuş Hindistan cevizi)", "12.03", "08.01 Açıklama Notu"],
  ["Ceviz ve bademin boş dış kabukları", "14.04", "08.02 hariç tutması"],
  ["At kestanesi", "23.08", "08.02 hariç tutması"],
  ["Çin su kestanesi (Eleocharis)", "07.14", "08.02 hariç tutması; Trapa natans ise 08.02"],
  ["Zeytin, domates, biber, kabak, patlıcan", "Fasıl 7", "Fasıl 8 Genel Açıklamalar"],
  ["Ardıç meyvesi", "09.09", "08.10 hariç tutması"],
  ["Keçiboynuzu; kayısı çekirdeği", "Fasıl 12", "Fasıl 8 Genel Açıklamalar"],
  ["Kakao tanesi", "18.01", "Fasıl 8 Genel Açıklamalar"],
  ["Meyve unu ve tozu; toz turunçgil kabuğu", "11.06", "Genel Açıklamalar; 08.14 hariç tutması"],
  ["Ozmotik dehidrasyonla kurutulmuş meyve", "20.08", "Fasıl 8 Genel Açıklamalar"],
  ["Şekerli meyve kabuğu", "20.06", "08.14 hariç tutması"],
  ["Kahve yerine kullanılan kavrulmuş kestane, badem, incir", "21.01", "Fasıl 8 Genel Açıklamalar"],
  ["Kuru meyvenin başka fasıl bitkileriyle karışımı", "21.06", "08.13 hariç tutması (genellikle)"]
 ],
 "tuzaklar": [
  "<b>Kaju 08.01, fındık 08.02.</b> Hindistan cevizi, Brezilya cevizi ve kaju cevizi 08.01’de adıyla sayılmıştır; diğer sert kabuklu meyveler 08.02’dedir.",
  "<b>Yer fıstığı Fasıl 8’de değildir.</b> Ham hali 12.02; kavrulmuşu ve ezmesi 20.08.",
  "<b>Kuru meyvede iki yol var.</b> 08.01–08.06’daki meyveler (kuru incir, kuru üzüm, kuru hurma, kuru muz) kendi pozisyonunda kalır; diğer kuru meyveler (kayısı, erik, elma) 08.13’e gider.",
  "<b>Dört pozisyon yalnız taze içindir.</b> 08.07–08.10 taze (soğutulmuş dahil) meyveyi kapsar; dondurulmuşu 08.11, kurutulmuşu 08.13’tedir.",
  "<b>Her incir 08.04 değildir.</b> 08.04’teki incir yalnız Ficus carica; kaktüs inciri (Frenk inciri) 08.10. Benzer şekilde Carica papaya 08.07, Asimina triloba (pawpaw) 08.10.",
  "<b>Meyve ve kabuğu ayrılır.</b> Turunçgil 08.05, kabuğu 08.14; toz kabuk 11.06, şekerli kabuk 20.06.",
  "<b>Pişirme yöntemi önemlidir.</b> Buharda veya suda pişirilip dondurulan meyve 08.11; başka yöntemle pişirilip dondurulan Fasıl 20.",
  "<b>Ozmotik dehidrasyon kurutma sayılmaz.</b> Şeker şurubunda bekletilip suyu alınan meyve 20.08; kendi doğal şekeriyle kaplı kuru hurma veya erik Fasıl 8.",
  "<b>Karışımda ortağa bakın.</b> Bu fasıldaki kuru meyve ve kuruyemişlerin karışımları 08.13; başka fasıl bitkileri veya bitki ekstraktıyla karışımları genellikle 21.06.",
  "<b>Kestane üç yere dağılır.</b> Yenilen kestane (Castanea) 08.02; at kestanesi 23.08; Çin su kestanesi 07.14."
 ],
 "hafiza": {
  "kanca": "6 + 4 + 4",
  "aciklama": "<b>İlk 6</b> (taze veya kuru): 08.01 Hindistan-Brezilya-kaju · 08.02 diğer kuruyemiş · 08.03 muz · 08.04 hurma-incir-tropikaller · 08.05 turunçgil · 08.06 üzüm. <b>Sonraki 4</b> (yalnız taze): 08.07 kavun-karpuz-papaya · 08.08 elma-armut-ayva · 08.09 kayısı-kiraz-şeftali-erik · 08.10 diğerleri. <b>Son 4</b> (hal): 08.11 donmuş · 08.12 geçici korunmuş · 08.13 kuru ve karışım · 08.14 kabuk. Pazar tezgâhı gibi: önce kuruyemişçi, sonra manav, en sonda derin dondurucu ve kuru meyve rafı."
 },
 "sinav_odagi": [
  "“Hangisi 8. fasılda sınıflandırılmaz?” kalıbı: sert kabuklu meyve sanılan ama 12.02’ye giden yer fıstığı.",
  "Pozisyon içi kapsam: “08.05’te sınıflandırılmaz” sorusunda turunçgil olmayan kivinin (08.10) ayırt edilmesi.",
  "“Diğerlerinden farklı pozisyon” kalıbı: 08.01’de adıyla sayılan kaju cevizinin, 08.02’deki fındık, kestane, pekan ve kola cevizinden ayrılması.",
  "Adı geçen meyvelerin pozisyon metinlerinin (08.01, 08.04, 08.05) bilinmesi ve “diğer” pozisyonlarının (08.02, 08.10) artık niteliği."
 ],
 "cikmis_ornekler": [
  {
   "soru": "Tarife Cetveline göre aşağıdakilerden hangisi 8 inci fasılda diğerlerinden farklı bir pozisyonda sınıflandırılır?",
   "secenekler": ["Taze fındık", "Taze kaju cevizi", "Taze kestane", "Taze pekan cevizi", "Taze kola cevizi"],
   "cevap": "B",
   "aciklama": "Kaju cevizi, Hindistan cevizi ve Brezilya ceviziyle birlikte 08.01’de adıyla sayılmıştır. Fındık, kestane, pekan ve kola cevizi “diğer kabuklu meyveler” olarak 08.02’dedir."
  },
  {
   "soru": "Aşağıdakilerden hangisi tarife cetvelinde 8. Fasılda <b>sınıflandırılmaz</b>?",
   "secenekler": ["Hindistan cevizi", "Yer fıstığı", "Kestane", "Antep fıstığı"],
   "cevap": "B",
   "aciklama": "08.02 Açıklama Notu yer fıstığını hariç tutarak 12.02’ye gönderir (kavrulmuşu ve ezmesi 20.08). Hindistan cevizi 08.01’de, kestane ve Antep fıstığı 08.02’dedir."
  }
 ],
 "ozet": [
  "08.01–08.06: adı geçen meyveler taze veya kurutulmuş; 08.07–08.10: yalnız taze (soğutulmuş dahil).",
  "Dondurulmuş 08.11; geçici korunmuş 08.12; diğer kuru meyveler ve karışımlar 08.13; turunçgil ve kavun-karpuz kabukları 08.14.",
  "Kaju 08.01, diğer kabuklu meyveler 08.02; yer fıstığı 12.02, kopra 12.03, at kestanesi 23.08.",
  "Sebze sayılan meyveler Fasıl 7; ardıç 09.09; kakao 18.01; keçiboynuzu ve çekirdekler Fasıl 12.",
  "Fasılda öngörülmeyen hazırlık (başka yöntemle pişirme, ozmotik dehidrasyon, şekerleme) Fasıl 20; meyve unu 11.06; kahve yerine kavrulmuş meyve 21.01.",
  "Ambalaj ve az şeker faslı değiştirmez: tenekede fındık, MAP’te çilek, kendi şekeriyle kaplı kuru hurma Fasıl 8’dedir."
 ],
 "sorular": []
}

S = obj["sorular"]

# 1 — E
S.append(q(
 "Tarife Cetveline göre, kurutulmuş incir (Ficus carica) hangi tarife pozisyonunda sınıflandırılır?",
 ["08.13", "08.10", "20.08", "08.12", "*08.04"],
 T_E,
 "08.04 pozisyon metni incirleri taze veya kurutulmuş olarak kapsar; 08.13 ise 08.01–08.06’daki meyveleri hariç tutar. Bu nedenle kuru incir 08.13’e değil 08.04’e girer. Tuzak, “kurutulmuş meyve” ifadesini görünce doğrudan 08.13’ü seçmektir.",
 "08.04 ve 08.13 pozisyon metinleri; 08.04 Açıklama Notu."
))
# 2 — B
S.append(q(
 "Tarife Cetveline göre, taze nar hangi tarife pozisyonunda sınıflandırılır?",
 ["08.09", "*08.10", "08.07", "08.08", "08.04"],
 T_E,
 "08.10 faslın önceki pozisyonlarında ve tarifenin diğer fasıllarında yer almayan bütün taze yenilen meyveleri kapsar; Açıklama Notu narı açıkça sayar. 08.04 hurma, incir ve tropikal meyveler; 08.07 kavunlar; 08.08 elma-armut-ayva; 08.09 kayısı-kiraz-şeftali-erik içindir.",
 "08.10 Açıklama Notu."
))
# 3 — D
S.append(q(
 "Tarife Cetveline göre, kurutulmuş ve kabuğu çıkarılmış çam fıstığı hangi tarife pozisyonunda sınıflandırılır?",
 ["08.01", "08.13", "12.02", "*08.02", "20.08"],
 T_E,
 "08.02 diğer sert kabuklu meyveleri taze veya kurutulmuş, kabuğu çıkarılmış veya soyulmuş olsun olmasın kapsar; Açıklama Notu çam fıstığını başlıca kabuklu meyveler arasında sayar. 08.13 kuru meyveler içindir ve sert kabuklu meyveyi tek başına almaz; 12.02 yer fıstığına aittir.",
 "08.02 pozisyon metni ve Açıklama Notu."
))
# 4 — A
S.append(q(
 "Tarife Cetveline göre, kabuğu çıkarılmış, rendelenmiş ve kurutulmuş, insan tüketimine uygun Hindistan cevizi hangi tarife pozisyonunda sınıflandırılır?",
 ["*08.01", "12.03", "08.13", "08.02", "11.06"],
 T_E,
 "08.01 Açıklama Notu kabukları çıkarılmış, rendelenmiş ve kurutulmuş Hindistan cevizini bu pozisyonda tutar. Hindistan cevizinin etli kısımlarının kurutulmasıyla elde edilen, insan tüketimine uygun olmayıp yağ üretiminde kullanılan kopra ise 12.03’tedir. Tuzak, “kurutulmuş Hindistan cevizi” ile kopranın karıştırılmasıdır.",
 "08.01 Açıklama Notu."
))
# 5 — C
S.append(q(
 "Tarife Cetveline göre, şeker ilave edilerek dondurulmuş ahududu hangi tarife pozisyonunda sınıflandırılır?",
 ["08.10", "08.12", "*08.11", "08.13", "20.08"],
 T_E,
 "08.11 dondurulmuş meyveleri, ilave şeker veya diğer tatlandırıcı katılmış olsun olmasın kapsar; Açıklama Notu şekerin çözme sırasında renk değişimini önlediğini belirtir. Taze ahududu 08.10’da olurdu; şeker ilavesi tek başına Fasıl 20’ye götürmez.",
 "08.11 pozisyon metni ve Açıklama Notu."
))
# 6 — C
S.append(q(
 "Aşağıdakilerden hangisi Tarife Cetvelinin 8. faslında <b>sınıflandırılmaz</b>?",
 ["Taze avokado",
  "Dış yüzeyi kendi doğal şekeriyle kaplanmış kuru hurma",
  "*Kakao taneleri",
  "Teneke kutuda sunulan kabuksuz fındık",
  "Modifiye atmosferde paketlenmiş (MAP) taze çilek"],
 T_O,
 "Fasıl 8 Genel Açıklamaları kakao tanelerini fasıl dışında bırakarak 18.01’e gönderir. Avokado 08.04’te; kendi şekeriyle kaplı kuru hurma, hava almayacak şekilde paketlenmiş fındık ve MAP ile paketlenmiş taze çilek ise açıklama notlarına göre Fasıl 8’de kalır.",
 "Fasıl 8 Genel Açıklamalar."
))
# 7 — A
S.append(q(
 "Aşağıdakilerden hangisi 08.05 pozisyonunda <b>yer almaz</b>?",
 ["*Kurutulmuş portakal kabuğu", "Seville (acı) portakalı", "Bergamot", "Kumkat", "Konservecilikte kullanılan yeşil küçük limonlar"],
 T_O,
 "08.05 Açıklama Notu turunçgil meyvelerinin kabuklarını hariç tutarak 08.14’e gönderir. Acı portakal, bergamot, kumkat ve konservecilikte kullanılan yeşil küçük limonlar 08.05’te sayılmıştır.",
 "08.05 Açıklama Notu; 08.14 pozisyon metni."
))
# 8 — E
S.append(q(
 "Aşağıdakilerden hangisi 08.02 pozisyonunda <b>sınıflandırılmaz</b>?",
 ["Kola cevizi", "Arek (betel) cevizi", "Trapa natans türü su kestanesi", "Makadamya cevizi", "*At kestanesi (Aesculus hippocastanum)"],
 T_O,
 "08.02 Açıklama Notu at kestanesini hariç tutarak 23.08’e gönderir. Kola ve arek cevizleri ile Trapa natans türü dikenli meyveler açıklama notunda sayılmıştır; makadamya cevizi de pozisyonun alt kırılımında adıyla geçer.",
 "08.02 pozisyon metni ve Açıklama Notu."
))
# 9 — D
S.append(q(
 "Aşağıdakilerden hangisi 08.13 pozisyonunda <b>yer almaz</b>?",
 ["Kuru kayısı (zerdali dahil)", "Kuru elma dilimleri", "Katkısız demirhindi meyve eti", "*Kuru üzüm", "Fındık, badem ve kuru üzüm karışımı"],
 T_O,
 "08.13 pozisyon metni 08.01–08.06’daki meyveleri hariç tutar; kuru üzüm 08.06’dadır. Kuru kayısı, kuru elma ve demirhindi eti 08.13’tedir. Fındık, badem ve kuru üzüm karışımı ise bu fasıldaki ürünlerin karışımı olarak 08.13’e girer.",
 "08.06 ve 08.13 pozisyon metinleri; 08.13 Açıklama Notu."
))
# 10 — B
S.append(q(
 "Tarife Cetveline göre aşağıdakilerden hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır? (Ürünlerin tamamı taze haldedir.)",
 ["Kayısı", "*Muşmula", "Vişne", "Nektarin", "Çakal eriği"],
 T_F,
 "Kayısı, vişne (kiraz çeşidi), nektarin (şeftali çeşidi) ve çakal eriği 08.09 pozisyon metninde ve açıklama notunda sayılmıştır. Muşmula ise 08.10 Açıklama Notunda diğer meyveler arasında yer alır.",
 "08.09 ve 08.10 Açıklama Notları."
))
# 11 — E
S.append(q(
 "Aşağıdaki taze meyvelerden hangisi Tarife Cetvelinde diğerlerinden farklı bir pozisyonda yer alır?",
 ["Kivi", "Durian", "Trabzon hurması", "Kaktüs inciri (Frenk inciri)", "*Papaya (Carica papaya)"],
 T_F,
 "08.07 pozisyon metni kavunlar ve papayayı kapsar; Açıklama Notu Carica papaya’yı açıkça sayar. Kivi, durian, Trabzon hurması ve kaktüs inciri 08.10’dadır; 08.04 Açıklama Notu da kaktüs incirini 08.10’a gönderir.",
 "08.07, 08.04 ve 08.10 Açıklama Notları."
))
# 12 — A
S.append(q(
 "Tarife Cetveline göre aşağıdakilerden hangisi diğerlerinden farklı bir fasılda sınıflandırılır?",
 ["*Ardıç meyvesi", "Kuşburnu", "Mürver meyvesi", "Üvez", "Hünnap"],
 T_F,
 "08.10 Açıklama Notu ardıç meyvelerini hariç tutarak 09.09’a gönderir; Fasıl 8 Genel Açıklamaları da ardıcı Fasıl 9 ürünleri arasında sayar. Kuşburnu, mürver meyvesi, üvez ve hünnap 08.10’da sayılan meyvelerdir.",
 "08.10 Açıklama Notu; Fasıl 8 Genel Açıklamalar."
))
# 13 — C
S.append(q(
 "Tarife Cetveline göre aşağıdaki eşya çiftlerinden hangisinde her iki eşya <b>aynı</b> pozisyonda sınıflandırılır?",
 ["Taze kayısı – kuru kayısı",
  "Taze çilek – dondurulmuş çilek",
  "*Taze üzüm – kuru üzüm",
  "Portakal – portakal kabuğu",
  "Taze elma – kuru elma"],
 T_F,
 "08.06 üzümleri taze veya kurutulmuş olarak birlikte kapsar. Taze kayısı 08.09 iken kuru kayısı 08.13; taze çilek 08.10 iken dondurulmuşu 08.11; portakal 08.05 iken kabuğu 08.14; taze elma 08.08 iken kuru elma 08.13’tedir.",
 "08.06 pozisyon metni ve Açıklama Notu."
))
# 14 — B
S.append(q(
 "Fasıl 8 notları ve Genel Açıklamalarına göre “soğutulmuş” meyveler ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
 ["Dondurulmuş meyvelerle birlikte 08.11 pozisyonunda sınıflandırılır.",
  "*Tazeleriyle aynı pozisyondadır; kavun, karpuz ve bazı turunçgillerde +10 °C’de tutma da soğutma sayılabilir.",
  "Yalnızca 0 °C’nin altında tutulan meyveler soğutulmuş sayılır.",
  "Geçici olarak korunmuş sayıldıklarından 08.12 pozisyonunda yer alır.",
  "Kavun ve karpuzda soğutma ancak –10 °C’de tutma ile kabul edilir."],
 T_N,
 "Not 2’ye göre soğutulmuş meyveler tazeleriyle aynı pozisyondadır. Genel Açıklamalar soğutmayı dondurmadan genellikle 0 °C civarına düşürme olarak tanımlar ve kavun, karpuz ile bazı turunçgillerde +10 °C’ye düşürüp bu derecede tutmayı da soğutma sayar.",
 "Fasıl 8 Not 2; Fasıl 8 Genel Açıklamalar."
))
# 15 — D
S.append(q(
 "Fasıl 8 Not 3’e göre, kurutulmuş meyve karakterini korumak şartıyla aşağıdaki işlem gruplarından hangisi kurutulmuş meyvenin Fasıl 8’de kalmasına engel <b>değildir</b>?",
 ["Uzun süre konsantre şeker şurubunda bekletme ve ardından havayla kurutma",
  "Kahve yerine kullanılmak üzere kavurma ve ufalama",
  "Toz haline getirme ve bitkisel yağ ilavesi",
  "*Kısmen rehidre etme, kükürtleme ve potasyum sorbat ilavesi",
  "Başka yöntemle pişirme ve bol miktarda glikoz şurubuyla kaplama"],
 T_N,
 "Not 3 kurutulmuş meyvenin kısmen rehidre edilebileceğini, korunması için düşük ısı işlemi, kükürtleme, sorbik asit veya potasyum sorbat ilavesi, görünümü için bitkisel yağ veya az miktarda glikoz şurubu ilavesi görebileceğini belirtir. Ozmotik dehidrasyon 20.08’e, kahve yerine kavurma 21.01’e, toz haline getirme 11.06’ya götürür.",
 "Fasıl 8 Not 3; Fasıl 8 Genel Açıklamalar."
))
# 16 — E
S.append(q(
 "Fasıl 8 Not 4’e göre 08.12 pozisyonu ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
 ["Şeker şurubunda konserve edilmiş ve hemen tüketilebilen meyveleri kapsar.",
  "Yalnızca dondurularak korunan meyve ve sert kabuklu meyveleri kapsar.",
  "Kükürt dioksit gazıyla işlem görmüş meyveler 08.12’den çıkarılarak Fasıl 20’ye gönderilir.",
  "Hemen yenmeye elverişli olsalar bile salamuradaki bütün meyveleri kapsar.",
  "*Geçici koruma için işlem görmüş ve bu haliyle derhal yenilmeye elverişli olmayan meyveleri kapsar."],
 T_N,
 "Not 4’e göre 08.12, taşınma veya depolama sırasında esas olarak geçici koruma sağlamak üzere işlem görmüş (kükürt dioksit gazı, salamura, kükürtlü su veya diğer koruyucu eriyikler) fakat bu halleriyle derhal yenilmeye elverişli olmayan meyve ve sert kabuklu meyvelere uygulanır. Hemen yenmeye elverişlilik bu pozisyonu dışlar.",
 "Fasıl 8 Not 4; 08.12 Açıklama Notu."
))
# 17 — A
S.append(q(
 "Fasıl 8 Genel Açıklamalarında tanımlanan “ozmotik dehidrasyon” ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
 ["*Meyve parçalarının konsantre şeker şurubunda bekletilerek su ve doğal şekerinin şuruptaki şekerle yer değiştirmesidir; bu meyveler 20.08’dedir.",
  "Meyvenin doğrudan güneş altında veya tünelden geçirilerek kurutulmasıdır; bu meyveler 08.13’te sınıflandırılır.",
  "Meyvenin dondurularak kurutulması işlemidir; bu yöntemle kurutulan meyveler 08.11’de sınıflandırılır.",
  "Kurutulmuş meyveye görünümü için az miktarda glikoz şurubu sürülmesidir; bu meyveler Fasıl 8’de kalır.",
  "Meyvenin kükürt dioksit gazıyla geçici olarak korunması işlemidir; bu meyveler 08.12’de sınıflandırılır."],
 T_N,
 "Genel Açıklamalara göre ozmotik dehidrasyon, meyve parçalarının uzun süre konsantre şeker şurubunda bekletilerek bünyedeki su ve doğal şekerin şuruptaki şekerle yer değiştirmesidir; meyve sonra havayla kurutulabilir. Bu meyveler Fasıl 8 dışında, 20.08’dedir. Diğer seçenekler başka işlemleri (güneşte kurutma, dondurarak kurutma, Not 3’teki glikoz şurubu, geçici koruma) tarif eder.",
 "Fasıl 8 Genel Açıklamalar."
))
# 18 — C
S.append(q(
 "Hava almayacak şekilde teneke kutulara konulmuş, başka bir işlem görmemiş kuru eriklerin kutularıyla birlikte sınıflandırılmasıyla ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
 ["Hava geçirmez ambalaj nedeniyle eşya Fasıl 20’de sınıflandırılır.",
  "Kutu ve erik GYK 3(b) uyarınca takım sayılır ve kutunun pozisyonunda sınıflandırılır.",
  "*Kutu, normal ambalaj olarak GYK 5(b) uyarınca kuru eriklerle birlikte 08.13’te sınıflandırılır.",
  "Kutu GYK 5(a) uyarınca ayrı sınıflandırılır; kuru erik 08.09’dadır.",
  "GYK 3(c) uyarınca geçerli pozisyonlardan numara sırasına göre sonuncusunda sınıflandırılır."],
 T_G,
 "Fasıl 8 Genel Açıklamalarına göre hava almayacak şekilde paketlenmiş kuru erik başka bir işlem görmedikçe Fasıl 8’de kalır; kuru erik 08.13’tedir (08.09 yalnız taze). GYK 5(b) uyarınca eşyanın ambalajında normal olarak kullanılan türden ambalaj maddeleri eşya ile birlikte sınıflandırılır. Ambalaj ile içerik takım oluşturmaz.",
 "GYK 5(b); Fasıl 8 Genel Açıklamalar; 08.13 pozisyon metni."
))
# 19 — B
S.append(q(
 "Kuru kayısı, kuru üzüm ve kabuksuz fındıktan oluşan karışımın 08.13 pozisyonunda sınıflandırılması hangi Genel Yorum Kuralına dayanır?",
 ["GYK 3(b), çünkü karışımın esas niteliğini kuru kayısı verir",
  "*GYK 1, çünkü 08.13 pozisyon metni bu fasıldaki kuruyemiş ve kuru meyve karışımlarını açıkça kapsar",
  "GYK 3(c), çünkü 08.13 geçerli pozisyonlardan numara sırasına göre sonuncusudur",
  "GYK 2(b), çünkü karışım olduğundan Fasıl 20’ye gider",
  "GYK 4, çünkü karışım en çok kuru kayısıya benzer"],
 T_G,
 "08.13 pozisyon metni “bu fasıldaki sert kabuklu meyvelerin veya kurutulmuş meyvelerin birbiriyle olan karışımları”nı adıyla kapsar; sınıflandırma pozisyon metniyle çözüldüğü için GYK 1 uygulanır. 08.13’ün numara olarak son pozisyon olması tesadüftür; GYK 3 ancak GYK 1 ile sonuca ulaşılamazsa devreye girer.",
 "GYK 1; 08.13 pozisyon metni ve Açıklama Notu."
))
# 20 — D
S.append(q(
 "Tarife Cetveline göre; taze kayısı ……, dondurulmuş kayısı ……, kurutulmuş kayısı ise …… pozisyonunda sınıflandırılır. Boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?",
 ["08.09 – 08.12 – 08.13", "08.13 – 08.11 – 08.09", "08.10 – 08.11 – 08.13", "*08.09 – 08.11 – 08.13", "08.09 – 08.11 – 08.04"],
 T_B,
 "Taze kayısı 08.09’da, dondurulmuş kayısı 08.11’de, kurutulmuş kayısı 08.13’tedir (08.13 Açıklama Notu kayısıyı kurutulan başlıca meyveler arasında sayar). 08.12 geçici korunmuş meyveler, 08.04 hurma-incir gibi tropikal meyveler içindir.",
 "08.09, 08.11 ve 08.13 pozisyon metinleri ve Açıklama Notları."
))
# 21 — E
S.append(q(
 "Tarife Cetveline göre aşağıdaki eşya–pozisyon eşleştirmelerinden hangisi <b>yanlıştır</b>?",
 ["Kopra – 12.03", "Ceviz boş dış kabuğu – 14.04", "Şekerli portakal kabuğu – 20.06", "Plantain – 08.03", "*Kola cevizi – 08.01"],
 T_B,
 "Kola cevizi 08.02 Açıklama Notunda sayılır ve 08.02’dedir; 08.01 yalnızca Hindistan cevizi, Brezilya cevizi ve kaju cevizini kapsar. Kopra 12.03, ceviz boş dış kabuğu 14.04, şekerli meyve kabuğu 20.06, plantain 08.03’tedir.",
 "08.01, 08.02, 08.03 ve 08.14 Açıklama Notları."
))
# 22 — A
S.append(q(
 "Tarife Cetveline göre aşağıdakilerden hangileri 08.10 pozisyonunda sınıflandırılır?  I. Taze kızılcık  II. Taze liçi  III. Taze ayva  IV. Asimina triloba türünün taze meyvesi (pawpaw)",
 ["*I, II ve IV", "I ve III", "II ve III", "I, III ve IV", "III ve IV"],
 T_C,
 "08.10 Açıklama Notu kızılcık, liçi ve Asimina triloba türünün meyvesini sayar; 08.07 Açıklama Notu da pawpaw’ı 08.10’a gönderir. Ayva ise 08.08 pozisyon metninde elma ve armutla birlikte yer alır.",
 "08.07, 08.08 ve 08.10 Açıklama Notları."
))
# 23 — C
S.append(q(
 "Fasıl 8 Genel Açıklamalarına göre aşağıdaki ifadelerden hangileri <b>doğrudur</b>?  I. Az miktarda şeker ilavesi meyvelerin bu fasılda sınıflandırılmasını etkilemez.  II. Homojenizasyon tek başına bir ürünü Fasıl 20’ye götürür.  III. Meyve unu ve tozu 11.06’dadır.  IV. Kavrulmuş ve genellikle kahve yerine kullanılan kestane 08.02’dedir.",
 ["I, II ve III", "II ve IV", "*I ve III", "III ve IV", "I ve IV"],
 T_C,
 "Genel Açıklamalara göre az miktarda şeker ilavesi sınıflandırmayı etkilemez (I doğru) ve meyve unu, ezmesi ve tozu 11.06’dadır (III doğru). Homojenizasyon tek başına Fasıl 20’ye götürmez (II yanlış); kahve yerine kullanılan kavrulmuş kestane, badem, incir 21.01’dedir (IV yanlış).",
 "Fasıl 8 Genel Açıklamalar."
))
# 24 — B
S.append(q(
 "Varillerde kükürtlü su içinde geçici olarak korunmaya alınmış, bu haliyle hemen yenmeye elverişli olmayan ve reçel ile şekerli meyve imalatında kullanılacak kirazlar ithal edilmektedir. Tarife Cetveline göre bu ürün hangi pozisyonda sınıflandırılır?",
 ["08.09", "*08.12", "08.11", "20.08", "08.13"],
 T_S,
 "Not 4’e göre geçici koruma amacıyla kükürtlü su gibi koruyucu eriyikler içinde işlem görmüş ve bu haliyle derhal yenmeye elverişli olmayan meyveler 08.12’dedir. Açıklama Notu, bu ürünlerin varil gibi kaplarda gıda sanayiine sunulduğunu ve kirazın en yaygın örnek olduğunu belirtir. Taze kiraz 08.09’da olurdu.",
 "Fasıl 8 Not 4; 08.12 Açıklama Notu."
))
# 25 — D
S.append(q(
 "Bitki çayı yapımında kullanılmak üzere süzen torbalara paketlenmiş, yalnızca kurutulmuş elma ve kurutulmuş kuşburnu parçalarından oluşan bir karışım ithal edilmektedir. Tarife Cetveline göre bu ürün hangi pozisyonda sınıflandırılır?",
 ["21.06", "12.11", "08.10", "*08.13", "21.01"],
 T_S,
 "08.13 Açıklama Notuna göre bu fasıldaki kurutulmuş meyvelerin karışımları, bitkisel çay ve içecek imali için paketlenmiş olsalar da 08.13’te kalır. Elma ve kuşburnu taze halde 08.08 ve 08.10’dadır; kurutulmuşları 08.13’e girer. Karışıma başka fasıllardan bitki parçaları veya bitki ekstraktı katılsaydı genellikle 21.06’ya giderdi.",
 "08.13 Açıklama Notu."
))

harf_ata(S, "EBDACCAEDB AEDBCCEADB BEADC")
yaz(8, obj)
