# Buka file dalam mode append (tambahkan)
file = open('C:/Users/malik/Kerjaan/python-file/pertemuan1/data.txt','a+')  
# Tulis baris baru ke file
file.write("\nHello Zaki")
# Pindahkan kursor ke awal file
file.seek(0)
# Baca seluruh isi file
text = file.read()
# Cetak isi file
print(text)
