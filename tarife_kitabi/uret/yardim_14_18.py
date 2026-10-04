"""Fasıl 14–18 üreticileri için ortak yardımcılar."""
import json
import os

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HARF = "ABCDE"


def q(soru, dogru, yanlislar, harf, tip, gerekce, dayanak):
    """Doğru seçeneği istenen harfin yerine yerleştirerek soru sözlüğü üretir."""
    assert len(yanlislar) == 4, soru
    i = HARF.index(harf)
    secenekler = list(yanlislar)
    secenekler.insert(i, dogru)
    return {
        "soru": soru,
        "secenekler": secenekler,
        "cevap": harf,
        "tip": tip,
        "gerekce": gerekce,
        "dayanak": dayanak,
    }


def yaz(no, obj):
    yol = os.path.join(KITAP, "data", f"fasil_{no:02d}.json")
    with open(yol, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    print(yol)
