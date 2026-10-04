"""Fasıl 59–63 modülleri için ortak yardımcılar."""
import json
import os
import random
from collections import Counter

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HARF = "ABCDE"

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


def Q(tip, soru, dogru, yanlis, gerekce, dayanak):
    assert tip in TIPLER, tip
    assert len(yanlis) == 4, soru
    return {"tip": tip, "soru": soru, "dogru": dogru, "yanlis": list(yanlis),
            "gerekce": gerekce, "dayanak": dayanak}


def _harfler(seed):
    rnd = random.Random(seed)
    while True:
        h = list(HARF * 5)
        rnd.shuffle(h)
        if all(not (h[i] == h[i + 1] == h[i + 2]) for i in range(len(h) - 2)):
            return h


def kur(sorular, seed):
    """Doğru seçeneği, dengeli ve düzensiz dağıtılmış harf konumuna yerleştirir."""
    assert len(sorular) == 25, len(sorular)
    harfler = _harfler(seed)
    out = []
    en_uzun = 0
    for s, h in zip(sorular, harfler):
        opts = list(s["yanlis"])
        opts.insert(HARF.index(h), s["dogru"])
        if len(s["dogru"]) > 12 and len(s["dogru"]) == max(len(o) for o in opts):
            en_uzun += 1
        out.append({"soru": s["soru"], "secenekler": opts, "cevap": h, "tip": s["tip"],
                    "gerekce": s["gerekce"], "dayanak": s["dayanak"]})
    t = Counter(q["tip"] for q in out)
    print("tip:", dict(t))
    for k, v in TIPLER.items():
        if t.get(k, 0) != v:
            print("  uyarı: tip sayısı", k, t.get(k, 0), "≠", v)
    print("harf:", dict(sorted(Counter(q["cevap"] for q in out).items())),
          "sıra:", "".join(harfler), "doğru=en uzun:", en_uzun)
    return out


def yaz(d, no):
    path = os.path.join(KITAP, "data", f"fasil_{no:02d}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
    print("yazıldı:", path)
