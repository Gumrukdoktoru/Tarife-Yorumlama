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


def _dogru(q):
    return q["secenekler"]["ABCDE".index(q["cevap"])]


KOK_STOP = {"tari", "cetv", "pozi", "sını", "aşağ", "hang", "yer", "alır", "fası", "bölü", "göre", "olan", "olar",
            "eşya", "dığı", "mama", "edil", "ilgi", "hükü", "nota"}


def koks(t):
    """Türkçe ekleri kabaca atmak için kelimelerin ilk 4 harfini alır."""
    return {w[:4] for w in norm(t).split() if len(w) > 2 and w not in STOP} - KOK_STOP


def _kayit(lab, soru, dogru):
    return (lab, toks(soru + " " + dogru), koks(soru), norm(dogru), toks(dogru))


def karma_overlap(esik=0.5, esik_kok=0.30):
    """Karma test sorularını önceki TÜM sorularla karşılaştırır.

    Havuz: 2.425 modül sorusu, 500 deneme sorusu, pilot/örnek sorular, 236 çıkmış soru ve diğer karma testler.
    Ölçüt 1: soru kökü + doğru şık kelime benzerliği ≥ esik.
    Ölçüt 2: doğru şık aynı (ya da çok benzer) VE soru kökü benzerliği ≥ esik_kok (aynı eşya, farklı ifade).
    """
    pool = []
    for f in glob.glob(os.path.join(DATA, "fasil_*.json")) + glob.glob(os.path.join(DATA, "deneme_*.json")):
        d = json.load(open(f, encoding="utf-8"))
        lab = (f"Fasıl {d['fasil']}" if d.get("tur") in ("fasil", "giris") else f"Deneme {d.get('no')}")
        for i, q in enumerate(d.get("sorular", []), 1):
            pool.append(_kayit(f"{lab} s{i}", q["soru"], _dogru(q)))
    ek = os.path.join(ROOT, "kaynak", "onceki_ek_sorular.json")
    if os.path.exists(ek):
        for i, q in enumerate(json.load(open(ek, encoding="utf-8")), 1):
            pool.append(_kayit(f"{q['kaynak']} s{i}", q["soru"], _dogru(q)))
    for q in json.load(open(os.path.join(ROOT, "kaynak", "cikmis_sorular.json"), encoding="utf-8")):
        pool.append((f"çıkmış {q['no']}", toks(q["metin"]), toks(q["metin"]), "", set()))
    flagged = 0
    seen = []
    for f in sorted(glob.glob(os.path.join(ROOT, "karma", "karma_*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        for i, q in enumerate(d["sorular"], 1):
            k = _kayit(f"Karma {d['no']} s{i}", q["soru"], _dogru(q))
            sebep = None
            for lab, t, kok, dn, dt in pool + seen:
                j = jacc(k[1], t)
                if j >= esik:
                    sebep = (j, lab, "metin")
                    break
                ayni = dn and (k[3] == dn or (len(k[4]) >= 2 and jacc(k[4], dt) >= 0.7))
                if ayni and jacc(k[2], kok) >= esik_kok:
                    sebep = (jacc(k[2], kok), lab, "aynı doğru cevap + benzer kök")
                    break
            if sebep:
                flagged += 1
                print(f"karma {d['no']} soru {i}: {sebep[2]} {sebep[0]:.2f} ({sebep[1]}) → {q['soru'][:90]}")
            seen.append(k)
    print("işaretlenen karma sorusu:", flagged)


def deneme_siki(esik_kok=0.30):
    """Deneme sorularında aynı doğru cevap + benzer kök (farklı ifadeyle aynı eşya) arar."""
    pool = []
    for f in sorted(glob.glob(os.path.join(DATA, "fasil_*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        for i, q in enumerate(d.get("sorular", []), 1):
            pool.append(_kayit(f"Fasıl {d['fasil']} s{i}", q["soru"], _dogru(q)))
    ek = os.path.join(ROOT, "kaynak", "onceki_ek_sorular.json")
    if os.path.exists(ek):
        for i, q in enumerate(json.load(open(ek, encoding="utf-8")), 1):
            pool.append(_kayit(f"{q['kaynak']} s{i}", q["soru"], _dogru(q)))
    seen, n = [], 0
    for f in sorted(glob.glob(os.path.join(DATA, "deneme_*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        for i, q in enumerate(d["sorular"], 1):
            k = _kayit(f"Deneme {d['no']} s{i}", q["soru"], _dogru(q))
            for lab, t, kok, dn, dt in pool + seen:
                ayni = dn and (k[3] == dn or (len(k[4]) >= 2 and jacc(k[4], dt) >= 0.7))
                if ayni and jacc(k[2], kok) >= esik_kok:
                    n += 1
                    print(f"deneme {d['no']} soru {i}: aynı doğru cevap + benzer kök {jacc(k[2], kok):.2f} ({lab}) → {q['soru'][:80]}")
                    break
            seen.append(k)
    print("sıkı denetimde işaretlenen deneme sorusu:", n)


if __name__ == "__main__":
    if "--deneme-siki" in sys.argv:
        deneme_siki()
    if "--karma" in sys.argv:
        karma_overlap()
    if "--ornek" in sys.argv:
        dedup_examples("--uygula" in sys.argv)
    if "--deneme" in sys.argv:
        deneme_overlap()
