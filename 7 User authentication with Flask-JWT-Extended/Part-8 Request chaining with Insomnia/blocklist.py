"""
blocklist.py

This file just contains the blocklist of the JW tokens. It will be imported by app and longout resource so that token can be added to the blocklist when the user logs out.

"""

## Ini akan berisi set token JWT, atau akan diimport oleh app dan kemudian akan digunakan untuk memeriksa token apakah token ada pada set saat ingin dingunakan

BLOCKLIST = set()
