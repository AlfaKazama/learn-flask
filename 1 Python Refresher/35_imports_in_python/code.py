###################################PART 1###########################################################

# # Import digunakan untuk mendapatkan code dari file lain ke file main kita

# # Jika kita tidak ingin mengimpor sesuatu secara spesifik, kita bisa melakukan ini langsung
# # import mymodule

# # Ini adalah cara import secara spesifik
# from mymodule import divide


# print(divide(10, 2)) 
# # ini juga akan mencetak mymodule.py: mymodule
# # ini terjadjadi karena hanya file yang kita run yang merupakan dunder main
# print(__name__)


###################################PART 2###########################################################

# # Jadi bagaimana cara ptyhon mengetahui mymodule berada ? import sys. import sys memungkikan kita menggunakan syd module yang datang dengan ptyhon dan itu membuka beberapa system functionalities. dan salah satusnya sys.path
# import sys

# # sys.path adalah jalur impor, dimaana python akan mencari file yang akan diimport 
# print(sys.path)


###################################PART 3###########################################################

import mymodule
import sys

print(mymodule.divide(10, 10))
print(sys.modules)