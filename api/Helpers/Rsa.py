import errno
import codecs

from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5
from Crypto.PublicKey import RSA


class Rsa(object):

    def __init__(self):
        self.private_key = open("private.pem", "rb").read()
        self.public_key = open("public.pem", "rb").read()

    def firmar(self, message=''):
        hash = MD5.new(message.encode('utf-8', 'ignore'))

        pri_key = RSA.import_key(self.private_key)

        signer = PKCS1_v1_5.new(pri_key)
        signature = signer.sign(hash)

        hexify = codecs.getencoder('hex')
        return hexify(signature)[0]

    def validar(self, message='', signature=''):

        dehexify = codecs.getdecoder('hex')
        sign = dehexify(signature)[0]

        hash = MD5.new(message)
        pub_key = RSA.import_key(self.public_key)

        verifier = PKCS1_v1_5.new(pub_key)

        if verifier.verify(hash, sign):
            print('Nice, the signature is valid!')
            return True
        else:
            print('No, the message was signed with the wrong private key or modified')
            return False
