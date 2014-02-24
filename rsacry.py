#!/bin/env python
from sys import exit
import argparse
import rsa

rsaBits = 1024
pubName = 'pub_rsa.pem'
priName = 'pri_rsa.pem'

def genKey():
    # generate key couple
    (pubKey, priKey) = rsa.newkeys(rsaBits)
    # write public key
    pub = pubKey.save_pkcs1()
    pubFile = open(pubName, 'w+')
    pubFile.write(pub)
    pubFile.close()
    # write private key
    pri = priKey.save_pkcs1()
    priFile = open(priName, 'w+')
    priFile.write(pri)
    priFile.close()
    return True

def enCryMes(message):
    # get public key to encry
    with open(pubName) as pubFile:
        pub = pubFile.read()
    pubKey = rsa.PublicKey.load_pkcs1(pub)
    # encry message
    enCry = rsa.encrypt(message, pubKey)
    enCryStr = ''
    for interMes in enCry:
        enCryStr += "%2.2x" % ord(interMes)
    return enCryStr

def deCryMes(message):
    # get private key to decry
    with open(priName) as priFile:
        pri = priFile.read()
    priKey = rsa.PrivateKey.load_pkcs1(pri)

    # check the len of the message
    lenmess = len(message)
    if lenmess % 2 != 0 : # the message must be even
        exit('error: your encry mes must be error')

    # get encryed message
    enCry = ''
    for i in range(lenmess/2):
        enTmp = message[i * 2 : (i + 1) * 2]
        enCry += chr(int(enTmp, 16))

    # decry mess
    deCry = rsa.decrypt(enCry, priKey)
    return deCry

def main():
    parser = argparse.ArgumentParser(description = 'Encry/Decry message')
    parser.add_argument('--genkey', action = 'store_true', 
                        dest = 'genKey', default = False,
                        help = 'generate public and private key couple')
    parser.add_argument('--encry' , action = 'store', dest = 'enCry',
                        help = 'the message you need to encrypt')
    parser.add_argument('--decry' , action = 'store', dest = 'deCry',
                        help = 'the message you need to decrypt')
    args = parser.parse_args()
    
    if args.genKey :
        genKey()
    if args.enCry:
        print enCryMes(args.enCry)
    if args.deCry:
        print deCryMes(args.deCry)

if __name__ == '__main__':
    main()
