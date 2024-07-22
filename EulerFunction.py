def funcEuler(n):
    '''
     мультипликативная арифметическая функция,
     значение которой равно количеству натуральных чисел,
     меньших либо равных n и взаимно простых с ним (gcd = 1).
     if phi(n) == n-1 -> n - prime number
    '''
    result = n
    i = 2
    while i*i <= n:
        if (n % i == 0):
            while (n % i == 0):
                n /= i
            result -= result / i
        i += 1
    if (n > 1):
        result -= result / n
    return int(result)


def main():
    print("N = 9: количество взаимно простых с N =", funcEuler(9))
    print("N = 11: количество взаимно простых с N =", funcEuler(11))

if __name__ == "__main__":
    main()
