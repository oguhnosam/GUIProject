'''
Hugo May
fune game version 4
integrating user interface
'''


import os
import time
import math
import random
import v4_library as libe
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk

moves = {'up':True, 'down':False, 'left':False, 'right':False}
player = None
mainframe = None
frame2 = None
info = None
btn_up = None
btn_down = None
btn_left = None
btn_right = None
btn_show_stats = None
btn_back = None
btn_attack = None
btn_items = None
btn_run = None
new_enemy = None
player_info = None
enemy_info = None



#beginning of making the rooms

def rm1():
    global room1
    global moves
    global new_room
    new_room.grid_remove()
    new_room = ttk.Label(mainframe, image = room1)
    new_room.grid(column = 0, row = 0)
    moves['up'] = True
    moves['down'] = False
    moves['left'] = False
    moves['right'] = False

def rm2():
    global room2
    global moves
    global new_room
    new_room.grid_remove()
    new_room = ttk.Label(mainframe, image = room2)
    new_room.grid(column = 0, row = 0)
    moves['up'] = True
    moves['down'] = False
    moves['left'] = False
    moves['right'] = True

def rm3():
    global room3
    global moves
    global new_room
    new_room.grid_remove()
    new_room = ttk.Label(mainframe, image = room3)
    new_room.grid(column = 0, row = 0)
    moves['up'] = True
    moves['down'] = True
    moves['left'] = False
    moves['right'] = True
    

def rm5():
    global room6
    global moves
    global new_room
    new_room.grid_remove()
    new_room = ttk.Label(mainframe, image = room5)
    new_room.grid(column = 0, row = 0)
    moves['up'] = False
    moves['down'] = False
    moves['left'] = False
    moves['right'] = True

def rm6():
    global room7
    global moves
    global new_room
    new_room.grid_remove()
    new_room = ttk.Label(mainframe, image = room6)
    new_room.grid(column = 0, row = 0)
    moves['up'] = False
    moves['down'] = True
    moves['left'] = False
    moves['right'] = True

def rm7():
    global room8
    global moves
    global new_room
    new_room.grid_remove()
    new_room = ttk.Label(mainframe, image = room7)
    new_room.grid(column = 0, row = 0)
    moves['up'] = False
    moves['down'] = True
    moves['left'] = True
    moves['right'] = True

def rm8():
    global room9
    global moves
    global new_room
    new_room.grid_remove()
    new_room = ttk.Label(mainframe, image = room8)
    new_room.grid(column = 0, row = 0)
    moves['up'] = False
    moves['down'] = True
    moves['left'] = False
    moves['right'] = False

def rm9():
    global room10
    global moves
    global new_room
    new_room.grid_remove()
    new_room = ttk.Label(mainframe, image = room9)
    new_room.grid(column = 0, row = 0)
    moves['up'] = False
    moves['down'] = True
    moves['left'] = True
    moves['right'] = False

def rm10():
    global room1
    global moves
    global new_room
    new_room.grid_remove()
    new_room = ttk.Label(mainframe, image = room10)
    new_room.grid(column = 0, row = 0)
    moves['up'] = True
    moves['down'] = False
    moves['left'] = True
    moves['right'] = True

def rm11():
    global room11
    global moves
    global new_room
    new_room.grid_remove()
    new_room = ttk.Label(mainframe, image = room11)
    new_room.grid(column = 0, row = 0)
    moves['up'] = False
    moves['down'] = False
    moves['left'] = True
    moves['right'] = False

def rm12():
    global room12
    global moves
    global new_room
    new_room.grid_remove()
    new_room = ttk.Label(mainframe, image = room12)
    new_room.grid(column = 0, row = 0)
    moves['up'] = True
    moves['down'] = False
    moves['left'] = True
    moves['right'] = False

def rm13():
    global room13
    global moves
    global new_room
    new_room.grid_remove()
    new_room = ttk.Label(mainframe, image = room13)
    new_room.grid(column = 0, row = 0)
    moves['up'] = True
    moves['down'] = False
    moves['left'] = True
    moves['right'] = True

def rm14():
    global room14
    global moves
    global new_room
    new_room.grid_remove()
    new_room = ttk.Label(mainframe, image = room14)
    new_room.grid(column = 0, row = 0)
    moves['up'] = False
    moves['down'] = False
    moves['left'] = True
    moves['right'] = True

def rm15():
    global room15
    global moves
    global new_room
    new_room.grid_remove()
    new_room = ttk.Label(mainframe, image = room15)
    new_room.grid(column = 0, row = 0)
    moves['up'] = True
    moves['down'] = True
    moves['left'] = False
    moves['right'] = False
#end of making rooms



#creates a new random enemy
def generate_enemy():
    global player
    global new_enemy
    en_type = random.randint(1,4)
    if en_type != 4:
        new_enemy = libe.enemy(level = player.level, type = en_type)
    else:
        new_enemy = libe.goblin(level = player.level, type = en_type)

#hides the movement buttons
def hide_buttons():
    global player
    global info
    global new_room
    global mainframe
    global btn_up
    global btn_down
    global btn_left
    global btn_right
    global btn_show_stats
    global btn_back

    #hides controller buttons
    btn_show_stats.grid_remove()
    btn_up.grid_remove()
    btn_down.grid_remove()
    btn_left.grid_remove()
    btn_right.grid_remove()

    #hides main display elements
    new_room.grid_remove()
    info.grid_remove()

#shows the hidden buttons
def restore_buttons():
    global new_room
    global btn_up
    global btn_down
    global btn_left
    global btn_right
    global btn_show_stats

    btn_show_stats.grid(row = 2, column = 0, columnspan = 2)
    btn_up.grid(column = 0, row = 0)
    btn_down.grid(column = 1, row = 0)
    btn_left.grid(column = 0, row = 1)
    btn_right.grid(column = 1, row = 1)
    new_room.grid(row = 0, column = 0)

#damages the player
def enemy_turn():
    global player
    global new_enemy
    global info
    global info2
    global damage_taken

    damage = new_enemy.attack

    high_roll = int(damage*.2)
    low_roll = int(damage*-.15)

    damage += random.randint(low_roll, high_roll)

    if random.randint(0, 12) == 1:
        crit = True
    else:
        crit = False

    if crit:
        damage *= 2

    if random.randint(1, 15) == 1:
        miss = True
    else:
        miss = False
    

    info2.grid_remove()
    if miss:
        info2 = ttk.Label(mainframe, text = 'The enemy lunged at you but missed!')
    else:
        if not crit:
            info2 = ttk.Label(mainframe, text = f'The enemy did {damage} damage!')
        else:
            info2 = ttk.Label(mainframe, text = f'The enemy did {damage} damage!\nA cricical hit!')

    info2.grid(row = 2, column = 0, columnspan = 2)


    player.stats['Health'] -= damage
    damage_taken += damage

#grants the player exp based on the enemy's strength, damage taken, and extra damage dealt
def end_combat():
    global player
    global new_enemy
    global mainframe
    global player_info
    global enemy_info
    global enemy_picture
    global enemy_max_health
    global info
    global info2
    global new_room
    global over_damage
    global damage_taken

    info.grid_remove()
    info2.grid_remove()
    player_info.grid_remove()
    enemy_info.grid_remove()
    enemy_picture.grid_remove()

    new_room.grid(row = 0, column = 0)

    restore_buttons()

    exp_gain = int(enemy_max_health/2 + over_damage + damage_taken/5)

    player.stats['Exp'] += exp_gain

    if player.stats['Exp'] > player.stats['Exp Requirement']:
        player.stats['Exp'] -= player.stats['Exp Requirement']
        player.stats['Exp Requirement'] = int(player.stats['Exp Requirement'] * 1.2)
        player.level += 1
        player.stats['Attack'] += 2
        player.stats['Max Health'] += 5
        player.stats['Health'] = player.stats['Max Health']
        info2 = ttk.Label(mainframe, text = 'You leveled up!')
        info2.grid(column = 0, row = 2)
    
    info = ttk.Label(mainframe, text = f'You defeated the {new_enemy.type}!\nYou gained {exp_gain} Exp!')
    info.grid(row = 1, column = 0)

#closes both windows
def quit_game():
    global controller
    global room

    room.destroy()
    controller.destroy()

#restarts the game
def play_again():
    global btn_quit
    global btn_play_again
    global info

    btn_quit.grid_remove()
    btn_play_again.grid_remove()
    info.grid_remove()

    beginning()

#if the player has died they can choose to end the game or try again
def end_game():
    global player
    global info
    global player_info
    global enemy_info
    global enemy_picture
    global info2
    global mainframe
    global frame2
    global btn_quit
    global btn_play_again
    player_info.grid_remove()
    enemy_info.grid_remove()
    enemy_picture.grid_remove()
    info2.grid_remove()
    info.grid_remove()
    if player.stats['Health'] < 1:
        info = ttk.Label(mainframe, text = f'You died.\nThe enemy had {new_enemy.health} health left.\nYou were level {player.level}.')
        info.grid(row = 0, column = 0)
        btn_quit = ttk.Button(frame2, text = 'Quit', command = quit_game)
        btn_play_again = ttk.Button(frame2, text = 'Play Again', command = play_again)
        btn_quit.grid(row = 0, column = 1)
        btn_play_again.grid(row = 0, column = 0)


    
#damages the enemy based on the player's attack stat and a random floor and celing
def player_attack():
    global player
    global new_enemy
    global mainframe
    global player_info
    global enemy_info
    global info
    global btn_attack
    global btn_items
    global btn_run
    global over_damage

    btn_attack.grid_remove()
    btn_items.grid_remove()
    btn_run.grid_remove()
    
    damage = player.stats['Attack']

    high_roll = int(damage*.2)
    low_roll = int(damage*-.15)

    damage += random.randint(low_roll, high_roll)

    if random.randint(0, 8) == 1:
        crit = True
    else:
        crit = False

    if crit:
        damage *= 2

    if random.randint(1, 15) == 1:
        miss = True
    else:
        miss = False
    

    info.grid_remove()
    if miss:
        info = ttk.Label(mainframe, text = 'You swung your sword but missed!')
    else:
        info = ttk.Label(mainframe, text = f'You did {damage} damage!')
    info.grid(row = 1, column = 0, columnspan = 2)


    new_enemy.health -= damage


    if not new_enemy.health < 1:
        enemy_turn()
        player_turn()
    else:
        over_damage = abs(new_enemy.health)
        end_combat()

    
#will allow the player to use the items they have collected
def player_use_item():
    global btn_back
    global btn_attack
    global btn_run
    global btn_items

    btn_attack.grid_remove()
    btn_run.grid_remove()
    btn_items.grid_remove()

    btn_back = ttk.Button(frame2, text = 'Back', command = player_turn)
    btn_back.grid(row = 0, column = 0)

#will allow the player to run from the fight
def player_run():
    pass

#creates the player's combat actions
def player_turn():
    global frame2
    global btn_attack
    global btn_items
    global btn_run
    global btn_back
    global player_info
    global enemy_info
    global enemy_max_health


    if btn_back.winfo_ismapped:
        btn_back.grid_remove()

    if player.stats['Health'] < 1:
        end_game()
    else:
        btn_attack.grid(row = 0, column = 0)
        btn_items.grid(row = 0, column = 1)
        btn_run.grid(row = 1, column = 0, columnspan = 2)
        player_info.grid_remove()
        enemy_info.grid_remove()
        player_info = ttk.Label(mainframe, text =f'You:\nHealth: {player.stats['Health']}/{player.stats['Max Health']}\nDefense: {player.stats['Defense']}')
        enemy_info = ttk.Label(mainframe, text = f'Enemy:\nHealth: {new_enemy.health}/{enemy_max_health}\nDefense: {new_enemy.defense}')
        player_info.grid(row = 3, column = 0)
        enemy_info.grid(row = 3, column = 1)
    

#creates a new enemy and begins combat
def combat():
    global player
    global new_enemy
    global enemies
    global orc
    global armored_orc
    global goblin
    global wolf
    global player_info
    global enemy_info
    global enemy_max_health
    global info2
    global enemy_picture
    global damage_taken
    damage_taken = 0
    info2 = ttk.Label(mainframe, text = '')
    player_info = ttk.Label(mainframe, text = '')
    enemy_info = ttk.Label(mainframe, text = '')
    hide_buttons()
    generate_enemy()
    enemy_max_health = new_enemy.health
    enemy_picture = ttk.Label(mainframe, image = enemies[new_enemy.type])
    enemy_picture.grid(row = 0, column = 0, columnspan = 2)
    player_turn()

#randomly selects an item and gives it to the player
def generate_item():
    global player
    global info
    global mainframe
    item = random.randint(0,6)
    if item == 0:
        player.inventory['berry'] += 1
        info.grid_remove()
        info = ttk.Label(mainframe, text = 'You found a berry!')
        info.grid(column = 0, row = 1)
    elif item == 1:
        player.inventory['bandage'] += 1
        info.grid_remove()
        info = ttk.Label(mainframe, text = 'You found some bandages!')
        info.grid(column = 0, row = 1)
    elif item == 2:
        player.inventory['lesser healing potion'] += 1
        info.grid_remove()
        info = ttk.Label(mainframe, text = 'You found a lesser healing potion!')
        info.grid(column = 0, row = 1)
    elif item == 3:
        player.inventory['lesser damage potion'] += 1
        info.grid_remove()
        info = ttk.Label(mainframe, text = 'You found a lesser damage potion!')
        info.grid(column = 0, row = 1)
    elif item == 4 and player.level >= 15:
        player.inventory['healing potion'] += 1
        info.grid_remove()
        info = ttk.Label(mainframe, text = 'You found a healing potion!')
        info.grid(column = 0, row = 1)
    elif item == 5 and player.level >= 15:
        player.inventory['damage potion'] += 1
        info.grid_remove()
        info = ttk.Label(mainframe, text = 'You found a damage potion!')
        info.grid(column = 0, row = 1)
    else:
        info.grid_remove()
        info = ttk.Label(mainframe, text = 'An empty room...')
        info.grid(column = 0, row = 1)

#creates a new room and decided what will happen with it, along with restoring 5 percent of the player's health
def room_event():
    global info
    global mainframe
    global player

    player.stats['Health'] += int(player.stats['Max Health'] *.05)
    if player.stats['Health'] > player.stats['Max Health']:
        player.stats['Health'] = player.stats['Max Health']

    num = random.randint(1,4)
    if num == 1:
        info.grid_remove()
        info = ttk.Label(mainframe, text = 'An empty room...')
        info.grid(column = 0, row = 1)
    elif num == 2 or num == 3:
        info.grid_remove()
        combat()
    elif num == 4:
        info.grid_remove()
        generate_item()


#checks if the player can move up and if so they move into a new room
def try_up():
    global moves
    global info
    global mainframe
    global info2
    info2.grid_remove()

    if moves['up']:
        num = random.randint(1,7)
        if num == 1:
            rm1()
        elif num == 2:
            rm2()
        elif num == 3:
            rm5()
        elif num == 4:
            rm11()
        elif num == 5:
            rm12()
        elif num == 6:
            rm13()
        elif num == 7:
            rm14()
        info.grid_remove()
        room_event()
    else:
        info.grid_remove()
        info = ttk.Label(mainframe, text = 'You cant go that way!')
        info.grid(column = 0, row = 1)


#checks if the player can move down and if so they move into a new room
def try_down():
    global moves
    global info
    global mainframe
    global info2
    info2.grid_remove()

    if moves['down']:
        num = random.randint(1,7)
        if num == 1:
            rm5()
        elif num == 2:
            rm6()
        elif num == 3:
            rm7()
        elif num == 4:
            rm8()
        elif num == 5:
            rm9()
        elif num == 6:
            rm11()
        elif num == 7:
            rm14()
        info.grid_remove()
        room_event()
    else:
        info.grid_remove()
        info = ttk.Label(mainframe, text = 'You cant go that way!')
        info.grid(column = 0, row = 1)

#checks if the player can move left and if so they move into a new room
def try_left():
    global moves
    global info
    global mainframe
    global info2
    info2.grid_remove()

    if moves['left']:
        num = random.randint(1,7)
        if num == 1:
            rm1()
        elif num == 2:
            rm8()
        elif num == 3:
            rm9()
        elif num == 4:
            rm11()
        elif num == 5:
            rm12()
        elif num == 6:
            rm10()
        elif num == 7:
            rm15()        
        info.grid_remove()
        room_event()
    else:
        info.grid_remove()
        info = ttk.Label(mainframe, text = 'You cant go that way!')
        info.grid(column = 0, row = 1)

#checks if the player can move right and if so they move into a new room
def try_right():
    global moves
    global info
    global mainframe
    global info2
    info2.grid_remove()

    if moves['right']:
        num = random.randint(1,7)
        if num == 1:
            rm1()
        elif num == 2:
            rm2()
        elif num == 3:
            rm3()
        elif num == 4:
            rm5()
        elif num == 5:
            rm6()
        elif num == 6:
            rm8()
        elif num == 7:
            rm15()
        info.grid_remove()
        room_event() 
    else:
        info.grid_remove()
        info = ttk.Label(mainframe, text = 'You cant go that way!')
        info.grid(column = 0, row = 1)

#restores the buttons and gui and removes the player stats
def hide_stats():
    global info
    global new_room
    global mainframe
    global btn_up
    global btn_down
    global btn_left
    global btn_right
    global btn_show_stats
    global btn_back

    #hides back button and stats
    btn_back.grid_remove()
    info.grid_remove()

    #restores buttons and gui
    restore_buttons()


#shows the player's attributes and stats
def show_stats():
    global player
    global info
    global new_room
    global mainframe
    global btn_up
    global btn_down
    global btn_left
    global btn_right
    global btn_show_stats
    global btn_back

    #hides buttons
    hide_buttons()

    #displays the stats
    info = ttk.Label(mainframe, text = str(player))
    info.grid(row = 1, column = 0)

    #makes back button
    btn_back = ttk.Button(frame2, text = "Back", command = hide_stats)
    btn_back.grid(row = 0, column = 0)

#creates the controller and all of the buttons it can use
def make_controller():
    global frame2
    global btn_up
    global btn_down
    global btn_left
    global btn_right
    global btn_show_stats
    global btn_attack
    global btn_items
    global btn_run
    global btn_back
    
    btn_up = ttk.Button(frame2, text = 'Up', command = try_up)
    btn_up.grid(column = 0, row = 0)
    btn_down = ttk.Button(frame2, text = 'Down', command = try_down)
    btn_down.grid(column = 1, row = 0)
    btn_left = ttk.Button(frame2, text = 'Left', command = try_left)
    btn_left.grid(column = 0, row = 1)
    btn_right = ttk.Button(frame2, text = 'Right', command = try_right)
    btn_right.grid(column = 1, row = 1)
    btn_show_stats = ttk.Button(frame2, text = "Show Stats", command = show_stats)
    btn_show_stats.grid(column = 0, row = 2, columnspan = 2)
    btn_attack = ttk.Button(frame2, text = 'Attack', command = player_attack)
    btn_items = ttk.Button(frame2, text = 'Items', command = player_use_item)
    btn_run = ttk.Button(frame2, text = 'Run', command = player_run)
    btn_back = ttk.Button(frame2, text = "Back", command = hide_stats)


#creates a player object and initiates the first room
def beginning():
    global player
    global frame2
    global mainframe
    global room
    global controller
    global room1
    global new_room
    global info
    global info2
    global start
    start.grid_remove()

    items = {'berry':0, 'bandage':0, 'lesser healing potion':0, 'lesser damage potion':0, 'healing potion':0, 'damage potion':0}
    player = libe.player(stats = {"Health" : 100, "Max Health" : 100, "Attack" : 7, "Defense" : 0, "Exp Requirement" : 50, "Exp" : 0}, inventory = items, level = 1)
    

    new_room = ttk.Label(mainframe, image = room1)
    new_room.grid(column = 0, row = 0)
    info = ttk.Label(mainframe, text = "This is the first room\nPlease select your move.")
    info.grid(column = 0, row = 1)
    info2 = ttk.Label(mainframe, text = '')
    info2.grid(column = 0, row = 2)
    make_controller()
    

#begins the game and initiates the 2 game windows

def main():
    #accesses needed variables
    global mainframe
    global frame2
    global room
    global controller
    global room1
    global room2
    global room3
    global room4
    global room5
    global room6
    global room7
    global room8
    global room9
    global room10
    global room11
    global room12
    global room13
    global room14
    global room15
    global orc
    global armored_orc
    global goblin
    global wolf
    global enemies
    global start
    #creates the main window
    room = Tk()
    room.title("Current Room")

    mainframe = ttk.Frame(room, padding = '12 12 12 12')
    mainframe.grid(column = 0, row = 0, sticky = (N, W, S, E))
    room.columnconfigure(0, weight = 1)
    room.rowconfigure(0, weight = 1)
    
    #creates the controller window   
    controller = Tk()
    controller.title("Controller")

    frame2 = ttk.Frame(controller, padding = '12 12 12 12')
    frame2.grid(column = 0, row = 0, sticky = (N, W, S, E))
    controller.columnconfigure(0, weight = 1)
    controller.rowconfigure(0, weight = 1)


#start button
    start = ttk.Button(frame2, text = "Start", command = beginning)
    start.grid(column = 0, row = 0)

#defining the rooms as images
    room1 = PhotoImage(file = "rm_1.png")
    room2 = PhotoImage(file = "rm_2.png")
    room3 = PhotoImage(file = "rm_3.png")
    room4 = PhotoImage(file = "rm_4.png")
    room5 = PhotoImage(file = "rm_5.png")
    room6 = PhotoImage(file = "rm_6.png")
    room7 = PhotoImage(file = "rm_7.png")
    room8 = PhotoImage(file = "rm_8.png")
    room9 = PhotoImage(file = "rm_9.png")
    room10 = PhotoImage(file = "rm_10.png")
    room11 = PhotoImage(file = "rm_11.png")
    room12 = PhotoImage(file = "rm_12.png")
    room13 = PhotoImage(file = "rm_13.png")
    room14 = PhotoImage(file = "rm_14.png")
    room15 = PhotoImage(file = "rm_15.png")
    armored_orc = PhotoImage(file = 'armored_orc.png')
    orc = PhotoImage(file = 'orc.png')
    goblin = PhotoImage(file = 'goblin.png')
    wolf = PhotoImage(file = 'wolf.png')
    enemies = {'orc' : orc, 'armored orc' : armored_orc, 'goblin' : goblin, 'wolf' : wolf}


    room.mainloop()


main()