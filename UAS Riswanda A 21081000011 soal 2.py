#cetak judul
print('Menentukan nilai terbesar dari 3 bilangan')

   
#menyiapkan variabel untuk menampung inputan user
#karena rangenya 3 maka siapkan 3 variabe

a = int(input('Masukan bilangan pertama: '))
b = int(input('Masukan bilangan kedua: '))
c = int(input('Masukan bilangan ketiga: '))

#menentukan nilai bilangan
maks = a
if b > maks:
    maks = b
if c > maks:
    maks = c
    
#mencetak hasil
print('Bilangan terbesar adalah: %d' % maks)