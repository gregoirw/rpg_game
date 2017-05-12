from random import randint
from termcolor import colored
from time import sleep
import time
import datetime
from datetime import date
import os
import maps
import screens
import csv

start_time = int(time.time())

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def load_map(level_map):
    level_map = level_map.split('\n')
    game_map = []
    for element in level_map:
        game_map.append(list(element))
    return game_map

def print_board(game_map):
    for row in game_map:
        for char in row:
            if str(char) == "o" or str(char) == "O":
                print(colored(char, 'blue'), end ='')
            elif str(char) == "A" or str(char) == "a":
                print(colored(char, 'green'), end ='')
            elif str(char) == "#" or str(char) == "$":
                print(colored(char, 'cyan'), end ='')
            elif str(char) == "X" or str(char) == "a":
                print(colored(char, 'white'), end ='')
            elif str(char) == "A" or str(char) == "a":
                print(colored(char, 'green'), end ='')

            else:
                print(char, end='')
        print()


def insert_player(game_map, width, height):
    game_map[width][height] = '@'
    return game_map


def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def movement(ch,x_pos,y_pos,game_map):
    stop=['X','|','/']
    if ch == 'a':
        if game_map[x_pos][y_pos - 1] not in stop:
            return [x_pos,y_pos-1]
        else:
            return [x_pos,y_pos]
    elif ch == 'w':
        if game_map[x_pos - 1][y_pos] not in stop:
            return [x_pos-1,y_pos]
        else:
            return [x_pos,y_pos]
    elif ch == 'd':
        if game_map[x_pos][y_pos + 1] not in stop:
            return [x_pos,y_pos+1]
        else:
            return [x_pos,y_pos]
    elif ch == 's':
        if game_map[x_pos + 1][y_pos] not in stop:
            return [x_pos+1,y_pos]
        else:
            return [x_pos,y_pos]

def hall_of_fame():
    now = str(date.today())
    Ender = int(time.time())
    dif = int((Ender - start_time))
    monsters_killed=12
    collected_items=14

    name = input("What's your name my knight? \n")
    os.system('clear')

    score = (name, str(now), dif, monsters_killed, collected_items)
    print('''
                    CONGRATULATIONS MY FRIEND!!! YOUR SCORE IS:
            ''')
    print("%s |" % name, str(now), "| playing time:", dif, "sec", "| monsters killed:", monsters_killed, "| collected items:", collected_items)

    with open('scores.csv', 'a', newline='') as csvfile:
        scorewriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        scorewriter.writerow(score)

    print('''

                            HALL OF FAME :

                    ''')

    with open('scores.csv', newline='') as csvfile:
        scorereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        score_list = list(scorereader)
#        print(score_list)
        print('''--------------------------------------------------------------------------------------
:    PLAYER NAME    :     DATE    : PLAYING TIME : MONSTERS KILLED : COLLECTED ITEMS :
--------------------------------------------------------------------------------''')
        for score in score_list:
            print(":",score[0]," "*(16-len(score[0])),":",
            score[1]," "*(9-len(score[1])),":",
            score[2],"sec"," "*(7-len(score[2])),":",
            score[3]," "*(14-len(score[3])),":",
            score[4]," "*(14-len(score[4])),":")
        print("--------------------------------------------------------------------------------------")


#def x_movement(ch):
#
#    if ch == 'w' and x_pos > 98:
#        return -1
#    elif ch == 's' and x_pos < 98:
#        return 1
#    else:
#        return 0


def force_exit(ch):
    if ch == 'q':
        exit()

def menu_screen():
    print(screens.start_screen)




def main():
    x_pos = 3
    y_pos = 53
    level=1
    menu_screen()
    while level == 1:
        character = getch()
        force_exit(character)
        os.system('clear')
        level_map = maps.level_1_map
        board = load_map(level_map)
        new_pos = movement(character, x_pos, y_pos,board)
        x_pos = new_pos[0]
        y_pos = new_pos[1]

        board_with_player = insert_player(board, x_pos, y_pos)
        print_board(board_with_player)
        if x_pos == 35 and y_pos == 97 or x_pos == 34 and y_pos == 97:
            os.system('clear')
            level = 2
    while level == 2:
        character = getch()
        force_exit(character)
        os.system('clear')
        level_map = maps.level_2_map
        board = load_map(level_map)
        new_pos = movement(character, x_pos, y_pos,board)
        x_pos = new_pos[0]
        y_pos = new_pos[1]

        board_with_player = insert_player(board, x_pos, y_pos)
        print_board(board_with_player)
        if x_pos == 2 and y_pos == 2:
            os.system('clear')
            hall_of_fame()
main()
