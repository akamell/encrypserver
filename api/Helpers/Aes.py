import base64
import hashlib, re
from Crypto import Random
from Crypto.Cipher import AES

class Aes(object):

    def __init__(self, key): 
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = self.decode_base64(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

    def decode_base64(self, data):
        altchars=b'+/'        
        data = re.sub('[^a-zA-Z0-9%s]+' % altchars, '', data)  # normalize
        missing_padding = len(data) % 4
        if missing_padding:
            data += '='* (4 - missing_padding)
        return base64.b64decode(data, altchars)

