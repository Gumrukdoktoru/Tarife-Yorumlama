"""Fasıl 3 – Balıklar, kabuklu hayvanlar, yumuşakçalar ve suda yaşayan diğer omurgasız hayvanlar → data/fasil_03.json

Temel: ornek_fasil_03.json (bloklar korunup geliştirildi; örnekteki 3 soru korunarak 25’e tamamlandı).
"""
import copy
import json
import os

from yardim_00_03 import KITAP, q, yaz, T_E, T_O, T_F, T_N, T_G, T_B, T_C, T_S

ornek = json.load(open(os.path.join(KITAP, "ornek_fasil_03.json"), encoding="utf-8"))
modul = copy.deepcopy(ornek)

# --- Öz ---
modul["oz"]["maddeler"] = ornek["oz"]["maddeler"] + [
    "Pişirme kural olarak Fasıl 16’ya gönderir; istisnalar: tütsüleme öncesinde veya sırasında pişme, kabuğu içinde buharda veya suda pişmiş kabuklu, kabuğu açmak için ısı şoku görmüş yumuşakça ve pişmiş üründen elde edilen yenilebilir un-pellet."
]

# --- Notlar ---
modul["notlar"] = [
    ["Fasıl 3 Not 1", "Fasıl 3 dışı: 01.06’daki memeliler; bunların etleri (02.08, 02.10); türleri veya halleri nedeniyle insanlarca yenilmeye elverişli olmayan cansız balıklar (karaciğer, nefis, yumurta ve spermleri dahil) ve diğer su hayvanları (Fasıl 5); bunların yenmeyen un, kaba un ve pelletleri (23.01); balık yumurtasından hazırlanan havyar ve havyar benzerleri (16.04)."],
    ["Fasıl 3 Not 2", "“Pellet”: doğrudan sıkıştırma veya <b>az miktarda</b> bağlayıcı ilavesiyle küçük topaklar halinde bir araya getirilen ürünler. Oran verilmemiştir. (Bölüm IV notunda ise bağlayıcı ağırlığın <b>%3</b>’ünü geçemez.)"],
    ["Fasıl 3 Not 3", "03.05 ila 03.08 pozisyonları insanların yemesine elverişli un, kaba un ve pelletleri kapsamaz → 03.09."],
    ["Genel Açıklamalar", "Fasıl; doğrudan tüketim, sanayi (konserve vb.), yumurta elde etme veya akvaryum gibi amaçlar için canlı veya ölü bütün balık ve su omurgasızlarını kapsar. “Soğutulmuş”: dondurmadan sıcaklığın genellikle 0 °C civarına düşürülmesi. “Dondurulmuş”: donma derecesi altında tamamen donuncaya kadar soğutma."],
    ["Genel Açıklamalar", "Yenilebilir balık nefisleri ve spermleri hazırlanmamış veya yalnız Fasıl 3 işlemleriyle hazırlanmışsa buradadır; başka şekilde hazırlananlar ile anında tüketime hazır havyar ve havyar ikameleri 16.04’tedir."],
    ["Genel Açıklamalar", "Kesilmiş, kıyılmış, öğütülmüş ürünler ve fasılın farklı pozisyonlarındaki ürünlerin karışım veya kombinasyonları (ör. 03.02–03.04 balıkları ile 03.06 kabukluları) Fasıl 3’te kalır. Hava geçirmez kap (konserve kutusunda tütsülenmiş somon) ve Modifiye Atmosferde Paketleme (MAP) faslı değiştirmez."],
    ["Genel Açıklamalar", "Pişirilmiş veya başka şekilde hazırlanmış ürünler Fasıl 16’dadır (yalnızca hamur veya ekmek kırıntısıyla kaplanmış fileto dahil). İstisnalar: tütsüleme öncesinde veya sırasında pişen tütsülenmiş ürünler (03.05–03.08), kabuğu içinde buharda veya suda pişirilmiş kabuklular (03.06), taşıma veya dondurmadan önce kabuğu açmak ya da dengede tutmak için ısı şokuna maruz kalan yumuşakçalar (03.07), pişmiş üründen elde edilen yenilebilir un ve pelletler (03.09)."],
    ["03.02 Açıklama Notu", "Bütün, başsız, bağırsakları çıkarılmış veya kılçıklı parçalar halinde taze veya soğutulmuş balıklar; fileto ve diğer balık etleri hariç (03.04). Nakliye için tuz veya buzla paketlenmiş, tuzlu su püskürtülmüş, şekerle hafifçe işlem görmüş veya birkaç defne yaprağıyla paketlenmiş balıklar ile gövdeden ayrılmış yenilebilir sakatat (deri, kuyruk, yüzme kesesi, baş, mide, yüzgeç, dil, karaciğer, yumurta, nefis, sperm) dahildir. 03.03 için aynı hükümler geçerlidir."],
    ["03.04 Açıklama Notu", "Fileto: balığın sağ veya sol yanını oluşturan, omurgaya paralel kesilmiş et şeridi; kafa, sindirim sistemi, yüzgeçler ve kemikler çıkarılmış, iki yan parça (sırt veya karından) birleştirilmemiş. Derinin bırakılması, tamamen çıkarılmamış küçük kemikler ve parçalara kesme sınıflandırmayı etkilemez. Diğer balık etleri: kılçıkları çıkarılmış etler (kıyılmış olsun olmasın). Pişirilmiş veya yalnız hamur ya da ekmek kırıntısıyla kaplanmış filetolar 16.04’tedir."],
    ["03.05 Açıklama Notu", "Kurutulmuş, tuzlanmış veya salamura edilmiş ya da tütsülenmiş balıklar ve yenilebilir sakatat (bütün, başsız, parça, fileto veya kıyılmış). Tuz ilave sodyum nitrit veya nitrat içerebilir; az miktarda şeker kullanılabilir. Bu işlemlerden iki veya daha fazlasını görenler de buradadır. Hariç: yenmeyen sakatat ve döküntüler (05.11); pişmiş veya yağ, sirke, zeytinyağlı salamurada muhafaza edilen balık, havyar (16.04); balık çorbası (21.04)."],
    ["03.06–03.08 Açıklama Notları", "Kabuklu (ıstakoz, kerevit, yengeç, karides), yumuşakça (istiridye, tarak, midye, mürekkep balığı, kalamar, ahtapot, salyangoz, deniz kulağı) ve diğer su omurgasızları (deniz kestanesi, deniz hıyarı, deniz anası) canlı, taze, soğutulmuş, dondurulmuş, kurutulmuş, tuzlanmış, salamura veya tütsülenmiş halde; başka işlem görmemiş parçaları dahil (ıstakoz kuyruğu, yengeç kıskacı, deniz kestanesi yumurtalığı). Yenilebilir istiridye yumurtası (yetiştiricilik için küçük istiridyeler) 03.07’dedir. Kaynatılmış veya sirkede muhafaza edilenler 16.05’tedir."],
    ["03.09 Açıklama Notu", "Balık, kabuklu, yumuşakça ve diğer su omurgasızlarından (pişirilmiş olsun olmasın) elde edilen insan tüketimine uygun un, kaba un ve pelletler; yağı alınmış (ör. solvent özütleme) veya ısıl işlem görmüş yenilebilir balık unu dahil. Yenmeyenler 23.01’dedir."],
    ["Fasıl 16 Not 2", "Müstahzarda balık, kabuklu, yumuşakça vb. ağırlıkça <b>%20’den fazla</b> ise Fasıl 16. <b>İstisna:</b> 19.02’deki doldurulmuş ürünler (ör. karidesli mantı) ve 21.03, 21.04."]
]

# --- Sınır komşuları ---
modul["sinir_komsulari"] = [
    ["Canlı balina, yunus, fok", "01.06", "Deniz memelisi (Fasıl 3 Not 1)"],
    ["Balina, yunus, fok eti; kurbağa bacağı", "02.08 / 02.10", "01.06 hayvanlarının eti"],
    ["Kaplumbağa yumurtası; yenilebilir cansız böcekler", "04.10", "Başka yerde yer almayan yenilebilir hayvansal ürün"],
    ["Deniz kabuğu, mürekkep balığı kemiği, mercan", "05.08", "Kabuk ve mercan pozisyonu"],
    ["Yenmeyen ölü balık, balık döküntüsü, yem amaçlı tuzlu morina nefisi, kuluçkalık döllenmiş balık yumurtası", "05.11", "İnsanların yemesine elverişsiz"],
    ["Eczacılıkta kullanılan, yenmeyen balık karaciğeri", "05.10", "05.11 Açıklama Notu hariç tutması"],
    ["Balık yağı", "15.04", "Balık ve deniz memelisi yağları"],
    ["Balık hülasası ve suyu", "16.03", "Hülasa ve sular"],
    ["Pişmiş, kaplanmış, yağda veya sirkede balık; balık sosisi ve ezmesi; havyar", "16.04", "Fasıl 3 dışı hazırlık"],
    ["Kabuğu çıkarılıp kaynatılmış karides; sirkede midye; kaynatılmış ahtapot", "16.05", "Fasıl 3 dışı hazırlık"],
    ["Karidesli veya balıklı doldurulmuş makarna", "19.02", "Doldurulmuş makarna; Fasıl 16 Not 2 istisnası"],
    ["Balık çorbası", "21.04", "03.05 hariç tutması"],
    ["Yenmeyen balık unu (yem)", "23.01", "Fasıl 3 Not 1"],
    ["Canlı deniz kaplumbağası", "01.06", "Sürüngendir; su omurgasızı değildir"]
]

# --- Tuzaklar ---
modul["tuzaklar"] = [
    "<b>Tütsülenirken pişen balık ≠ pişmiş balık.</b> Tütsüleme öncesinde veya sırasında pişen balık 03.05’te kalır. Hamur veya ekmek kırıntısıyla kaplanan fileto ise pişmemiş olsa bile 16.04’e gider.",
    "<b>Kabuk içinde pişirme ≠ kabuğu çıkarıp kaynatma.</b> Kabuğuyla buharda veya suda pişirilen kabuklu 03.06’da; kabuğu çıkarılıp kaynatılan 16.05’te.",
    "<b>Isı şoku pişirme değildir.</b> Kabuğu açmak veya yumuşakçayı dengede tutmak için uygulanan haşlama 03.07’yi bozmaz; kaynayan suda pişirme ise 16.05’e gönderir.",
    "<b>Balina, yunus ve fok memelidir.</b> Canlı 01.06, eti 02.08 veya 02.10.",
    "<b>Balık yumurtası dört yola ayrılır.</b> Yenilebilir ve yalnız Fasıl 3 işlemi görmüşse balığın haline göre 03.02 / 03.03 / 03.05; havyar 16.04; yem amaçlı veya kuluçkalık 05.11. Fasıl 4’te (kuş yumurtaları) yer almaz.",
    "<b>Fileto sınırı.</b> Deri ve küçük kılçık kalması 03.04’ü bozmaz; iki yan parçanın sırttan veya karından birleşik kalması fileto niteliğini bozar. Tuzlanan fileto 03.05’e geçer.",
    "<b>Ambalaj faslı değiştirmez, işlem değiştirir.</b> Hava geçirmez kutudaki tütsülenmiş somon ve MAP ambalajlı taze balık Fasıl 3’tedir.",
    "<b>Pişmişlik 03.09’u bozmaz.</b> Pişmiş balıktan elde edilen yenilebilir un 03.09’da kalır.",
    "<b>Mürekkep balığı balık değildir.</b> Yumuşakçadır → 03.07. Salyangoz ve deniz kulağı da yumuşakçadır; deniz kestanesi ve deniz hıyarı ise 03.08’dir."
]

S = []
# 1 (örnek)
S.append(ornek["sorular"][0])
# 2 (örnek)
S.append(ornek["sorular"][1])
# 3 (örnek)
S.append(ornek["sorular"][2])
# 4
S.append(q("Tarife Cetveline göre blok şeklinde dondurulmuş morina balığı filetoları hangi pozisyonda sınıflandırılır?",
           ["03.02", "03.03", "*03.04", "03.05", "16.04"], T_E,
           "03.04 balık filetolarını ve diğer balık etlerini taze, soğutulmuş veya dondurulmuş (özellikle blok şeklinde dondurulmuş) olarak kapsar. 03.02 ve 03.03 pozisyon metinleri 03.04’teki filetoları açıkça hariç tutar. 03.05 kurutma, tuzlama, salamura veya tütsüleme; 16.04 pişirme veya kaplama gerektirir.",
           "03.04 pozisyon metni ve Açıklama Notu; 03.03 pozisyon metni."))
# 5
S.append(q("Aşağıdaki canlı su hayvanlarından hangisi diğerlerinden <b>farklı</b> bir pozisyonda sınıflandırılır?",
           ["*Canlı ahtapot", "Canlı ıstakoz", "Canlı yengeç", "Canlı kerevit", "Canlı karides"], T_F,
           "Istakoz, yengeç, kerevit ve karides 03.06 açıklama notunda başlıca kabuklu hayvanlar olarak sayılır ve canlı halleri de 03.06’dadır. Ahtapot ise yumuşakçadır; 03.07’de sınıflandırılır. Tuzak, bütün deniz canlılarını “kabuklu” sanmaktır.",
           "03.06 ve 03.07 pozisyon metinleri ve Açıklama Notları."))
# 6
S.append(q("Aşağıdakilerden hangisi 03.07 pozisyonunda <b>sınıflandırılmaz</b>?",
           ["Canlı istiridye", "Dondurulmuş ahtapot", "Kurutulmuş kalamar",
            "İnsan gıdası olarak kullanılmaya elverişli, yetiştiricilik amaçlı küçük istiridyeler (istiridye yumurtası)",
            "*Sirkede muhafaza edilmiş midye"], T_O,
           "03.07 Açıklama Notu, pozisyonda yer almayan işlemlerle hazırlanmış veya muhafaza edilmiş yumuşakçaları (ör. kaynayan suda pişirilmiş veya sirkede muhafaza edilenler) hariç tutar; bunlar 16.05’tedir. Canlı istiridye, dondurulmuş ahtapot, kurutulmuş kalamar ve yenilebilir istiridye yumurtası 03.07’dedir.",
           "03.07 pozisyon metni ve Açıklama Notu."))
# 7
S.append(q("Tarife Cetveline göre insan tüketimine uygun, solvent özütleme yöntemiyle yağı alınmış ve ısıl işlem görmüş balık unu hangi pozisyonda sınıflandırılır?",
           ["03.05", "*03.09", "05.11", "16.04", "23.01"], T_E,
           "03.09 Açıklama Notuna göre insan tüketimine uygun, yağı alınmış (ör. solvent özütleme yöntemiyle) veya ısıl işleme tabi tutulmuş balık unu burada sınıflandırılır; ısıl işlem ve pişirme 03.09’u bozmaz. Fasıl 3 Not 3 yenilebilir unları 03.05–03.08 dışında bırakır. Yenmeyen balık unu 23.01’e gider (tuzak).",
           "Fasıl 3 Not 3; 03.09 Açıklama Notu."))
# 8
S.append(q("03.04 açıklama notuna göre “balık filetosu” ile ilgili aşağıdakilerden hangisi <b>yanlıştır</b>?",
           ["Balığın sağ veya sol yanını oluşturan, omurga kemiğine paralel kesilmiş et şerididir.",
            "Kafa, sindirim sistemi, yüzgeçler ve kemikler çıkarılmıştır.",
            "Filetoyu tutmak için derinin ayrılmamış olması sınıflandırmayı etkilemez.",
            "*İki yan parçanın sırttan veya karından birleşik kalması fileto niteliğini etkilemez.",
            "Parçalar halinde kesilmiş filetolar da fileto olarak sınıflandırılır."], T_N,
           "Açıklama notuna göre filetoda iki yan parça birleştirilmemiştir (ör. sırt veya karınla); birleşik kalan yan parçalar fileto tanımına uymaz. Omurgaya paralel kesim, kafa-sindirim sistemi-yüzgeç-kemiklerin çıkarılması, derinin bırakılabilmesi ve parçalara kesilmiş filetoların fileto sayılması notta açıkça yer alır.",
           "03.04 Açıklama Notu."))
# 9
S.append(q("Aşağıdakilerden hangisi diğerlerinden farklı bir <b>fasılda</b> yer alır?",
           ["Kabuğu içinde suda kaynatılmış, dondurulmuş yengeç",
            "Tütsülenme sırasında pişmiş tütsülenmiş midye",
            "*Kaynayan suda pişirilmiş ahtapot",
            "Kabuğunu açmak için ısı şokuna tabi tutulmuş istiridye",
            "Pişirilmiş karidesten elde edilmiş yenilebilir karides unu"], T_F,
           "Kaynayan suda pişirilmiş yumuşakçalar Fasıl 3’te belirtilmeyen bir işlem gördüğünden 16.05’te, yani Fasıl 16’dadır. Kabuğu içinde suda kaynatılmış kabuklu (03.06), tütsüleme sırasında pişen yumuşakça (03.07), ısı şoku görmüş yumuşakça (03.07) ve pişmiş üründen yenilebilir un (03.09) Genel Açıklamalardaki istisnalar gereği Fasıl 3’te kalır.",
           "Fasıl 3 Genel Açıklamalar; 03.06, 03.07 ve 03.09 Açıklama Notları."))
# 10
S.append(q("Aşağıdakilerden hangisi 03.05 pozisyonunda <b>yer almaz</b>?",
           ["Tuzlanmış ringa", "*Zeytinyağında muhafaza edilmiş sardalya", "Kurutulmuş morina", "Tütsülenmiş somon filetosu", "Tuzlanmış, yenilebilir balık başları"], T_O,
           "03.05 Açıklama Notu, yağ, sirke veya zeytinyağlı salamurada muhafaza edilen balıkları diğer şekilde hazırlanmış balık sayar ve 16.04’e gönderir. Tuzlanmış ringa, kurutulmuş morina, tütsülenmiş fileto ve tuzlanmış yenilebilir balık başları (sakatat) 03.05’tedir.",
           "03.05 Açıklama Notu, hariç tutmalar."))
# 11
S.append(q("Tarife Cetveline göre insan tüketimine uygun, kurutulmuş deniz hıyarı hangi pozisyonda sınıflandırılır?",
           ["03.05", "03.06", "03.07", "*03.08", "16.05"], T_E,
           "Deniz hıyarı kabuklu hayvan ve yumuşakça dışındaki su omurgasızıdır; 03.08 bu hayvanları canlı, taze, soğutulmuş, dondurulmuş, kurutulmuş, tuzlanmış veya salamura edilmiş olarak kapsar ve açıklama notunda deniz hıyarını sayar. 03.05 yalnız balıklar içindir; kurutma Fasıl 3 işlemi olduğundan 16.05’e gidilmez.",
           "03.08 pozisyon metni ve Açıklama Notu."))
# 12
S.append(q("Aynı karton kutuda perakende satışa sunulan; bir kutu karides konservesi, bir kutu karaciğer ezmesi, bir kutu peynir ve bir kutu dilimlenmiş domuz pastırmasının sınıflandırılmasıyla ilgili aşağıdakilerden hangisi doğrudur?",
           ["GYK 3(b) uyarınca esas niteliği veren karides konservesine göre 16.05’te sınıflandırılır.",
            "GYK 3(c) uyarınca numara sırasına göre sonuncu pozisyonda sınıflandırılır.",
            "*Takım oluşturmadığından her ürün kendi pozisyonunda ayrı ayrı sınıflandırılır.",
            "GYK 5(b) uyarınca karton kutuyla birlikte tek bir pozisyonda sınıflandırılır.",
            "GYK 2(b) uyarınca karışım sayılarak 16.04’te sınıflandırılır."], T_G,
           "GYK 3(b) açıklama notu bu bileşimi açıkça takım oluşturmayan ürünlere örnek verir: ürünler belirli bir ihtiyaç veya işlev için bir araya getirilmemiştir; her biri tek başına uygun pozisyonda (karides konservesi 16.05, karaciğer ezmesi ve pastırma 16.02, peynir 04.06) sınıflandırılır. Esas nitelik ya da numara sırası ancak bir takım veya bileşik eşya varsa gündeme gelir.",
           "GYK 3(b) Açıklama Notu (X)."))
# 13
S.append(q("Aşağıdaki balık yumurtalarından hangisi diğerlerinden farklı bir <b>fasılda</b> sınıflandırılır?",
           ["Taze, yenilebilir mersin balığı yumurtası", "Dondurulmuş, yenilebilir alabalık yumurtası", "Tütsülenmiş, yenilebilir morina yumurtası",
            "Soğutulmuş, yenilebilir somon nefisi", "*Kuluçkada kullanılmak üzere döllenmiş balık yumurtaları"], T_F,
           "Kuluçkada kullanılan döllenmiş yumurtalar yenmeyen balık yumurtası olarak 05.11’de (Fasıl 5) yer alır. Yenilebilir yumurta ve nefisler balığın haline göre taze veya soğutulmuşsa 03.02, dondurulmuşsa 03.03, tütsülenmişse 03.05’te, yani Fasıl 3’tedir. Mersin balığı yumurtası ancak havyar olarak hazırlanırsa 16.04’e gider.",
           "Fasıl 3 Not 1 ve Genel Açıklamalar; 03.02 ve 03.05 Açıklama Notları; 05.11 Açıklama Notu."))
# 14
S.append(q("03.05 açıklama notuna göre tuzlanmış veya salamura edilmiş balıklarla ilgili aşağıdakilerden hangisi doğrudur?",
           ["*Tuzlamada kullanılan tuzlar ilave sodyum nitrit veya sodyum nitrat içerebilir.",
            "Tuzlamada az miktarda şeker kullanılması balığı 16.04’e gönderir.",
            "Hem tuzlanıp hem tütsülenen balıklar 16.04’te sınıflandırılır.",
            "Fileto halindeki tuzlanmış balıklar 03.04’te kalır.",
            "Tuzlanmış yenilebilir balık sakatatı 05.11’de sınıflandırılır."], T_N,
           "Açıklama notuna göre tuzlanmış veya salamura edilmiş balıkların hazırlanmasında kullanılan tuzlar ilave sodyum nitrit veya nitrat içerebilir. Az miktarda şeker sınıflandırmayı etkilemez; iki veya daha fazla işlem gören balıklar da 03.05’tedir. Fileto ve yenilebilir sakatat tuzlanınca 03.05’e girer; yalnız yenmeyen sakatat 05.11’dedir.",
           "03.05 Açıklama Notu."))
# 15
S.append(q("Aşağıdaki ürün – pozisyon eşleştirmelerinden hangisi <b>yanlıştır</b>?",
           ["Canlı süs balığı – 03.01", "Dondurulmuş kalamar – 03.07", "Tuzlanmış ringa – 03.05",
            "*Dondurulmuş deniz kestanesi – 03.06", "İnsan tüketimine uygun karides pelleti – 03.09"], T_B,
           "Deniz kestanesi kabuklu hayvan değil, diğer su omurgasızıdır; 03.06 Açıklama Notu 03.08’deki deniz kestanesini açıkça hariç tutar. Canlı süs balığı 03.01, kalamar (yumuşakça) 03.07, tuzlanmış ringa 03.05, yenilebilir karides pelleti 03.09’dadır.",
           "03.06 Açıklama Notu, hariç tutmalar; 03.08 Açıklama Notu."))
# 16
S.append(q("Aşağıdakilerden hangisi 03.04 pozisyonunda <b>sınıflandırılmaz</b>?",
           ["Birkaç defne yaprağıyla paketlenmiş taze balık filetosu", "Hafifçe şekerle işlem görmüş dondurulmuş fileto",
            "Nakliye için buzla paketlenmiş soğutulmuş fileto", "Kıyılmış ve dondurulmuş balık eti",
            "*Yalnızca ekmek kırıntısıyla kaplanmış, pişirilmemiş dondurulmuş fileto"], T_O,
           "Pişirilmiş filetolar ile yalnızca hamur veya ufalanmış ekmekle kaplanmış filetolar (dondurulmuş olsun olmasın) 16.04’tedir; kaplama, pişirme olmasa da Fasıl 3 dışı bir hazırlıktır. Defne yaprağıyla paketleme, hafif şeker, nakliye için buz ve kıyma 03.04 Açıklama Notunda pozisyonda kalan haller olarak sayılmıştır.",
           "03.04 Açıklama Notu; Fasıl 3 Genel Açıklamalar."))
# 17
S.append(q("Tarife Cetveline göre gövdeden ayrılmış, insan tüketimine uygun taze köpek balığı yüzgeçleri hangi pozisyonda sınıflandırılır?",
           ["*03.02", "03.04", "03.05", "05.11", "16.04"], T_E,
           "03.02 Açıklama Notuna göre taze veya soğutulmuş, gövdenin geri kalanından ayrılmış yenilebilir balık sakatatı (deri, kuyruk, yüzme kesesi, baş, yüzgeç vb.) bu pozisyonda sınıflandırılır. 03.04 fileto ve balık etleri, 03.05 kurutulmuş veya tuzlanmış ürünler içindir; yenilebilir olduğundan 05.11 uygulanmaz.",
           "03.02 Açıklama Notu."))
# 18
S.append(q("Aşağıdakilerden hangileri Fasıl 3 notu gereğince bu fasla dahil <b>değildir</b>?  I. Canlı yunus  II. Balık yumurtasından hazırlanan havyar  III. İnsanların yemesine elverişli karides unu  IV. İnsanların yemesine elverişli olmayan balık pelleti",
           ["I ve II", "II ve III", "*I, II ve IV", "I, III ve IV", "II, III ve IV"], T_C,
           "Fasıl 3 Not 1; 01.06’daki memelileri (yunus), havyarı (16.04) ve yenmeyen un, kaba un ve pelletleri (23.01) fasıl dışında bırakır. İnsanların yemesine elverişli karides unu ise Fasıl 3 Not 3 gereği 03.09’dadır.",
           "Fasıl 3 Not 1 ve Not 3."))
# 19
S.append(q("Aşağıdaki dondurulmuş su ürünlerinden hangisi diğerleriyle aynı pozisyonda <b>yer almaz</b>?",
           ["Dondurulmuş deniz kestanesi", "*Dondurulmuş deniz kulağı", "Dondurulmuş deniz hıyarı", "Dondurulmuş deniz anası", "Dondurulmuş deniz kestanesi yumurtalıkları"], T_F,
           "Deniz kulağı bir yumuşakçadır ve 03.07 Açıklama Notunda başlıca yumuşakçalar arasında sayılır. Deniz kestanesi, deniz hıyarı ve deniz anası 03.08’deki diğer su omurgasızlarıdır; deniz kestanesi yumurtalıkları da başka işlem görmemiş parça olarak 03.08’dedir.",
           "03.07 ve 03.08 Açıklama Notları."))
# 20
S.append(q("Fasıl 3 Genel Açıklamalarına göre aşağıdakilerden hangisi doğrudur?",
           ["Konserve kutusuna konulan her balık 16.04’te sınıflandırılır.",
            "*Modifiye atmosferde paketlenmiş (MAP) taze balık Fasıl 3’te kalır.",
            "Fasılın farklı pozisyonlarındaki ürünlerin karışımları Fasıl 16’ya gider.",
            "Kıyılmış veya öğütülmüş balık Fasıl 3 dışında kalır.",
            "Taşıma öncesinde kabuğunu açmak için ısı şokuna maruz kalan yumuşakçalar 16.05’te sınıflandırılır."], T_N,
           "Genel Açıklamalar, MAP işlemiyle paketlenen taze veya soğutulmuş balığın Fasıl 3’te kaldığını açıkça belirtir. Hava geçirmez kaba konulmak tek başına Fasıl 16’ya göndermez (konserve kutusunda tütsülenmiş somon 03.05). Kıyma ve öğütme ile fasıl içi karışımlar Fasıl 3’te kalır; ısı şoku görmüş yumuşakçalar 03.07’dedir.",
           "Fasıl 3 Genel Açıklamalar."))
# 21
S.append(q("03.02 pozisyonunda ton balıkları için tek tireli bir alt pozisyon grubu bulunmakta, ancak bu grup yenilebilir balık sakatatını hariç tutmakta; karaciğer, yumurta, yüzgeç gibi yenilebilir sakatat ise ayrı bir tek tireli grupta yer almaktadır. Taze ton balığı karaciğerinin hangi tek tireli gruba gireceğinin belirlenmesinde esas alınan kural hangisidir?",
           ["GYK 2(b)", "GYK 3(a)", "GYK 3(c)", "GYK 4", "*GYK 6"], T_G,
           "Pozisyon (03.02) belirlendikten sonra alt pozisyon seçimi GYK 6’ya göre, yalnızca aynı seviyedeki tek tireli alt pozisyonların metinleri karşılaştırılarak yapılır. Ton balığı grubunun metni yenilebilir sakatatı hariç tuttuğundan karaciğer sakatat grubuna girer. GYK 3(a) ve 3(c) pozisyon düzeyinde birden fazla pozisyona girebilen eşya, GYK 4 ise hiçbir pozisyona girmeyen eşya içindir.",
           "GYK 6; 03.02 pozisyon metni ve Açıklama Notu."))
# 22
S.append(q("Fasıl 3 Genel Açıklamalarına göre, tütsüleme işleminden önce veya tütsüleme sırasında pişirilen tütsülenmiş balıklar ........ pozisyonunda; kabuğu içinde buharda veya suda pişirilmiş kabuklu hayvanlar ise ........ pozisyonunda yer alır. Boşlukları doğru tamamlayan seçenek hangisidir?",
           ["*03.05 – 03.06", "16.04 – 16.05", "03.05 – 16.05", "16.04 – 03.06", "03.04 – 03.06"], T_B,
           "Genel Açıklamalar bu iki durumu pişirme kuralının istisnası olarak sayar: tütsüleme öncesinde veya sırasında pişen tütsülenmiş balıklar 03.05’te, kabuğu içinde buharda veya suda pişirilmiş kabuklular 03.06’da kalır. Tuzak, “pişmiş” kelimesini görünce doğrudan Fasıl 16’yı seçmektir.",
           "Fasıl 3 Genel Açıklamalar; 03.05 ve 03.06 pozisyon metinleri."))
# 23
S.append(q("Fasıl 3 Genel Açıklamalarına göre aşağıdaki işlemlerden hangileri ürünü Fasıl 3 dışına <b>çıkarmaz</b>?  I. Balığın kıyılması veya öğütülmesi  II. Balık filetosunun yalnızca ekmek kırıntısıyla kaplanması  III. Nakliye sırasında taze balığa tuzlu su püskürtülmesi  IV. Midyenin taşımadan önce kabuğunu açmak için ısı şokuna tabi tutulması",
           ["I ve III", "II ve IV", "I, II ve III", "*I, III ve IV", "II, III ve IV"], T_C,
           "Kıyma ve öğütme (Genel Açıklamalar), nakliye için tuzlu su püskürtme (03.02 Açıklama Notu) ve kabuğu açmak için ısı şoku (03.07 Açıklama Notu) ürünü Fasıl 3’te bırakır. Yalnızca ekmek kırıntısıyla kaplanmış fileto ise 16.04’e gider.",
           "Fasıl 3 Genel Açıklamalar; 03.02, 03.04 ve 03.07 Açıklama Notları."))
# 24
S.append(q("Bir firma; taze somon filetolarını az miktarda tuz ve şekerle hafifçe tuzlamış, ardından soğuk tütsülemiş, vakumlu ambalajlayıp dondurmuştur. Ürün pişirilmemiş ve başka katkı içermemektedir. Bu ürün hangi pozisyonda sınıflandırılır?",
           ["03.02", "03.03", "03.04", "*03.05", "16.04"], T_S,
           "Tütsülenmiş balıklar (filetolar dahil) 03.05’tedir; tuzlama ve tütsüleme gibi iki işlem görmesi ve az miktarda şeker kullanılması bu sonucu değiştirmez. Dondurulmuş olması onu 03.03 veya 03.04’e götürmez; bu pozisyonlar yalnız taze, soğutulmuş veya dondurulmuş haller içindir. Ambalaj faslı değiştirmediğinden ve ürün başka şekilde hazırlanmadığından 16.04 uygulanmaz.",
           "03.05 pozisyon metni ve Açıklama Notu; Fasıl 3 Genel Açıklamalar."))
# 25
S.append(q("Bir ithalatçı aynı sevkiyatta; kabuğundan çıkarılmış ve yalnızca dondurulmuş deniz taraklarını ve taşımadan önce kabuğunu açmak amacıyla pişirme gerektirmeyen ısı şokuna tabi tutulup dondurulmuş midyeleri ayrı kolilerde getirmiştir. Bu ürünlerle ilgili aşağıdakilerden hangisi doğrudur?",
           ["Deniz tarakları 03.07’de, midyeler 16.05’te sınıflandırılır.",
            "Deniz tarakları 03.06’da, midyeler 03.07’de sınıflandırılır.",
            "Her ikisi de 16.05’te sınıflandırılır.",
            "Deniz tarakları 03.07’de, midyeler 03.09’da sınıflandırılır.",
            "*Her ikisi de 03.07’de sınıflandırılır."], T_S,
           "Taraklar ve midyeler yumuşakçadır; 03.07 bunları kabuklu olsun olmasın dondurulmuş halde kapsar. Açıklama notu, taşıma veya dondurmadan önce kabuğu açmak ya da dengede tutmak için ısı şokuna maruz kalan yumuşakçaları da 03.07’ye dahil eder; bu işlem pişirme sayılmaz. Tuzak, haşlamayı pişirme sayıp 16.05’i seçmektir.",
           "03.07 pozisyon metni ve Açıklama Notu; Fasıl 3 Genel Açıklamalar."))

modul["sorular"] = S
yaz(3, modul)
