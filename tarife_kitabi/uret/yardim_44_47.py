"""Fasıl 44–47 modülleri için ortak yardımcılar."""
import json
import os
from collections import Counter

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

T_E = "Eşya → 4’lü pozisyon"
T_O = "Olumsuz teşhis"
T_F = "Farklı/aynı pozisyon veya fasıl"
T_N = "Fasıl notu · Tanım/Eşik"
T_G = "Genel Yorum Kuralı"
T_B = "Eşleştirme / Boşluk doldurma"
T_C = "Çoktan-çoğa (I–IV)"
T_S = "Senaryo"


def q(soru, dogru, yanlislar, harf, tip, gerekce, dayanak):
    """Doğru seçeneği verilen harfin yerine koyarak soru sözlüğü üretir."""
    assert len(yanlislar) == 4, soru
    idx = "ABCDE".index(harf)
    secenekler = list(yanlislar)
    secenekler.insert(idx, dogru)
    return {"soru": soru, "secenekler": secenekler, "cevap": harf, "tip": tip,
            "gerekce": gerekce, "dayanak": dayanak}


def yaz(no, obj):
    sorular = obj["sorular"]
    sayac = Counter(s["cevap"] for s in sorular)
    tipler = Counter(s["tip"] for s in sorular)
    yol = os.path.join(KITAP, "data", f"fasil_{no:02d}.json")
    with open(yol, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    print(yol, len(sorular), dict(sorted(sayac.items())))
    for t, n in tipler.items():
        print("  ", n, t)
