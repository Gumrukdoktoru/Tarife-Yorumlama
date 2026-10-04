"""Fasıl 70–72 modülleri için ortak yardımcılar."""
import json
import os
from collections import Counter

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ESYA = "Eşya → 4’lü pozisyon"
OLUMSUZ = "Olumsuz teşhis"
FARKLI = "Farklı/aynı pozisyon veya fasıl"
TANIM = "Fasıl notu · Tanım/Eşik"
GYK = "Genel Yorum Kuralı"
ESLES = "Eşleştirme / Boşluk doldurma"
COKLU = "Çoktan-çoğa (I–IV)"
SENARYO = "Senaryo"

TIP_HEDEF = {ESYA: 5, OLUMSUZ: 4, FARKLI: 4, TANIM: 4, GYK: 2, ESLES: 2, COKLU: 2, SENARYO: 2}


def soru(tip, metin, dogru, yanlislar, harf, gerekce, dayanak):
    """Doğru seçeneği 'harf' konumuna yerleştirir; yanlışlar verilen sırayla kalır."""
    assert len(yanlislar) == 4, metin
    assert harf in "ABCDE", metin
    secenekler = list(yanlislar)
    secenekler.insert("ABCDE".index(harf), dogru)
    assert len(set(secenekler)) == 5, metin
    return {"soru": metin, "secenekler": secenekler, "cevap": harf, "tip": tip,
            "gerekce": gerekce, "dayanak": dayanak}


def kaydet(obj, nn):
    sayac = Counter(q["cevap"] for q in obj["sorular"])
    tipler = Counter(q["tip"] for q in obj["sorular"])
    print("soru sayısı:", len(obj["sorular"]), "cevaplar:", dict(sorted(sayac.items())))
    for t, n in TIP_HEDEF.items():
        if tipler.get(t, 0) != n:
            print(f"  tip uyarısı: {t}: {tipler.get(t, 0)} (hedef {n})")
    yol = os.path.join(KITAP, "data", f"fasil_{nn:02d}.json")
    with open(yol, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    print("yazıldı:", yol)
