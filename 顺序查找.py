def shuncha(q,de):
    q.append(de)
    for i in range(len(q)):
        try:
            if q[:-1][i] == de:
                return True
        except:
            return False


if __name__ == '__main__':
    a = shuncha([3,45,3,22,23,4,5,52,2],264654654465)
    print(a)

