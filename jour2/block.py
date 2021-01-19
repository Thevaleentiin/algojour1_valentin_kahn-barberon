from datetime import datetime
from hashlib import sha256
import random
import string

def calculateHash(block):
    bloc = str(block.index) + str(block.previous_hash) + str(block.timestamp) + str(block.data) + str(block.nonce)
    return(sha256(bloc.encode('utf-8')).hexdigest())

pow_length = 3

class Block:
    def __init__(self, previous_hash, data):
        self.index = 1
        self.previous_hash = previous_hash
        self.timestamp = datetime.now()
        self.data = data
        self.nonce = 0
        self.self_hash = self.mine_hash()

    def mine_hash(self):
        test_hash = calculateHash(self)
        while (test_hash[:pow_length] != "0" * pow_length):
            self.nonce = self.nonce + 1
            test_hash = calculateHash(self)
        return test_hash



class Blockchain:
    def __init__(self, pow, length):
        self.chain = []
        self.pow = pow
        self.length = length
        self.current_previous_hash = None

    def new_block(self, data):
        block = Block(self.current_previous_hash, data)
        self.chain.append(block)
        self.current_previous_hash = block.self_hash

blockchain_length = 4

blockchain = Blockchain(None, blockchain_length)
for i in range(0, blockchain.length):
    lowercases = string.ascii_lowercase
    block_data = ''.join(random.choice(lowercases) for i in range(20))
    blockchain.new_block(block_data)

for i in range(0, blockchain_length):
    print("Block #" + str(i))
    print("Index : " + str(blockchain.chain[i].index))
    print("Previous hash : " + str(blockchain.chain[i].previous_hash))
    print("Timestamp : " + str(blockchain.chain[i].timestamp))
    print("Self hash : " + str(blockchain.chain[i].self_hash))
    print("Data : " + str(blockchain.chain[i].data))
    print("Nonce : " + str(blockchain.chain[i].nonce))
    print(" ")