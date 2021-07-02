#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cores import colors
from sys import exit
import random
import time

s1  = str('\n***bem vindo a Dungeon***\n')
print(colors("branco","magenta",s1))

def board():
    caracter = []
    count = 0
    while count < 100:
        if  count >= 0 and count < 5:
            caracter.append("*")
        elif count >= 5 and count < 15:
            caracter.append("@")
        elif count >= 15 and count < 35:
            caracter.append("#")
        elif count >= 35 and count < 65:
            caracter.append("^")
        elif count >= 65 and count < 100:
            caracter.append("_")
        count += 1
        
    matrix = []
    for k in range(10):
        matrix.append(["0"]*10)
    for i in range(10):
        for j in range(10):
            matrix[i][j] = random.choice(caracter)
    matrix[0][0] = "T"
    matrix[9][9] = "P"

    return matrix
    

def movement(matrix,string, lista):
    for l in range(10):
        for c in range(10):
            if matrix[l][c] == "P":
                x,y = l,c

    if string=="l" or string=="L":
        return matrix, lista

    if string=="w" or string=="W":
        if (x) == (9) and y == 9:
            lista[0] = matrix[x-1][y]
            matrix[ 9 ][9] = " "
            matrix[x-1][y] = "P"
            return matrix, lista
        elif x == 0:
            print("\nVocê está na borda Norte\n")
            return matrix, lista
        else:
            matrix[x][y] = lista[0]
            lista[0] = matrix[x-1][y]
            matrix[x-1][y] = "P"
            if (x-1,y) == (0,0):
                victory()
                time.sleep(2)
                return exit()
            else:
                return matrix, lista
    
    elif string=="s" or string=="S":
        if x == 9:
            print("\nVocê está na borda Sul\n")
            return matrix,lista
        else:
            matrix[x][y] = lista[0]
            lista[0] = matrix[x+1][y]
            matrix[x+1][y] = "P"
            return matrix, lista
    
    elif string=="d" or string=="D":
        if y == 9:
            print("\nVocê está na borda Leste\n")
            return matrix,lista
        else:
            matrix[x][y] = lista[0]
            lista[0] = matrix[x][y+1]
            matrix[x][y+1] = "P"
            return matrix, lista
    
    elif string=="a" or string=="A":
        if (x) == (9) and (y) == (9):
            lista[0] = matrix[x][y-1]
            matrix[ 9 ][9] = " "
            matrix[x][y-1] = "P"
            return matrix, lista
        elif y == 0:
            print("\nVocê está na borda Oeste\n")
            return matrix,lista
        else:
            matrix[x][y] = lista[0]
            lista[0] = matrix[x][y-1]
            matrix[x][y-1] = "P"
            if (x,y-1) == (0,0):
                victory()
                time.sleep(2)
                return exit()
            else:
                return matrix, lista
    else:
        return matrix, lista
        

def life_implement(lista,string,life):

    if string == "l" or string == "L":
        life += 20
        if life > 100:
            life = 100
            return life
        else:
            return life
    
    if lista[0] == "^":
        life -= 15
        return life
    elif lista[0] == "#":
        life -= 25
        return life
    elif lista[0] == "@":
        life -= 40
        return life
    elif lista[0] == "*":
        life -= 60 
        return life
    else:
        return life
    
def victory():
    s1 = "*"*21
    s2 = "*    você_venceu    *"
    print(colors("branco","verde",s1))
    print(colors("branco","verde",s2))
    print(colors("branco","verde",s1))


def print_movement(matrix):
    for l in range(10):
        s = ''
        for c in range(10):
            cc = matrix[l][c]
            s += str(cc + "  ")
        S = colors("branco","magenta"," "+ s +" ")
        print(S)


def chamamento():
    
    a = board()
    status  = str(input("\nDigite seu nome: "))
    l       = [""]
    v       = 100
    potion  = 3

    s4 = str("\n%s; life - %d; pocões - %d.  " %(status, v, potion))
    print(colors("amarelo","preto",s4))
    print_movement(a)
    while True:
        s2  = str("\nMova-se: W, A, S, ou D  ou recupere vida:L ->>> ")
        s2c = colors("amarelo","preto",s2)
        m = str(input(s2c))
        print("\n")

        b,L     = movement(a,m,l)
        life    = life_implement(L,m,v)
        v       = life
        if m == "l" or m =="L":
            potion -= 1
        if potion   <= 0:
            potion = 0
        if life     <= 0:
            s3 = "\nvocê perdeu! :( :( :( \n"
            print(colors("branco","vermelho",s3))
            time.sleep(1)
            break
        if m == "exit" or m == "EXIT":
            print("você desistiu")
            break
        s5 = str("%s; life - %d; pocões - %d.  " %(status, life, potion))
        print(colors("amarelo","preto",s5))
        print_movement(b)
        a = b 
        l = L

chamamento()