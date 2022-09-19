# Encrypt = base64.encode ( invert ( combine ( ( data ) + ( key ) ) ) )
# Decrypt = combine ( ( invert ( base64.decode ) ) + ( key ) )
# byteArray->b64encode->byteArray ~~ byteArray->decodebytes->byteArray
# b->invert->b
# b,b->combine->b
# b,b->encrypt->b
# b,b->decrypt->b
# b,b->encode->b
# b,b->decode->b

from base64 import b64encode as e,b64decode as d
from util_crypto import *

def encrypt(bKey,bPlainData):
	K=bKey
	D=bPlainData
	encrypted = invert ( combine(K,D) )
	return e(encrypted)

def decrypt(bKey,bCypherData):
	bCypherData+=b'=='
	K=bKey
	D= (
				d( bCypherData ) )
	D=invert(D)
	return combine(K,D)

def encodeData(filename,keys,data):
	f=open(filename,'ab')
	data=data.encode()
	for x in keys.split(' '):
		data=encrypt(x.encode(),data)
	f.write(data)
	f.write(b'\n')
	f.close()
	print('encoding finished')
	print('YOUR CYPHER DATA IS : ',data.decode())
	return
	
def decodeData(filename,keys,*args):
	f=open(filename,'rb')
	data=f.readline()
	while(data):
		for x in reversed( keys.split(' ') ):
			data=decrypt(x.encode(),data)
		print('YOUR PLAIN DATA IS :',data.decode())
		data=f.readline()
	f.close()
	print('decoding finished')
	return
	

operation=int(input("(0) Encode\n(1) Decode\n Enter Operation : "))
if not operation:
	data=input("Enter data : ")
else:
	data=''
keys=input("Enter keys (Separated by space) : ")
filename=input("Enter filename : ")

op={0:encodeData,1:decodeData}
op[operation](filename,keys,data)
input("Enter to quit ")
