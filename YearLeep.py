def year_leap(year):
    return bool(not year % 4 and year % 100 or not year % 400)

def main():
    print(year_leap(2024))
    print(year_leap(2025))

if __name__ == "__main__":
    main()
