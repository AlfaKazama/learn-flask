# Inheritance memungkian class dapat mengakses method atau properties dari class lain

class Device:
  def __init__(self, name, connected_by):
    self.name = name
    self.connected_by = connected_by
    self.connected = True

  def __str__(self):
    # !r berarti memanggil rerp method dari self.name (sehingga akan tampak sudah berisi tanda kutip) Kita melakukan ini lebih baik dari pada manual memberikan tanda kutip
    return f"Device {self.name!r} ({self.connected_by})"
  
  def disconnect(self):
    self.connected = False
    print("Disconnected.")


printer = Device("Printer", "USB")
print(printer)

#################################################################################################################

# # Menggunakan inheritance: Membuat class lain yang akan menggunakan method dan properties pada class Device


# class Device: 
#   def __init__(self, name, connected_by):
#     self.name = name
#     self.connected_by = connected_by
#     self.connected = True

#   def __str__(self):
#     # !r berarti memanggil rerp method dari self.name (sehingga akan tampak sudah berisi tanda kutip) Kita melakukan ini lebih baik dari pada manual memberikan tanda kutip
#     return f"Device {self.name!r} ({self.connected_by})"
  
#   def disconnect(self):
#     self.connected = False
#     print("Disconnected.")


# # Membuat class baru "Printer" dan mewarisi device
# # Class ini memiliki akses kesemua method dan properties dari class Device
# class Printer(Device):
#   def __init__(self, name, connected_by, capacity):
#     # Kita cukup memanggil parent class device, dengan super dan init method. init methodnya ini merujuk ke parent classnya 
#     super().__init__(name, connected_by) 
#     self.capacity = capacity
#     self.remaining_pages = capacity

#   def __str__(self):
#     return f"{super().__str__()} ({self.remaining_pages} pages remaining)"
  
#   def print(self, pages):
#     if not self.connected:
#       print("Your printer is not connected!")
#       return
#     print(f"Printing {pages} pages")
#     self.remaining_pages -= pages
#     # super().disconnect()
#     # self.disconnect()


# hp = Printer("HP Printer", "USB", 100)
# print(hp)

# hp.print(10)
# print(hp.remaining_pages)

# # Ketika kita memanggil disconnect(), akan terjadi 3 tingkatan panggilan: Pertama python akan mengecek adakah method disconnect() pada class Printer, jika tidak ada dia akan mengecek lagi pada parentnya class Device, jika masih tidak ada python akan mengecek pada object. Jika di object tidak ada maka akan error
# hp.disconnect()
# hp.print(20)
