print(30*'033[92m=')
print('PROGRAM LIMAS SEGITIGA')
print(30*'033[92m=')

def input_user():
    '''mengambil input dari user'''
    global a
    global t
    global T
    a = int(input('masukan nilai alas segitiga = '))
    t = int(input('masukan nilai tinggi segitiga = '))
    T = int(input('masukan nilai tinggi limas = '))
    return a, t, T

a,t,T = input_user()
'''beberapa variable'''
luas_alas = 0.5 * a * t #luas alas segitiga
sisi_1 = ((a/2)**2 + T**2)**0.5 # tinggi sisi pertama
sisi_2 = ((a/2)**2 + T**2)**0.5 # tinggi sisi kedua
luas_sisi = (0.5 * a * sisi_1) + (0.5 * a * sisi_2) + (0.5 * a * sisi_1) # 3 sisi segitiga


volume_limas_segitiga = lambda T : (1/3) * luas_alas * T
luas_limas_segitiga = lambda luas_alas,luas_sisi : luas_alas + luas_sisi

print(f'hasil perhitungan volume limas segitiga = {volume_limas_segitiga(T):.2f}')
print(f'hasil perhitungan luas limas segitiga = {luas_limas_segitiga(luas_alas,luas_sisi):.2f} ')