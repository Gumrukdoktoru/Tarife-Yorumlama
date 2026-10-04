"""Fasıl 9–13 üreticileri için ortak yardımcılar."""
import json
import os
from collections import Counter

LET = "ABCDE"
KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

T_ES = "Eşya → 4’lü pozisyon"
T_OL = "Olumsuz teşhis"
T_FA = "Farklı/aynı pozisyon veya fasıl"
T_NO = "Fasıl notu · Tanım/Eşik"
T_GY = "Genel Yorum Kuralı"
T_EB = "Eşleştirme / Boşluk doldurma"
T_CC = "Çoktan-çoğa (I–IV)"
T_SE = "Senaryo"

BEKLENEN = {T_ES: 5, T_OL: 4, T_FA: 4, T_NO: 4, T_GY: 2, T_EB: 2, T_CC: 2, T_SE: 2}


def Q(tip, soru, dogru, yanlis, harf, gerekce, dayanak):
    """Doğru seçeneği istenen harfin yerine koyarak soru sözlüğü üretir."""
    assert len(yanlis) == 4, soru
    i = LET.index(harf)
    opts = list(yanlis[:i]) + [dogru] + list(yanlis[i:])
    return {"soru": soru, "secenekler": opts, "cevap": harf, "tip": tip,
            "gerekce": gerekce, "dayanak": dayanak}


def sirala(sorular, sira):
    assert sorted(sira) == sorted(sorular.keys()), "sıra listesi eksik/fazla"
    liste = [sorular[k] for k in sira]
    harfler = "".join(q["cevap"] for q in liste)
    cnt = Counter(harfler)
    assert all(cnt[L] == 5 for L in LET), cnt
    tipler = Counter(q["tip"] for q in liste)
    assert tipler == Counter(BEKLENEN), tipler
    for j in range(len(harfler) - 2):
        assert not (harfler[j] == harfler[j + 1] == harfler[j + 2]), f"üçlü seri: {harfler}"
    print("Cevap dizisi:", harfler)
    return liste


def yaz(no, obj):
    yol = os.path.join(KITAP, "data", f"fasil_{no:02d}.json")
    with open(yol, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    print("yazıldı:", yol)
