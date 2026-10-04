"""Fasıl 48–52 modülleri için ortak yardımcılar."""
import json
import os
import random
from collections import Counter

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ESYA = "Eşya → 4’lü pozisyon"
OLUMSUZ = "Olumsuz teşhis"
FARKLI = "Farklı/aynı pozisyon veya fasıl"
TANIM = "Fasıl notu · Tanım/Eşik"
GYK = "Genel Yorum Kuralı"
ESLE = "Eşleştirme / Boşluk doldurma"
COKLU = "Çoktan-çoğa (I–IV)"
SENARYO = "Senaryo"

BEKLENEN_TIP = {ESYA: 5, OLUMSUZ: 4, FARKLI: 4, TANIM: 4, GYK: 2, ESLE: 2, COKLU: 2, SENARYO: 2}


def S(soru, secenekler, cevap, tip, gerekce, dayanak):
    assert len(secenekler) == 5, soru
    assert cevap in "ABCDE"
    return {"soru": soru, "secenekler": secenekler, "cevap": cevap, "tip": tip,
            "gerekce": gerekce, "dayanak": dayanak}


def yaz(obj, no, tohum):
    qs = obj["sorular"]
    rnd = random.Random(tohum)
    rnd.shuffle(qs)
    harf = Counter(q["cevap"] for q in qs)
    tip = Counter(q["tip"] for q in qs)
    assert len(qs) == 25, len(qs)
    assert all(harf[h] == 5 for h in "ABCDE"), harf
    for t, n in BEKLENEN_TIP.items():
        if abs(tip[t] - n) > 1:
            raise AssertionError(f"tip dağılımı: {tip}")
    yol = os.path.join(KITAP, "data", f"fasil_{no:02d}.json")
    with open(yol, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    print(yol, dict(harf), dict(tip))
