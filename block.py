import hashlib
import datetime
#block merkle 
class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        sha.update(hash_str.encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [Block("Genesis Block", "0")]
        self.merkle_root = None

    def add_block(self, student_info):
        previous_hash = self.chain[-1].hash
        new_block = Block(student_info, previous_hash)
        self.chain.append(new_block)
        self.update_merkle_root()

    def get_transactions(self):
        return [block.data for block in self.chain[1:]]

    def update_merkle_root(self):
        transactions = self.get_transactions()
        self.merkle_root = self.calc_merkle_root(transactions)

    def calc_merkle_root(self, transactions):
        if len(transactions) == 0:
            return None
        elif len(transactions) == 1:
            return hashlib.sha256(str(transactions[0]).encode()).hexdigest()

        merkle = []
        for t in transactions:
            merkle.append(hashlib.sha256(str(t).encode()).hexdigest())

        while len(merkle) > 1:
            if len(merkle) % 2 != 0:
                merkle.append(merkle[-1])

            new_merkle = []
            for i in range(0, len(merkle), 2):
                new_merkle.append(hashlib.sha256((merkle[i] + merkle[i+1]).encode()).hexdigest())

            merkle = new_merkle

        return merkle[0]

# menu 

def print_blockchain(blockchain):
    for block in blockchain.chain:
        print("Timestamp: ", block.timestamp)
        print("Data: ", block.data)
        print("Hash: ", block.hash)
        print("Previous Hash: ", block.previous_hash)
        print("\n")
    print("Merkle Root: ", blockchain.merkle_root)

def add_student_info(blockchain):
    student_info = {}
    student_info["std_id"] = input("Enter student ID: ")
    student_info["std_name"] = input("Enter student name: ")
    student_info["std_surname"] = input("Enter student surname: ")
    student_info["std_gender"] = input("Enter student gender: ")
    student_info["std_birthday"] = input("Enter student birthday: ")
    blockchain.add_block(student_info)
    print("Student info added to blockchain!")

def menu():
    blockchain = Blockchain()

    while True:
        print("\nMenu:")
        print("1. Add student info to blockchain")
        print("2. Print blockchain")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student_info(blockchain)
        elif choice == "2":
            print_blockchain(blockchain)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

menu()
