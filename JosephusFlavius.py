'''
Задача Иосифа Флавия(Josephus Flavius task):
    N – объектов расположены по кругу, и пронумерованы числами от 1 до N,
    начиная с первой исключается каждый k-тый объект,
    до тех пор пока не останется один единственный.
    По заданным N и k необходимо определить номер оставшегося объекта.

Josephus Flavius task:
    N – objects are arranged in a circle, and numbered from 1 to N,
    starting from the first, every k-th object is excluded,
    until only one remains.
    Given N and k, it is necessary to determine the number
    of the remaining object.
'''

def jsf_flv(n, k):
    res = 0
    for i in range(1, n+1):
        res = (res + k) % i
    return res + 1


def main():
    print(jsf_flv(10, 3))

if __name__ == "__main__":
    main()
