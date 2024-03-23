from math import sqrt, ceil
from PIL import Image

def fti(bits):
    z = sqrt(len(bits))
    x, y = int(ceil(z)), int(ceil(z))
    im = Image.new('L', (x, y))
    for idx, i in enumerate(bits):
        im.putpixel((idx%x,(idx//x)%y), i*255)
    return im

def main():
    with open(fn := (input("File: ")), 'rb') as f:
        n = f.read()
    r = 1 if input('reverse order?(y,n) ')=='y' else 0
    m = []
    if r:
        for i in n:
            for x in range(8):
                m.append((i//2**(x))%2)
    else:
        for i in n:
            for x in range(8):
                m.append((i//2**(7-x))%2)

    fti(m).save(fn+'.png')


if __name__ == '__main__':
    main()
