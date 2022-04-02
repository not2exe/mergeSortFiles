import os
def mergeSortFiles(n, sizep):
    a = [i for i in open("A.txt", encoding='utf-8')]
    b = open("B.txt", "w", encoding='utf-8')
    c = open("C.txt", "w", encoding='utf-8')

    i = 0
    while i < len(a):
        j = 0
        while i < len(a) and j < sizep:
            b.write(a[i])
            i += 1
            j += 1
        j = 0
        while i < len(a) and j < sizep:
            c.write(a[i])
            i += 1
            j += 1

    os.system(r'nul>A.txt')

    b.close()
    c.close()
    merge(n, sizep)


def merge(n, sizep):
    a = open("A.txt", "w", encoding='utf-8')
    b = [i for i in open("B.txt", encoding='utf-8')]
    c = [i for i in open("C.txt", encoding='utf-8')]
    ib = 0
    ic = 0

    while ib < len(b) and ic < len(c):
        i, j = 0, 0
        while ib < len(b) and ic < len(c) and i < sizep and j < sizep:
            if int(b[ib][0]) < int(c[ic][0]):
                a.write(b[ib])
                i += 1
                ib += 1
            else:
                a.write(c[ic])
                j += 1
                ic += 1
        while ib < len(b) and i < sizep:
            a.write(b[ib])
            i += 1
            ib += 1
        while ic < len(c) and j < sizep:
            a.write(c[ic])
            j += 1
            ic += 1
    while ib < len(b):
        a.write(b[ib])
        ib += 1
    while ic < len(b):
        a.write(c[ic])
        ic += 1

    os.system(r'nul>B.txt')
    os.system(r'nul>C.txt')

    a.close()
    if sizep == n:
        return
    mergeSortFiles(n, sizep * 2)


mergeSortFiles(32, 1)
