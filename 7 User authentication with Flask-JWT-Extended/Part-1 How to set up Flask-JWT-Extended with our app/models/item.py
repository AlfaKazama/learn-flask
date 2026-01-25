from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)

    store_id = db.Column(
        db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False
    )
    store = db.relationship("StoreModel", back_populates="items")

    # menambhakan ini untuk menghubungkan satu dengan yang lain dan kita perlu menambahkan secondary
    # secondary ini merujuk pada table secondary yang kita buat yaitu table "items_tags"
    tags = db.relationship("TagModel", back_populates="items", secondary="item_tags")

    # perhatikan tidak ada kita menambahkan tag_id, atau item_id pada proses ini, karena semuanya melewati/mengaksesknya melalui table sekunder