# # Multability pada python, dan bagaimana hal itu dapat mempengaruhi program kita

# a = []
# b = a


# # outputnya sama persis, a dan b adalah name untuk object yang sama
# print(id(a))
# print(id(b))

#############################################################################################################

# # ketika kita mencoba memodifikasi a, maka kita akan melihat bawa a dan b keduanya berubah
# # itu bearti bahwa a dan b keduanya adalah reference ke object yang sama

# a = []
# b = a

# a.append(35)
# print(a)
# print(b)

#############################################################################################################
# Jika kita mengubah b menjadi empty list, maka kita akan lihat perbedaaanya
# karena keduanya dibaut secara terpisah, dan disimpan secara terpisah

# a = []
# b = []

# a.append(35)
# print(a)
# print(b)

# # perhatikan id nya berbeda
# print(id(a))
# print(id(b))


#############################################################################################################

# # fakta bahwa kita dapat mengubah list, setelah kita menciptakannya (mengcreatenya) itu berati bahwa list adalah "mutable"
# # mutable berati kita dapat mengubahnya

# # Beberapa value tidak dapat diubah, dan merupakan immutable values

# # Namun dalam python, semua hal adalah mutable, kaerena semuanya adalah object, kecuali spesifik tidak ada cara untuk mengubah properties object itu sendiri

# # kita membuat tuple, tidak ada cara untuk menambah dan menghapus element pada tuple
# a = ()
# b = ()

# # kita tidak bisa menggunakan appen()
# # dan jika kita melakukan ini akan membuat tuple baru, bukan memodifikasinya
# # Jadi tuple adalah immutable
# a = a + (15, )

#############################################################################################################

# # Contoh lain, a dan b memilki value yang sama, dan kita akan melihat idnya sama

# a = 8597
# b = 8597

# print(id(a))
# print(id(b))


# # lalu mengapa ketika kita sama sama membuat empty list pada a dan b, idnya berbeda, tetapi tidak pada integer ? 
# # ptyhon memiliki optimization dimana ketika sebuah integer dibuat, maka tidak akan menciptakan kembali jika ada yang identik dengan yang digunakan. jadi ptyhon tahu 8597 telah dibuat, jadi tidak perlu menciptakan yang baru

#############################################################################################################

# integer juga merupakan immutable, kita tidak dapat mengubahnya 

a = 8597
b = 8597

print(id(a))
print(id(b))

# jika kita melakukan ini, b tidak akan berubah karena nilai "8597" diciptakan pertama kali dan "a" adalah name dari nilai tersebut. assgiment name (pemberian) nama terjadi dengan tanda sama dengan (=)
# dan disini kita membuat "8598" dan kita memberi namenya "a"
# namun "b" masih merupakan name untuk "8997", itu tidak berubah sama sekali
a = 8598

print(id(a))
print(id(b))