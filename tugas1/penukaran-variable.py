# inisialisasi variable
piring1 = "Manggis"
piring2 = "Pisang"
piring3 = None

#Tampilan awal sebelum ditukar
print("Sebelum ditukar :")
print("Piring 1 =", piring1)
print("piring 2 =", piring2)
print("Piring 3 =", piring3)

#proses penukaran
piring3 = piring1
piring1 = piring2
piring2 = piring3
piring3 = None

#Tampilan setelah penukaran
print("Setelah ditukar :")
print("Piring 1 =", piring1)
print("piring 2 =", piring2)
print("Piring 3 :", piring3)

