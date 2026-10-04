#!/usr/bin/env python3
"""Tarife kitabını data/*.json dosyalarından PDF olarak dizer.

Kullanım: python3 build_book.py cikti.pdf [--fasil 1,2,3] [--denemesiz]
"""
import json
import os
import re
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.utils import simpleSplit
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Flowable, Frame, KeepTogether, ListFlowable,
                                ListItem, NextPageTemplate, PageBreak, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle, CondPageBreak)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.environ.get("BOOK_DATA", os.path.join(ROOT, "data"))
FD = "/usr/share/fonts/truetype/liberation/"
pdfmetrics.registerFont(TTFont("LS", FD + "LiberationSans-Regular.ttf"))
pdfmetrics.registerFont(TTFont("LS-B", FD + "LiberationSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("LS-I", FD + "LiberationSans-Italic.ttf"))
pdfmetrics.registerFont(TTFont("LS-BI", FD + "LiberationSans-BoldItalic.ttf"))
pdfmetrics.registerFontFamily("LS", normal="LS", bold="LS-B", italic="LS-I", boldItalic="LS-BI")
pdfmetrics.registerFont(TTFont("DVS-B", "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"))

NAVY = colors.HexColor("#1F3A5F")
NAVY_D = colors.HexColor("#16304F")
GOLD = colors.HexColor("#C9A227")
INK = colors.HexColor("#1E2329")
MUTED = colors.HexColor("#5B6573")
RULE = colors.HexColor("#D5DAE1")
HEAD_BG = colors.HexColor("#E8EDF3")
ZEBRA = colors.HexColor("#F6F8FA")
CALLOUT_BG = colors.HexColor("#EEF3F9")
WARN = colors.HexColor("#A15C07")
WARN_BG = colors.HexColor("#FDF4E7")
OK = colors.HexColor("#2E7D4F")
OK_BG = colors.HexColor("#EAF5EE")

PAGE_W, PAGE_H = A4
LM = RM = 18 * mm
TM, BM = 18 * mm, 18 * mm
W = PAGE_W - LM - RM

base = ParagraphStyle("base", fontName="LS", fontSize=9.4, leading=13.0, textColor=INK)
small = ParagraphStyle("small", parent=base, fontSize=8.2, leading=11, textColor=MUTED)
kicker = ParagraphStyle("kicker", parent=base, fontName="LS-B", fontSize=8.6, leading=11, textColor=GOLD)
title = ParagraphStyle("title", parent=base, fontName="LS-B", fontSize=19, leading=23.5, textColor=NAVY)
subtitle = ParagraphStyle("subtitle", parent=base, fontSize=10.5, leading=14, textColor=MUTED)
h1 = ParagraphStyle("h1", parent=base, fontName="LS-B", fontSize=12, leading=15.5, textColor=NAVY,
                    spaceBefore=12, spaceAfter=5)
h2 = ParagraphStyle("h2", parent=base, fontName="LS-B", fontSize=10.2, leading=13.5, textColor=NAVY,
                    spaceBefore=4, spaceAfter=3)
cell = ParagraphStyle("cell", parent=base, fontSize=8.5, leading=11.2)
cell_b = ParagraphStyle("cell_b", parent=cell, fontName="LS-B")
cell_h = ParagraphStyle("cell_h", parent=cell, fontName="LS-B", textColor=NAVY)
big = ParagraphStyle("big", parent=base, fontName="LS-B", fontSize=10.2, leading=14.2, textColor=NAVY)
qstem = ParagraphStyle("qstem", parent=base, fontSize=9.6, leading=13.4)
opt = ParagraphStyle("opt", parent=base, fontSize=9.4, leading=12.8, leftIndent=14)
optc = ParagraphStyle("optc", parent=base, fontSize=9.4, leading=12.8)
toc0 = ParagraphStyle("toc0", parent=base, fontName="LS-B", fontSize=10, leading=13, textColor=NAVY,
                      spaceBefore=7, leftIndent=0, rightIndent=16)
toc1 = ParagraphStyle("toc1", parent=base, fontSize=9, leading=11.6, leftIndent=14, firstLineIndent=0,
                      rightIndent=16)
tocmark0 = ParagraphStyle("tocmark0", parent=base, fontSize=0.1, leading=0.1, textColor=colors.white)


def tr_lower(s):
    return s.replace("I", "ı").replace("İ", "i").lower()


def sentence(s):
    s = re.sub(r"\s+", " ", s).strip()
    low = tr_lower(s)
    return low[:1].upper() + low[1:] if low else low


def P(t, s=base):
    return Paragraph(t, s)


def bullets(items, style=base, left=11):
    return ListFlowable([ListItem(P(t, style), leftIndent=left, value="•") for t in items],
                        bulletType="bullet", start="•", leftIndent=left, bulletFontName="LS",
                        bulletFontSize=style.fontSize)


def box(flowables, bg, bar, pad=8):
    t = Table([[flowables]], colWidths=[W])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg), ("LINEBEFORE", (0, 0), (0, -1), 3, bar),
                           ("TOPPADDING", (0, 0), (-1, -1), pad), ("BOTTOMPADDING", (0, 0), (-1, -1), pad),
                           ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10)]))
    return t


def table(header, rows, widths, bold_first=True):
    data = [[P(c, cell_h) for c in header]]
    for r in rows:
        data.append([P(r[0], cell_b if bold_first else cell)] + [P(c, cell) for c in r[1:]])
    t = Table(data, colWidths=widths, repeatRows=1)
    ts = [("BACKGROUND", (0, 0), (-1, 0), HEAD_BG), ("LINEBELOW", (0, 0), (-1, 0), 0.8, NAVY),
          ("LINEBELOW", (0, 1), (-1, -1), 0.4, RULE), ("VALIGN", (0, 0), (-1, -1), "TOP"),
          ("TOPPADDING", (0, 0), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
          ("LEFTPADDING", (0, 0), (-1, -1), 4.5), ("RIGHTPADDING", (0, 0), (-1, -1), 4.5)]
    for i in range(1, len(data)):
        if i % 2 == 0:
            ts.append(("BACKGROUND", (0, i), (-1, i), ZEBRA))
    t.setStyle(TableStyle(ts))
    return t


class Marker(Flowable):
    """Sayfa üst bilgisini ayarlar (görünmez)."""

    def __init__(self, left, right=""):
        super().__init__()
        self.left, self.right = left, right

    def wrap(self, aw, ah):
        return 0, 0

    def draw(self):
        self.canv._hdr = (self.left, self.right)


class TocMark(Paragraph):
    """İçindekilere girdi bırakan görünmez paragraf."""

    def __init__(self, level, text, key):
        super().__init__("&nbsp;", tocmark0)
        self._toc = (level, text, key)


# ---------------------------------------------------------------- sayfa şablonları
def draw_header_footer(c, doc):
    c.saveState()
    left, right = getattr(c, "_hdr", ("", ""))
    c.setFont("LS", 7.6)
    c.setFillColor(MUTED)
    if left:
        if len(left) > 105:
            left = left[:105].rsplit(" ", 1)[0].rstrip(";,") + "…"
        c.drawString(LM, PAGE_H - 11 * mm, left)
    if right:
        c.drawRightString(PAGE_W - RM, PAGE_H - 11 * mm, right)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.5)
    c.line(LM, PAGE_H - 12.5 * mm, PAGE_W - RM, PAGE_H - 12.5 * mm)
    c.line(LM, 12.5 * mm, PAGE_W - RM, 12.5 * mm)
    c.setFont("LS-B", 8)
    c.setFillColor(NAVY)
    c.drawCentredString(PAGE_W / 2, 8 * mm, str(doc.page))
    c.restoreState()


def draw_cover(c, doc):
    c.saveState()
    c.setFillColor(NAVY_D)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    # ince altın çizgiler
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.2)
    c.line(LM, PAGE_H - 30 * mm, PAGE_W - RM, PAGE_H - 30 * mm)
    c.line(LM, 34 * mm, PAGE_W - RM, 34 * mm)
    # fasıl numarası ızgarası (dekor)
    c.setFont("LS-B", 7)
    c.setFillColor(colors.HexColor("#2C4C75"))
    x0, y0 = LM, 48 * mm
    for i in range(1, 98):
        col, row = (i - 1) % 14, (i - 1) // 14
        c.drawString(x0 + col * (W / 14), y0 + (6 - row) * 7 * mm, f"{i:02d}")
    c.setFillColor(GOLD)
    c.setFont("LS-B", 9)
    c.drawString(LM, PAGE_H - 25 * mm, "GÜMRÜK MÜŞAVİRLİĞİ VE GÜMRÜK MÜŞAVİR YARDIMCILIĞI SINAVLARINA HAZIRLIK")
    c.setFillColor(colors.white)
    c.setFont("LS-B", 64)
    c.drawString(LM - 2, PAGE_H - 75 * mm, "TARİFE")
    c.setFont("LS", 17)
    c.drawString(LM, PAGE_H - 90 * mm, "Türk Gümrük Tarife Cetveli")
    c.setFont("LS-B", 17)
    c.drawString(LM, PAGE_H - 100 * mm, "Ders Notları ve Sınav Soruları")
    c.setFillColor(colors.HexColor("#C9D3E0"))
    c.setFont("LS", 11.5)
    lines = ["Genel Yorum Kuralları ve Fasıl 1–97",
             "Her fasılda on bloklu ders notu ve 25 soru",
             f"{STATS[2][0]} deneme sınavı · {STATS[3][0]} soru",
             "4’lü tarife pozisyonu düzeyi"]
    y = PAGE_H - 120 * mm
    for ln in lines:
        c.setFillColor(GOLD)
        c.rect(LM, y + 1.2 * mm, 2.2 * mm, 2.2 * mm, stroke=0, fill=1)
        c.setFillColor(colors.HexColor("#E6ECF3"))
        c.drawString(LM + 6 * mm, y, ln)
        y -= 8 * mm
    c.restoreState()


STATS = [("98", "modül"), ("2.425", "fasıl sorusu"), ("10", "deneme"), ("500", "deneme sorusu")]


def fmt_n(n):
    return f"{n:,}".replace(",", ".")


def draw_back(c, doc):
    c.saveState()
    c.setFillColor(NAVY_D)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.2)
    c.line(LM, PAGE_H - 30 * mm, PAGE_W - RM, PAGE_H - 30 * mm)
    c.setFillColor(colors.white)
    c.setFont("LS-B", 26)
    c.drawString(LM, PAGE_H - 50 * mm, "TARİFE")
    c.setFont("LS", 12)
    c.setFillColor(colors.HexColor("#C9D3E0"))
    c.drawString(LM, PAGE_H - 58 * mm, "Ders Notları ve Sınav Soruları")
    text = ("Bu kitap, Türk Gümrük Tarife Cetvelinin Genel Yorum Kurallarını ve 97 faslını aynı on bloklu yapıyla "
            "ele alır: 30 saniyede öz, karar tablosu, 4’lü pozisyon haritası, notlar ve eşikler, sınır komşuları, "
            "tuzak noktalar, hafıza kancası, çıkmış sorularda baz alınan noktalar, çıkmış soru örnekleri ve "
            "60 saniyelik özet. Her fasıl, çıkmış soruların tarzında hazırlanmış 25 soru ile cevap anahtarı ve "
            "gerekçelerle biter. Kitabın sonunda tüm tarifeyi kapsayan, fasıl sorularından bağımsız 10 deneme "
            "sınavı yer alır.")
    c.setFont("LS", 11)
    c.setFillColor(colors.HexColor("#E6ECF3"))
    y = PAGE_H - 80 * mm
    for ln in simpleSplit(text, "LS", 11, W):
        c.drawString(LM, y, ln)
        y -= 15.5
    y -= 10 * mm
    stats = STATS
    bw = W / 4
    for i, (n, lab) in enumerate(stats):
        x = LM + i * bw
        c.setFillColor(GOLD)
        c.setFont("LS-B", 24)
        c.drawString(x, y, n)
        c.setFillColor(colors.HexColor("#C9D3E0"))
        c.setFont("LS", 9.5)
        c.drawString(x, y - 6 * mm, lab)
    c.restoreState()


def draw_divider(c, doc):
    c.saveState()
    c.setFillColor(NAVY_D)
    c.rect(0, 0, 62 * mm, PAGE_H, stroke=0, fill=1)
    c.setFillColor(GOLD)
    c.rect(62 * mm, 0, 1.6 * mm, PAGE_H, stroke=0, fill=1)
    c.restoreState()


class Book(BaseDocTemplate):
    def __init__(self, fn, **kw):
        super().__init__(fn, pagesize=A4, leftMargin=LM, rightMargin=RM, topMargin=TM, bottomMargin=BM, **kw)
        normal = Frame(LM, BM, W, PAGE_H - TM - BM, id="n", leftPadding=0, rightPadding=0,
                       topPadding=0, bottomPadding=0)
        full = Frame(LM, BM, W, PAGE_H - TM - BM, id="f")
        div = Frame(75 * mm, BM, PAGE_W - 75 * mm - RM, PAGE_H - TM - BM, id="d", leftPadding=0,
                    rightPadding=0)
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[full], onPage=draw_cover),
            PageTemplate(id="plain", frames=[normal]),
            PageTemplate(id="normal", frames=[normal], onPageEnd=draw_header_footer),
            PageTemplate(id="divider", frames=[div], onPage=draw_divider),
            PageTemplate(id="back", frames=[full], onPage=draw_back),
        ])

    def afterFlowable(self, f):
        t = getattr(f, "_toc", None)
        if t:
            level, text, key = t
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(re.sub("<[^>]+>", "", text), key, level=level, closed=(level == 0))
            self.notify("TOCEntry", (level, text, self.page, key))


# ---------------------------------------------------------------- içerik
B = json.load(open(os.path.join(ROOT, "kaynak", "basliklar.json"), encoding="utf-8"))
FB = B["fasil_basliklari"]
BOLUMLER = B["bolumler"]
BOLUM_BY_FIRST = {b["ilk_fasil"]: b for b in BOLUMLER}


def bolum_of(n):
    cur = None
    for b in BOLUMLER:
        if b["ilk_fasil"] <= n:
            cur = b
    return cur


BLOK_ADLARI = ["30 saniyede öz", "Karar tablosu", "Pozisyon haritası (4’lü)", "Notlar, tanımlar ve eşikler",
               "Sınır komşuları", "Tuzak noktalar", "Hafıza kancası", "Çıkmış sorularda baz alınanlar",
               "Çıkmış soru örnekleri", "60 saniyelik özet"]


def block_head(i, name):
    return P(f'<font color="#5B6573">BLOK {i}</font>  ·  {name}', h1)


def options_flow(opts, letters="ABCDE"):
    if all(len(re.sub("<[^>]+>", "", o)) <= 16 for o in opts):
        n = len(opts)
        cells = [P(f"<b>{letters[i]})</b> {o}", optc) for i, o in enumerate(opts)]
        t = Table([cells], colWidths=[(W - 14) / n] * n)
        t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (0, 0), 14), ("LEFTPADDING", (1, 0), (-1, -1), 0),
                               ("TOPPADDING", (0, 0), (-1, -1), 1), ("BOTTOMPADDING", (0, 0), (-1, -1), 1)]))
        return [t]
    return [P(f"<b>{letters[i]})</b> {o}", opt) for i, o in enumerate(opts)]


ROMAN_STMT = re.compile(r"\s+(?=(?:I|II|III|IV|V)\.\s)")


def fix_stem(t):
    """Çoktan-çoğa sorularında I–IV önermelerini ayrı satıra alır."""
    if "<br/>" in t or not (re.search(r"(^|\s)I\.\s", t) and re.search(r"(^|\s)II\.\s", t)):
        return t
    return ROMAN_STMT.sub("<br/>", t)


def question_flow(i, q):
    parts = [P(f"<b>{i}-</b> {fix_stem(q['soru'])}", qstem), Spacer(1, 2.5)]
    parts += options_flow(q["secenekler"])
    parts.append(Spacer(1, 8))
    return KeepTogether(parts)


def answer_key(qs, per_row=5):
    rows, row = [], []
    for i, q in enumerate(qs, 1):
        row.append(P(f"<b>{i}-{q['cevap']}</b>", big))
        if len(row) == per_row:
            rows.append(row)
            row = []
    if row:
        rows.append(row + [""] * (per_row - len(row)))
    t = Table(rows, colWidths=[W / per_row] * per_row)
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), CALLOUT_BG), ("LINEBEFORE", (0, 0), (0, -1), 3, NAVY),
                           ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                           ("LEFTPADDING", (0, 0), (-1, -1), 10)]))
    return t


def answers_flow(qs, extra_fasil=False):
    out = []
    for i, q in enumerate(qs, 1):
        head = f"<b>{i}- Doğru Cevap: {q['cevap']}</b>"
        if extra_fasil and q.get("fasil") not in (None, ""):
            fz = q["fasil"]
            lab = "Genel Yorum Kuralları" if str(fz).upper() in ("GYK", "0") else f"Fasıl {fz}"
            head += f'  <font color="#5B6573" size="8">· {lab}</font>'
        out.append(KeepTogether([
            P(head, qstem), Spacer(1, 1.5),
            P(f"<b>Gerekçe:</b> {q['gerekce']}"), Spacer(1, 1.5),
            P(f"<b>Dayanak:</b> <i>{q['dayanak']}</i>"), Spacer(1, 7)]))
    return out


def module_story(d):
    n = d["fasil"]
    giris = d.get("tur") == "giris"
    if giris:
        label, ttl, bol = "GİRİŞ", "Tarifenin yorumu ile ilgili genel kurallar", None
    else:
        label = f"FASIL {n}"
        ttl = FB.get(str(n)) or d.get("baslik", "")
        bol = bolum_of(n)
    hdr_left = "Genel Yorum Kuralları" if giris else f"Fasıl {n} · {re.sub('<[^>]+>', '', ttl)}"
    hdr_right = "" if giris else f"Bölüm {bol['no']}"
    s = [NextPageTemplate("normal"), PageBreak(), Marker(hdr_left, hdr_right)]
    s.append(TocMark(0 if giris else 1, ("Genel Yorum Kuralları" if giris else f"Fasıl {n} — {ttl}"),
                     f"m{n:02d}"))
    s += [P(label, kicker), Spacer(1, 3), P(ttl, title), Spacer(1, 4)]
    if bol:
        s.append(P(f"Bölüm {bol['no']} — {sentence(bol['baslik'])}", subtitle))
    s.append(Spacer(1, 4))
    if d.get("sakli"):
        s.append(box([P(d.get("aciklama", ""), big)], CALLOUT_BG, NAVY))
        return s

    # Blok 1
    s.append(block_head(1, BLOK_ADLARI[0]))
    s.append(box([P(d["oz"]["vurgu"], big)], CALLOUT_BG, NAVY))
    s.append(Spacer(1, 5))
    s.append(bullets(d["oz"]["maddeler"]))
    # Blok 2
    kt = d["karar_tablosu"]
    s.append(CondPageBreak(45 * mm))
    s.append(block_head(2, BLOK_ADLARI[1]))
    if kt.get("aciklama"):
        s += [P(kt["aciklama"]), Spacer(1, 4)]
    s.append(table(["Sıra", "Soru", "Sonuç"], kt["satirlar"], [11 * mm, 0.58 * (W - 11 * mm), 0.42 * (W - 11 * mm)]))
    if kt.get("dipnot"):
        s += [Spacer(1, 3), P(kt["dipnot"], small)]
    # Blok 3
    s.append(CondPageBreak(45 * mm))
    s.append(block_head(3, "Kuralların haritası" if giris else BLOK_ADLARI[2]))
    hdr = d.get("pozisyon_haritasi_basliklar") or ["Pozisyon", "Kapsam", "Ayırt edici anahtar", "Tipik sınav eşyası"]
    s.append(table(hdr, d["pozisyon_haritasi"], [19 * mm, 0.30 * (W - 19 * mm), 0.37 * (W - 19 * mm), 0.33 * (W - 19 * mm)]))
    # Blok 4
    s.append(CondPageBreak(40 * mm))
    s.append(block_head(4, BLOK_ADLARI[3]))
    s.append(table(["Kaynak", "Hüküm"], d["notlar"], [34 * mm, W - 34 * mm]))
    # Blok 5
    s.append(CondPageBreak(40 * mm))
    s.append(block_head(5, "Sık karıştırılan durumlar" if giris else BLOK_ADLARI[4]))
    hdr5 = d.get("sinir_komsulari_basliklar") or ["Eşya", "Pozisyon", "Neden"]
    s.append(table(hdr5, d["sinir_komsulari"], [0.42 * W, 0.17 * W, 0.41 * W]))
    # Blok 6
    s.append(CondPageBreak(45 * mm))
    s.append(block_head(6, BLOK_ADLARI[5]))
    s.append(box([bullets(d["tuzaklar"], cell)], WARN_BG, WARN))
    # Blok 7
    s.append(KeepTogether([block_head(7, BLOK_ADLARI[6]), P(f"<b>{d['hafiza']['kanca']}</b>"), Spacer(1, 3),
                           P(d["hafiza"]["aciklama"])]))
    # Blok 8
    s.append(KeepTogether([block_head(8, BLOK_ADLARI[7]),
                           P("Çıkmış sorularda bu konu ile ilgili şunlar baz alınmıştır:"), Spacer(1, 3),
                           bullets(d["sinav_odagi"])]))
    # Blok 9
    if d.get("cikmis_ornekler"):
        s.append(CondPageBreak(50 * mm))
        s.append(block_head(9, BLOK_ADLARI[8]))
        for j, e in enumerate(d["cikmis_ornekler"], 1):
            inner = [P(f"<b>Örnek {j}.</b> {fix_stem(e['soru'])}", qstem), Spacer(1, 2)]
            inner += [P(f"<b>{'ABCDE'[k]})</b> {o}", optc) for k, o in enumerate(e["secenekler"])]
            inner += [Spacer(1, 3), P(f"<b>Cevap: {e['cevap']}</b> — {e['aciklama']}", cell)]
            s.append(KeepTogether([box(inner, OK_BG, OK), Spacer(1, 5)]))
        ozet_no = 10
    else:
        ozet_no = 9
    # Blok 10
    s.append(KeepTogether([block_head(ozet_no, BLOK_ADLARI[9]), bullets(d["ozet"])]))

    # Sorular
    qs = d["sorular"]
    s += [PageBreak(), P(f"{label} · SORULAR", kicker), Spacer(1, 2),
          P(f"{len(qs)} Soru · 5 Şıklı (A–E)", subtitle), Spacer(1, 8)]
    for i, q in enumerate(qs, 1):
        s.append(question_flow(i, q))
    # Cevaplar
    s += [PageBreak(), P(f"{label} · CEVAP ANAHTARI VE GEREKÇELER", kicker), Spacer(1, 6), answer_key(qs), Spacer(1, 8)]
    s += answers_flow(qs)
    return s


def divider_story(b, fasillar):
    s = [NextPageTemplate("divider"), PageBreak(), TocMark(0, f"Bölüm {b['no']} — {sentence(b['baslik'])}", f"b{b['no']}"),
         Spacer(1, 40 * mm), P("BÖLÜM", kicker), Spacer(1, 2),
         P(b["no"], ParagraphStyle("roman", parent=title, fontName="DVS-B", fontSize=54, leading=62)), Spacer(1, 8),
         P(b["baslik"], ParagraphStyle("btitle", parent=title, fontSize=15, leading=20)), Spacer(1, 14)]
    rows = [[P(f"<b>Fasıl {n}</b>", cell), P(FB.get(str(n), ""), cell)] for n in fasillar]
    t = Table(rows, colWidths=[22 * mm, PAGE_W - 75 * mm - RM - 22 * mm])
    t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 0.4, RULE), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                           ("LEFTPADDING", (0, 0), (-1, -1), 0)]))
    s.append(t)
    return s


def deneme_story(d):
    no = d["no"]
    qs = d["sorular"]
    s = [NextPageTemplate("normal"), PageBreak(), Marker(f"Deneme Sınavı {no}", "Denemeler"),
         TocMark(1, f"Deneme Sınavı {no}", f"d{no:02d}"),
         P(f"DENEME SINAVI {no}", kicker), Spacer(1, 3), P(f"Deneme {no}", title), Spacer(1, 3),
         P(f"{len(qs)} Soru · 5 Şıklı (A–E) · Tüm tarife", subtitle), Spacer(1, 10)]
    for i, q in enumerate(qs, 1):
        s.append(question_flow(i, q))
    s += [PageBreak(), Marker(f"Deneme Sınavı {no} · Cevaplar", "Denemeler"),
          P(f"DENEME {no} · CEVAP ANAHTARI VE GEREKÇELER", kicker), Spacer(1, 6), answer_key(qs, 10), Spacer(1, 8)]
    s += answers_flow(qs, extra_fasil=True)
    return s


def main():
    out = sys.argv[1]
    only = None
    if "--fasil" in sys.argv:
        only = {int(x) for x in sys.argv[sys.argv.index("--fasil") + 1].split(",")}
    denemesiz = "--denemesiz" in sys.argv
    mods = {}
    for n in range(0, 98):
        p = os.path.join(DATA, f"fasil_{n:02d}.json")
        if os.path.exists(p) and (only is None or n in only):
            mods[n] = json.load(open(p, encoding="utf-8"))
    denemeler = []
    if not denemesiz:
        for k in range(1, 11):
            p = os.path.join(DATA, f"deneme_{k:02d}.json")
            if os.path.exists(p):
                denemeler.append(json.load(open(p, encoding="utf-8")))

    global STATS
    STATS = [(str(len(mods)), "modül"),
             (fmt_n(sum(len(m.get("sorular", [])) for m in mods.values())), "fasıl sorusu"),
             (str(len(denemeler)), "deneme"),
             (fmt_n(sum(len(d["sorular"]) for d in denemeler)), "deneme sorusu")]
    story = [NextPageTemplate("cover"), Spacer(1, 1), NextPageTemplate("plain"), PageBreak()]
    # İçindekiler
    toc = TableOfContents(dotsMinLevel=1)
    toc.levelStyles = [toc0, toc1]
    story += [P("İÇİNDEKİLER", ParagraphStyle("tt", parent=title, fontSize=20, spaceAfter=10)), Spacer(1, 6), toc]
    if 0 in mods:
        story += module_story(mods[0])
    for b_i, b in enumerate(BOLUMLER):
        first = b["ilk_fasil"]
        last = (BOLUMLER[b_i + 1]["ilk_fasil"] - 1) if b_i + 1 < len(BOLUMLER) else 97
        fas = [n for n in range(first, last + 1)]
        present = [n for n in fas if n in mods]
        if not present:
            continue
        story += divider_story(b, fas)
        for n in present:
            story += module_story(mods[n])
    if denemeler:
        story += [NextPageTemplate("divider"), PageBreak(), TocMark(0, "Deneme Sınavları", "denemeler"),
                  Spacer(1, 40 * mm), P("TÜM TARİFE", kicker), Spacer(1, 2),
                  P("Deneme Sınavları", ParagraphStyle("dt", parent=title, fontSize=30, leading=36)), Spacer(1, 10),
                  P(f"{len(denemeler)} deneme · her biri 50 soru · fasıl sorularından bağımsız. Cevap anahtarı ve "
                    "gerekçeler her denemenin arkasındadır.", subtitle)]
        for d in denemeler:
            story += deneme_story(d)
    story += [NextPageTemplate("back"), PageBreak(), Spacer(1, 1)]
    doc = Book(out, title="Tarife – Ders Notları ve Sınav Soruları",
               subject="Türk Gümrük Tarife Cetveli, Genel Yorum Kuralları ve Fasıl 1–97", author="")
    doc.multiBuild(story)
    print("ok", out, "modül:", len(mods), "deneme:", len(denemeler))


if __name__ == "__main__":
    main()
