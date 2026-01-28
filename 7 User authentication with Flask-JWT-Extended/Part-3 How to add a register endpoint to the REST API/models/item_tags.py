from db import db

# Model ini akan mendefinisikan tabel sekunder yang akan kita gunakan antara item dan tag
# kita akan menerapkan many to many relationship
class ItemTags(db.Model):
  __tablename__ = "items_tags"

  id = db.Column(db.Integer, primary_key=True)

  # bagian yang menarik adalah dua kolom berikutnya, link to item dan link to tags
  # mereka akan mendifinisikan hubungan (relationship) antara individual item dan individual tag
  # inilah cara kita mendefinisikan tabel sekunder yang akan kita gunakan pada many to many relationship:
  item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
  tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"))

  # Kita akan menghubungkan satu dengan yang lain 


