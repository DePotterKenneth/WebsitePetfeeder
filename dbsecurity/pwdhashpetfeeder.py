import hashlib
import binascii
import os

from model.dbsecurity.dbconn import DbConnection

# voorbeeld DB schema ter referentie
# NB: hash en salt hebben vaste lengte
#   --> datatype CHAR( aantal bytes x 2 )

db_ = DbConnection(database="petfeeder_db")


def setpasword(password):
    # 1) paswoord omzetten naar type bytes
    pwd_bytes = bytes(password, 'utf-8')

    # 2) random salt genereren, resultaat is al in bytes
    salt_bytes = os.urandom(16)

    # 3) hash berekenen
    hash_bytes = hashlib.pbkdf2_hmac('sha256', pwd_bytes, salt_bytes, 100000)

    # 4) omzetten naar hex-string
    salt_string = binascii.hexlify(salt_bytes).decode('utf-8')
    hash_string = binascii.hexlify(hash_bytes).decode('utf-8')

    # 5) opslaan in db
    # PyCharm valt over de syntax maar dat geeft niet
    sql = (
        'UPDATE tblsettings SET pasword_hash = %(new_hash)s, pasword_salt = %(new_salt)s WHERE settings_id = 1; '
    )

    params = {
        'new_hash': hash_string,
        'new_salt': salt_string,
    }

    # uitvoeren & klaar!
    result = db_.execute(sql, params)


def verify_credentials(password):

    # 1) hash en salt opvragen uit db
    sql = 'SELECT pasword_hash, pasword_salt FROM petfeeder_db.tblsettings where settings_id = 1;'

    result = db_.query(sql, dictionary= True)

    db_user = result[0]

    # hash en salt uit resultaat halen
    db_hash_string = db_user['pasword_hash']
    db_salt_string = db_user['pasword_salt']

    # 2) hash berekenen met INGEVOERD WACHTWOORD en OPGESLAGEN SALT
    # eerst beide weer omzetten naar type bytes
    pwd_bytes = bytes(password, 'utf_8')
    db_salt_bytes = binascii.unhexlify(db_salt_string)

    # nieuwe hash berekenen
    hash_bytes = hashlib.pbkdf2_hmac('sha256', pwd_bytes, db_salt_bytes, 100000)

    # omzetten naar string om te kunnen vergelijken
    hash_string = binascii.hexlify(hash_bytes).decode('utf-8')

    # 3) enkel als het wachtwoord juist was komt de hash overeen
    return hash_string == db_hash_string

