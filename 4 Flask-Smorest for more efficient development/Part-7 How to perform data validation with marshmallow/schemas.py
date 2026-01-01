from marshmallow import Schema, fields


# Mengecek data yang dikirimkan client kepada kita, pastikan benar dan sesuai schema

class ItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    

class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)