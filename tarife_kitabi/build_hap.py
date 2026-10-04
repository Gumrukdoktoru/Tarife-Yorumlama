#!/usr/bin/env python3
"""Hap Bilgi Kitabını dizer: son 5 sınav analizi + fasıl hap bilgileri + 10 karma test.

Kullanım: python3 build_hap.py cikti.pdf
"""
import collections
import glob
import json
import os
import re
import sys

from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (CondPageBreak, Flowable, KeepTogether, NextPageTemplate, PageBreak, Spacer,
                                Table, TableStyle)
from reportlab.platypus.flowables import BalancedColumns
from reportlab.platypus.tableofcontents import TableOfContents

import build_book as bb
from build_book import (CALLOUT_BG, GOLD, HEAD_BG, INK, LM, MUTED, NAVY, NAVY_D, OK, OK_BG, PAGE_H, PAGE_W,
                        RM, RULE, W, WARN, WARN_BG, ZEBRA, Marker, P, TocMark, base, bullets, fix_stem, kicker,
                        sentence, small, subtitle, title, toc0, toc1)

ROOT = bb.ROOT
KAY = os.path.join(ROOT, "kaynak")
HAP = os.path.join(ROOT, "hap")
KARMA = os.path.join(ROOT, "karma")
BASL = json.load(open(os.path.join(KAY, "basliklar.json"), encoding="utf-8"))
FB = BASL["fasil_basliklari"]
BOLUMLER = BASL["bolumler"]
LOGO = os.path.join(KAY, "gorsel", "logo.png")

# Kompakt stiller
c_base = ParagraphStyle("c_base", parent=base, fontSize=8.6, leading=11.4)
c_small = ParagraphStyle("c_small", parent=base, fontSize=7.8, leading=10.2, textColor=MUTED)
c_cell = ParagraphStyle("c_cell", parent=base, fontSize=7.9, leading=10.0)
c_cell_b = ParagraphStyle("c_cell_b", parent=c_cell, fontName="LS-B")
c_cell_h = ParagraphStyle("c_cell_h", parent=c_cell, fontName="LS-B", textColor=NAVY)
c_h1 = ParagraphStyle("c_h1", parent=base, fontName="LS-B", fontSize=12.5, leading=16, textColor=NAVY,
                      spaceBefore=6, spaceAfter=4)
c_h2 = ParagraphStyle("c_h2", parent=base, fontName="LS-B", fontSize=9.8, leading=12.6, textColor=NAVY)
c_bolum = ParagraphStyle("c_bolum", parent=base, fontName="LS-B", fontSize=9.2, leading=12, textColor=colors.white)
q_stem = ParagraphStyle("q_stem", parent=base, fontSize=8.9, leading=11.9)
q_opt = ParagraphStyle("q_opt", parent=base, fontSize=8.6, leading=11.2, leftIndent=12)
q_optc = ParagraphStyle("q_optc", parent=base, fontSize=8.6, leading=11.2)
a_txt = ParagraphStyle("a_txt", parent=base, fontSize=7.7, leading=9.9)
key_st = ParagraphStyle("key_st", parent=base, fontName="LS-B", fontSize=8.6, leading=11, textColor=NAVY)

# Sıralı (tek ton) mavi rampa: 0 = hiç sorulmadı
SEQ = ["#EEF1F5", "#CDE2FB", "#86B6EF", "#3987E5", "#1C5CAB", "#0D366B"]
SEQ_SINIR = [0, 1, 2, 3, 5, 8]  # her kovanın alt sınırı (ana soru sayısı)


def seq_renk(n):
    k = 0
    for i, s in enumerate(SEQ_SINIR):
        if n >= s:
            k = i
    return SEQ[k], (colors.white if k >= 4 else INK)


def bolum_of(n):
    cur = None
    for b in BOLUMLER:
        if b["ilk_fasil"] <= n:
            cur = b
    return cur


# ---------------------------------------------------------------- analiz verisi
def analiz_yukle():
    p = os.path.join(KAY, "son5_analiz.json")
    if not os.path.exists(p):
        return []
    return json.load(open(p, encoding="utf-8"))


def fasil_list(x):
    out = []
    for v in x or []:
        if isinstance(v, int) or (isinstance(v, str) and v.isdigit()):
            out.append(int(v))
        elif isinstance(v, str) and v.upper() == "GYK":
            out.append(0)
    return out


def istatistik(A):
    tar = [r for r in A if r.get("kapsam") in ("tarife", "tarife_yapisi")]
    tip = collections.Counter(r["tip"] for r in tar)
    kapsam = collections.Counter(r.get("kapsam") for r in A)
    ana = collections.Counter()
    sec = collections.Counter()
    konular = collections.defaultdict(list)
    for r in tar:
        fa = set(fasil_list(r.get("fasil_ana")))
        for f in fa:
            ana[f] += 1
            if r.get("konu"):
                konular[f].append(r["konu"])
        for f in set(fasil_list(r.get("fasil_secenek"))) - fa:
            sec[f] += 1
    bol = collections.Counter()
    for f, c in ana.items():
        if f:
            bol[bolum_of(f)["no"]] += c
    poz = collections.Counter(p for r in tar for p in set(r.get("pozisyonlar") or []) if re.fullmatch(r"\d\d\.\d\d", p))
    return dict(n=len(A), n_tar=len(tar), tip=tip, kapsam=kapsam, ana=ana, sec=sec, bol=bol, poz=poz,
                konular=konular, kalip=kalip_ornekleri(tar))


def kalip_ornekleri(tar):
    d = collections.defaultdict(list)
    for r in tar:
        k = (r.get("kalip") or "").strip()
        if k and k not in d[r["tip"]]:
            d[r["tip"]].append(k)
    return d


# ---------------------------------------------------------------- grafikler
class HBar(Flowable):
    """Tek seri yatay çubuk grafiği (büyüklüğe göre sıralı, değer etiketi çubuğun sağında)."""

    def __init__(self, rows, width=W, label_w=62 * mm, bar_h=9, gap=4.5, renk=NAVY, toplam=None):
        super().__init__()
        self.rows, self.width, self.label_w = rows, width, label_w
        self.bar_h, self.gap, self.renk, self.toplam = bar_h, gap, renk, toplam

    def wrap(self, aw, ah):
        self.height = len(self.rows) * (self.bar_h + self.gap) + 4
        return self.width, self.height

    def draw(self):
        c = self.canv
        mx = max((v for _, v in self.rows), default=1) or 1
        plot_w = self.width - self.label_w - 22 * mm
        y = self.height - self.bar_h - 2
        for lab, v in self.rows:
            c.setFont("LS", 8)
            c.setFillColor(INK)
            c.drawRightString(self.label_w - 6, y + 2, lab)
            w = max(2, plot_w * v / mx)
            c.setFillColor(self.renk)
            c.roundRect(self.label_w, y, w, self.bar_h, 2, stroke=0, fill=1)
            c.setFillColor(INK)
            c.setFont("LS-B", 8)
            txt = str(v)
            if self.toplam:
                txt += f"  ·  %{round(100 * v / self.toplam)}"
            c.drawString(self.label_w + w + 4, y + 2, txt)
            y -= self.bar_h + self.gap
        # taban çizgisi
        c.setStrokeColor(RULE)
        c.setLineWidth(0.6)
        c.line(self.label_w, 2, self.label_w, self.height - 1)


class IsiIzgara(Flowable):
    """97 fasıllık ısı ızgarası: hücre rengi = son 5 sınavdaki ana soru sayısı."""

    def __init__(self, ana, sec, cols=14):
        super().__init__()
        self.ana, self.sec, self.cols = ana, sec, cols
        self.cw = W / cols
        self.ch = 11.5 * mm

    def wrap(self, aw, ah):
        rows = (97 + self.cols - 1) // self.cols
        self.height = rows * self.ch + 16 * mm
        return W, self.height

    def draw(self):
        c = self.canv
        top = self.height
        for n in range(1, 98):
            r, k = divmod(n - 1, self.cols)
            x = k * self.cw
            y = top - (r + 1) * self.ch
            bg, fg = seq_renk(self.ana.get(n, 0))
            c.setFillColor(colors.HexColor(bg) if isinstance(bg, str) else bg)
            c.setStrokeColor(colors.white)
            c.setLineWidth(1.5)
            c.roundRect(x + 1, y + 1, self.cw - 2, self.ch - 2, 2.5, stroke=1, fill=1)
            c.setFillColor(fg)
            c.setFont("LS-B", 8.5)
            c.drawCentredString(x + self.cw / 2, y + self.ch - 4.3 * mm, f"{n:02d}")
            a, s = self.ana.get(n, 0), self.sec.get(n, 0)
            c.setFont("LS", 6.6)
            if n == 77:
                c.drawCentredString(x + self.cw / 2, y + 2.2 * mm, "saklı")
            elif a or s:
                c.drawCentredString(x + self.cw / 2, y + 2.2 * mm, f"{a} · {s}")
        # ölçek açıklaması
        y = 3 * mm
        c.setFont("LS", 7.5)
        c.setFillColor(INK)
        c.drawString(0, y + 6.5 * mm, "Hücre rengi: fasılın doğru cevap / soru konusu olduğu soru sayısı.  "
                                      "Hücredeki sayılar: konu · yalnız seçeneklerde.")
        etik = ["0", "1", "2", "3–4", "5–7", "8+"]
        x = 0
        for i, e in enumerate(etik):
            c.setFillColor(colors.HexColor(SEQ[i]))
            c.roundRect(x, y, 9 * mm, 4.2 * mm, 1.5, stroke=0, fill=1)
            c.setFillColor(INK)
            c.drawString(x + 10.5 * mm, y + 1.2 * mm, e)
            x += 24 * mm


def stat_tiles(items):
    cells = []
    for v, lab in items:
        cells.append([P(f'<font size="14.5" color="#1F3A5F"><b>{v}</b></font>', ParagraphStyle("tv", parent=base, leading=17)), Spacer(1, 2),
                      P(lab, c_small)])
    t = Table([cells], colWidths=[W / len(items)] * len(items))
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), CALLOUT_BG), ("LINEBEFORE", (0, 0), (0, -1), 3, NAVY),
                           ("LINEAFTER", (0, 0), (-2, -1), 0.6, colors.white),
                           ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                           ("LEFTPADDING", (0, 0), (-1, -1), 9), ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    return t


def ctable(header, rows, widths, bold_first=True, zebra=True):
    data = [[P(h, c_cell_h) for h in header]] if header else []
    for r in rows:
        data.append([P(str(r[0]), c_cell_b if bold_first else c_cell)] + [P(str(x), c_cell) for x in r[1:]])
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    ts = [("LINEBELOW", (0, 0), (-1, -1), 0.35, RULE), ("VALIGN", (0, 0), (-1, -1), "TOP"),
          ("TOPPADDING", (0, 0), (-1, -1), 2.2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2),
          ("LEFTPADDING", (0, 0), (-1, -1), 3.5), ("RIGHTPADDING", (0, 0), (-1, -1), 3.5)]
    if header:
        ts += [("BACKGROUND", (0, 0), (-1, 0), HEAD_BG), ("LINEBELOW", (0, 0), (-1, 0), 0.8, NAVY)]
    if zebra:
        for i in range(1 if header else 0, len(data)):
            if (i % 2 == 0) == bool(header):
                ts.append(("BACKGROUND", (0, i), (-1, i), ZEBRA))
    t.setStyle(TableStyle(ts))
    return t


def cbox(flowables, bg, bar, pad=5):
    t = Table([[flowables]], colWidths=[W])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg), ("LINEBEFORE", (0, 0), (0, -1), 2.5, bar),
                           ("TOPPADDING", (0, 0), (-1, -1), pad), ("BOTTOMPADDING", (0, 0), (-1, -1), pad),
                           ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8)]))
    return t


# ---------------------------------------------------------------- bölümler
TIP_SIRASI = ["Eşya → 4’lü pozisyon", "Pozisyon → eşya", "Olumsuz teşhis", "Farklı/aynı pozisyon veya fasıl",
              "Fasıl/Bölüm bulma", "Fasıl notu · Tanım/Eşik", "Genel Yorum Kuralı", "Sıralama",
              "Çoktan-çoğa / Eşleştirme", "Senaryo", "Tarife yapısı"]
TIP_IPUCU = {
    "Eşya → 4’lü pozisyon": "Önce fasıl notundaki hariç listesine bak; sonra pozisyon metni, en son artık pozisyon.",
    "Pozisyon → eşya": "Seçeneklerdeki her eşyanın gerçek pozisyonunu bul; tek uyan doğru cevaptır.",
    "Olumsuz teşhis": "Fasıl/Bölüm notunun “kapsamaz” listesi çoğu zaman doğru cevabı verir.",
    "Farklı/aynı pozisyon veya fasıl": "Her seçeneği ayrı sınıflandır; çoğunluğun ortak fasılını bul, ayrık olanı işaretle.",
    "Fasıl/Bölüm bulma": "Fasıl başlıklarının sırası ve Bölüm sınırları ezber gerektirir; harita tablosunu kullan.",
    "Fasıl notu · Tanım/Eşik": "Yüzde, ölçü ve tanım içeren notlar ezberlenir; sayılar seçeneklerde oynanır.",
    "Genel Yorum Kuralı": "Takım → 3(b), demonte/eksik → 2(a), karışım → 2(b)/3, mahfaza → 5(a), ambalaj → 5(b).",
    "Sıralama": "Her eşyayı 4’lü pozisyonuna çevir, numaraya göre küçükten büyüğe diz.",
    "Çoktan-çoğa / Eşleştirme": "Önce kesin yanlış önermeyi ele; kalan seçenek sayısı hızla düşer.",
    "Senaryo": "Uzun tanımda belirleyici özelliği (madde, işlev, işlenme derecesi) ayıkla.",
    "Tarife yapısı": "Bölüm/Fasıl/pozisyon hiyerarşisini ve notların bağlayıcılığını bil.",
}


def analiz_story(S):
    s = [NextPageTemplate("normal"), PageBreak(), Marker("Son 5 Sınavın Analizi", "Bölüm 1"),
         TocMark(0, "Bölüm 1 — Son 5 Sınavın Analizi", "analiz"),
         P("BÖLÜM 1", kicker), Spacer(1, 2), P("Son 5 Sınavın Analizi", title), Spacer(1, 3),
         P("Son beş Gümrük Müşavirliği sınavındaki tarife soruları tek tek sınıflandırıldı: soru tipi, sorunun "
           "konusu olan fasıl, seçeneklerde yer alan fasıllar ve sorulan 4’lü pozisyonlar. Bu kitaptaki hap "
           "bilgilerin ağırlığı ve karma testlerdeki soru dağılımı bu sayımlara göre ayarlandı.", c_base),
         Spacer(1, 7)]
    top_f = next(((f, c) for f, c in S["ana"].most_common() if f), (0, 0))
    s.append(stat_tiles([(S["n"], "incelenen sınav sorusu"), (S["n_tar"], "4’lü pozisyon / not düzeyinde tarife sorusu"),
                         (len([f for f in S["ana"] if f]), "fasıl en az bir sorunun konusu oldu"),
                         (f"Fasıl {top_f[0]}", f"en çok sorulan fasıl: {top_f[1]} soru"),
                         (f"GYK {S['ana'].get(0, 0)}", "soruda Genel Yorum Kuralları konu oldu")]))
    s.append(Spacer(1, 4))
    dis = S["kapsam"].get("alt_pozisyon", 0) + S["kapsam"].get("mevzuat", 0)
    if dis:
        s.append(P(f"Not: {dis} soru alt pozisyon (6 hane ve üstü) ya da mevzuat konusuydu; kitabın 4’lü pozisyon "
                   "ve not düzeyindeki kapsamı dışında kaldığı için sayımlara alınmadı.", c_small))
    # 1.1 soru tipleri
    s += [Spacer(1, 6), TocMark(1, "Soru tipi yoğunluğu", "an_tip"), P("1.1 Soru tipi yoğunluğu", c_h1)]
    rows = sorted(S["tip"].items(), key=lambda kv: -kv[1])
    s.append(HBar([(k, v) for k, v in rows], label_w=58 * mm, toplam=S["n_tar"]))
    s.append(Spacer(1, 6))
    # 1.2 soru kalıpları
    s += [CondPageBreak(60 * mm), TocMark(1, "Nasıl soruluyor: soru kalıpları", "an_kalip"),
          P("1.2 Nasıl soruluyor: soru kalıpları ve çözüm yolu", c_h1)]
    kt = []
    for t, v in rows:
        ornek = "<br/>".join("• " + k for k in S["kalip"].get(t, [])[:2])
        kt.append([f"{t}<br/><font color='#5B6573'>{v} soru</font>", ornek, TIP_IPUCU.get(t, "")])
    s.append(ctable(["Soru tipi", "Sınavdaki kalıp", "Çözüm yolu"], kt, [38 * mm, 0.52 * (W - 38 * mm), 0.48 * (W - 38 * mm)]))
    # 1.3 bölüm yoğunluğu
    s += [CondPageBreak(90 * mm), TocMark(1, "Bölümlere göre dağılım", "an_bol"),
          P("1.3 Bölümlere göre dağılım", c_h1)]
    brows = []
    for b in BOLUMLER:
        if S["bol"].get(b["no"]):
            ad = sentence(b["baslik"])
            ad = ad if len(ad) <= 38 else ad[:37].rsplit(" ", 1)[0] + "…"
            brows.append((f"{b['no']} · {ad}", S["bol"][b["no"]]))
    brows.sort(key=lambda kv: -kv[1])
    s.append(HBar(brows, label_w=70 * mm, bar_h=8, gap=3.5))
    if S["ana"].get(0):
        s.append(P(f"Genel Yorum Kuralları ayrıca {S['ana'][0]} sorunun konusu oldu.", c_small))
    # 1.4 fasıl haritası
    s += [PageBreak(), TocMark(1, "97 fasılın sınav haritası", "an_harita"), P("1.4 97 fasılın sınav haritası", c_h1),
          P("Koyu hücreler en çok sorulan fasıllardır. Açık gri fasıllar son beş sınavda soru konusu olmadı; "
            "bunlar seçeneklerde çeldirici olarak yer almış olabilir.", c_base), Spacer(1, 5),
          IsiIzgara(S["ana"], S["sec"])]
    # 1.5 en çok sorulan fasıllar
    s += [Spacer(1, 6), TocMark(1, "En çok sorulan fasıllar ve konuları", "an_top"),
          P("1.5 En çok sorulan fasıllar ve sorulan konular", c_h1)]
    trow = []
    for f, c in S["ana"].most_common(22):
        ad = "Genel Yorum Kuralları" if f == 0 else f"Fasıl {f}"
        konu = "; ".join(dict.fromkeys(S["konular"].get(f, [])))
        if len(konu) > 260:
            konu = konu[:258].rsplit(";", 1)[0] + "; …"
        trow.append([ad, str(c), str(S["sec"].get(f, 0)), konu])
    s.append(ctable(["Fasıl", "Konu", "Seçenek", "Sorulan konular"], trow, [27 * mm, 11 * mm, 15 * mm, W - 53 * mm]))
    # 1.6 pozisyonlar
    s += [CondPageBreak(50 * mm), TocMark(1, "En çok geçen 4’lü pozisyonlar", "an_poz"),
          P("1.6 Sorularda en çok geçen 4’lü pozisyonlar", c_h1)]
    pz = [(p, n) for p, n in S["poz"].most_common() if n >= 2]
    cols = 5
    prow = []
    for i in range(0, len(pz), cols):
        chunk = pz[i:i + cols]
        prow.append([f"<b>{p}</b>  <font color='#5B6573'>×{n}</font>" for p, n in chunk] + [""] * (cols - len(chunk)))
    if prow:
        s.append(ctable(None, prow, [W / cols] * cols, bold_first=False))
    tek = sorted(p for p, n in S["poz"].items() if n == 1)
    if tek:
        s += [Spacer(1, 4), P("<b>Bir kez sorulanlar:</b> " + ", ".join(tek) + ".", c_cell)]
    # 1.7 sorulmayan fasıllar
    hic = [n for n in range(1, 98) if n != 77 and not S["ana"].get(n)]
    s += [Spacer(1, 6), TocMark(1, "Son 5 sınavda konu olmayan fasıllar", "an_yok"),
          P("1.7 Son 5 sınavda konu olmayan fasıllar", c_h1),
          P(", ".join(f"{n}" + (f" <font color='#5B6573'>(seçenekte ×{S['sec'][n]})</font>" if S["sec"].get(n) else "")
                      for n in hic) + ".", c_base),
          Spacer(1, 3),
          P("Bu fasıllar hap bölümünde kısa tutuldu; yine de seçeneklerde çeldirici olarak sık görülürler.", c_small)]
    return s


def hap_fasil(d, S):
    n = d["fasil"]
    ad = "Genel Yorum Kuralları" if n == 0 else f"Fasıl {n} · {FB.get(str(n), '')}"
    sayi = S["ana"].get(n, 0)
    rozet = f"<font color='#C9A227'><b>{d.get('kademe', '')}</b></font>"
    head = Table([[P(f"<b>{ad}</b>", c_h2),
                   P(f"{rozet}  <font color='#5B6573'>sınavda konu: {sayi} · seçenek: {S['sec'].get(n, 0)}</font>",
                     ParagraphStyle('r', parent=c_small, alignment=2))]],
                 colWidths=[W - 52 * mm, 52 * mm])
    head.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, 0), 0.9, NAVY), ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
                              ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                              ("BOTTOMPADDING", (0, 0), (-1, -1), 2), ("TOPPADDING", (0, 0), (-1, -1), 0)]))
    out = [head, Spacer(1, 3)]
    if d.get("sinavda"):
        out.append(cbox([P(f"<b>Sınavda:</b> {d['sinavda']}", c_cell)], CALLOUT_BG, NAVY, pad=3.5))
        out.append(Spacer(1, 3))
    first = out[:]
    rest = []
    pz = d.get("pozisyonlar") or []
    if pz:
        half = (len(pz) + 1) // 2 if len(pz) > 3 else len(pz)
        left, right = pz[:half], pz[half:]
        rows = []
        for i in range(half):
            a = left[i]
            b = right[i] if i < len(right) else ["", ""]
            rows.append([f"<b>{a[0]}</b>", a[1], f"<b>{b[0]}</b>", b[1]])
        if right:
            t = ctable(None, rows, [13 * mm, W / 2 - 13 * mm, 13 * mm, W / 2 - 13 * mm], bold_first=False)
        else:
            t = ctable(None, [[r[0], r[1]] for r in rows], [13 * mm, W - 13 * mm], bold_first=False)
        rest += [t, Spacer(1, 3)]
    if d.get("hap"):
        rest += [bullets(d["hap"], c_cell, left=9), Spacer(1, 3)]
    if d.get("karistirilan"):
        rows = [[k[0], f"<b>{k[1]}</b>", k[2]] for k in d["karistirilan"]]
        t = ctable(["Karıştırılan eşya", "Poz.", "Neden"], rows, [0.36 * W, 15 * mm, 0.64 * W - 15 * mm],
                   bold_first=False)
        rest += [cbox([t], WARN_BG, WARN, pad=2)]
    rest.append(Spacer(1, 8))
    return [KeepTogether(first + rest[:2])] + rest[2:]


def hap_story(S):
    s = [NextPageTemplate("normal"), PageBreak(), Marker("Hap Bilgiler", "Bölüm 2"),
         TocMark(0, "Bölüm 2 — 4’lü Pozisyonlarla Hap Bilgiler", "hap"),
         P("BÖLÜM 2", kicker), Spacer(1, 2), P("4’lü Pozisyonlarla Hap Bilgiler", title), Spacer(1, 3),
         P("Her fasılda: sınavda nasıl sorulduğu, en çok işe yarayan 4’lü pozisyonlar, notlardan hap kurallar ve "
           "karıştırılan eşya. Kademe harfi (A en çok sorulan) fasıla ayrılan yeri gösterir.", c_base),
         Spacer(1, 6)]
    files = {int(re.search(r"(\d\d)\.json$", f).group(1)): f for f in glob.glob(os.path.join(HAP, "fasil_*.json"))}
    if 0 in files:
        d = json.load(open(files[0], encoding="utf-8"))
        s += [TocMark(1, "Genel Yorum Kuralları", "h00")] + hap_fasil(d, S)
    for bi, b in enumerate(BOLUMLER):
        son = BOLUMLER[bi + 1]["ilk_fasil"] - 1 if bi + 1 < len(BOLUMLER) else 97
        fas = [n for n in range(b["ilk_fasil"], son + 1) if n in files]
        if not fas:
            continue
        bar = Table([[P(f"BÖLÜM {b['no']} — {b['baslik']}", c_bolum)]], colWidths=[W])
        bar.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), NAVY), ("TOPPADDING", (0, 0), (-1, -1), 3.5),
                                 ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5), ("LEFTPADDING", (0, 0), (-1, -1), 7)]))
        s += [CondPageBreak(55 * mm), Marker(f"Bölüm {b['no']} · {sentence(b['baslik'])}", "Hap Bilgiler"),
              TocMark(1, f"Bölüm {b['no']} — {sentence(b['baslik'])}", f"hb{b['no']}"), bar, Spacer(1, 5)]
        for n in fas:
            d = json.load(open(files[n], encoding="utf-8"))
            s += hap_fasil(d, S)
    return s


def opts_flow(opts):
    if all(len(re.sub("<[^>]+>", "", o)) <= 16 for o in opts):
        t = Table([[P(f"<b>{'ABCDE'[k]})</b> {o}", q_optc) for k, o in enumerate(opts)]],
                  colWidths=[(W - 12) / 5] * 5)
        t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 0),
                               ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
        w = Table([[t]], colWidths=[W])
        w.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 12), ("TOPPADDING", (0, 0), (-1, -1), 0),
                               ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
        return [w]
    return [P(f"<b>{'ABCDE'[k]})</b> {o}", q_opt) for k, o in enumerate(opts)]


def karma_story(tests):
    s = [NextPageTemplate("normal"), PageBreak(), Marker("Karma Testler", "Bölüm 3"),
         TocMark(0, "Bölüm 3 — Karma Testler", "karma"),
         P("BÖLÜM 3", kicker), Spacer(1, 2), P("Karma Testler", title), Spacer(1, 3),
         P(f"{len(tests)} test × 20 soru. Soru tipleri ve fasıl ağırlıkları son beş sınavın yoğunluğuna göre "
           "dağıtıldı; sorular kitabın ana bölümündeki ve deneme sınavlarındaki sorulardan ve çıkmış sorulardan "
           "bağımsızdır. Cevap anahtarı ve kısa gerekçeler kitabın sonundadır.", c_base), Spacer(1, 8)]
    for i, d in enumerate(tests):
        if i:
            s.append(PageBreak())
        s += [Marker(f"Karma Test {d['no']}", "Karma Testler"), TocMark(1, f"Karma Test {d['no']}", f"k{d['no']}"),
              P(f"KARMA TEST {d['no']}", kicker), Spacer(1, 1),
              P(f"20 soru · 5 şıklı · süre önerisi 25 dakika", c_small), Spacer(1, 5)]
        for j, q in enumerate(d["sorular"], 1):
            s.append(KeepTogether([P(f"<b>{j}-</b> {fix_stem(q['soru'])}", q_stem), Spacer(1, 1.5)]
                                  + opts_flow(q["secenekler"]) + [Spacer(1, 5.5)]))
    # cevaplar
    s += [PageBreak(), Marker("Karma Testler · Cevaplar", "Bölüm 3"),
          TocMark(1, "Cevap anahtarları ve gerekçeler", "kcev"),
          P("CEVAP ANAHTARLARI VE GEREKÇELER", kicker), Spacer(1, 4)]
    for d in tests:
        qs = d["sorular"]
        row1 = [P(f"<b>{j}-{q['cevap']}</b>", key_st) for j, q in enumerate(qs[:10], 1)]
        row2 = [P(f"<b>{j}-{q['cevap']}</b>", key_st) for j, q in enumerate(qs[10:], 11)]
        key = Table([row1, row2], colWidths=[W / 10] * 10)
        key.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), CALLOUT_BG), ("LINEBEFORE", (0, 0), (0, -1), 2.5, NAVY),
                                 ("TOPPADDING", (0, 0), (-1, -1), 1.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
                                 ("LEFTPADDING", (0, 0), (-1, -1), 6)]))
        items = []
        for j, q in enumerate(qs, 1):
            fz = q.get("fasil")
            lab = ("GYK" if str(fz).upper() in ("GYK", "0") else
                   "Tarife yapısı" if str(fz) == "Genel" else f"F.{fz}")
            items.append(P(f"<b>{j}-{q['cevap']}</b> <font color='#5B6573'>({lab})</font> {q['gerekce']} "
                           f"<font color='#5B6573'><i>{q['dayanak']}</i></font>", a_txt))
            items.append(Spacer(1, 2.2))
        s += [CondPageBreak(40 * mm), P(f"<b>Karma Test {d['no']}</b>", c_h2), Spacer(1, 2), key, Spacer(1, 3),
              BalancedColumns(items, nCols=2, innerPadding=8, leftPadding=0, rightPadding=0), Spacer(1, 7)]
    return s


# ---------------------------------------------------------------- kapaklar
def draw_cover(c, doc):
    c.saveState()
    c.setFillColor(NAVY_D)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.2)
    c.line(LM, PAGE_H - 30 * mm, PAGE_W - RM, PAGE_H - 30 * mm)
    c.setFillColor(GOLD)
    c.setFont("LS-B", 9)
    c.drawString(LM, PAGE_H - 25 * mm, "GÜMRÜK MÜŞAVİRLİĞİ SINAVINA HAZIRLIK · TARİFE")
    c.setFillColor(colors.white)
    c.setFont("LS-B", 50)
    c.drawString(LM - 2, PAGE_H - 72 * mm, "HAP BİLGİ")
    c.setFont("LS", 19)
    c.drawString(LM, PAGE_H - 86 * mm, "Türk Gümrük Tarife Cetveli")
    c.setFont("LS-B", 15)
    c.drawString(LM, PAGE_H - 96 * mm, "Son 5 Sınava Göre 4’lü Pozisyonlar ve Karma Testler")
    c.setFont("LS", 11.5)
    y = PAGE_H - 116 * mm
    for ln in COVER_LINES:
        c.setFillColor(GOLD)
        c.rect(LM, y + 1.2 * mm, 2.2 * mm, 2.2 * mm, stroke=0, fill=1)
        c.setFillColor(colors.HexColor("#E6ECF3"))
        c.drawString(LM + 6 * mm, y, ln)
        y -= 8 * mm
    # logo şeridi
    c.setFillColor(colors.white)
    c.roundRect(LM, 26 * mm, PAGE_W - LM - RM, 30 * mm, 3, stroke=0, fill=1)
    if os.path.exists(LOGO):
        from reportlab.lib.utils import ImageReader
        iw, ih = ImageReader(LOGO).getSize()
        lw = 120 * mm
        lh = lw * ih / iw
        c.drawImage(LOGO, (PAGE_W - lw) / 2, 26 * mm + (30 * mm - lh) / 2, lw, lh, mask="auto")
    c.restoreState()


COVER_LINES = []


def draw_back(c, doc):
    c.saveState()
    c.setFillColor(NAVY_D)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.2)
    c.line(LM, PAGE_H - 30 * mm, PAGE_W - RM, PAGE_H - 30 * mm)
    c.setFillColor(colors.white)
    c.setFont("LS-B", 24)
    c.drawString(LM, PAGE_H - 48 * mm, "HAP BİLGİ")
    c.setFont("LS", 11)
    c.setFillColor(colors.HexColor("#E6ECF3"))
    y = PAGE_H - 64 * mm
    from reportlab.lib.utils import simpleSplit
    for ln in simpleSplit(BACK_TEXT[0], "LS", 11, W):
        c.drawString(LM, y, ln)
        y -= 15.5
    y -= 10 * mm
    bw = W / len(BACK_STATS)
    for i, (n, lab) in enumerate(BACK_STATS):
        c.setFillColor(GOLD)
        c.setFont("LS-B", 22)
        c.drawString(LM + i * bw, y, str(n))
        c.setFillColor(colors.HexColor("#C9D3E0"))
        c.setFont("LS", 9)
        c.drawString(LM + i * bw, y - 6 * mm, lab)
    c.setFillColor(colors.white)
    c.roundRect(LM, 26 * mm, PAGE_W - LM - RM, 30 * mm, 3, stroke=0, fill=1)
    if os.path.exists(LOGO):
        from reportlab.lib.utils import ImageReader
        iw, ih = ImageReader(LOGO).getSize()
        lw = 120 * mm
        lh = lw * ih / iw
        c.drawImage(LOGO, (PAGE_W - lw) / 2, 26 * mm + (30 * mm - lh) / 2, lw, lh, mask="auto")
    c.restoreState()


BACK_TEXT = [""]
BACK_STATS = []


class HapBook(bb.Book):
    def __init__(self, fn, **kw):
        super().__init__(fn, **kw)
        for t in self.pageTemplates:
            if t.id == "cover":
                t.onPage = draw_cover
            if t.id == "back":
                t.onPage = draw_back


def main():
    out = sys.argv[1]
    A = analiz_yukle()
    S = istatistik(A)
    tests = [json.load(open(f, encoding="utf-8")) for f in sorted(glob.glob(os.path.join(KARMA, "karma_*.json")))]
    nq = sum(len(t["sorular"]) for t in tests)
    COVER_LINES[:] = [f"Son 5 sınavın {S['n']} sorusunun tip ve fasıl analizi",
                      "Soru tipi yoğunluğuna göre ağırlıklandırılmış hap bilgiler",
                      "Genel Yorum Kuralları ve Fasıl 1–97, 4’lü pozisyon düzeyi",
                      f"{len(tests)} karma test · {nq} yeni soru"]
    BACK_TEXT[0] = ("Bu kitap, son beş Gümrük Müşavirliği sınavındaki tarife sorularını tek tek sınıflandırır; "
                    "hangi fasılların, hangi soru kalıplarıyla, ne sıklıkta sorulduğunu gösterir. Hap bilgiler "
                    "4’lü pozisyon düzeyindedir ve sınavda en çok sorulan fasıllara daha fazla yer ayırır. "
                    "Karma testler, sınavdaki soru tipi yoğunluğuna göre hazırlanmış ve daha önce sorulmamış "
                    "sorulardan oluşur.")
    BACK_STATS[:] = [(S["n"], "incelenen sınav sorusu"), (98, "hap bilgi başlığı"), (len(tests), "karma test"),
                     (nq, "yeni soru")]
    story = [NextPageTemplate("cover"), Spacer(1, 1), NextPageTemplate("plain"), PageBreak()]
    toc = TableOfContents(dotsMinLevel=1)
    toc.levelStyles = [toc0, toc1]
    story += [Marker("İçindekiler", ""), P("İÇİNDEKİLER", ParagraphStyle("tt", parent=title, fontSize=18,
                                                                          spaceAfter=8)), Spacer(1, 4), toc]
    story += analiz_story(S)
    story += hap_story(S)
    if tests:
        story += karma_story(tests)
    story += [NextPageTemplate("back"), PageBreak(), Spacer(1, 1)]
    doc = HapBook(out, title="Hap Bilgi – Tarife (Son 5 Sınav)",
                  subject="Türk Gümrük Tarife Cetveli hap bilgileri ve karma testler", author="")
    doc.multiBuild(story)
    print("ok", out, "hap:", len(glob.glob(os.path.join(HAP, "fasil_*.json"))), "karma:", len(tests))


if __name__ == "__main__":
    main()
