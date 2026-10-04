#!/usr/bin/env python3
"""GYK payını azaltma: karma_03 (s7, s17) ve karma_04 (s16, s20) GYK sorularını
plandaki fasıl/tipte yeni sorularla değiştirir (kaynak/gyk_azaltma_plani.json).
Cevap harfi korunur; diğer sorulara dokunulmaz.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

YENI = {
    3: {
        7: {
            "soru": "Fasıl 95 Not 1 ve Not 3 hükümlerine göre, yalnızca uzaktan kumandalı model gemilerde "
                    "kullanılmak üzere tasarlanmış ve ayrı olarak sunulan aşağıdaki aksam ve parçalardan hangisi "
                    "Fasıl 95’te, ait olduğu eşyanın pozisyonunda sınıflandırılır?",
            "secenekler": [
                "Model gemiyi yürüten elektrik motoru",
                "Model gemiye mahsus minyatür içten yanmalı pistonlu motor",
                "Model gemiyi uzaktan yönlendiren elektromanyetik kumanda aleti",
                "Model geminin yakıt sistemine mahsus küçük sıvı pompası",
                "Model gemi gövdesine takılan adi metalden vida ve somunlar",
            ],
            "cevap": "B",
            "tip": "Fasıl notu · Tanım/Eşik",
            "gerekce": "Not 3 fasıl eşyasına mahsus aksamı ait olduğu eşyayla sınıflandırır; 95.03 Açıklama Notu "
                       "model gemilere mahsus minyatür içten yanmalı motorları bu aksamdan sayar. Not 1(m) ve 1(k) "
                       "ise elektrik motorlarını (85.01), uzaktan kumandaları (85.26), sıvı pompalarını (84.13) ve "
                       "genel kullanıma mahsus metal parçaları hariç tutar.",
            "dayanak": "Fasıl 95 Not 1(k), 1(m) ve Not 3; 95.03 Açıklama Notu (aksam, parça ve aksesuarlar).",
            "fasil": 95,
        },
        17: {
            "soru": "Tarife Cetveline göre; motoru veya mekanik itme tertibatı bulunmayan, tekerlekleri kullanıcı "
                    "tarafından doğrudan elle itilerek hareket ettirilen ve engellilerin ulaşımı için özel olarak "
                    "tasarlanmış tekerlekli sandalye hangi fasılda yer alır?",
            "secenekler": ["Fasıl 87", "Fasıl 90", "Fasıl 94", "Fasıl 73", "Fasıl 84"],
            "cevap": "A",
            "tip": "Fasıl/Bölüm bulma",
            "gerekce": "87.13, engellilerin ulaşımı için tasarlanmış koltuk ve taşıyıcıları itici tertibatlı olsun "
                       "olmasın kapsar; 90.18 Açıklama Notu da engelliler için tekerlekli koltukları 87.13’e "
                       "gönderir. Hastane içi tekerlekli sedyeler 94.02’de kalır; çelik iskelet sınıflandırmayı "
                       "değiştirmez.",
            "dayanak": "87.13 pozisyon metni ve Açıklama Notu; 90.18 Açıklama Notu; 94.02 Açıklama Notu.",
            "fasil": 87,
        },
    },
    4: {
        16: {
            "soru": "Aşağıdaki ahşap eşyadan hangisi “ahşap mutfak ve sofra eşyası”nın yer aldığı 44.19 "
                    "pozisyonunda <b>sınıflandırılmaz</b>?",
            "secenekler": [
                "Ahşaptan salata servis kaşığı ve çatalı",
                "Ahşap gövdeli bulaşık fırçası",
                "Tornalanmış ahşap tas",
                "Mutfakta kullanılan ahşap ölçek",
                "Mutfakta kullanılan alelade ahşap baharat kutusu",
            ],
            "cevap": "B",
            "tip": "Olumsuz teşhis",
            "gerekce": "44.19 Açıklama Notu fırça ve süpürgeleri pozisyon dışında bırakır; bulaşık fırçası 96.03’te "
                       "yer alır, yalnız ahşap gövdesi 44.17’ye girerdi. Servis kaşık-çatalı, tas, mutfak ölçeği ve "
                       "alelade baharat kutusu aynı notta 44.19 eşyası olarak sayılır.",
            "dayanak": "44.19 Açıklama Notu; 44.17 pozisyon metni; Fasıl 44 Not 1; 96.03 Açıklama Notu.",
            "fasil": 44,
        },
        20: {
            "soru": "Tarife Cetveline göre, tedavide kullanılmak üzere hazırlanmış; hastalığın adı, kullanma şekli "
                    "ve dozu etiketinde belirtilmiş perakende satış ambalajındaki kolloidal kükürt hangi pozisyonda "
                    "sınıflandırılır?",
            "secenekler": ["28.02", "30.04", "30.03", "28.43", "38.08"],
            "cevap": "B",
            "tip": "Eşya → 4’lü pozisyon",
            "gerekce": "Not 3 gereği Fasıl 28 ürünleri karışım sayılmaz; kolloidal kükürt dozlandırılmış veya perakende "
                       "ambalajlıysa 30.04’e, diğer hallerde 28.02’ye girer. 30.03 onu açıkça dışarıda bırakır; 28.43 "
                       "ise yalnız kolloidal kıymetli metallere aittir.",
            "dayanak": "Fasıl 30 Not 3; 30.03 ve 30.04 Açıklama Notları; 28.02 Açıklama Notu.",
            "fasil": 30,
        },
    },
}


def main():
    for no, degisim in YENI.items():
        yol = os.path.join(ROOT, "karma", f"karma_{no:02d}.json")
        d = json.load(open(yol, encoding="utf-8"))
        for sira, q in degisim.items():
            eski = d["sorular"][sira - 1]
            if eski.get("fasil") not in ("GYK", q["fasil"]):
                raise SystemExit(f"karma {no} s{sira}: beklenmeyen soru (fasıl {eski.get('fasil')})")
            if eski["cevap"] != q["cevap"]:
                raise SystemExit(f"karma {no} s{sira}: cevap harfi değişiyor ({eski['cevap']} → {q['cevap']})")
            d["sorular"][sira - 1] = q
        with open(yol, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=1)
        print("yazıldı:", yol)


if __name__ == "__main__":
    main()
