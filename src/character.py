#!/usr/bin/env python
import random

class Character(object):
    
    def __init__(self, name, hit_chance=75, hp=50, dmg=10, crit_chance=5):
        self.name = name
        self.hit_chance = hit_chance
        self.hp = hp
        self.dmg = dmg
        self.crit_chance = crit_chance
        
    def __swing(self, opp_char):
        '''
        Args: Opponent Character object.
        Returns: Boolean value signaling success or failure.
        '''
        roll = random.randint(0,100)
        if (self._hit_chance < roll):
            return False
        else:
            return True
    
    def __get_damage(self):
        
        
    def attack(self, opp_char):
        if self.swing(opp_char):
            self.damage(opp_char)
        else:
            print "%s swung at %s but missed!" % (self.name, opp_char.name)
        
    
    def __send_damage(self, amount, opp_char):
        self.hp = self.hp - amount