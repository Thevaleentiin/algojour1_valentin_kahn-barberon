from datetime import datetime
from hashlib import sha256
import random
import string

def calculateHash(block):
    bloc = str(block.index) + str(block.previous_hash) + str(block.timestamp) + str(block.data) + str(block.nonce)
    return(sha256(bloc.encode('utf-8')).hexdigest())

class Block:
    def __init__(self, index, previous_hash, data, pow):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = datetime.now()
        self.data = data
        self.nonce = 0
        self.mine_hash()

    def mine_hash(self):
        test_hash = calculateHash(self)
        while (test_hash[:pow] != "0" * pow):
            self.nonce = self.nonce + 1
            test_hash = calculateHash(self)
        self.self_hash = test_hash


class Blockchain:
    def __init__(self, pow):
        self.chain = []
        self.pow = pow
        self.current_previous_hash = None

    def add_block(self, data):
        block = Block(len(self.chain), self.current_previous_hash, data, self.pow)
        self.chain.append(block)
        self.current_previous_hash = block.self_hash

    def delete_block(self):
        self.chain.pop()

    def security_check(self):
        length = len(self.chain)
        if (length == 1 and calculateHash(self.chain[0]) != self.chain[0].self_hash):
            return False
        for i in range(0, length - 1):
            if (calculateHash(self.chain[i]) != self.chain[i].self_hash or self.chain[i].self_hash != self.chain[i + 1].previous_hash):
                return False
        return True

    def display(self):
        print("Blockchain validity : " + str(blockchain.security_check()))
        for block in self.chain:
            print(" ")
            print("Block #" + str(block.index))
            print("Previous hash : " + str(block.previous_hash))
            print("Timestamp : " + str(block.timestamp))
            print("Self hash : " + str(block.self_hash))
            print("Data : " + str(block.data))
            print("Nonce : " + str(block.nonce))
            print(" ")


pow = input("Entrez la taille de la preuve de travail : ")
blockchain = Blockchain(pow)
blockchain.add_block("Genesis block")
blockchain.display()
again = raw_input("Voulez vous ajouter un nouveau block ? (Y/n)")
if (again == "y" or again == ""):
    data = raw_input("Entrez une data : ")
    while (data):
        blockchain.add_block(data)
        blockchain.display()
        again = raw_input("Voulez vous ajouter un nouveau block ? (Y/n)")
        if (again == "y" or again == ""):
            data = raw_input("Entrez une data : ")
        else:
            break

    