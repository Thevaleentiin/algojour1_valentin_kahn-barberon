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

    def display(self):
        print(" ")
        print("Block #" + str(self.index))
        print("Previous hash : " + str(self.previous_hash))
        print("Timestamp : " + str(self.timestamp))
        print("Self hash : " + str(self.self_hash))
        print("Data : " + str(self.data))
        print("Nonce : " + str(self.nonce))
        print(" ")

    def toJSON(self):
        return jsonpickle.encode(self)


class Blockchain:
    def __init__(self, pow):
        self.chain = []
        self.pow = pow
        self.current_previous_hash = None

    def get_by_index(self, index):
        if (int(index) >= len(self.chain)):
            print("Aucun block ne correspond a cet index")
            return None
        return self.chain[int(index)]

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
    
    def validity_display(self):
        print("Blockchain validity : " + str(self.security_check()))

    def display(self):
        self.validity_display()
        for block in self.chain:
            block.display()

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
        action = input("Que voulez vous faire ? (ADD/del/search/quit)")
        if (action == "add" or action == "ADD" or action == ""):
            data = input("Entrez la data de votre block : ")
            blockchain.add_block(data)
            blockchain.display()
        elif (action == "del"):
            blockchain.delete_block()
            print("Le dernier block a été supprimé")
            blockchain.display()
        elif (action == "search"):
            index = input("Quel est l'index du block recherché ? ")
            searched_block = blockchain.get_by_index(index)
            if (searched_block != None):
                searched_block.display()
        elif (action == "quit"):
            blockchain.display()
            break
        else:
            print("Commande incorrecte")

    file.write(blockchain.toJSON())
    file.close()

        