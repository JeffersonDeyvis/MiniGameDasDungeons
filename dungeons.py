#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import exit
import random
import time
import os

class colors:
    white           = '\033[37m'
    cyan            = '\033[1;96m'
    yellow          = '\033[33m'
    red             = '\033[31m'
    green           = '\033[32m'
    blue            = '\033[34m'
    light_magenta   = '\033[1;95m'
    end             = '\033[0;0m'


def clean_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def starting():
    clean_terminal()
    for i in range(1,6):
        clean_terminal()
        print(colors.yellow + "welcome to the dungeons" + colors.end + '\n')
        a = str(colors.green + "."*i + colors.end)
        print(colors.green + "starting"+a + colors.end)
        time.sleep(0.4)
    clean_terminal()

def loser():
    lost = colors.red + "YOU LOST " + colors.end
    Face = colors.red + ":( " + colors.end
    clean_terminal()
    for i in range(4):
        lost_string   = Face*i
        print('\n' + lost + lost_string)
        time.sleep(0.5)
        clean_terminal()

def board():
    q = str(colors.cyan + 'P' + colors.end)
    caracter = "*"*5 + "@"*10 +"#"*20 + "^"*30 +"_"*35
    matrix   = []

    for k in range(10):
        matrix.append(["0"]*10)
    for i in range(10):
        for j in range(10):
            matrix[i][j] = random.choice(caracter)
    matrix[0][0] = "T"
    matrix[9][9] = q

    return matrix
    
def movement(matrix,string, word):
    q = str(colors.cyan + 'P' + colors.end)
    for l in range(10):
        for c in range(10):
            if matrix[l][c] == q:
                x,y = l,c

    if string=="l":
        return matrix, word

    if string=="w":
        if (x,y) == (9,9):
            word        = matrix[x-1][y]
            matrix[ 9 ][9]  = " "
            matrix[x-1][y]  = q
            return matrix, word
        elif x == 0:
            print("\nyou are on the north edge\n".upper())
            time.sleep(2)
            return matrix, word
        else:
            matrix[x][y]    = word
            word            = matrix[x-1][y]
            matrix[x-1][y]  = q
            if (x-1,y) == (0,0):
                victory()
                time.sleep(2)
                return 0,0
            else:
                return matrix, word
        
    elif string=="s":
        if x == 9:
            print("\nyou are on the south edge\n".upper())
            time.sleep(2)
            return matrix,word
        else:
            matrix[x][y]    = word
            word        = matrix[x+1][y]
            matrix[x+1][y]  = q
            return matrix, word
    
    elif string=="d":
        if y == 9:
            print("\nyou are on the east edge\n".upper())
            time.sleep(2)
            return matrix,word
        else:
            matrix[x][y]    = word
            word        = matrix[x][y+1]
            matrix[x][y+1]  = q
            return matrix, word
    
    elif string=="a":
        if (x,y) == (9,9):
            word        = matrix[x][y-1]
            matrix[ 9 ][9]  = " "
            matrix[x][y-1]  = q
            return matrix, word
        elif y == 0:
            print("\nyou are on the west edge\n".upper())
            time.sleep(2)
            return matrix,word
        else:
            matrix[x][y] = word
            word = matrix[x][y-1]
            matrix[x][y-1] = q
            if (x,y-1) == (0,0):
                victory()
                time.sleep(2)
                return 0,0
            else:
                return matrix, word
    else:
        return matrix, word

def life_implement(word,string,life):
    caractere = {'_':0, '^':-15, '#':-25, '@':-40, '*':-60,'l':20,'':0}    
    
    if string == 'l':
        l = caractere[string]
    elif word in caractere:
        l = caractere[word]
    else: return life
    
    life += l
    if life > 100:
        return 100
    else: return life

def victory():
    victory = colors.green + "YOU WIN" + colors.end
    for i in range(21):
        line    = colors.green + "*"*i + colors.end
        clean_terminal()
        print(line)
        print(victory.center(i))
        print(line)
        time.sleep(0.1)
        clean_terminal()

def print_movement(matrix):
    for l in range(10):
        s = ''
        for c in range(10):
            cc = matrix[l][c]
            s += str(cc + "  ")
        print(s)

def help(FUNCTION):
    clean_terminal()
    board = '*       HELP!      *'
    l = len(board)
    line  = '*'*l
    border = '*'+' '*(l-2) +'*' 
    d = 'TRAP DAMAGE'
    print(line)
    print(board)
    print(line)
    print('*' + d.center(l-2) + '*')
    print('*' + '_  \u2192  0 damage'.center(l-2) + '*')
    print('*' + '^  \u2192 15 damage'.center(l-2) + '*')
    print('*' + '#  \u2192 25 damage'.center(l-2) + '*')
    print('*' + '@  \u2192 40 damage'.center(l-2) + '*')
    print('*' + '*  \u2192 60 damage'.center(l-2) + '*')
    print('*' + 'l  \u2192 20 HP    '.center(l-2) + '*')
    print(line)
    print('*' + 'MOVEMENT'.center(l-2) + '*')
    print(border)
    print('*' + 'W  ... (\u2191)'.center(l-2) + '*')
    print('*' + 'S  ... (\u2193)'.center(l-2) + '*')
    print('*' + 'A  ... (\u2190)'.center(l-2) + '*')
    print('*' + 'D  ... (\u2192)'.center(l-2) + '*')
    print(border)
    print(line)
    key = str(input("\nPRESS ANY KEY..."))
    time.sleep(1)
    return (FUNCTION)
    
def call():
    T = True
    status  = str(input("\nTYPE YOUR NAME: ")).upper()
    while T == True:
        clean_terminal()
        starting()   
        a = board()
        l       = ''
        v       = 100
        potion  = 3

        s4 = str("\n%s; LIFE - %d; POTIONS - %d. " %(status, v, potion))
        print(colors.light_magenta + s4 + colors.end)
        print_movement(a)
        while True:
            
            string  = "\nTYPE: A(\u2190), W(\u2191), S(\u2193), D(\u2192), L, HELP, OR EXIT \u2192 "
            m       = str.lower(input(string))

            if m == 'help'.lower():
                b,L = help(movement(a,m,l))
            else:
                b,L     = movement(a,m,l)
                
            if b == 0:
                break
            life    = life_implement(L,m,v)
            v       = life
            if m == "l" or m =="L":
                potion -= 1
            if potion   <= 0:
                potion = 0
            if life     <= 0:
                loser()
                time.sleep(1)
                clean_terminal()
                time.sleep(0.5)
                break
                
            if m == "exit":
                clean_terminal()
                time.sleep(1)
                lost = 'Did you give up'
                print('\n'+ lost.center(40,'*') + "\n")
                time.sleep(.5)
                print(colors.red + "ENDING THE GAME..." + colors.end)
                time.sleep(1)
                clean_terminal()
                time.sleep(0.5)
                break
            clean_terminal()
            s5 = str("\n%s; LIFE - %d; POTIONS - %d.  " %(status, life, potion))
            print(colors.light_magenta + s5 + colors.end)
            print_movement(b)
            
            a = b 
            l = L
        play_again = str(input("do you want to play again (Y/N)? ")).lower()
        if play_again == 'y':
            T = True
        elif play_again == 'n':
            print(colors.red + "ENDING THE GAME..." + colors.end)
            time.sleep(1)
            clean_terminal()
            T = False
        else: play_again

call()