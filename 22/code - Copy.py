# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 17:51:25 2016

@author: Dick84
"""

from random import randint

class BossDead(Exception):
    def __init__(self, message = 'The boss is dead'):
        super().__init__(message)

class PlayerDead(Exception):
    def __init__(self, message = 'The player is dead'):
        super().__init__(message)

class OutOfMana(Exception):
    def __init__(self, message = 'Out of mana'):
        super().__init__(message)
        
class SameSpell(Exception):
    def __init__(self, message = 'Casting the same spell twice'):
        super().__init__(message)  

class SpellContainer():    
    '''
    Magic Missile costs 53 mana. It instantly does 4 damage.
    Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
    Shield costs 113 mana. It starts an effect that lasts for 6 turns. 
        While it is active, your armor is increased by 7.
    Poison costs 173 mana. It starts an effect that lasts for 6 turns. 
        At the start of each turn while it is active, it deals the boss 3 damage.
    Recharge costs 229 mana. It starts an effect that lasts for 5 turns. 
        At the start of each turn while it is active, it gives you 101 new mana.
    '''
    
    hits = 	{      # c    du da h  de ma
     'Magic Missile':  (53,  1, 4, 0, 0, 0  )
    ,'Drain':          (73,  1, 2, 2, 0, 0  )
    ,'Shield':         (113, 6, 0, 0, 7, 0  )
    ,'Poison':         (173, 6, 3, 0, 0, 0  )
    ,'Recharge':       (229, 5, 0, 0, 0, 101)
    ,'Boss Hit':       (0,   1, 10, 0, 0, 0 )
	}
 
    user_spells = ['MagicMissile', 'Drain', 'Shield', 'Poison', 'Recharge']

    @classmethod
    def GetSpellData(self, hit_name):
        x =  self.hits[hit_name]
        cost, duration, damage, hp, defense, mana = x
#        print(x)
        return x
    
    @classmethod
    def GetCost(self, hit_name):
        c = self.hits[hit_name][0]
        return c

    @classmethod
    def GetDuration(self, hit_name):
        du = self.hits[hit_name][1]
        return du

    @classmethod
    def GetDamage(self, hit_name):
        da = self.hits[hit_name][2]
        return da
    
    @classmethod
    def GetHealing(cls, hit_name):
        h = cls.hits[hit_name][3]
        return h
    
    @classmethod
    def GetDefense(self, hit_name):
        de = self.hits[hit_name][4]
        return de
    
    @classmethod
    def GetMana(self, hit_name):
        m = self.hits[hit_name][5]
        return m
        

class TimeMachine():
    def __init__(self):
        self.characters = []
    def register(self, c, priority):
        self.characters.append((c, priority))
        # bad coding but whoooo cares !
        self.characters = sorted(self.characters, key=lambda c: c[1])
    
    def tick(self):
        for c, _ in self.characters:
            c.tick()
            
class Character():
    def __init__(self, hp):
        self.hp = hp
        self.mana = 50
        self.hitlist = {}
    
    def Hit(self, hit_name):
        if hit_name in self.hitlist.keys():
            raise SameSpell
#        print('{} casting {}'.format(type(self), hit_name))
        d = SpellContainer.GetDuration(hit_name)
        self.hitlist[hit_name] = d
    
    def ReceiveDamage(self, hp):
        if hp < 1 :
            return
        self.hp -= hp
        print('{} suffered for {} to {}'.format(self.__class__.__name__, hp, self.hp))
        if self.hp < 0:            
            if type(self) is Boss:
                raise BossDead()
            else:
                raise PlayerDead()
    
    def Heal(self, hp):
        if type(self) is Boss:
            return
        if hp < 1 :
            return
        self.hp += hp
        print('{} healed for {} to {}'.format(self.__class__.__name__, hp, self.hp))

    def tick(self):
        d = 0
        hp = 0
        if 'Boss Hit' in self.hitlist:
            bosshit = True
        else:
            bosshit = False
        for hit in list(self.hitlist.keys())[:]:
            if type(self) is Boss:
                assert hit == 'Boss Hit', hit
            da = SpellContainer.GetDamage(hit)
#            if (da > 0):
#                print('{} taking {} hp.'.format(hit, da))
            de = SpellContainer.GetDefense(hit)
            
            d = da - de
            hp += SpellContainer.GetHealing(hit)
            self.mana += SpellContainer.GetMana(hit)
    
            self.hitlist[hit] = self.hitlist[hit] - 1
            if self.hitlist[hit] == 0:
                self.hitlist.pop(hit)
            
        if (bosshit):
            if d < 1:
                d = 1
                assert False, str(self.hitlist)
        self.ReceiveDamage(d)
#        elif d > 0:
#            assert False, 'thought this wouldn''t happen'
        self.Heal(hp)  


class Player(Character):
    def __init__(self, hp, mana):
        Character.__init__(self, hp)
        self.mana = mana
        self.total_spent_mana = []
        
    def can_cast(self, hit_name):
        c = SpellContainer.GetCost(hit_name)
        return c <= self.mana
        
    def cast(self, character, hit_name):       
        co, du, da, hp, de, ma = SpellContainer.GetSpellData(hit_name)
        self.spend_mana(co)
        
        if da > 0:
            character.Hit(hit_name)
        if hp > 0 or de > 0 or ma > 0:
            self.Hit(hit_name)
            
    def spend_mana(self, mana):
        self.mana -= mana
        if (self.mana < 0):
            raise OutOfMana()
        self.total_spent_mana.append(mana)
    
    

class Boss(Character):
    '''
    Hit Points: 71
    Damage: 10
    '''
    def __init__(self, hp):
        Character.__init__(self, hp)
    
        


i = 0
min_mana = 99999999
for i in range(10000000):
    try:
        b = Boss(71)
        p = Player(50, 500)
        t = TimeMachine()
        t.register(p, 1)
        t.register(b, 2)        
        while True:
#            print('you have {}'.format(p.hp))
#            print('boss has {}'.format(b.hp))
#            i = int(input())
            i = randint(0,4)
            hit_name = SpellContainer.user_spells[i]
            p.cast(b, hit_name)
            p.Hit('Boss Hit')
            t.tick()
    except SameSpell:
        pass
    except (PlayerDead, OutOfMana) as o:
        pass
    except BossDead:
        if sum(p.total_spent_mana) < min_mana:
            min_mana = sum(p.total_spent_mana)
            print(p.total_spent_mana, min_mana, p.hp)

# 101 too low
