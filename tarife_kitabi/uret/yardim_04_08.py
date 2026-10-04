"""Fasıl 4–8 üreticileri için ortak yardımcılar.

Seçeneklerden doğru olanın başına "*" konur; harf otomatik hesaplanır.
"""
import json
import os
from collections import Counter

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HARF = "ABCDE"

T_E = "Eşya → 4’lü pozisyon"
T_O = "Olumsuz teşhis"
T_F = "Farklı/aynı pozisyon veya fasıl"
T_N = "Fasıl notu · Tanım/Eşik"
T_G = "Genel Yorum Kuralı"
T_B = "Eşleştirme / Boşluk doldurma"
T_C = "Çoktan-çoğa (I–IV)"
T_S = "Senaryo"


def q(soru, secenekler, tip, gerekce, dayanak):
    assert len(secenekler) == 5, soru
    yildiz = [i for i, s in enumerate(secenekler) if s.startswith("*")]
    assert len(yildiz) == 1, soru
    i = yildiz[0]
    temiz = [s[1:] if k == i else s for k, s in enumerate(secenekler)]
    return {
        "soru": soru,
        "secenekler": temiz,
        "cevap": HARF[i],
        "tip": tip,
        "gerekce": gerekce,
        "dayanak": dayanak,
    }


def yaz(no, obj):
    c = Counter(s["cevap"] for s in obj["sorular"])
    t = Counter(s["tip"] for s in obj["sorular"])
    print("şık dağılımı:", dict(sorted(c.items())), "sıra:", "".join(s["cevap"] for s in obj["sorular"]))
    print("tip dağılımı:", dict(t))
    yol = os.path.join(KITAP, "data", f"fasil_{no:02d}.json")
    with open(yol, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    print(yol)


def harf_ata(sorular, sira):
    """Doğru seçeneği, verilen harf sırasına göre yer değiştirerek taşır."""
    sira = sira.replace(" ", "")
    assert len(sira) == len(sorular)
    for s, h in zip(sorular, sira):
        i = HARF.index(s["cevap"])
        j = HARF.index(h)
        o = s["secenekler"]
        o[i], o[j] = o[j], o[i]
        s["cevap"] = h
