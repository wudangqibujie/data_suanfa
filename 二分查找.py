def erfencha(q,de):
    lo = 0
    hi = len(q)-1
    while hi>=lo:
        mi = int((lo+hi)/2)
        if q[mi] == de:
            return True
        elif q[mi] < de:
            print(q[mi])
            lo = mi+1
        else:
            hi = mi-1
    else:
        return False

if __name__ == '__main__':
    a = erfencha([2,7,8,12,19,21,23,45],455)
    print(a)
