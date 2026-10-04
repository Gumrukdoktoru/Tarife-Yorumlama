# TARİFE KİTABI – DENEME SINAVI YAZIM KURALLARI

You are writing one 50-question practice exam ("deneme sınavı") for a Turkish customs-tariff study book.
KITAP = `/tmp/claude-0/-home-user-Tarife-Yorumlama/897bdcf6-ad3f-5910-9875-e3a0942c3912/scratchpad/kitap`.

First read `KITAP/SPEC.md` (the chapter-module rules). Its **Absolute rules** (notes only, 4-digit level
only, no years, accuracy first, markup, no letters inside options) apply here unchanged.

## Sources
- `KITAP/kaynak/fasillar/FASILnn.txt` — chapter texts (your only content source); `KITAP/kaynak/gyk.txt` for GYK.
- `KITAP/data/fasil_NN.json` — the finished chapter modules. Read the relevant module's notes blocks
  to orient yourself quickly, **but your questions must be independent of the module questions**:
  before writing a question on chapter N, read the stems in `fasil_NN.json → sorular` and use different
  goods, different wording and preferably a different angle. Do not copy past exam questions either
  (`KITAP/kaynak/cikmis_sorular.json`).
- `KITAP/kaynak/deneme_dagilimi.json` — which chapters each deneme must draw from (see your prompt).

## Content of one deneme
- 50 questions, all chapters/sections as allocated in your prompt (one question per allocated slot;
  "GYK" slots are Genel Yorum Kuralları questions using goods from any chapter). A slot's question must be
  answered mainly by that chapter's notes; cross-chapter questions ("hangisi farklı fasılda yer alır")
  are welcome — tag them with the slot's chapter.
- Type mix across the 50 (±2): 11 "Eşya → 4’lü pozisyon", 8 "Olumsuz teşhis", 8 "Farklı/aynı pozisyon
  veya fasıl", 7 "Fasıl notu · Tanım/Eşik", 6 "Genel Yorum Kuralı" (the 5 GYK slots + 1), 3 "Eşleştirme /
  Boşluk doldurma", 3 "Çoktan-çoğa (I–IV)", 4 "Senaryo".
- Order: mix sections (do not group by chapter); keep a rough easy→hard flow.
- **Answer distribution: exactly 10 × A, 10 × B, 10 × C, 10 × D, 10 × E**, irregular sequence.
- Each question: `{"soru","secenekler":[5],"cevap","tip","gerekce","dayanak","fasil"}` where `fasil` is an
  int chapter number, or the string "GYK".
- `gerekce` 2–4 sentences (why right, why tempting distractors are wrong); `dayanak` like
  "Fasıl 84 Not 5; 84.71 Açıklama Notu." or "GYK 3(b)."

## Output
- File: `KITAP/data/deneme_KK.json` (two digits) with `{"tur":"deneme","no":K,"sorular":[...50...]}`,
  written via Python `json.dump(..., ensure_ascii=False, indent=1)`.
- Run `python3 KITAP/validate.py KITAP/data/deneme_KK.json` until it prints OK.
- Self-check: one correct option per question (verify every distractor against the text), letter counts
  10 each, no 6-digit codes, no years, no overlap with the module questions of the same chapters.
- Final reply: file written + doubts (≤8 lines).
