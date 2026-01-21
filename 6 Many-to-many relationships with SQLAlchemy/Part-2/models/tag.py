from db import db


## Kita membuat tag model dengan nama table "tags" yang memiliki column id, name, store_id, store

class TagModel(db.Model):
  __tablename__ = "tags"


  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  store_id = db.Column(db.String(), db.ForeignKey("stores.id"), nullable=False)

  store = db.relationship("StoreModel", back_populates="tags")