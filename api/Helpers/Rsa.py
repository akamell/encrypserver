import errno
from Crypto.Hash import SHA256
from Crypto.Hash import MD5
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Signature import PKCS1_PSS

class Rsa(object):

    def __init__(self): 
        #self.private_key = 'private.pem'
        #self.public_key = 'public.pem'
        random_generator = Random.new().read
        key = RSA.generate(2048, random_generator)
        self.private_key, self.public_key = key, key.publickey()

    def firmar(self, message = ''):
        try:
            #with open(self.private_key, 'r') as f:
            #    key = RSA.importKey(f.read())
            key = self.private_key
        except IOError as e:
            return "NADAAAAA"
            if e.errno != errno.ENOENT:
                raise
            # No private key, generate a new one. This can take a few seconds.
            key = RSA.generate(4096)
            with open(self.private_key, 'wb') as f:
                f.write(key.exportKey('PEM'))
            with open(self.public_key, 'wb') as f:
                f.write(key.publickey().exportKey('PEM'))

        #hasherS = SHA256.new(message)
        #hasher = MD5.new(message.encode('utf-8'))
        hasher = MD5.new()
        hasher.update(message)
        #hasher = h.hexdigest()
        #print(h.hexdigest())
        print(hasher.hexdigest())
        #print(hasherS.hexdigest())
        signer = PKCS1_v1_5.new(key)
        #signer = PKCS1_PSS.new(key)
        #signature = signer.sign(hasher)
        #return signature
        digest = MD5.new()
        digest.update(message)
        return signer.sign(digest)


    def validar(self, message = '', signature = ''):
        with open(self.public_key, 'rb') as f:
            key = RSA.importKey(f.read())
        #hasher = SHA256.new(message)
        hasher = MD5.new(message)
        verifier = PKCS1_v1_5.new(key)
        if verifier.verify(hasher, signature):
            print('Nice, the signature is valid!')
            return True
        else:
            print('No, the message was signed with the wrong private key or modified')
            return False
