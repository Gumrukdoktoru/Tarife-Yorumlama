"""Fasıl 53–58 modülleri için ortak yardımcılar."""
import json
import os
from collections import Counter

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HARF = "ABCDE"


def S(soru, dogru, yanlis, cevap, tip, gerekce, dayanak):
    """Doğru seçeneği istenen harfin yerine yerleştirir."""
    assert len(yanlis) == 4, soru
    i = HARF.index(cevap)
    opts = list(yanlis)
    opts.insert(i, dogru)
    return {"soru": soru, "secenekler": opts, "cevap": cevap, "tip": tip,
            "gerekce": gerekce, "dayanak": dayanak}


def SX(soru, secenekler, cevap, tip, gerekce, dayanak):
    """Seçenekler doğal sırada verildiğinde (I–IV soruları)."""
    assert len(secenekler) == 5, soru
    return {"soru": soru, "secenekler": list(secenekler), "cevap": cevap, "tip": tip,
            "gerekce": gerekce, "dayanak": dayanak}


TIPLER = {
    "Eşya → 4’lü pozisyon": 5,
    "Olumsuz teşhis": 4,
    "Farklı/aynı pozisyon veya fasıl": 4,
    "Fasıl notu · Tanım/Eşik": 4,
    "Genel Yorum Kuralı": 2,
    "Eşleştirme / Boşluk doldurma": 2,
    "Çoktan-çoğa (I–IV)": 2,
    "Senaryo": 2,
}


def yaz(d, no):
    qs = d["sorular"]
    c = Counter(q["cevap"] for q in qs)
    t = Counter(q["tip"] for q in qs)
    print("harf:", dict(sorted(c.items())), "tip:", dict(t))
    for k in t:
        assert k in TIPLER, k
    path = os.path.join(KITAP, "data", f"fasil_{no:02d}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
    print("yazıldı:", path)
