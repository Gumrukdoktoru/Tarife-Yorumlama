# Tarife Kitabı – kaynak dosyalar

- `data/fasil_00.json` (GYK) ve `data/fasil_01–97.json`: fasıl modülleri (ders notu blokları + 25 soru)
- `data/deneme_01–10.json`: 50'şer soruluk denemeler
- `build_book.py`: kitabı PDF olarak dizer → `python3 build_book.py Tarife_Kitabi.pdf`
- `validate.py`: veri dosyalarını kurallara göre denetler
- `son_kontrol.py`: tekrar eden çıkmış soru örneklerini ve benzer deneme sorularını bulur
- `SPEC.md`, `DENEME_SPEC.md`: modül ve deneme yazım kuralları
- `doc2txt.py`: FASILnn.doc dosyalarından metin çıkarır (kaynak/fasillar için)

## Hap Bilgi Kitabı (son 5 sınava göre)
- `kaynak/son5_analiz.json`: son 5 Gümrük Müşavirliği sınavının 123 tarife sorusunun tip/fasıl sınıflandırması
- `kaynak/karma_dagilimi.json`: fasıl kademeleri (A/B/C) ve 10×20 karma test yuvaları
- `hap/fasil_00–97.json`: 4’lü pozisyon düzeyinde hap bilgiler
- `karma/karma_01–10.json`: 20’şer soruluk karma testler
- `build_hap.py`: kitabı dizer → `python3 build_hap.py Hap_Bilgi_Kitabi.pdf`
- `son_kontrol.py --karma`: karma soruları önceki tüm sorularla (modül, deneme, pilot, çıkmış, diğer karma) karşılaştırır
