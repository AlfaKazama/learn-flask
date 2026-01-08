from marshmallow import Schema, fields


# Mengecek data yang dikirimkan client kepada kita, pastikan benar dan sesuai schema

# Kita telah membuat one many relationship, jadi akan ada perubahan pada class class schemas
class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class ItemSchema(PlainItemSchema):
    # ini berarti setiap kali kita menggunakan ItemSchema, kita dapat meneruskan store_id saat kita menerima data dari client
    store_id = fields.Int(required=True, load_only=True)

    # ini akan digunakan saat mengembalikan/return data dari client, bukan digunakan saat menerima (receive) data dari client
    store = fields.Nested(PlainStoreSchema(), dump_only=True)


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema(), dump_only=True))