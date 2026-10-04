#!/usr/bin/env python3
"""GYK azaltma: karma_09 (s7, s19) ve karma_10 (s19, s20) sorularını yeni tiplerle değiştirir.

Plan: kaynak/gyk_azaltma_plani.json. Cevap harfleri korunur (4'er dağılım bozulmaz).
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

YENI = {
    "09": {
        # s7: Fasıl 42 – Farklı/aynı pozisyon veya fasıl (cevap A)
        7: {
            "soru": "Makinelerde veya diğer teknik işlerde kullanılan ve ayrı olarak sunulan aşağıdaki deri "
                    "eşyadan hangisi Tarife Cetvelinde diğerlerinden farklı bir fasılda sınıflandırılır?",
            "secenekler": [
                "Deri esaslı, üzerine iğneleri takılmış kard garnitürü",
                "Dokuma tezgâhlarına mahsus deri toplayıcı",
                "Matbaa makinelerine ait deri silindir manşonu",
                "Deriden yapılmış hortum",
                "Tulumba ve preslere ait deri rondela",
            ],
            "cevap": "A",
            "tip": "Farklı/aynı pozisyon veya fasıl",
            "gerekce": "Bölüm XVI Not 1(b), makinelerde kullanılan deri eşyayı 42.05’e bırakır; toplayıcı, "
                       "silindir manşonu, hortum ve rondela bu nedenle Fasıl 42’dedir. Üzerine iğneleri "
                       "takılmış kard garnitürü ise 42.05 Açıklama Notu gereği 84.48’de yer alır.",
            "dayanak": "Bölüm XVI Not 1(b); 42.05 Açıklama Notu; 84.48 pozisyon metni.",
            "fasil": 42,
        },
        # s19: Fasıl 84 – Olumsuz teşhis (cevap D)
        19: {
            "soru": "Borular, kazanlar, tanklar ve benzeri kaplar için musluk, valf ve benzeri cihazları "
                    "kapsayan 84.81 pozisyonu dikkate alındığında aşağıdakilerden hangisi bu pozisyonda "
                    "<b>sınıflandırılmaz</b>?",
            "secenekler": [
                "İç lastik valfi",
                "Soda-su şişelerine mahsus valf",
                "Karbondioksit basıncıyla beslenen, elle çalıştırılan musluklu, bar tezgâhlarına mahsus "
                "bira dağıtıcısı",
                "İçten yanmalı motorlara mahsus emme (alma) veya egzoz (salıverme) valfi",
                "Termostatik kontrollü karıştırma valfi",
            ],
            "cevap": "D",
            "tip": "Olumsuz teşhis",
            "gerekce": "84.81 Açıklama Notuna göre asıl manada musluk olmayan, benzer işlev gören mekanik "
                       "parçalar ait oldukları makinenin aksamıdır; motorların emme ve egzoz valfleri 84.09’dadır. "
                       "İç lastik ve soda şişesi valfleri, bira dağıtıcısı ve termostatik karıştırma valfi "
                       "84.81’dedir.",
            "dayanak": "84.81 Açıklama Notu; 84.09 pozisyon metni.",
            "fasil": 84,
        },
    },
    "10": {
        # s19: Fasıl 84 – Sıralama (cevap B)
        19: {
            "soru": "Fasıl 84’te yer alan aşağıdaki makine ve cihazların Tarife Cetvelindeki sıraya göre "
                    "(pozisyon numarası küçükten büyüğe) doğru dizilişi hangisidir?"
                    "<br/>I. Şarap imalinde kullanılan hidrolik üzüm presi"
                    "<br/>II. Tütün kıyma makinesi"
                    "<br/>III. Akaryakıtlı ocak brülörü"
                    "<br/>IV. Elle çevrilen kollu, mekanik kurşun kalem açma cihazı"
                    "<br/>V. Otomobiller için portatif hidrolik kriko",
            "secenekler": [
                "V – III – I – IV – II",
                "III – V – I – IV – II",
                "III – V – IV – I – II",
                "III – I – V – IV – II",
                "III – V – I – II – IV",
            ],
            "cevap": "B",
            "tip": "Sıralama",
            "gerekce": "Ocak brülörü 84.16, portatif kriko 84.25, üzüm presi 84.35, mekanik kurşun kalem açma "
                       "cihazı 84.72, tütün kıyma makinesi 84.78’dedir. Tuzak, tütün makinesini içecek "
                       "preslerinin hemen ardında sanmaktır.",
            "dayanak": "84.16, 84.25, 84.35, 84.72 ve 84.78 pozisyon metinleri ve Açıklama Notları.",
            "fasil": 84,
        },
        # s20: Genel – Tarife yapısı (cevap C)
        20: {
            "soru": "Tarife Cetvelinde bazı bölümlerin başında, o bölümün fasıllarına uygulanan bölüm notları "
                    "yer alırken bazı bölümler doğrudan ilk fasılla başlar. Aşağıdaki bölümlerden hangisinin "
                    "başında bölüm notu <b>bulunur</b>?",
            "secenekler": [
                "Bölüm V",
                "Bölüm IX",
                "Bölüm II",
                "Bölüm XIII",
                "Bölüm XVIII",
            ],
            "cevap": "C",
            "tip": "Tarife yapısı",
            "gerekce": "Bölüm II’nin başında “pellet” tabirini tanımlayan bir bölüm notu vardır. Bölüm V, IX, "
                       "XIII ve XVIII ise doğrudan ilk fasıllarının (25, 44, 68 ve 90) notlarıyla başlar; her "
                       "bölümün bir bölüm notu olduğunu sanmak tuzaktır.",
            "dayanak": "Bölüm II Notu; Fasıl 25, 44, 68 ve 90 başlangıç metinleri.",
            "fasil": "Genel",
        },
    },
}


def main():
    for kk, degisim in YENI.items():
        yol = os.path.join(ROOT, "karma", f"karma_{kk}.json")
        with open(yol, encoding="utf-8") as f:
            d = json.load(f)
        for no, yeni in degisim.items():
            eski = d["sorular"][no - 1]
            assert eski["cevap"] == yeni["cevap"], (kk, no, eski["cevap"], yeni["cevap"])
            d["sorular"][no - 1] = yeni
        with open(yol, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=1)
        print("yazıldı:", yol, sorted(degisim))


if __name__ == "__main__":
    main()
