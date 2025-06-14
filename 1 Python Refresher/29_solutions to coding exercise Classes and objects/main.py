# class Store:
#   def __init__(self, name):
#     # You'll need 'name' as an argument to this method
#     # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
#     self.name = name
#     self.items = []

#   def add_items(self, name, price):     
#     # Create a dictionary with keys name and price, and append that to self.items.
#     self.items.append({name: price})

#   def stock_price(self):
#     # Add together all item prices in self.items and return the total.
#     total = 0
    
#     # for price in self.items:
#     #   total += list(price.values())[0]
#     #   print(total)

#     for item in self.items:
#       for price in item.values():
#         total += price
#     return total
  

# jurmiStore = Store("Jurmi Store")
# jurmiStore.add_items("14 watt hannoc lamp", 27000)
# jurmiStore.add_items("4-hole terminal", 19000)
# jurmiStore.add_items("100 meters of 2.5 fiber power cable", 235000)
# print(jurmiStore.items)
# print(jurmiStore.stock_price())

#################################################################################################################
## Solution from videos

class Store:
  def __init__(self, name):
    # You'll need 'name' as an argument to this method
    # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
    self.name = name
    self.items = []

  def add_items(self, name, price):     
    # Create a dictionary with keys name and price, and append that to self.items.
    item = {"name": name, "price": price}
    self.items.append(item)

  def stock_price(self):
    ## Add together all item prices in self.items and return the total.
    # total = 0
    # for item in self.items:
    #   total += item["price"]
    # return total

    # Kita bisa menggunakan list comprehension
    return sum([item["price"] for item in self.items])
  

jurmiStore = Store("Jurmi Store")
jurmiStore.add_items("14 watt hannoc lamp", 27000)
jurmiStore.add_items("4-hole terminal", 19000)
jurmiStore.add_items("100 meters of 2.5 fiber power cable", 235000)
print(jurmiStore.items)
print(jurmiStore.stock_price())