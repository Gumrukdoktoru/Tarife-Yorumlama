import olefile, struct, sys
def extract(path):
    ole = olefile.OleFileIO(path)
    wd = ole.openstream('WordDocument').read()
    flags = struct.unpack_from('<H', wd, 0x0A)[0]
    table = '1Table' if flags & 0x0200 else '0Table'
    tb = ole.openstream(table).read()
    fcClx, lcbClx = struct.unpack_from('<II', wd, 0x01A2)
    clx = tb[fcClx:fcClx+lcbClx]
    i = 0
    while clx[i] == 1:
        cb = struct.unpack_from('<H', clx, i+1)[0]; i += 3 + cb
    assert clx[i] == 2
    lcb = struct.unpack_from('<I', clx, i+1)[0]
    plc = clx[i+5:i+5+lcb]
    n = (lcb - 4) // 12
    cps = struct.unpack_from('<%dI' % (n+1), plc, 0)
    out = []
    for k in range(n):
        pcd = plc[4*(n+1) + 8*k: 4*(n+1) + 8*k + 8]
        fc = struct.unpack_from('<I', pcd, 2)[0]
        cnt = cps[k+1] - cps[k]
        if fc & 0x40000000:
            off = (fc & ~0x40000000) // 2
            out.append(wd[off:off+cnt].decode('cp1254', 'replace'))
        else:
            out.append(wd[fc:fc+2*cnt].decode('utf-16le', 'replace'))
    t = ''.join(out)
    t = t.replace('\r', '\n').replace('\x07', ' | ').replace('\x0b', '\n').replace('\x0c', '\n')
    return t
print(extract(sys.argv[1]))
