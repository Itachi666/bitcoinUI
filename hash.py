import hashlib
import sys

def hash():
    #if len(sys.argv) != 2:
     #   sys.exit('Usage: %s file' % sys.argv[0])

    filename = '1.pdf'       #sys.argv[1]
    m = hashlib.sha256()
    with open(filename, 'rb') as fp:
        while True:
            blk = fp.read(4096) # 4KB per block
            if not blk: break
            m.update(blk)

    m.update(str(1235))
    k=m.hexdigest()
    print m.hexdigest(), filename
    print int(k,16)

if __name__ == '__main__':
    main()