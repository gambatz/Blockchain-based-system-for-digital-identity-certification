# New storage models

class CollectionStorage:
    def __init__(self):
        self.collections = []

class AssetStorage:
    def __init__(self):
        self.assets = []

class ExpTokenStorage:
    def __init__(self):
        self.exptokens = []

    def _delete_(self,id,exptokenstorage,_ad):
        for exptoken in exptokenstorage.exptokens:
            if exptoken.id == id:
               for address in _ad.addresses:
                   if address["address"]["pbc"] == exptoken.owner:
                      address["info"]["exptokens"].pop(address["info"]["exptokens"].index(exptoken.id))

class TradeStorage:
    def __init__(self):
        self.trades = []