def invert(bData):
	bInvData=b''
	for b in bData:
		bInvData+= (~b&255).to_bytes(1,'little')
	return bInvData
	
def combine(bKey,bData):
	merge=b''
	for i in range(0,len(bData)):
		merge+= ( bData[i] ^ bKey[i%len(bKey)] ) .to_bytes(1,'little')
	return merge
	
