#!/usr/bin/env python3
"""Tarife kitabı veri dosyalarını doğrular.

Kullanım: python3 validate.py dosya1.json [dosya2.json ...]
Her dosya için "OK" ya da hata listesi basar. Hata varsa çıkış kodu 1 olur.
"""
import json
import re
import sys
from collections import Counter

LETTERS = "ABCDE"
TAG_RE = re.compile(r"</?(b|i)>|<br/>")
SIX_DIGIT = re.compile(r"\b\d{4}\.\d{2}\b|\b\d{4}\.\d{2}\.\d{2}|\b\d{6,}\b")
YEAR = re.compile(r"\b(19[5-9]\d|20[0-4]\d)\b")
BANNED = [
    "repo", "derleme", ".json", ".txt", ".doc", "S.1", "S.2", "S.9", "çıkmış soru dosyası",
    "gümrük vergisi", "İGV", "KDV", "474 sayılı", "Bağlayıcı Tarife Bilgisi", "İthalat Rejimi",
    "GTİP", "12 haneli", "istatistik pozisyonu",
]
BAD_CHARS = set("✓✗▸►◆★☆■□▪▫✔✘")


def texts(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, list):
        for x in obj:
            yield from texts(x)
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from texts(v)


def check_markup(s, where, errs):
    stripped = TAG_RE.sub("", s)
    if "<" in stripped or ">" in stripped:
        errs.append(f"{where}: izin verilmeyen '<' veya '>' (yalnız <b>, <i> kullanılabilir): {s[:80]!r}")
    if re.search(r"&(?!amp;|nbsp;|lt;|gt;)", s):
        errs.append(f"{where}: kaçışsız '&' karakteri (&amp; yazın): {s[:80]!r}")
    for tag in ("b", "i"):
        if s.count(f"<{tag}>") != s.count(f"</{tag}>"):
            errs.append(f"{where}: kapanmamış <{tag}> etiketi: {s[:80]!r}")
    bad = BAD_CHARS.intersection(s)
    if bad:
        errs.append(f"{where}: fontta olmayan karakter {bad}")


def check_questions(qs, n_expected, per_letter, where, errs, warns, allow_six=False):
    if len(qs) != n_expected:
        errs.append(f"{where}: {len(qs)} soru var, {n_expected} olmalı")
    cnt = Counter()
    stems = set()
    for i, q in enumerate(qs, 1):
        w = f"{where} soru {i}"
        for k in ("soru", "secenekler", "cevap", "gerekce", "dayanak", "tip"):
            if k not in q or (isinstance(q.get(k), str) and not q.get(k).strip()):
                errs.append(f"{w}: '{k}' eksik/boş")
        opts = q.get("secenekler", [])
        if len(opts) != 5:
            errs.append(f"{w}: {len(opts)} seçenek, 5 olmalı")
        if len(set(o.strip().lower() for o in opts)) != len(opts):
            errs.append(f"{w}: tekrarlanan seçenek")
        for o in opts:
            if re.match(r"^\s*[A-Ea-e][\)\.]\s", o):
                errs.append(f"{w}: seçenek metni harf ile başlıyor (A) yazmayın): {o[:40]!r}")
        c = q.get("cevap")
        if c not in LETTERS:
            errs.append(f"{w}: geçersiz cevap {c!r}")
        cnt[c] += 1
        st = re.sub(r"\W+", " ", q.get("soru", "").lower()).strip()
        if st in stems:
            errs.append(f"{w}: aynı soru kökü tekrar ediyor")
        stems.add(st)
        if q.get("gerekce") and len(q["gerekce"]) < 80:
            warns.append(f"{w}: gerekçe çok kısa")
        if not allow_six:
            for s in texts(q):
                if SIX_DIGIT.search(s):
                    errs.append(f"{w}: 4 haneden uzun kod: {SIX_DIGIT.search(s).group(0)}")
    if per_letter and len(qs) == n_expected:
        bad = {L: cnt[L] for L in LETTERS if cnt[L] != per_letter}
        if bad:
            errs.append(f"{where}: şık dağılımı dengesiz {dict(cnt)} (her harf {per_letter} olmalı)")


def validate(path):
    errs, warns = [], []
    try:
        d = json.load(open(path, encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return [f"JSON okunamadı: {e}"], []
    tur = d.get("tur")
    for s in texts(d):
        check_markup(s, path, errs)
        if YEAR.search(s):
            warns.append(f"yıl gibi görünen sayı: {YEAR.search(s).group(0)} → {s[:70]!r}")
        for b in BANNED:
            if b.lower() in s.lower():
                errs.append(f"yasaklı ifade {b!r}: {s[:70]!r}")
    if tur in ("fasil", "giris"):
        if d.get("sakli"):
            return errs, warns
        req = ["fasil", "baslik", "bolum", "oz", "karar_tablosu", "pozisyon_haritasi", "notlar",
               "sinir_komsulari", "tuzaklar", "hafiza", "sinav_odagi", "cikmis_ornekler", "ozet", "sorular"]
        for k in req:
            if k not in d:
                errs.append(f"'{k}' alanı eksik")
        if errs:
            return errs, warns
        if not d["oz"].get("vurgu") or len(d["oz"].get("maddeler", [])) < 2:
            errs.append("oz: vurgu ve en az 2 madde olmalı")
        for r in d["karar_tablosu"].get("satirlar", []):
            if len(r) != 3:
                errs.append(f"karar_tablosu satırı 3 hücre olmalı: {r}")
        if len(d["karar_tablosu"].get("satirlar", [])) < 4:
            errs.append("karar_tablosu en az 4 satır olmalı")
        for r in d["pozisyon_haritasi"]:
            if len(r) != 4:
                errs.append(f"pozisyon_haritasi satırı 4 hücre olmalı: {r}")
        for r in d["notlar"]:
            if len(r) != 2:
                errs.append(f"notlar satırı 2 hücre olmalı: {r}")
        for r in d["sinir_komsulari"]:
            if len(r) != 3:
                errs.append(f"sinir_komsulari satırı 3 hücre olmalı: {r}")
        if len(d["tuzaklar"]) < 5:
            errs.append("tuzaklar en az 5 madde olmalı")
        if not (3 <= len(d["sinav_odagi"]) <= 8):
            errs.append("sinav_odagi 3–8 madde olmalı")
        if len(d["cikmis_ornekler"]) > 2:
            errs.append("cikmis_ornekler en fazla 2 olmalı")
        for j, e in enumerate(d["cikmis_ornekler"], 1):
            for k in ("soru", "secenekler", "cevap", "aciklama"):
                if not e.get(k):
                    errs.append(f"cikmis_ornekler {j}: '{k}' eksik")
            if e.get("cevap") and e.get("secenekler") and "ABCDE".index(e["cevap"]) >= len(e["secenekler"]):
                errs.append(f"cikmis_ornekler {j}: cevap harfi seçenek sayısını aşıyor")
        if len(d["ozet"]) < 4:
            errs.append("ozet en az 4 madde olmalı")
        # 4 haneden uzun kod kontrolü (soru dışı alanlar)
        for k in ("oz", "karar_tablosu", "pozisyon_haritasi", "notlar", "sinir_komsulari", "tuzaklar",
                  "hafiza", "sinav_odagi", "cikmis_ornekler", "ozet"):
            for s in texts(d[k]):
                m = SIX_DIGIT.search(s)
                if m:
                    errs.append(f"{k}: 4 haneden uzun kod: {m.group(0)} → {s[:60]!r}")
        check_questions(d["sorular"], 25, 5, "sorular", errs, warns)
    elif tur == "deneme":
        check_questions(d.get("sorular", []), 50, 10, f"deneme {d.get('no')}", errs, warns)
        for i, q in enumerate(d.get("sorular", []), 1):
            if "fasil" not in q:
                errs.append(f"deneme soru {i}: 'fasil' alanı eksik")
    elif tur == "karma":
        check_questions(d.get("sorular", []), 20, 4, f"karma {d.get('no')}", errs, warns)
        for i, q in enumerate(d.get("sorular", []), 1):
            if "fasil" not in q:
                errs.append(f"karma soru {i}: 'fasil' alanı eksik")
            if len(q.get("gerekce", "")) > 420:
                warns.append(f"karma soru {i}: gerekçe uzun ({len(q['gerekce'])} karakter, ≤ 420 olmalı)")
    elif tur == "hap":
        for k in ("fasil", "sinavda", "pozisyonlar", "hap", "karistirilan"):
            if k not in d:
                errs.append(f"'{k}' alanı eksik")
        if errs:
            return errs, warns
        for r in d["pozisyonlar"]:
            if len(r) != 2:
                errs.append(f"pozisyonlar satırı 2 hücre olmalı: {r}")
        for r in d["karistirilan"]:
            if len(r) != 3:
                errs.append(f"karistirilan satırı 3 hücre olmalı: {r}")
        for b in d["hap"]:
            if len(b.split()) > 40:
                warns.append(f"hap maddesi uzun ({len(b.split())} kelime): {b[:60]!r}")
        for s in texts(d):
            m = SIX_DIGIT.search(s)
            if m:
                errs.append(f"4 haneden uzun kod: {m.group(0)} → {s[:60]!r}")
    else:
        errs.append(f"bilinmeyen tur: {tur!r}")
    return errs, warns


def main():
    bad = False
    for p in sys.argv[1:]:
        errs, warns = validate(p)
        if errs:
            bad = True
            print(f"HATA {p} ({len(errs)}):")
            for e in errs[:60]:
                print("  -", e)
        else:
            print(f"OK {p}")
        for w in warns[:20]:
            print("  uyarı:", w)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
