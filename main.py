from gcd import gcd


def main():
    print(gcd(int(input("gcd, number1 = ")), int(input("gcd, number2 = "))))


if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("Wrong input")