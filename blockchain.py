import hashlib

def hashGenerator(data):
    result=hashlib.sha256(data.encode())
    return result.hexdigest()

class Block:
    def __init__(self,data,hash,prev_hash):
        self.data=data
        self.hash=hash
        self.prev_hash=prev_hash


class Blockchain:
    def __init__(self):
      hashLast=hashGenerator('ethereum')
      hashStart=hashGenerator('solidity')

      genesis=Block('first_block',hashStart,hashLast)
      self.chain=[genesis]

    def add_block(self,data):
        prev_hash=self.chain[-1].hash
        hash=hashGenerator(data+prev_hash)
        block=Block(data,hash,prev_hash)
        self.chain.append(block)

bc=Blockchain()
bc.add_block('second_block')
bc.add_block('third_block')
bc.add_block('fourth_block')

for block in bc.chain:
    print(block.__dict__)
    print("\n")

