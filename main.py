a = int(input("Saisir le premier nombre"))
b = int(input("Saisir le premier nombre"))

if a < b:
    temp = a
    a = b
    b = temp

r = b % a

while r != 0:
    a = b
    b = r
    r = b % a

print("Le PGCD est", b)
