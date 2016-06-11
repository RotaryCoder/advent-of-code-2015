# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 16:59:46 2016

@author: Dick84
"""

''' INPUT
Hit Points: 103
Damage: 9
Armor: 2
'''

from itertools import combinations
from abc import ABCMeta

class EquipmentItem(object):
    def __init__(self, name, cost, damage, defense):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.defense = defense
        
    def __repr__(self):
        return '{}[{}: c({}), d({}), a({})]'.format(
            self.__class__.__name__,
            self.name, 
            self.cost, 
            self.damage,
            self.defense)
            
    def __str__(self):
        return self.name
            
    @staticmethod
    def get_damage(item):
        if item is None:
            return 0        
        assert issubclass(type(item), EquipmentItem), 'method for EquipmentItem only'
        return item.damage
        
    @staticmethod
    def get_defense(item):
        if item is None:
            return 0
        assert issubclass(type(item), EquipmentItem), 'method for EquipmentItem only'
        return item.defense    
    
        
class Weapon(EquipmentItem):
    def __init__(self, name, cost, damage):
        EquipmentItem.__init__(self, name, cost, damage, 0)
        
        
class Armor(EquipmentItem):
    def __init__(self, name, cost, defense):
        EquipmentItem.__init__(self, name, cost, 0, defense)

        
class Ring(EquipmentItem):
    def __init__(self, name, cost, damage, defense):
        EquipmentItem.__init__(self, name, cost, damage, defense)
      
      
class Shop(object):
    weapons = []
    armors = [] 
    rings = []
    def __init__(self):
        self.AddItem(Weapon('Dagger',8,4))
        self.AddItem(Weapon('Shortsword',10,5))
        self.AddItem(Weapon('Warhammer',25,6))
        self.AddItem(Weapon('Longsword',40,7))
        self.AddItem(Weapon('Greataxe',74,8))
        
        self.AddItem(Armor('Leather',13,1))
        self.AddItem(Armor('Chainmail',31,2))
        self.AddItem(Armor('Splintmail',53,3))
        self.AddItem(Armor('Bandedmail',75,4))
        self.AddItem(Armor('Platemail',102,5))
        self.armors.append(None)
        
        self.AddItem(Ring('Damage+1',25,1,0))
        self.AddItem(Ring('Damage+2',50,2,0))
        self.AddItem(Ring('Damage+3',100,3,0))
        self.AddItem(Ring('Defense+1',20,0,1))
        self.AddItem(Ring('Defense+2',40,0,2))
        self.AddItem(Ring('Defense+3',80,0,3))
        self.rings.append(None)
        self.rings.append(None)
        
    def AddItem(self, equipment_item):
        if type(equipment_item) == Weapon:
            self.weapons.append(equipment_item)        
        elif type(equipment_item) == Armor:
            self.armors.append(equipment_item)
        elif type(equipment_item) == Ring:
            self.rings.append(equipment_item)
        else:
            raise NotImplementedError
    
    def __str__(self):
        armors = [str(x) for x in self.armors]
        weapons = [str(x) for x in self.weapons]
        rings = [str(x) for x in self.rings]
        return str([armors,weapons,rings])
        
        
class Buyer(object):
    def __init__(self, initial_money):
        self.money = initial_money
        
    def buy(self, equipment_item):
        if equipment_item == None:
            return
        self.money -= equipment_item.cost
    
    
class Fighter(object):
    def __init__(self, hitpoints):
        self.hitpoints = hitpoints
        
    def hit(self, opponent):

        opponent.hitpoints -= max(1, self.damage() - opponent.defense())
        
    def __str__(self):
        x = 'Fighter({})'.format(self.hitpoints)
        return x
        
    def dead(self):
        if self.hitpoints <=0:
            return True
        else:
            return False
        
    
class Player(Buyer, Fighter):
#    def buy(self, shop, )
    armor = None
    weapon = None
    ring1 = None
    ring2 = None
    
    def __init__(self):
        Buyer.__init__(self, 0)
        Fighter.__init__(self, 100)
        
    def equip_armor(self, armor):
        self.armor = armor
        self.buy(armor)
    
    def equip_weapon(self, weapon):
        self.weapon = weapon
        self.buy(weapon)
        
    def equip_ring1(self, ring):
        self.ring1 = ring
        self.buy(ring)
        
    def equip_ring2(self, ring):
        self.ring2 = ring
        self.buy(ring) 
        
    def equip_rings(self, rings):
        ring1, ring2 = rings
        self.equip_ring1(ring1)
        self.equip_ring2(ring2)
        
    def damage(self):
        assert self.weapon is not None, 'must have weapon equipped'
        d = 0
        d += EquipmentItem.get_damage(self.weapon)
        d += EquipmentItem.get_damage(self.ring1)
        d += EquipmentItem.get_damage(self.ring2)
        return d
        
    def defense(self):
        d = 0
        d += EquipmentItem.get_defense(self.armor)
        d += EquipmentItem.get_defense(self.ring1)
        d += EquipmentItem.get_defense(self.ring2)
        return d
            
        
    def __str__(self):
        a = str(self.armor)
        w = str(self.weapon)
        r1 = str(self.ring1)
        r2 = str(self.ring2)
        da = str(self.damage())
        de = str(self.defense())
        m = str(self.money)
        return str([a,w,r1,r2,da,de,m])
 
#Hit Points: 103
#Damage: 9
#Armor: 2       
class Boss(Fighter):
    def __init__(self):
        Fighter.__init__(self, 103)
        
    def damage(self):
        return 9
        
    def defense(self):
        return 2
    

def fight(player, boss):
    while True:
        player.hit(boss)
        if boss.dead():
            return True
        boss.hit(player)
        if player.dead():
            return False
                
    
s = Shop()
best_p = None
worst_p = None
for armor in s.armors:
    for weapon in s.weapons:
        for rings in combinations(s.rings, 2):
            p = Player()
            b = Boss()
            p.equip_armor(armor)
            p.equip_weapon(weapon)
            p.equip_rings(rings)
            if fight(p, b):
                if best_p == None or p.money > best_p.money:
                    best_p = p
            else:
                if worst_p == None or p.money < worst_p.money:
                    worst_p = p
            
# 90 too low
print(best_p)
print(worst_p)
# ['Chainmail', 'Longsword', 'Damage+2', 'None', '9', '2', '-121']
