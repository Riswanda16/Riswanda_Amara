#judul
print('Program mengurutkan 3 bilangan')
# siapkan list untuk menampung input dari user
data = []

#siapkan variabel untuk menampung setiap inputan user    
a = int(input('Masukan angka: '))
b = int(input('Masukan bilangan ke dua: '))
c = int(input('Masukan bilangan ke tiga: '))

#data.append digunakan untuk menampilkan inputan user
data.append(a)
data.append(b)
data.append(c)

#menampilkan output
 
print('Data acak: ', data)
#menggunakan list.sort() untuk mengurutkan angka secara ascending
list.sort(data)
print('Data urut: ', data)

#selesai