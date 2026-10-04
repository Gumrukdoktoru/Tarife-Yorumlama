#!/usr/bin/env python3
"""Fasıl 89 modülü üreteci."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yardim_86_89 import EP, OT, FA, TN, GY, ES, CC, SN, soru, yaz  # noqa: E402

obj = {
    "tur": "fasil",
    "fasil": 89,
    "baslik": "Gemiler ve suda yüzen taşıt ve araçlar",
    "bolum": "XVII",
    "oz": {
        "vurgu": "Fasıl 89 suda yüzen taşıtları işlevine göre ayırır: insan veya yük taşıyan gemiler 89.01, balıkçı ve fabrika gemileri 89.02, eğlence-spor tekneleri ve kürekli kayıklar 89.03, römorkör ve itici gemiler 89.04, seferi ikinci planda kalan iş gemileri, yüzer havuzlar ve yüzer platformlar 89.05, diğer gemiler (savaş gemileri dahil) 89.06, gemi karakteri olmayan yüzen araçlar 89.07, sökülecek gemiler 89.08. Gemi teknesi dışında gemi aksamı için Fasıl 89’da pozisyon yoktur.",
        "maddeler": [
            "Ayrı gelen gemi aksamı (tekne hariç) gemiye ait olduğu belli olsa bile kendi pozisyonunda sınıflandırılır: ahşap kürek 44.21, halat 56.07, yelken 63.06, çapa 73.16, pervane 84.87, dümen ve sevk-idare teçhizatı 84.79, motor Fasıl 84.",
            "Tamamlanmamış gemiler, tekneler ve monte edilmemiş gemiler belirli bir gemi türünün temel özelliğine sahipse o türün pozisyonunda, değilse 89.06’da sınıflandırılır (Not 1).",
            "Suda işletilmek üzere imal olunan hava yastıklı taşıtlar (sahile çıkabilsin veya buz üzerinde işleyebilsin) Fasıl 89’da; hem karada hem suda işleyen motorlu taşıtlar Fasıl 87’de, deniz uçakları 88.02’de.",
            "Yüzer vasıtalar üzerine monte edilmiş tüm hareketli makineler (yüzen vinç, tarama makinesi) Fasıl 89’da kalır.",
        ],
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Süs modeli, teşhir modeli, oyuncak, su kayağı, eğlence parkı sandalı, 100 yılı aşkın antika gemi mi?",
             "<b>44.20</b> / <b>83.06</b> · <b>90.23</b> · <b>95.03</b> · <b>95.06</b> · <b>95.08</b> · <b>97.06</b>"],
            ["2", "Hem karada hem suda kullanılan motorlu taşıt mı?", "Fasıl 87 (amfibi tank <b>87.10</b>)"],
            ["3", "Ayrı gelen gemi aksamı mı? (tekne hariç)", "Kendi pozisyonu (<b>84.87</b> pervane, <b>73.16</b> çapa, <b>63.06</b> yelken)"],
            ["4", "Sökülmek amacıyla mı getirilmiş?", "<b>89.08</b>"],
            ["5", "Gemi karakteri yok, kullanıldığı yerde sabit duran yüzen araç mı? (sal, şamandıra, silindirik duba, yüzen iskele)",
             "<b>89.07</b>"],
            ["6", "Spor-eğlence teknesi, kürekli kayık, kano veya kürekli cankurtaran botu mu?", "<b>89.03</b>"],
            ["7", "Ticari balıkçı gemisi veya balık işleme-konserve fabrika gemisi mi?", "<b>89.02</b>"],
            ["8", "Gemi çekmek veya itmek için mi düzenlenmiş? (römorkör, itici gemi)", "<b>89.04</b>"],
            ["9", "Asıl görevini sabit noktada yapan iş gemisi, yüzer havuz veya yüzer-dalabilen platform mu?*",
             "<b>89.05</b>"],
            ["10", "İnsan veya yük taşımak için mi? (yolcu gemisi, feribot, tanker, kargo, mavna)", "<b>89.01</b>"],
            ["11", "Hiçbiri değilse (savaş gemisi, denizaltı, buz kıran, kablo gemisi, kılavuz gemisi, hastane gemisi)",
             "<b>89.06</b>"],
        ],
        "dipnot": "* Fener gemileri, yangın söndürme gemileri, tarak gemileri, yüzer vinçler, yüzer evler. Ne yüzen ne de dalabilen sabit sondaj platformları 84.30’dadır.",
    },
    "pozisyon_haritasi": [
        ["89.01", "Yolcu, gezinti, feribot, yük gemileri, mavnalar", "İnsan veya yük taşıma",
         "Yolcu gemisi, araba feribotu, tanker, frigorifik gemi, konteyner gemisi, mavna"],
        ["89.02", "Balıkçı gemileri; fabrika gemileri", "Ticari balıkçılık; işleme ve konserve",
         "Trol gemisi, ton balığı avcısı, balina avı gemisi, konserve fabrika gemisi"],
        ["89.03", "Yatlar, eğlence-spor tekneleri; kürekli kayıklar, kanolar", "Spor ve eğlence amacı",
         "Yat, yelkenli, şişirilebilir bot, su bisikleti, kano, kürekli cankurtaran botu"],
        ["89.04", "Römorkörler ve itici gemiler", "Çekme veya itme; insan-yük taşımaz",
         "Römorkör, itici gemi, itici römorkör, kurtarma römorkörü"],
        ["89.05", "Fener, yangın söndürme, tarak gemileri, yüzer vinçler; yüzer havuzlar; yüzer platformlar",
         "Görev sabit noktada; seyir ikinci planda",
         "Tarak gemisi, yüzer vinç, yüzer havuz, kendini kaldırabilen platform, yüzer ev"],
        ["89.06", "Diğer gemiler (savaş ve kurtarma gemileri dahil)", "89.01–89.05 dışı; kürekliler hariç",
         "Savaş gemisi, denizaltı, buz kıran, kablo gemisi, hastane gemisi, kılavuz gemi"],
        ["89.07", "Diğer yüzen araçlar (sal, tank, koferdam, şamandıra, işaret kulesi)", "Gemi karakteri yok; yerinde sabit",
         "Şişirilebilir sal, şamandıra, yüzen iskele, silindirik duba, canlı balık havuzu"],
        ["89.08", "Sökülecek gemiler ve yüzer araçlar", "Sökülmek amacıyla getirilme",
         "Miadını doldurmuş, makineleri sökülmüş gemi"],
    ],
    "notlar": [
        ["Fasıl 89 Not 1",
         "İnşası bitmemiş veya tamamlanmamış gemiler ve gemi tekneleri ile inşası bitirilmiş gemilerin sökülmüş veya henüz monte edilmemiş olanları, belirli bir tür geminin temel özelliklerine sahip değilse 89.06’da sınıflandırılır; sahipse (Genel Açıklamalar) o gemi türünün pozisyonunda yer alır."],
        ["Bölüm XVII Not 4 ve Not 5",
         "Hem denizde hem karada kullanılan motorlu taşıtlar Fasıl 87’dedir. Hava yastıklı taşıtlardan suda işletilmek üzere imal olunanlar, sahile ve iskeleye çıkabilecek veya buz üzerinde işletilebilecek yapıda olsun olmasın Fasıl 89’da; karada veya hem karada hem suda işleyenler Fasıl 87’de; kılavuz hatlılar Fasıl 86’dadır."],
        ["Bölüm XVII Genel Açıklamalar (II) ve (III)",
         "Yüzer vasıtalar üzerine monte edilmiş tüm hareketli makinalar (yüzen vinçler, tarama makinaları, tahılları kaldırıp ayırma makinaları) Fasıl 89’da yer alır. Fasıl 89’da gemi teknesi dışında aksam, parça ve aksesuar hükmü bulunmaz; bunlar gemiye mahsus olsa bile diğer fasıllarda sınıflandırılır."],
        ["Fasıl 89 Genel Açıklamalar (kapsam)",
         "Fasıl; kendinden hareketli olsun olmasın gemileri, vapurları, batardolar, seyyar iskeleler ve şamandıralar gibi yüzen yapıları ve su üzerinde seyahat için düzenlenmiş hava yastıklı taşıtları kapsar. Hareket motorları, denizcilik aletleri, kaldırma makineleri ve mefruşatı takılmamış tamamlanmamış tekneler ile her maddeden gemi tekneleri dahildir."],
        ["Fasıl 89 Genel Açıklamalar (aksam)",
         "Ayrı gelen gemi aksamı kendi rejimine tabidir: Bölüm XVII Not 2 eşyası; kısa ve uzun ahşap kürekler (44.21); dokumaya elverişli halat ve ipler (56.07); yelkenler (63.06); gemi direkleri, ambar ağzı ve kapakları gibi metal inşaat karakterli tekne aksamı (73.08); demir-çelik halatlar (73.12); demir-çelik çapalar (73.16); pervaneler ve yandan çarklı gemi çarkları (84.87); dümenler (44.21, 73.25, 73.26 vb.) ve gemi dümen ve sevk-idare teçhizatı (84.79)."],
        ["Fasıl 89 Genel Açıklamalar (hariçler)",
         "Süs veya dekor amaçlı model gemiler (44.20, 83.06 vb.), 90.23’teki modeller, mayınlar ve torpiller (93.06), çocuklar için gemi şeklinde oyuncaklar (95.03), su kayakları (95.06), eğlence parkı ve fuar sandalları (95.08), 100 yılı aşkın antika gemiler (97.06). Hem karada hem suda seyahat eden taşıtlar Fasıl 87’de, deniz uçakları 88.02’de."],
        ["89.01 Açıklama Notu",
         "Yolcu ve gezinti gemileri; araba, tren ve küçük nehir feribotları dahil her cins feribot; tankerler (petrol, metan, şarap vb.); frigorifik gemiler; maden cevheri, dökme yük, konteyner, ro-ro ve mavna taşıyan gemiler dahil her cins kargo gemisi; malzeme ve bazen insan taşıyan düz güverteli mavnalar ve dubalar. Deniz ve iç sularda (göl, kanal, nehir) kullanılabilirler."],
        ["89.02 Açıklama Notu",
         "Deniz veya iç sularda ticari balıkçılık için düzenlenmiş gemiler (balina avı ve ton balığı avcı gemileri dahil) ve balık konservesi vb. fabrika gemileri. Turizm mevsiminde gezi amacıyla da kullanılabilen balıkçı gemileri 89.02’de kalır; spor amaçlı balıkçı tekneleri 89.03’tedir."],
        ["89.03 Açıklama Notu",
         "Spor ve eğlence amaçlı tüm deniz taşıtları: yatlar, yelkenli ve motorlu botlar, kayıklar, gezinti sandalları, eskimo kayıkları, kanolar, pedallı su bisikletleri, spor balıkçılığı tekneleri, monte edilebilen, katlanan ve şişirilen botlar. Kürekle kullanılan cankurtaran botları da buradadır; diğer cankurtaran botları 89.06’dadır."],
        ["89.04 Açıklama Notu",
         "Römorkörler gemileri çekmek için düzenlenir; özel şekilleri, takviyeli tekneleri, büyüklüklerine göre güçlü makineleri ve çekme tertibatlarıyla ayırt edilir, yolcu veya eşya taşımaz. İtici gemiler mavna itmeye mahsus teçhizat ve yüksek (teleskopik olabilen) dümen köşkü ile ayırt edilir. İtici römorkörler ve kurtarma römorkörleri dahildir. Yangın söndürme veya pompalama donanımlı olabilirler; yalnız yangın söndürme gemileri ise 89.05’tedir."],
        ["89.05 Açıklama Notu",
         "Asıl görevlerini normal olarak sabit bir pozisyonda yapan, seferi ikinci derecede olan gemiler: fener gemileri, yangın söndürme gemileri, tarak gemileri, batık gemileri yüzdürmeye mahsus kaldırıcı tertibatlı gemiler, vinç ve elevatörlü dubalar, yüzer evler, yüzer çamaşırhaneler ve değirmenler; yüzen havuzlar; yüzen veya dalabilen sondaj ve üretim platformları (kendini kaldırabilen, su altında kalabilen, yarı dalan). Hariç: sabit (ne yüzen ne dalabilen) platformlar (84.30), feribotlar (89.01), deniz ürünleri fabrika gemileri (89.02), kablo döşeme gemileri ve okyanus meteoroloji gemileri (89.06)."],
        ["89.06 Açıklama Notu",
         "89.01–89.05’te daha özel olarak yer almayan deniz taşıtları: silahlı ve zırhlı savaş gemileri, silahsız çıkarma gemileri ve yardımcı donanma gemileri, denizaltılar; savaş gemisi özelliklerine sahip, sivil makamlarca (gümrük, polis) kullanılan gemiler; kürekli olmayan cankurtaran sandalları; bilimsel araştırma, laboratuvar ve okyanus meteoroloji gemileri; kablo döşeme gemileri; kılavuz gemiler; buz kıranlar; hastane gemileri; “dracone”lar. Hariç: mavnalar (89.01), yüzer vinç tabanı olarak düzenlenmiş mavnalar (89.05), geçici köprü dubaları ve sallar (89.07)."],
        ["89.07 Açıklama Notu",
         "Gemi karakterine sahip olmayan, kullanıldıkları yerde sabit duran yüzen araçlar: geçici köprülere destek içi boş silindirik dubalar (gemi biçimli dubalar 89.01 veya 89.05), canlı balık ve kabuklu muhafazasına mahsus delikli yüzer havuzlar, yüzen tanklar, koferdamlar, yüzen iskeleler, şamandıralar, işaret kuleleri, paravanlar, denize değince otomatik şişen can salları, havuz kapısı işlevli yüzen araçlar. Hariç: harici tertibatla daldırılan dalgıç çanları (genellikle 84.79), cankurtaran yelek, kemer ve simitleri (maddesine göre)."],
        ["89.08 Açıklama Notu",
         "Sökülmek amacıyla getirilen 89.01–89.07 gemileri ve yüzen araçları; genellikle hasar görmüş veya miadını doldurmuştur ve makineleri, kumanda aletleri veya diğer teçhizatı ithalden önce çıkarılmış olabilir."],
    ],
    "sinir_komsulari": [
        ["Gemi dizel motoru", "84.08", "Bölüm XVII Not 2(e); her çeşit araç motoru Fasıl 84"],
        ["Gemi pervanesi; yandan çarklı gemi çarkı", "84.87", "Fasıl 89’da aksam hükmü yok"],
        ["Demir veya çelikten çapa", "73.16", "Fasıl 89 Genel Açıklamalar"],
        ["Yelken", "63.06", "Fasıl 89 Genel Açıklamalar"],
        ["Ahşap kürek", "44.21", "Fasıl 89 Genel Açıklamalar"],
        ["Dokumaya elverişli maddeden halat", "56.07", "Fasıl 89 Genel Açıklamalar"],
        ["Gemi dümen ve sevk-idare teçhizatı", "84.79", "Fasıl 89 Genel Açıklamalar"],
        ["Denizcilikle ilgili alet ve cihazlar", "90.14", "Bölüm XVII Not 2(g)"],
        ["Hem karada hem suda giden motorlu taşıt; amfibi tank", "Fasıl 87 / 87.10", "Bölüm XVII Not 4; 87.10 Açıklama Notu"],
        ["Deniz uçağı", "88.02", "Hava taşıtı; Fasıl 89 Genel Açıklamalar"],
        ["Ne yüzen ne dalabilen sabit sondaj platformu", "84.30", "89.05 hariç tutması"],
        ["Dalgıç çanı (harici tertibatla daldırılan metal oda)", "84.79", "89.07 hariç tutması"],
        ["Cankurtaran yeleği, kemeri, simidi", "Maddesine göre", "89.07 hariç tutması"],
        ["Mayın, torpil", "93.06", "Fasıl 89 Genel Açıklamalar"],
        ["Gemi şeklinde oyuncak; su kayağı; eğlence parkı sandalı; 100 yılı aşkın antika gemi", "95.03 / 95.06 / 95.08 / 97.06", "Fasıl 89 Genel Açıklamalar"],
    ],
    "tuzaklar": [
        "<b>Gemi aksamı Fasıl 89’da değildir.</b> Tekne hariç; pervane 84.87, çapa 73.16, yelken 63.06, halat 56.07, motor 84.08, dümen teçhizatı 84.79. Uçak pervanesi ise 88.07’dedir.",
        "<b>Römorkör yangın söndürebilir.</b> Yangın söndürme veya pompalama donanımlı römorkör 89.04’te kalır; yalnız yangın söndürme gemisi 89.05’tedir.",
        "<b>Cankurtaran üçe ayrılır.</b> Kürekle hareket eden cankurtaran botu 89.03; diğer cankurtaran sandalları 89.06; denize değince şişen can salı 89.07; can yeleği ve simidi maddesine göre.",
        "<b>Feribot 89.05 değildir.</b> Her cins feribot insan-yük taşıyan gemi olarak 89.01’de; balık fabrika gemisi 89.02’de; kablo gemisi ve okyanus meteoroloji gemisi 89.06’da.",
        "<b>Dubanın şekline bakılır.</b> Geçici köprü için içi boş silindirik duba 89.07; gemi biçimli duba 89.01 veya 89.05; vinç tabanı olarak düzenlenmiş mavna 89.05.",
        "<b>Platform yüzüyorsa 89.05.</b> Kendini kaldırabilen, dalabilen ve yarı dalan sondaj-üretim platformları 89.05’te; ne yüzen ne dalabilen sabit platformlar 84.30’da.",
        "<b>Gümrük ve polis botu savaş gemisi sınıfındadır.</b> Savaş gemisi özelliklerine sahip, sivil makamlarca kullanılan gemiler 89.06’dadır.",
        "<b>Balıkçı gemisi turistik gezi yapsa da 89.02’dir;</b> spor balıkçılığı teknesi ise 89.03’tedir.",
        "<b>Hava yastıklı taşıtta işlediği ortam belirleyicidir.</b> Suda işletilmek üzere imal edilen (sahile çıkabilsin veya buzda gidebilsin) 89; hem karada hem suda 87; kılavuz hatlı 86.",
        "<b>Tamamlanmamış tekne her zaman 89.06 değildir.</b> Belirli bir gemi türünün (ör. tanker) temel özelliğine sahipse o türün pozisyonunda; sahip değilse 89.06. Sökülmek için getirilen gemi ise 89.08.",
    ],
    "hafiza": {
        "kanca": "YO – BA – YAT – RÖ – İŞ – DİĞ – YÜZ – SÖK",
        "aciklama": "<b>YO</b>lcu ve yük 89.01 · <b>BA</b>lıkçı 89.02 · <b>YAT</b> ve kayık 89.03 · <b>RÖ</b>morkör 89.04 · <b>İŞ</b> gemisi ve platform 89.05 · <b>DİĞ</b>er (savaş) 89.06 · <b>YÜZ</b>en araç 89.07 · <b>SÖK</b>ülecek 89.08. Görsel benzetme: bir limana girin; rıhtımda yolcu gemisi ve tanker, yanında balıkçı teknesi, marinada yatlar, gemileri çeken römorkör, açıkta sabit duran tarak gemisi ve yüzer vinç, gri savaş gemisi ve buz kıran, liman ağzında şamandıralar, en uçta sökülmeyi bekleyen hurda gemi."
    },
    "sinav_odagi": [
        "Bu fasıl çıkmış sorularda az yer almıştır; doğrudan sorulan konu römorkörlerdir, diğer sorularda 89.03 gibi pozisyonlar seçeneklerde çeldirici olarak kullanılmıştır.",
        "Römorkörlerin 89.04’te sınıflandırıldığı; 84.08, 87.01 (traktör), 87.16 (römork) ve 88.04 çeldiricileriyle “çeken araç” kavramının karıştırılması.",
        "Deniz taşıtları için dizel motorların gemiye mahsus olsa bile 84.08’de kaldığı; 89.03 ve 88.02 çeldiricileri (Bölüm XVII Not 2(e)).",
        "Fasıl gruplama soruları: gemi pervanesinin nükleer reaktör, bilyalı yatak ve yürüyen merdiven ile aynı fasılda (Fasıl 84) yer aldığı.",
        "Gemi aksamının (pervane, çapa, yelken, motor) Fasıl 89 dışında kalması ve hem karada hem suda giden taşıtların Fasıl 87’ye gitmesi, bölüm notlarıyla birlikte düşünülmesi gereken konulardır.",
    ],
    "cikmis_ornekler": [
        {
            "soru": "Römorkörler, Tarife Cetvelinde hangi pozisyonda sınıflandırılır?",
            "secenekler": ["84.08", "87.01", "87.16", "88.04", "89.04"],
            "cevap": "E",
            "aciklama": "89.04 römorkörleri ve itici gemileri kapsar; römorkörler gemileri çekmek için düzenlenmiş, yolcu veya eşya taşımayan deniz taşıtlarıdır. 87.01 kara traktörleri, 87.16 römorklar içindir; “çekme” işlevi bu çeldiricilere çekebilir.",
        },
        {
            "soru": "Deniz taşıtları için sıkıştırmayla ateşlemeli içten yanmalı pistonlu motorlar (dizel ve yarı dizel), Tarife Cetvelinde hangi tarife pozisyonunda sınıflandırılır?",
            "secenekler": ["89.03", "88.02", "84.08", "85.01"],
            "cevap": "C",
            "aciklama": "Bölüm XVII Not 2(e) ve Fasıl 89 Genel Açıklamaları gereği gemiye mahsus olsa bile motorlar aksam sayılmaz; her çeşit araç motoru 84.07–84.12’de, dizel motorlar 84.08’de sınıflandırılır. Fasıl 89’da gemi teknesi dışında aksam pozisyonu yoktur.",
        },
    ],
    "ozet": [
        "İnsan-yük 89.01, balıkçı ve fabrika gemisi 89.02, spor-eğlence ve kürekli tekne 89.03, römorkör ve itici 89.04.",
        "Görevini sabit noktada yapan iş gemisi, yüzer havuz, yüzer veya dalabilen platform 89.05; sabit platform 84.30.",
        "Kalan gemiler (savaş, denizaltı, buz kıran, kablo, hastane, kılavuz) 89.06; gemi karakteri olmayan sabit yüzen araçlar 89.07; sökülecek gemi 89.08.",
        "Gemi aksamı (tekne hariç) Fasıl 89’da değil: motor 84.08, pervane 84.87, çapa 73.16, yelken 63.06.",
        "Tamamlanmamış tekne, belirli gemi türünün temel özelliğine sahipse o türde; değilse 89.06 (Not 1).",
        "Suda işleyen hava yastıklı taşıt 89; amfibi motorlu taşıt 87; deniz uçağı 88.02.",
    ],
}

S = []

# --- Eşya → 4’lü pozisyon (5) ---
S.append(soru(
    "Tarife Cetveline göre, mavnaları itmek için özel itme teçhizatı ve yüksek teleskopik dümen köşkü bulunan, yolcu veya eşya taşımak için düzenlenmemiş itici gemi hangi pozisyonda sınıflandırılır?",
    "89.04", ["89.01", "89.05", "89.06", "87.01"], "C", EP,
    "89.04 römorkörleri ve itici gemileri kapsar; itici gemiler mavna itmeye mahsus teçhizatları ve yüksek, teleskopik olabilen dümen köşkleriyle ayırt edilir. Mavna 89.01’dedir, ancak onu iten gemi 89.04’tedir. 87.01 kara traktörleri içindir; “itme-çekme” işlevi bu çeldiriciye götürebilir.",
    "89.04 pozisyon metni ve Açıklama Notu (B)."))
S.append(soru(
    "Okyanus meteoroloji istasyonu olarak kullanılan gemi hangi pozisyonda yer alır?",
    "89.06", ["89.05", "89.07", "89.01", "89.02"], "E", EP,
    "89.06 Açıklama Notu bilimsel araştırma ve laboratuvar gemileriyle birlikte okyanus meteoroloji istasyonlarınca kullanılan gemileri sayar; 89.05 Açıklama Notu da bu gemileri açıkça 89.05 dışında bırakarak 89.06’ya gönderir. Sabit bir noktada görev yapması onu 89.05’e götürmez; tuzak budur.",
    "89.05 hariç tutmaları; 89.06 Açıklama Notu."))
S.append(soru(
    "Canlı balıkları ve kabuklu deniz hayvanlarını muhafazaya mahsus delikli yüzer havuz hangi pozisyonda sınıflandırılır?",
    "89.07", ["89.02", "89.05", "89.06", "89.01"], "A", EP,
    "89.07 gemi karakterine haiz olmayan, kullanıldıkları yerde sabit duran yüzen araçları kapsar ve canlı balık ile kabuklu hayvanları muhafazaya mahsus delikli yüzer havuzları açıkça sayar. Balıkçılıkla ilgili olması onu 89.02’ye götürmez; 89.02 balıkçı ve fabrika gemileri içindir.",
    "89.07 Açıklama Notu (2)."))
S.append(soru(
    "Avlanan balıkları işleyip konserve haline getiren donanıma sahip fabrika gemisi hangi pozisyonda yer alır?",
    "89.02", ["89.01", "89.05", "89.06", "89.04"], "D", EP,
    "89.02 balıkçı gemilerini ve balıkçılık ürünlerinin işlenmesine, korunmasına ve konserve edilmesine mahsus fabrika gemilerini kapsar. 89.05 Açıklama Notu deniz ürünleri fabrika gemilerini açıkça hariç tutarak 89.02’ye gönderir. Yük taşımadığından 89.01 de değildir.",
    "89.02 pozisyon metni ve Açıklama Notu; 89.05 hariç tutmaları."))
S.append(soru(
    "Suda giden, pedalla hareket ettirilen eğlence amaçlı su bisikleti hangi pozisyonda sınıflandırılır?",
    "89.03", ["87.12", "95.06", "89.07", "95.08"], "B", EP,
    "89.03 Açıklama Notu spor ve eğlence amaçlı tüm deniz taşıtlarını kapsar ve suda giden pedallı su bisikletlerini açıkça sayar. Pedal nedeniyle 87.12 (bisiklet) düşünmek tuzaktır. 95.06 su kayakları, 95.08 eğlence parkı sandalları içindir; 89.07 gemi karakteri olmayan sabit yüzen araçları kapsar.",
    "89.03 Açıklama Notu; Fasıl 89 Genel Açıklamalar, hariç tutmalar."))

# --- Olumsuz teşhis (4) ---
S.append(soru(
    "Aşağıdakilerden hangisi Tarife Cetvelinin 89. faslında <b>sınıflandırılmaz</b>?",
    "Gemi pervanesi",
    ["Petrol tankeri", "Denizaltı", "Yüzen havuz", "Şişirilebilir sal"],
    "D", OT,
    "Fasıl 89 Genel Açıklamaları ayrı gelen gemi aksamının (tekne hariç) gemiye ait olduğu anlaşılsa bile kendi rejimine tabi olduğunu belirtir; pervaneler ve yandan çarklı gemi çarkları 84.87’dedir. Tanker 89.01, denizaltı 89.06, yüzen havuz 89.05, şişirilebilir sal 89.07’dedir.",
    "Fasıl 89 Genel Açıklamalar; Bölüm XVII Genel Açıklamalar (III)."))
S.append(soru(
    "Aşağıdakilerden hangisi 89.05 pozisyonunda <b>sınıflandırılmaz</b>?",
    "Araba taşıyan feribot",
    ["Fener gemisi", "Tarak gemisi", "Yüzer vinç", "Yarı dalan sondaj platformu"],
    "B", OT,
    "89.05 Açıklama Notu feribotları açıkça hariç tutar; araba, tren ve küçük nehir feribotları dahil her cins feribot 89.01’dedir. Fener gemisi, tarak gemisi, yüzer vinç ve yarı dalan sondaj platformu asıl görevini sabit noktada yapan yüzer yapılar olarak 89.05’tedir.",
    "89.01 ve 89.05 Açıklama Notları."))
S.append(soru(
    "Aşağıdakilerden hangisi 89.07 pozisyonunda <b>sınıflandırılmaz</b>?",
    "Metal odadan ibaret dalgıç çanı",
    ["Işıklı şamandıra", "Yüzen iskele", "Köprü ayağı inşasında kullanılan koferdam", "Mayın taramada kullanılan paravan"],
    "E", OT,
    "89.07 Açıklama Notu, harici bir tertibatla suya daldırılıp çıkarılan metal odadan ibaret dalgıç çanlarını hariç tutar; bunlar genellikle 84.79’dadır. Şamandıralar, yüzen iskeleler, koferdamlar ve mayın tarama paravanları gemi karakteri olmayan yüzen araçlar olarak 89.07’de sayılmıştır.",
    "89.07 Açıklama Notu ve hariç tutmalar."))
S.append(soru(
    "Aşağıdakilerden hangisi 89.06 pozisyonunda <b>sınıflandırılmaz</b>?",
    "Kürekli cankurtaran botu",
    ["Buz kıran", "Kılavuz gemi", "Hastane gemisi", "Su altı kablo döşeme gemisi"],
    "A", OT,
    "89.03 Açıklama Notu kürekle kullanılan cankurtaran botlarını kapsar; 89.06 başlığı da kürekli olanları hariç tutar. Buz kıranlar, kılavuz gemiler, hastane gemileri ve kablo döşeme gemileri 89.06 Açıklama Notunda sayılmıştır.",
    "89.03 ve 89.06 pozisyon metinleri ve Açıklama Notları."))

# --- Farklı/aynı pozisyon veya fasıl (4) ---
S.append(soru(
    "Aşağıdakilerden hangisi diğerlerinden farklı bir pozisyonda yer alır?",
    "Balina avı gemisi",
    ["Konteyner gemisi", "Ro-ro gemisi", "Frigorifik gemi", "Düz güverteli yük mavnası"],
    "C", FA,
    "Balina avı gemileri ticari balıkçılık gemisi olarak 89.02’dedir. Konteyner gemisi, ro-ro gemisi, frigorifik gemi ve düz güverteli mavna insan veya yük taşımaya mahsus gemiler olarak 89.01 Açıklama Notunda sayılmıştır.",
    "89.01 ve 89.02 Açıklama Notları."))
S.append(soru(
    "Aşağıdakilerden hangisi diğerlerinden farklı bir fasılda sınıflandırılır?",
    "Su kayağı",
    ["Yat", "Eskimo kayığı", "Katlanabilir bot", "Kano"],
    "A", FA,
    "Fasıl 89 Genel Açıklamaları su kayaklarını ve benzerlerini hariç tutar; bunlar 95.06’da, yani Fasıl 95’tedir. Yat, eskimo kayığı, katlanabilir bot ve kano spor ve eğlence tekneleri olarak 89.03’tedir.",
    "Fasıl 89 Genel Açıklamalar, hariç tutmalar; 89.03 Açıklama Notu."))
S.append(soru(
    "Aşağıdaki eşya çiftlerinden hangisinde her iki eşya da aynı pozisyonda sınıflandırılır?",
    "Yüzer ev – Yüzer çamaşırhane",
    ["Römorkör – Yangın söndürme gemisi", "Savaş gemisi – Mayın", "Yolcu gemisi – Okyanus meteoroloji gemisi", "Yüzer vinç – Geçici köprü dubası"],
    "E", FA,
    "89.05 Açıklama Notu yüzer evleri, yüzer çamaşırhaneleri ve yüzer değirmenleri aynı grupta sayar. Römorkör 89.04, yangın söndürme gemisi 89.05; savaş gemisi 89.06, mayın 93.06; yolcu gemisi 89.01, meteoroloji gemisi 89.06; yüzer vinç 89.05, silindirik köprü dubası 89.07’dir.",
    "89.01, 89.04–89.07 Açıklama Notları."))
S.append(soru(
    "Aşağıdakilerden hangisi diğerlerinden farklı bir fasılda yer alır?",
    "Hem karada hem suda kullanılmak üzere özel imal edilmiş motorlu taşıt",
    ["Yalnız suda işletilmek üzere imal edilmiş, sahile çıkabilen hava yastıklı taşıt", "Savaş gemisi özellikli gümrük muhafaza botu", "Batık gemileri yüzdürmeye mahsus kaldırıcı tertibatlı gemi", "Sıvıları su yüzeyinde çekerek taşımaya mahsus dracone"],
    "B", FA,
    "Bölüm XVII Not 4 hem denizde hem karada kullanılan motorlu taşıtları Fasıl 87’ye gönderir. Suda işletilmek üzere imal edilen hava yastıklı taşıt sahile çıkabilse de Not 5 gereği Fasıl 89’dadır; gümrük botu ve dracone 89.06’da, batık yüzdürme gemisi 89.05’tedir.",
    "Bölüm XVII Not 4 ve Not 5; 89.05 ve 89.06 Açıklama Notları."))

# --- Fasıl notu · Tanım/Eşik (4) ---
S.append(soru(
    "Fasıl 89 Not 1 ve Genel Açıklamalarına göre inşası bitmemiş bir gemi teknesi nasıl sınıflandırılır?",
    "Belirli bir gemi türünün temel özelliğine sahipse o türün pozisyonunda, sahip değilse 89.06’da",
    ["Her durumda 89.06’da", "Her durumda sökülecek gemi olarak 89.08’de", "Gemi aksamı olarak yapıldığı maddeye göre (73.08 vb.)", "Temel özelliğe sahip olsa bile gemi karakteri taşımadığından 89.07’de"],
    "D", TN,
    "Not 1 ve Genel Açıklamalar tamamlanmamış gemi ve teknelerin, esas özelliğine sahip oldukları gemi türünün rejimine tabi olduğunu, aksi takdirde 89.06’da sınıflandırılacağını belirtir. Gemi teknesi Fasıl 89’da kalan tek aksam türüdür; maddesine göre sınıflandırılmaz. 89.08 yalnız sökülmek amacıyla getirilen gemiler içindir.",
    "Fasıl 89 Not 1; Fasıl 89 Genel Açıklamalar."))
S.append(soru(
    "Fasıl 89 Genel Açıklamalarına göre gemilere ait aksam ve parçalarla ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
    "Tekne dışındaki aksam, gemiye ait olsa da kendi pozisyonunda sınıflandırılır.",
    ["Gemiye mahsus olduğu açıkça anlaşılan aksam 89.06’da sınıflandırılır.",
     "Gemi aksamı Bölüm XVII Not 3 uyarınca asıl kullanımına göre Fasıl 89’da sınıflandırılır.",
     "Yalnız gemi pervaneleri ve çapaları Fasıl 89’da yer alır.",
     "Gemi tekneleri de Fasıl 89 dışında, yapıldıkları maddeye göre sınıflandırılır."],
    "C", TN,
    "Fasıl 89 Genel Açıklamalarına göre fasıl, gemilerin ayrı gelen aksam, parça ve teferruatını (gemi tekneleri hariç) kapsamaz; bunlar gemiye ait olduğu anlaşılsa bile kendi rejimine tabidir. Bölüm XVII Not 3 yalnız Fasıl 86–88 için hüküm getirir. Pervaneler 84.87’de, çapalar 73.16’dadır; her maddeden gemi tekneleri ise Fasıl 89’dadır.",
    "Fasıl 89 Genel Açıklamalar; Bölüm XVII Not 3."))
S.append(soru(
    "89.07 Açıklama Notuna göre bu pozisyondaki yüzen araçların temel özelliği hangisidir?",
    "Gemi karakteri taşımamaları ve yerinde sabit durmaları",
    ["Kendinden hareketli olmaları ve insan taşımaya mahsus olmaları", "Yalnız şişirilebilir maddelerden yapılmış olmaları", "Sökülmek amacıyla getirilmiş olmaları", "Asıl görevlerini seyir halinde yerine getirmeleri"],
    "B", TN,
    "89.07 Açıklama Notu bu pozisyonun gemi karakterine haiz bulunmayan, kullanıldıkları yerde sabit duran çeşitli yüzer vasıtaları kapsadığını belirtir (dubalar, şamandıralar, yüzen iskeleler, koferdamlar). Şişirilebilir sallar bu pozisyondadır ama tek ölçüt değildir; sökülecek araçlar 89.08’e gider.",
    "89.07 Açıklama Notu."))
S.append(soru(
    "89.05 Açıklama Notuna göre fener gemileri, tarak gemileri ve yüzer vinçlerin ortak özelliği hangisidir?",
    "Asıl görevlerini normalde sabit bir noktada yapmaları",
    ["İnsan ve yük taşımak için düzenlenmiş olmaları", "Kürekle hareket ettirilmeleri", "Silah ve zırhlı kalkanla donatılmış savaş gemisi olmaları", "Yalnız iç sularda (göl, kanal, nehir) kullanılmaları"],
    "E", TN,
    "89.05 Açıklama Notu bu gemilerin normal olarak asıl görevlerini sabit bir pozisyonda yaptığını, seferin esas görevlerine göre ikinci derecede kaldığını belirtir. İnsan-yük taşıma 89.01’in, silah ve zırh 89.06’daki savaş gemilerinin, kürek 89.03’ün özelliğidir.",
    "89.05 pozisyon metni ve Açıklama Notu (A)."))

# --- Genel Yorum Kuralı (2) ---
S.append(soru(
    "Bütün parçaları birlikte, monte edilmemiş halde sunulan katlanabilir eğlence kanosu hangi pozisyonda ve hangi Genel Yorum Kuralları uyarınca sınıflandırılır?",
    "89.03 – GYK 1, 2(a) ve 6",
    ["89.07 – GYK 1 ve 6", "89.03 – GYK 3(b) ve 6", "95.06 – GYK 1 ve 6", "89.06 – GYK 1, 2(a) ve 6"],
    "A", GY,
    "GYK 2(a) monte edilmemiş halde sunulan eşyayı tamamlanmış eşya gibi sınıflandırır; Fasıl 89 Not 1 de monte edilmemiş gemilerin, belirli bir türün temel özelliğine sahipse o türde kalacağını gösterir. Kano 89.03’te açıkça sayılmıştır ve alt pozisyon GYK 6 ile belirlenir. Temel özellik açık olduğundan 89.06’ya gitmez.",
    "GYK 1, 2(a) ve 6; Fasıl 89 Not 1; 89.03 Açıklama Notu."))
S.append(soru(
    "Sökülmek amacıyla getirilen, makineleri ve kumanda cihazları ithalden önce çıkarılmış eski yolcu gemisi hangi pozisyonda ve hangi kural uyarınca sınıflandırılır?",
    "89.08 – GYK 1",
    ["89.01 – GYK 1 ve 2(a)", "89.01 – GYK 2(a) ve 6", "89.06 – GYK 1", "89.06 – GYK 2(a)"],
    "D", GY,
    "89.08 pozisyon metni sökülecek gemileri açıkça kapsar ve Açıklama Notu bunların makineleri, kumanda aletleri veya diğer teçhizatı ithalden önce çıkarılmış olabileceğini belirtir; sınıflandırma doğrudan pozisyon metniyle, yani GYK 1 ile yapılır. Eksik gemiyi GYK 2(a) ile 89.01’e veya Not 1 ile 89.06’ya götürmek tuzaktır; belirleyici olan sökülme amacıdır.",
    "GYK 1; 89.08 pozisyon metni ve Açıklama Notu."))

# --- Eşleştirme / Boşluk doldurma (2) ---
S.append(soru(
    "Aşağıdaki deniz taşıtları ile pozisyonların doğru eşleştirmesi hangi seçenekte verilmiştir?<br/>I. Buz kıran<br/>II. Hem itmek hem çekmek için düzenlenmiş itici römorkör<br/>III. Ton balığı avcı gemisi<br/>IV. Gemi tamirinde kullanılan yüzen havuz<br/>a) 89.05 · b) 89.02 · c) 89.06 · d) 89.04",
    "I-c, II-d, III-b, IV-a",
    ["I-d, II-c, III-b, IV-a", "I-c, II-d, III-a, IV-b", "I-a, II-d, III-b, IV-c", "I-c, II-b, III-d, IV-a"],
    "C", ES,
    "Buz kıranlar 89.06’da, itici römorkörler 89.04’te, ton balığı avcı gemileri 89.02’de, yüzen havuzlar 89.05’tedir. Yüzen havuzun bir tür atölye olarak sabit noktada çalışması onu 89.05’e verir; buz kıran ise 89.01–89.05’e girmediğinden 89.06’dadır.",
    "89.02, 89.04, 89.05 (B), 89.06 Açıklama Notları."))
S.append(soru(
    "Bölüm XVII Not 5’e göre suda işletilmek üzere imal olunan hava yastıklı taşıtlar, sahile ve iskeleye çıkabilecek şekilde olsun olmasın ..... Fasılda; hem karada hem de suda işletilmek üzere imal olunanlar ise ..... Fasılda sınıflandırılır. Boşluklara sırasıyla gelmesi gerekenler hangisidir?",
    "89 – 87",
    ["87 – 89", "89 – 89", "86 – 87", "87 – 87"],
    "E", ES,
    "Not 5 hava yastıklı taşıtları en çok benzedikleri taşıtlarla sınıflandırır: suda işletilmek üzere imal olunanlar sahile çıkabilse veya buz üzerinde işleyebilse de Fasıl 89’da; karada veya hem karada hem suda işleyenler Fasıl 87’de; kılavuz hatlılar Fasıl 86’dadır.",
    "Bölüm XVII Not 5; Fasıl 89 Genel Açıklamalar."))

# --- Çoktan-çoğa (2) ---
S.append(soru(
    "Aşağıdaki gemi aksam ve donanımından hangileri Fasıl 89 dışında, kendi pozisyonlarında sınıflandırılır?<br/>I. Demir veya çelikten çapa<br/>II. Yelken<br/>III. Plastikten yapılmış yat teknesi<br/>IV. Yandan çarklı gemiye ait çark",
    "I, II ve IV",
    ["I ve II", "II, III ve IV", "III ve IV", "Yalnız IV"],
    "B", CC,
    "Fasıl 89 Genel Açıklamaları demir-çelik çapaları 73.16’ya, yelkenleri 63.06’ya, pervaneleri ve yandan çarklı gemi çarklarını 84.87’ye gönderir. Her maddeden yapılmış gemi tekneleri ise Fasıl 89’da kalan tek aksam türüdür.",
    "Fasıl 89 Genel Açıklamalar."))
S.append(soru(
    "89.03 pozisyonu ile ilgili aşağıdaki ifadelerden hangileri <b>doğrudur</b>?<br/>I. Monte edilebilen, katlanan veya şişirilen botları kapsar.<br/>II. Kürekle kullanılan cankurtaran botlarını kapsar.<br/>III. Turizm mevsiminde gezi amacıyla da kullanılan ticari balıkçı gemilerini kapsar.<br/>IV. Spor balıkçılığında kullanılan tekneleri kapsar.",
    "I, II ve IV",
    ["I ve II", "II ve III", "I, III ve IV", "III ve IV"],
    "D", CC,
    "89.03 Açıklama Notu monte edilebilen, katlanan ve şişirilen botları, kürekle kullanılan cankurtaran botlarını ve balıkçılık sporu teknelerini sayar. Turizm mevsiminde gezi amacıyla da kullanılan balıkçı gemileri ise 89.02 Açıklama Notu gereği 89.02’de kalır.",
    "89.02 ve 89.03 Açıklama Notları."))

# --- Senaryo (2) ---
S.append(soru(
    "Kıyıdan uzak yataklarda petrol aramak için kullanılan; dubalardan oluşan, çalışma mevkiinde geri alınabilir ayakları deniz yatağına indirilerek platformu su seviyesinin üzerine kaldırabilen, vinç, tulumba ve personel kışlası bulunan ve yedekte çekilerek yer değiştirebilen yapı hangi pozisyonda sınıflandırılır?",
    "89.05",
    ["84.30", "89.06", "89.07", "84.26"],
    "A", SN,
    "89.05 yüzer veya dalabilen sondaj ve üretim platformlarını kapsar; Açıklama Notu geri alınabilir ayaklarıyla platformu su üzerine kaldıran “kendini kaldırabilen platformları” açıkça sayar. Ne yüzen ne dalabilen sabit platformlar 84.30’dadır; bu yapı yüzer ve çekilerek taşınabilir olduğundan 89.05’te kalır. Üzerindeki vinçler ayrı sınıflandırılmaz.",
    "89.05 pozisyon metni ve Açıklama Notu (C)(1)."))
S.append(soru(
    "Savaş sırasında asker ve araç çıkarmak için kullanılan, silahla donatılmamış ve zırhlı kalkanı bulunmayan çıkarma gemisi hangi pozisyonda yer alır?",
    "89.06",
    ["89.01", "87.10", "89.04", "93.06"],
    "C", SN,
    "89.06 Açıklama Notu silahlarla donatılmamış, zırhlı kalkanları olmayan fakat savaş sırasında kullanılan çıkarma gemilerini ve yardımcı donanma gemilerini savaş gemileriyle birlikte sayar. İnsan ve araç taşısa da 89.01’e gitmez. 87.10 karada ve suda giden zırhlı çıkarma araçları (paletli) içindir; tekerleksiz bir gemi söz konusudur.",
    "89.06 Açıklama Notu (1)(b); 87.10 Açıklama Notu."))

obj["sorular"] = S
yaz(obj)
