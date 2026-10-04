#!/usr/bin/env python3
"""Son kontroller.

1) Fasıllar arasında tekrar eden çıkmış soru örneklerini ayıklar (--uygula ile dosyaya yazar).
2) Deneme sorularını aynı fasılın modül sorularıyla ve çıkmış sorularla karşılaştırıp benzerleri raporlar.
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")
STOP = set("ve veya ile bir bu da de için hangi hangisi aşağıdakilerden aşağıdaki tarife cetveline göre "
           "cetvelinin pozisyonunda pozisyonda sınıflandırılır sınıflandırılmaz yer alır almaz olan olarak "
           "fasılda faslında eşya eşyası olsun olmasın".split())


def norm(t):
    t = re.sub(r"<[^>]+>", " ", t.lower())
    return re.sub(r"[^\wçğıöşüâî\.]+", " ", t).strip()


def toks(t):
    return {w for w in norm(t).split() if len(w) > 2 and w not in STOP}


def jacc(a, b):
    return len(a & b) / max(1, len(a | b))


def dedup_examples(apply):
    mods = {}
    for f in sorted(glob.glob(os.path.join(DATA, "fasil_*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        if d.get("sakli"):
            continue
        mods[d["fasil"]] = (f, d)
    occ = {}
    for n, (f, d) in mods.items():
        for i, e in enumerate(d.get("cikmis_ornekler", [])):
            occ.setdefault(norm(e["soru"] + " " + " ".join(e["secenekler"]))[:300], []).append((n, i))
    changed = set()
    removed = []
    for key, lst in occ.items():
        if len(lst) < 2:
            continue
        # tutulacak modül: soru metninde fasıl numarası geçen ya da doğru şıktaki pozisyonun faslı
        def score(item):
            n, i = item
            e = mods[n][1]["cikmis_ornekler"][i]
            s = 0
            if re.search(rf"\b{n}\s*[\.’']?\s*(inci|ıncı|uncu|üncü|nci|ncı|ncu|ncü)?\s*fas", e["soru"].lower()):
                s += 3
            try:
                dogru = e["secenekler"]["ABCDE".index(e["cevap"])]
            except Exception:  # noqa: BLE001
                dogru = ""
            if re.match(rf"^\s*{n:02d}\.\d\d", dogru):
                s += 2
            return (s, -n)
        keep = max(lst, key=score)
        for n, i in lst:
            if (n, i) == keep:
                continue
            d = mods[n][1]
            if len(d["cikmis_ornekler"]) >= 2:
                removed.append((n, i, keep[0], key[:70]))
    # silmeleri uygula (indeksler kaymasın diye ters sırada)
    by_mod = {}
    for n, i, k, key in removed:
        by_mod.setdefault(n, []).append(i)
    for n, idxs in by_mod.items():
        d = mods[n][1]
        for i in sorted(set(idxs), reverse=True):
            if len(d["cikmis_ornekler"]) > 1:
                del d["cikmis_ornekler"][i]
                changed.add(n)
    for n, i, k, key in removed:
        print(f"örnek tekrarı: Fasıl {n} → Fasıl {k}'de tutuldu: {key}")
    if apply:
        for n in changed:
            f, d = mods[n]
            json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"tekrar eden örnek grubu: {sum(1 for v in occ.values() if len(v) > 1)}; silinen: {len(changed)} modülde")


def deneme_overlap():
    mods = {}
    for f in glob.glob(os.path.join(DATA, "fasil_*.json")):
        d = json.load(open(f, encoding="utf-8"))
        mods[d["fasil"]] = [toks(q["soru"] + " " + q["secenekler"]["ABCDE".index(q["cevap"])])
                            for q in d.get("sorular", [])]
    allmod = [(n, t) for n, lst in mods.items() for t in lst]
    past = [toks(q["metin"]) for q in json.load(open(os.path.join(ROOT, "kaynak", "cikmis_sorular.json"), encoding="utf-8"))]
    flagged = 0
    seen = []
    for f in sorted(glob.glob(os.path.join(DATA, "deneme_*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        for i, q in enumerate(d["sorular"], 1):
            t = toks(q["soru"] + " " + q["secenekler"]["ABCDE".index(q["cevap"])])
            best = max(((jacc(t, m), n) for n, m in allmod), default=(0, None))
            bp = max((jacc(t, p) for p in past), default=0)
            bd = max(((jacc(t, s), lab) for lab, s in seen), default=(0, None))
            if best[0] >= 0.55 or bp >= 0.55 or bd[0] >= 0.55:
                flagged += 1
                print(f"deneme {d['no']} soru {i}: modül benzerliği {best[0]:.2f} (Fasıl {best[1]}), "
                      f"çıkmış {bp:.2f}, diğer deneme {bd[0]:.2f} {bd[1] or ''} → {q['soru'][:90]}")
            seen.append((f"d{d['no']}s{i}", t))
    print("işaretlenen deneme sorusu:", flagged)


if __name__ == "__main__":
    if "--ornek" in sys.argv:
        dedup_examples("--uygula" in sys.argv)
    if "--deneme" in sys.argv:
        deneme_overlap()
