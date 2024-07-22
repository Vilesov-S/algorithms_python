def gray_code(n : int) -> list:
    return [bin(i^(i>>1))[2:].zfill(n) for i in range(1<<n)]

def main():
    for st in gray_code(4):
        print(st, int(st, 2))

if __name__ == "__main__":
    main()
