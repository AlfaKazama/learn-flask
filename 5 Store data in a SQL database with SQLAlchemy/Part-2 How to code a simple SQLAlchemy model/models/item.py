from db import db

# ini akan menjadi mapping antara baris dalam tabel (row in table) ke class python
class ItemModel(db.Model):
  # ini akan memberi tahu sqlalchemy bahwa kita ingin membuat table yang berisi "items" untuk class ini
  __tablename__ = "items"

  # dan kemudian kita tentukan kolom kolom apa saja yang seharusnya ada pada tabel tersebut:

  # beginilah cara kita mendefinisikan klom yang akan menjadi bagian dari items table ini
  # ini akan menjadi integer kolom dan merupakan primary key (seara default saat kita menggunakan Postgress, ini akan membuatnya bertambah otomatis, jadi kolom id akan diisi terlebih dahulu oleh database dan akan diberikan nomor yang tersediat dalam urutan angka, dimulai dari satu dan seterusnya)
  id = db.Column(db.Integer, primary_key=True)

  # kolom ini string dengan maximal 80 karakter dan "name" suatu items akan menjadi unique. dan nullable bernilai false, yang berati kita tidak dapat membuat yang tidak memiliki name. Jika kita menghapus "unique=True" itu berati kita dapat membuat beberapa item dengan nama yang sama.
  name = db.Column(db.String(80), unique=True, nullable=False) 
  price = db.Column(db.Float(precision=2), unique=False, nullable=False)
  # store_id akan menjadi tautan antara "items" table dan "stores" table
  # value dalam "store_id" harus sesuai dengan valude "id" dalam stores table
  # kita akan menggunakan one many relationships
  store_id = db.Column(db.Integer, unique=False, nullable=False)