from architectures.blockchain import Blockchain
from architectures.block import Block
from architectures.wallet import Wallet
from architectures.transaction import Transaction
from architectures.nft import CollectionStorage, AssetStorage, TradeStorage, ExpTokenStorage
from datetime import datetime

wallett=Wallet()
wallett.create_wallet()
wallett.create_wallet()
#wallett.create_wallet()

ix= ExpTokenStorage()


class Trilio:
    def __init__(self):
        self.trilio = Blockchain(
            name="Trilio", 
            difficulty=4,
            minimum_transactions=1
        )
        # Create genisis
        self.trilio.chain.append(Block(datetime.now().timestamp(), ["genisis block"]))
        self.Wallet = Wallet()
        self.TradeStorage = TradeStorage()
        self.CollectionStorage = CollectionStorage()
        self.AssetStorage = AssetStorage()
    
    def validate_chain(self):
        for i in range(len(self.trilio.chain)):
            if self.trilio.chain[i].transactions[0] != "genisis block":
                if self.trilio.chain[i].get_hash() != self.trilio.chain[i].hash:
                    return False
                
                if self.trilio.chain[i].previous_hash != self.trilio.chain[i-1].hash:
                    return False
    
    def create_block(self,addresses, exptokens, collections=None, assets=None, trades=None, ):
        nonce = self.trilio.difficulty ** 12
        for i in range(nonce):
            pass
        if self.trilio.pending_transactions[0].input["type"]=="exptoken-transfer":
            
           for i in range (len(self.trilio.chain)):#controllo ciclico sulla sicurezza
                publ=wallett.get_public_key(self.trilio.mobile_transactions[i].input["data"]["_from"])
                if self.trilio.pending_transactions[0].input["data"]["exptoken_id"] == self.trilio.mobile_transactions[i].input["data"]["exptoken_id"] and self.trilio.pending_transactions[0].input["data"]["_to"] == publ:
                   ix._delete_(self.trilio.mobile_transactions[i].input["data"]["exptoken_id"],ix,wallett)
                   print("Recycled Token")
                   return "Recycled Token"
                
                    
                

        if len(self.trilio.pending_transactions) >= self.trilio.minimum_transactions:
            # block.hash, block.timestamp, block.transactions, block.previous_hash
            transactions = self.trilio.pending_transactions
            self.trilio.pending_transactions = []
            block = Block(datetime.now().timestamp(), transactions, self.trilio.chain[len(self.trilio.chain)-1].hash, addresses, collections, assets, trades, exptokens)
            self.trilio.chain.append(block)
            return block
        else:
            return False
    
    def create_transaction(self, timestamp, data):
        self.trilio.pending_transactions.append(
            Transaction(timestamp,data=data)
        )
        self.trilio.mobile_transactions.append(
            Transaction(timestamp,data=data)
        )
        self.create_block(
            addresses=wallett,
            exptokens=ix,
            collections=self.CollectionStorage,
            trades=self.TradeStorage,
            assets=self.AssetStorage
        )
    
    def get_transaction(self, data):
        for block in self.trilio.chain:
            for transaction in block.transactions:
                if transaction.hash == data:
                    return transaction
    
    class Wallet(Wallet):pass
    class TradeStorage(TradeStorage):pass
    class CollectionStorage(CollectionStorage):pass
    class AssetStorage(AssetStorage):pass
