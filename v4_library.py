'''
Hugo May 
fune game version 4 library
definition of classes and objects

'''

class player(object):

    def __init__(self, level, inventory, stats):
        self.level = level
        self.inventory = inventory
        self.stats = stats

    def __str__(self):
        return f'Level : {self.level}\nInventory : {self.inventory}\nStats : {self.stats}'

class enemy(object):

    def __init__(self, level, type):
        self.level = level
        self.type = type

        if self.type == 1:
            '''
            #health = 60 + 6 per level
            #attack = 7 + 2 per level
            #defense = 0 + .2 per level
            '''
            self.health = 60 + (6 * self.level)
            self.attack = 7 + (2 * self.level)
            self.defense = 0 + int(.20 * self.level)
            self.type = 'wolf'

        elif self.type == 2:
            '''
            #health = 85 + 9 per level
            #attack = 5 + 1.5 per level
            #defense = 2 + .25 per level
            '''
            self.health = 85 + (9 * self.level)
            self.attack = 5 + int(1.5 * self.level)
            self.defense = 2 + int(.25 * self.level)
            self.type = 'orc'
        elif self.type == 3:
            '''
            #health = 75 + 7 per level
            #attack = 4 + 1.2 per level
            #defense = 5 + 1.5 per level
            '''
            self.health = 75 + (7 * self.level)
            self.attack = 4 + int(1.2 * self.level)
            self.defense = 5 + int(1.5 * self.level)
            self.type = 'armored orc'

    def __str__(self):
        return f'Health : {self.health}\nAttack : {self.attack}\nDefense : {self.defense}\n'
        

class goblin(enemy):

    def __init__(self, level, type):
        super().__init__(level, type)
        '''
        #health = 50 + 5 per level
        #attack = 3 + 1.2 per level
        #defense = 0
        '''
        self.health = 50 + (5 * self.level)
        self.attack = 3 + int(1.2 * self.level)
        self.defense = 0
        self.type = 'goblin'


'''
new_player = player(1, {'Health Potion':0, 'Damage Potion':0, 'Bandage':0}, {'Max Health':100, 'Health':100,'Strength':5, 'Defense':0})
print(new_player)
'''

'''
new_enemy = goblin(10, 5, 0)
print(new_enemy, isinstance(new_enemy, goblin))
new_enemy = enemy(20, 10, 5)
print(new_enemy, isinstance(new_enemy, goblin))
'''

