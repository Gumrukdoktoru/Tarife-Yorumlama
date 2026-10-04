"""Fasıl 86–89 modül üreteçleri için ortak yardımcılar."""
import json
import os
from collections import Counter

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HARF = "ABCDE"

EP = "Eşya → 4’lü pozisyon"
OT = "Olumsuz teşhis"
FA = "Farklı/aynı pozisyon veya fasıl"
TN = "Fasıl notu · Tanım/Eşik"
GY = "Genel Yorum Kuralı"
ES = "Eşleştirme / Boşluk doldurma"
CC = "Çoktan-çoğa (I–IV)"
SN = "Senaryo"

BEKLENEN = {EP: 5, OT: 4, FA: 4, TN: 4, GY: 2, ES: 2, CC: 2, SN: 2}


def soru(metin, dogru, celdiriciler, harf, tip, gerekce, dayanak):
    """Doğru seçeneği verilen harfin yerine yerleştirerek soru sözlüğü üretir."""
    assert len(celdiriciler) == 4, metin
    assert dogru not in celdiriciler, metin
    assert tip in BEKLENEN, tip
    secenekler = list(celdiriciler)
    secenekler.insert(HARF.index(harf), dogru)
    return {"soru": metin, "secenekler": secenekler, "cevap": harf, "tip": tip,
            "gerekce": gerekce, "dayanak": dayanak}


def yaz(obj):
    qs = obj["sorular"]
    c = Counter(q["cevap"] for q in qs)
    t = Counter(q["tip"] for q in qs)
    assert len(qs) == 25, len(qs)
    assert all(c[h] == 5 for h in HARF), c
    assert dict(t) == BEKLENEN, t
    yol = os.path.join(KITAP, "data", "fasil_%02d.json" % obj["fasil"])
    with open(yol, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    print("yazıldı:", yol, dict(sorted(c.items())))
