import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yardim_04_08 import q, yaz, harf_ata, T_E, T_O, T_F, T_N, T_G, T_B, T_C, T_S  # noqa: E402

obj = {
 "tur": "fasil",
 "fasil": 6,
 "baslik": "Canlı ağaçlar ve diğer bitkiler; yumrular, kökler ve benzerleri; kesme çiçekler ve süs yaprakları",
 "bolum": "II",
 "oz": {
  "vurgu": "Fasıl 6, fidanlıkçı ve çiçekçilerin dikim veya süs amacıyla sunduğu canlı bitkileri ve buket ya da süs için uygun kesme çiçek ve yaprakları kapsar. Önce sorulacak soru şudur: Ürün Fasıl 7’de adı geçen bir sebze (patates, soğan, sarımsak) mi, yoksa sunuluş şekliyle buket veya süse uygun olmayan bir bitki mi? İkisi de değilse yer, toprak altı (06.01), canlı bitki (06.02), çiçek (06.03) veya yaprak (06.04) ayrımıyla bulunur.",
  "maddeler": [
   "Bölüm II’nin ilk faslıdır; Bölüm II notu “pellet” tabirini tanımlar: bağlayıcı ağırlıkça en fazla %3.",
   "Çiçek soğanları, yumrular, rizomlar ve hindiba bitkisi-kökleri 06.01; diğer canlı bitkiler, çelikler, aşı kalemleri ve mantar miselleri 06.02.",
   "Kesme çiçek ve tomurcuk 06.03; çiçeksiz yaprak, dal, ot, yosun ve liken 06.04. Bir buket çiçek içeriyorsa 06.03’tür.",
   "Buket, çelenk ve çiçek sepetlerinde diğer maddelerden aksesuarlar dikkate alınmaz (Not 2); kolajlar ise 97.01’dedir.",
   "Dikimlik olsa bile patates, soğan, şalot ve sarımsak Fasıl 7’dedir (Not 1)."
  ]
 },
 "karar_tablosu": {
  "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
  "satirlar": [
   ["1", "Fasıl 7’de yer alan bir ürün mü? (patates, soğan, şalot, sarımsak, beyaz yer elması; dikim amaçlı olsa bile)", "Fasıl <b>7</b>"],
   ["2", "Zencefil rizomu veya kavrulmamış Cichorium intybus sativum hindiba kökü mü?", "<b>09.10</b> · <b>12.12</b>"],
   ["3", "Sunuluş şekliyle buket veya süse uygun olmayan, parfümeri, eczacılık veya zirai mücadele vb. amaçlı çiçek ya da bitki mi? Örgü işlerinde kullanılan bitki mi?", "<b>12.11</b> · <b>14.01</b>"],
   ["4", "Kolaj veya benzeri dekoratif plaket mi?", "<b>97.01</b>"],
   ["5", "Çiçek soğanı, yumru, yumrulu kök, rizom (dinlenme halinde, sürgün vermiş veya çiçeklenmiş) ya da hindiba bitkisi veya kökü mü?", "<b>06.01</b> (saksıda olsa bile)"],
   ["6", "Canlı ağaç, çalı, fide, canlı kök, çelik, daldırma, aşı kalemi veya mantar miseli mi?", "<b>06.02</b>"],
   ["7", "Kesme çiçek veya tomurcuk ya da bunları içeren buket, çelenk, sepet mi? (çiçekli kesme dal dahil)", "<b>06.03</b>"],
   ["8", "Çiçeksiz yaprak, dal, ot, yosun, liken veya bunlardan buket mi? Yeniden dikime elverişsiz Noel ağacı mı?", "<b>06.04</b>"]
  ],
  "dipnot": "* Kesme çiçekler, yapraklar ve bunlardan yapılan çiçekçi eşyası taze, kurutulmuş, boyanmış, ağartılmış veya emprenye edilmiş olabilir; kurdele, kağıt süs, tel çerçeve gibi aksesuarlar sınıflandırmayı değiştirmez (Fasıl 6 Not 2)."
 },
 "pozisyon_haritasi": [
  ["06.01", "Çiçek soğanları, yumrular, yumrulu kökler, rizomlar; hindiba bitkisi ve kökleri", "Dinlenme halinde, sürgün vermiş veya çiçeklenmiş; saksıda olabilir", "Lale, sümbül, nergis soğanı; yıldız (dahlia) yumrusu; ravent rizomu"],
  ["06.02", "Diğer canlı bitkiler (kökleri dahil), çelikler, daldırmalar; mantar miselleri", "Ağaç, çalı, fide, anaç, aşılı veya aşısız; saksıda olabilir", "Meyve fidanı, gül fidanı, açelya, mantar miseli"],
  ["06.03", "Kesme çiçekler ve çiçek tomurcukları", "Buket veya süs amacına uygun; çiçekli buket ve çelenk dahil", "Taze gül, kurutulmuş karanfil, çiçekli manolya dalı"],
  ["06.04", "Süs yaprakları, dallar, otlar, yosunlar ve likenler (çiçeksiz)", "Çiçek veya tomurcuk içermez; süs için meyve içerebilir", "Kesme çam dalı, kuru süs otu, yeniden dikilemeyen Noel ağacı"]
 ],
 "notlar": [
  ["Bölüm II Not 1", "Bu bölümde “pellet”: doğrudan doğruya sıkıştırılmak suretiyle veya ağırlığının <b>%3’ünü</b> geçmeyecek oranda bir bağlayıcı ilavesiyle küçük topaklar halinde bir araya getirilen ürünler."],
  ["Fasıl 6 Not 1", "06.01’in ikinci kısmı (hindiba bitkisi ve kökleri) saklı kalmak şartıyla bu fasıl, genellikle bahçıvanlar, fidan yetiştiricileri ve çiçekçiler tarafından sadece dikme veya süs amacıyla elde edilen canlı ağaçları ve diğer eşyayı (fideler dahil) kapsar. Fasıl 7’deki patatesler, soğanlar, şalotlar, sarımsaklar veya diğer ürünler bu fasla dahil değildir."],
  ["Fasıl 6 Not 2", "06.03 veya 06.04’teki bir eşyaya yapılan atıf, tamamen veya kısmen bu eşyadan yapılmış buket, çiçek sepeti, çelenk ve benzeri maddelere de yapılmış sayılır; diğer maddelerden yapılmış aksesuarlar dikkate alınmaz. 97.01’deki kolajlar veya benzeri dekoratif plaketler dahil değildir."],
  ["Genel Açıklamalar", "Fasıl; fidanlık bahçıvanları veya çiçekçilerce yetiştirilen cinsten, dikim veya süs amaçlı bütün canlı bitkileri (ağaçlar, çalılar, fideler, tıbbi bitkiler dahil) ve hindiba bitkileri ile köklerini (12.12 kökleri hariç) kapsar. Gıda ve dikim amaçlı çeşitlerinin ayırt edilemediği tohumlar, meyveler ve bazı yumru ve soğanlar (patates, soğan, şalot, sarımsak) kapsam dışıdır."],
  ["Genel Açıklamalar", "Fasla ayrıca kesme çiçekler, çiçek tomurcukları, süs yaprakları, dallar ve bitkinin diğer kısımları (taze, kurutulmuş, boyanmış, ağartılmış, emprenye edilmiş veya süs amacıyla başka şekilde hazırlanmış) ile buket, çelenk, çiçek sepeti ve benzeri çiçekçi eşyası dahildir."],
  ["06.01 Açıklama Notu", "Saksı, kasa vb. içinde olabilir. Süs için kullanılmayan bitkilerin yumru ve rizomlarını da (ravent rizomları, kuşkonmaz grifleri) kapsar. Hariç: Fasıl 7’deki soğan, şalot, sarımsak, patates, beyaz yer elması; zencefil rizomları (09.10); kavrulmamış Cichorium intybus sativum hindiba kökleri (12.12)."],
  ["06.02 Açıklama Notu", "Ağaçlar ve her nevi çalılar (orman, meyve, süs; aşı anaçları dahil), dikim için bitki ve fideler, bitkilerin canlı kökleri, köksüz çelikler, daldırmalar, aşı kalemleri, oburdal ve sürgünler ile toprakla karışık olsun olmasın mantar miselleri. Yalın veya top köklü ya da saksı, tüp, kutu içinde olabilir. Yumrulu kökler (06.01) ve hindiba kökü (06.01 veya 12.12) hariç."],
  ["06.03 Açıklama Notu", "Çiçek veya tomurcuk içeren kesilmiş ağaç dalları, funda veya çalılar (ör. manolya, bazı gül tipleri) kesme çiçek sayılır. Buket vb., çiçekçi eşyasının temel özelliğine sahip olduğu sürece kurdele, kağıt süs gibi aksesuar içerse de buradadır. Bulundukları durumda buket veya süs için uygun olmayan, parfümeri, eczacılık, zirai mücadele vb. amaçlı çiçek, taç yaprak ve tomurcuklar 12.11’dedir."],
  ["06.04 Açıklama Notu", "Yaprak, dal, ot, yosun veya likenden buketler süs amacıyla meyve içerebilir; çiçek veya tomurcuk içerirse 06.03’e geçer. Yeniden dikime elverişli olmayan canlı Noel ağaçları (kökü kesilmiş, kökü kaynar suya daldırılarak öldürülmüş) buradadır. Hariç: parfümeri, eczacılık vb. amaçlı bitkiler (12.11), örgü işlerinde kullanılanlar (14.01), kolajlar (97.01)."]
 ],
 "sinir_komsulari": [
  ["Dikimlik soğan, sarımsak, şalot, patates", "Fasıl 7", "Fasıl 6 Not 1; dikim amacı faslı değiştirmez"],
  ["Beyaz yer elması", "Fasıl 7", "06.01 hariç tutması"],
  ["Zencefil rizomu", "09.10", "06.01 hariç tutması"],
  ["Kavrulmamış hindiba kökü (Cichorium intybus sativum)", "12.12", "06.01 hariç tutması"],
  ["Taze başlı veya kıvırcık hindiba", "07.05", "Sebze; hindiba bitkisi ve kökü 06.01 veya 12.12"],
  ["Parfümeri veya eczacılık için çiçek ve taç yaprağı", "12.11", "Buket veya süs için uygun değil"],
  ["Örgü işlerinde kullanılan bitkiler", "14.01", "06.04 hariç tutması"],
  ["Kurutulmuş çiçek veya yapraktan kolaj, dekoratif plaket", "97.01", "Fasıl 6 Not 2"],
  ["Yeniden dikilmek üzere sebze fidesi", "06.02", "Fasıl 7 Genel Açıklamaları: fideler Fasıl 7 dışı"],
  ["Taze yenilen mantar", "07.09", "Mantar miseli 06.02, yenilen mantar sebze"],
  ["Yenilebilir deniz yosunu ve algler", "12.12", "Fasıl 7 Genel Açıklamaları; süs yosunu ve likeni 06.04 ile karıştırılmamalı"]
 ],
 "tuzaklar": [
  "<b>Dikim amacı Fasıl 7 ürününü Fasıl 6’ya taşımaz.</b> Dikimlik patates, soğan, soğan seti, şalot ve sarımsak Fasıl 7’dedir (Not 1).",
  "<b>Yumrulu kök 06.01, diğer canlı kök 06.02.</b> Yıldız (dahlia) gibi yumrulu kökler 06.01’de; bitkilerin canlı kökleri, köksüz çelikler ve daldırmalar 06.02’dedir.",
  "<b>Çiçeklenmiş soğan da 06.01’dir.</b> 06.01, dinlenme halinde, sürgün vermiş veya çiçeklenmiş soğan ve yumruları saksıda olsa bile kapsar.",
  "<b>Bir çiçek pozisyonu değiştirir.</b> Yaprak ve dallardan oluşan buket çiçek veya tomurcuk içerirse 06.04’ten 06.03’e geçer; çiçekli kesme dal (manolya) kesme çiçektir.",
  "<b>Aksesuar sınıflandırmayı değiştirmez.</b> Kurdele, kağıt süs, tel çerçeve içeren buket ve çelenkler çiçekçi eşyası niteliğini koruyorsa 06.03 veya 06.04’te kalır (Not 2).",
  "<b>Sunuluş şekli belirler.</b> Buket veya süs için uygun olmayan, parfümeri veya eczacılık amaçlı çiçek ve yapraklar 12.11’e gider; örgülük bitkiler 14.01’e.",
  "<b>Noel ağacında dikilebilirlik belirleyicidir.</b> Kökü kesilmiş veya kaynar suyla öldürülmüş, yeniden dikime elverişsiz ağaç 06.04; köklü ve dikime uygun ağaç canlı bitki olarak 06.02.",
  "<b>Hindiba üç yere ayrılır.</b> Hindiba bitkisi ve kökleri 06.01; kavrulmamış Cichorium intybus sativum kökü 12.12; taze yaprak veya baş hindiba sebze olarak 07.05.",
  "<b>Kolaj çiçekçi eşyası değildir.</b> 97.01’deki kolajlar ve dekoratif plaketler, kurutulmuş çiçek veya yapraktan yapılmış olsalar da Fasıl 6’ya girmez."
 ],
 "hafiza": {
  "kanca": "ALT – CANLI – ÇİÇEK – YAPRAK",
  "aciklama": "Bir çiçekçi dükkânını aşağıdan yukarı düşünün: toprak <b>altı</b>ndaki soğan, yumru ve rizomlar 06.01; toprağa dikilecek <b>canlı</b> fidan, çelik ve misel 06.02; vitrindeki kesme <b>çiçek</b>ler 06.03; onları süsleyen <b>yaprak</b>, dal ve yosunlar 06.04. Kural: buket içinde tek bir çiçek bile varsa 06.03."
 },
 "sinav_odagi": [
  "Bu fasıl çıkmış sorularda doğrudan pek sorulmamış; daha çok Bölüm II’nin kapsamı (hangi fasıl başlıklarının “Bitkisel Ürünler” bölümünde yer aldığı) üzerinden gündeme gelmiştir.",
  "Bölüm II’deki fasıl başlıklarının (sebzeler, hububat, lak-sakız-reçine) Bölüm IV’teki gıda müstahzarlarıyla karıştırılması kalıbı.",
  "Bitkilerin kullanım amacına göre ayrılması: parfümeri, eczacılık veya bitki çayı amaçlı bitkilerin 12.11’de toplanması; Fasıl 6’da da buket veya süse uygun olmayan çiçeklerin 12.11’e gitmesi.",
  "“Çelenk” gibi adı çiçekçi eşyasını çağrıştıran ama bitkisel olmayan ürünlerde isme değil malzemeye bakılması; Not 2 yalnızca 06.03 ve 06.04 eşyasından yapılmış çelenkleri kapsar."
 ],
 "cikmis_ornekler": [
  {
   "soru": "Aşağıdakilerden hangisi Tarife Cetveli’nin 2. Bölümünde bulunan “Bitkisel Ürünler” içerisinde <b>yer almaz</b>?",
   "secenekler": ["Yenilen sebzeler ve bazı kök ve yumrular", "Yenilen çeşitli gıda müstahzarları", "Hububat", "Lak; sakız, reçine ve diğer bitkisel özsu ve hülasalar"],
   "cevap": "B",
   "aciklama": "Bölüm II, Fasıl 6–14’ü kapsar: yenilen sebzeler Fasıl 7, hububat Fasıl 10, lak-sakız-reçine Fasıl 13’tür. “Yenilen çeşitli gıda müstahzarları” Fasıl 21’in başlığıdır ve Fasıl 16 ile başlayan Bölüm IV’tedir."
  }
 ],
 "ozet": [
  "Fasıl 6: dikim veya süs amaçlı canlı bitkiler ile buket veya süse uygun kesme çiçek ve yapraklar; Bölüm II’nin ilk faslı (pellet bağlayıcısı en fazla %3).",
  "Soğan, yumru, rizom ve hindiba bitkisi-kökü 06.01; diğer canlı bitkiler, çelikler, misel 06.02.",
  "Çiçek veya tomurcuk varsa 06.03; yoksa yaprak-dal-ot-yosun-liken 06.04; yeniden dikilemeyen Noel ağacı 06.04.",
  "Buket ve çelenkte aksesuar dikkate alınmaz; kolajlar 97.01.",
  "Fasıl 7 ürünleri dikimlik olsa da Fasıl 7; zencefil 09.10; kavrulmamış hindiba kökü 12.12.",
  "Buket veya süse uygun olmayan çiçek ve bitkiler 12.11; örgülük bitkiler 14.01."
 ],
 "sorular": []
}

S = obj["sorular"]

# 1 — D
S.append(q(
 "Tarife Cetveline göre, saksı içinde ve çiçeklenmiş halde satışa sunulan sümbül soğanı hangi tarife pozisyonunda sınıflandırılır?",
 ["06.02", "06.03", "07.03", "*06.01", "06.04"],
 T_E,
 "06.01 çiçek soğanlarını dinlenme halinde, sürgün vermiş veya çiçeklenmiş olarak kapsar; Açıklama Notu saksı veya kasa içinde olmalarının sonucu değiştirmediğini belirtir ve sümbülü örnekler arasında sayar. Çiçek açmış olması onu 06.03’e (kesme çiçek) götürmez; 07.03 yenilen soğanlar içindir.",
 "06.01 pozisyon metni ve Açıklama Notu."
))
# 2 — A
S.append(q(
 "Tarife Cetveline göre, toprakla karıştırılmış halde sunulan mantar miselleri (mantar tohumu) hangi tarife pozisyonunda sınıflandırılır?",
 ["*06.02", "07.09", "07.11", "06.01", "07.12"],
 T_E,
 "06.02 pozisyon metni mantar misellerini açıkça sayar; Açıklama Notu toprak veya bitkisel maddelerle karıştırılmış olsun olmasın misellerden oluşan mantar tohumlarını bu pozisyonda tutar. Yenilen taze mantar 07.09’da, geçici korunmuş mantar 07.11’de, kurutulmuş mantar 07.12’dedir.",
 "06.02 pozisyon metni ve Açıklama Notu."
))
# 3 — E
S.append(q(
 "Tarife Cetveline göre, süs amacıyla kesilmiş, çiçekleri üzerinde bulunan manolya dalları hangi tarife pozisyonunda sınıflandırılır?",
 ["06.04", "06.02", "12.11", "14.01", "*06.03"],
 T_E,
 "06.03 Açıklama Notuna göre kesilmiş ağaç dalları, funda veya çalılar çiçek veya çiçek tomurcuğu (ör. manolya, bazı gül tipleri) içeriyorsa kesme çiçek sayılır. Çiçeksiz dallar 06.04’e girerdi. Tuzak, “dal” kelimesine bakıp 06.04’ü seçmektir.",
 "06.03 Açıklama Notu."
))
# 4 — B
S.append(q(
 "Tarife Cetveline göre, çiçek ve tomurcuk içermeyen, ağartılıp boyanmış, süs amaçlı kuru otlardan oluşan demet hangi tarife pozisyonunda sınıflandırılır?",
 ["06.03", "*06.04", "12.11", "14.01", "06.02"],
 T_E,
 "06.04 buket yapmaya elverişli veya süs amacına uygun, çiçeksiz bitki yaprakları, dalları, otlar, yosunlar ve likenleri taze, kurutulmuş, boyanmış, ağartılmış veya başka şekilde hazırlanmış olarak kapsar. Çiçek içermediği için 06.03 değildir; süs amaçlı olduğu için 12.11 veya 14.01’e de gitmez.",
 "06.04 pozisyon metni ve Açıklama Notu."
))
# 5 — C
S.append(q(
 "Tarife Cetveline göre, dinlenme halindeki ravent rizomları hangi tarife pozisyonunda sınıflandırılır?",
 ["07.09", "06.02", "*06.01", "12.11", "07.14"],
 T_E,
 "06.01 Açıklama Notu, pozisyonun süs için kullanılmayan bitkilerin yumru ve rizomlarını da kapsadığını belirtir ve ravent rizomlarını örnek verir. Ravent 07.09’da sebze olarak geçse de dinlenme halindeki rizomu 06.01’dedir. 07.14 nişasta ve inülince zengin kök ve yumrular içindir.",
 "06.01 Açıklama Notu."
))
# 6 — B
S.append(q(
 "Aşağıdakilerden hangisi Tarife Cetvelinin 6. faslında <b>sınıflandırılmaz</b>?",
 ["Dinlenme halindeki lale soğanı",
  "*Dikim amacıyla ithal edilen soğan setleri",
  "Aşılı gül fidanı",
  "Köksüz asma çeliği",
  "Kurutulmuş ve boyanmış süs yaprakları"],
 T_O,
 "Fasıl 6 Not 1, Fasıl 7’deki soğanları bu fasıldan hariç tutar; 07.03 Açıklama Notu soğan setlerini de sayar ve Fasıl 7 Genel Açıklamaları dikim amacının sonucu değiştirmediğini belirtir. Lale soğanı 06.01, aşılı gül fidanı ve köksüz çelik 06.02, boyanmış süs yaprakları 06.04’tedir.",
 "Fasıl 6 Not 1; 07.03 Açıklama Notu; Fasıl 7 Genel Açıklamalar."
))
# 7 — E
S.append(q(
 "Aşağıdakilerden hangisi 06.01 pozisyonunda <b>yer almaz</b>?",
 ["Yıldız (dahlia) yumrulu kökleri", "Sürgün vermiş nergis soğanı", "Kuşkonmaz grifleri", "Hindiba bitkisi", "*Zencefil rizomu"],
 T_O,
 "06.01 Açıklama Notu zencefil rizomlarını hariç tutarak 09.10’a gönderir. Yıldız yumrulu kökleri, sürgün vermiş nergis soğanı, kuşkonmaz grifleri ve hindiba bitkisi 06.01’dedir.",
 "06.01 pozisyon metni ve Açıklama Notu."
))
# 8 — D
S.append(q(
 "Aşağıdakilerden hangisi 06.03 pozisyonunda <b>sınıflandırılmaz</b>?",
 ["Kurdele ve kağıt süslerle tamamlanmış taze gül buketi",
  "Süs amaçlı, ağartılmış ve boyanmış kuru çiçekler",
  "Çiçek tomurcuklarıyla birleştirilmiş çelenk",
  "*Sunuluş şekliyle buket veya süse uygun olmayan, parfümeri sanayiinde kullanılacak gül taç yaprakları",
  "Cekete takılmak üzere hazırlanmış karanfil"],
 T_O,
 "06.03 Açıklama Notu, bulundukları durumda buket veya süs için uygun olmayan, parfümeri, eczacılık veya benzeri amaçlarla kullanılan çiçek, taç yaprak ve tomurcukları hariç tutar (12.11). Aksesuarlı buket, boyanmış kuru çiçek, tomurcuklu çelenk ve cekete takılan çiçek 06.03’tedir.",
 "06.03 Açıklama Notu; Fasıl 6 Not 2."
))
# 9 — A
S.append(q(
 "Aşağıdakilerden hangisi 06.04 pozisyonunda <b>yer almaz</b>?",
 ["*Örgü işlerinde kullanılan cinsten kurutulmuş otlar",
  "Süs amaçlı kurutulmuş likenler",
  "Süs amaçlı meyveler eklenmiş, çiçek içermeyen yaprak buketi",
  "Boyanmış süs otları",
  "Süs amaçlı, yeşil yapraklı ve çiçeksiz kesme dallar"],
 T_O,
 "06.04 Açıklama Notu, örgü işlerinde kullanılan cinsten bitki ve bitki kısımlarını (otlar dahil) hariç tutar ve 14.01’e gönderir. Süs amaçlı likenler, meyveli ama çiçeksiz yaprak buketi, boyanmış süs otları ve çiçeksiz kesme dallar 06.04’tedir.",
 "06.04 Açıklama Notu."
))
# 10 — C
S.append(q(
 "Tarife Cetveline göre aşağıdakilerden hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır?",
 ["Aşı için anaç", "Köksüz çelik", "*Kuzgun kılıcı soğanı", "Aşılı meyve fidanı", "Saksıda canlı gül bitkisi"],
 T_F,
 "Kuzgun kılıcı (glaieul) 06.01 Açıklama Notunda çiçek soğanları arasında sayılır. Aşı anaçları, köksüz çelikler, meyve fidanları ve saksıdaki canlı bitkiler 06.02’dedir. Tuzak, saksıda olmayı 06.01–06.02 ayrımında ölçüt sanmaktır.",
 "06.01 ve 06.02 Açıklama Notları."
))
# 11 — E
S.append(q(
 "Tarife Cetveline göre aşağıdakilerden hangisi diğerlerinden farklı bir fasılda sınıflandırılır?",
 ["Lale soğanı", "Kardelen soğanı", "Süsen (iris) rizomu", "Buhurumeryem yumrusu", "*Beyaz yer elması yumrusu"],
 T_F,
 "06.01 Açıklama Notu, Fasıl 7’deki bazı soğan, yumru ve rizomları (soğan, şalot, sarımsak, patates, beyaz yer elması) hariç tutar; yer elması 07.14 pozisyon metninde sayılmıştır. Lale, kardelen, süsen ve buhurumeryem süs bitkisi soğan ve yumruları olarak 06.01’dedir.",
 "06.01 Açıklama Notu; Fasıl 6 Not 1; 07.14 pozisyon metni."
))
# 12 — B
S.append(q(
 "Tarife Cetveline göre aşağıdaki eşya çiftlerinden hangisinde her iki eşya <b>aynı</b> pozisyonda sınıflandırılır?",
 ["Taze kesme gül – aşılı gül fidanı",
  "*Çiçeksiz taze çam dalı – süs amaçlı kurutulmuş yosun",
  "Hindiba bitkisi – taze başlı hindiba",
  "Dinlenme halindeki lale soğanı – soğan seti",
  "Çiçekli manolya dalı – çiçeksiz manolya dalı"],
 T_F,
 "Çiçeksiz dal ile süs amaçlı yosun 06.04’te birlikte yer alır. Kesme gül 06.03 iken gül fidanı 06.02; hindiba bitkisi 06.01 iken taze başlı hindiba 07.05; lale soğanı 06.01 iken soğan seti 07.03; çiçekli dal 06.03 iken çiçeksiz dal 06.04’tedir.",
 "06.03 ve 06.04 Açıklama Notları; 07.05 Açıklama Notu."
))
# 13 — D
S.append(q(
 "Aşağıdaki bitkisel ürünlerden hangisi Tarife Cetvelinde diğerlerinden farklı bir fasılda yer alır?",
 ["Kesme karanfil", "Kurutulmuş süs yaprağı", "Mantar miseli", "*Kurutulmuş çiçeklerle yapılmış kolaj (dekoratif plaket)", "Yeniden dikilecek sebze fidesi"],
 T_F,
 "Fasıl 6 Not 2, 97.01’deki kolajları ve benzeri dekoratif plaketleri 06.03 ve 06.04’ün kapsamı dışında bırakır. Kesme karanfil 06.03, kurutulmuş süs yaprağı 06.04, mantar miseli ve dikilecek sebze fidesi 06.02’dedir; yani dördü Fasıl 6’dadır.",
 "Fasıl 6 Not 2; Fasıl 7 Genel Açıklamalar."
))
# 14 — A
S.append(q(
 "Tarife Cetvelinin Bölüm II notuna göre “pellet” tabiri ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
 ["*Doğrudan sıkıştırılarak veya ağırlığının %3’ünü geçmeyen bağlayıcı ilavesiyle küçük topaklar haline getirilen ürünlerdir.",
  "Ağırlığının %5’ini geçmeyecek oranda bağlayıcı içeren ve sıkıştırılmış topaklardır.",
  "Yalnızca bağlayıcı ilavesiyle elde edilir; doğrudan sıkıştırılmış topaklar pellet sayılmaz.",
  "Bağlayıcı oranı ağırlıkça %3’ten az olan ürünler pellet tanımının dışında kalır.",
  "Pellet tanımı Bölüm II’de yalnızca Fasıl 7’deki ürünler için geçerlidir."],
 T_N,
 "Bölüm II notu pelleti, doğrudan doğruya sıkıştırılmak suretiyle veya ağırlığının %3’ünü geçmeyecek oranda bir bağlayıcı ilavesiyle küçük topaklar halinde bir araya getirilen ürünler olarak tanımlar ve bölümün tamamına uygulanır. %3 bir üst sınırdır; daha az bağlayıcı veya hiç bağlayıcı olmaması tanımı bozmaz.",
 "Bölüm II Not 1."
))
# 15 — C
S.append(q(
 "Fasıl 6 Not 1 ve Genel Açıklamalarına göre aşağıdakilerden hangisi <b>doğrudur</b>?",
 ["Dikim amacıyla ithal edilen patates ve sarımsak, Fasıl 7 yerine Fasıl 6’da sınıflandırılır.",
  "Fasıl yalnızca süs amaçlı bitkileri kapsar; tıbbi bitkilerin fideleri kapsam dışıdır.",
  "*Fasıl, dikme veya süs amaçlı canlı ağaç ve bitkileri kapsar; Fasıl 7’deki patates, soğan, şalot ve sarımsak hariçtir.",
  "Hindiba bitkisi ve kökleri her durumda Fasıl 12’de sınıflandırılır.",
  "Fasıl, gıda ve ekim amacıyla kullanılan bütün tohum ve meyveleri de kapsar."],
 T_N,
 "Not 1’e göre fasıl, bahçıvan, fidan yetiştiricisi ve çiçekçilerin dikme veya süs amacıyla elde ettiği canlı ağaç ve bitkileri kapsar; Fasıl 7’deki patates, soğan, şalot ve sarımsak hariçtir. Genel Açıklamalar tıbbi bitkileri kapsama alır, tohum ve meyveleri dışlar. Hindiba bitkisi ve kökleri 06.01’dedir; yalnızca kavrulmamış Cichorium intybus sativum kökleri 12.12’ye gider.",
 "Fasıl 6 Not 1; Fasıl 6 Genel Açıklamalar; 06.01 Açıklama Notu."
))
# 16 — E
S.append(q(
 "06.03 ve 06.04 Açıklama Notlarına göre, yaprak, dal ve otlardan oluşan bir buketin bu iki pozisyondan hangisinde sınıflandırılacağını belirleyen ölçüt aşağıdakilerden hangisidir?",
 ["Kurdele, tel gibi aksesuarların değeri",
  "Süs amaçlı meyve içerip içermemesi",
  "Taze veya kurutulmuş olması",
  "Boyanmış veya ağartılmış olması",
  "*Çiçek veya çiçek tomurcuğu içerip içermemesi"],
 T_N,
 "06.04 Açıklama Notuna göre yaprak, dal ve otlardan buketler süs amaçlı meyve içerebilir; ancak çiçek veya çiçek tomurcuğu içerirlerse 06.03’e geçer. Her iki pozisyon da taze, kurutulmuş, boyanmış veya ağartılmış ürünleri kapsar; aksesuarlar ise Not 2 gereği dikkate alınmaz.",
 "06.03 ve 06.04 Açıklama Notları; Fasıl 6 Not 2."
))
# 17 — B
S.append(q(
 "06.04 Açıklama Notuna göre canlı Noel ağaçlarının 06.04 pozisyonunda sınıflandırılması için aranan koşul aşağıdakilerden hangisidir?",
 ["Saksı içinde sunulması",
  "*Yeniden dikime elverişli olmaması",
  "Süs eşyasıyla donatılmış olması",
  "Belirli bir boyun altında olması",
  "Kurutulmuş veya boyanmış olması"],
 T_N,
 "06.04 Açıklama Notu, yeniden dikime elverişli olmamak koşuluyla canlı Noel ağaçlarını (ör. kökü kesilmiş veya kökü kaynar suya daldırılarak öldürülmüş) bu pozisyona alır. Saksıda olmak tersine canlı bitkilerin (06.02) bir sunuluş şeklidir; boy veya süsleme ölçüt değildir.",
 "06.04 Açıklama Notu; 06.02 Açıklama Notu."
))
# 18 — A
S.append(q(
 "Genel Yorum Kuralı 2(a)’nın (imali bitirilmemiş, tamamlanmamış veya birleştirilmemiş eşya) Fasıl 6 ürünlerine uygulanmasıyla ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
 ["*Kuralın bu kısımları, I ila VI. Bölümlere giren eşyaya normal olarak uygulanmaz.",
  "Kural 2(a), Bölüm II eşyasında diğer kurallardan önce ve her durumda uygulanır.",
  "Kural 2(a) yalnızca Fasıl 6’daki buket ve çelenklere uygulanır.",
  "Kural 2(a), demonte sunulan çiçek sepetlerini her durumda 06.03’e sokar.",
  "Kural 2(a), Bölüm II’de yalnızca alt pozisyon düzeyinde uygulanır."],
 T_G,
 "GYK 2(a) Açıklama Notu, hem tamamlanmamış eşya hem de birleştirilmemiş eşya kısımları için, I ila VI. Bölümlere ait pozisyonların kapsamı açısından kuralın normal olarak bu bölümlere giren eşyaya uygulanmadığını belirtir. Fasıl 6 Bölüm II’dedir. Buket ve çelenkler Fasıl 6 Not 2 ile, yani GYK 1 ile sınıflandırılır.",
 "GYK 2(a) Açıklama Notu (III) ve (IX)."
))
# 19 — D
S.append(q(
 "Kurdele, tel ve kağıt süs gibi başka maddelerden aksesuarlar içeren taze çiçek buketinin, aksesuarlar dikkate alınmadan 06.03 pozisyonunda sınıflandırılması hangi kurala dayanır?",
 ["GYK 3(b), çünkü buketin esas niteliğini çiçekler verir",
  "GYK 3(c), çünkü 06.03 geçerli pozisyonlardan sonuncusudur",
  "GYK 5(b), çünkü aksesuarlar ambalaj maddesi sayılır",
  "*GYK 1, çünkü Fasıl 6 Not 2 aksesuarların dikkate alınmayacağını hükme bağlar",
  "GYK 2(b), çünkü buket çiçek ve başka maddelerin karışımıdır"],
 T_G,
 "Fasıl 6 Not 2, 06.03 veya 06.04 eşyasından yapılmış buket, çelenk ve sepetlerde diğer maddelerden aksesuarların dikkate alınmayacağını açıkça belirtir. Sınıflandırma not hükmüyle çözüldüğünden GYK 1 uygulanır. GYK 3 kuralları, notlarda aksine hüküm bulunmadığında ve ancak GYK 1 ile sonuca ulaşılamazsa devreye girer.",
 "GYK 1; Fasıl 6 Not 2; GYK 3 Açıklama Notu (II)."
))
# 20 — C
S.append(q(
 "Tarife Cetveline göre; dinlenme halindeki lale soğanı ……, aşılı gül fidanı ……, kesilmiş taze gül ise …… pozisyonunda sınıflandırılır. Boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?",
 ["06.02 – 06.01 – 06.03", "06.01 – 06.02 – 06.04", "*06.01 – 06.02 – 06.03", "06.01 – 06.03 – 06.03", "07.03 – 06.02 – 06.03"],
 T_B,
 "Lale soğanı çiçek soğanı olarak 06.01’de, aşılı gül fidanı canlı bitki olarak 06.02’de, kesilmiş taze gül kesme çiçek olarak 06.03’tedir. 06.04 çiçeksiz yapraklar içindir; 07.03 yenilen soğanlar içindir.",
 "06.01, 06.02 ve 06.03 pozisyon metinleri."
))
# 21 — E
S.append(q(
 "Tarife Cetveline göre aşağıdaki eşya–pozisyon eşleştirmelerinden hangisi <b>yanlıştır</b>?",
 ["Zencefil rizomu – 09.10",
  "Kavrulmamış Cichorium intybus sativum hindiba kökü – 12.12",
  "Mantar miseli – 06.02",
  "Çiçeksiz süs yaprağı – 06.04",
  "*Hindiba bitkisi – 07.05"],
 T_B,
 "Hindiba bitkisi ve kökleri 06.01’dedir; 07.05 Açıklama Notu da hindiba bitkisi ve köklerini hariç tutarak 06.01 veya 12.12’ye gönderir. 07.05 yalnızca yaprakları yenen taze hindibayı kapsar. Diğer eşleştirmeler 06.01, 06.02 ve 06.04 Açıklama Notlarıyla uyumludur.",
 "06.01 Açıklama Notu; 07.05 Açıklama Notu."
))
# 22 — B
S.append(q(
 "Tarife Cetveline göre aşağıdakilerden hangileri 06.02 pozisyonunda sınıflandırılır?  I. Orman ağacı fidanları  II. Oburdal ve sürgünler  III. Dinlenme halindeki süsen rizomları  IV. Bitkilerin canlı kökleri",
 ["I ve III", "*I, II ve IV", "II ve III", "III ve IV", "I, II, III ve IV"],
 T_C,
 "06.02 Açıklama Notu orman, meyve ve süs ağaçlarını, köksüz çelik ve daldırmaları, oburdal ve sürgünleri ve bitkilerin canlı köklerini sayar. Rizomlar ise dinlenme halinde olsun olmasın 06.01’dedir.",
 "06.01 ve 06.02 Açıklama Notları."
))
# 23 — A
S.append(q(
 "Tarife Cetveline göre aşağıdaki ifadelerden hangileri <b>doğrudur</b>?  I. Fasıl 6, dikim amaçlı tıbbi bitkileri de canlı bitki olarak kapsar.  II. Kesme çiçekler emprenye edilmiş olsalar bile 06.03’te kalabilir.  III. Kurutulmuş çiçeklerden yapılmış kolajlar 06.03’tedir.  IV. Çiçek soğanları saksı içinde sunulursa 06.02’ye geçer.",
 ["*I ve II", "I ve III", "II ve IV", "I, II ve IV", "III ve IV"],
 T_C,
 "Genel Açıklamalar tıbbi bitkileri fasıl kapsamında sayar (I doğru); 06.03 pozisyon metni taze, kurutulmuş, boyanmış, ağartılmış veya emprenye edilmiş kesme çiçekleri kapsar (II doğru). Not 2 kolajları 97.01’e bırakır (III yanlış); 06.01 saksıdaki soğanları da kapsar (IV yanlış).",
 "Fasıl 6 Not 2; Fasıl 6 Genel Açıklamalar; 06.01 ve 06.03 pozisyon metinleri."
))
# 24 — D
S.append(q(
 "Toprağıyla birlikte saksıda sunulan, çiçek açmış, canlı bir açelya bitkisi hediye amacıyla kurdele ile süslenerek ithal edilmektedir. Tarife Cetveline göre bu eşya hangi pozisyonda sınıflandırılır?",
 ["06.03", "06.01", "06.04", "*06.02", "12.11"],
 T_S,
 "06.02 diğer canlı bitkileri kökleriyle kapsar; Açıklama Notuna göre bu bitkiler saksı, tüp veya kutu içinde sunulabilir ve rododendron ve açelyalar pozisyonun alt kırılımında ayrıca anılır. Çiçek açmış olması onu kesme çiçek (06.03) yapmaz; kesilmemiş canlı bitkidir. Soğan veya yumru olmadığından 06.01 de değildir.",
 "06.02 pozisyon metni ve Açıklama Notu."
))
# 25 — C
S.append(q(
 "Kurutulmuş yapraklar, ağaç dalları ve süs amaçlı meyvelerden oluşan, hiç çiçek veya tomurcuk içermeyen, tel çerçeve üzerine yapılmış ve kurdeleyle süslenmiş bir kapı çelengi ithal edilmektedir. Tarife Cetveline göre bu eşya hangi pozisyonda sınıflandırılır?",
 ["06.03", "97.01", "*06.04", "14.01", "12.11"],
 T_S,
 "06.04 yaprak, dal ve benzerlerinden yapılmış çelenkleri kapsar; Açıklama Notuna göre kurdele, tel çerçeve gibi aksesuarlar ve süs amaçlı meyveler sonucu değiştirmez. Çiçek veya tomurcuk bulunmadığından 06.03’e geçmez; kolaj veya dekoratif plaket olmadığından 97.01 de değildir.",
 "Fasıl 6 Not 2; 06.04 Açıklama Notu."
))

harf_ata(S, "DAEBCBEDAC BDECAAECBD CDAEB")
yaz(6, obj)
