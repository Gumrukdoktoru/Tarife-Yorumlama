# HAP BİLGİ KİTABI – KARMA TEST YAZIM KURALLARI

You are writing one 20-question mixed test ("karma test") for a Turkish customs-tariff pocket summary book.
KITAP = `/tmp/claude-0/-home-user-Tarife-Yorumlama/897bdcf6-ad3f-5910-9875-e3a0942c3912/scratchpad/kitap`.

First read `KITAP/SPEC.md` (Absolute rules: notes only, 4-digit level only, no years, accuracy first, markup,
no letters inside options). They apply unchanged.

## The rule of this book: model the LAST 5 EXAMS, never repeat a question
- `KITAP/kaynak/son5_analiz.json` + `KITAP/kaynak/son5_ozet.json`: classified questions of the last 5 exams
  (tip, kalip = stem pattern, konu, pozisyonlar). **Write your questions in the same stem patterns and
  difficulty as these exam questions** (e.g. "Tarife Cetveline göre … hangi pozisyonda sınıflandırılır?",
  "Aşağıdakilerden hangisi … faslında yer almaz?", "… hangisi diğerlerinden farklı bir fasılda yer alır?",
  "… tarife cetvelindeki sıraya göre doğru dizilişi hangisidir?"). Full texts: `KITAP/kaynak/cikmis_sorular.json`.
- **Never repeat an existing question**: not the past exam questions, not the 2,425 module questions
  (`KITAP/data/fasil_NN.json → sorular`), not the 500 deneme questions (`KITAP/data/deneme_KK.json`), not the
  other karma tests (`KITAP/karma/karma_*.json`, some are being written in parallel). Before writing a
  question on chapter N, skim the module and deneme stems for chapter N and choose different goods / a
  different angle. Concepts may repeat; goods + wording must not.

## GYK share (user rule)
- Genel Yorum Kuralı questions must be **3–5 %** of all questions: in a 20-question karma test exactly **1** GYK question.

## Content
- 20 questions, one per slot given in your prompt (slot = chapter + question type). Order: mixed sections,
  rough easy→hard.
- Question types (`tip`, exactly these names): "Eşya → 4’lü pozisyon", "Pozisyon → eşya", "Olumsuz teşhis",
  "Farklı/aynı pozisyon veya fasıl", "Fasıl/Bölüm bulma", "Fasıl notu · Tanım/Eşik", "Genel Yorum Kuralı",
  "Sıralama", "Çoktan-çoğa / Eşleştirme", "Senaryo", "Tarife yapısı".
  - "Sıralama": 4–5 goods; options are orderings like "II – IV – I – III"; order = ascending heading number.
  - "Fasıl/Bölüm bulma": options are chapter numbers ("Fasıl 62") or section numerals ("Bölüm XI").
  - "Tarife yapısı": only about the structure of the nomenclature at heading/chapter/section level
    (number of sections/chapters, what a 4-digit heading is, how chapter notes/section notes work, the
    position of a chapter in a section). No 6-digit codes, no legislation.
- 5 options A–E, exactly one correct. **Answer distribution: exactly 4 × A, 4 × B, 4 × C, 4 × D, 4 × E**,
  irregular sequence.
- Each question: `{"soru","secenekler":[5],"cevap","tip","gerekce","dayanak","fasil"}`; `fasil` int or "GYK".
- `gerekce`: 1–2 sentences, ≤ 45 words (≤ 420 characters): why the answer is right + the trap.
  `dayanak`: e.g. "Fasıl 95 Not 1(…); 95.03 Açıklama Notu." / "GYK 3(b)."

## Output
- `KITAP/karma/karma_KK.json` (two digits): `{"tur":"karma","no":K,"sorular":[...20...]}`, written by a
  Python script `KITAP/uret/karma_KK.py` (json.dump ensure_ascii=False, indent=1).
- `python3 KITAP/validate.py KITAP/karma/karma_KK.json` → must print OK.
- `cd KITAP && python3 son_kontrol.py --karma` → rewrite any of YOUR questions flagged (similarity ≥ 0.50),
  keeping letter, fasil and tip; repeat until none of yours is flagged.
- Self-check every answer and every distractor against the chapter text.
- Final reply: file written + doubts (≤ 6 lines).
