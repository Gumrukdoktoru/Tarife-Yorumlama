#!/usr/bin/env python3
"""son_kontrol.py --deneme-siki'nin işaretlediği (aynı eşya + aynı cevap) deneme sorularını yenileriyle değiştirir.

Her yeni soru eskisinin fasıl etiketini, tipini ve cevap harfini korur (her harf 10 dengesi bozulmaz).
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")

# (deneme no, soru no 1'den başlar) -> yeni soru
YENI = {
 (2, 1): {
  "soru": "Tarife Cetveline göre, yumurtadan yeni çıkmış canlı evcil ördek yavruları (palazlar) hangi pozisyonda sınıflandırılır?",
  "secenekler": ["01.06", "01.05", "04.07", "02.07", "05.11"],
  "cevap": "B",
  "tip": "Eşya → 4’lü pozisyon",
  "gerekce": "Bölüm I Not 1’e göre bu bölümde bir hayvan cins veya türüne yapılan atıf, metinde aksi belirtilmedikçe o türün yavrusunu da kapsar; 01.05 pozisyon metni evcil ördekleri ismen saydığından palazlar da bu pozisyondadır ve pozisyon içinde ağırlığı 185 gramı geçmeyen kanatlılar ayrıca gösterilmiştir. 01.06 ise yabani ördekler gibi 01.05’te ismen geçmeyen kuşları kapsar. Döllenmiş kuluçkalık yumurtalar 04.07’de yer alsa da yumurtadan çıkmış yavrular canlı hayvandır; 02.07 kümes hayvanlarının etlerini, 05.11 ise insan tüketimine uygun olmayan ölü hayvanları kapsar.",
  "dayanak": "Bölüm I Not 1; 01.05 pozisyon metni ve Açıklama Notu; 04.07 Açıklama Notu.",
  "fasil": 1,
 },
 (3, 50): {
  "soru": "Bir otomotiv yan sanayi firması; kaide üzerine monte edilmiş, insan koluna benzer mafsallı yapıda, elektrik motorlarıyla hareket eden ve programlanabilen bir sanayi robotu ithal etmektedir. Robot, kıskaçlı tutucusuyla ağır döküm parçalarını bir taşıyıcı banttan kaldırıp diğerine yüklemek ve boşaltmak üzere özel olarak imal edilmiştir; farklı aletler takılarak başka işlerde kullanılamamaktadır. Tarife Cetveline göre bu robot hangi pozisyonda sınıflandırılır?",
  "secenekler": ["84.79", "85.15", "84.28", "84.24", "84.26"],
  "cevap": "C",
  "tip": "Senaryo",
  "gerekce": "84.79 Açıklama Notu bu pozisyona yalnızca farklı aletler kullanılarak çeşitli basit işlevleri yerine getirebilen sanayi robotlarını alır; belirli bir işlevi yerine getirmek üzere özel olarak imal edilmiş robotlar gördükleri işleve göre sınıflandırılır. 84.28 Açıklama Notu da kaldırma, yükleme, boşaltma vb. işleri yapmak üzere özel olarak imal edilmiş sanayi robotlarını bu pozisyonda sayar. 85.15 kaynak yapan, 84.24 toz veya sıvı püskürten robotlar içindir; 84.26 ise vinçler ve hareketli kaldırma çerçeveleri gibi makineleri kapsar ve robotları saymaz.",
  "dayanak": "84.24, 84.28 ve 84.79 Açıklama Notları; 85.15 Açıklama Notu.",
  "fasil": 84,
 },
 (4, 7): {
  "soru": "Tarife Cetveline göre, durum buğdayı irmiğinden yapılan hamuruna renk ve aroma vermek amacıyla kakao tozu katılmış; pişirilmemiş, doldurulmamış ve kurutulmuş erişte (tagliatelle) hangi pozisyonda sınıflandırılır?",
  "secenekler": ["18.06", "19.01", "19.02", "19.05", "21.06"],
  "cevap": "C",
  "tip": "Eşya → 4’lü pozisyon",
  "gerekce": "Fasıl 18 Not 1(b), 19.02 pozisyonunda yer alan müstahzarları kakao içerseler bile bu fasıl dışında bırakır; bu nedenle kakao içeren gıda müstahzarlarını 18.06’ya veren hüküm bu makarnaya uygulanmaz. 19.02 Açıklama Notuna göre makarna hamuru renk ve aroma verici maddelerle karıştırılabilir ve kurutulmuş erişte (tagliatelle) bu pozisyonda sayılır. 19.01 tarifenin başka yerinde belirtilmeyen un esaslı müstahzarları kapsadığından ismen yer alan makarnaya uygulanmaz; ürün fırınlanmış bir ekmekçilik ürünü olmadığından 19.05’e, genel nitelikli 21.06’ya da gidilmez.",
  "dayanak": "Fasıl 18 Not 1(b); 19.02 pozisyon metni ve Açıklama Notu.",
  "fasil": 18,
 },
 (4, 27): {
  "soru": "Tarife Cetveline göre, şeker, glikoz şurubu, tereyağı ve yoğunlaştırılmış sütün birlikte pişirilmesiyle elde edilen; kakao içermeyen, tek tek ambalajlanmış ve olduğu gibi yenmeye hazır sütlü karamel şekerlemeler hangi pozisyonda sınıflandırılır?",
  "secenekler": ["17.02", "19.01", "21.06", "18.06", "17.04"],
  "cevap": "E",
  "tip": "Eşya → 4’lü pozisyon",
  "gerekce": "17.04 Açıklama Notu, olduğu gibi yenilmeye elverişli şekercilik mamulleri arasında karamelleri ismen sayar; ürün kakao içermediğinden 18.06’ya gitmez. 17.02’deki “karamel” ise şekerlerin veya melasın 120–180 °C’de uzun süre ısıtılmasıyla elde edilen, aroma veya renk verici olarak kullanılan esmer maddedir ve şekerleme değildir. Esasında süt ürünleri bulunsa da 19.01 Açıklama Notu şeker mamulleri karakterine sahip ürünleri bu pozisyon dışında bırakarak 17.04’e gönderir; 21.06 ise doğrudan şekerlemeye dönüştürülmeye uygun olmayan yağlı ezmeler gibi ürünler içindir.",
  "dayanak": "17.02 ve 17.04 Açıklama Notları; 19.01 Açıklama Notu.",
  "fasil": 17,
 },
 (4, 41): {
  "soru": "Tarife Cetveline göre, arı mumu ile parafin mumu karışımının terebentin esansı içinde eritilmesiyle hazırlanmış, ahşap mobilya ve parkelerin parlatılması ve korunmasında kullanılan macun kıvamındaki cila hangi pozisyonda sınıflandırılır?",
  "secenekler": ["34.04", "15.21", "38.09", "34.05", "27.12"],
  "cevap": "D",
  "tip": "Eşya → 4’lü pozisyon",
  "gerekce": "Farklı mumların karışımları Fasıl 34 Not 5(b) uyarınca 34.04’teki müstahzar mumlar arasında yer alsa da aynı Notun istisna hükmü, sıvı bir ortamda karıştırılmış, dağıtılmış veya eritilmiş mumları 34.04 dışında bırakır. 34.05 Açıklama Notu, terebentin esansı emdirilmiş mumlardan oluşan cilaları mobilya ve döşeme cilaları arasında örnek olarak sayar. 15.21 karıştırılmamış bitkisel ve hayvansal mumları, 27.12 parafin gibi mineral mumları kapsar; 38.09 ise mensucat, kâğıt ve deri sanayiinde kullanılan apre ve finisaj müstahzarları içindir.",
  "dayanak": "Fasıl 34 Not 5; 34.04 ve 34.05 Açıklama Notları.",
  "fasil": 34,
 },
 (5, 17): {
  "soru": "Tarife Cetveline göre, iç lastiklerin onarımında kullanılmak üzere hazırlanmış, vulkanize kauçuk bir mesnet üzerinde kendi kendine vulkanize olan bir kauçuk tabakasından ibaret, kenarları şevlenmiş dikdörtgen yamalar hangi pozisyonda sınıflandırılır?",
  "secenekler": ["40.16", "40.08", "40.13", "40.12", "35.06"],
  "cevap": "A",
  "tip": "Eşya → 4’lü pozisyon",
  "gerekce": "40.16 Açıklama Notu, iç lastik onarımı için kenarları şevlenmiş dikdörtgen veya kalıplanarak ya da kesilerek elde edilmiş yamaları, genellikle vulkanize kauçuk mesnet üzerinde kendi kendine vulkanize olan bir kauçuk tabakasından ibaret oldukları belirtilerek bu pozisyonda sayar. Kenarları şevlenerek basit dikdörtgen kesimin ötesinde işlem gördüğünden Fasıl 40 Not 9’daki levha ve şerit tanımına uymaz ve 40.08’e girmez. İç lastikte kullanılması onu 40.13’e, lastikle ilgili olması da 40.12’deki sırt ve kolanlara götürmez; ürün 35.06’daki hazır yapıştırıcılardan biri değil, bitmiş bir kauçuk eşyadır.",
  "dayanak": "Fasıl 40 Not 9; 40.16 Açıklama Notu.",
  "fasil": 40,
 },
 (7, 19): {
  "soru": "Tarife Cetveline göre, havuç ve kereviz sularının karıştırılmasıyla hazırlanmış; fermente edilmemiş, alkol ve ilave su katılmamış, yalnızca tuz ve baharat eklenmiş sebze suyu hangi pozisyonda sınıflandırılır?",
  "secenekler": ["20.05", "22.02", "20.09", "21.06", "20.02"],
  "cevap": "C",
  "tip": "Eşya → 4’lü pozisyon",
  "gerekce": "20.09 pozisyonu fermente edilmemiş ve alkol katılmamış sebze sularını kapsar; Açıklama Notu bu sebze sularının ilave tuz, baharat veya aroma maddesi içerebileceğini ve farklı tipteki sebze suları karışımlarının da bu pozisyonda yer aldığını belirtir. 20.05 Açıklama Notu sebze sularını açıkça bu pozisyon dışında bırakarak 20.09’a gönderir. Ürüne normal oranı aşan su katılmadığından 22.02’deki seyreltilmiş içecek karakterini taşımaz; domates suyu içermediğinden kuru madde oranına bağlı 20.02 kuralı da söz konusu olmaz.",
  "dayanak": "Fasıl 20 Not 6; 20.05 ve 20.09 Açıklama Notları.",
  "fasil": 20,
 },
}


def main():
    by_file = {}
    for (no, sn), q in YENI.items():
        by_file.setdefault(no, []).append((sn, q))
    for no, items in sorted(by_file.items()):
        path = os.path.join(DATA, f"deneme_{no:02d}.json")
        d = json.load(open(path, encoding="utf-8"))
        for sn, q in items:
            eski = d["sorular"][sn - 1]
            for k in ("fasil", "tip", "cevap"):
                assert eski[k] == q[k], f"deneme {no} soru {sn}: {k} uyuşmuyor ({eski[k]!r} ≠ {q[k]!r})"
            d["sorular"][sn - 1] = q
            print(f"deneme {no} soru {sn} değiştirildi")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
