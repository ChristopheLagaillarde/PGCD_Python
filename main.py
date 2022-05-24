from gcd import gcd


def main() -> None:
    try:
        print(gcd(int(input("gcd, number1 = ")), int(input("gcd, number2 = "))))
    except ValueError:
        print("Wrong input")


if __name__ == "__main__":
    main()
