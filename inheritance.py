from chef import chef
from chineseChef import chineseChef

myChef = chef()

myChef.makeChicken()
myChef.makeSalad()
myChef.makeSpecialDish()

mychineseChef = chineseChef() # chineseChef inherits from chef

mychineseChef.makeChicken()
mychineseChef.makeSalad()
mychineseChef.makeSpecialDish()