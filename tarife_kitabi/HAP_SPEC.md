# HAP BİLGİ KİTABI – FASIL SAYFASI YAZIM KURALLARI

You are writing chapter entries for a compact Turkish customs-tariff **pocket summary book** ("Hap Bilgi
Kitabı", max 100 pages in total for 97 chapters + GYK + analysis + 200 test questions). Every word must earn
its place. All content in **Turkish**.

KITAP = `/tmp/claude-0/-home-user-Tarife-Yorumlama/897bdcf6-ad3f-5910-9875-e3a0942c3912/scratchpad/kitap`

## Sources
- `KITAP/data/fasil_NN.json` — the finished, verified chapter modules (oz, karar_tablosu, pozisyon_haritasi,
  notlar, sinir_komsulari, tuzaklar, ozet). **Your main source**: condense it. Check anything you add or
  rephrase against `KITAP/kaynak/fasillar/FASILnn.txt` (official chapter text). GYK: `KITAP/kaynak/gyk.txt`
  and `KITAP/data/fasil_00.json`.
- `KITAP/kaynak/son5_analiz.json` — the classified questions of the **last 5 exams** (one record per question:
  kapsam, tip, fasil_ana, fasil_secenek, pozisyonlar, konu, kalip, cevap_gecerli). Use the records whose
  `fasil_ana` or `fasil_secenek` contains your chapter to write `sinavda` and to choose what to emphasise.
  The full question text is in `KITAP/kaynak/cikmis_sorular.json` (same `no`).

## Absolute rules (same as the main book)
1. Notes only: only what the tariff texts say. No tax rates, no legislation, no national/CN codes, no years,
   no question numbers, no file names.
2. **4-digit level only**: headings as `NN.NN`. Never a 6-digit or longer code.
3. Accuracy first; skip garbled sentences of the Turkish text.
4. Markup: only `<b>…</b>`, `<i>…</i>`, `<br/>`; write `&amp;` for &; no bare `<` `>`.
   Allowed special characters: → • – — “ ” ’ ≠ ≤ ≥ ° % ·  (no ✓ ✗ ★ ■ or emoji).

## JSON: `KITAP/hap/fasil_NN.json` (two digits; `fasil_00.json` = GYK)
```
{
 "tur": "hap",
 "fasil": 84,                       // int, 0 for GYK
 "kademe": "A" | "B" | "C",         // given in your prompt (exam weight tier)
 "sinavda": "1–2 sentences: what the last 5 exams asked about this chapter and HOW (pattern), e.g.
             'Son 5 sınavda 6 kez: 84.71/85.28 ayrımı, 84.79 artık pozisyon ve Not 2 (84.19 istisnaları) …'.
             If never asked: 'Son 5 sınavda doğrudan sorulmadı; …' and say if it appeared among options.",
 "pozisyonlar": [["NN.NN", "≤ 8 words: scope + key"], ...],      // the most exam-relevant headings, in order
 "hap": ["<b>Key phrase:</b> ≤ 30 words of rule/threshold/definition", ...],
 "karistirilan": [["goods (≤ 8 words)", "NN.NN", "≤ 12 words: why / not NN.NN"], ...]
}
```
Sizes by tier (strict — the page budget depends on it):
| kademe | pozisyonlar | hap | karistirilan |
|---|---|---|---|
| A (most asked) | 8–12 | 6–8 | 4–6 |
| B | 4–6 | 4–5 | 2–3 |
| C | 2–4 | 2–3 | 1–2 |

Content priorities: (1) what the last 5 exams tested, (2) chapter/section notes with numbers, percentages,
dimensions, definitions, (3) exclusions that send goods elsewhere, (4) look-alike goods in other chapters.
Prefer facts a candidate can use to answer "hangi pozisyonda / hangisi yer almaz / hangisi farklı" questions.
Fasıl 77 (saklı): `{"tur":"hap","fasil":77,"kademe":"C","sinavda":"Saklı fasıl.","pozisyonlar":[],"hap":["…one sentence…"],"karistirilan":[]}`.

## Procedure
1. For each of your chapters: read the module JSON, the son5_analiz records for the chapter, then write.
2. Write all files with one Python script (json.dump ensure_ascii=False, indent=1); keep it in
   `KITAP/uret/hap_<your group>.py`.
3. Run `python3 KITAP/validate.py KITAP/hap/fasil_NN.json ...` until every file prints OK; fix warnings about
   long bullets.
4. Final reply: files written + doubts (≤ 6 lines).
