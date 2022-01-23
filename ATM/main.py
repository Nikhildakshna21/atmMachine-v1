from card import Card
from atm import ATM

card = Card(49053,2002)

atm = ATM(card,49053,2002)

atm.withDraw(6000)
atm.checkBalance()

print('hi')