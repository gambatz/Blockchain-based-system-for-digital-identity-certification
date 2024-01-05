from architectures.block import ExpiringTokenAutority
from datetime import datetime
import PySimpleGUI as psg
from trilio import Trilio, wallett, ix

exp=ExpiringTokenAutority(wallett.addresses[1]["address"]["pbc"],wallett,ix)
exp=ExpiringTokenAutority(wallett.addresses[0]["address"]["pbc"],wallett,ix)
exp=ExpiringTokenAutority(wallett.addresses[0]["address"]["pbc"],wallett,ix)
print(wallett.addresses)
catena=Trilio()
print(catena.trilio.chain[0].transactions[0])

layout = [
   [psg.Text("chose the receiver"), psg.Combo([wallett.addresses[0]["address"]["pbc"],wallett.addresses[1]["address"]["pbc"]],key="-TO-")],
   [psg.Button("Send"), psg.Exit()],
   

]
window = psg.Window('Transaction', layout, size=(715, 180))
while True:
   event, values = window.read()
   print(event, values)
   if event == "Send":
      result = values['-TO-'] 
   if event == psg.WIN_CLOSED or event == 'Send':
      break
window.close()

catena.create_transaction(
          datetime.now(),
          data={
        "type":"exptoken-transfer",
        "data":{
            "_to":result,
            "_from":wallett.addresses[1]["address"]["pve"],
            "exptoken_id":wallett.addresses[1]["info"]["exptokens"][0],
            
        }
    }
)



#print(catena.trilio.chain[1].status)
print("")
print("")
print(catena.trilio.chain[1].transactions[0].input)
#print(catena.trilio.chain[2].transactions[0].input)
#print(catena.trilio.chain[3].transactions[0].input["data"]["exptoken_id"])
catena.validate_chain
#catena.get_transaction(catena.trilio.chain[3].transactions[0].input["data"])
#print(wallet.addresses[0]["info"]["exptokens"])
#print(wallet.addresses[1]["info"]["exptokens"])
print(wallett.addresses)