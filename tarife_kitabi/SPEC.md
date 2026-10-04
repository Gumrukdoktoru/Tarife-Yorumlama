# TARİFE KİTABI – FASIL MODÜLÜ YAZIM KURALLARI

You are writing one or more chapter modules ("fasıl modülü") for a Turkish customs-tariff study book
(Türk Gümrük Tarife Cetveli, Fasıl 1–97). The book is for the Gümrük Müşavirliği / Gümrük Müşavir
Yardımcılığı exam. Every module is a JSON file that a renderer turns into PDF pages. All content is in
**Turkish**.

Root folder (call it KITAP): `/tmp/claude-0/-home-user-Tarife-Yorumlama/897bdcf6-ad3f-5910-9875-e3a0942c3912/scratchpad/kitap`

## Inputs
- `KITAP/kaynak/fasillar/FASILnn.txt` — full official text of each chapter: Bölüm notları (in the first
  chapter of each section), Fasıl notları, Alt pozisyon notları, pozisyon metinleri and the Turkish
  Explanatory Notes (Açıklama Notları / İzahname). **This is your only content source.**
  Big files (e.g. 28, 29, 84, 85, 90) can be read in parts; use `grep -n` for heading lines
  (`^\s*NN\.NN`) and for "hariç", "kapsamaz", "dahil değildir", "Not" etc.
- `KITAP/kaynak/gyk.txt` — Genel Yorum Kuralları (only for the GYK module).
- `KITAP/kaynak/kisaltmalar.txt` — official table of contents, abbreviations and symbols.
- `KITAP/kaynak/basliklar.json` — official chapter titles (`fasil_basliklari`, sentence case) and
  section list (`bolumler`: no, ilk_fasil, baslik).
- `KITAP/kaynak/cikmis_sorular.json` — 236 past exam questions: `no`, `metin` (question + options),
  `cevap` (official answer letter), `fasillar` (auto-detected chapters, incomplete — also search
  `metin` yourself for your chapter's 4-digit headings like "03.06", chapter-number mentions like
  "3. fasıl", and typical goods names of the chapter).
- `KITAP/ornek_fasil_03.json` — a worked example of the format (it only has 3 questions; a real module
  needs 25). Match its tone, density and markup.

## Absolute rules
1. **Notes only.** Use only what is in the tariff texts above. No tax rates, no trade-policy measures,
   no legislation (474 sayılı Kanun, BTB, İthalat Rejimi, etc.), no national/CN codes, no outside facts,
   no names/brands, no file names, no "repo", no past-question numbers.
2. **4-digit level only.** Headings are written `NN.NN` (e.g. `03.06`, `84.71`). Never write 6-digit
   subheadings (`0302.91`, `8471.30`), or any longer code, anywhere — not in notes, not in options, not in
   explanations. Chapter numbers ("Fasıl 16") and section numbers ("Bölüm XV") are fine. If a past
   question's original options are 6-digit or longer, do not use it as an example.
3. **No years.** Never write a calendar year (no "2022", no "HS 2022", no exam year). Remove any year
   from past-question text you quote ("2022 yılı Türk Gümrük Tarife Cetveli’nin" → "Türk Gümrük Tarife
   Cetveli’nin").
4. **Accuracy first.** Every statement, every correct answer and every "why the distractor is wrong"
   must be supported by the chapter text. If a sentence of the Turkish text looks garbled or
   mistranslated, do not build a question on it. If unsure whether an item belongs to a heading, do not
   use that item.
5. **Markup.** Strings are rendered by ReportLab. Allowed inline tags: `<b>…</b>`, `<i>…</i>` and the line break `<br/>` (use it to put I–IV statements of a Çoktan-çoğa question on separate lines).
   Never use a bare `<` or `>`; write "&" as `&amp;`. Allowed special characters: → • – — “ ” ’ ≠ ≤ ≥ ° % ·
   Do not use ✓ ✗ ▸ ★ ■ or emoji.
6. Do not put "A)" etc. inside option strings; the renderer adds letters.

## JSON format (one file per chapter: `KITAP/data/fasil_NN.json`, two digits)
```
{
 "tur": "fasil",              // "giris" only for the GYK module
 "fasil": 3,                  // int; 0 for GYK
 "baslik": "...",             // official title from basliklar.json fasil_basliklari (sentence case)
 "bolum": "I",                // Roman numeral of the section ("" for GYK)
 "oz": {"vurgu": "1–3 sentences: the core test of the chapter", "maddeler": [3–5 bullets]},
 "karar_tablosu": {"aciklama": "...", "satirlar": [["1","question","→ heading(s)"], ... 5–12 rows], "dipnot": "" or "* ..."},
 "pozisyon_haritasi": [["NN.NN","short scope","distinguishing key","typical exam goods"], ...],   // EVERY 4-digit heading of the chapter, in order
 "notlar": [["Bölüm X Not n" | "Fasıl N Not n" | "Genel Açıklamalar" | "NN.NN Açıklama Notu", "rule in plain Turkish"], ...],
 "sinir_komsulari": [["goods","NN.NN (or NN.NN / NN.NN)","why"], ... 8–15 rows],   // goods that look like this chapter but go elsewhere (and vice versa)
 "tuzaklar": [6–10 bullets, each starting with a bold one-line trap: "<b>…</b> explanation"],
 "hafiza": {"kanca": "short mnemonic", "aciklama": "1–3 sentences"},
 "sinav_odagi": [4–7 bullets],        // see "Past-exam blocks"
 "cikmis_ornekler": [1–2 items {"soru","secenekler":[4 or 5],"cevap":"B","aciklama":"1–2 sentences"}],
 "ozet": [5–7 bullets: the 60-second summary],
 "sorular": [25 questions, see below]
}
```
Section notes: if your chapter is the **first chapter of a section** (1, 6, 15, 16, 25, 28, 39, 41, 44,
47, 50, 64, 68, 71, 72, 84, 86, 90, 93, 94, 97), put every Bölüm note first in `notlar` ("Bölüm XI Not 1",
…). Otherwise mention a section note only if it matters for the chapter.
Long chapters (many headings): keep each `pozisyon_haritasi` cell short (2–8 words) but list all headings.
`notlar`: cover every Fasıl note (summarised faithfully; keep numbers, percentages, dimensions and
definitions exactly), then the most exam-relevant definitions/thresholds from the Explanatory Notes.
Skip subheading notes unless they define a term used at heading level (and never cite a subheading code).

## Past-exam blocks
- `sinav_odagi` (rendered under the heading "Çıkmış sorularda bu konuda şunlar baz alınmıştır"): 4–7
  bullets describing what past questions tested for this chapter (concepts, typical goods, traps,
  question patterns such as "hangisi bu fasılda yer almaz", "farklı pozisyon", definitions, GYK use).
  Base them on the actual past questions that concern your chapter (directly, or with your chapter's
  headings among the options). If very few concern it, say so in the first bullet ("Bu fasıl çıkmış
  sorularda daha çok seçeneklerde/çeldirici olarak yer almıştır") and describe how it appeared.
- `cikmis_ornekler`: 1–2 past questions shown as examples: copy the stem and the original options
  (fix obvious OCR glitches, remove years, keep meaning), give the official answer letter from `cevap`,
  and a 1–2 sentence explanation grounded in the notes. Only use a question whose official answer is
  still correct under the current text and whose options are 4-digit headings, chapter numbers or
  words. If none concerns your chapter at all, use one from a neighbouring chapter of the same section
  that involves your chapter's goods; if there is truly nothing suitable, use an empty list.

## The 25 questions (`sorular`)
Each item: `{"soru": str, "secenekler": [5 strings], "cevap": "A".."E", "tip": str, "gerekce": str, "dayanak": str}`
- Style: modelled on recent exam questions ("Tarife Cetveline göre …", 5 options A–E). Negations in bold:
  `<b>sınıflandırılmaz</b>`, `<b>yer almaz</b>`, `<b>yanlıştır</b>`, `<b>değildir</b>`.
- Type mix (±1 where the chapter has no material for a type):
  - 6 × "Eşya → 4’lü pozisyon" (options are 5 headings, e.g. "03.06")
  - 4 × "Olumsuz teşhis" ("hangisi … faslında/pozisyonunda <b>sınıflandırılmaz</b>?")
  - 4 × "Farklı/aynı pozisyon veya fasıl" ("hangisi diğerlerinden farklı bir pozisyonda/fasılda yer alır?")
  - 4 × "Fasıl notu · Tanım/Eşik" (definitions, percentages, dimensions, criteria from the notes)
  - 1 × "Genel Yorum Kuralı" (user rule: GYK questions are 3–5 % of all questions, so 1 of 25; which GYK classifies a goods of this chapter; sets, unfinished/unassembled, mixtures)
  - 2 × "Eşleştirme / Boşluk doldurma"
  - 2 × "Çoktan-çoğa (I–IV)" (statements I–IV in the stem; options like "I ve II", "I, II ve IV")
  - 2 × "Senaryo" (a described product with several features; one heading)
- **Answer distribution: exactly 5 × A, 5 × B, 5 × C, 5 × D, 5 × E.** Spread them irregularly.
- Options: plausible, same category and similar length; the correct one must not be systematically the
  longest; no "Hepsi"/"Hiçbiri". Distractors should come from the chapter's exclusion lists, neighbouring
  headings and look-alike goods in other chapters.
- Exactly one correct option. Re-check every distractor against the text.
- Do not copy past questions; new goods/wording (concepts may repeat).
- `gerekce`: 2–4 sentences: why the answer is right, why the tempting distractors are wrong, the trap.
- `dayanak`: e.g. "Fasıl 3 Not 1; 03.06 Açıklama Notu." / "Bölüm XV Not 7." / "GYK 3(b)."
- `tip`: one of the type names above.

## Procedure
1. Read your chapter text(s) fully (big ones in parts) and the related past questions.
2. Write the JSON with a Python script (`json.dump(obj, f, ensure_ascii=False, indent=1)`) to
   `KITAP/data/fasil_NN.json`. Keep your generator script in `KITAP/uret/` if you use one.
3. Run `python3 KITAP/validate.py KITAP/data/fasil_NN.json` and fix every error until it prints `OK`.
   Review the warnings too.
4. Self-check pass: re-read all 25 questions against the text; confirm one correct answer each, the
   letter counts (5 each), no 6-digit codes, no years.
5. Final reply: list the files written and any doubts (≤10 lines). Do not paste the JSON.
