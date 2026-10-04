import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yardim_04_08 import q, yaz, T_E, T_O, T_F, T_N, T_G, T_B, T_C, T_S  # noqa: E402

obj = {
 "tur": "fasil",
 "fasil": 7,
 "baslik": "Yenilen sebzeler ve bazı kök ve yumrular",
 "bolum": "II",
 "oz": {
  "vurgu": "Fasıl 7 iki eksende okunur: önce sebzenin türü (taze veya soğutulmuş halde 07.01–07.09), sonra uygulanan hal (dondurulmuş 07.10, geçici korunmuş 07.11, kurutulmuş 07.12). Kuru kabuksuz baklagiller 07.13’te, nişasta ve inülince zengin kök ve yumrular her halde 07.14’tedir. Fasılda öngörülmeyen bir hazırlık görmüş sebze Fasıl 20’ye gider.",
  "maddeler": [
   "“Sebze” kavramı Not 2 ile genişler: mantar, domalan, zeytin, kebere, kabaklar, patlıcan, tatlı mısır, Capsicum ve Pimenta meyveleri, rezene, maydanoz, tarhun, tere, güvey otu.",
   "Kurutulmuş, ezilmiş veya öğütülmüş Capsicum ve Pimenta meyveleri Fasıl 7 dışıdır → 09.04.",
   "Unlar Fasıl 11’dedir: patates unu ve flokonu 11.05; kuru baklagil ve 07.14 köklerinin unu 11.06.",
   "Ambalaj (hava geçirmez kap, MAP) ve kullanım amacı (gıda, ekim) faslı değiştirmez; ancak yeniden dikilecek fideler 06.02’dedir.",
   "Nane, fesleğen, biberiye, ada çayı gibi şifalı otlar 12.11; yenilebilir deniz yosunu 12.12; yem bitkileri 12.14."
  ]
 },
 "karar_tablosu": {
  "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
  "satirlar": [
   ["1", "Kaba yem veya yem bitkisi mi? (İsveç şalgamı, hayvan pancarı, kök yemler, saman, yonca, fiğ)", "<b>12.14</b> (pancar ve havuç başları <b>23.08</b>)"],
   ["2", "Fasıl 7 dışında özel yeri olan bitki mi? (şifalı ot, yenilebilir deniz yosunu, şeker pancarı, soya, keçiboynuzu, hububat)", "<b>12.11</b> / <b>12.12</b> / <b>12.01</b> / Fasıl <b>10</b>"],
   ["3", "Kurutulmuş, ezilmiş veya öğütülmüş Capsicum veya Pimenta meyvesi mi?", "<b>09.04</b>"],
   ["4", "Un, kaba un, toz, flokon mu? (patates; kuru baklagil; 07.14 kökleri)", "<b>11.05</b> / <b>11.06</b>"],
   ["5", "Fasıl 7’de öngörülmeyen bir işlem görmüş mü? (buhar veya kaynatma dışında pişirme, laktik fermantasyon, soda çözeltisi, diğer bileşenlerle hazırlama)", "Fasıl <b>20</b> / Bölüm IV (hazır çorba <b>21.04</b>, karışık baharat <b>21.03</b>)"],
   ["6", "Manyok, ararot, salep, yer elması, tatlı patates veya benzeri nişastalı-inülinli kök ya da sagu özü mü?", "<b>07.14</b> (taze, dondurulmuş, kurutulmuş, pellet)"],
   ["7", "Kurutulmuş, kabuksuz baklagil mi?", "<b>07.13</b> (tohumluk dahil)"],
   ["8", "Kurutulmuş sebze mi? (toz, dilim, julienne)", "<b>07.12</b>"],
   ["9", "Geçici olarak korunmuş ve bu haliyle hemen yenmeye elverişsiz mi?", "<b>07.11</b>"],
   ["10", "Dondurulmuş mu? (önce buharda veya suda pişirilmiş olabilir)", "<b>07.10</b>"],
   ["11", "Taze veya soğutulmuş mu?", "Türüne göre <b>07.01</b>–<b>07.09</b>"]
  ],
  "dipnot": "* Patates: taze 07.01, dondurulmuş 07.10, kurutulmuş 07.12, unu ve flokonu 11.05; tatlı patates her halde 07.14. Homojenizasyon tek başına Fasıl 20’ye götürmez; hava geçirmez kap veya MAP ambalaj faslı değiştirmez."
 },
 "pozisyon_haritasi": [
  ["07.01", "Patates (taze veya soğutulmuş)", "Tohumluk dahil; tatlı patates hariç", "Sofralık ve tohumluk patates"],
  ["07.02", "Domates (taze veya soğutulmuş)", "Her tür domates", "Taze domates"],
  ["07.03", "Soğan, şalot, sarımsak, pırasa, diğer soğanımsılar", "Soğan setleri ve taze soğan dahil", "Soğan seti, sarımsak, pırasa, frenk soğanı"],
  ["07.04", "Lahana, karnabahar, alabaş, yaprak lahana, benzeri brassikalar", "Kök halindeki lahanalar hariç", "Brokoli, Brüksel lahanası, Çin lahanası"],
  ["07.05", "Marul ve hindiba", "Hindiba bitkisi ve kökü hariç", "Baş marul, kıvırcık yapraklı hindiba"],
  ["07.06", "Havuç, şalgam, kırmızı pancar, kök kerevizi, turp vb. kökler", "Başları kesilmiş olabilir; yem kökleri hariç", "Kırmızı pancar, yaban turpu, yaban havucu"],
  ["07.07", "Hıyar ve kornişon", "Yalnız taze veya soğutulmuş", "Taze kornişon"],
  ["07.08", "Baklagiller (kabuklu veya kabuksuz)", "Taze veya soğutulmuş; soya ve keçiboynuzu hariç", "Taze bezelye, taze fasulye, taze bakla"],
  ["07.09", "Diğer sebzeler", "Kuşkonmaz, patlıcan, yaprak kerevizi, mantar, biber, ıspanak, zeytin, kabak, otlar", "Taze mantar, dolmalık biber, taze maydanoz"],
  ["07.10", "Dondurulmuş sebzeler", "Çiğ veya buharda-suda pişirilmiş; tuz veya şeker olabilir", "Dondurulmuş bezelye, dondurulmuş sebze karışımı"],
  ["07.11", "Geçici olarak konserve edilmiş sebzeler", "Hemen yenmeye elverişsiz; kükürt dioksit, salamura", "Fıçıda salamura zeytin, kükürtlü suda mantar"],
  ["07.12", "Kurutulmuş sebzeler", "Bütün, kesilmiş, dilimlenmiş, toz; başka hazırlık yok", "Soğan tozu, kurutulmuş mantar, julienne"],
  ["07.13", "Kuru baklagiller (kabuksuz)", "Tohumluk dahil; ikiye ayrılmış olabilir", "Kuru nohut, mercimek, kuru fasulye"],
  ["07.14", "Manyok, ararot, salep, yer elması, tatlı patates vb.; sagu özü", "Nişasta veya inülin; dilim veya pellet (bağlayıcı en fazla %3)", "Manyok pelleti, tatlı patates, Çin su kestanesi"]
 ],
 "notlar": [
  ["Bölüm II Not 1", "“Pellet”: doğrudan sıkıştırma veya ağırlığının <b>%3’ünü</b> geçmeyecek oranda bağlayıcı ilavesiyle küçük topaklar halinde bir araya getirilen ürünler (07.14’teki pelletler için önemlidir)."],
  ["Fasıl 7 Not 1", "12.14’te yer alan kaba yemler bu fasla dahil değildir."],
  ["Fasıl 7 Not 2", "07.09, 07.10, 07.11 ve 07.12’deki “sebzeler” kelimesine yenilen mantarlar, domalanlar, zeytinler, kebereler, sakız kabağı, bal kabağı, patlıcanlar, tatlı mısır (Zea mays var. saccharata), Capsicum veya Pimenta cinsinin meyveleri, rezene, maydanoz, frenk maydanozu, tarhun, tere, mercan köşkü otu (Majorana hortensis veya Origanum majorana) dahildir."],
  ["Fasıl 7 Not 3", "07.12, 07.01–07.11’deki bütün sebzelerin kurutulmuş olanlarını kapsar. Hariç: (a) kabuksuz kuru baklagiller (07.13); (b) 11.02–11.04’teki şekillerde tatlı mısır; (c) patates unu, kaba unu, tozu, flokonu, granülü ve pelleti (11.05); (d) 07.13’teki kuru baklagillerin unu, kaba unu ve tozu (11.06)."],
  ["Fasıl 7 Not 4", "Capsicum veya Pimenta cinslerinin kurutulmuş veya ezilmiş ya da öğütülmüş meyveleri bu fasla dahil değildir (09.04)."],
  ["Fasıl 7 Not 5", "07.11, kullanımdan önce taşınma veya depolama sırasında esas olarak geçici koruma sağlamak üzere işlem görmüş (kükürt dioksit gazı, salamura, kükürtlü su veya diğer koruyucu eriyikler), fakat bu halleriyle derhal yenilmeye elverişli olmayan sebzelere uygulanır."],
  ["Genel Açıklamalar", "Sebzeler taze, soğutulmuş, dondurulmuş (pişirilmemiş veya buharda ya da suda kaynatılarak pişirilmiş), geçici olarak konserve edilmiş veya kurutulmuş (suyu alınmış, buharlaştırılmış, dondurularak kurutulmuş) olabilir; bütün, dilimlenmiş, parçalanmış, rendelenmiş, kabuğu soyulmuş olabilir. Kurutulup toz haline getirilmiş sebzeler tat verici olarak kullanılsalar bile 07.12’dedir."],
  ["Genel Açıklamalar", "“Soğutulmuş”: dondurmadan sıcaklığın genellikle <b>0 °C</b> civarına düşürülmesi; patates gibi bazı ürünlerde <b>+10 °C</b>’ye düşürülüp bu sıcaklıkta tutulma da yeterlidir. “Dondurulmuş”: ürünün tamamen donuncaya kadar donma noktasının altında soğutulması."],
  ["Genel Açıklamalar", "Fasıl için öngörülmeyen bir işlemle konserve edilen veya hazırlanan sebzeler Fasıl 20’dedir; ancak tek başına homojenizasyon Fasıl 20’ye götürmez. Hava sızdırmaz kaplara konulmuş (teneke kutuda soğan tozu) veya MAP ile paketlenmiş sebzeler bu fasılda kalır."],
  ["Genel Açıklamalar", "Taze veya kurutulmuş sebzeler yiyecek, ekim veya dikim amaçlı olsalar da bu fasıldadır (patates, soğan, sarımsak, baklagiller); yeniden dikilecek fideler 06.02’dedir. Hariç: hindiba bitkisi ve kökü (06.01 veya 12.12); hububat (Fasıl 10); şeker pancarı ve şeker kamışı (12.12); 07.14 köklerinin unu (11.06); fesleğen, hodan, çörtük otu, tüm nane çeşitleri, biberiye, sedef otu, ada çayı ve kurutulmuş dul avrat otu kökleri (12.11); yenilebilen deniz yosunu ve algler (12.12); İsveç şalgamı, hayvan pancarı, saman, yonca, üçgül, fiğ ve benzeri yemler (12.14); pancar veya havuç başları (23.08)."],
  ["07.10 Açıklama Notu", "Dondurulmadan önce buharda veya kaynar suda pişirilmiş ya da tuz veya şeker ilave edilmiş sebzeler ve dondurulmuş sebze karışımları buradadır. Diğer işlemlerle pişirilmiş sebzeler Fasıl 20’ye, diğer bileşenlerle hazırlanmış sebzeler Bölüm IV’e gider."],
  ["07.11 Açıklama Notu", "Genellikle fıçı veya varillerde, sanayiye hammadde olarak sunulur (soğan, zeytin, kebere, hıyar, kornişon, mantar, domalan, domates). Salamuraya ek olarak soda çözeltisi veya laktik fermantasyon gibi özel işlem görenler Fasıl 20’dedir (zeytin, lahana turşusu, kornişon, yeşil fasulye)."],
  ["07.13 Açıklama Notu", "Tohumluk (kimyasal işlemle yenilemez hale getirilmiş olsa bile) veya başka amaçlı kurutulmuş, kabuğu çıkarılmış baklagiller; enzim faaliyetini durdurmak için orta ısıya tabi tutulabilir, taneleri ikiye ayrılmış olabilir. Hariç: unları (11.06), soya (12.01), bakla dışındaki fiğ, burçak ve acı bakla tohumları (12.09), keçiboynuzu (12.12)."],
  ["07.14 Açıklama Notu", "Taze, soğutulmuş, dondurulmuş veya kurutulmuş, dilimlenmiş veya pellet halinde kök ve yumrular; pellette bağlayıcı ağırlıkça <b>%3’ü</b> geçemez. Çin su kestanesi (Eleocharis dulcis veya tuberosa) dahildir. Hariç: unları (11.06), nişastaları (11.08), tapyoka (19.03), yıldız çiçeği yumruları (06.01), patatesler (07.01 veya 07.12)."]
 ],
 "sinir_komsulari": [
  ["Kurutulmuş veya öğütülmüş kırmızı biber (Capsicum)", "09.04", "Fasıl 7 Not 4"],
  ["Nane, fesleğen, biberiye, ada çayı", "12.11", "Fasıl 7 Genel Açıklamalar"],
  ["Yabani güvey otu (Origanum vulgare)", "12.11", "07.09 hariç tutması; güvey otu (O. majorana) 07.09"],
  ["Soya fasulyesi", "12.01", "07.08 ve 07.13 hariç tutmaları"],
  ["Keçiboynuzu", "12.12", "07.08 ve 07.13 hariç tutmaları"],
  ["Bakla dışındaki fiğ, burçak, acı bakla tohumları", "12.09", "07.13 hariç tutması"],
  ["İsveç şalgamı, hayvan pancarı, yonca, saman", "12.14", "Fasıl 7 Not 1; Genel Açıklamalar"],
  ["Pancar veya havuç başları", "23.08", "Genel Açıklamalar"],
  ["Yenilebilir deniz yosunu ve algler", "12.12", "Genel Açıklamalar"],
  ["Patates unu, flokonu, pelleti", "11.05", "Fasıl 7 Not 3(c)"],
  ["Kuru baklagil unu; manyok unu", "11.06", "Not 3(d); 07.14 hariç tutması"],
  ["Tapyoka; manyok nişastası", "19.03 / 11.08", "07.14 hariç tutması"],
  ["Laktik fermantasyonla hazırlanmış lahana turşusu", "Fasıl 20", "07.11 hariç tutması"],
  ["Kuru sebzeden hazır çorba; karışık baharat", "21.04 / 21.03", "07.12 hariç tutması"],
  ["Yeniden dikilecek sebze fidesi", "06.02", "Genel Açıklamalar"]
 ],
 "tuzaklar": [
  "<b>Biber hale göre ikiye ayrılır.</b> Taze veya soğutulmuş Capsicum ve Pimenta 07.09, dondurulmuşu 07.10; kurutulmuş, ezilmiş veya öğütülmüş olanı 09.04 (Not 4).",
  "<b>Dikim amacı faslı değiştirmez.</b> Tohumluk patates 07.01, soğan seti 07.03, tohumluk kuru baklagil 07.13; ama yeniden dikilecek fide 06.02.",
  "<b>Pişirme yöntemi önemlidir.</b> Buharda veya suda kaynatılıp dondurulan sebze 07.10; başka yöntemlerle pişirilmiş sebze Fasıl 20.",
  "<b>Geçici koruma konserve değildir.</b> Salamurada geçici korunan ve hemen yenmeyen zeytin 07.11; soda çözeltisi veya laktik fermantasyon görmüş zeytin ya da lahana turşusu Fasıl 20.",
  "<b>Kuru baklagil 07.12’ye girmez.</b> Kabuksuz kuru baklagil 07.13; unu 11.06.",
  "<b>Patates ile tatlı patates farklı yollardan gider.</b> Patates taze 07.01, dondurulmuş 07.10, kurutulmuş 07.12, unu 11.05; tatlı patates her halde 07.14.",
  "<b>Tat verici olarak kullanılsa da kurutulmuş sebze 07.12’dir.</b> Soğan tozu, sarımsak tozu, kurutulmuş maydanoz 07.12; karışık baharat ve çeşniler ise 21.03.",
  "<b>Ot mu, sebze mi?</b> Maydanoz, tere, tarhun, kişniş, dere otu, güvey otu (O. majorana) 07.09; nane, fesleğen, biberiye, ada çayı ve yabani güvey otu (O. vulgare) 12.11.",
  "<b>Hindiba ve dul avrat otu bölünür.</b> Taze hindiba 07.05; hindiba bitkisi ve kökü 06.01 veya 12.12. Taze dul avrat otu kökü 07.06, geçici korunmuşu 07.11, kurutulmuşu 12.11.",
  "<b>Ambalaj faslı değiştirmez.</b> Teneke kutuda soğan tozu ve MAP ile paketlenmiş taze sebze Fasıl 7’de kalır."
 ],
 "hafiza": {
  "kanca": "PA–DO–SO–LA–MA–HA–HI–BA–Dİ  |  DON–GEÇ–KUR–BAK–NİŞ",
  "aciklama": "Türler: <b>PA</b>tates 07.01 · <b>DO</b>mates 07.02 · <b>SO</b>ğan 07.03 · <b>LA</b>hana 07.04 · <b>MA</b>rul 07.05 · <b>HA</b>vuç 07.06 · <b>HI</b>yar 07.07 · <b>BA</b>klagil 07.08 · <b>Dİ</b>ğer 07.09. Haller: <b>DON</b>durulmuş 07.10 · <b>GEÇ</b>ici korunmuş 07.11 · <b>KUR</b>utulmuş 07.12 · kuru <b>BAK</b>lagil 07.13 · <b>NİŞ</b>astalı kökler 07.14. Cümle: “Patates, domates, soğan; lahana, marul, havuç; hıyar, bakla, diğerleri — sonra buzluk, fıçı, kurutma rafı, bakliyat çuvalı, nişasta ambarı.”"
 },
 "sinav_odagi": [
  "Fasıl 7 çıkmış sorularda daha çok komşu fasıllarla (9 ve 12) karşılaştırma şeklinde gelmiştir: “hangisi 9. fasılda sınıflandırılmaz” sorusunda doğru cevap, 07.14 pozisyon metninde adı geçen salep olmuştur.",
  "Şifalı otların ayrımı: bitkisel çay yapımında kullanılacak ada çayının 07.12 değil 12.11’de olduğu; seçeneklerde 07.12 çeldirici olarak kullanılmıştır.",
  "Bölüm II kapsamı sorularında “Yenilen sebzeler ve bazı kök ve yumrular” başlığının Bölüm II’de yer aldığının bilinmesi.",
  "Ürünün kullanım şekline (baharat, içecek) değil, pozisyon metni ve notlara bakılması (GYK 1): salep, manyok ve tatlı patates 07.14’te açıkça sayılmıştır."
 ],
 "cikmis_ornekler": [
  {
   "soru": "Aşağıdaki bitkisel ürünlerden hangisi Türk Gümrük Tarife Cetveli’nin 9. faslında <b>sınıflandırılmaz</b>?",
   "secenekler": ["Salep", "Vanilya", "Tarçın", "Defne yaprağı"],
   "cevap": "A",
   "aciklama": "Salep, 07.14 pozisyon metninde manyok, ararot, yer elması ve tatlı patatesle birlikte açıkça sayıldığından Fasıl 7’dedir. Diğer seçenekler baharat olarak Fasıl 9’da kalır."
  },
  {
   "soru": "Bitkisel çay yapımında kullanılacak ada çayı aşağıdaki tarife pozisyonlarının hangisinde sınıflandırılır?",
   "secenekler": ["09.02", "09.10", "12.11", "07.12"],
   "cevap": "C",
   "aciklama": "Fasıl 7 Genel Açıklamaları ada çayı, nane, biberiye gibi bazen yemeklik de kullanılan şifalı otları Fasıl 7 dışında bırakarak 12.11’e gönderir; kurutulmuş olması onu 07.12’ye sokmaz."
  }
 ],
 "ozet": [
  "Taze veya soğutulmuş sebzeler türüne göre 07.01–07.09; sonra hal sırası: dondurulmuş 07.10, geçici korunmuş 07.11, kurutulmuş 07.12.",
  "Kuru kabuksuz baklagil 07.13 (tohumluk dahil); nişastalı-inülinli kökler, salep ve sagu özü her halde 07.14.",
  "Kurutulmuş veya öğütülmüş biber 09.04; şifalı otlar 12.11; deniz yosunu 12.12; yem bitkileri 12.14.",
  "Unlar Fasıl 11’de: patates 11.05; kuru baklagil ve 07.14 kökleri 11.06.",
  "Fasılda öngörülmeyen hazırlık (başka yöntemle pişirme, fermantasyon, soda) Fasıl 20; tek başına homojenizasyon yetmez.",
  "Ambalaj (hava geçirmez kap, MAP) ve kullanım amacı (gıda, ekim) faslı değiştirmez; yeniden dikilecek fide 06.02."
 ],
 "sorular": []
}

S = obj["sorular"]

# 1 — B
S.append(q(
 "Tarife Cetveline göre, buharda pişirildikten sonra dondurulmuş tatlı mısır taneleri hangi tarife pozisyonunda sınıflandırılır?",
 ["07.09", "*07.10", "07.12", "07.11", "07.14"],
 T_E,
 "Not 2’ye göre tatlı mısır (Zea mays var. saccharata) 07.09–07.12 anlamında sebzedir. 07.10 pişirilmemiş veya buharda ya da suda kaynatılarak pişirilmiş dondurulmuş sebzeleri kapsar. Taze tatlı mısır 07.09’da olurdu; buharda pişirme 07.10’u bozmaz.",
 "Fasıl 7 Not 2; 07.10 pozisyon metni ve Açıklama Notu."
))
# 2 — E
S.append(q(
 "Tarife Cetveline göre, kurutulup toz haline getirilmiş, çorbalara tat vermek için kullanılan sarımsak hangi tarife pozisyonunda sınıflandırılır?",
 ["07.03", "09.10", "21.03", "21.04", "*07.12"],
 T_E,
 "07.12 kurutulmuş sebzeleri toz halinde de kapsar; Açıklama Notu çorbalarda veya tat verici olarak kullanılan toz soğan, sarımsak vb.yi sayar. Genel Açıklamalar, tat verme amacıyla kullanılmalarının sonucu değiştirmediğini belirtir. Taze sarımsak 07.03’te; karışık baharat 21.03’te, hazır çorba 21.04’tedir.",
 "07.12 Açıklama Notu; Fasıl 7 Genel Açıklamalar."
))
# 3 — A
S.append(q(
 "Tarife Cetveline göre, kurutulmuş, kabuğu çıkarılmış ve taneleri ikiye ayrılmış kırmızı mercimek hangi tarife pozisyonunda sınıflandırılır?",
 ["*07.13", "07.08", "07.12", "11.06", "12.09"],
 T_E,
 "07.13 kabuksuz kuru baklagilleri, taneleri ikiye ayrılmış veya tane kabukları çıkarılmış olsun olmasın kapsar; mercimek açıklama notunda sayılmıştır. Not 3(a) kuru baklagilleri 07.12’nin dışında tutar. Taze mercimek 07.08’de, mercimek unu 11.06’dadır.",
 "Fasıl 7 Not 3(a); 07.13 pozisyon metni ve Açıklama Notu."
))
# 4 — C
S.append(q(
 "Tarife Cetveline göre, Çin su kestanesi olarak bilinen Eleocharis dulcis türünün taze, yenilebilir yumruları hangi tarife pozisyonunda sınıflandırılır?",
 ["08.02", "07.09", "*07.14", "07.06", "06.01"],
 T_E,
 "07.14 Açıklama Notu Çin su kestanesi olarak bilinen Eleocharis dulcis veya Eleocharis tuberosa yumrularını açıkça bu pozisyona alır. 07.09 ve 08.02 Açıklama Notları bu ürünü kendi kapsamlarından çıkararak 07.14’e gönderir. Tuzak, “kestane” adı nedeniyle 08.02’yi seçmektir.",
 "07.14, 07.09 ve 08.02 Açıklama Notları."
))
# 5 — D
S.append(q(
 "Tarife Cetveline göre, taze yaprak kerevizi hangi tarife pozisyonunda sınıflandırılır?",
 ["07.06", "07.04", "07.05", "*07.09", "12.11"],
 T_E,
 "07.09 pozisyonu yaprak kerevizlerini (kök kerevizi hariç) kapsar. 07.06 kök kerevizini içerir ve Açıklama Notu yaprak kerevizlerini açıkça hariç tutar. Tuzak, “kereviz” kelimesiyle iki ürünü aynı pozisyonda sanmaktır.",
 "07.06 ve 07.09 Açıklama Notları."
))
# 6 — D
S.append(q(
 "Aşağıdakilerden hangisi Tarife Cetvelinin 7. faslında <b>sınıflandırılmaz</b>?",
 ["Taze maydanoz", "Taze tarhun", "Taze tere", "*Taze nane", "Taze dere otu"],
 T_O,
 "Fasıl 7 Genel Açıklamaları tüm nane çeşitlerini, bazen yemeklik olarak kullanılsalar da şifalı otlar arasında sayıp 12.11’e gönderir. Maydanoz, tarhun ve tere Not 2’de sebze olarak sayılmıştır; dere otu da 07.09 Açıklama Notunda yer alır.",
 "Fasıl 7 Not 2; Fasıl 7 Genel Açıklamalar (d); 07.09 Açıklama Notu."
))
# 7 — E
S.append(q(
 "Aşağıdakilerden hangisi 07.12 pozisyonunda <b>sınıflandırılmaz</b>?",
 ["Dondurularak kurutulmuş mantar",
  "Kurutulmuş havuç dilimleri",
  "Kurutulmuş soğan tozu",
  "“Julienne” türü kurutulmuş sebze karışımı",
  "*Kurutulup öğütülmüş kırmızı biber (Capsicum)"],
 T_O,
 "Not 4, Capsicum veya Pimenta cinsinin kurutulmuş, ezilmiş veya öğütülmüş meyvelerini Fasıl 7 dışında bırakarak 09.04’e gönderir. Dondurularak kurutulmuş mantar, kurutulmuş havuç, soğan tozu ve julienne karışımı 07.12 Açıklama Notunda sayılan ürünlerdir.",
 "Fasıl 7 Not 4; 07.12 Açıklama Notu."
))
# 8 — B
S.append(q(
 "Aşağıdakilerden hangisi 07.08 pozisyonunda <b>yer almaz</b>?",
 ["Taze nohut", "*Taze soya fasulyesi", "Taze bakla", "Taze börülce", "Taze guar (Siyam baklası) tohumu"],
 T_O,
 "07.08 Açıklama Notu soya fasulyesini hariç tutarak 12.01’e gönderir. Nohut, bakla, börülce ve guar tohumu taze baklagiller olarak 07.08’de sayılmıştır.",
 "07.08 Açıklama Notu."
))
# 9 — A
S.append(q(
 "Aşağıdakilerden hangisi Fasıl 7 notları ve açıklama notları uyarınca bu fasılda <b>yer almaz</b>?",
 ["*Hayvan yemi olarak kullanılan İsveç şalgamı",
  "Teneke kutuya konulmuş kurutulmuş soğan tozu",
  "Modifiye atmosferde paketlenmiş (MAP) taze marul",
  "Yalnızca homojenize edilmiş taze sebze",
  "Ekim amacıyla ithal edilen kabuksuz kuru fasulye"],
 T_O,
 "Not 1 12.14’teki kaba yemleri fasıl dışında bırakır; Genel Açıklamalar İsveç şalgamını bu yemler arasında sayar. Hava sızdırmaz kap ve MAP ambalaj faslı değiştirmez; tek başına homojenizasyon Fasıl 20’ye götürmez; tohumluk kuru baklagiller 07.13’tedir.",
 "Fasıl 7 Not 1; Fasıl 7 Genel Açıklamalar; 07.13 Açıklama Notu."
))
# 10 — C
S.append(q(
 "Tarife Cetveline göre aşağıdakilerden hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır? (Ürünlerin tamamı taze haldedir.)",
 ["Havuç", "Kırmızı pancar", "*Tatlı patates", "Kök kerevizi", "Yaban turpu"],
 T_F,
 "Havuç, kırmızı pancar, kök kerevizi ve yaban turpu 07.06’daki yenilen köklerdir. Tatlı patates ise nişastaca zengin yumru olarak 07.14 pozisyon metninde adıyla sayılmıştır; 07.01 Açıklama Notu da onu patatesten ayırır.",
 "07.06 Açıklama Notu; 07.14 pozisyon metni; 07.01 Açıklama Notu."
))
# 11 — E
S.append(q(
 "Aşağıdaki taze sebzelerden hangisi Tarife Cetvelinde diğerlerinden farklı bir pozisyonda yer alır?",
 ["Brokoli", "Brüksel lahanası", "Alabaş", "Çin lahanası", "*Şalgam"],
 T_F,
 "Brokoli, Brüksel lahanası, alabaş ve Çin lahanası 07.04’teki başlı veya yapraklı brassikalardır. 07.04 Açıklama Notu kök halindeki lahanaları hariç tutar ve şalgamı 07.06’ya gönderir.",
 "07.04 ve 07.06 Açıklama Notları."
))
# 12 — A
S.append(q(
 "Tarife Cetveline göre aşağıdakilerden hangisi diğerlerinden farklı bir fasılda sınıflandırılır?",
 ["*Yenilebilir deniz yosunu", "Taze Agaricus cinsi mantar", "Taze domalan (Tuber spp.)", "Taze bamya", "Taze enginar"],
 T_F,
 "Fasıl 7 Genel Açıklamaları yenilebilen deniz yosunu ve diğer algleri fasıl dışında bırakır (12.12). Mantar, domalan, bamya ve enginar 07.09’daki sebzelerdir.",
 "Fasıl 7 Genel Açıklamalar (e); 07.09 Açıklama Notu."
))
# 13 — B
S.append(q(
 "Tarife Cetveline göre aşağıdaki eşya çiftlerinden hangisinde her iki eşya <b>aynı</b> pozisyonda sınıflandırılır? (Ürünlerin tamamı taze haldedir.)",
 ["Patates – tatlı patates",
  "*Zeytin – patlıcan",
  "Bezelye – kuru kabuksuz bezelye",
  "Hıyar – kabak",
  "Pırasa – ıspanak"],
 T_F,
 "Not 2 zeytin ve patlıcanı sebze sayar; her ikisi de taze halde 07.09’dadır. Patates 07.01 iken tatlı patates 07.14; taze bezelye 07.08 iken kuru kabuksuz bezelye 07.13; hıyar 07.07 iken kabak 07.09; pırasa 07.03 iken ıspanak 07.09’dadır.",
 "Fasıl 7 Not 2; 07.09 pozisyon metni ve Açıklama Notu."
))
# 14 — D
S.append(q(
 "Fasıl 7 Not 2’ye göre 07.09 ila 07.12 pozisyonlarındaki “sebzeler” kelimesinin kapsamına aşağıdakilerden hangisi <b>girmez</b>?",
 ["Tatlı mısır (Zea mays var. saccharata)", "Rezene", "Kebere", "*Biberiye", "Mercan köşkü otu (Origanum majorana)"],
 T_N,
 "Not 2 sebzeler kelimesine yenilen mantar, domalan, zeytin, kebere, kabaklar, patlıcan, tatlı mısır, Capsicum ve Pimenta meyveleri, rezene, maydanoz, frenk maydanozu, tarhun, tere ve mercan köşkü otunu dahil eder. Biberiye bu listede yoktur; Genel Açıklamalar onu 12.11’e gönderir.",
 "Fasıl 7 Not 2; Fasıl 7 Genel Açıklamalar (d)."
))
# 15 — C
S.append(q(
 "Fasıl 7 Not 3’e göre 07.12 pozisyonu ile ilgili aşağıdakilerden hangisi <b>yanlıştır</b>?",
 ["07.01 ila 07.11’deki sebzelerin kurutulmuş olanlarını kapsar.",
  "Kabuksuz kuru baklagiller 07.12’de değil 07.13’tedir.",
  "*11.02 ila 11.04’te belirtilen şekillerdeki tatlı mısır 07.12’de kalır.",
  "Patates unu, flokonu ve pelletleri 11.05’tedir.",
  "07.13’teki kuru baklagillerin unu ve tozu 11.06’dadır."],
 T_N,
 "Not 3, 07.12’nin 07.01–07.11’deki sebzelerin kurutulmuş olanlarını kapsadığını belirtir ve dört istisna sayar: kuru kabuksuz baklagiller (07.13), 11.02–11.04’teki şekillerde tatlı mısır, patates unu-flokonu-pelleti (11.05) ve kuru baklagil unu (11.06). Dolayısıyla 11.02–11.04 şeklindeki tatlı mısır 07.12’de kalmaz.",
 "Fasıl 7 Not 3."
))
# 16 — A
S.append(q(
 "Fasıl 7 Not 5’e göre bir sebzenin 07.11 pozisyonunda sınıflandırılabilmesi için aşağıdaki özelliklerden hangisini taşıması gerekir?",
 ["*Geçici koruma amacıyla işlem görmüş olması ve bu haliyle derhal yenilmeye elverişli olmaması",
  "Laktik fermantasyona tabi tutulmuş olması ve hemen tüketilebilir durumda bulunması",
  "Sirke ile hazırlanıp hava geçirmez kaplara konulmuş olması",
  "Dondurulmadan önce buharda veya suda kaynatılarak pişirilmiş olması",
  "Soda çözeltisiyle işlem görüp salamura içinde perakende satışa sunulması"],
 T_N,
 "Not 5’e göre 07.11, taşınma veya depolama sırasında esas olarak geçici koruma sağlamak üzere işlem görmüş (kükürt dioksit gazı, salamura, kükürtlü su vb.) fakat bu halleriyle derhal yenilmeye elverişli olmayan sebzelere uygulanır. Laktik fermantasyon veya soda çözeltisi gibi özel işlemler Fasıl 20’ye götürür; buharda pişirilip dondurma 07.10’un konusudur.",
 "Fasıl 7 Not 5; 07.11 Açıklama Notu."
))
# 17 — E
S.append(q(
 "Fasıl 7 Genel Açıklamalarına göre “soğutulmuş” tabiri ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
 ["Ürünün tamamen donuncaya kadar donma noktasının altında soğutulmasıdır.",
  "Yalnızca –10 °C’nin altında tutulan ürünler soğutulmuş sayılır.",
  "Patateste +10 °C, diğer bütün sebzelerde –18 °C esas alınır.",
  "Soğutulmuş sebzeler dondurulmuş sebzelerle birlikte 07.10’da yer alır.",
  "*Genellikle 0 °C civarına dondurmadan düşürmedir; patates gibi bazı ürünlerde +10 °C’de tutma da yeterlidir."],
 T_N,
 "Genel Açıklamalara göre “soğutulmuş”, ürünün sıcaklığını dondurmadan genellikle 0 °C civarına düşürmektir; patates gibi bazı ürünler +10 °C’ye düşürülüp bu sıcaklıkta tutulursa da soğutulmuş sayılabilir. Tamamen donuncaya kadar soğutma “dondurulmuş” tanımıdır. Soğutulmuş sebzeler tazeleriyle birlikte 07.01–07.09’dadır.",
 "Fasıl 7 Genel Açıklamalar."
))
# 18 — B
S.append(q(
 "Dondurulmuş bezelye, havuç ve tatlı mısırdan oluşan karışımın sınıflandırılmasıyla ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
 ["GYK 3(b) uyarınca ağırlıkça en fazla olan sebzenin pozisyonunda sınıflandırılır.",
  "*07.10 dondurulmuş sebze karışımlarını kapsadığından GYK 1 uyarınca 07.10’da sınıflandırılır.",
  "GYK 3(c) uyarınca geçerli pozisyonlardan numara sırasına göre sonuncusunda sınıflandırılır.",
  "Karışım olduğu için GYK 2(b) uyarınca Fasıl 20’de sınıflandırılır.",
  "GYK 4 uyarınca en çok benzediği sebzenin pozisyonunda sınıflandırılır."],
 T_G,
 "07.10 Açıklama Notu dondurulmuş sebze karışımlarının da bu pozisyonda yer aldığını belirtir; bileşenlerin her biri de dondurulmuş sebze olarak 07.10’dadır. Sınıflandırma pozisyon metni ve açıklamalarla çözüldüğünden GYK 1 uygulanır; karışım veya esas nitelik kurallarına (2(b), 3(b), 3(c)) başvurulmaz.",
 "GYK 1; 07.10 Açıklama Notu."
))
# 19 — D
S.append(q(
 "Taze patateslerin 07.01 pozisyonu içinde “tohumluk” olanlar ve diğerleri şeklinde ayrı alt pozisyonlarda sınıflandırılması hangi Genel Yorum Kuralına göre yapılır?",
 ["GYK 1", "GYK 3(a)", "GYK 3(b)", "*GYK 6", "GYK 4"],
 T_G,
 "Ürünün 07.01’de olduğu GYK 1 ile pozisyon metnine göre belirlenir. Aynı pozisyon içindeki alt pozisyonlar arasındaki seçim ise, yalnızca aynı seviyedeki alt pozisyonların karşılaştırılmasıyla ve ilgili alt pozisyon notlarına göre GYK 6 ile yapılır. “Tohumluk” tabirinin açıklaması da alt pozisyon düzeyindedir.",
 "GYK 6 ve Açıklama Notu; 07.01 Açıklama Notu."
))
# 20 — C
S.append(q(
 "Tarife Cetveline göre; taze patates ……, dondurulmuş patates ……, kurutulmuş patates ……, patates flokonu ise …… pozisyonunda sınıflandırılır. Boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?",
 ["07.01 – 07.10 – 07.14 – 11.05",
  "07.01 – 07.11 – 07.12 – 11.06",
  "*07.01 – 07.10 – 07.12 – 11.05",
  "07.14 – 07.10 – 07.12 – 11.05",
  "07.01 – 07.10 – 07.12 – 07.14"],
 T_B,
 "Taze patates 07.01’de, dondurulmuş patates 07.10’da (Açıklama Notu patatesi dondurulan başlıca sebzeler arasında sayar), kurutulmuş patates 07.12’dedir. Not 3(c) patates unu, kaba unu, tozu, flokonu, granülü ve pelletini 11.05’e gönderir. 07.14 Açıklama Notu da patatesleri 07.14’ün dışında tutar.",
 "Fasıl 7 Not 3(c); 07.10, 07.12 ve 07.14 Açıklama Notları."
))
# 21 — E
S.append(q(
 "Tarife Cetveline göre aşağıdaki eşya–pozisyon eşleştirmelerinden hangisi <b>doğrudur</b>?",
 ["Keçiboynuzu – 07.08",
  "Pancar başları – 07.06",
  "Laktik fermantasyonla hazırlanmış lahana turşusu – 07.11",
  "Yabani güvey otu (Origanum vulgare) – 07.09",
  "*Taze kuşkonmaz – 07.09"],
 T_B,
 "Kuşkonmaz 07.09 pozisyonunda adıyla sayılır. Keçiboynuzu 12.12’de; pancar başları 23.08’de; laktik fermantasyon görmüş lahana turşusu Fasıl 20’de; yabani güvey otu (Origanum vulgare) 12.11’dedir.",
 "07.08, 07.09, 07.11 Açıklama Notları; Fasıl 7 Genel Açıklamalar."
))
# 22 — A
S.append(q(
 "Tarife Cetveline göre aşağıdakilerden hangileri 07.14 pozisyonunda sınıflandırılır?  I. Dilimlenmiş ve kurutulmuş manyok  II. Sagu özü  III. Manyok unu  IV. Dondurulmuş tatlı patates",
 ["*I, II ve IV", "I ve III", "II ve III", "I, III ve IV", "III ve IV"],
 T_C,
 "07.14 manyok, tatlı patates ve benzeri kök ve yumruları taze, soğutulmuş, dondurulmuş veya kurutulmuş, dilimlenmiş veya pellet halinde kapsar; sagu özü pozisyon metninde sayılmıştır. 07.14 Açıklama Notu bu ürünlerin unlarını hariç tutarak 11.06’ya gönderir.",
 "07.14 pozisyon metni ve Açıklama Notu."
))
# 23 — D
S.append(q(
 "Tarife Cetveline göre aşağıdaki ifadelerden hangileri <b>doğrudur</b>?  I. Ekim amacıyla ithal edilen soğanlar Fasıl 7’de kalır.  II. Yeniden dikilecek sebze fideleri Fasıl 7’dedir.  III. Tohumluk olarak kullanılacak, kimyasal işlemle yenilemez hale getirilmiş kuru kabuksuz bezelye 07.13’tedir.  IV. Fasıl 7 ürünleri hava geçirmez kaplara konulursa her durumda Fasıl 20’ye geçer.",
 ["I, II ve III", "II ve IV", "III ve IV", "*I ve III", "I ve IV"],
 T_C,
 "Genel Açıklamalara göre taze veya kurutulmuş sebzeler ekim veya dikim amaçlı olsa da bu fasıldadır (I doğru), ancak yeniden dikilecek fideler 06.02’dedir (II yanlış). 07.13 Açıklama Notu kimyasal işlemle yenilemez hale getirilmiş tohumluk baklagilleri de kapsar (III doğru). Hava sızdırmaz kapta olmak tek başına faslı değiştirmez (IV yanlış).",
 "Fasıl 7 Genel Açıklamalar; 07.13 Açıklama Notu."
))
# 24 — C
S.append(q(
 "Fıçılar içinde salamurada geçici olarak korunmaya alınmış, bu haliyle hemen yenmeye elverişli olmayan ve sanayide hammadde olarak kullanılacak zeytinler ithal edilmektedir. Tarife Cetveline göre bu ürün hangi pozisyonda sınıflandırılır?",
 ["07.09", "07.10", "*07.11", "07.12", "08.12"],
 T_S,
 "Not 2 zeytini sebze sayar; Not 5’e göre geçici koruma amacıyla salamuraya konulmuş ve bu haliyle derhal yenmeye elverişli olmayan sebzeler 07.11’dedir. 07.11 Açıklama Notu fıçıdaki sanayi hammaddesi zeytinleri örnek verir. Zeytin meyve faslında değil Fasıl 7’de olduğundan 08.12 de değildir.",
 "Fasıl 7 Not 2 ve Not 5; 07.11 Açıklama Notu; Fasıl 8 Genel Açıklamalar."
))
# 25 — B
S.append(q(
 "Manyok unundan, ağırlıkça %2 oranında melas bağlayıcı ilave edilerek küçük topaklar halinde sıkıştırılmış ve hayvan yemi imalatında kullanılacak ürün ithal edilmektedir. Tarife Cetveline göre bu ürün hangi pozisyonda sınıflandırılır?",
 ["11.06", "*07.14", "11.08", "12.14", "23.08"],
 T_S,
 "07.14 Açıklama Notu, 11.06’daki un, kaba un veya tozlardan yapılmış pelletleri de bu pozisyona alır; pellette bağlayıcı (melas vb.) ağırlıkça %3’ü geçmemelidir, bu da Bölüm II notundaki pellet tanımıyla uyumludur. %2 bağlayıcı bu sınırın içindedir. Pelletlenmemiş manyok unu 11.06’da kalırdı.",
 "Bölüm II Not 1; 07.14 Açıklama Notu."
))

yaz(7, obj)
