from marshmallow import Schema, fields

# Schema akan digunakan untuk memvalidasi incoming data dan mengubah outgoing data, menjadi data yang valid sesuai schema

class ItemSchema(Schema):
    # Field "id" bertipe string.
    # Kita kasih parameter dump_only=True artinya:
    # Field ini HANYA muncul saat data DIKIRIM KELUAR (response API).
    # Field ini TIDAK boleh dikirim dari client saat membuat/mengupdate data (request API).
    # Biasanya ID itu dibuat otomatis di server (misalnya pakai uuid), 
    # jadi user tidak perlu kirim ID, cukup server yang generate.
    id = fields.Str(dump_only=True)

    # Field "name" juga bertipe string.
    # Kita kasih parameter required=True artinya:
    # Saat client kirim request field "name" wajib ada di JSON payload.
    # Kalau field "name" tidak ada, maka request akan dianggap invalid.
    # Field ini digunakan untuk menerima data DARI client.
    name = fields.Str(required=True)

    # Field "Price" bertipe float.
    # Kita kasih parameter requeire=True dengan alasan yang sama dengan field name
    price = fields.Float(required=True)

    # Field "store_id" bertipe string.
    # Kita kasih parameter requeire=True dengan alasan yang sama dengan field name
    store_id = fields.Str(required=True)

# Jadi 3 field selain id, akan digunakan untuk validasi data yang berasal dari request. 


class ItemUpdateSchema(Schema):
    # Kita tidak memerlukan required=True, Karena saat update, kita biasanya tidak wajib mengirim semua field. Client boleh update sebagian data saja. Misalnya cuma mau update harga, tanpa ubah nama. (atau bahkan bisa tidak mengirim field sama sekali)
    name = fields.Str()
    price = fields.Float()
    

class StoreSchema(Schema):
    id = fields.Str(dumpy_only=True)
    name = fields.Str(required=True)