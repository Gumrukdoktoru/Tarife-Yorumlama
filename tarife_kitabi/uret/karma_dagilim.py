#!/usr/bin/env python3
"""Son 5 sınav analizinden hap kademelerini ve 10×20 karma test yuvalarını üretir."""
import json, math, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import build_hap as bh

A = bh.analiz_yukle(); S = bh.istatistik(A)
w = {f: 2 * S['ana'].get(f, 0) + S['sec'].get(f, 0) for f in range(0, 98)}

# --- hap kademeleri
kademe = {}
for f in range(0, 98):
    kademe[f] = 'A' if w[f] >= 8 or f == 0 else ('B' if w[f] >= 4 else 'C')
kademe[77] = 'C'

# --- tip kotaları (200 soru, son 5 sınav tarife sorularına orantılı)
N = 200
tip = dict(S['tip'])
GYK_PAY = 0.05  # kullanıcı kuralı: GYK soruları toplamın %3–5'i
top = sum(tip.values())
raw = {t: N * c / top for t, c in tip.items()}
kota = {t: math.floor(v) for t, v in raw.items()}
for t in sorted(raw, key=lambda t: -(raw[t] - kota[t]))[:N - sum(kota.values())]:
    kota[t] += 1

# GYK kotasını %5'e indir, artanı diğer tiplere oranla dağıt
hedef = round(N * GYK_PAY)
fazla = kota['Genel Yorum Kuralı'] - hedef
if fazla > 0:
    kota['Genel Yorum Kuralı'] = hedef
    diger_raw = {t: fazla * c / (top - tip['Genel Yorum Kuralı']) for t, c in tip.items() if t != 'Genel Yorum Kuralı'}
    ek = {t: math.floor(v) for t, v in diger_raw.items()}
    for t in sorted(diger_raw, key=lambda t: -(diger_raw[t] - ek[t]))[:fazla - sum(ek.values())]:
        ek[t] += 1
    for t, v in ek.items():
        kota[t] += v

# --- fasıl yuvaları (GYK ve Tarife yapısı dışındaki tipler)
n_gyk = kota['Genel Yorum Kuralı']; n_yapi = kota['Tarife yapısı']
R = N - n_gyk - n_yapi
fas = [f for f in range(1, 98) if w[f] > 0]
yuva = {f: 1 for f in fas}
kalan = R - len(fas)
tw = sum(w[f] for f in fas)
rawf = {f: kalan * w[f] / tw for f in fas}
for f in fas:
    yuva[f] += math.floor(rawf[f])
for f in sorted(fas, key=lambda f: -(rawf[f] - math.floor(rawf[f])))[:R - sum(yuva.values())]:
    yuva[f] += 1

# --- tiplerin fasıl yuvalarına dağıtımı
diger = {t: k for t, k in kota.items() if t not in ('Genel Yorum Kuralı', 'Tarife yapısı')}
slots = []
for f in sorted(fas, key=lambda f: -yuva[f]):
    used = []
    for _ in range(yuva[f]):
        aday = sorted(diger, key=lambda t: (t in used, -diger[t]))
        t = next(t for t in aday if diger[t] > 0)
        diger[t] -= 1; used.append(t)
        slots.append((f, t))
slots += [('GYK', 'Genel Yorum Kuralı')] * n_gyk + [('Genel', 'Tarife yapısı')] * n_yapi
assert len(slots) == N, len(slots)

# --- 10 teste dağıt: aynı fasıl bir testte tekrar etmesin, tipler dengeli olsun
random.seed(7)
random.shuffle(slots)
slots.sort(key=lambda s: -(w.get(s[0], 0) if isinstance(s[0], int) else 50))
tests = [[] for _ in range(10)]
for f, t in slots:
    def cost(T):
        return (len(T) >= 20, sum(1 for x in T if x[0] == f) * 3 + sum(1 for x in T if x[1] == t), len(T))
    min(tests, key=cost).append((f, t))
assert all(len(T) == 20 for T in tests)
out = {'kademe': kademe, 'agirlik': w, 'tip_kota': kota,
       'testler': {str(i + 1): [[f, t] for f, t in sorted(T, key=lambda x: (str(x[0]).zfill(3)))] for i, T in enumerate(tests)}}
json.dump(out, open(os.path.join(bh.KAY, 'karma_dagilimi.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
from collections import Counter
print('kademe', Counter(kademe.values()), 'A:', [f for f in kademe if kademe[f] == 'A'])
print('tip kota', kota)
print('en çok yuva', sorted(((yuva[f], f) for f in fas), reverse=True)[:12])
for i, T in enumerate(tests, 1):
    c = Counter(str(x[0]) for x in T)
    print(i, 'tekrar eden fasıl:', {k: v for k, v in c.items() if v > 1 and k not in ('GYK', 'Genel')}, 'GYK', c['GYK'], 'yapı', c['Genel'])
