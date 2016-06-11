# -*- coding: utf-8 -*-

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

    user_spells = ['Magic Missile', 'Drain', 'Shield', 'Poison', 'Recharge']

    @classmethod
    def FromCost(cls, cost):
        for hitname, value in cls.hits.items():
            if value[0] == cost:
                return hitname

    @classmethod
    def GetSpellData(cls, hit_name):
        x =  cls.hits[hit_name]
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
#        print('{} receiving {}'.format(self.__class__.__name__, hit_name))
        d = SpellContainer.GetDuration(hit_name)
        self.hitlist[hit_name] = d

    def ReceiveDamage(self, hp):
        if hp < 1 :
            return
        self.hp -= hp
#        print('{} suffered for {} to {}'.format(self.__class__.__name__, hp, self.hp))
        if self.hp <= 0:            
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
#        print('{} healed for {} to {}'.format(self.__class__.__name__, hp, self.hp))

    def tick(self):
        d = 0
        hp = 0
        popped = None

        # Part Deux

        if type(self) is Boss:
            if 'Magic Missile' in self.hitlist:
                d += 4
            if 'Drain' in self.hitlist:
                d += 2
            if 'Poison' in self.hitlist:
                d += 3
            assert 'Boss Hit' not in self.hitlist
#            assert d < 5
            self.ReceiveDamage(d)
        else:

            if 'Boss Hit' in self.hitlist:
                d += 10
                if 'Shield' in self.hitlist:
                    d -= 7
                self.ReceiveDamage(d)
            if 'Drain' in self.hitlist:
                self.Heal(2)
            if 'Recharge' in self.hitlist:
                self.mana += 101

        for hit in list(self.hitlist.keys())[:]:
            self.hitlist[hit] -= 1
            if self.hitlist[hit] == 0:
                self.hitlist.pop(hit)

class Player(Character):
    def __init__(self, hp, mana):
        Character.__init__(self, hp)
        self.mana = mana
        self.total_spent_mana = []

    def can_cast(self, boss, hit_name):
        b = True        
        c = SpellContainer.GetCost(hit_name)
        b &= c <= self.mana
        b &= hit_name not in self.hitlist
        b &= hit_name not in boss.hitlist
        return b

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
        assert len(self.total_spent_mana) < 100

class Boss(Character):
    '''
    Hit Points: 71
    Damage: 10
    '''
    def __init__(self, hp):
        Character.__init__(self, hp)

def print_stats(player, boss, hit):
    return
    print('-- Player turn --')
    defense = 0            
    if 'Shield' in p.hitlist:
        defense = 7
    print('- Player has {} hit points, {} armor, {} mana'.format(
        player.hp, defense, player.mana))
    print('- Boss has {} hit points'.format(boss.hp))
    print('Player casts {}.'.format(hit))
    print()

i = 0
min_mana = 9999999
maxlife = 99999
for i in range(99999):
    try:
        b = Boss(71)
        p = Player(50, 500)
        t = TimeMachine()
        t.register(p, 1)
        t.register(b, 2)  
        preferred =  [113, 229, 173, 113, 229, 173, 113, 229, 173]
        for j in range(9999999):
#            print('you have {}'.format(p.hp))
#            print('boss has {}'.format(b.hp))
#            i = int(input())
            can_cast = False
            hit_name = ''            
            for k in range(200):
#                print(p.mana)
                if len(preferred) > 0:
                    x = preferred.pop(0)
                    hit_name = SpellContainer.FromCost(x)
                    can_cast = True
                    break
                elif p.can_cast(b, 'Shield') and randint(0, 3) > 0:
                    hit_name = 'Shield'
                    can_cast = True
                    break                    
                elif p.mana < 300 and randint(0,3) > 0 and p.can_cast(b, 'Recharge'):
                    hit_name = 'Recharge'
                    can_cast = True
                    break
                elif p.mana < 450 and randint(0,2) == 0 and p.can_cast(b, 'Recharge'):
                    hit_name = 'Recharge'
                    can_cast = True
                    break
                elif p.can_cast(b, 'Poison') and randint(0,2) == 0:
                    hit_name = 'Poison'
                    can_cast = True
                    break
                elif p.can_cast(b, 'Drain') and randint(0,2) == 0:
                    hit_name = 'Drain'
                    can_cast = True
                    break
                else:
                    i = randint(0,4)
                    hit_name = SpellContainer.user_spells[i]
                    can_cast = p.can_cast(b, hit_name)
                    if can_cast:
                        break
                assert i < 198
            p.ReceiveDamage(1)
            print_stats(p, b, hit_name)    
            p.cast(b, hit_name)
            t.tick()
            print_stats(p, b, 'Boss Hit')
            p.Hit('Boss Hit')
            t.tick()
    except SameSpell:
        raise
    except PlayerDead as d:
#        print(str(d))
        pass
#        if b.hp <= maxlife:
#            maxlife = b.hp
#            y = [SpellContainer.FromCost(x) for x in p.total_spent_mana]
#            print('b{} p{} {}'.format(b.hp, p.hp, p.total_spent_mana ))
#            print(y)
    except OutOfMana as o:
#        raise
#        print(str(o))
        pass
    except BossDead:
#        print('Win ',p.total_spent_mana, min_mana, p.hp)

        new_min_mana = sum(p.total_spent_mana)
        if new_min_mana < min_mana:
            min_mana = new_min_mana            
            print('Win {} {} {}'.format(str(p.total_spent_mana), min_mana, p.hp))

# 101 too low
# 1937 too high

#Win  [113, 229, 173, 113, 229, 173, 113, 229, 173, 73, 113, 173, 53] 1957 6
#Win  [173, 229, 113, 173, 229, 113, 173, 229, 113, 173, 53, 113] 1884 3
#Win  [173, 229, 113, 173, 229, 113, 173, 229, 113, 173, 73, 73] 1864 7
#Win  [173, 229, 113, 173, 229, 113, 173, 229, 113, 173, 53, 53] 1824 3