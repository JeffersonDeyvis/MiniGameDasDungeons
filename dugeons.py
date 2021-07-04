#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import exit
import random
import time
import os

def clean_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def starting():
    clean_terminal()
    for i in range(1,6):
        clean_terminal()
        print("welcome to the dungeons\n")
        a = str("."*i)
        print("starting"+a)
        time.sleep(0.4)
    clean_terminal()

def loser():
    lost = "YOU LOST "
    Face = ":( "
    clean_terminal()
    for i in range(4):
        lost_string   = Face*i
        print('\n' + lost + lost_string)
        time.sleep(0.5)
        clean_terminal()

def board():
    caracter = "*"*5 + "@"*10 +"#"*20 + "^"*30 +"_"*35
    matrix   = []

    for k in range(10):
        matrix.append(["0"]*10)
    for i in range(10):
        for j in range(10):
            matrix[i][j] = random.choice(caracter)
    matrix[0][0] = "T"
    matrix[9][9] = "P"

    return matrix
    

def movement(matrix,string, word):
    for l in range(10):
        for c in range(10):
            if matrix[l][c] == "P":
                x,y = l,c

    if string=="l":
        return matrix, word

    if string=="w":
        if (x,y) == (9,9):
            word        = matrix[x-1][y]
            matrix[ 9 ][9]  = " "
            matrix[x-1][y]  = "P"
            return matrix, word
        elif x == 0:
            print("\nyou are on the north edge\n".upper())
            return matrix, word
        else:
            matrix[x][y]    = word
            word            = matrix[x-1][y]
            matrix[x-1][y]  = "P"
            if (x-1,y) == (0,0):
                victory()
                time.sleep(2)
                return exit()
            else:
                return matrix, word
        
    elif string=="s":
        if x == 9:
            print("\nyou are on the south edge\n".upper())
            return matrix,word
        else:
            matrix[x][y]    = word
            word        = matrix[x+1][y]
            matrix[x+1][y]  = "P"
            return matrix, word
    
    elif string=="d":
        if y == 9:
            print("\nyou are on the east edge\n".upper())
            return matrix,word
        else:
            matrix[x][y]    = word
            word        = matrix[x][y+1]
            matrix[x][y+1]  = "P"
            return matrix, word
    
    elif string=="a":
        if (x,y) == (9,9):
            word        = matrix[x][y-1]
            matrix[ 9 ][9]  = " "
            matrix[x][y-1]  = "P"
            return matrix, word
        elif y == 0:
            print("\nyou are on the west edge\n".upper())
            return matrix,word
        else:
            matrix[x][y] = word
            word = matrix[x][y-1]
            matrix[x][y-1] = "P"
            if (x,y-1) == (0,0):
                victory()
                time.sleep(2)
                return exit()
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
    victory = "YOU WIN"
    for i in range(21):
        line    = "*"*i
        clean_terminal()
        print(line)
        print(victory.center(i))
        print(line)
        time.sleep(0.1)
        clean_terminal()


def print_movement(matrix):
    #clean_terminal()
    for l in range(10):
        s = ''
        for c in range(10):
            cc = matrix[l][c]
            s += str(cc + "  ")
        print(s)


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

        s4 = str("\n%s; LIFE - %d; POTIONS - %d.  " %(status, v, potion))
        print(s4)
        print_movement(a)
        while True:
            
            string  = "\nMOVE ON: A(\u2190), W(\u2191), S(\u2193), OR D(\u2192)  OR HEAL YOURSELF: L \u279c "
            m       = str.lower(input(string))
            b,L     = movement(a,m,l)
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
                lost = 'Did you give up'
                print(lost.center(40,'*'))
                time.sleep(1)
                clean_terminal()
                time.sleep(0.5)
                break
            clean_terminal()
            s5 = str("\n%s; LIFE - %d; POTIONS - %d.  " %(status, life, potion))
            print(s5)
            print_movement(b)
            
            a = b 
            l = L
        play_again = str(input("do you want to play again (Y/N)? ")).lower()
        if play_again == 'y':
            T = True
        elif play_again == 'n':
            T = False
        else: play_again

        

call()