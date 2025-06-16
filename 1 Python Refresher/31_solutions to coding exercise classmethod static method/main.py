class Store:
  def __init__(self, name):
    self.name = name
    self.items = []

  def add_item(self, name, price):
    self.items.append({
      "name": name, 
      "price": price
    })

  def stock_price(self):
    total = 0
    for item in self.items:
      total += item["price"]
    return total
  
  @classmethod
  def franchise(cls, store):
    # Returns another, store, with the same name as the argument's name, plis " - franchise
    return cls(store.name + " - franchise")


  @staticmethod
  def store_details(store):
    # Returns a string respresenting the argument
    # it should be in the format 'NAME, total stock price: TOTAL"
    return '{}, total stock price: {}'.format(store.name, int(store.stock_price()))


store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)
store2.add_item("Mouse", 100)

# print(Store.franchise(store).name)
# print(Store.franchise(store2).name)

# print(Store.store_details(store))
# print(Store.store_details(store2))

print(Store.franchise(store).name)
print(store.franchise(store).name)
print(store2.franchise(store).name)
print(store.franchise(store2).name)

print(store.store_details(store2))
print(store2.store_details(store2))
print(Store.store_details(store))
print(Store.store_details(store2))