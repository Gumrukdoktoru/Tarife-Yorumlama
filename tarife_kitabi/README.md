# Tarife Kitabı – kaynak dosyalar

- `data/fasil_00.json` (GYK) ve `data/fasil_01–97.json`: fasıl modülleri (ders notu blokları + 25 soru)
- `data/deneme_01–10.json`: 50'şer soruluk denemeler
- `build_book.py`: kitabı PDF olarak dizer → `python3 build_book.py Tarife_Kitabi.pdf`
- `validate.py`: veri dosyalarını kurallara göre denetler
- `son_kontrol.py`: tekrar eden çıkmış soru örneklerini ve benzer deneme sorularını bulur
- `SPEC.md`, `DENEME_SPEC.md`: modül ve deneme yazım kuralları
- `doc2txt.py`: FASILnn.doc dosyalarından metin çıkarır (kaynak/fasillar için)
