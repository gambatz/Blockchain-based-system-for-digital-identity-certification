from datetime import datetime
import unittest
from trilio import Trilio, wallett, ix
from architectures.block import ExpiringTokenAutority


class Test_Trilio(unittest.TestCase):
      
      def setUp(self):
          self.exp=ExpiringTokenAutority(wallett.addresses[1]["address"]["pbc"],wallett,ix)
          self.exp=ExpiringTokenAutority(wallett.addresses[1]["address"]["pbc"],wallett,ix)
          self.exp=ExpiringTokenAutority(wallett.addresses[1]["address"]["pbc"],wallett,ix)
          self.catena=Trilio()
          
          
          
      def tearDown(self):
          print("sciao")

      def test_block_not_ok(self):
           var=[ ]
           self.catena.create_transaction(
    datetime.now(),
    data={
        "type":"exptoken-transfer",
        "data":{
            "_to":wallett.addresses[0]["address"]["pbc"],
            "_from":wallett.addresses[1]["address"]["pve"],
            "exptoken_id":wallett.addresses[1]["info"]["exptokens"][0],
            
        }
    }
)
           var.append(self.catena.trilio.chain[1].transactions[0].input["data"]["exptoken_id"])
           self.catena.create_transaction(
    datetime.now(),
    data={
        "type":"exptoken-transfer",
        "data":{
            "_to":wallett.addresses[1]["address"]["pbc"],
            "_from":wallett.addresses[0]["address"]["pve"],
            "exptoken_id":wallett.addresses[0]["info"]["exptokens"][0],
            
        }
    }
)
           #var.append(self.catena.trilio.chain[2].transactions[0].input["data"]["exptoken_id"])
           self.assertEqual(wallett.addresses[0]["info"]["exptokens"],[ ])
           self.assertEqual(wallett.addresses[0]["info"]["benefits"],0)

      def test_block_ok(self):
          var1=[ ]
          print("test_block")
          self.catena.create_transaction(
          datetime.now(),
          data={
        "type":"exptoken-transfer",
        "data":{
            "_to":wallett.addresses[0]["address"]["pbc"],
            "_from":wallett.addresses[1]["address"]["pve"],
            "exptoken_id":wallett.addresses[1]["info"]["exptokens"][0],
            
        }
    }
)
          var1.append(self.catena.trilio.chain[1].transactions[0].input["data"]["exptoken_id"])
          self.assertEqual(wallett.addresses[0]["info"]["exptokens"],var1)
          self.assertEqual(wallett.addresses[1]["info"]["benefits"],1)


      def test_block_ok_benefits(self):
          var=[ ]
          print("test_block")
          self.catena.create_transaction(
          datetime.now(),
          data={
        "type":"exptoken-transfer",
        "data":{
            "_to":wallett.addresses[0]["address"]["pbc"],
            "_from":wallett.addresses[1]["address"]["pve"],
            "exptoken_id":wallett.addresses[1]["info"]["exptokens"][0],
            
        }
    }
)
          var.append(self.catena.trilio.chain[1].transactions[0].input["data"]["exptoken_id"])
          self.catena.create_transaction(
          datetime.now(),
          data={
        "type":"exptoken-transfer",
        "data":{
            "_to":wallett.addresses[0]["address"]["pbc"],
            "_from":wallett.addresses[1]["address"]["pve"],
            "exptoken_id":wallett.addresses[1]["info"]["exptokens"][0],
            
        }
    }
)
          var.append(self.catena.trilio.chain[2].transactions[0].input["data"]["exptoken_id"])
          self.catena.create_transaction(
          datetime.now(),
          data={
        "type":"exptoken-transfer",
        "data":{
            "_to":wallett.addresses[0]["address"]["pbc"],
            "_from":wallett.addresses[1]["address"]["pve"],
            "exptoken_id":wallett.addresses[1]["info"]["exptokens"][0],
            
        }
    }
)
          var.append(self.catena.trilio.chain[3].transactions[0].input["data"]["exptoken_id"])

          self.assertEqual(wallett.addresses[0]["info"]["exptokens"],var)
          self.assertNotEqual(wallett.addresses[1]["info"]["exptokens"],None)
          self.assertEqual(wallett.addresses[1]["info"]["benefits"],0)


if __name__ == ' __main__ ':
     unittest.main()
