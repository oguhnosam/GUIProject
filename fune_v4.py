'''
Hugo May 
fune game version 4
preparing to integrate user interface

'''

import os
import time
import math
import random

CLEAR = '\n' * 100


# start of the room ascii art
def rm1():
    moves = {'up':True, 'down':False, 'left':False, 'right':False}
    print("xxxxxxxxxx/////////xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx        O        xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    return moves

def rm2():
    moves = {'up':True, 'down':False, 'left':True, 'right':False}
    print("xxxxxxxxxx/////////xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("/|||||                 xxxxxx")
    print("/|||||        O        xxxxxx")
    print("/|||||                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    return moves

def rm3():
    moves = {'up':True, 'down':False, 'left':False, 'right':True}
    print("xxxxxxxxxx/////////xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 |||||/")
    print("xxxxxx        O        |||||/")
    print("xxxxxx                 |||||/")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    return moves

def rm4():
    moves = {'up':True, 'down':True, 'left':False, 'right':False}
    print("xxxxxxxxxx/////////xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx        O        xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx/////////xxxxxxxxxx")
    return moves

def rm5():
    moves = {'up':True, 'down':True, 'left':True, 'right':False}
    print("xxxxxxxxxx/////////xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("/|||||                 xxxxxx")
    print("/|||||        O        xxxxxx")
    print("/|||||                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx/////////xxxxxxxxxx")
    return moves

def rm6():
    moves = {'up':True, 'down':True, 'left':False, 'right':True}
    print("xxxxxxxxxx/////////xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 |||||/")
    print("xxxxxx        O        |||||/")
    print("xxxxxx                 |||||/")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx/////////xxxxxxxxxx")
    return moves

def rm7():
    moves = {'up':True, 'down':False, 'left':True, 'right':True}
    print("xxxxxxxxxx/////////xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("/|||||                 |||||/")
    print("/|||||        O        |||||/")
    print("/|||||                 |||||/")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    return moves
    
def rm8():
    moves = {'up':False, 'down':True, 'left':False, 'right':False}
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx        O        xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx/////////xxxxxxxxxx")
    return moves

def rm9():
    moves = {'up':False, 'down':True, 'left':False, 'right':True}
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 |||||/")
    print("xxxxxx        O        |||||/")
    print("xxxxxx                 |||||/")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx/////////xxxxxxxxxx")
    return moves
    
def rm10():
    moves = {'up':False, 'down':True, 'left':True, 'right':False}
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("/|||||                 xxxxxx")
    print("/|||||        O        xxxxxx")
    print("/|||||                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx/////////xxxxxxxxxx")
    return moves

def rm11():
    moves = {'up':False, 'down':True, 'left':True, 'right':True}
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("/|||||                 |||||/")
    print("/|||||        O        |||||/")
    print("/|||||                 |||||/")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx/////////xxxxxxxxxx")
    return moves
    
def rm12():
    moves = {'up':False, 'down':False, 'left':True, 'right':True}
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("/|||||                 |||||/")
    print("/|||||        O        |||||/")
    print("/|||||                 |||||/")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    return moves
    
def rm13():
    moves = {'up':False, 'down':False, 'left':True, 'right':False}
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("/|||||                 xxxxxx")
    print("/|||||        O        xxxxxx")
    print("/|||||                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    return moves

def rm14():
    moves = {'up':False, 'down':False, 'left':False, 'right':True}
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 |||||/")
    print("xxxxxx        O        |||||/")
    print("xxxxxx                 |||||/")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    return moves

#list of rooms that dont have a down movement
def no_downs():
    num = random.randint(1,7)
    if num == 1:
        moves = rm1()
    elif num == 2:
        moves = rm2()
    elif num == 3:
        moves = rm3()
    elif num == 4:
        moves = rm7()
    elif num == 5:
        moves = rm12()
    elif num == 6:
        moves = rm13()
    elif num == 7:
        moves = rm14()
    else:
        print('no downs broke')
    return moves
    
# list of rooms that don't have an up move
def no_ups():
    num = random.randint(1,7)
    if num == 1:
        moves = rm8()
    elif num == 2:
        moves = rm9()
    elif num == 3:
        moves = rm10()
    elif num == 4:
        moves = rm11()
    elif num == 5:
        moves = rm12()
    elif num == 6:
        moves = rm13()
    elif num == 7:
        moves = rm14()
    else:
        print('no ups broke')
    return moves

# list of rooms that don't have a right move
def no_rights():
    num = random.randint(1,7)
    if num == 1:
        moves = rm1()
    elif num == 2:
        moves = rm2()
    elif num == 3:
        moves = rm4()
    elif num == 4:
        moves = rm5()
    elif num == 5:
        moves = rm8()
    elif num == 6:
        moves = rm10()
    elif num == 7:
        moves = rm13()
    else:
        print('no rights broke')
    return moves

# list of rooms that don't have a left move
def no_lefts():
    num = random.randint(1,7)
    if num == 1:
        moves = rm1()
    elif num == 2:
        moves = rm3()
    elif num == 3:
        moves = rm4()
    elif num == 4:
        moves = rm6()
    elif num == 5:
        moves = rm8()
    elif num == 6:
        moves = rm9()
    elif num == 7:
        moves = rm14()
    else:
        print('no lefts broke')
    return moves

def generate_room(move):
    if move == 'up':
        moves = no_downs()
    elif move == 'down':
        moves = no_ups()
    elif move == 'left':
        moves = no_rights()
    elif move == 'right':
        moves = no_lefts()
    else:
        print('generate room broken')
    return moves

def generate_enemy(lvl):
    '''
    generates 1 of 4 different enemy types
    1st is a wolf : high damage medium health low defense
    2nd is an orc : meduim attack high health medium low defense
    3rd is an armored orc : medium attack medium high health high defense
    4th is a goblin : low attack low health no defense but can steal items on hit
    '''

    en_type = random.randint(0, 3)
    is_goblin = False
    if en_type == 0:
        '''
        health = 60 + 6 per level
        attack = 7 + 2 per level
        defense = 0 + .2 per level
        '''
        en_health = 60 + (6 * lvl)
        en_attack = 7 + (2 * lvl)
        en_defense = 0 + int(.20 * lvl)
        print('A wolf appears...')

    elif en_type == 1:
        '''
        health = 85 + 9 per level
        attack = 5 + 1.5 per level
        defense = 2 + .25 per level
        '''
        en_health = 85 + (9 * lvl)
        en_attack = 5 + int(1.5 * lvl)
        en_defense = 2 + int(.25 * lvl)
        print('An orc appears...')
    elif en_type == 2:
        '''
        health = 75 + 7 per level
        attack = 4 + 1.2 per level
        defense = 5 + 1.5 per level
        '''
        en_health = 75 + (7 * lvl)
        en_attack = 4 + int(1.2 * lvl)
        en_defense = 5 + int(1.5 * lvl)
        print('An orc clad in armor appears...')
    elif en_type == 3:
        '''
        health = 50 + 5 per level
        attack = 3 + 1.2 per level
        defense = 0
        '''
        is_goblin == True
        en_health = 50 + (5 * lvl)
        en_attack = 3 + int(1.2 * lvl)
        en_defense = 0

    return en_health, en_attack, en_defense, is_goblin


'''
In the event the player wants to attack the program must calculate a few things
if the player can land the attack based on a hardcoded accuracy
how much damage the player will do based on a random number between a floor 15% lower and 20% higher than the player's attack
how much damage is negated by enemy defense
whether or not the player will land a critical strike, doubling damage, based on a hardcoded chance of 1/7
how much damage is boosted by potions
whether of not the player deals more damage than needed to kill the enemy

'''
def player_attack(en_health, en_defense, attack, damage_boost):
    ext_damage = 0
    accuracy = random.randint(0,15)
    if accuracy == 1:
        print('You tried to attack but missed...')
    else:
        '''
        to add variety within the game the player will not do a set amount of damage each hit
        instead the player will deal anywhere between 15% lower or 20% higher than their actual damage stat
        '''
        high = attack * .2
        low = attack * -.15
        divr = random.randint(int(low), int(high))

        #removes 1 point of damage for every 2 points of defense
        damage = attack + divr - int(en_defense/2)

        #tries for a critical hit
        crit = random.randint(0,7)
        if crit == 1:
            damage *= 2
            print('Critical Hit!')
        
        #multiplies the damage by the damage boost variable
        damage *= damage_boost

        #truncates the damage delt to the enemy and subtracts it from the enemy's health
        damage = int(damage)
        en_health -= damage

        '''
        checks to see if the player has overkilled the enemy
        this amount of extra damage will go towards the player's exp count
        '''
        if en_health < 0:
            ext_damage = abs(en_health)

        print('The enemy took', damage, 'damage!')

        return en_health, ext_damage

def player_use_item(max_health, health, attack, items, en_health, en_defense, last_player_action, potion_sickness, d_boost, d_boost_timer):
    for i in items:
        #adds an s to the prompt if needed
        if items[i] == 1:
            print('You have', items[i], i)
        else:
            print(f'You have {items[i]} {i}s')
    #takes the player input on which item they want
    choice = input('What item would you like to use? (enter cancel to exit): ').lower()

    #makes sure that the player entered a valid item
    if choice in items:

        #makes sure that the player has one of the items they chose
        if items[choice] > 0:
            #berry : +15 health
            if choice == 'berry':
                health += 15
                if health > max_health:
                    health = max_health
            
            #bandage : +15% health
            elif choice == 'bandages':
                health += int(max_health * .15)
                if health > max_health:
                    health = max_health

            #lesser healing potion : +25% health
            #3 round potion sickness after use
            elif choice == 'lesser healing potion' and potion_sick < 1:
                health += int(max_health * .25)
                if health > max_health:
                    health = max_health
                potion_sick = 4
            
            #lesser damage potion : +20% damage for 2 turns
            #4 round potion sickness after use
            elif choice == 'lesser damage potion' and potion_sick < 1:
                d_boost = 1.2
                d_boost_timer = 3
                potion_sick = 5

            #health potion : +50% health
            #5 round potion sickness after use
            elif choice == 'health potion' and potion_sick < 1:
                health += int(max_health * .5)
                if health > max_health:
                    health = max_health
                potion_sick = 6
            #damage potion : +50% damage for 3 turns
            #7 round potion sickness after use
            elif choice == 'damage potion' and potion_sick < 1:
                d_boost = 1.5
                d_boost_timer = 4
                potion_sick = 8
        #in the event the player has none of the item they selected
        else:
            print('You do not have any of that item')
            player_use_item(max_health, health, attack, items, en_health, en_defense, last_player_action, potion_sickness, d_boost, d_boost_timer)
        
        #if the player has selected a damage potion
        if 'damage' in choice:
            print('You will deal', d_boost, 'times damage for', d_boost_timer - 1, 'turns.')
        
        #if the player has selected a potion
        if 'potion' in choice:
            print('You have potion sickness for', potion_sick - 1, 'turns.')
    
    #retries the turn if the player does not want to use an item
    elif choice == 'cancel':
        player_turn(max_health, health, attack, items, en_health, en_defense, last_player_action, potion_sickness, d_boost, d_boost_timer)
    
    #in the event the player selected an invalid item
    else:
        print('Invalid input, try again.')
        player_use_item(items, max_health, health, potion_sick, d_boost, d_boost_timer)

#1/7 chance to run away
def player_run():
    run = random.rand_int(0,6)
    if run == 0:
        print('You got away safely.')
        return True
    else:
        print('You couldn\'t get away.')
        return False

#player chooses what they will do during their turn
def player_turn(max_health, health, attack, items, en_health, en_defense, last_player_action, potion_sickness, d_boost, d_boost_timer):
    
    ran = False
    
    player_choice = input('Do you want to attack (attack), use an item (item), run (run), or preform the previous action (press enter): ').lower()
    if player_choice == '' or player_choice == 'attack' or player_choice == 'item' or player_choice == 'run':
        if player_choice != '':
            last_player_action = player_choice
        if last_player_action == 'attack':
            en_health = player_attack(en_health, en_defense, attack, d_boost)
        elif last_player_action == 'item':
            player_use_item(max_health, health, attack, items, en_health, en_defense, last_player_action, potion_sickness, d_boost, d_boost_timer)
        else:
            ran = player_run()    
    else:
        #validates recalls the function if the player entered an invalid input
        print('Invalid input, try again.')
        health, items, last_player_action, potion_sickness, d_boost, d_boost_timer, ran = player_turn(max_health, health, attack, items, en_health, en_defense, last_player_action, potion_sickness, d_boost, d_boost_timer)
    
    '''
    if the player is still potion sick the game removes a count of potion sickness and checks if it was a damage potion. 
    If so the program also removes a count of the damage boost timer
    '''
    if potion_sickness > 0:
        potion_sickness -=1
        if d_boost_timer > 0:
            d_boost_timer -=1
            if d_boost_timer == 0:
                d_boost = 1


    #returns all variables that can possibly change in this function
    return health, items, last_player_action, potion_sickness, d_boost, d_boost_timer, ran    
        

#The enemy will attack unless it is a goblin
#if the enemy is a goblin there is a chance for it to steal one of the items that the player has the most of
def en_turn(en_health, health, defense, en_attack, is_goblin):
    print('yippee')

def combat(end_game, health, max_health, attack, defense, items, exp, max_exp, level):
    '''
    creates the enemy and enemy type
    sets the en_max_health variable the the enemy's starting health
    this is so that the program can calculate how much exp the player should recieve
    '''
    en_health, en_attack, en_defense, is_goblin = generate_enemy(level)
    en_max_health = en_health
    
    '''
    initializes the players combat variables
    '''
    last_player_action = None
    run = False   
    d_boost_timer = 0
    d_boost = 1
    potion_sickness = 0


    while en_health > 0 and health > 0 and not(run):
        print('You:', health,'/',max_health,'HP\nEnemy',en_health,'/',en_max_health,'HP')
        health, items, last_player_action, potion_sickness, d_boost, d_boost_timer, run = player_turn(max_health, health, attack, items, en_health, en_defense, last_player_action, potion_sickness, d_boost, d_boost_timer)
        en_turn()
        time.sleep(2)
        print(CLEAR)
    return end_game, health, max_health, attack, defense, items, exp, max_exp, level

def generate_item(items, level):
    item = random.randint(0,6)
    if item == 0:
        items['berry'] += 1
        print("You found a berry!")
    elif item == 1:
        items['bandage'] += 1
        print('You found a bandage!')
    elif item == 2:
        items['lesser healing potion'] += 1
        print('You found a lesser healing potion!')
    elif item == 3:
        items['lesser damage potion'] += 1
        print('You found a lesser damage potion!')
    elif item == 4 and level >= 15:
        items['healing potion'] += 1
        print('You found a healing potion')
    elif item == 5 and level >= 15:
        items['damage potion'] += 1
        print('You found a damage potion!')
    else:
        print('An empty room...')
    return items

def new_room(end_game, health, max_health, attack, defense, items, exp, max_exp, level, move):
    room = random.randint(0, 4)
    if room < 2:
        print("An empty room...")
    elif room == 3:
        items = generate_item(items, level)
    else:
        end_game, health, max_health, attack, defense, items, exp, max_exp, level = combat(end_game, health, max_health, attack, defense, items, exp, max_exp, level)
    moves = generate_room(move)
    move = player_movement(moves)
    return end_game, health, max_health, attack, defense, items, exp, max_exp, level, move

def valid_input(moves, player_move):
    if player_move in moves:    
        if moves[player_move]:
            return True
        else:
            print('You can\'t go that way')
            return False
    else:
        print('Invalid input try again.')
        return False

def player_movement(moves):
    player_move = input("Enter which direction would you like to move. \n(up, down, left, right)\n_______________\n")
    player_move = player_move.lower()
    while not(valid_input(moves, player_move)):
        player_move = input("Enter which direction would you like to move. \n(up, down, left, right)\n_______________\n")
    return player_move

def starting_room():
    moves = {'up':True, 'down':False, 'left':False, 'right':False}
    print("xxxxxxxxxx/////////xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxxxxxx_________xxxxxxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx        O        xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxx                 xxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    move = player_movement(moves)
    return move

def beginning():
    end_game = None
    health = 100
    max_health = 100
    attack = 7
    defense = 0
    items = {'berry':0, 'bandage':0, 'lesser healing potion':0, 'lesser damage potion':0, 'healing potion':0, 'damage potion':0}
    exp = 0
    max_exp = 50
    level = 1
    move = starting_room()
    moves = {'up':False, 'down':False, 'left':False, 'right':False}
    while health > 0 and end_game != 1:
        if health < max_health:
            health += int(max_health * .05)
            if health > max_health:
                health = max_health
        end_game, health, max_health, attack, defense, items, exp, max_exp, level, move = new_room(end_game, health, max_health, attack, defense, items, exp, max_exp, level, move)
        print(CLEAR)

def main():
    start = None
    print("Welcome to fune 4\nThis rendition focuses on incorporating a user interface into gameplay\nHave fun!")
    start = input("Press enter to begin: ")
    while start != '':
        start = input("Press ONLY enter to begin")
    beginning()
    

main()