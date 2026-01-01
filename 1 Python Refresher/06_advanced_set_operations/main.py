# # Function "difference()"

# friends = {"Bob", "Rolf", "Anne"}
# abroad = {"Bob", "Anne"}

# ## Membuat variabel set yang menampung teman yang tidak berada diluar negeri
# local_friends = friends.difference(abroad) # .difference() mengambil set friends dan menghapus element element yang sama pada abroad
# # local_friends = abroad.difference(friends) # kamu juga bisa melakukan ini, tapi akan menghasilkan hasil yang berbeda. akan menghasilkan empty set
# print(local_friends)

######################################################################
# Function "union()"

local = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

friends = local.union(local, abroad) # menggabungkan set local dan abroad
print(friends)

######################################################################
# # Function "intersection()"

# art = {"Bob", "Jen", "Rolf", "Charlie"}
# science = {"Bob", "Jen", "Adam", "Anne"}

# # Membuat set yang menampung orang yang belajar art dan science (belajar keduanya)
# both = art.intersection(science) # irisan dari kedua set
# print(both)