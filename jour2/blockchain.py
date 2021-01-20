from datetime import datetime
from hashlib import sha256
import random
import string
import jsonpickle
import sys

def calculateHash(block):
    bloc = str(block.index) + str(block.previous_hash) + str(block.timestamp) + str(block.data) + str(block.nonce)
    return(sha256(bloc.encode('utf-8')).hexdigest())

class Block:
    def __init__(self, index, previous_hash, data, pow):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = str(datetime.now())
        self.data = data
        self.nonce = 0
        self.pow = pow
        self.mine_hash()

    def mine_hash(self):
        test_hash = calculateHash(self)
        while (test_hash[:int(self.pow)] != "0" * int(self.pow)):
            self.nonce = self.nonce + 1
            test_hash = calculateHash(self)
        self.self_hash = test_hash

    def toJSON(self):
        return jsonpickle.encode(self)


class Blockchain:
    def __init__(self, pow):
        self.chain = []
        self.pow = pow
        self.current_previous_hash = None

    def add_block(self, data):
        block = Block(len(self.chain), self.current_previous_hash, data, self.pow)
        self.chain.append(block)
        self.current_previous_hash = block.self_hash

    def load_block(self, block):
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
        print("Blockchain validity : " + str(self.security_check()))
        for block in self.chain:
            print(" ")
            print("Block #" + str(block.index))
            print("Previous hash : " + str(block.previous_hash))
            print("Timestamp : " + str(block.timestamp))
            print("Self hash : " + str(block.self_hash))
            print("Data : " + str(block.data))
            print("Nonce : " + str(block.nonce))
            print(" ")

    def toJSON(self):
        return jsonpickle.encode(self)

def load_blockchain_from_file(file):
    json_content = file.read()
    if len(json_content) != 0:
        blockchain_object = jsonpickle.decode(json_content)
        blockchain = Blockchain(blockchain_object.pow)
        for block in blockchain_object.chain:
            blockchain.load_block(block)
        return blockchain
    return None

try:
    file = open(sys.argv[1], "r")
    blockchain = load_blockchain_from_file(file)
    file.close()
except IOError:
    print(sys.argv[1] + " created.")
    blockchain = None
finally:
    file = open(sys.argv[1], "w")
    if (blockchain == None):
        pow = input("Entrez la taille de la preuve de travail : ")
        blockchain = Blockchain(pow)
        blockchain.add_block("Genesis block")
    blockchain.display()

    while(True):
        action = input("Que voulez vous faire ? (ADD/del/quit)")
        if (action == "add" or action == "ADD" or action == ""):
            data = input("Entrez la data de votre block : ")
            blockchain.add_block(data)
            blockchain.display()
        elif (action == "del"):
            blockchain.delete_block()
            print("Le dernier block a été supprimé")
            blockchain.display()
        elif (action == "quit"):
            blockchain.display()
            break
        else:
            print("Commande incorrecte")

    file.write(blockchain.toJSON())
    file.close()

        