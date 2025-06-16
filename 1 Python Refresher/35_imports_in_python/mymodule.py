###################################PART 1###########################################################

# def divide(dividend, divisor):
#   return dividend / divisor

# # __name__ adalah variable global dalam ptyhon, yang bergantung pada file mana kita berada
# # ini memungkinkan kita untuk membedakan, antara file yang kita run dan file yang kita import
# print("mymodule.py: ", __name__) # kita akan mencetak mymodule.py dan kemudian dunder main (dunder istilah yang digunakan umum pada ptyhon)


###################################PART 2###########################################################

# def divide(dividend, divisor):
#   return dividend / divisor

# print("mymodule.py: ", __name__) 

###################################PART 3###########################################################

def divide(dividend, divisor):
  return dividend / divisor

print("mymodule.py: ", __name__) 

import libs.mylib