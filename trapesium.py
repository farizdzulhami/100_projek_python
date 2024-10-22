print('='*40)
print('PROGRAM TRAPESIUM')
print('='*40)

sisi1 = int(input('Sisi sejajar 1\t\t: '))
sisi2 = int(input('Sisi sejajar 2\t\t: '))
sisi3 = int(input("Sisi tidak sejajar 1\t: "))
sisi4 =int(input('Sisi tidak sejajar 2\t: '))
t = int(input('Tnggi\t\t: '))

l = 1/2 * (sisi1+sisi2) * t
k = sisi1+sisi2+sisi3+sisi4

print(f'Luas\t\t\t: {l}')
print(f'Keliling\t\t: {k}')